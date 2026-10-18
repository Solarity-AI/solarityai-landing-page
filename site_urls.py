"""Match the static host's final URLs without touching asset or external links."""
from html import escape, unescape
import re
from urllib.parse import urlsplit, urlunsplit


def public_path(route):
    """Content directories are served with a slash; 404 is a standalone file."""
    return route if route in ('/', '/404') else route.rstrip('/') + '/'


def normalize_page_links(document, routes):
    """Normalize only known, root-relative page anchors; retain inquiry context."""
    known = {route.rstrip('/') or '/' for route in routes}

    def anchor(match):
        tag = match.group()

        def href(attribute):
            value = unescape(attribute.group(2))
            parts = urlsplit(value)
            route = parts.path.rstrip('/') or '/'
            if (parts.scheme or parts.netloc or not parts.path.startswith('/')
                    or route not in known):
                return attribute.group()
            url = urlunsplit(('', '', public_path(route), parts.query, parts.fragment))
            return 'href=' + attribute.group(1) + escape(url, quote=True) + attribute.group(1)

        return re.sub(r'(?<=\s)href\s*=\s*([\"\x27])(.*?)\1', href, tag, flags=re.I)

    return re.sub(r'<a\b[^>]*>', anchor, document, flags=re.I)
