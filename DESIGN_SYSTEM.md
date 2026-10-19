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
| `home.css` | Home opening and credits row, portfolio wall, platform teaser, thesis, founder strip |
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
- **Header (P3).**
  - Interior pages: an opaque `--bg` bar from first paint with a `--line-soft` hairline and no blur.
  - Home:
    - `navigation.js` adds `html.header-over-hero` in the head when the visit starts at the top with no `#fragment`.
    - An IntersectionObserver (220px root margin) turns the bar solid before the hero's credits row slides under it, and transparent again at the top.
    - Without JavaScript or IntersectionObserver, and while the mobile menu is open, the bar is solid.
    - The class is listed in `DYNAMIC_CLASSES`.
  - The hero's top scrim keeps nav and Contact text at 4.9:1 or better against the brightest sky behind them (measured at 1920, 1440, 1280, 1024 and 390).
  - Wordmark: Manrope 600 at 16px, +0.06em, with "AI" in `--sand`.
  - Nav links: 14px. A sun-core hairline draws under hover, focus and the current page.
  - Contact is a ghost button (gold label, `--control-border`). On phones it becomes a compact text link beside a borderless menu icon.
  - The mobile menu is a full-height scene of display-face links over a dawn glow.
- **Home opening (P3).**
  - Height is `clamp(640px, 100svh, 960px)`. The title is two lines ("Building for / human *potential.*"), followed by the deck, Investor inquiries (primary) and Partnership inquiries (ghost).
  - Bottom edge: a credits row of the four app links, "Four apps · iOS & Android" and "Explore the portfolio ↓". An amber afterglow runs into the next scene.
  - Warm umber scrims clear by half the width, and a soft shadow carries the title over bright sky.
  - Phones: a 560px art strip, the title on its lower fade, and the caption on a chip.
  - The hero `sizes` (`(max-width: 560px) 1233px, 2113px`) matches the AVIF preload exactly.
- **Close (P4).**
  - Every corporate page ends once, with `closing_scene()` in `visual_home.py`: a chapter-scale statement and two standard actions, Investor inquiries and Partnership inquiries. Platform leads with Partnership inquiries.
  - The scene supplies its own padding: 108–112px or less before the statement at 1440 and above. The dawn glow (`--light-field`) fades out before the scene's edge, so it dissolves into the footer with no step.
  - Contact links in `main`: Home has 4 and Platform 3.
  - These repeats were removed: the strategy closing row, the three per-module "Discuss X Max" links and the "Discuss the platform direction" pill.
- **Action labels.** Investor inquiries, Partnership inquiries, Book a conversation, Email Ata.
- **Footer (P4).**
  - No slogan. Three directories under caps labels: Portfolio (the four apps), Company and Contact (Investor and Partnership inquiries, Email Ata ↗, Book a conversation ↗ opening in a new tab).
  - Signature: the sun mark (192/320px lossless crops of the official lockup, made with the favicon crop and committed under `dist/assets/brand/`) and SOLARITY AI, sized in container units. It spans 99.9% of the wrap at 1024, 1440 and 1920 and sits on an ember glow.
  - One legal line, plus the App Store and Google Play trademark notices.
  - On phones the footer is 631px (0.75 of an 844px viewport is 633), and every target is 44px or taller.
- **Product assets (P5a).**
  - Screenshot derivatives trim baked-in listing hairlines: per side, the smallest inset (16px at most) whose outer 8px lines match the interior within 30 levels. The crops are recorded in `research-assets/image-optimization.json`. The originals in `dist/assets/` are unchanged.
  - `check_site.py` rejects any derivative whose outer band (8px at source scale) differs from the interior by more than 40 levels.
  - Screens stay WebP: at matched size AVIF measured softer on UI text.
  - Icons gain 224w and 320w.
  - Official store badges sit in `source-assets/badges/`, with provenance in `research-assets/store-badges.json`. They are published once P5b references them.
  - **Native re-fetch:** `refetch_native_screens.py` fetched all ten published screenshots at 1284×2778 from the same official listing URLs into `source-assets/native/`, which is git-ignored.
    - The founder confirmed them on 2026-10-19. The published originals are now the natives as WebP q95, about 139 KiB each, so full-size views are crisp.
    - Derivatives are 400, 800 and 1200w.
    - All ten match the published files (mean difference 1.3–2.2 levels; 99th percentile 22 or less).
    - Checksums are in `research-assets/native-refetch.json`.
- **Product stage and openings (P5b).**
  - The stage is a pool of world light behind the real image, masked at `closest-side`, so no box edge shows. Every screen sits on the same plate (`--radius-plate`, `--elev-object`, world-tint rim).
  - Product pages:
    - Title = the product name, with the slogan as a display-face deck.
    - A 104px icon with a world glow.
    - The official badges (`visual_stage.store_badges`) directly under the copy. Each ↗ sits outside the badge's clear space.
  - The opening screen is a 3:4 window (`.plate--window`) aimed by each product's `crop_focus` below the poster headline, 420px on desktop. Enlarge opens the full native image.
  - Measured on every product page: badges end by 819px at 1440×900 and by 649px at 390×844. Every opening screen loads a source at least as wide as its rendered width × DPR.
  - Product-specific:
    - IQ opens on its straight focus-selection frame.
    - Sleep is one centered night scene.
    - Sleep's empty-profile frame is retired to `source-assets/`.
    - The status dot and the "Get X ↓" link are removed.
  - Pages end with `product_close`: icon, statement, badges and one inquiry path, in the product's world light, which fades inside the scene.
  - Open item: every official IQ frame is light cyan, so IQ's screen is still the brightest surface in its first viewport. A darker official UI export is requested from the founder.
- **Home wall and Apps lineup (P5b-2).**
  - Home shows all four apps at once, as world cards. Each card has a 3:4 window aimed by `crop_focus`, a 56px icon and the name in the display face, one link to the product page, and an App Store / Google Play pair. Phones show a 2×2 grid, and the store links stay on the product pages.
  - Measured:
    - 1440×900: the four cards span 555px and fit in one view.
    - 1280×800: they span 523px.
    - 390×844: the wall ends 915px below its heading (limit 928px, 1.1 viewports).
  - The Home header turns solid before the hero's credits row slides under it (220px root margin).
  - Apps opens with a lineup of the four 112px icons on world glows. The lineup is the in-page navigation.
  - Each app follows as a world band on alternating sides: a 64px icon, the name at chapter size, a deck summary, the official badges (with the Only Fitness disclosure once) and "Explore X →".
  - Screens are 3:4 windows capped at 340px, or 55svh on phones. Images no longer open the viewer, and the status dot is gone.
- **Investors narrative (P6a).**
  - The opening puts the title beside its lede, actions and page index. The four store-listed apps follow as a lit showroom: a 3:4 window aimed by `crop_focus`, icon, name and category, one link to the product page, and an App Store / Google Play pair.
  - Measured: all four frames are fully visible at 1440×900 (lowest at 854px) and 1280×800 (781px, with smaller windows below 860px of height). At 390×844 the frames become a keyboard-operable rail, and its first plate shows 211px in the first view.
  - The fact band (`#at-a-glance`) states only verified facts: the company and city, the founder's name and portrait, and the number of apps listed on both stores, counted from APPS.
  - Two registers: **Today** is a lit card with the four icons and a filled evidence status; **Ahead** is a dashed card with the hollow `.status.vision` ring and a link to Platform. Vision never borrows the evidence styling.
  - The close pairs the founder booking (times as the primary, email as the outline) with the one reprise of the approved sunrise on this page, captioned "Conceptual brand artwork".
  - Every chapter heading on the page uses the display face. Section glows fade in from transparent on every edge, so no band shows a seam.
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
  - Phase P3 (opening frame and header) is implemented: see Header and Home opening below.
  - Phase P4 (closing frame, footer and CTA hierarchy) is implemented: see Close and Footer below.
  - Phase P5a (product asset pipeline) is implemented. The founder confirmed the native screenshots on 2026-10-19, so they are published (see Product assets below).
  - Phase P5b is implemented: product openings, stage, badges and product close (P5b-1), plus the Home portfolio wall and the Apps lineup (P5b-2).
  - Phase P6a (Investors: fact band, evidence and vision registers, booking close) is implemented. P6b (the platform diagram) follows.
- **Still open:** the motion contract (plan §5, Phase P9).
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
- The Home portfolio wall lists the four apps in APPS order, each with its icon, one link to its page and both store links (`check_site.py` enforces this). It replaced the native explorer in P5b.
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
