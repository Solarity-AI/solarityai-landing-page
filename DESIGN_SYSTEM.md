# Solarity AI design system

Updated October 13, 2026. Current reference-inspired pass starts from public deployed version 19. The original seven-file system refactor started from version 18.

## Direction

The site presents a consumer product company to investors and strategic partners. Its four store-listed apps provide tangible product evidence; Engineering Max, Management Max, and Marketing Max are real web apps, each shown with its own status, and their mobile versions are a stated plan. Design should keep evidence and plans visibly distinct.

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

Shared findings included 34 stylesheet sources, repeated declarations across successive visual passes, inconsistent radii and type scales, and fragile cross-file override ordering. All 34 legacy CSS sources were removed from the active checkout and remain available in Git history. Eight files now define the maintained system (`careers.css` joined later).

## Source responsibilities

| File under `design/system/` | Responsibility |
| --- | --- |
| `foundation.css` | Tokens, reset, semantics, type scale, grids, controls, dialog, shared closing invitation |
| `chrome.css` | Header, active navigation, mobile disclosure and no-JS fallback, footer |
| `home.css` | Home opening and credits row, portfolio wall, platform teaser, thesis, founder strip |
| `products.css` | Apps directory and all four product detail compositions |
| `company.css` | Company, Platform, Investors & Partners |
| `contact.css` | Contact page (direct email and booking links, topic choices), 404 recovery |
| `careers.css` | Careers page, role cards and the application form with its error states |
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
  - Phones: a 560px art strip and the title on its lower fade. (The caption chip was removed on 2026-10-19.)
  - The hero `sizes` matches the AVIF preload exactly. It is now `(max-width: 560px) 680px, 2113px`.
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
- **App factory map (P6b).**
  - Superseded on 2026-10-19: the map is now `platform_map(apps, saas)`, appears on Platform only, and its nodes are the three web apps with their real statuses. As first built, `platform_map(apps, variant)` in `visual_sections.py` was shared by Platform and Home. The store-listed apps are the lit source on a horizon with the evidence chip. Build, Operate and Grow are dashed vision nodes, each with `.status.vision`. Connectors are dashed and decorative: they read as informing the direction, never as integrations.
  - One legend per map replaces the scattered retractions: the two chips, then "Conceptual company strategy." with the existing note. The figcaption also holds a screen-reader sentence naming the apps and the three directions.
  - On Platform the icons link to the apps and the nodes to the module sections. On Home the map is illustrative, and the section keeps its one "Explore the app factory →".
  - Phones get a compact vertical map: the icons above a glowing line past three outlined nodes. It measures 345px, 41% of a 390×844 viewport (limit 60%).
  - Platform's opening is top-aligned, with the vision chip under the lede. Its legend ends at 674px at 1440×900 and 662px at 1280×800, inside the first view.
  - Modules are numbered chapters: a display numeral, the name in the display face, the vision chip, and an outlined, decorative stage word (`--type-stage`, `aria-hidden`). On phones the numeral sits above the name. Modules carry no contact links.
  - Platform has one numbered sequence, the modules. The three-step argument lives only on Platform, keeps its order without numerals, and no longer repeats the Build ↓ Operate ↓ Grow ↓ links.
  - Measured mean luminance: evidence is brighter than vision on every page (Platform map 55.7 vs 41.8, Home map 57.0 vs 41.0, Investors Today 33.1 vs Ahead 32.3).
  - `check_site.py` requires the map on Home and Platform, the Vision chip on each node, and the legend.
  - Deferred: pinning the map beside the scrolling modules with an active-node glow belongs to the motion contract (P9). The headline rewrites marked *(copy)* still wait for founder approval.
- **Web apps (October 19, 2026).** The founder added Engineering Max, Management Max and Marketing Max to the portfolio as live web apps. This supersedes the P6b vision nodes.
  - `saas_products.py` holds their names, stages (Build, Operate, Grow), statuses, taglines, facts and screens. Each statement comes from the product's own site (`research-assets/saas-evidence.json`). Pages show a status chip in the evidence register ("Web app · private testing", "Web app · free plan", "Web app · internal V1"). Only the mobile versions carry the hollow vision chip ("Mobile versions are planned.").
  - Screens use the `web` image role (WebP at 640, 960, 1440, 1920 and 2560, ending at the screenshot's own width) inside `.web-window`, a quiet browser frame that names the product's address. Screens taller than they are wide get `.web-window--tall`, capped at 500px on Platform.
  - Home: after the consumer wall, the app factory section shows the three web apps as cards. Each card has a 16:10 window, the stage word, the name in the display face, the category, the tagline, the status and "Visit site ↗", and the card links to its Platform chapter. The map no longer appears on Home.
  - Platform: the map's nodes are solid hairline panels with each product's stage status, and the legend says the lines show where the work comes from, not data integrations. Each web app has a numbered chapter with the category, name, status, tagline, summary, facts, availability, "Visit <domain> ↗" and its real screens with a caption. Chapters alternate sides and stack on phones.
  - Footer: the portfolio is two groups, Mobile apps (four) and Web apps (three, linking to their Platform chapters). Desktop shows four columns; phones show a 2×2 grid.
  - `check_site.py` requires the three Home cards in order with their screens and links, the three Platform chapters with a screen and a link to their own site, a status on every map node, and the three web apps in every footer.
- **Home hero (October 19, 2026).** The founder removed the "Conceptual brand artwork" caption, and `check_site.py` now fails if it returns. The grade is CSS only, so the approved pixels are untouched: film grain, a warm bloom at the sun and a soft edge vignette. The build master is the approved artwork upscaled 2× to 3720×1690 with Real-ESRGAN x4plus (founder-approved; `research-assets/solar-ascent-artwork.json`). Variants run from 480 to 3720. A 2× desktop now loads 3720, at 1.07 device pixels per image pixel instead of 2.13. A 3× phone loads 2560 (1.44 instead of 2.0), and a 2× phone keeps the same 1860 file (the phone `sizes` is 853px for that reason). Lighthouse mobile is unchanged for the hero (the same 1860 AVIF, 128 KB). The Home web app cards add about 150 ms of lab LCP (3,010 to 3,160 ms) through their three 640px screens, which are lazy and low priority.
- **Ten improvements (October 19, 2026).**
  - The web apps appear on every portfolio surface. Apps ends with a "Web apps" band, and the Investors showroom adds a compact row after the four framed apps. Both reuse `saas_cards()`, so Home, Apps and Investors render one card design. Contact's topics and the 404 recovery list name them too.
  - Platform's web app screens open in the screenshot viewer, with previous and next. Each link keeps the full-size image as its native target and passes its own `data-image-caption`. The viewer falls back to the default line, so the mobile-app galleries are unchanged.
  - Link previews: `make_social_images.py` composes 1200×630 images from approved material only (the hero master, the official icons and screens, the web app screens, the sun mark and the site fonts). There is one per app, plus Apps, Platform, Investors and a default. It writes them to `source-assets/social/`, and they are committed and published on reference. Every page sets `og:image` width, height and alt, `og:site_name` and `twitter:image`.
  - Structured data: an Organization node on every page. Home adds a WebSite; each app page adds a MobileApplication with its store links and a BreadcrumbList; Apps adds the list of apps; Platform adds the three WebApplications. No ratings, prices or store categories are stated.
  - Security headers: a Content-Security-Policy built at build time. Each inline script that runs is allowed by its SHA-256 hash, so the policy can't go stale. The policy also allows only the Cloudflare analytics beacon and the FormSubmit form action. Alongside it: HSTS (one year, no subdomains) and Permissions-Policy. No COOP: its process swap breaks Lighthouse and PageSpeed Insights traces (NO_NAVSTART), and the site opens no cross-origin popups. `check_site.py` fails on an unhashed inline script, a script wildcard, or a missing header. Measured: no violations on any of the 12 routes, with navigation, the menu and the gallery working.
  - Typography: every section heading uses the display face (Apps, product, Platform, Company, Careers and Contact sections) at its section size, weight 400.
  - Motion: scroll reveals rise 36px into place as content enters, driven by the scroll position rather than a timer. They run only under `prefers-reduced-motion: no-preference` and `@supports (animation-timeline: view())`. Content already on screen is complete, and the hero is never animated. They move only, so text keeps full contrast in every state; an opacity fade dropped Lighthouse accessibility to 96 for text not yet scrolled to. `check_site.py` fails on keyframes or scroll timelines outside the guard, and on any hero animation.
  - Footer wordmark: a "Signature Fallback" face (Arial at 93.6%) keeps the uppercase wordmark inside the wrap before Manrope loads. Measured at 1440: 1,071 px with Manrope and 1,071 px with the fallback, where Arial at the body fallback's scale was 1,184 px and clipped.
  - The 404 page keeps the site grid (title at the 88 px gutter at 1440); only its recovery list is narrowed.
- **Mobile performance (October 19, 2026).**
  - `content-visibility: auto` on every section of `main` after the opening, and on the footer. Below-the-fold content skips style and layout until it nears the viewport, and the remembered size keeps scrolling stable. In-page jumps still land below the header (measured: top 112 px on Investors, Platform, Apps and Home).
  - Not on `.conversation-band`: content-visibility clips paint to the box, and the closing scene's glow spills past its centred wrap by design (it showed hard vertical edges). The footer is full-width, so it clips nothing.
  - The Home hero declares 680 px for phones, which sets the file the browser picks, not the drawn size. A 3× phone still loads 2560, 2.625× loads 1860, 2× loads 1440, and Lighthouse's 1.75× phone loads 1200 (68 KB instead of 128 KB).
  - Measured locally (Lighthouse 13.5 mobile, A/B against `develop`, 2 runs): Home style and layout 444–522 → 202–208 ms, blocking time 137–178 → 0–7 ms, LCP 3,084 → 2,635 ms, local score 92–93 → 97. CLS and accessibility unchanged (0, 100). The local server sends uncompressed HTML (74 KB against 18 KB brotli in production), so the local LCP runs about 0.4 s above PageSpeed's.
  - Rejected after measuring: a phone-only crop of the hero (`<source media>` with per-media preloads) made LCP 300 ms worse and FCP 150 ms worse than the size cap. Dropping the font preloads raised FCP by 400 ms.
- **Design pass (October 19, 2026).** Ten changes, with no new copy apart from the Company founder paragraph, which now names the web apps instead of "an app factory vision".
  - **Panels replace plain three-column text.** Product features, Company principles, Platform's three steps and Careers benefits use `--elev-panel` panels with `--elev-panel-edge`, `--radius-panel` and a 14–22 px gap.
    - Product features take the product's world: a glowing 52 px icon tile (`color-mix` of `--world`), a quiet display numeral in `--world-tint`, and a world glow inside the panel.
    - Principles are numbered in the display face; headings reserve two lines so the paragraphs align.
    - Platform's steps are unnumbered (the web app chapters own the page's one numbered sequence) and joined by a horizon line at a sun dot.
  - **Platform callout.** "People remain responsible for the decisions" is a pull-quote: a sun-core left rule, a warm fade, the display face, at most 820 px wide.
  - **Icon tiles.** Contact topics and Careers benefits carry 48 px sun-core tiles. New icons: invest, partner, apps, message, share, globe, spark, in the existing 24 px stroke set (`visual_sections.symbol`). In Careers the icon sits inside the `<dt>`, which keeps the description list valid.
  - **Company founder.** A 4:5 editorial print, at most 440 px wide, in a 0.8 / 1.2 grid. The card no longer repeats "Connect with Ata"; the column's button is the one action.
  - **Platform chapter index.** A sticky pill under the header lists Build, Operate and Grow with each product; chapters scroll to 176 px below the top so they clear it. On phones it is three static columns.
  - **Investors FAQ.** The questions are numbered in the display face; the open question's number turns sun-core over a warm fade.
  - **Hover.** On pointer devices with motion allowed, cards and panels lift 4 px and catch a sun hairline. The lift uses `translate`, which composes with the scroll reveal's `transform`.
  - **Typography and brand.** Headings use `text-wrap: balance` and paragraphs `text-wrap: pretty`. Text selection is sun-core on ink, and the scrollbar and form accents follow the palette.
  - **Measured (local Lighthouse mobile, A/B against `develop`).** Product page, Company, Platform and Contact hold 99–100, CLS 0, accessibility 100. Home's local FCP rises 150 ms, a local-server artifact: `develop`'s own Home padded by 1 KB of comment shows the same 150 ms. That server sends the HTML uncompressed (75 KB), while production sends 18 KB.
- **Website pass (October 19, 2026).** Ten improvements found by a Lighthouse audit of every production route, plus checks of delivery, standards and accessibility.
  - **Right-sized screens.** `SCREEN_WIDTHS` adds 260 and 600. 260 is the smallest width at which every screen passes the edge check: 240 measured 41 against the limit of 40. `sizes` now match the measured drawn widths: Home wall 31vw on phones (drawn at 119 px), Investors showroom 47vw (180 px), Company founder print 440 px.
  - **LCP priority.** The first Investors showroom frame and the Company founder print load with `fetchpriority="high"`.
  - **Below-the-fold images yield.** The Home wall's screens load with `fetchpriority="low"`, so they never compete with the hero.
  - **Store badge.** The official Google Play badge is served as 181 px and 362 px WebP (resized only) instead of the 646 px PNG. The PNG master stays in `source-assets/badges/`.
  - **FAQ structured data.** Investors adds a `FAQPage` built from the same `ux_content.FAQ` list the page renders, so the two can't drift.
  - **Home-screen icons.** `make_app_icons.py` writes the official sun mark on charcoal as `apple-touch-icon.png` (180 px) and `icon-192.png`. No web manifest: fetching it during load cost Lighthouse 70 ms of LCP on every page (measured, then removed).
  - **security.txt.** `/.well-known/security.txt` (RFC 9116) names the founder's email and GitHub private vulnerability reporting. Its `Expires` is fixed at 2027-10-19, so renew it before then.
  - **High contrast.** Under `forced-colors`, every panel, icon tile, the Platform index and the pull-quote keep a `CanvasText` outline.
  - **More contrast.** `prefers-contrast: more` raises `--muted`, `--dim`, `--sand` and the hairline tokens.
  - **Keyboard parity.** A card holding keyboard focus lifts and lights like a hovered one (`:has(:focus-visible)`), with motion allowed.
  - **Measured (local Lighthouse mobile, A/B against `develop`).** Investors LCP 3,250 → 2,490 ms and score 93 → 97. Home LCP 2,785 → 2,638 ms and 96 → 97. Apps and Company unchanged. CLS 0 and accessibility 100 throughout.
- **QA pass (October 19, 2026).** Coverage:
  - A static crawl of `dist/`: links, anchors, IDs, ARIA references, headings, metadata and JSON-LD.
  - The 14 external links.
  - A browser sweep of all 12 routes at 10 widths from 320 to 1920.
  - axe-core 4.14 (WCAG 2.2 AA plus best practice).
  - A keyboard focus walk, and the WCAG 1.4.12 text-spacing test.
  - The menu, screenshot viewer, contact links, copy button and careers validation, with the form provider blocked so nothing was sent.
  - A read of every page's copy.

  Fixed:
  - **Apps summaries on phones** were cut to one line with an ellipsis. They now wrap in full.
  - **Investors FAQ heading.** A non-breaking space in "A few useful answers." ran it 71–100 px past its column at 1024 px and wider.
  - **Investors booking heading.** The image track took a fixed 600 px, so "Compare perspectives with the founder." overflowed its column by 84 px at 1024 and 10 px at 1280. The track is now `min(600px, 50%)`.
  - **Product titles** no longer use `nowrap` on desktop. Every name still fits on one line from 851 px up, and under text spacing "Fitness Max" wraps instead of running into the phone art.
  - **Platform index at 320 px.** "Management Max" overflowed its cell by 7 px. Phones up to 360 px get tighter cell padding.
  - **404 description** went from 34 characters to a full sentence.
  - **App factory map status.** `capitalize()` turned "internal V1" into "Internal v1". Only the first letter is raised now.
  - **Serial comma** added in the lists that lacked it (meta descriptions, the web app intro, and the Engineering, Management and Marketing Max facts), matching the rest of the site.

  `check_site.py` now fails on a non-breaking space inside an h1–h3, and on `text-overflow: ellipsis` anywhere but the browser-frame address label. No axe violations, and every interactive check passed.
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
  - Phase P6 is implemented: the Investors narrative (P6a) and the shared app factory map with the Platform modules (P6b).
  - The three web apps joined the portfolio on 2026-10-19 (Home, Platform, Investors, footer): see Web apps above.
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
