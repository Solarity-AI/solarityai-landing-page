"""HTTP checks for a deployed copy of dist/: routes, redirects, 404, headers, MIME.

Production image (nginx), for example in CI:

    docker build -t solarityai-site . && docker run -d -p 8080:80 solarityai-site
    python deploy/smoke_test.py http://localhost:8080

Cloudflare Pages (a *.pages.dev deployment or https://solarityai.com):

    python deploy/smoke_test.py https://<project>.pages.dev --platform pages

Expectations come from dist/ itself (sitemap routes, _headers and _redirects
rules, published assets), so the test follows the site without separate
maintenance. Only GET requests are sent.
"""
from __future__ import annotations

import argparse
import gzip
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / 'dist'
IMMUTABLE = 'public, max-age=31536000, immutable'
USER_AGENT = 'Mozilla/5.0 (compatible; SolaritySmokeTest/1.0)'
SECURITY = {
    'x-content-type-options': 'nosniff',
    'referrer-policy': 'strict-origin-when-cross-origin',
    'x-frame-options': 'SAMEORIGIN',
}
# Equivalent registrations of the same format differ between servers.
TYPE_ALIASES = {'application/javascript': 'text/javascript', 'text/xml': 'application/xml',
                'image/vnd.microsoft.icon': 'image/x-icon'}


class _NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


OPENER = build_opener(_NoRedirect)
failures: list[str] = []


def get(base: str, path: str, **headers) -> tuple[int, dict, bytes]:
    try:
        response = OPENER.open(Request(base + path, headers={'User-Agent': USER_AGENT, **headers}), timeout=20)
    except HTTPError as error:
        response = error
    return response.status, {k.lower(): v for k, v in response.headers.items()}, response.read()


def expect(condition: bool, message: str) -> None:
    if not condition:
        failures.append(message)


def mime(headers: dict) -> str:
    value = headers.get('content-type', '').split(';')[0].strip().lower()
    return TYPE_ALIASES.get(value, value)


def location(base: str, headers: dict) -> str:
    """Location as a path, whether the server sent it relative or absolute."""
    value = headers.get('location', '')
    return value[len(base):] if value.startswith(base) else value


def header_rules() -> dict[str, dict[str, str]]:
    rules, current = {}, None
    for line in (DIST / '_headers').read_text(encoding='utf-8').splitlines():
        if line and not line[0].isspace():
            current = line
            rules[current] = {}
        elif line.strip() and current:
            name, value = line.strip().split(':', 1)
            rules[current][name.lower()] = value.strip()
    return rules


def declared(path: str, rules: dict) -> dict[str, str]:
    expected = {}
    for pattern, headers in rules.items():
        if pattern == path or (pattern.endswith('*') and path.startswith(pattern[:-1])):
            expected.update(headers)
    return expected


def legacy_redirects() -> dict[str, str]:
    redirects = {'/index.html': '/'}
    for line in (DIST / '_redirects').read_text(encoding='utf-8').splitlines():
        old, new, _ = line.split()
        redirects[old] = new
    redirects['/careers.html?success=true'] = '/careers/'
    return redirects


def first(pattern: str) -> str:
    match = next(iter(sorted(DIST.glob(pattern))), None)
    if match is None:
        raise SystemExit(f'No published file matches {pattern}')
    return '/' + match.relative_to(DIST).as_posix()


def revalidates(cache: str) -> bool:
    return 'no-cache' in cache or 'max-age=0' in cache


def main(base: str, platform: str) -> int:
    base = base.rstrip('/')
    nginx = platform == 'nginx'
    # Pages normalizes slashes and /index.html itself, with 308.
    moved = {301} if nginx else {301, 308}
    rules = header_rules()
    namespace = '{http://www.sitemaps.org/schemas/sitemap/0.9}'
    routes = [urlsplit(node.text).path for node in ET.parse(DIST / 'sitemap.xml').iter(namespace + 'loc')]
    checked = 0

    for path in routes:
        status, headers, body = get(base, path)
        checked += 1
        expect(status == 200, f'{path}: status {status}')
        expect(mime(headers) == 'text/html', f'{path}: content-type {headers.get("content-type")}')
        cache = headers.get('cache-control', '')
        expect(cache == 'no-cache' if nginx else revalidates(cache), f'{path}: cache-control {cache!r}')
        for name, value in {**SECURITY, **declared(path, rules)}.items():
            expect(headers.get(name) == value, f'{path}: {name} is {headers.get(name)!r}, expected {value!r}')
        expect(body == (DIST / path.lstrip('/') / 'index.html').read_bytes(), f'{path}: served page differs from dist')
        if path != '/':
            status, headers, _ = get(base, path.rstrip('/'))
            checked += 1
            expect(status in moved and location(base, headers) == path,
                   f'{path.rstrip("/")}: expected redirect to {path}, got {status} {headers.get("location")}')

    for old, new in legacy_redirects().items():
        status, headers, _ = get(base, old)
        checked += 1
        expect(status in moved and location(base, headers).split('?')[0] == new,
               f'{old}: expected redirect to {new}, got {status} {headers.get("location")}')

    for path in ('/__missing-page', '/_headers', '/_redirects'):
        status, headers, body = get(base, path)
        checked += 1
        expect(status == 404, f'{path}: status {status}, expected 404')
        expect(b'is not here' in body and b'noindex' in body, f'{path}: custom noindex 404 page not served')
        expect(headers.get('x-content-type-options') == 'nosniff', f'{path}: missing nosniff on 404')
        if nginx:
            expect(headers.get('x-robots-tag') == 'noindex, follow', f'{path}: X-Robots-Tag {headers.get("x-robots-tag")!r}')

    status, headers, _ = get(base, '/404')
    checked += 1
    expect(status == (404 if nginx else status) and headers.get('x-robots-tag') == 'noindex, follow',
           f'/404: status {status}, X-Robots-Tag {headers.get("x-robots-tag")!r}')

    status, headers, body = get(base, '/', **{'Accept-Encoding': 'gzip'})
    checked += 1
    expect(headers.get('content-encoding') == 'gzip' and b'<html' in gzip.decompress(body), '/: response is not gzip-compressed')

    day = 'public, max-age=86400'
    assets = {
        first('assets/optimized/*.webp'): ('image/webp', IMMUTABLE),
        first('assets/optimized/*.avif'): ('image/avif', IMMUTABLE),
        first('assets/runtime/*.js'): ('text/javascript', IMMUTABLE),
        first('assets/fonts/*.woff2'): ('font/woff2', IMMUTABLE),
        '/assets/fonts/OFL-Manrope.txt': ('text/plain', day),
        first('assets/*-screen-*.webp'): ('image/webp', day),
        first('assets/*-social.jpg'): ('image/jpeg', day),
        '/favicon.ico': ('image/x-icon', 'public, max-age=604800'),
        '/robots.txt': ('text/plain', day),
        '/sitemap.xml': ('application/xml', day),
    }
    for path, (content_type, cache) in assets.items():
        status, headers, body = get(base, path)
        checked += 1
        actual = headers.get('cache-control', '')
        expect(status == 200, f'{path}: status {status}')
        expect(mime(headers) == content_type, f'{path}: content-type {headers.get("content-type")!r}, expected {content_type}')
        if nginx or cache == IMMUTABLE:
            expect(actual == cache, f'{path}: cache-control {actual!r}, expected {cache!r}')
        else:
            expect('immutable' not in actual, f'{path}: unfingerprinted file is cached as immutable')
        expect(body == (DIST / path.lstrip('/')).read_bytes(), f'{path}: served bytes differ from dist')
        for name, value in {**SECURITY, **declared(path, rules)}.items():
            expect(headers.get(name) == value, f'{path}: {name} is {headers.get(name)!r}, expected {value!r}')

    if nginx:
        status, _, body = get(base, '/health')
        checked += 1
        expect(status == 200 and body.strip() == b'healthy', '/health: not healthy')

    if failures:
        print(f'{len(failures)} problems in {checked} {platform} server checks:')
        print('\n'.join('  - ' + failure for failure in failures))
        return 1
    print(f'All {checked} {platform} server checks passed for {base}')
    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    parser.add_argument('base', nargs='?', default='http://localhost:8080')
    parser.add_argument('--platform', choices=('nginx', 'pages'), default='nginx')
    args = parser.parse_args()
    raise SystemExit(main(args.base, args.platform))
