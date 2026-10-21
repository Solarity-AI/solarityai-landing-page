"""The escaping contract in templating.py: plain values escape exactly as html.escape(quote=True) does,
Markup passes through, and a missing variable fails the build instead of rendering empty."""
import unittest
from html import escape

from jinja2 import UndefinedError
from markupsafe import Markup

from templating import ENV


class EscapingContractTest(unittest.TestCase):
    def render(self, source, **context):
        return ENV.from_string(source).render(**context)

    def test_plain_values_match_html_escape(self):
        tricky = 'Ali & "Ece" <b>bold</b> it\'s Çağrı'
        self.assertEqual(self.render('{{ v }}', v=tricky), escape(tricky, quote=True))
        self.assertEqual(self.render('<a title="{{ v }}">', v=tricky), '<a title="' + escape(tricky, quote=True) + '">')

    def test_quotes_use_html_escape_entities(self):
        out = self.render('{{ v }}', v='"\'')
        self.assertEqual(out, '&quot;&#x27;')

    def test_markup_and_safe_pass_through(self):
        self.assertEqual(self.render('{{ v }}', v=Markup('<em>x</em>')), '<em>x</em>')
        self.assertEqual(self.render('{{ v|safe }}', v='<em>x</em>'), '<em>x</em>')

    def test_numbers_render_as_text(self):
        self.assertEqual(self.render('{{ v }}', v=42), '42')

    def test_missing_variable_fails(self):
        with self.assertRaises(UndefinedError):
            self.render('{{ missing }}')


if __name__ == '__main__':
    unittest.main()
