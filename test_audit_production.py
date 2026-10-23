"""audit_production.audit_assets: an edge copy with the previous _headers is re-checked fresh, not reported."""
import unittest
from unittest import mock

import audit_production
from hosting_rules import parse_headers

RULES = parse_headers('/*\n  Content-Security-Policy: new\n')


def responses(table):
    """A fake fetch: the headers each URL answers with."""
    calls = []
    def fetch(url, body=True):
        calls.append(url)
        return {'url': url, 'status': 200, 'headers': table(url), 'bytes': 0, 'text': ''}
    return fetch, calls


class AuditAssetsTest(unittest.TestCase):
    def audit(self, table):
        fetch, calls = responses(table)
        findings = []
        with mock.patch.object(audit_production, 'fetch', fetch):
            results = audit_production.audit_assets({'/assets/a.webp'}, 'https://solarityai.com', RULES, findings)
        return results['/assets/a.webp'], findings, calls

    def test_edge_copy_with_previous_headers_is_rechecked_fresh(self):
        record, findings, calls = self.audit(lambda url: {'content-type': 'image/webp', 'content-security-policy': 'new' if 'audit-fresh' in url else 'old', 'cf-cache-status': 'MISS' if 'audit-fresh' in url else 'HIT'})
        self.assertEqual(record['missing_expected_headers'], [])
        self.assertEqual(record['edge_copy_missing_headers'], ['content-security-policy: expected "new", got "old"'])
        self.assertEqual(findings, [])
        self.assertEqual(len(calls), 2)

    def test_a_deployment_missing_the_header_is_still_reported(self):
        record, findings, calls = self.audit(lambda url: {'content-type': 'image/webp', 'cf-cache-status': 'HIT'})
        self.assertEqual(record['missing_expected_headers'], ['content-security-policy: expected "new", got ""'])

    def test_an_uncached_response_is_not_refetched(self):
        record, findings, calls = self.audit(lambda url: {'content-type': 'image/webp', 'content-security-policy': 'old', 'cf-cache-status': 'MISS'})
        self.assertEqual(len(calls), 1)
        self.assertNotIn('edge_copy_missing_headers', record)
        self.assertEqual(len(record['missing_expected_headers']), 1)


if __name__ == '__main__':
    unittest.main()
