"""Tests for seo.py: stable page dates, a consistent schema.org graph, and the crawler files."""
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock
from urllib.robotparser import RobotFileParser

import seo

APP = dict(slug='sleep-max', name='Sleep Max', category='Sleep & daily routines', summary='A sleep diary.',
           intro='For people who want to pay closer attention to their sleep habits.',
           features=[('Reflect on your nights', 'Record sleep in a diary.')], note='General wellness only.',
           apple='https://apps.apple.com/us/app/sleep-max-rest-best/id6806709872',
           google='https://play.google.com/store/apps/details?id=com.solarityai.sleepmax')
WEB = dict(slug='engineering-max', name='Engineering Max', url='https://engineeringmax.solarityai.com/',
           category='App engineering', status='Web app · private testing', tagline='Find and fix.',
           summary='Checks a report.', facts=('155 rules',), availability='Free during private testing.')
PAGES = {'/': ('Solarity AI: home', 'Home description.', '<main>home</main>'),
         '/apps/sleep-max': ('Sleep Max: app', 'Sleep description.', '<main>sleep</main>'),
         '/platform': ('Web apps', 'Platform description.', '<main>platform</main>'),
         '/404': ('Page not found', 'Missing.', '<main>404</main>')}


def build_graph(path):
    title, desc, _ = PAGES[path]
    return seo.graph(path, title + ' | Solarity AI', desc, apps=[APP], saas=[WEB], faq=[('Q?', '<p>A.</p>')],
                     email='founder@example.com', logo='/logo.webp', portrait='/portrait.webp',
                     social_image='social/default.jpg', modified='2026-10-19')['@graph']


def defined_ids(value, found=None):
    found = set() if found is None else found
    if isinstance(value, dict):
        if '@type' in value and '@id' in value:
            found.add(value['@id'])
        for item in value.values():
            defined_ids(item, found)
    elif isinstance(value, list):
        for item in value:
            defined_ids(item, found)
    return found


class ScriptJsonTest(unittest.TestCase):
    def test_no_string_can_close_the_script_element(self):
        data = {'name': 'Ends </script><script>alert(1)</script>', 'text': 'iOS & Android'}
        out = seo.script_json(data)
        self.assertNotIn('<', out)
        self.assertNotIn('>', out)
        self.assertNotIn('&', out)
        self.assertEqual(json.loads(out), data)


class PageDatesTest(unittest.TestCase):
    def dates(self, pages, today):
        with mock.patch.object(seo, 'datetime') as clock:
            clock.date.today.return_value.isoformat.return_value = today
            return seo.page_dates(pages)

    def test_unchanged_content_keeps_its_date_on_a_later_day(self):
        with tempfile.TemporaryDirectory() as folder, mock.patch.object(seo, 'DATES_FILE', Path(folder) / 'dates.json'):
            first = self.dates(PAGES, '2026-10-19')
            stored = seo.DATES_FILE.read_bytes()
            self.assertEqual(self.dates(PAGES, '2026-12-01'), first)
            self.assertEqual(seo.DATES_FILE.read_bytes(), stored)

    def test_title_description_or_body_change_moves_only_that_page(self):
        with tempfile.TemporaryDirectory() as folder, mock.patch.object(seo, 'DATES_FILE', Path(folder) / 'dates.json'):
            self.dates(PAGES, '2026-10-19')
            for index in range(3):
                changed = dict(PAGES)
                parts = list(changed['/platform'])
                parts[index] += ' (edited)'
                changed['/platform'] = tuple(parts)
                dates = self.dates(changed, f'2026-11-0{index + 1}')
                self.assertEqual(dates['/platform'], f'2026-11-0{index + 1}')
                self.assertEqual(dates['/'], '2026-10-19')


class GraphTest(unittest.TestCase):
    def test_every_reference_points_to_a_defined_node(self):
        for path in PAGES:
            graph = build_graph(path)
            ids = defined_ids(graph)
            refs = {value for value in json.dumps(graph).split('"@id": "')[1:] for value in [value.split('"')[0]]}
            self.assertLessEqual(refs, ids, path)

    def test_page_node_uses_the_canonical_url(self):
        self.assertTrue(any(n.get('@id') == 'https://solarityai.com/404#webpage' for n in build_graph('/404')))
        self.assertTrue(any(n.get('@id') == 'https://solarityai.com/apps/sleep-max/#webpage' for n in build_graph('/apps/sleep-max')))

    def test_error_page_has_no_breadcrumb(self):
        self.assertNotIn('BreadcrumbList', {n['@type'] for n in build_graph('/404')})

    def test_states_no_ratings_offers_or_prices(self):
        for path in PAGES:
            text = json.dumps(build_graph(path))
            for banned in ('aggregateRating', 'review', 'offers', 'price'):
                self.assertNotIn(banned, text, path)

    def test_app_carries_store_identity(self):
        app = next(n for n in build_graph('/apps/sleep-max') if n['@type'] == 'MobileApplication')
        self.assertEqual(app['sameAs'], [APP['apple'], APP['google']])
        self.assertIn('Sleep Max - Rest Best', app['alternateName'])

    def test_apps_name_their_published_screenshots(self):
        def nodes(path):
            return seo.graph(path, 'Page | Solarity AI', 'Description.', apps=[{**APP, 'screen': 'sleep-max-screen-4.webp'}],
                             saas=[{**WEB, 'screens': [{'file': 'engineering-max-overview.webp'}]}], faq=[],
                             email='founder@example.com', logo='/logo.webp', portrait='/portrait.webp',
                             social_image='social/default.jpg', modified='2026-10-19')['@graph']
        app = next(n for n in nodes('/apps/sleep-max') if n['@type'] == 'MobileApplication')
        web = next(n for n in nodes('/platform') if n['@type'] == 'ItemList')['itemListElement'][0]['item']
        self.assertEqual(app['screenshot'], ['https://solarityai.com/assets/sleep-max-screen-4.webp'])
        self.assertEqual(web['screenshot'], ['https://solarityai.com/assets/engineering-max-overview.webp'])


TEAM = [dict(slug='hasan-ak', name='Hasan Ak', role='Staff engineer', linkedin='https://www.linkedin.com/in/example/',
             image='/hasan-480.webp'),
        dict(slug='batuhan-yuceturk', name='Batuhan Yücetürk', role='Marketing engineer', image='')]


class TeamTest(unittest.TestCase):
    def company_graph(self):
        return seo.graph('/company', 'Company | Solarity AI', 'About.', apps=[APP], saas=[WEB], faq=[],
                         email='founder@example.com', logo='/logo.webp', portrait='/portrait.webp',
                         social_image='social/default.jpg', modified='2026-10-21', team=TEAM)['@graph']

    def test_company_lists_each_member_with_only_their_published_facts(self):
        people = {n['name']: n for n in self.company_graph() if n['@type'] == 'Person'}
        self.assertEqual(people['Hasan Ak']['jobTitle'], 'Staff engineer')
        self.assertEqual(people['Hasan Ak']['sameAs'], ['https://www.linkedin.com/in/example/'])
        self.assertEqual(people['Hasan Ak']['image'], 'https://solarityai.com/hasan-480.webp')
        self.assertNotIn('sameAs', people['Batuhan Yücetürk'])
        self.assertNotIn('image', people['Batuhan Yücetürk'])

    def test_organization_names_founder_and_team_as_employees(self):
        graph = self.company_graph()
        employees = [ref['@id'] for ref in graph[0]['employee']]
        self.assertEqual(employees[0], seo.FOUNDER_ID)
        self.assertLessEqual(set(employees), defined_ids(graph))
        self.assertNotIn('employee', build_graph('/')[0])

    def test_llms_roster_carries_roles(self):
        self.assertEqual(seo.team_line(TEAM), 'Hasan Ak (staff engineer) and Batuhan Yücetürk (marketing engineer)')


class ProfilesTest(unittest.TestCase):
    def test_organization_lists_store_pages_then_every_company_channel(self):
        from company_facts import COMPANY_PROFILES
        self.assertEqual(seo.ORG_PROFILES[:2], [url for _, url in seo.STORE_PROFILES])
        self.assertEqual(seo.ORG_PROFILES[2:], [url for _, url in COMPANY_PROFILES])
        self.assertEqual(len(set(seo.ORG_PROFILES)), len(seo.ORG_PROFILES))
        self.assertNotIn('https://x.com/solarity_ai_company', seo.ORG_PROFILES)


class CrawlerFilesTest(unittest.TestCase):
    def test_robots_welcomes_search_and_ai_crawlers(self):
        robots = RobotFileParser()
        robots.parse(seo.robots_txt().splitlines())
        for agent in ['*', 'Googlebot', 'Bingbot', *seo.AI_CRAWLERS]:
            self.assertTrue(robots.can_fetch(agent, 'https://solarityai.com/apps/'), agent)
        self.assertEqual(robots.site_maps(), ['https://solarityai.com/sitemap.xml'])

    def test_sitemap_lists_content_pages_with_dates(self):
        xml = seo.sitemap_xml(PAGES, {p: '2026-10-19' for p in PAGES})
        self.assertIn('<loc>https://solarityai.com/apps/sleep-max/</loc><lastmod>2026-10-19</lastmod>', xml)
        self.assertNotIn('404', xml)

    def test_sitemap_lists_each_page_images(self):
        image = 'https://solarityai.com/assets/optimized/a&b.webp'
        xml = seo.sitemap_xml(PAGES, {p: '2026-10-19' for p in PAGES}, {'/platform': [image]})
        self.assertIn('xmlns:image="http://www.google.com/schemas/sitemap-image/1.1"', xml)
        self.assertIn('<lastmod>2026-10-19</lastmod><image:image><image:loc>https://solarityai.com/assets/optimized/a&amp;b.webp'
                      '</image:loc></image:image></url>', xml)
        self.assertEqual(xml.count('<image:image>'), 1)

    def test_llms_summary_and_full_file(self):
        pages = {**PAGES, '/apps': ('Apps', '', ''), '/company': ('Company', '', ''), '/investors-partners': ('I', '', ''),
                 '/careers': ('C', '', ''), '/contact': ('Contact', '', '')}
        short = seo.llms_txt(pages, apps=[APP], saas=[WEB], email='founder@example.com')
        full = seo.llms_txt(pages, apps=[APP], saas=[WEB], email='founder@example.com', full=True)
        self.assertTrue(short.startswith('# Solarity AI\n\n> '))
        self.assertIn('https://solarityai.com/llms-full.txt', short)
        self.assertIn('Context: General wellness only.', full)
        self.assertIn('155 rules', full)


if __name__ == '__main__':
    unittest.main()
