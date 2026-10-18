"""HTTP checks for the production image: routes, redirects, 404, headers, MIME.

Run against a container built from the Dockerfile, for example:

    docker build -t solarityai-site . && docker run -d -p 8080:80 solarityai-site
    python deploy/smoke_test.py http://localhost:8080

Expectations come from dist/ itself (sitemap routes, _headers rules, assets),
so the test follows the site without separate maintenance.
"""
from __future__ import annotations

import gzip
from pathlib import Path
import sys
from urllib.error import HTTPError
from urllib.parse import urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / 'dist'
IMMUTABLE = 'public, max-age=31536000, immutable'
SECURITY = {
    'x-content-type-options': 'nosniff',
    'referrer-policy': 'strict-origin-when-cross-origin',
    'x-frame-options': 'SAMEORIGIN',
}
LEGACY_REDIRECTS = {
    '/index.html': '/',
    '/careers.html': '/careers/',
    '/careers.html?success=true': '/careers/',
    '/blog.html': '/',
    '/legal.html': '/contact/',
    '/docs/xtract-demo.html': '/',
}


class _NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


OPENER = build_opener(_NoRedirect)
failures: list[str] = []


def get(base: str, path: str, **headers) -> tuple[int, dict, bytes]:
    try:
        response = OPENER.open(Request(base + path, headers=headers), timeout=15)
    except HTTPError as error:
        response = error
    return response.status, {k.lower(): v for k, v in response.headers.items()}, response.read()


def expect(condition: bool, message: str) -> None:
    if not condition:
        failures.append(message)


def mime(headers: dict) -> str:
    return headers.get('content-type', '').split(';')[0].strip()


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


def first(pattern: str) -> str:
    match = next(iter(sorted(DIST.glob(pattern))), None)
    if match is None:
        raise SystemExit(f'No published file matches {pattern}')
    return '/' + match.relative_to(DIST).as_posix()


def main(base: str) -> int:
    base = base.rstrip('/')
    rules = header_rules()
    namespace = '{http://www.sitemaps.org/schemas/sitemap/0.9}'
    routes = [urlsplit(node.text).path for node in ET.parse(DIST / 'sitemap.xml').iter(namespace + 'loc')]

    for path in routes:
        status, headers, body = get(base, path)
        expect(status == 200, f'{path}: status {status}')
        expect(mime(headers) == 'text/html', f'{path}: content-type {headers.get("content-type")}')
        expect(headers.get('cache-control') == 'no-cache', f'{path}: cache-control {headers.get("cache-control")}')
        for name, value in {**SECURITY, **declared(path, rules)}.items():
            expect(headers.get(name) == value, f'{path}: {name} is {headers.get(name)!r}, expected {value!r}')
        expect(b'<html' in body, f'{path}: body is not an HTML document')
        if path != '/':
            status, headers, _ = get(base, path.rstrip('/'))
            expect(status == 301 and headers.get('location') == path,
                   f'{path.rstrip("/")}: expected 301 to {path}, got {status} {headers.get("location")}')

    for old, new in LEGACY_REDIRECTS.items():
        status, headers, _ = get(base, old)
        expect(status == 301 and headers.get('location') == new,
               f'{old}: expected 301 to {new}, got {status} {headers.get("location")}')

    for path in ('/__missing-page', '/404', '/_headers'):
        status, headers, body = get(base, path)
        expect(status == 404, f'{path}: status {status}, expected 404')
        expect(b'is not here' in body, f'{path}: custom 404 page not served')
        expect(headers.get('x-robots-tag') == 'noindex, follow', f'{path}: X-Robots-Tag {headers.get("x-robots-tag")!r}')
        expect(headers.get('x-content-type-options') == 'nosniff', f'{path}: missing nosniff on 404')

    status, headers, body = get(base, '/', **{'Accept-Encoding': 'gzip'})
    expect(headers.get('content-encoding') == 'gzip' and b'<html' in gzip.decompress(body), '/: response is not gzip-compressed')

    assets = {
        first('assets/optimized/*.webp'): ('image/webp', IMMUTABLE),
        first('assets/optimized/*.avif'): ('image/avif', IMMUTABLE),
        first('assets/runtime/*.js'): ('application/javascript', IMMUTABLE),
        first('assets/fonts/*.woff2'): ('font/woff2', IMMUTABLE),
        '/assets/fonts/OFL-Manrope.txt': ('text/plain', 'public, max-age=86400'),
        first('assets/*-screen-*.webp'): ('image/webp', 'public, max-age=86400'),
        first('assets/*-social.jpg'): ('image/jpeg', 'public, max-age=86400'),
        '/favicon.ico': ('image/x-icon', 'public, max-age=604800'),
        '/robots.txt': ('text/plain', 'public, max-age=86400'),
        '/sitemap.xml': ('text/xml', 'public, max-age=86400'),
    }
    for path, (content_type, cache) in assets.items():
        status, headers, body = get(base, path)
        expect(status == 200, f'{path}: status {status}')
        expect(mime(headers) == content_type, f'{path}: content-type {headers.get("content-type")!r}, expected {content_type}')
        expect(headers.get('cache-control') == cache, f'{path}: cache-control {headers.get("cache-control")!r}, expected {cache!r}')
        expect(body == (DIST / path.lstrip('/')).read_bytes(), f'{path}: served bytes differ from dist')
        for name, value in {**SECURITY, **declared(path, rules)}.items():
            expect(headers.get(name) == value, f'{path}: {name} is {headers.get(name)!r}, expected {value!r}')

    status, _, body = get(base, '/health')
    expect(status == 200 and body.strip() == b'healthy', '/health: not healthy')

    checked = len(routes) * 2 + len(LEGACY_REDIRECTS) + 3 + 1 + len(assets) + 1
    if failures:
        print(f'{len(failures)} of {checked} server checks failed:')
        print('\n'.join('  - ' + failure for failure in failures))
        return 1
    print(f'All {checked} server checks passed for {base}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1] if len(sys.argv) > 1 else 'http://localhost:8080'))
