"""The production workflow: a run for a commit that a newer main commit replaced must not file a failure
(two merges seconds apart once filed issue #147), and a passing run closes the open production issue."""
import re
import unittest
from pathlib import Path

WORKFLOW = (Path(__file__).resolve().parent / '.github' / 'workflows' / 'production.yml').read_text(encoding='utf-8')


def step(name):
    match = re.search(r'- name: ' + re.escape(name) + r'\n(.*?)(?=\n      - name: |\Z)', WORKFLOW, re.S)
    return match.group(1) if match else ''


class ProductionWorkflowTest(unittest.TestCase):
    def test_a_superseded_push_stands_down_instead_of_failing(self):
        smoke = step('Wait for the deploy, then smoke-test it')
        self.assertIn('repos/${GITHUB_REPOSITORY}/commits/main', smoke)
        self.assertRegex(smoke, r'"\$latest" != "\$GITHUB_SHA"')
        self.assertIn('superseded=true', smoke)
        # The check runs inside the retry loop, before the run gives up.
        self.assertLess(smoke.index('superseded=true'), smoke.index('exit 1'))

    def test_a_passing_run_closes_the_production_issue(self):
        close = step('Close the production issue once production passes')
        self.assertIn("steps.smoke.outputs.superseded != 'true'", close)
        self.assertIn('gh issue close', close)
        self.assertIn('--label production', close)


if __name__ == '__main__':
    unittest.main()
