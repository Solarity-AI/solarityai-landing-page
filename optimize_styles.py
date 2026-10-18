"""Conservative, dependency-free CSS filtering for this static site.

Only selector branches requiring a class absent from the supplied document are
removed. Functional pseudo-classes, escapes, and unknown at-rules are retained.
Declaration order, values, and cascade order are never rewritten. This is a
build-time byte reduction, not a substitute for a rendered visual audit.
"""
from html.parser import HTMLParser
import re


DYNAMIC_CLASSES = frozenset({
    'nav-enhanced', 'is-open', 'nav-open', 'image-preview-open',
})
_IDENTIFIER = re.compile(r'-?[_a-zA-Z][_a-zA-Z0-9-]*')
_CONDITIONAL_RULES = frozenset({'media', 'supports', 'container', 'layer'})


class _ClassCollector(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.classes = set()

    def handle_starttag(self, tag, attrs):
        self.classes.update(dict(attrs).get('class', '').split())


def _opaque_end(text, index):
    """Return the end of a CSS string/comment, or None for an ordinary char."""
    if text.startswith('/*', index):
        end = text.find('*/', index + 2)
        if end < 0:
            raise ValueError('Unterminated CSS comment')
        return end + 2
    if text[index] in "\"'":
        quote, end = text[index], index + 1
        while end < len(text):
            if text[end] == '\\':
                end += 2
            elif text[end] == quote:
                return end + 1
            else:
                end += 1
        raise ValueError('Unterminated CSS string')
    return None


def _find_separator(text, start, separators):
    """Find a top-level delimiter without mistaking function/string contents."""
    parens = brackets = 0
    i = start
    while i < len(text):
        opaque = _opaque_end(text, i)
        if opaque is not None:
            i = opaque
            continue
        char = text[i]
        if char == '\\':
            i += 2
            continue
        if char == '(':
            parens += 1
        elif char == ')':
            parens -= 1
        elif char == '[':
            brackets += 1
        elif char == ']':
            brackets -= 1
        elif not parens and not brackets and char in separators:
            return i
        if parens < 0 or brackets < 0:
            raise ValueError('Unbalanced CSS prelude')
        i += 1
    if parens or brackets:
        raise ValueError('Unbalanced CSS prelude')
    return len(text)


def _block_end(text, opening):
    depth, i = 1, opening + 1
    while i < len(text):
        opaque = _opaque_end(text, i)
        if opaque is not None:
            i = opaque
            continue
        if text[i] == '\\':
            i += 2
            continue
        if text[i] == '{':
            depth += 1
        elif text[i] == '}':
            depth -= 1
            if depth == 0:
                return i
        i += 1
    raise ValueError('Unterminated CSS block')


def _selector_branches(selector):
    start = 0
    while start < len(selector):
        end = _find_separator(selector, start, ',')
        yield selector[start:end].strip()
        start = end + 1


def _required_classes(selector):
    """Return required classes, or None if a branch is intentionally opaque."""
    # :not(.absent) can match everything. :is/.where/:has and escaped names also
    # need a full selector parser. Keep their complete branch conservatively.
    if '\\' in selector or re.search(r':[\w-]+\s*\(', selector):
        return None
    classes, bracket_depth, i = set(), 0, 0
    while i < len(selector):
        opaque = _opaque_end(selector, i)
        if opaque is not None:
            i = opaque
            continue
        char = selector[i]
        if char == '[':
            bracket_depth += 1
        elif char == ']':
            bracket_depth -= 1
        elif char == '.' and not bracket_depth:
            match = _IDENTIFIER.match(selector, i + 1)
            if match is None:
                return None
            classes.add(match.group())
            i = match.end()
            continue
        i += 1
    return classes


def _filter_rules(css, classes, stats):
    output, start = [], 0
    while start < len(css):
        while start < len(css):
            if css[start].isspace():
                start += 1
            elif css.startswith('/*', start):
                start = _opaque_end(css, start)
            else:
                break
        if start == len(css):
            break
        end = _find_separator(css, start, '{;')
        if end == len(css):
            if css[start:].strip():
                raise ValueError('CSS rule has no block or terminator')
            break
        if css[end] == ';':
            output.append(css[start:end + 1])
            start = end + 1
            continue
        close = _block_end(css, end)
        prelude, body = css[start:end].strip(), css[end + 1:close]
        if prelude.startswith('@'):
            match = re.match(r'@([\w-]+)', prelude)
            name = match.group(1).lower() if match else ''
            if name in _CONDITIONAL_RULES:
                filtered = _filter_rules(body, classes, stats)
                # Even an empty named layer establishes cascade order.
                if filtered or name == 'layer':
                    output.append(_compact(prelude) + '{' + filtered + '}')
            else:
                # Keyframes, font-face and any future syntax remain untouched.
                output.append(css[start:close + 1])
        else:
            branches = list(_selector_branches(prelude))
            keep = []
            for branch in branches:
                stats['selector_branches_examined'] += 1
                required = _required_classes(branch)
                if required is None or required <= classes:
                    keep.append(branch)
                else:
                    stats['selector_branches_removed'] += 1
            if keep:
                output.append(_compact(','.join(keep) + '{' + body + '}'))
        start = close + 1
    return ''.join(output)


def _compact(css):
    """Remove formatting only; preserve strings and all operator whitespace."""
    out, pending_space, i = [], False, 0
    while i < len(css):
        char = css[i]
        if char.isspace():
            pending_space = True
            i += 1
            continue
        opaque = _opaque_end(css, i)
        if opaque is not None and css.startswith('/*', i):
            # Preserve a minimal separator where removing a comment could join
            # tokens or change a compound selector into a descendant selector.
            before = css[i - 1] if i else ''
            after = css[opaque] if opaque < len(css) else ''
            if before and after and not before.isspace() and not after.isspace():
                if pending_space and out and out[-1][-1] not in '{;':
                    out.append(' ')
                out.append('/**/')
                pending_space = False
            i = opaque
            continue
        if pending_space and out and out[-1][-1] not in '{;}' and char not in '{};':
            out.append(' ')
        pending_space = False
        if opaque is not None:
            out.append(css[i:opaque])
            i = opaque
        elif char == '\\' and i + 1 < len(css):
            out.append(css[i:i + 2])
            i += 2
        else:
            out.append(char)
            i += 1
    return ''.join(out).strip()


def optimize_css(css, html, dynamic_classes=()):
    """Return (css_text, metrics) for one generated HTML route.

    The caller owns cache naming, delivery and the complete source bundle.
    Explicit classes discovered in future JavaScript must be passed here.
    """
    collector = _ClassCollector()
    collector.feed(html)
    classes = collector.classes | DYNAMIC_CLASSES | set(dynamic_classes)
    metrics = {'source_bytes': len(css.encode()), 'html_classes': len(collector.classes),
               'selector_branches_examined': 0, 'selector_branches_removed': 0}
    compact = _filter_rules(css, classes, metrics)
    metrics['output_bytes'] = len(compact.encode())
    metrics['bytes_removed'] = metrics['source_bytes'] - metrics['output_bytes']
    return compact, metrics
