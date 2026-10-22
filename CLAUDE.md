# Solarity AI: coding handoff

This repository holds the complete source of the public Solarity AI corporate site, https://solarityai.com. It began as the October 18, 2026 export of Site version 24; `SOURCE_MANIFEST.json` records that export and does not describe the current tree. See START_HERE.md for setup.

## Read first

1. Read this file and `DESIGN_SYSTEM.md` for the current architecture, rules and behavior. `CINEMATIC_REFINEMENT.md` is the October 13 record behind them.
2. Read `build_site.py`, the relevant component modules, and `CONTENT_REGISTER.md` before editing.
3. Treat older README and design-log sections as history. They describe superseded contact composers, hero artwork, font choices, stylesheet counts, and route counts. The implemented source and the latest cinematic refinement take precedence for the exported state.
4. Follow the founder's latest instructions for any new work. Public launch status, product capabilities, and commercial claims must be reverified before new publication; the sources of each published fact are in `CONTENT_REGISTER.md`.

## Architecture

- Static HTML/CSS/JavaScript, generated with Python. No React, Next.js, Vite, npm package manifest, database, or build framework is required.
- `build_site.py`: APPS records, page assembly, metadata, canonical origin, contacts, hosting headers and redirects, and the authoritative stylesheet list. `seo.py` writes the sitemap and robots.txt.
- `templates/`: all page markup, as Jinja templates in one folder per module (since 2026-10-20). `templating.py` renders them, escaping values exactly as `html.escape` does. Components return `str(render(...))` where callers join plain strings, because `Markup + str` escapes the plain side. `check_site.py` fails if HTML elements reappear in the component modules, or if a template has CRLF line endings. The wiki page "Templates" has the rules.
- `visual_*.py`, `product_story.py`, `ux_components.py`, `ux_content.py`: the data and logic for shared and route-specific sections; each renders its own templates. `saas_products.py` holds the three web apps; `visual_saas.py` renders them on Home and Platform. `visual_stage.py` holds the official store badges and the product close; `visual_catalog.py` holds the Home portfolio wall and the Apps lineup. The Home explorer (`product_explorer.py`) was retired in P5b.
- `design/system/`: 8 maintained CSS files. Edit these sources, not the generated `design/presentation.css` bundle (used only for build hashing) or inline output.
- `scripts/`: 7 maintained scripts: navigation, the screenshot viewer (with previous/next browsing), contact context, careers validation, the copy-address button, `sections.js` (opens linked FAQ answers, "Show all answers", and marks the current section in sticky indexes), and `not-found.js` (the 404 page's closest-match suggestion). The build inlines navigation in `<head>` before first paint to protect mobile layout stability, and inlines `sections.js` as a module at the end of the pages that use it (Investors, Platform); both ship through `performance_build.compact_script` (comment lines and indentation removed). The others are fingerprinted external files loaded only where used. A blocking or layout-forcing script costs Lighthouse first paint on the long pages: measure before adding one. `UX_REFINEMENTS.md` lists the October 18 UX pass and the contracts it relies on.
- `company_facts.py` and `visual_record.py`: the dated shipping record (App Store release dates), plus the founder record, team details, company line and program brief. Those four stay hidden until their facts are filled in `company_facts.py`, as do App Store campaign tags until `APPLE_CAMPAIGN_PROVIDER` holds the App Store Connect provider token (`site_urls.attributed` tags visible store and web-app links; schema.org keeps the plain URLs). `test_records.py` covers both states.
- `seo.py`: search and AI answer-engine metadata. It builds the schema.org graph for each page, `robots.txt` (search and AI crawlers welcome), the sitemap with `lastmod` from `research-assets/page-dates.json`, `llms.txt` and `llms-full.txt`, and the IndexNow key. `deploy/indexnow.py` (run by `.github/workflows/indexnow.yml` after each deploy) submits changed pages. `CONTENT_REGISTER.md` lists the sources for every fact it states.
- `visual_policies.py` renders the accessibility statement (`/accessibility`) and the website data page (`/website-data`). Both describe the site as built; re-verify them (cookies, analytics, form provider, testing) before changing hosting, scripts or forms.
- `visual_press.py` renders the press kit at `/press`. `make_press_assets.py` is run by hand. It writes the sun mark (`source-assets/press/`, using the documented crop of the official lockup), plus JPEG and PNG copies of the approved WebP portrait, icons and product screens, because many publishing tools refuse WebP. The build packs the kit into a byte-identical ZIP.
- `make_social_images.py`: run by hand; writes the 1200×630 link-preview images to `source-assets/social/` from approved material only. Commit its output. The build publishes the images on reference, which keeps the bytes identical across machines.
- `optimize_images.py`: local responsive WebP/AVIF variants, recorded edge trims for store screenshots, and the image manifest. `refetch_native_screens.py` re-fetches the published screenshots at native resolution into the git-ignored `source-assets/native/` for founder confirmation; it publishes nothing. `optimize_styles.py`: conservative route CSS filtering; classes that only scripts add belong in its `DYNAMIC_CLASSES`. `performance_build.py`: delivery optimization, including each page's speculation rules. They prefetch same-origin pages on visitor intent and must never prerender, which would run analytics for pages nobody opened. `check_site.py` enforces this.
- `dist/`: the publish set, meaning exactly what is deployed. **Do not delete dist before a build.** `dist/assets/` still holds published originals that have no other copy: full-size app screenshots (native gallery links), brand variants, and the two fonts (Manrope and Newsreader). `check_site.py` fails if `dist/` contains a file that no page references, apart from the host files in its `HOST_FILES` (`_headers`, `_redirects`, `robots.txt`, `sitemap.xml`, `llms.txt`, `llms-full.txt`, the IndexNow key, `favicon.ico`, `.well-known/security.txt` and the two font licenses).
- `source-assets/`: build inputs and unpublished approved files that are never deployed. This covers app-icon and hero masters, original brand files, team portraits, unused brand variants, and font provenance. If a page references `/assets/<path>` and only `source-assets/<path>` exists, the build publishes it automatically. `source-assets/retired/` holds retired artwork and scripts, which are never republished. `research-assets/deploy-separation.json` records every move.
- The build writes `dist/favicon.ico` from the documented sun crop of the original lockup. It also prunes stale content-addressed files in `dist/assets/optimized/` and `dist/assets/runtime/`.
- `research-assets/`: original approved hero, asset provenance, content evidence, optimization manifests, measured source-byte reports, and `production-audit.json`.
- `audit_production.py`: read-only audit of the live origin (routes, redirects, 404, headers vs `_headers`, MIME types, caching, favicon, exposed legacy files). Pass `--lighthouse <cli>` to add Lighthouse mobile/desktop runs. Results are summarized in `PRODUCTION_AUDIT.md`.

## Validation

Run from the project root after changes:

```sh
python validate.py
```

`validate.py` runs, in order and stopping at the first failure: `python build_site.py`, `python check_site.py` (0 errors required), every `test_*.py` with `unittest`, and every `test-*.cjs` with `node --test`. CI (`site-checks.yml`) runs the same steps and also fails if the rebuilt build outputs differ from the committed ones. New test files are picked up by name, with no edits to the script, the docs or CI.

Use `python3` if that is the Python 3 command on the local machine. On Windows, run the same commands with `.venv\Scripts\python.exe`. Build and audit scripts read and write text as explicit UTF-8 with LF newlines, and `.gitattributes` keeps LF in checkouts, because script fingerprints and inline-script hashes use raw bytes. Keep `encoding='utf-8'` (and `newline='\n'` on writes) in any new file I/O. `check_site.py` also fails when a `<br>` that CSS hides at some widths would join two words (put a space before such breaks). It also fails when a same-site link uses ↗. ↗ marks links that leave the Site (other origins, `mailto:`). Same-site links use →, and in-page jumps use ↓. Numbers are written as digits (founder, 2026-10-22): `check_site.py` fails when a number from two upward is spelled out in page text, metadata or `llms.txt`. "One" stays a word only where it is a pronoun ("made from one that already worked"). The export was checked with Python 3.12.14 and Node 24.19.0; `.python-version` and `.nvmrc` record the majors (3.12, 24), and `requirements.txt` pins Pillow 13.0.0. The third-party Python dependencies are Pillow, Jinja2 and MarkupSafe, pinned in `requirements.txt`. Browser testing and fresh Lighthouse results are separate from these static and behavior checks. Never claim measurements that were not run.

## Preserve unless the founder requests a change

- Investor and strategic partner objective; broad company self-improvement positioning.
- The company is in Dallas, Texas (founder, 2026-10-22; earlier copy said Irving). Every page, the schema.org address, the vCard and the press kit say Dallas.
- The approved stairway hero (founder, 2026-10-22): `research-assets/stairway-ascent-approved.webp` (a person walking up a lit stairway above the clouds toward a rising sun), with build master `source-assets/stairway-ascent.webp`: the supplied image upscaled 2× to 3344×1882 with Real-ESRGAN x4plus (`research-assets/stairway-ascent-artwork.json`). It is published only as `/assets/optimized/stairway-ascent-*` variants. Regenerate the master only from the approved file. The earlier natural-sunrise artwork is retired (`source-assets/retired/solar-ascent.webp`, `research-assets/solar-ascent-artwork.json`); do not restore retired artwork merely because older files remain.
- 4 consumer app names: Looks Max, IQ Max, Sleep Max, Fitness Max. Fitness Max's store-name disclosure is Only Fitness. Voice Max is retired from this Site.
- Approved company team: Ata Turhan plus Hasan Ak, Ali Yılmaz, Emrecan Özkan, Eren Öz, Melik Kaplan, Batuhan Yücetürk (the roster order, founder, 2026-10-21). Portraits: the founder's Drive "Profile Photos" folder (2026-10-21), cropped to one 4:5 frame in `source-assets/team/` and recorded in `research-assets/team-portraits.json`; Emrecan Özkan shows a monogram until a photo is supplied. Do not invent roles, portraits, credentials, or traction.
- Three SaaS products (the site's name for them since the founder's 2026-10-22 request; they run on the web): Engineering Max, Management Max and Marketing Max, all labeled early access (founder, 2026-10-20; Management Max also has a free plan), described only from their own sites (`saas_products.py`, `research-assets/saas-evidence.json`). Re-read those sites before changing a status, plan or capability. Mobile versions are a founder-stated plan and stay labeled as planned. No customer, usage or revenue claims.
- Current contact behavior is direct email/booking. It does not collect or submit contact messages. Keep query-derived subjects encoded and bounded. The page accepts only the topics in `CONTEXT_TOPICS` in `scripts/contact.js` (the 4 apps and the partnership topics; founder, 2026-10-22), so a crafted link cannot put its own text on the page. `check_site.py` fails if a site link passes a topic missing from that list: add new topics there.
- Careers posts to `https://formsubmit.co/careers@solarityai.com` with native validation, CAPTCHA, honeypot, provider confirmation, and direct email fallback. Activation and inbox receipt were confirmed on the earlier GPT Sites origin and remain unverified on solarityai.com. See `CAREERS_DELIVERY.md` for the evidence and the one-application test. Never treat a URL query parameter as delivery proof.
- Public access and the production domain `https://solarityai.com` (canonical origin since the move into this repository). `.openai/hosting.json` records the earlier GPT Sites deployment identity, but contains no deployment credential. Do not change DNS, the domain, or the deployment pipelines as part of ordinary code work.
- Native navigation, accessible focus and dialog behavior, reduced-motion support, explicit image dimensions, and matching hero preload.
- The Content-Security-Policy in `_headers` is generated from the built pages: a new inline script gets its hash automatically. A new third-party script, form target or connection must be added to `content_security_policy()` in `build_site.py`, and verified on the branch preview before merging.
- Motion stays opt-in: keyframes and scroll timelines live only under `prefers-reduced-motion: no-preference` (enforced by `check_site.py`), and reveals move but never fade text.

## Repository, deployment, and commits

This project lives in `github.com/Solarity-AI/solarityai-landing-page`, which also holds the infrastructure for solarityai.com.

- **Production host: Cloudflare Pages** (since 2026-10-18). The Pages project `solarityai-landing-page` is connected to this repository with production branch `main` (the default and only long-lived branch since 2026-10-20; `develop`, the production branch before that, was retired and deleted), no build command, and build output directory `dist`, so **every push or merge to `main` deploys solarityai.com**. Other branches get preview deployments on `<branch>.solarityai-landing-page.pages.dev`. Pages applies `dist/_headers` and `dist/_redirects`, both generated by `build_site.py`. `_redirects` keeps the previous site's URLs working with 301s: `/careers.html`, `/blog.html`, `/legal.html` and `/docs/xtract-demo.html`. Pages itself redirects `/index.html` and slashless routes.
- **Cloudflare zone behavior on solarityai.com.** Email Address Obfuscation would rewrite `mailto:` links, so every page body is wrapped in `<!--email_off-->…<!--/email_off-->`, which Cloudflare honors and then strips (`check_site.py` enforces the wrapper). The zone's Web Analytics setting injects a cookieless beacon script for browsers. `www` and `http` redirects are Cloudflare edge rules.
- **Verify a deployment** with `python deploy/smoke_test.py` (defaults to https://solarityai.com, or pass a `pages.dev` URL). It checks every route, redirect, the custom 404, `_headers` rules, MIME types, caching, and that files are byte-identical to `dist/` apart from the known edge changes above. `python audit_production.py` adds a broader read-only audit, plus Lighthouse with `--lighthouse <cli>`.
- `.github/workflows/site-checks.yml` runs on every pull request and on `main`. It rebuilds the site and fails if the committed `dist/` differs, then runs the static audit and both test suites. Merge only when it and the Cloudflare Pages preview check pass.
- **GitHub automation.**
  - **Workflows** (`.github/workflows/`), all with actions pinned to commit SHAs (the repository requires it; Dependabot updates the pins weekly):

    | Workflow | What it does |
    |---|---|
    | `site-checks` | Rebuild, dist drift, audit and tests. Required. |
    | `codeql` | Python, JavaScript and Actions. |
    | `dependency-review` | Reviews dependency changes in pull requests. |
    | `labeler` | Labels pull requests by area. |
    | `preview` | Waits for the PR's Cloudflare preview, smoke-tests it, and records informational Lighthouse runs. |
    | `production` | After each deploy and every 3 hours, smoke-tests solarityai.com and opens or updates a `production` issue when it fails (the schedule also catches a merge whose push event never triggered a deploy). |
    | `indexnow` | Submits changed pages after a deploy. |
    | `release` | Manual: tags `main` and publishes the live `dist/` with generated notes. |

  - **Settings and protections:**
    - The ruleset on `main` (the default branch) requires a pull request and the "Build and static checks" and "Cloudflare Pages" checks. It blocks force pushes and deletion, and blocks merges that add high-severity code scanning alerts.
    - Secret scanning with push protection, Dependabot alerts and security updates, and private vulnerability reporting are on.
    - The Production environment only accepts `main`.
  - **Community files:** issue forms, the PR template, CODEOWNERS, CONTRIBUTING, SECURITY and CODE_OF_CONDUCT live in `.github/`.
  - **Codespaces:** `.devcontainer/` opens with Python 3.12, Node 24 and a built site.
- **Removed pipelines.** Production was previously a Docker/nginx image rolled out by Woodpecker (`ci.solarityai.com`) to Kubernetes behind Caddy, with an AWS S3/CloudFront workflow alongside. Woodpecker stopped accepting GitHub webhooks (HTTP 400) and the AWS workflow failed on every run, so both were removed from this repository on 2026-10-18 (see git history). The old servers may still be running and are no longer receiving solarityai.com traffic. `ansible/` is an older, manually run EC2/nginx setup that is also unused for solarityai.com.
- Commits follow `Commit Rules.md` and `skills/git-conventional-commit`: one logical change per commit, with a single-line, lowercase, imperative Conventional Commit message of at most 50 characters (for example `fix: keep words apart at hidden line breaks`).
- A domain change requires coordinated edits to the origin in `build_site.py`, `seo.py`, `check_site.py`, `audit_production.py`, `deploy/smoke_test.py`, the `host` in `deploy/indexnow.py`, and the careers `_url` in `visual_careers.py`. Then attach the new domain to the Pages project, and verify with `python deploy/smoke_test.py` and `python audit_production.py`.

Missing optional source material: a matched set of clean app UI exports, approved team roles/additional portraits, and the upstream font TTFs. The complete deployable fonts, licenses, provenance, and all build-required image files are included. Some historical provenance records reference scratch paths that are no longer available; those are not build dependencies.

Local coding needs no deployment: build, check, and preview locally, then open a pull request.
