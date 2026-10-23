"""hosting_rules and the smoke test's comparison helpers: a wrong rule match or edge-change strip
would let a broken deployment pass, or fail a healthy one."""
import importlib.util
import unittest
from pathlib import Path

from hosting_rules import declared, header_rules, parse_headers

ROOT = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location('smoke_test', ROOT / 'deploy' / 'smoke_test.py')
smoke = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(smoke)

SAMPLE = """/*
  X-Content-Type-Options: nosniff
  Cache-Control: public, max-age=0, must-revalidate
/assets/*
  Cache-Control: public, max-age=31536000, immutable
/404
  X-Robots-Tag: noindex, follow
"""


class HeaderRulesTest(unittest.TestCase):
    def test_parses_patterns_with_lowercase_names(self):
        rules = parse_headers(SAMPLE)
        self.assertEqual(list(rules), ['/*', '/assets/*', '/404'])
        self.assertEqual(rules['/404'], {'x-robots-tag': 'noindex, follow'})

    def test_later_matching_rules_override_earlier_ones(self):
        rules = parse_headers(SAMPLE)
        self.assertEqual(declared('/assets/site.js', rules)['cache-control'], 'public, max-age=31536000, immutable')
        self.assertEqual(declared('/', rules), {'x-content-type-options': 'nosniff', 'cache-control': 'public, max-age=0, must-revalidate'})

    def test_exact_patterns_match_only_their_path(self):
        rules = parse_headers(SAMPLE)
        self.assertIn('x-robots-tag', declared('/404', rules))
        self.assertNotIn('x-robots-tag', declared('/404.html', rules))

    def test_reads_the_published_file(self):
        rules = header_rules(ROOT / 'dist')
        self.assertIn('/*', rules)
        self.assertEqual(rules, smoke._header_rules(smoke.DIST))


class SmokeHelpersTest(unittest.TestCase):
    def test_location_is_a_path_whether_relative_or_absolute(self):
        base = 'https://solarityai.com'
        self.assertEqual(smoke.location(base, {'location': base + '/careers/'}), '/careers/')
        self.assertEqual(smoke.location(base, {'location': '/careers/'}), '/careers/')
        self.assertEqual(smoke.location(base, {}), '')

    def test_strips_only_the_known_edge_changes(self):
        page = (b'<!--email_off--><main>x</main><!--/email_off-->'
                b'<script defer src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon="{}"></script>\n</body>')
        self.assertEqual(smoke.without_email_markers(page), b'<main>x</main></body>')
        other = b'<script src="https://example.com/beacon.js"></script>'
        self.assertEqual(smoke.without_email_markers(other), other)

    def test_revalidation_directives(self):
        self.assertTrue(smoke.revalidates('public, max-age=0, must-revalidate'))
        self.assertTrue(smoke.revalidates('no-cache'))
        self.assertFalse(smoke.revalidates('public, max-age=31536000, immutable'))

    def test_equivalent_content_types_compare_equal(self):
        self.assertEqual(smoke.mime({'content-type': 'application/javascript; charset=utf-8'}), 'text/javascript')
        self.assertEqual(smoke.mime({'content-type': 'Image/Vnd.Microsoft.Icon'}), 'image/x-icon')


if __name__ == '__main__':
    unittest.main()
