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
- `visual_*.py`, `product_explorer.py`, `product_story.py`, `ux_components.py`, `ux_content.py`: shared and route-specific HTML.
- `design/system/`: 8 maintained CSS files. Edit these sources, not generated `dist/assets/presentation.css` or inline output.
- `scripts/`: 4 maintained scripts for navigation, screenshot gallery, contact context, and careers validation. The build fingerprints external scripts and inlines navigation before first paint to protect mobile layout stability.
- `optimize_images.py`: local responsive WebP/AVIF variants and the image manifest. `optimize_styles.py`: conservative route CSS filtering. `performance_build.py`: delivery optimization.
- `dist/`: complete ready-to-serve website and original assets. **Do not delete dist before a build.** `dist/assets/` contains maintained source images and fonts as well as generated derivatives.
- `research-assets/`: original approved hero, asset provenance, content evidence, optimization manifests, and measured source-byte reports.

## Validation

Run from the project root after changes:

```sh
python build_site.py
python check_site.py
python -m unittest test_optimize_styles.py test_site_urls.py
node --test test-navigation.cjs test-contact.cjs test-gallery.cjs test-careers.cjs
```

Use `python3` if that is the Python 3 command on the local machine. On Windows, run the same commands with `.venv\Scripts\python.exe`. Build and audit scripts read and write text as explicit UTF-8 with LF newlines, and `.gitattributes` keeps LF in checkouts, because script fingerprints and inline-script hashes use raw bytes. Keep `encoding='utf-8'` (and `newline='\n'` on writes) in any new file I/O. `check_site.py` also fails when a `<br>` that CSS hides at some widths would join two words. Put a space before such breaks. The export was checked with Python 3.12.14, Pillow 12.3.0, and Node 24.19.0. Pillow is the only third-party Python dependency. Browser testing and fresh Lighthouse results are separate from these static and behavior checks. Never claim measurements that were not run.

## Preserve unless the founder requests a change

- Investor and strategic partner objective; broad company self-improvement positioning.
- The approved natural-sunrise hero: `research-assets/solar-ascent-approved.png`, with deployed master `dist/assets/solar-ascent.webp`. Do not restore retired artwork merely because older files remain.
- 4 consumer app names: Looks Max, IQ Max, Sleep Max, Fitness Max. Fitness Max's store-name disclosure is Only Fitness. Voice Max is retired from this Site.
- Approved company team: Ata Turhan plus Emrecan Özkan, Ali Yılmaz, Hasan Ak, Eren Öz, Batuhan Yücetürk, Melik Kaplan. Do not invent roles, portraits, credentials, or traction.
- App factory pages distinguish company strategy from verified deployed capabilities. Obtain current evidence before strengthening claims.
- Current contact behavior is direct email/booking. It does not collect or submit contact messages. Keep query-derived subjects encoded and bounded.
- Careers posts to `https://formsubmit.co/careers@solarityai.com` with native validation, CAPTCHA, honeypot, provider confirmation, and direct email fallback. Activation and actual inbox receipt remain unverified. Never treat a URL query parameter as delivery proof.
- Public access and the current deployment domain. `.openai/hosting.json` records the existing Site identity, but contains no deployment credential. Do not change solarityai.com or DNS as part of ordinary code work.
- Native navigation, accessible focus and dialog behavior, reduced-motion support, explicit image dimensions, and matching hero preload.

## Hosting and open dependencies

Deploy `dist/` to a suitable static host. Preview locally using the command in START_HERE.md. A new domain requires coordinated changes to the origin in `build_site.py`, `check_site.py`, and the careers `_url` in `visual_careers.py`. Verify actual host routing, 404 behavior, security headers, and caching; the included `_headers` file alone is not proof that a host applies those rules.

Missing optional source material: a matched set of clean app UI exports, approved team roles/additional portraits, and the upstream font TTF. The complete deployable font, license, provenance, and all build-required image files are included. Some historical provenance records reference scratch paths that are no longer available; those are not build dependencies.

No production redeployment is needed to begin local coding from this ZIP.
