# Solarity AI: coding handoff

This is the complete source export of the public Solarity AI corporate Site, version 24, commit `27e009b87c931d61e0464bc6460041e80417db95`, exported October 18, 2026. See START_HERE.md for setup and SOURCE_MANIFEST.json for provenance and checksums. The live website was not changed to create this export.

## Read first

1. Read this file and `CINEMATIC_REFINEMENT.md` for the current architecture and behavior.
2. Read `build_site.py`, the relevant component modules, and `CONTENT_REGISTER.md` before editing.
3. Treat older README and design-log sections as history. They describe superseded contact composers, hero artwork, font choices, stylesheet counts, and route counts. The implemented source and the latest cinematic refinement take precedence for the exported state.
4. Follow the founder's latest instructions for any new work. Public launch status, product capabilities, and commercial claims must be reverified before new publication; this export preserves the October 13 implementation, not a new factual review.

## Architecture

- Static HTML/CSS/JavaScript, generated with Python. No React, Next.js, Vite, npm package manifest, database, or build framework is required.
- `build_site.py`: APPS records, page assembly, metadata, canonical origin, contacts, sitemap, robots, hosting headers, and the authoritative stylesheet list.
- `visual_*.py`, `product_story.py`, `ux_components.py`, `ux_content.py`: shared and route-specific HTML. `visual_stage.py` holds the official store badges and the product close; `visual_catalog.py` holds the Home portfolio wall and the Apps lineup. The Home explorer (`product_explorer.py`) was retired in P5b.
- `design/system/`: 8 maintained CSS files. Edit these sources, not the generated `design/presentation.css` bundle (used only for build hashing) or inline output.
- `scripts/`: 5 maintained scripts for navigation, the screenshot viewer (with previous/next browsing), contact context, careers validation, and the copy-address button. The build fingerprints external scripts and inlines navigation before first paint to protect mobile layout stability. `UX_REFINEMENTS.md` lists the October 18 UX pass and the contracts it relies on.
- `optimize_images.py`: local responsive WebP/AVIF variants, recorded edge trims for store screenshots, and the image manifest. `refetch_native_screens.py` re-fetches the published screenshots at native resolution into the git-ignored `source-assets/native/` for founder confirmation; it publishes nothing. `optimize_styles.py`: conservative route CSS filtering; classes that only scripts add belong in its `DYNAMIC_CLASSES`. `performance_build.py`: delivery optimization, including each page's speculation rules. They prefetch same-origin pages on visitor intent and must never prerender, which would run analytics for pages nobody opened. `check_site.py` enforces this.
- `dist/`: the publish set, meaning exactly what is deployed. **Do not delete dist before a build.** `dist/assets/` still holds published originals that have no other copy: full-size app screenshots (native gallery links), the social image, brand variants, and the font. `check_site.py` fails if `dist/` contains a file that no page references, apart from `_headers`, `robots.txt`, `sitemap.xml`, `favicon.ico`, and the font license.
- `source-assets/`: build inputs and unpublished approved files that are never deployed. This covers app-icon and hero masters, original brand files, team portraits, unused brand variants, and font provenance. If a page references `/assets/<path>` and only `source-assets/<path>` exists, the build publishes it automatically. `source-assets/retired/` holds retired artwork and scripts, which are never republished. `research-assets/deploy-separation.json` records every move.
- The build writes `dist/favicon.ico` from the documented sun crop of the original lockup. It also prunes stale content-addressed files in `dist/assets/optimized/` and `dist/assets/runtime/`.
- `research-assets/`: original approved hero, asset provenance, content evidence, optimization manifests, measured source-byte reports, and `production-audit.json`.
- `audit_production.py`: read-only audit of the live origin (routes, redirects, 404, headers vs `_headers`, MIME types, caching, favicon, exposed legacy files). Pass `--lighthouse <cli>` to add Lighthouse mobile/desktop runs. Results are summarized in `PRODUCTION_AUDIT.md`.

## Validation

Run from the project root after changes:

```sh
python build_site.py
python check_site.py
python -m unittest test_optimize_styles.py test_site_urls.py
node --test test-navigation.cjs test-contact.cjs test-gallery.cjs test-careers.cjs test-copy.cjs
```

Use `python3` if that is the Python 3 command on the local machine. On Windows, run the same commands with `.venv\Scripts\python.exe`. Build and audit scripts read and write text as explicit UTF-8 with LF newlines, and `.gitattributes` keeps LF in checkouts, because script fingerprints and inline-script hashes use raw bytes. Keep `encoding='utf-8'` (and `newline='\n'` on writes) in any new file I/O. `check_site.py` also fails when a `<br>` that CSS hides at some widths would join two words (put a space before such breaks). It also fails when a same-site link uses ↗. ↗ marks links that leave the Site (other origins, `mailto:`). Same-site links use →, and in-page jumps use ↓. The export was checked with Python 3.12.14, Pillow 12.3.0, and Node 24.19.0. Pillow is the only third-party Python dependency. Browser testing and fresh Lighthouse results are separate from these static and behavior checks. Never claim measurements that were not run.

## Preserve unless the founder requests a change

- Investor and strategic partner objective; broad company self-improvement positioning.
- The approved natural-sunrise hero: `research-assets/solar-ascent-approved.png`, with build master `source-assets/solar-ascent.webp` (published only as `/assets/optimized/solar-ascent-*` variants). Do not restore retired artwork merely because older files remain.
- 4 consumer app names: Looks Max, IQ Max, Sleep Max, Fitness Max. Fitness Max's store-name disclosure is Only Fitness. Voice Max is retired from this Site.
- Approved company team: Ata Turhan plus Emrecan Özkan, Ali Yılmaz, Hasan Ak, Eren Öz, Batuhan Yücetürk, Melik Kaplan. Do not invent roles, portraits, credentials, or traction.
- App factory pages distinguish company strategy from verified deployed capabilities. Obtain current evidence before strengthening claims.
- Current contact behavior is direct email/booking. It does not collect or submit contact messages. Keep query-derived subjects encoded and bounded.
- Careers posts to `https://formsubmit.co/careers@solarityai.com` with native validation, CAPTCHA, honeypot, provider confirmation, and direct email fallback. Activation and actual inbox receipt remain unverified. See `CAREERS_DELIVERY.md` for the evidence and the one-application test. Never treat a URL query parameter as delivery proof.
- Public access and the production domain `https://solarityai.com` (canonical origin since the move into this repository). `.openai/hosting.json` records the earlier GPT Sites deployment identity, but contains no deployment credential. Do not change DNS, the domain, or the deployment pipelines as part of ordinary code work.
- Native navigation, accessible focus and dialog behavior, reduced-motion support, explicit image dimensions, and matching hero preload.

## Repository, deployment, and commits

This project lives in `github.com/Solarity-AI/solarityai-landing-page`, which also holds the infrastructure for solarityai.com.

- **Production host: Cloudflare Pages** (since 2026-10-18). The Pages project `solarityai-landing-page` is connected to this repository with production branch `develop`, no build command, and build output directory `dist`, so **every push or merge to `develop` deploys solarityai.com**. Other branches get preview deployments on `<branch>.solarityai-landing-page.pages.dev`. Pages applies `dist/_headers` and `dist/_redirects`, both generated by `build_site.py`. `_redirects` keeps the previous site's URLs working with 301s: `/careers.html`, `/blog.html`, `/legal.html` and `/docs/xtract-demo.html`. Pages itself redirects `/index.html` and slashless routes.
- **Cloudflare zone behavior on solarityai.com.** Email Address Obfuscation would rewrite `mailto:` links, so every page body is wrapped in `<!--email_off-->…<!--/email_off-->`, which Cloudflare honors and then strips (`check_site.py` enforces the wrapper). The zone's Web Analytics setting injects a cookieless beacon script for browsers. `www` and `http` redirects are Cloudflare edge rules.
- **Verify a deployment** with `python deploy/smoke_test.py` (defaults to https://solarityai.com, or pass a `pages.dev` URL). It checks every route, redirect, the custom 404, `_headers` rules, MIME types, caching, and that files are byte-identical to `dist/` apart from the known edge changes above. `python audit_production.py` adds a broader read-only audit, plus Lighthouse with `--lighthouse <cli>`.
- `.github/workflows/site-checks.yml` runs on every pull request and on `develop`. It rebuilds the site and fails if the committed `dist/` differs, then runs the static audit and both test suites. Merge only when it and the Cloudflare Pages preview check pass.
- **Removed pipelines.** Production was previously a Docker/nginx image rolled out by Woodpecker (`ci.solarityai.com`) to Kubernetes behind Caddy, with an AWS S3/CloudFront workflow alongside. Woodpecker stopped accepting GitHub webhooks (HTTP 400) and the AWS workflow failed on every run, so both were removed from this repository on 2026-10-18 (see git history). The old servers may still be running and are no longer receiving solarityai.com traffic. `ansible/` is an older, manually run EC2/nginx setup that is also unused for solarityai.com.
- Commits follow `Commit Rules.md` and `skills/git-conventional-commit`: one logical change per commit, with a single-line, lowercase, imperative Conventional Commit message of at most 50 characters (for example `fix: keep words apart at hidden line breaks`).
- A domain change requires coordinated edits to the origin in `build_site.py`, `check_site.py`, `audit_production.py`, and the careers `_url` in `visual_careers.py`. Then attach the new domain to the Pages project, and verify with `python deploy/smoke_test.py` and `python audit_production.py`.

Missing optional source material: a matched set of clean app UI exports, approved team roles/additional portraits, and the upstream font TTF. The complete deployable font, license, provenance, and all build-required image files are included. Some historical provenance records reference scratch paths that are no longer available; those are not build dependencies.

Local coding needs no deployment: build, check, and preview locally, then open a pull request.
