# Production audit, solarityai.com, 2026-10-18

Origin: `https://solarityai.com`, served by Cloudflare Pages (project `solarityai-landing-page`, production branch `develop`) since 2026-10-18. Raw data: `research-assets/production-audit.json`. Re-run with `python audit_production.py` and `python deploy/smoke_test.py`, adding `--lighthouse <path to lighthouse/cli/index.js>` to the audit for lab scores.

## Method

- **`deploy/smoke_test.py`**: 42 checks covering all 11 routes, slashless and legacy redirects, the custom 404, `_headers` rules, MIME types, caching, and byte-for-byte comparison with `dist/`.
- **`audit_production.py`**: read-only GET requests to all 11 sitemap routes, 71 referenced assets, `/favicon.ico`, and the 45 paths that the previous host exposed.
- **Lighthouse 13.5.0**: headless Chrome 155 on the auditor's Windows machine, one run per route and form factor (22 runs in all). Mobile uses default simulated throttling; desktop uses `--preset=desktop`. These are lab results from this machine, not Google PageSpeed Insights runs or real-user field data.

## Results

- **Smoke test: 42 of 42 pass.** Every page is byte-identical to `dist/` apart from two known Cloudflare edge changes: the `email_off` markers are stripped after being honored, and the Web Analytics beacon is injected.
- **HTTP audit: no findings.**
  - All routes return 200 with canonical URLs.
  - Slashless routes redirect (308). The old `/careers.html`, `/blog.html`, `/legal.html` and `/docs/xtract-demo.html` URLs redirect with 301, and `/index.html` with 308.
  - Missing pages return 404 with the custom page.
  - Security headers (`nosniff`, Referrer-Policy, X-Frame-Options) and immutable caching for fingerprinted files are applied, and all MIME types are correct.
  - `/favicon.ico` returns 200. None of the previous host's 45 legacy files are reachable.
- **`www` and `http`** redirect to `https://solarityai.com` through Cloudflare edge rules.

| Lighthouse (11 routes) | Mobile | Desktop |
| --- | --- | --- |
| Performance | 92–99 (home 92, six routes 99) | 99–100 |
| Accessibility | 100 | 100 |
| Best Practices | 100 | 100 |
| SEO | 100 | 100 |

- **Mobile metrics:** FCP 1.6–1.9 s, LCP 1.8–3.2 s (home slowest), TBT 0 ms, CLS 0, Speed Index 1.7–3.0 s.
- **Desktop metrics:** FCP 0.4–0.7 s, LCP 0.6–0.7 s, TBT 0 ms, CLS 0.

**Web Analytics trade-off.** The zone's Cloudflare Web Analytics beacon (`static.cloudflareinsights.com`, ~10 KiB) sits on the home page's network chain, and Lighthouse flags it as legacy JavaScript. In back-to-back home-page runs the identical site without the beacon (`pages.dev`) scored 96 and 99 on mobile, against 94 and 93 on solarityai.com. Run-to-run variance is large (LCP 1.7–3.1 s), so these are indicative only. Keeping the analytics is a product decision. It can be switched off under the zone's Web Analytics settings.

## Compared with the previous host (GPT Sites, measured earlier the same day)

- **Best Practices:** 81 → **100**. The host-injected Cloudflare bot-challenge script is gone.
- **HTTP findings:** the previous host ignored `_headers` (no security headers, `max-age=0` on fingerprinted files), served 62 of 71 assets as `application/octet-stream`, returned 404 for `/favicon.ico`, and exposed 45 legacy files. **All are resolved on Cloudflare Pages.**
- **Mobile Performance:** the previous host scored 100 on every route. Most of the difference is the Web Analytics beacon and lab variance, as shown above.

## Open items

1. Careers: repeat the FormSubmit activation test once on `https://solarityai.com/careers/#apply` (see `CAREERS_DELIVERY.md`).
2. Decide whether to keep Cloudflare Web Analytics on the zone.
3. The old Woodpecker/Kubernetes server and the AWS resources no longer serve solarityai.com. Whoever runs them can shut them down.

## Redesign baseline (Phase P0, 2026-10-18)

This is the before measurement for the cinematic redesign (`CINEMATIC_PREMIUM_PLAN.md`). It was taken at develop `b0eff9b` on https://solarityai-landing-page.pages.dev, which serves the same files as solarityai.com without the analytics beacon.

Method: Lighthouse 13.5.0 in headless Chrome 155 on this Windows machine. It ran 3 times per route and form factor (36 runs), and the table shows the median. Mobile uses default simulated throttling; desktop uses `--preset=desktop`. These are lab results, not field data. Raw medians are in `research-assets/baseline-2026-10-18/lighthouse-medians.json`.

| Route | Form factor | Perf | A11y | Best practices | SEO | LCP median (range) | FCP | CLS | TBT |
|---|---|---|---|---|---|---|---|---|---|
| `/` | mobile | 100 | 100 | 100 | 100 | 1.72 s (1692–1723 ms) | 1.10 s | 0.000 | 0 ms |
| `/investors-partners/` | mobile | 100 | 100 | 100 | 100 | 1.13 s (1115–1253 ms) | 0.88 s | 0.000 | 0 ms |
| `/apps/looks-max/` | mobile | 100 | 100 | 100 | 100 | 1.27 s (1264–1909 ms) | 1.02 s | 0.000 | 0 ms |
| `/apps/iq-max/` | mobile | 100 | 100 | 100 | 100 | 1.27 s (1270–1317 ms) | 1.04 s | 0.000 | 0 ms |
| `/platform/` | mobile | 100 | 100 | 100 | 100 | 1.12 s (1099–1147 ms) | 0.87 s | 0.000 | 0 ms |
| `/company/` | mobile | 100 | 100 | 100 | 100 | 1.26 s (1258–1311 ms) | 0.86 s | 0.000 | 0 ms |
| `/` | desktop | 100 | 100 | 100 | 100 | 0.48 s (427–587 ms) | 0.35 s | 0.000 | 0 ms |
| `/investors-partners/` | desktop | 100 | 100 | 100 | 100 | 0.39 s (390–392 ms) | 0.29 s | 0.000 | 0 ms |
| `/apps/looks-max/` | desktop | 100 | 100 | 100 | 100 | 0.37 s (342–400 ms) | 0.33 s | 0.000 | 0 ms |
| `/apps/iq-max/` | desktop | 100 | 100 | 100 | 100 | 0.40 s (343–486 ms) | 0.32 s | 0.000 | 0 ms |
| `/platform/` | desktop | 100 | 100 | 100 | 100 | 0.35 s (342–370 ms) | 0.28 s | 0.000 | 0 ms |
| `/company/` | desktop | 100 | 100 | 100 | 100 | 0.44 s (337–504 ms) | 0.27 s | 0.000 | 0 ms |

All 36 runs scored 100 in all four categories, with CLS 0 and TBT 0. The redesign must hold these numbers. The mobile home LCP, 1.72 s, is the figure most at risk from new fonts and larger imagery. Plan §10 sets the budgets.

## Phase P2 type measurement (2026-10-18)

The Newsreader display face was measured against the P0 baseline. Lighthouse 13.5.0 ran mobile simulated throttling, three runs each.

- **Cross-network runs were too noisy to compare builds.** Back-to-back runs against Cloudflare from this machine varied by up to 700 ms on the same page, so the comparison used one local server instead.
- **Controlled A/B on the Investors page (local server, uncompressed):**

  | Build | LCP median | Runs (ms) |
  |---|---|---|
  | P0 | 2,118 ms | 2,117 / 2,118 / 2,136 |
  | P1 | 2,116 ms | 2,110 / 2,116 / 2,119 |
  | P2 | 2,225 ms | 2,197 / 2,225 / 2,298 |

  - P1 (light and color) costs nothing.
  - P2 costs about +109 ms of simulated slow-4G LCP. That is the 27 KB display-font preload competing for bandwidth, 9 ms over the plan's +100 ms target.
  - It is kept deliberately: without the preload, a first visit would usually render titles in the Georgia fallback.
- **Display font loading.** With `font-display: swap` the title re-rendered when the font arrived. That moved LCP by +600 to +850 ms on the preview. The face therefore loads `optional`.
- **Home.** With `optional`, preloading the display face on Home measured 2,857 ms against 2,855 ms without, so Home keeps the preload.
- **Layout shift.** CLS was 0 in every P2 run.

