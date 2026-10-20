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
