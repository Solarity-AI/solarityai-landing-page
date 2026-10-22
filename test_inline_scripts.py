"""performance_build.inline_scripts: the parser behind the CSP hash list and the script checks.
A script must be found whatever its tag case or spacing, with its text byte-exact for hashing."""
import unittest

from performance_build import inline_scripts


class InlineScriptsTest(unittest.TestCase):
    def test_finds_scripts_regardless_of_tag_case_and_spacing(self):
        page = ('<p>x</p><SCRIPT>one()</SCRIPT><script type="module" >two()</script >'
                '<Script src="/a.js"></Script>')
        self.assertEqual(inline_scripts(page), [({}, 'one()'), ({'type': 'module'}, 'two()'), ({'src': '/a.js'}, '')])

    def test_keeps_script_text_byte_exact(self):
        body = 'if (a < b && c) { x = "&amp; </p>"; }'
        self.assertEqual(inline_scripts('<script>' + body + '</script>')[0][1], body)

    def test_reads_json_ld_and_speculation_rules_by_type(self):
        page = '<script type="application/ld+json">{"@type":"Thing"}</script><script type="speculationrules">{}</script>'
        self.assertEqual([attrs['type'] for attrs, _ in inline_scripts(page)], ['application/ld+json', 'speculationrules'])

    def test_text_that_looks_like_a_tag_is_not_a_script(self):
        self.assertEqual(inline_scripts('<p>&lt;script&gt;alert(1)&lt;/script&gt;</p>'), [])


if __name__ == '__main__':
    unittest.main()
