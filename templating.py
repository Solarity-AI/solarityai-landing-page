"""Jinja rendering for the page markup in templates/.

Templates escape every value by default, exactly as html.escape(value, quote=True) does, so the
generated HTML is byte-for-byte what the earlier f-string markup produced. HTML built elsewhere
(another template, a component) is Markup and passes through unchanged; a template marks any other
deliberately raw value with |safe.
"""
from html import escape
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined
from markupsafe import Markup

TEMPLATES = Path(__file__).resolve().parent / 'templates'


def _finalize(value):
    """Escape plain values the html.escape way (&quot; and &#x27;), not MarkupSafe's (&#34; and &#39;)."""
    if isinstance(value, Markup) or value is None:
        return value
    return Markup(escape(str(value), quote=True))


ENV = Environment(
    loader=FileSystemLoader(TEMPLATES, encoding='utf-8'),
    autoescape=True,
    finalize=_finalize,
    undefined=StrictUndefined,
    keep_trailing_newline=False,
    auto_reload=False,
)


def render(template, /, **context):
    """Render templates/<template> and return Markup, so the result can be placed in other templates.
    template is positional-only, so any keyword (including name) is free for template variables."""
    return Markup(ENV.get_template(template).render(**context))
