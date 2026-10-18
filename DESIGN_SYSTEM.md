# Solarity AI design system

Updated October 13, 2026. Current reference-inspired pass starts from public deployed version 19. The original seven-file system refactor started from version 18.

## Direction

The site presents a consumer product company to investors and strategic partners. Its four store-listed apps provide tangible product evidence; Engineering Max, Management Max, and Marketing Max remain an explicitly identified platform vision. Design should reinforce that distinction.

The visual language combines charcoal, warm solar accents, off-white type, restrained paper surfaces, editorial proportions, and authentic product screens. Authentic product imagery now leads Home and Investors. The conceptual human-progress artwork remains secondary on Company, where genuine people lead. No new decorative website assets, fonts, dependencies, or runtime JavaScript were added. See `REFERENCE_DESIGN_PASS.md` for the current route-by-route implementation map and verification limits.

## Audit and implementation

Every generated route was audited in source before implementation. Browser rendering was unavailable, so findings and verification below do not constitute a rendered visual certification.

| Route | Highest-impact weakness | Implemented response |
| --- | --- | --- |
| Home | Repeated surfaces, oversized mobile selector, fixed 860px panel minimum | Clear hero, compact evidence rail, native product explorer with overlapping grid cells that reserve the largest actual panel, quieter platform and thesis sections |
| Apps | Box-heavy repeated presentation and inconsistent screenshot proportions | Concise directory, alternating editorial desktop rows, consistent genuine screenshot stages, ordered mobile stack |
| Looks Max | Competing typography and enclosure styles | Focused product identity, balanced store actions, numbered feature list, distinct single-screen product story |
| IQ Max | Repeated cards and misaligned paired evidence | Clear opening hierarchy, compact feature narrative, aligned two-screen story with subgrid enhancement |
| Sleep Max | Long introductory composition and inconsistent evidence styling | Fluid headings, a proportionate genuine opening screen, editorial single-screen story, readable wellness context |
| Fitness Max | Dense interface evidence competing with introductory copy | Consistent screenshot scale, paired story, clearly maintained Only Fitness store-name disclosure |
| Platform | Large index cards followed by repetitive module treatment | Compact Build/Operate/Grow index, two-column module explanations, quieter strategy sequence and partnership action |
| Company | Conceptual artwork preceded real people; portraits were undersized | Founder-led opening, larger uncropped portrait, six-person roster, editorial principles, secondary conceptual artwork |
| Investors & Partners | Repeated closing invitation and scattered evidence | Four-app evidence list beside distinct platform vision, concise partnership rows, five native FAQs, one founder booking closer |
| Contact | Numerous conflicting style passes and weak grouping | Composed inquiry workspace, clearer topic controls, optional fields, errors, and distinct review sheet; honest email handoff retained |
| 404 | Unrelated orbital decoration | Direct recovery message and useful destination directory |

Shared findings included 34 stylesheet sources, repeated declarations across successive visual passes, inconsistent radii and type scales, and fragile cross-file override ordering. All 34 legacy CSS sources were removed from the active checkout and remain available in Git history. Seven files now define the maintained system.

## Source responsibilities

| File under `design/system/` | Responsibility |
| --- | --- |
| `foundation.css` | Tokens, reset, semantics, type scale, grids, controls, dialog, shared closing invitation |
| `chrome.css` | Header, active navigation, mobile disclosure and no-JS fallback, footer |
| `home.css` | Home hero, evidence, native explorer, platform teaser, thesis, founder strip |
| `products.css` | Apps directory and all four product detail compositions |
| `company.css` | Company, Platform, Investors & Partners |
| `contact.css` | Contact form, review/error/optional states, 404 recovery |
| `accessibility.css` | Final reduced-motion, forced-color, and print rules |

The declared cascade is `foundation, components, pages, accessibility`. Modify the responsible source rather than appending another override file. The generated presentation bundle and each inline route stylesheet are build outputs.

## Design rules

- Background `#111518`; quiet surface `#191e22`; raised surface `#222a30`.
- Primary text `#f2f0e9`; secondary `#bdc4c8`; supporting `#a6b0b7`.
- Solar accent `#e7c696`; paper `#eee9dd`; dark paper text `#1b272e`.
- Product accent tokens apply to each corresponding route and its related content.
- System sans-serif for reading and controls, Georgia for selective editorial contrast, system monospace for small indices. No downloaded fonts.
- Fluid gutters from 20 to 56px; content maximum 1248px; fluid section spacing from 56 to 104px.
- Base body text 16px with generous line height. Large titles and section headings use bounded `clamp()` scales. Keep long text in readable measures.
- Standard radius 4px; larger image/dialog radius 8px. Borders define structure. Shadows are limited to product imagery and dialogs.
- Primary actions use a restrained pill radius and have at least 52px height; compact navigation and secondary links use at least 44px where appropriate. Do not move entire controls on hover.
- Readable type, whitespace, and section composition provide hierarchy. Do not add continuous decoration, fake dashboards, redundant card shells, animated counters, or hidden-content entrances.

## CSS and browser support

Current official MDN guidance was consulted on October 13, 2026:

- [Cascade layers](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@layer), Baseline widely available since March 2022.
- [Subgrid](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Subgrid), Baseline widely available since September 2023.
- [Container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries) and [container-type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type).

The implementation uses Grid, Flexbox, fluid type, logical spacing properties, and explicit cascade layers. Product story alignment uses subgrid inside `@supports`, with a complete ordinary-grid fallback. `text-wrap: balance` is optional enhancement; normal wrapping remains usable. Dialog and navigation viewport limits declare `vh` before `dvh`. No critical content depends on an animation or a view transition. Container queries were considered; these route-specific compositions are adequately served by their explicit Grid and viewport rules, so no additional containment dependency was introduced.

Responsive source rules cover 360, 390, 768, 1024, and 1440px contexts, including intermediate 560/640/650/850/1050/1100/1150px changes. There is an extra compact header rule through 390px. This is source-level responsive coverage, not measured rendered viewport testing.

## Behavior and delivery guardrails

- Preserve the synchronous navigation script before inline CSS. It establishes mobile layout before first paint and retains the expanded no-JS fallback.
- Preserve the four native explorer radio inputs and their label/panel relationships. Invisible panels retain intrinsic layout space but are not interactive; print exposes all four.
- Keep screenshot links as native image destinations enhanced with the existing accessible dialog. Preserve close, Escape, backdrop, modified-click, unsupported-dialog, and focus-return behavior.
- Keep form input out of URLs until the user deliberately opens the reviewed email draft. Never show a delivered/sent success state. No backend submission is configured.
- Images retain dimensions, genuine uncropped app content, responsive candidates, and updated `sizes` declarations. The Company founder portrait and opening product proof are eager; later conceptual artwork remains lazy.
- The homepage primary authentic product image uses responsive WebP delivery and an exactly matching preload. Company retains optimized conceptual artwork. Route-specific inline CSS and conditional gallery/contact scripts remain intact.
- Reduced-motion mode disables motion. Essential content is immediately visible. Native scrolling and navigation are unchanged.

## Baseline version 19 verification

- `python3 build_site.py`: generated 10 content pages and the custom 404.
- `python3 check_site.py`: all 11 pages, 326 internal links/fragments, and 323 local asset references passed without errors or warnings.
- 19 Python tests passed for CSS optimization and route normalization.
- 32 Node tests passed for navigation, contact logic, and screenshot gallery behavior.
- Independent source review covered narrow layouts, hidden/control states, product contrast pairs, subgrid fallback, and component contracts.
- Observed defects corrected: founder heading-level skip, missing product route accent inheritance, contact error border being overridden on hover, contact enhancement text-height changes, small-header width pressure, and mismatched responsive image-size hints.
- Artifact byte comparison is in `research-assets/design-system-byte-comparison.json`. These are source and gzip-compressed build sizes, not measured HTTP transfers or Lighthouse scores.

The supported browser workflow was unavailable. No browser screenshots, rendered overflow measurements, live keyboard/screen-reader testing, or new Lighthouse/PageSpeed scores were obtained. Earlier 100 scores reported by the founder are historical and must not be represented as current measurements. A browser pass should prioritize five viewport widths, mobile menu open/closed states, all product selections, gallery focus return, FAQ expansion, and Contact invalid/optional/review states.

Existing content dependencies remain: applicable corporate legal policies, verified portraits for three selected members, and verified team-role details. These have not been invented. Hosting-controlled custom headers and immutable caching are declared but were not enforced by the host in earlier HTTP checks.
