"""check_site.py rules, called one at a time now that the audit is split into named checks."""
import unittest

import check_site
from check_site import Document


def page(markup):
    d = Document()
    d.feed(markup)
    return d


class CheckSiteRulesTest(unittest.TestCase):
    def setUp(self):
        check_site.errors.clear()

    def test_spelled_numbers_read_visible_text_and_attributes_but_not_scripts(self):
        markup = '<p>Three apps</p><img alt="seven steps"><script>var four = 4</script><p>one of them</p>'
        self.assertEqual(check_site.spelled_numbers(markup), ['seven', 'three'])

    def test_page_text_rules(self):
        text = '<body><!--email_off--><p>A — B</p><!--/email_off--></body>'
        check_site.check_page_text('privacy/index.html', '/privacy', page(text), text)
        self.assertEqual(check_site.errors, ['privacy/index.html: long dash'])

    def test_founder_portrait_only_on_company_and_press(self):
        text = '<body><!--email_off--><img src="/assets/brand/ata-turhan-320.webp" alt=""><!--/email_off--></body>'
        for route, expected in (('/company', []), ('/careers', ['careers/index.html: founder portrait outside Company and the Press kit'])):
            check_site.errors.clear()
            check_site.check_page_text(route.strip('/') + '/index.html', route, page(text), text)
            self.assertEqual(check_site.errors, expected)

    def test_error_page_names_no_canonical_or_og_url(self):
        head = ('<title>Page not found | Solarity AI</title><meta name="description" content="x"><meta name="viewport" content="x">'
                '<meta property="og:title" content="x"><meta property="og:description" content="x"><meta property="og:image" content="x">'
                '<meta name="referrer" content="strict-origin-when-cross-origin"><h1>Gone</h1>')
        d = page(head)
        meta = {a.get('name') or a.get('property'): a.get('content', '') for t, a in d.tags if t == 'meta'}
        check_site.check_page_metadata('404.html', d, meta, '/404')
        self.assertEqual(check_site.errors, [])
        check_site.check_page_metadata('404.html', d, {**meta, 'og:url': 'https://solarityai.com/404'}, '/404')
        self.assertEqual(check_site.errors, ['404.html: Open Graph URL must match the final canonical URL'])

    def test_heading_levels_may_not_skip(self):
        d = page('<title>x</title><h1>a</h1><h2>b</h2><h4>c</h4>')
        check_site.check_page_metadata('x.html', d, {}, '/x')
        self.assertIn('x.html: heading level skips from H2 to H4', check_site.errors)

    def test_contrast_ratio(self):
        self.assertAlmostEqual(check_site.contrast((255, 255, 255), (0, 0, 0)), 21.0)
        self.assertAlmostEqual(check_site.contrast((118, 118, 118), (255, 255, 255)), 4.54, places=2)

    def test_unicode_ranges(self):
        self.assertEqual(check_site.unicode_ranges('U+0020-007E, U+00A0'), [(0x20, 0x7E), (0xA0, 0xA0)])

    def test_contact_topics_are_read_from_the_script(self):
        self.assertIn('Looks Max', check_site.contact_topics())

    def test_routes_of_published_files(self):
        self.assertEqual(check_site.route_of(check_site.DIST / 'index.html'), '/')
        self.assertEqual(check_site.route_of(check_site.DIST / '404.html'), '/404')
        self.assertEqual(check_site.route_of(check_site.DIST / 'apps' / 'iq-max' / 'index.html'), '/apps/iq-max')


if __name__ == '__main__':
    unittest.main()
