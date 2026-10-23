"""How Cloudflare Pages reads dist/_headers, shared by the static audit, the smoke test and the production audit."""
from __future__ import annotations

from pathlib import Path
from urllib.request import HTTPRedirectHandler

# Equivalent registrations of the same format differ between servers.
TYPE_ALIASES = {'application/javascript': 'text/javascript', 'text/xml': 'application/xml',
                'image/vnd.microsoft.icon': 'image/x-icon'}
# cf-cache-status values for a response served from Cloudflare's edge copy. Such a copy keeps the headers it was
# cached with until it expires, even after a deploy changes _headers.
EDGE_CACHED = {'HIT', 'REVALIDATED', 'STALE', 'UPDATING'}


class NoRedirect(HTTPRedirectHandler):
    """Report redirects instead of following them."""
    def redirect_request(self, *args, **kwargs):
        return None


def parse_headers(text: str) -> dict[str, dict[str, str]]:
    """Each rule's path pattern and its headers, with lowercase names."""
    rules, current = {}, None
    for line in text.splitlines():
        if line and not line[0].isspace():
            current = line
            rules[current] = {}
        elif line.strip() and current:
            name, value = line.strip().split(':', 1)
            rules[current][name.lower()] = value.strip()
    return rules


def header_rules(dist: Path) -> dict[str, dict[str, str]]:
    return parse_headers((dist / '_headers').read_text(encoding='utf-8'))


def declared(path: str, rules: dict) -> dict[str, str]:
    """The headers Pages sends for path: every matching rule, later rules overriding earlier ones."""
    expected = {}
    for pattern, headers in rules.items():
        if pattern == path or (pattern.endswith('*') and path.startswith(pattern[:-1])):
            expected.update(headers)
    return expected
