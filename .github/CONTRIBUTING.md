# Contributing

Start with [CLAUDE.md](../CLAUDE.md) for the architecture and the rules, and [START_HERE.md](../START_HERE.md) for setup.

1. Branch from `develop`. Every push to `develop` deploys https://solarityai.com, so changes arrive by pull request.
2. Edit the Python components, `design/system/` and `scripts/`, never the generated output. Then run `python build_site.py` and commit `dist/` and `site-pages.json`. Never delete `dist/`.
3. Run `python check_site.py` and both test suites (listed in the pull request template).
4. Keep claims sourced: product capabilities, statuses, prices and traction come from store listings, the products' own sites or a dated founder decision, recorded in `CONTENT_REGISTER.md`.
5. Commits follow [Commit Rules.md](../Commit%20Rules.md): one logical change, with a lowercase, imperative Conventional Commit message of at most 50 characters.

## What runs on a pull request

| Check | What it does |
|---|---|
| Site checks | Rebuilds the site and fails if the committed `dist/` differs. Then it runs the static audit and both test suites. |
| Cloudflare Pages | Builds the branch preview at `<branch>.solarityai-landing-page.pages.dev`. |
| Preview | Waits for that preview, smoke-tests it against `dist/`, and attaches Lighthouse reports. |
| CodeQL | Scans the Python, the browser scripts and the workflows. |
| Dependency review | Blocks dependency changes with known high-severity vulnerabilities. |
| Labeler | Labels the pull request by the areas it changes. |

After a merge, **Production** waits for solarityai.com to serve the new `dist/` and smoke-tests it. It runs again daily and opens an issue if the site drifts. **Release** (run by hand) tags what is live and attaches the deployed `dist/`.
