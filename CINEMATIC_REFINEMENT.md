# Cinematic refinement, October 13, 2026

This pass addresses the approved 24-point cinematic audit as one design system. The natural-sunrise hero remains the exact founder-approved asset. Product facts, store destinations, the four-app scope, founder identity, selected team, public audience, and Sites origin are preserved.

## Audit dispositions

| Audit finding | Implemented response |
| --- | --- |
| 1. Identity ends at the hero | Warm near-black, ivory, solar accents, lighting, type, and section rhythm now continue across all routes. |
| 2. Generic, inconsistent type | One self-hosted Manrope variable font replaces operating-system display typography and repeated Georgia emphasis. |
| 3. Repeated page compositions | Product-specific openings, a conceptual platform diagram, larger investor evidence, a founder-led company page, and direct contact each have distinct structures. |
| 4. Excessive indices and chrome | Removed redundant numbering, viewer bars, badges, footer arrows, and repeated decorative emphasis. |
| 5. Uniform scale and density | Larger focal elements, quieter supporting copy, and deliberate changes in section density establish hierarchy. |
| 6. Motion lacks purpose | Restrained image movement, product-selection transitions, navigation feedback, and focus states support existing actions. Essential content remains immediately visible. |
| 7. Header separate from hero | The homepage header overlaps the opening artwork with a legible dark fallback; other routes retain stable navigation. |
| 8. Artwork over-darkened | Lighter, directional masking exposes the approved sky, sun, and ascent while protecting text. |
| 9. Mobile artwork arrives late | The solar scene begins at the top of the mobile opening; copy enters below the focal imagery. |
| 10. Repeated app lists and abstraction | Strategy now explains how product experience informs workflow development instead of repeating the portfolio grid. |
| 11. Founder too small | The homepage portrait grows to 300px desktop, 220px tablet, and 160px mobile, with a stronger company composition. |
| 12. Boxed art label | A discreet unboxed caption identifies conceptual artwork. |
| 13. Mismatched product promotions | Complete, authentic store imagery now shares neutral staging and consistent captions. A fully matched set of clean UI exports remains an asset dependency. |
| 14. Document-viewer appearance | Removed screenshot toolbars and source bars. A quiet, accessible Enlarge action retains native image navigation and the existing dialog. |
| 15. Small interfaces | Product screens grow to up to 340px on detail pages, 320px in the portfolio, and 300px in the homepage explorer. |
| 16. Identical product pages | Looks, IQ, Sleep, and Fitness use distinct editorial arrangements without changing their factual content. |
| 17. Mobile imagery buried | Detail-page source order is title, artwork, then supporting copy. A compact Get app jump reaches the store actions directly. |
| 18. Portfolio repeats details | The portfolio is a concise image-led collection; full explanations remain on product pages. |
| 19. Platform lacks a visual | An accessible HTML/SVG diagram clarifies the intended Build, Operate, Grow relationship and explicitly labels it conceptual strategy. |
| 20. Investor evidence too small | Larger authentic product images form a dedicated evidence section with two mobile columns. |
| 21. Inconsistent team profiles | All six approved additional members share an intentional typographic roster. No roles or missing portraits were invented. |
| 22. Careers overly procedural | Authentic founder imagery, clearer role presentation, and a simpler application composition provide human context. Detailed job posters remain linked to the existing official source. |
| 23. Recruiting form friction | Any valid email provider is accepted; LinkedIn and portfolio are optional. Native FormSubmit CAPTCHA and confirmation are retained because receiver activation and AJAX delivery behavior are not verified. |
| 24. Cumbersome contact composer | Direct email, verified booking, and four native inquiry topics replace the draft/review/copy workflow. Product and inquiry context enhance the email subject. |

## Implementation and maintenance

- Shared tokens, typography, controls, navigation, and footer: `design/system/foundation.css`, `design/system/chrome.css`, and `visual_chrome.py`.
- Home composition and native product explorer: `visual_home.py`, `product_explorer.py`, and `design/system/home.css`.
- Product data and store destinations: `build_site.py`, `APPS`. Product composition: `visual_products.py`, `visual_catalog.py`, and `product_story.py`.
- Platform, investor, and company composition: `visual_strategy.py`, `visual_company_upgrade.py`, `visual_sections.py`, and `visual_team.py`.
- Contact destinations and native topics: `visual_contact.py`. Context enhancement: `scripts/contact.js`.
- Careers content/form: `visual_careers.py`. Optional fields, validation, and role preselection: `scripts/careers.js`.
- Font source, license, hash, and subset information: `dist/assets/fonts/font-sources.json` and `OFL-Manrope.txt`. The 26,292-byte WOFF2 is self-hosted, fingerprinted, preloaded, and uses `font-display: optional` to avoid late swaps. No third-party runtime font request is added.

The existing image pipeline retains full images, responsive variants, intrinsic dimensions, and matching hero preload. The homepage keeps its existing 2,798-byte navigation script and has no external JavaScript request. The contact route's JavaScript falls from 17,566 to 5,503 source bytes, including navigation. These are artifact sizes, not measured HTTP transfer or Lighthouse results.

## Verification scope

- 19 Python tests pass for route normalization and conservative CSS filtering.
- 34 Node tests pass for navigation, image dialog behavior, contact context and email encoding, application validation, and role preselection.
- Static checks cover all 12 generated routes, local links/fragments/assets, unique IDs, headings, accessible form labels, native fallbacks, canonical URLs, sitemap, robots, script hashes, font hashes, cache scope, and the approved hero contract.
- Independent source review covers 360, 390, 768, 1024, and 1440px layouts, plus intermediate breakpoints. It identified a careers glow-box overflow and a narrow platform label column; both were corrected before publication.
- Browser rendering, measured layout/CLS, live form delivery, and fresh Lighthouse/PageSpeed results were not tested. The supported browser tool was unavailable, so no alternate browser workflow or preview server was started.

## Remaining dependencies

1. Confirm FormSubmit activation and actual receipt for `careers@solarityai.com`. No test application or activation email was sent by the agent. The visible site explains the provider handoff and provides direct recruiting email; it never fabricates a success state.
2. Supply a matched set of clean product UI exports for a fully unified screenshot art direction. Current store assets remain authentic and unaltered.
3. Supply approved team roles and any additional portraits if richer individual biographies are desired. The current complete roster is ready to use without them.
4. Run rendered desktop/mobile QA and fresh PageSpeed measurements in an available browser before treating the prior 100 scores as reconfirmed.
