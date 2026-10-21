"""Public URL contracts: remove redirects without losing inquiry context."""
import unittest
from site_urls import attributed, normalize_page_links, public_path


class PublicURLTests(unittest.TestCase):
    routes=('/', '/apps', '/apps/looks-max', '/contact', '/404')

    def normalize(self,markup):
        return normalize_page_links(markup,self.routes)

    def test_directory_and_standalone_routes(self):
        self.assertEqual(public_path('/apps/looks-max'),'/apps/looks-max/')
        self.assertEqual(public_path('/apps/'),'/apps/')
        self.assertEqual(public_path('/'),'/')
        self.assertEqual(public_path('/404'),'/404')

    def test_inquiry_query_and_fragment_are_preserved(self):
        markup='<a href="/contact?type=Strategic+partner&amp;product=Looks+Max#prepare-inquiry">Connect</a>'
        expected='<a href="/contact/?type=Strategic+partner&amp;product=Looks+Max#prepare-inquiry">Connect</a>'
        self.assertEqual(self.normalize(markup),expected)

    def test_encoded_unicode_and_special_query_characters_are_unchanged(self):
        markup='<a href="/contact?type=Other&amp;product=%F0%9F%8C%9E%26%3F%23%2F">Contact</a>'
        self.assertEqual(self.normalize(markup),markup.replace('/contact?','/contact/?'))

    def test_assets_external_protocol_and_unknown_paths_are_unchanged(self):
        markup=''.join(f'<a href="{url}">Link</a>' for url in ['/assets/screen.webp','https://example.com/apps','//example.com/apps','mailto:hello@example.com','/unknown','apps','#main'])
        self.assertEqual(self.normalize(markup),markup)

    def test_single_quoted_anchors_and_portfolio_fragments(self):
        self.assertEqual(self.normalize("<a href='/apps#looks-max'>Portfolio</a>"),"<a href='/apps/#looks-max'>Portfolio</a>")

    def test_non_anchor_attributes_and_text_are_not_rewritten(self):
        markup='<link href="/apps"><p data-href="/apps">/apps</p><a data-href="/apps" href="/apps">/apps</a>'
        self.assertEqual(self.normalize(markup),markup.replace(' href="/apps">/apps</a>',' href="/apps/">/apps</a>'))

    def test_normalization_is_idempotent(self):
        markup='<a href="/apps/">Apps</a><a href="/">Home</a><a href="/404">Error</a>'
        self.assertEqual(self.normalize(self.normalize(markup)),markup)




class AttributedLinkTests(unittest.TestCase):
    play='https://play.google.com/store/apps/details?id=com.solarityai.sleepmax'
    apple='https://apps.apple.com/us/app/sleep-max-rest-best/id6806709872'

    def test_google_play_and_web_apps_name_the_surface(self):
        self.assertEqual(attributed(self.play,'store-badge'),
                         self.play+'&utm_source=solarityai.com&utm_medium=website&utm_campaign=store-badge')
        self.assertEqual(attributed('https://engineeringmax.solarityai.com/','site-link'),
                         'https://engineeringmax.solarityai.com/?utm_source=solarityai.com&utm_medium=website&utm_campaign=site-link')

    def test_app_store_needs_the_provider_token(self):
        self.assertEqual(attributed(self.apple,'store-badge'),self.apple)
        self.assertEqual(attributed(self.apple,'store-badge','123456'),
                         self.apple+'?pt=123456&ct=solarityai-store-badge&mt=8')

    def test_other_hosts_are_untouched(self):
        for url in ('mailto:ata.turhan@solarityai.com','https://calendar.google.com/x','/apps/looks-max/','https://github.com/Solarity-AI',
                    'https://notplay.google.com/store','https://evilsolarityai.com/'):
            self.assertEqual(attributed(url,'footer'),url)


if __name__=='__main__':
    unittest.main()
