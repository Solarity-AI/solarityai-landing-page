# Continue this project in Claude

This is the git repository `github.com/Solarity-AI/solarityai-landing-page`. It holds the complete source: build scripts, the 12 generated pages (11 routes and the 404), CSS, JavaScript, tests, original and optimized assets, the font licenses, and the design and content records.

## 1. Open the folder

Clone the repository (`git clone https://github.com/Solarity-AI/solarityai-landing-page.git solarity-ai-project`), open `solarity-ai-project` in your editor, and give Claude access to that folder. Ask Claude to read `CLAUDE.md` before making changes.

## 2. Install the dependency

Use Python 3.12+ and Node.js. This export was verified with Python 3.12.14, Pillow 12.3.0, and Node 24.19.0. Node is used only for tests; there are no npm packages to install.

Windows PowerShell:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe build_site.py
.\.venv\Scripts\python.exe check_site.py
.\.venv\Scripts\python.exe -m unittest test_optimize_styles.py test_site_urls.py test_seo.py test_records.py
node --test test-navigation.cjs test-contact.cjs test-gallery.cjs test-careers.cjs test-copy.cjs
```

macOS or Linux:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python build_site.py
python check_site.py
python -m unittest test_optimize_styles.py test_site_urls.py test_seo.py test_records.py
node --test test-navigation.cjs test-contact.cjs test-gallery.cjs test-careers.cjs test-copy.cjs
```

Pillow must support WebP and AVIF to regenerate every image format. Existing optimized assets are included, so no external image downloads are needed. If the exact dependency pin is unavailable on your platform, use a compatible Pillow build with both encoders and rerun validation.

## 3. Preview locally

Windows:

```powershell
.\.venv\Scripts\python.exe -m http.server 8000 --bind 127.0.0.1 --directory dist
```

macOS/Linux, with the environment active:

```sh
python -m http.server 8000 --bind 127.0.0.1 --directory dist
```

Open http://127.0.0.1:8000/ in your browser. Directory-index routes such as `/apps/looks-max/` work. This simple preview does not emulate production custom 404 responses, hosting headers, or access settings.

To audit the live deployment (read-only GET requests), run `python audit_production.py`. See `PRODUCTION_AUDIT.md` for the latest results and `CAREERS_DELIVERY.md` for the careers delivery test.

## 4. Continue in Claude

Suggested initial instruction:

> Read CLAUDE.md and DESIGN_SYSTEM.md. Inspect the existing source and run the documented validation. Preserve the approved design, authentic assets, factual boundaries, and working behavior. Then continue with the specific changes I request. Do not replace this project with a new framework or rewrite generated HTML directly.

`.gitignore` keeps `.venv/`, machine caches and local secrets out of git. `SOURCE_MANIFEST.json` is the historical record of the October 2026 export this repository started from; it does not describe the current tree.

Production is https://solarityai.com, deployed from the `main` branch of `github.com/Solarity-AI/solarityai-landing-page` (see CLAUDE.md, "Repository, deployment, and commits"). The earlier GPT Sites deployment at https://solarity-company.the-ata-turhan.chatgpt.site is not updated from this repository.
