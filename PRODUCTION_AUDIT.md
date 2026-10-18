# Production audit, 2026-10-18

Origin: `https://solarity-company.the-ata-turhan.chatgpt.site` (deployed Site version 24, unchanged by this work). This is a dated record of the GPT Sites deployment, measured before the move to solarityai.com. After the first deploy from this repository, run `python audit_production.py` (it now defaults to `https://solarityai.com`); `deploy/nginx.conf` addresses the header, caching, MIME and favicon findings below. Raw data: `research-assets/production-audit.json`. Re-run with `python audit_production.py`, adding `--lighthouse <path to lighthouse/cli/index.js>` for lab scores.

## Method

- **HTTP checks**: read-only GET requests from `audit_production.py`, without following redirects. They covered all 11 sitemap routes, their no-slash forms, a missing path, `/404`, all 71 assets the pages reference, `/favicon.ico`, and the 45 legacy paths listed in `research-assets/deploy-separation.json`.
- **Lighthouse**: 13.5.0 in headless Chrome 155 on the auditor's Windows machine (benchmark index 4414), one run per route and form factor, 22 runs in all. Mobile uses Lighthouse's default simulated throttling (150 ms RTT, ~1.6 Mbps, 4× CPU). Desktop uses `--preset=desktop`.
- **Not used**: Google PageSpeed Insights. Its keyless API quota returned HTTP 429, so these are lab results from this machine, not Google-hosted runs or real-user field data.

## Lighthouse results (all 11 routes)

| Category | Mobile | Desktop |
| --- | --- | --- |
| Performance | 100 on every route | 100 on every route |
| Accessibility | 100 on every route | 100 on every route |
| Best Practices | 81 on every route | 81 on every route |
| SEO | 100 on every route | 100 on every route |

Mobile ranges: FCP 0.9–1.1 s, LCP 0.9–1.7 s (home is slowest at 1.7 s), TBT 0–50 ms, CLS 0, Speed Index 0.9–2.2 s. Desktop ranges: FCP 0.2–0.4 s, LCP 0.2–0.4 s, TBT 0 ms, CLS 0.

- **Best Practices 81** comes entirely from the `deprecations` audit. It flags `/cdn-cgi/challenge-platform/scripts/jsd/main.js`, a Cloudflare bot-challenge script that the host injects (StorageType.persistent and the Protected Audience API). The Site's own code has no deprecated APIs and no console errors. Raising this score needs a host setting or a different host, not a Site change.
- **`label-content-name-mismatch`** (weight 0, informational) was flagged on every page. The header wordmark's visible text was "SOLARITYAI" while its accessible name is "Solarity AI home". **Fixed locally**: `visual_chrome.py` now renders "SOLARITY AI" with pixel-identical layout. It takes effect on the next deploy.
- **`image-delivery-insight`**: about 4 KiB could be saved on the 96 px header sun at its 30–34 px display size. Not changed.

## HTTP findings

| Check | Result |
| --- | --- |
| 11 sitemap routes | All 200 `text/html`, canonical matches the URL |
| No-slash routes (`/apps`, …) | All 307 to the slash URL |
| Missing path | 404 status with the custom page and `noindex,follow` meta |
| `/404` directly | 200 (custom page, `noindex` meta) |
| `_headers` rules | **Not applied.** No `X-Content-Type-Options`, `Referrer-Policy` or `X-Robots-Tag` on any response, and `/_headers` itself downloads publicly |
| Caching | **Every** page and asset is sent `public, max-age=0, must-revalidate`, including fingerprinted assets meant to be `immutable` (Cloudflare edge HITs still occur) |
| MIME types | **62 of 71** referenced assets are served as `application/octet-stream`: all WebP images and the WOFF2 font. Pages render because browsers sniff images and fonts, but the screenshot "Enlarge" fallback (opening the image in a new tab) may download the file instead of showing it |
| `/favicon.ico` | 404. **Fixed locally**: the build now publishes `/favicon.ico` |
| Legacy files | 45 files outside the current publish set are public (retired artwork, old `site.js`, stale scripts, masters, `_headers`). **Fixed locally**: none of them are in `dist/` anymore. They disappear on the next deploy if the host replaces rather than merges files |

## What needs the host or founder

1. **Redeploy `dist/`**, then re-run `python audit_production.py`. It should show `/favicon.ico` 200 and no exposed legacy files except `/_headers` if the host keeps serving it.
2. **Response headers, caching, MIME types**: this host ignores `_headers`. If its dashboard offers header or MIME settings, apply the rules in `dist/_headers` there. Otherwise those rules only take effect on a host that honors `_headers` (for example Cloudflare Pages or Netlify). Moving hosts is a founder decision, so nothing was changed here.
3. **Cloudflare bot challenge**: disabling the injected challenge script (if the host allows) would lift Best Practices to 100.
