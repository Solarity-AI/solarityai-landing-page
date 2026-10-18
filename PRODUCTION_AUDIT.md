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
