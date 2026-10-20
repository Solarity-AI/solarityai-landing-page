## What and why

<!-- One logical change. Name the page or component, and the founder request or problem it answers. -->

## Claims

- [ ] No new product capability, launch status, price, customer, traction or delivery claim, **or** each one is sourced in `CONTENT_REGISTER.md` (and `research-assets/`).

## Checks

- [ ] `python build_site.py`, with `dist/` and `site-pages.json` committed
- [ ] `python check_site.py` reports 0 errors
- [ ] `python -m unittest test_optimize_styles.py test_site_urls.py test_seo.py`
- [ ] `node --test test-navigation.cjs test-contact.cjs test-gallery.cjs test-careers.cjs test-copy.cjs`
- [ ] Rendered at desktop and phone widths, for visual changes (say how)

Merging into `main` deploys https://solarityai.com.
