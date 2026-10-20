"""Tests for visual_record.py: the shipping record, and the company facts that stay hidden until supplied."""
import unittest
from unittest import mock

import company_facts
import visual_record

APPS = [dict(slug=s, name=n, category='Category', color='amber', apple=f'https://apps.apple.com/us/app/{s}/id1')
        for s, n in (('looks-max', 'Looks Max'), ('fitness-max', 'Fitness Max'), ('iq-max', 'IQ Max'), ('sleep-max', 'Sleep Max'))]


class ShippingRecordTest(unittest.TestCase):
    def test_counts_launches_and_weeks_from_the_dates(self):
        html = visual_record.shipping_record(APPS)
        self.assertIn('Four apps in twelve weeks.', html)
        self.assertIn('June 23, 2026', html)
        self.assertIn('September 16, 2026', html)
        self.assertEqual(html.count('class="record-step"'), 4)
        self.assertIn('datetime="2026-08-15"', html)

    def test_every_launch_links_to_its_public_listing(self):
        html = visual_record.shipping_record(APPS)
        for app in APPS:
            self.assertIn(f'href="{app["apple"]}" target="_blank" rel="noopener noreferrer"', html)

    def test_releases_name_known_apps_in_date_order(self):
        dates = [d for _, d in company_facts.APP_STORE_RELEASES]
        self.assertEqual(dates, sorted(dates))
        self.assertLessEqual({s for s, _ in company_facts.APP_STORE_RELEASES}, {a['slug'] for a in APPS})

    def test_web_milestones_appear_only_when_complete(self):
        self.assertNotIn('record-track--web', visual_record.shipping_record(APPS))
        milestones = [{'slug': 'engineering-max', 'date': '2026-10-01', 'label': 'Private testing opened'},
                      {'slug': 'management-max', 'date': '', 'label': 'Missing date'}]
        with mock.patch.object(visual_record, 'WEB_APP_MILESTONES', milestones):
            html = visual_record.shipping_record(APPS)
        self.assertIn('Private testing opened', html)
        self.assertNotIn('Missing date', html)


class RecordHelpersTest(unittest.TestCase):
    def test_summary_matches_the_release_dates(self):
        summary = visual_record.record_summary()
        self.assertEqual((summary['count'], summary['weeks'], summary['first']), (4, 12, 'June 23, 2026'))
        self.assertEqual((summary['count_word'], summary['weeks_word']), ('four', 'twelve'))

    def test_since_dates_only_for_recorded_apps(self):
        self.assertEqual(visual_record.app_store_since('sleep-max'), 'September 16, 2026')
        self.assertEqual(visual_record.app_store_since('unknown-app'), '')


class SummariesTest(unittest.TestCase):
    def test_app_compare_lists_store_apps_with_dates(self):
        apps = [dict(a, category='Sleep & routines', summary='A <diary>.') for a in APPS]
        html = visual_record.app_compare(apps)
        self.assertEqual(html.count('<tr data-product-accent'), 4)
        self.assertIn('<time datetime="2026-06-23">June 23, 2026</time>', html)
        self.assertIn('A &lt;diary&gt;.', html)

    def test_web_compare_keeps_status_capitals(self):
        saas = [dict(slug='m', name='Marketing Max', domain='marketingmax.solarityai.com', stage='Grow', category='Video',
                     tagline='Reels.', status='Web app · internal V1', availability='Early access.')]
        html = visual_record.web_compare(saas)
        self.assertIn('Internal V1', html)
        self.assertNotIn('Internal v1', html)

    def test_company_facts_show_verified_values_only(self):
        html = visual_record.company_facts('founder@example.com')
        self.assertIn('Solarity AI LLC</dd>', html)
        self.assertNotIn('founded', html.split('<dt>Company</dt>')[1].split('</div>')[0])
        with mock.patch.dict(visual_record.COMPANY, {'founded': '2025'}):
            self.assertIn('Solarity AI LLC, founded 2025', visual_record.company_facts('founder@example.com'))


class HiddenUntilSuppliedTest(unittest.TestCase):
    def test_empty_facts_render_nothing(self):
        self.assertEqual(visual_record.founder_record(), '')
        self.assertEqual(visual_record.team_detail('Ali Yılmaz'), '')
        self.assertEqual(visual_record.company_line(), '')
        self.assertEqual(visual_record.program_brief(), '')

    def test_founder_record_escapes_and_links(self):
        founder = {'bio': 'Built <apps> & tools.', 'why': 'Because.', 'linkedin': 'https://www.linkedin.com/in/example/'}
        with mock.patch.object(visual_record, 'FOUNDER', founder):
            html = visual_record.founder_record()
        self.assertIn('Built &lt;apps&gt; &amp; tools.', html)
        self.assertIn('href="https://www.linkedin.com/in/example/"', html)
        self.assertIn('↗', html)

    def test_team_detail_shows_only_supplied_fields(self):
        details = {'Ali Yılmaz': {'role': 'Mobile engineer', 'commitment': 'Full-time'}}
        with mock.patch.object(visual_record, 'TEAM_DETAILS', details):
            html = visual_record.team_detail('Ali Yılmaz')
            self.assertEqual(visual_record.team_detail('Hasan Ak'), '')
        self.assertIn('Mobile engineer', html)
        self.assertNotIn('LinkedIn', html)

    def test_company_line_needs_a_fact_beyond_the_name(self):
        with mock.patch.dict(visual_record.COMPANY, {'founded': '2025', 'registered_in': 'Texas'}):
            self.assertEqual(visual_record.company_line(), 'Solarity AI LLC · founded 2025 · registered in Texas')

    def test_brief_ignores_undated_numbers(self):
        brief = {'seeking': 'A place in an accelerator.', 'use': '', 'why_now': '', 'one_pager': '',
                 'metrics': [{'value': '1,000', 'label': 'downloads', 'as_of': '2026-10-01'},
                             {'value': '9,999', 'label': 'undated users'}]}
        with mock.patch.object(visual_record, 'PROGRAM_BRIEF', brief):
            html = visual_record.program_brief()
        self.assertIn('A place in an accelerator.', html)
        self.assertIn('1,000', html)
        self.assertIn('As of October 1, 2026.', html)
        self.assertNotIn('9,999', html)


if __name__ == '__main__':
    unittest.main()


class DownloadsTest(unittest.TestCase):
    def test_answer_ids_are_stable_fragments(self):
        from ux_content import FAQ, answer_id
        self.assertEqual(answer_id('What is Solarity AI?'), 'faq-what-is-solarity-ai')
        self.assertEqual(answer_id('Can <em>other</em> teams use it?'), 'faq-can-other-teams-use-it')
        ids = [answer_id(q) for q, _ in FAQ]
        self.assertEqual(len(ids), len(set(ids)))

    def test_press_kit_archive_is_reproducible(self):
        import io
        import zipfile
        from visual_press import press_kit_zip
        APPS = [{'slug': s, 'apple': 'https://apps.apple.com/'} for s in ('looks-max', 'iq-max', 'sleep-max', 'fitness-max')]
        data = press_kit_zip(APPS)
        self.assertEqual(data, press_kit_zip(APPS))
        names = zipfile.ZipFile(io.BytesIO(data)).namelist()
        self.assertEqual(names[0], 'solarity-ai-press-kit/README.txt')
        self.assertIn('solarity-ai-press-kit/solarity-sun-mark.png', names)
        self.assertEqual(sum(n.endswith('-icon.webp') for n in names), 4)
        for info in zipfile.ZipFile(io.BytesIO(data)).infolist():
            self.assertEqual((info.compress_type, info.create_system, info.date_time), (zipfile.ZIP_STORED, 3, (2026, 10, 20, 0, 0, 0)))

    def test_founder_card_states_only_published_facts(self):
        from visual_contact import founder_vcard
        card = founder_vcard('founder@example.com')
        self.assertTrue(card.startswith('BEGIN:VCARD\r\nVERSION:3.0\r\n') and card.endswith('END:VCARD\r\n'))
        self.assertNotIn('\n', card.replace('\r\n', ''))
        for line in ['FN:Ata Turhan', 'ORG:Solarity AI LLC', 'TITLE:Founder', 'EMAIL;TYPE=INTERNET,WORK:founder@example.com']:
            self.assertIn(line + '\r\n', card)
        self.assertNotIn('TEL', card)
