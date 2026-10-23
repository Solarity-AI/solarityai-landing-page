"""Read-only audit of the deployed Site: routing, 404, headers, caching, assets.

Only GET requests are sent to the public origin. Nothing is submitted, changed,
or deployed. Optionally runs Lighthouse (mobile and desktop) against every
sitemap route when a local Lighthouse CLI is supplied:

    python audit_production.py
    python audit_production.py --lighthouse path/to/lighthouse/cli/index.js

Results are written to research-assets/production-audit.json. Lighthouse lab
results depend on the machine and network that ran them; they are not Google
PageSpeed Insights field data.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlsplit
from urllib.request import Request, build_opener
import xml.etree.ElementTree as ET

from hosting_rules import EDGE_CACHED, TYPE_ALIASES, NoRedirect, declared as expected_headers, header_rules as _header_rules

ROOT = Path(__file__).parent
DIST = ROOT / 'dist'
ORIGIN = 'https://solarityai.com'
REPORT = ROOT / 'research-assets' / 'production-audit.json'
SEPARATION = ROOT / 'research-assets' / 'deploy-separation.json'
# A query unique to this run: a fixed one would itself be cached at the edge after the first run.
FRESH = time.time_ns()
USER_AGENT = 'Mozilla/5.0 (compatible; SolarityProductionAudit/1.0; read-only)'
EXPECTED_TYPES = {
    '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript',
    '.webp': 'image/webp', '.avif': 'image/avif', '.jpg': 'image/jpeg',
    '.png': 'image/png', '.svg': 'image/svg+xml', '.ico': 'image/x-icon',
    '.woff2': 'font/woff2', '.txt': 'text/plain', '.xml': 'application/xml',
}
_OPENER = build_opener(NoRedirect)


def fetch(url: str, body: bool = True) -> dict:
    """GET without following redirects; return status, headers, and optional text."""
    request = Request(url, headers={'User-Agent': USER_AGENT})
    try:
        response = _OPENER.open(request, timeout=30)
    except HTTPError as error:
        response = error
    except URLError as error:
        return {'url': url, 'error': str(error.reason)}
    data = response.read() if body else b''
    headers = {name.lower(): value for name, value in response.headers.items()}
    headers.pop('set-cookie', None)
    return {
        'url': url,
        'status': response.status if hasattr(response, 'status') else response.code,
        'headers': headers,
        'bytes': len(data),
        'text': data.decode('utf-8', 'replace') if body else '',
    }


class _Head(HTMLParser):
    def __init__(self):
        super().__init__()
        self.canonical = None
        self.robots = None
        self.title = ''
        self.h1 = ''
        self._in = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'link' and a.get('rel') == 'canonical':
            self.canonical = a.get('href')
        if tag == 'meta' and a.get('name') == 'robots':
            self.robots = a.get('content')
        if tag in ('title', 'h1'):
            self._in = tag

    def handle_endtag(self, tag):
        if tag == self._in:
            self._in = None

    def handle_data(self, data):
        if self._in == 'title':
            self.title += data
        elif self._in == 'h1':
            self.h1 += data


def head_of(text: str) -> _Head:
    parser = _Head()
    parser.feed(text)
    return parser


def compare_headers(path: str, actual: dict, rules: dict) -> list[str]:
    missing = []
    for name, value in expected_headers(path, rules).items():
        if actual.get(name, '').lower() != value.lower():
            missing.append(f'{name}: expected "{value}", got "{actual.get(name, "")}"')
    return missing


def content_type_ok(path: str, actual: str) -> bool:
    expected = EXPECTED_TYPES.get(Path(urlsplit(path).path).suffix.lower())
    mime = TYPE_ALIASES.get(actual.split(';')[0].strip().lower(), actual.split(';')[0].strip().lower())
    return expected is None or mime == expected


def asset_urls(text: str, origin: str) -> set[str]:
    pattern = r'(?:' + re.escape(origin) + r'|(?<![\w.-]))(/assets/[^"\'\s,)*]+)(?![\w*])'
    return {match.split('#')[0] for match in re.findall(pattern, text)}


def run_lighthouse(cli: str, urls: list[str]) -> dict:
    results = {}
    with tempfile.TemporaryDirectory() as folder:
        for url in urls:
            for form_factor in ('mobile', 'desktop'):
                output = Path(folder) / 'report.json'
                command = ['node', cli, url, '--quiet', '--output=json', f'--output-path={output}',
                           '--only-categories=performance,accessibility,best-practices,seo',
                           '--chrome-flags=--headless=new --no-first-run']
                if form_factor == 'desktop':
                    command.append('--preset=desktop')
                completed = subprocess.run(command, capture_output=True, text=True, encoding='utf-8')
                if completed.returncode or not output.exists():
                    results.setdefault(url, {})[form_factor] = {'error': completed.stderr.strip()[-500:]}
                    continue
                lhr = json.loads(output.read_text(encoding='utf-8'))
                audits = lhr['audits']
                results.setdefault(url, {})[form_factor] = {
                    'lighthouse_version': lhr['lighthouseVersion'],
                    'scores': {key: round(category['score'] * 100) if category['score'] is not None else None
                               for key, category in lhr['categories'].items()},
                    'metrics': {name: audits[name].get('displayValue') for name in (
                        'first-contentful-paint', 'largest-contentful-paint', 'total-blocking-time',
                        'cumulative-layout-shift', 'speed-index')},
                    'failed_audits': sorted(
                        key for key, audit in audits.items()
                        if audit.get('score') is not None and audit.get('score') < 0.9
                        and audit.get('scoreDisplayMode') in ('binary', 'numeric', 'metricSavings')),
                    'run_warnings': lhr.get('runWarnings', []),
                }
                print(f'  lighthouse {form_factor:7} {url}: {results[url][form_factor]["scores"]}')
    return results


def audit_pages(routes: list[str], origin: str, rules: dict, findings: list[str]) -> tuple[dict, set[str]]:
    """Each sitemap route: status, type, caching, canonical, robots and headers. Also returns the assets they reference."""
    pages, assets = {}, set()
    for url in routes:
        result = fetch(url)
        head = head_of(result.get('text', ''))
        path = urlsplit(url).path
        missing = compare_headers(path, result.get('headers', {}), rules)
        pages[path] = {
            'status': result.get('status'),
            'content_type': result.get('headers', {}).get('content-type'),
            'cache_control': result.get('headers', {}).get('cache-control'),
            'bytes': result.get('bytes'),
            'canonical_ok': head.canonical == ORIGIN + path,
            'robots': head.robots,
            'missing_expected_headers': missing,
        }
        if result.get('status') != 200:
            findings.append(f'{path}: status {result.get("status")}')
        # Pages always name the production origin as canonical, also on a preview.
        if head.canonical != ORIGIN + path:
            findings.append(f'{path}: canonical {head.canonical!r} does not match {ORIGIN + path}')
        assets |= asset_urls(result.get('text', ''), origin)
    return pages, assets


def audit_trailing_slash_redirects(routes: list[str], origin: str, findings: list[str]) -> dict:
    redirects = {}
    for url in routes:
        path = urlsplit(url).path
        if path != '/':
            result = fetch(origin + path.rstrip('/'), body=False)
            target = urljoin(origin + path, result.get('headers', {}).get('location', ''))
            redirects[path.rstrip('/')] = {'status': result.get('status'), 'location': target}
            if result.get('status') not in (301, 302, 307, 308) or target != url:
                findings.append(f'{path.rstrip("/")}: does not redirect to {url}')
    return redirects


def audit_not_found(origin: str, rules: dict, findings: list[str]) -> dict:
    missing_page = fetch(origin + '/__solarity-audit-missing-page')
    missing_head = head_of(missing_page.get('text', ''))
    not_found = {
        'status': missing_page.get('status'),
        'custom_page': 'is not here' in missing_head.h1,
        'meta_robots': missing_head.robots,
        'x_robots_tag': missing_page.get('headers', {}).get('x-robots-tag'),
        'missing_expected_headers': compare_headers('/404', missing_page.get('headers', {}), rules),
    }
    error_page = fetch(origin + '/404')
    not_found['direct_404_status'] = error_page.get('status')
    not_found['direct_404_missing_expected_headers'] = compare_headers('/404', error_page.get('headers', {}), rules)
    if not_found['status'] != 404:
        findings.append(f'Missing pages return status {not_found["status"]}, not 404')
    if not not_found['custom_page']:
        findings.append('Missing pages do not render the custom 404 document')
    if 'noindex' not in (not_found['meta_robots'] or '') and 'noindex' not in (not_found['x_robots_tag'] or ''):
        findings.append('404 responses are indexable')
    return not_found


def audit_assets(assets: set[str], origin: str, rules: dict, findings: list[str]) -> dict:
    asset_results = {}
    for path in sorted(assets):
        result = fetch(origin + path, body=False)
        headers = result.get('headers', {})
        missing = compare_headers(path, headers, rules)
        record = {
            'status': result.get('status'),
            'content_type': headers.get('content-type'),
            'cache_control': headers.get('cache-control'),
        }
        if missing and headers.get('cf-cache-status') in EDGE_CACHED:
            # An unchanged file keeps the headers Cloudflare cached with it, even after a deploy changes _headers
            # (for example a new inline-script hash in the CSP). Judge what the deployment serves, and record the lag.
            fresh = fetch(f'{origin}{path}?audit-fresh={FRESH}', body=False)
            record['edge_copy_missing_headers'] = missing
            missing = compare_headers(path, fresh.get('headers', {}), rules)
        record['missing_expected_headers'] = missing
        record['content_type_ok'] = content_type_ok(path, headers.get('content-type', ''))
        asset_results[path] = record
        if result.get('status') != 200:
            findings.append(f'{path}: status {result.get("status")}')
    wrong_types = sorted(path for path, item in asset_results.items() if not item['content_type_ok'])
    if wrong_types:
        findings.append(f'{len(wrong_types)} referenced assets have an unexpected Content-Type, e.g. '
                        f'{wrong_types[0]} -> {asset_results[wrong_types[0]]["content_type"]}')
    return asset_results


def audit_favicon(origin: str, findings: list[str]) -> dict:
    favicon = fetch(origin + '/favicon.ico', body=False)
    if favicon.get('status') != 200:
        findings.append(f'/favicon.ico: status {favicon.get("status")}')
    return {'status': favicon.get('status'), 'content_type': favicon.get('headers', {}).get('content-type')}


def audit_unpublished_files(origin: str, findings: list[str]) -> dict:
    """Files that local builds no longer publish but an older deployment may still expose."""
    exposed = {}
    probe = ['/_headers']
    if SEPARATION.exists():
        separation = json.loads(SEPARATION.read_text(encoding='utf-8'))
        probe += [item['published_path'] for item in separation['moved'] + separation['removed_generated']]
    for path in probe:
        if (DIST / path.lstrip('/')).is_file():
            continue
        result = fetch(origin + path, body=False)
        if result.get('status') == 200:
            exposed[path] = result.get('headers', {}).get('content-type')
    if exposed:
        findings.append(f'{len(exposed)} files outside the current publish set are publicly reachable')
    return exposed


def add_lighthouse(report: dict, cli: str | None, routes: list[str], origin: str) -> None:
    """Run Lighthouse when a CLI is given; otherwise carry over earlier results for the same origin."""
    if cli:
        report['lighthouse'] = run_lighthouse(cli, routes)
    elif REPORT.exists():
        previous = json.loads(REPORT.read_text(encoding='utf-8'))
        # Lab results describe one host; never attribute them to another origin.
        if 'lighthouse' in previous and previous.get('origin') == origin:
            report['lighthouse'] = previous['lighthouse']
            report['lighthouse_measured_at'] = previous.get('lighthouse_measured_at', previous['measured_at'])
            report['lighthouse_note'] = 'Carried over from measured_at ' + report['lighthouse_measured_at']
    if cli:
        report['lighthouse_measured_at'] = report['measured_at']


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    parser.add_argument('--origin', default=ORIGIN)
    parser.add_argument('--lighthouse', help='Path to a local Lighthouse CLI index.js')
    args = parser.parse_args()
    origin = args.origin.rstrip('/')
    rules = _header_rules(DIST)
    findings: list[str] = []
    report = {
        'measured_at': datetime.now(timezone.utc).isoformat(timespec='seconds'),
        'origin': origin,
        'scope': 'Read-only GET requests against the public origin. Lab Lighthouse runs, when present, '
                 'come from the auditing machine, not Google PageSpeed Insights field data.',
    }

    sitemap = fetch(origin + '/sitemap.xml')
    namespace = '{http://www.sitemaps.org/schemas/sitemap/0.9}'
    if sitemap.get('status') != 200 or 'text' not in sitemap:
        print(f'{origin}/sitemap.xml: status {sitemap.get("status")}; nothing to audit', file=sys.stderr)
        return 1
    # The sitemap names the canonical origin; audit the same paths on the origin requested.
    routes = [origin + urlsplit(node.text).path for node in ET.fromstring(sitemap['text']).iter(namespace + 'loc')]
    pages, assets = audit_pages(routes, origin, rules, findings)
    report['pages'] = pages
    report['trailing_slash_redirects'] = audit_trailing_slash_redirects(routes, origin, findings)
    report['not_found'] = audit_not_found(origin, rules, findings)
    asset_results = audit_assets(assets, origin, rules, findings)
    report['assets'] = asset_results
    report['favicon_ico'] = audit_favicon(origin, findings)
    report['publicly_reachable_unpublished_files'] = audit_unpublished_files(origin, findings)
    unapplied = sorted({item.split(':')[0] for record in [*pages.values(), *asset_results.values()]
                        for item in record['missing_expected_headers']})
    if unapplied:
        findings.append('Host does not apply _headers rules for: ' + ', '.join(unapplied))
    add_lighthouse(report, args.lighthouse, routes, origin)

    report['findings'] = findings
    REPORT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n', encoding='utf-8', newline='\n')
    sys.stdout.reconfigure(encoding='utf-8')
    print(json.dumps({'origin': origin, 'pages': len(pages), 'assets': len(asset_results), 'findings': findings}, indent=2, ensure_ascii=False))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
