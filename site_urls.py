"""Match the static host's final URLs without touching asset or external links."""
from html import escape, unescape
import re
from urllib.parse import urlencode, urlsplit, urlunsplit


def public_path(route):
    """Content directories are served with a slash; 404 is a standalone file."""
    return route if route in ('/', '/404') else route.rstrip('/') + '/'


def attributed(url, campaign, apple_provider=''):
    """The store or web-app link a visible control uses, tagged with where on this site the visit came from.

    Google Play and the web apps take utm_source/utm_medium/utm_campaign (Play Console's tracked channels
    report installs per tag). The App Store only attributes a campaign link that carries the owner's
    App Store Connect provider token (pt) beside ct, so without one the link stays as listed.
    The tags name the site surface, never the visitor; schema.org keeps the untagged URLs."""
    parts = urlsplit(url)
    host = parts.netloc.lower()
    tags = []
    if host == 'apps.apple.com':
        if not apple_provider:
            return url
        tags = [('pt', apple_provider), ('ct', 'solarityai-' + campaign), ('mt', '8')]
    elif host == 'play.google.com' or host.endswith('.solarityai.com'):
        tags = [('utm_source', 'solarityai.com'), ('utm_medium', 'website'), ('utm_campaign', campaign)]
    if not tags:
        return url
    query = parts.query + ('&' if parts.query else '') + urlencode(tags)
    return urlunsplit((parts.scheme, parts.netloc, parts.path, query, parts.fragment))


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
