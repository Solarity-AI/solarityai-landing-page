# Solarity AI: 10 UX improvements

Implemented October 18, 2026. This pass makes the Site faster to act on and easier to move through. It keeps the approved visual direction, content, 4-app portfolio, and contact destinations. No product capability, launch status, or delivery claim changed.

| # | Area | Implemented improvement | Purpose |
|---|---|---|---|
| 1 | Contact | The email address and booking action come before the founder profile in source order. Wide screens keep the profile on the left; phones put both actions on the first screen. | Show visitors how to reach Ata without scrolling. Both actions are visible on arrival at 360x780, 375x667, 390x844, and 768x1024. |
| 2 | Contact and Careers | A Copy address button beside each email address. It appears only when the browser offers clipboard access, and it confirms the copy or explains how to select the address instead. | Help visitors who have no mail app configured, without claiming that anything was sent. |
| 3 | Investors & Partners | An On this page index: Portfolio, Thesis, Partnerships, Questions, and Talk with the founder. | Let investors jump straight to the part of a long page they came for. |
| 4 | Whole Site | Every link that opens a new tab says so to screen readers. | Prevent unexpected context changes for assistive-technology users. |
| 5 | Mobile navigation | The page behind the open menu no longer scrolls. | Keep the menu in place when a visitor scrolls inside it. |
| 6 | In-page jumps | One header offset for every anchor. Jumps animate after the visitor's first interaction, honoring reduced motion. | Land anchors just below the header. Deep links still open at their target instantly. |
| 7 | Apps | Each product name in the portfolio links to its app page. | Match the common expectation that a product title opens the product. |
| 8 | Screenshot viewer | Previous and Next buttons, Left and Right arrow keys, and an "N of M" count. | Browse a product's screenshots without closing and reopening the viewer. |
| 9 | Careers form | LinkedIn and portfolio links pasted without `https://` are completed. LinkedIn country addresses such as `tr.linkedin.com` are accepted. Placeholders show the expected format. | Stop rejecting the links candidates usually paste. |
| 10 | Whole Site | Chromium browsers prefetch a same-origin page when a visitor shows intent to open it. | Open the next page without a network wait. |

## Contracts to keep

- **Anchor offset:** `scroll-padding-top` on `html` in `foundation.css` is the only jump offset. Adding `scroll-margin` to targets doubles it.
- **Smooth scrolling:** `scripts/navigation.js` adds `html.smooth-scroll` on the first pointer or key press, so a deep link on load jumps instantly. The class is listed in `DYNAMIC_CLASSES` in `optimize_styles.py`; without it, route filtering removes the rule.
- **Contact layout:** keep `.contact-direct` before `.contact-person` in `visual_contact.py`. Grid placement in `contact.css` restores the desktop columns.
- **Copy button:** `copy_button` in `ux_components.py` renders the button hidden; `scripts/copy.js` reveals it only when `navigator.clipboard.writeText` exists. Any page whose markup contains `data-copy` loads the script, and `check_site.py` checks this.
- **New tabs:** `check_site.py` fails if a `target="_blank"` link lacks the "opens in a new tab" text. Screenshot links are exempt because the viewer opens in place; modified clicks still open the image natively.
- **Screenshot sequence:** the viewer browses the page's same-origin `.screenshot-open` links in reading order. Markup without the navigation controls keeps single-image previews.
- **Careers links:** `withScheme` in `scripts/careers.js` adds `https://` only to input that starts with a domain. Everything else goes to validation unchanged. LinkedIn accepts `www.` or a two-letter country subdomain, with the same `/in/<name>` path rule. Keep the HTML `pattern` and the script in step.
- **Investors index:** the targets are `#portfolio`, `#thesis`, `#conversation-paths`, `#investor-questions`, and `#booking` in `visual_company_upgrade.py`.
- **Speculation rules:**
  - `SPECULATION_RULES` in `performance_build.py` prefetches only `<a>` links matching `/*` and skips `/assets/*`. Eagerness is `moderate`: hover or pointer down on desktop, viewport heuristics on phones.
  - Prefetch runs no script, so Cloudflare Web Analytics and FormSubmit never see a speculative visit. Never switch to prerender.
  - `check_site.py` rejects prerender, eager rules, a missing asset exclusion, malformed JSON, and duplicate blocks.
  - Cloudflare Speed Brain is off for this zone: no `Speculation-Rules` header, and `/cdn-cgi/speculation` returns `{}`. The rules therefore live in the document.

## Verification

- **Static checks:** `build_site.py` and `check_site.py` pass with no errors or warnings.
- **Tests:** 19 Python tests and 46 node tests pass, including the new `test-copy.cjs` and the new gallery, navigation, and careers cases.
- **Browser audit:** 12 routes × 5 widths (360, 390, 768, 1024, 1440) were checked in a Chromium browser pane for overflow, text under 12px, undersized controls, and failed images. No issues were found.
- **Behavior checks in the browser:** each improvement was checked. Clipboard access is denied in the test pane, which exercised the honest failure message.
- **Prefetch:** the embedded test browser has preloading turned off and made no speculative requests, even with an `immediate` rule. A separate headless Chrome was tested on the HTTPS Cloudflare branch preview at 1280px:
  - Hovering the Company link sent one `/company/` request with `Sec-Purpose: prefetch`.
  - The click was served from that prefetch (`deliveryType: navigational-prefetch`).
  - Hovering a screenshot link prefetched nothing.
  - Phone viewport heuristics were not tested.
