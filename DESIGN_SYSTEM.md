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

All values below are tokens on `:root` in `design/system/foundation.css`. `check_site.py` fails the build when a stylesheet bypasses the type, weight, radius, or eyebrow rules, hard-codes a color in a border, outline or shadow, breaks the contrast matrix, or moves a neutral off its color axis.

- **Color (Phase P1, October 18, 2026).**
  - Warm ember neutrals (R ≥ G ≥ B): `--bg` `#0f0d0b`, `--surface`, `--raised`, `--line`, `--line-soft`, `--ink`. Text: `--text`, `--muted`, `--dim`.
  - Solar ramp, each with one job:
    - `--sun-core` is the primary action, the one emphasized word, and focus.
    - `--gold` is links and current state.
    - `--sand` is labels and eyebrows.
    - `--bronze` is rules and control borders, never small text.
    - `--ember` and `--haze` are light only.
    - `--accent` is a legacy alias of `--gold`.
  - Scene tones, "one day of light". Interior pages open at `--tone-blue` under a key light from the upper right (`--key-x`, `--key-y`). Closing bands end in `--light-field` golden light, introduced by the `--horizon` rule. The footer is a dusk bridge into `--tone-footer`.
  - Product worlds (founder-approved): `--{looks,iq,sleep,fitness}-{deep,world,tint}`. Product routes, `[data-product-accent]` and the matching classes set `--world-deep`, `--world` and `--world-tint`.
    - `--world` is only a glow (45% or less), a rim or a stroke, never a fill behind text.
    - Text in a world sits on `--world-deep` or on at most 35% world light. It uses ivory, `--muted` or the tint, never `--dim`.
  - Paper is retired. Evidence uses lit panels (`--elev-panel` with `--elev-panel-edge`). Vision is drawn in outline: transparent, with a dashed `--bronze` border and dashed inner rules.
  - Grain (`--grain`) is an inline SVG noise tile at about 3% opacity, used on the page and on closing scenes. It needs no file and no request.
  - Glows sit on a pseudo-element larger than their box and fade at `closest-side`, so they never show an edge.
- **Type (Phase P2, October 18, 2026).**
  - Two self-hosted faces:
    - Manrope variable does the work.
    - Newsreader, at its display optical size in one 400 roman (27,416 bytes, founder choice A1), carries every `h1` and the chapter headings listed in `foundation.css`. Those are the statements, product names, closes and Platform numerals.
  - Both faces are preloaded with `font-display: optional`. Metric-matched fallbacks keep lines stable:
    - Georgia for Newsreader: `size-adjust` 101.5%.
    - Arial for Manrope: `size-adjust` 103.94%.
  - Arrows come from Manrope through the `Display Arrows` face. Provenance is in `source-assets/fonts/font-sources.json`.
  - Roles: `--type-title` (one title moment per page), `--type-chapter` (display), `--type-section` (Manrope 500, `h2`), `--type-sub` (`h3`), `--type-deck` (ledes), `--type-body` (17–18px), `--type-meta`, `--type-label`, `--type-signature`.
  - Page stylesheets never declare a fluid `clamp()` size. Display tracking is −0.015em or −0.01em, and no large Manrope text is tighter than −0.02em.
  - Emphasis is `--sun-core` on a phrase (`em`, `span` or `.muted` inside `h1` and `h2`), never a face or weight change.
  - Breaks fall only between sentences. `p`, `li`, `dd`, `figcaption` and `.lede` use `text-wrap: pretty`. "iOS & Android" never breaks.
  - The small text scale `--text-2xs`…`--text-xl` remains for labels and supporting copy. Nothing renders below 12px.
  - `check_site.py` enforces:
    - no raw `clamp()` font size outside `foundation.css`;
    - no monospace face;
    - 61,440 font bytes or fewer per route (now 53,708);
    - every heading character inside the display subset.
- **Weights.** 400 for reading, 500 for headings and emphasis, 600 for labels, buttons and `strong`.
- **Eyebrows, now folios (P2 follow-up).**
  - One style: a 32px `--bronze` rule plus a 12px, weight-600, `.12em` caps label in `--sand`.
  - Strings are written in sentence case. CSS applies the capitals.
  - Use at most one per chapter, at four words or fewer, and never repeating the heading or the brand. The site went from 50 to 18.
  - Product names beside their icons are identity, not folios: no capitals, tracking or rule.
- **Numbers.** Only real sequences are numbered: the Platform's Build, Operate, Grow modules, set as display numerals. The FAQ, partnership topics, principles and 404 list have no numbers.
- **Captions.** Every screenshot attribution comes from `provenance()` in `image_provenance.py` ("Official App Store imagery with sample content.") and uses the `.caption` style (12px, `--dim`).
  - Use it once per gallery, wall or viewer.
  - Per-image detail lives in the alt text and in short step captions ("Focus selection").
  - The hero keeps "Conceptual brand artwork". The hero uses a lighter gold for legibility over the artwork. The product-name label beside each app icon is 13px in its product accent.
- **Measure.** Body paragraphs default to `--measure` (52ch, about 75 characters per line in Manrope, whose 0 is wider than its average letter). Wider containers must not stretch reading text past it.
- **Headings.** `text-wrap: balance`. A span that follows a forced `<br>` becomes its own block, so it balances independently rather than stranding a word.
- **Radii.** `--radius-control` 10px (inputs, dialog controls, chips), `--radius-plate` 14px (screenshots), `--radius-panel` 20px (lit panels, stages, portraits, the dialog), `--radius-pill` (buttons), `--radius-icon` 24% (app icons, at every size), and `50%` only for true circles.
- **Buttons.** One 14px label. Standard buttons are 52px high; `.small` is 44px. Store buttons grow only for their two-line content. Arrow glyphs use `line-height: 1` so they never change a button's height.
- **Portraits.** Founder imagery uses `--radius-panel` and `--shadow-portrait` (an alias of `--elev-object`), and stands in a warm key light.
- **Spacing.** Fluid gutters (`--gutter`), content maximum 1264px, fluid section spacing (`--space-section`).
- **Light, not borders, gives structure** (this replaces the October 13 "borders define structure" rule, with founder approval). Elevation is expressed as light: `--elev-panel` for lit panels, `--elev-object` for screenshots and portraits, `--elev-overlay` for the dialog backdrop. Glows must be motivated: behind a focal object, from the one key light. Fake dashboards, animated counters and hidden-content entrances remain out.
- **Buttons (P1).** The primary is `--sun-core` with an inner highlight and a warm bloom on hover and focus. The outline button is a `--control-border` hairline whose hover fill is `rgb(255 207 122 / .08)`.
- **Status chips.** `.status` has a filled sun dot for evidence; `.status.vision` has a hollow ring for vision. Both always carry text.

## Cinematic redesign: Phase P0 status (October 18, 2026)

`CINEMATIC_PREMIUM_PLAN.md` is the approved-for-review plan; its "Required corrections" section overrides the plan text. Until the founder decides the items below, the design rules above stay in force and no page changes.

- **Founder specimen:** `research-assets/specimen/founder-specimen.html`. It is local and never deployed. Open it from the file system in a desktop browser. It shows the three display-face options (A1 Newsreader, A2 Instrument Serif, B Manrope 300) on the Home hero, the Investors opener and a product opening; the four product color worlds on real screenshots with live contrast figures; and the header floating over the sunrise at 1440 and 390. The candidate faces load from Google Fonts for review only. Production would self-host a measured subset (plan §3.1 and corrections 3 to 5).
- **Founder decisions (October 18, 2026):**
  - Display face: **A1 Newsreader**. This reverses the October 13 one-family rule. Phase P2 subsets and self-hosts it under the plan's corrections 3 to 5 (KiB budget, Latin Extended-A and arrows, Reserved Font Name check).
  - Product world hues: **approved as shown** in the specimen. Looks Max violet, IQ Max blue, Sleep Max indigo, Fitness Max ember.
  - Home header: **approved to float over the hero** (Phase P3). Interior pages keep a solid bar.
  - Phase P1 (light, color and materials) is implemented: see the rules above and the P1 pull request.
  - Phase P2 (type system) is implemented: see the Type rule above.
  - The P2 follow-up (folios, numbering, captions) is implemented: see the rules above.
- **Still open:** the motion contract (plan §5, Phase P9), and the portfolio wall replacing the Home explorer (Phase P5b).
- **Founder material:** plan §9 lists every asset and content item needed. None of it is invented in the meantime.
- **Baseline renders:** `research-assets/baseline-2026-10-18/` holds full-page captures of https://solarityai.com (develop `b0eff9b`). It covers all 12 pages at 360, 390, 768, 1024 and 1440, plus Home and Investors at 1280x800 and 1920x1080, and a reduced-motion pass at 390 and 1440. `index.json` records each page height; none overflows horizontally. The JPEGs (about 21 MB) are kept out of git; only `index.json` is committed. Regenerate them with `node research-assets/baseline-2026-10-18/capture.mjs https://solarityai.com <folder>`.
- **Lighthouse baseline:** recorded in `PRODUCTION_AUDIT.md`.

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
