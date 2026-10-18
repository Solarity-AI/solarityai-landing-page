# Solarity AI: cinematic and premium redesign plan

Prepared October 18, 2026. This document is a plan only; no design change has been made yet.

## How this was produced

- Every route was captured in headless Chrome at 1440x900 and 390x844: 140 viewport slices across 12 pages.
- 8 reviewers audited those screenshots and the source, each through one lens: home, product pages, corporate pages, chrome and conversion, typography, color and light, motion, and investor persuasion.
- A skeptic re-checked each reviewer's findings against the evidence. 168 findings were kept and 1 was refuted.
- The kept findings were merged into 96 distinct problems in 10 themes: 4 critical, 32 high, 47 medium and 13 low.
- 3 independent directions were proposed: solar cinema, private-bank editorial, and product as protagonist. A judge scored them and wrote the plan below.
- A final critic reviewed the plan. Its required corrections appear in the next section and override the plan wherever they conflict.

No product capability, metric, logo, testimonial or image is invented. Anything that needs new material is listed under founder-supplied material.

## Executive summary

I merged 168 verified findings from 8 lenses into 96 distinct problems in 10 themes: 4 critical, 32 high, 47 medium and 13 low. 13 of them need material from the founder. The site is competent but reads as average for one reason above the others: the approved sunrise is its only cinematic idea, and it is used once. About 800px down, every page becomes the same flat near-black canvas. Each page then repeats the same recipe: a gold eyebrow, a tightly tracked two-line Manrope headline at weight 500, a grey 16px paragraph, hairline lists and two gold pills. The strongest proof, four real shipped apps, appears as soft 300-340px store ads in clashing art directions inside an inert brown box. The founder appears as a reused white studio headshot with no statement of his own. The six team members are names only. Every page ends on the same unlit CTA band, followed by a second sign-off.

Recommended order of work: (1) Foundations. Build a light and color token system sampled from the hero, rebase the neutrals on a warm axis, build a solar accent ramp and per-product color worlds. Choose a display voice from a founder-approved specimen, fix the scale, tracking and deck tokens, and write a motion contract. Review every value in rendered 1440px and 390px screenshots. (2) Opening frame. Make the header transparent over the sky, set the hero to 100svh with a designed bottom edge, lighten the scrims, and set the headline as two lines. (3) Products. Build lit product stages, add per-asset edge crops, re-fetch the screenshots at native resolution, replace the duplicated home lists with a single portfolio wall, use official store badges, and give each product page a signature chapter. (4) Investor narrative. Add a verified fact band, give evidence and vision distinct visual registers, and redraw the platform as a dark, product-rooted diagram. (5) Endings and chrome. Build one closing horizon scene, a compact footer, a CTA hierarchy and calmer mobile chrome. (6) Motion, as a finishing layer: an arrival sequence, scroll reveals guarded by @supports and reduced-motion, and view transitions.

Decisions taken where findings conflicted:
- The recognizable sunrise appears in the hero plus at most one reprise. Other pages use CSS light or a tiny pre-blurred derivative of the art.
- The founder portrait is cropped, framed and vignetted only. Any grade needs founder approval, and the background is never replaced.
- No partial team portraits and no monogram plates until all six members have approved roles and photos.
- A sticky chapter rail is optional. A progress hairline comes first.

Founder materials needed:
- a higher-resolution hero master
- matched clean product UI exports
- a populated Sleep Max screen
- a first-person founder statement, signature and profile link
- an editorial founder portrait
- team roles and portraits
- verifiable metrics and dates
- the vector logo and a wordmark decision
- privacy and terms links

No product claims, metrics or UI are invented anywhere in this plan.

## Why the site reads as average (root causes)

- Earlier passes were never reviewed in a rendered browser. DESIGN_SYSTEM.md:13 says routes were 'audited in source' with 'Browser rendering was unavailable', and CINEMATIC_REFINEMENT.md:52 says the same. As a result, the light was specified at 1-13% alpha and never reached the screen, and word collisions, orphaned words, baked edge artifacts, header seams and dead bands all shipped unnoticed.
- The design-system guardrails forbid the tools a cinematic site needs. 'Borders define structure', shadows only on imagery, 'Do not add continuous decoration', a ban on hidden-content entrances, and motion limited to feedback (DESIGN_SYSTEM.md:62-63, REFERENCE_DESIGN_PASS.md:32) leave only hairlines and hover nudges. The October 13 pass removed inconsistency by removing contrast: one face, one weight, one accent, one surface.
- Checklist passes replaced art direction. The 24- and 30-item audits fixed individual items inside one safe template (gold eyebrow, two-line couplet headline, grey paragraph, hairline list, two pills). Pages therefore differ in their wording, not their scenes, and no page has defined scene types, a hierarchy crescendo or a distinct opening and ending.
- The hero is the only atmospheric asset, and nothing extends its light. No light tokens, product color worlds or deliberate tonal ramp exist, so every scene after the first fold reads as default dark mode. The 1860x845 master also limits how the art can be scaled or reused.
- Product evidence rests on 600px App Store marketing posters in four clashing art directions with baked edge artifacts. Staging was neutralized (one brown box, pastel accents) instead of designed, and the matched clean UI exports have been an open dependency since October 13.
- Hedging and repetition stand in for hierarchy. Verified facts are set in 12-13px dim type, the vision gets the brightest surfaces and product-style affordances, disclaimers repeat under every image and vision block, and CTAs and arrows repeat, so the investor path (proof, vision, founder, ask) is never staged.
- Gaps in founder-dependent content are covered with type. With no founder statement, team roles, portraits, metrics or high-resolution masters, the layout enlarges names, slogans and empty sections, and the result reads as placeholder.
- The system grew pass by pass instead of from tokens: 66 one-off clamp() sizes, seven label tracking values, hard-coded green-grey and bronze border hexes, three radius languages, four numeral styles and three caption wordings. Discerning viewers sense this as 'not quite designed'.

## Required corrections from the final review

Critic verdict: The plan is strong and nearly complete. Every critical and high register id maps to a phase, no claims, metrics, logos or UI are invented, the sunrise hero is kept, and the contrast figures I spot-checked are right: bronze on --bg is 4.62:1, dim on --bg 7.44:1, ink on sun-core 12.57:1. The Manrope byte figure (26,292) and the gzip baselines (HTML 8.8 to 15.7 KiB, inline CSS 5.7 to 9.1 KiB) also match dist/. It is not ready to implement as written. Two motion specs conflict or misbehave: two animations drive the same transform on the hero image, and the view-timeline reveals leave content dim at rest. The font budget is broken by the plan's own cap. The display-face subset omits the Turkish characters the site uses. Product-world colors have no text-contrast rule (ivory on Fitness ember is 2.77:1). The store-badge ↗ exemption weakens a CLAUDE.md convention without need. Two fold-fit acceptance targets are not feasible at 1280x800 or on the 390px wall. Several smaller items are missing or inconsistent: the @layer order update, the header state while the mobile menu is open, the OFL Reserved Font Name check, a founder face near the top of Investors, and the vision row inside the evidence ledger. None of these needs founder material to fix.

1. **inconsistency**: §5 gives .progress-hero-image two transform animations: 'Hero settle' (scale 1.05 to 1 over 1600ms) and 'Hero depth' (scroll(root) translateY 0 to 8%, overscaled to 1.1). Two animations on one property do not combine. The later one in the animation list overrides the other, so either the settle or the drift disappears. The 1.1 overscale also conflicts with the settle ending at scale 1.
   - **Correction:** Split the two across elements. Put the scroll-linked translate and the 1.1 overscale on the <picture> wrapper, and the one-shot settle (scale 1.05 to 1, relative to the wrapper) on the <img>. Alternatively use animation-composition: add on one element and verify it in Safari. State in P9 acceptance that the image edges are never exposed at scrollY 0 and at 100vh, at 390px, 1024px and 1920px.
2. **risk**: The 'Reveal: rise' spec (animation-timeline: view(); animation-range: entry 5% entry 40%; opacity 0 to 1) is measured against each element's own height. For a block 600px or taller, any text in the lower part of the viewport stays partly transparent while the visitor is stopped there. That contradicts 'content is visible once in view'. It also makes the P9 acceptance 'reduced-motion renders match motion renders within 0.5%' impossible for any capture taken mid-scroll, because scroll-driven animations never finish.
   - **Correction:** Apply reveals only to small atomic blocks: a plate, a ledger row, a tile, a heading group of 300px or less. Never apply them to whole sections or body paragraphs. Use a range of entry 0% to entry 100%, capped by the cover range, so the animation completes within about 200px of travel. Start opacity at 0.3 or higher for any text-bearing block, or reveal text by transform only. Change the P9 acceptance to compare captures at fixed scroll positions where each revealed element is at least 30% past entry, plus a full-page capture after scrolling through the page and back.
3. **constraint violation**: The font budget is internally inconsistent. Manrope is 26,292 bytes (measured) and the display face is capped at 34 KB, which totals 60.3 KB if KB means 1000 bytes. That exceeds the plan's own '60 KB or less per route' budget, so the check_site budget would fail or need fudging.
   - **Correction:** State the units as KiB and set the budget to 60 KiB (61,440 bytes), or cap the display subset at 33,000 bytes. Enforce it in check_site by summing the woff2 bytes referenced per route.
4. **missing detail**: The display-face subset is Basic Latin, Latin-1 Supplement and General Punctuation. It omits Latin Extended-A (ı U+0131, ş, ğ), which the Turkish team names need (Yılmaz), and the arrows → ↗ ↓ (U+2190 block), which the plan sets in display type in mobile menu labels and possibly in statements and ledger values. With unicode-range, these characters fall back one at a time to Georgia, so mixed faces appear inside a single word. The existing Manrope subset already includes Latin Extended-A and arrows.
   - **Correction:** Match the Manrope coverage: Basic Latin, Latin-1, Latin Extended-A, General Punctuation and U+2190-2193/U+2197. Re-estimate the bytes and keep the cap from the previous gap. Add a check_site rule that every character rendered inside a display-face selector (h1, .chapter, .statement, ledger values, menu labels) is in the subset's cmap. Alternatively, set the arrows in a Manrope span.
5. **risk**: Font licensing is under-specified. Instancing Newsreader to opsz 72 / wght 400 and subsetting it count as modifications under the OFL. If a font declares a Reserved Font Name, a modified version must not use that name. The plan records the source and license but never checks for an RFN, and it names the @font-face family 'Newsreader'.
   - **Correction:** In P2, read the OFL header of the chosen family's OFL.txt and record in font-sources.json whether it declares a Reserved Font Name. If it does, ship the instance under a different family name (for example 'Solarity Display') and keep the copyright line. Ship OFL-<Family>.txt unchanged, add it to HOST_FILES, and record the fontTools version and the exact instancer/subset command so the output is reproducible.
6. **constraint violation**: No rule governs text over the vivid product-world colors. My computed ratios: ivory #f5f1e8 on --fitness-world #ff5a1f is 2.77:1, which fails AA. --dim on --sleep-world #3a42b0 is 3.11:1. The plan places 'closing_scene(product)' 'in the world colors' and puts world glows behind badges and copy, but its contrast matrix covers only token pairs, not text over glow cores. 'Body text stays ivory' does not stop a Fitness closing band from failing.
   - **Correction:** Add a token rule. --world is used only as a glow at 45% alpha or less, or as a rim or stroke, and never as a fill behind text. Any text inside a world scene sits on --world-deep or on a blend of at most 35% world over --world-deep that is verified to give ivory 4.5:1 or better and --dim 4.5:1 or better. Add those blended pairs to the check_site contrast matrix for all four products. Never use --dim inside world stages; use --muted or the --world-tint.
7. **inconsistency**: Exempting a.store-badge from check_site's 'external link lacks ↗' rule contradicts register T5-05 ('keep … the ↗') and weakens a project-wide convention in CLAUDE.md. The stated reason, that the badge artwork cannot be modified, does not require the exemption, because the ↗ can sit outside the badge and its clear space.
   - **Correction:** Keep the rule. Render the ↗ as a small glyph inside the link but outside the badge's clear-space box (for example a span after the <img>, separated by the required clear space), with aria-hidden and the sr-only '(opens in a new tab)'. If brand guidelines prevent even that, limit the exemption to links whose only child is a badge <img> and require the sr-only text, enforced in check_site.
8. **risk**: Two fold-fit targets are probably infeasible. (a) On Investors at 1280x800, the stack is header 88px, padding of about 64px, a two-line title at --type-chapter (about 150px), a gap of about 48px, 3:4 plates at 240-260px (320-347px tall) and an icon, name, category and two-link row (about 90px). That is about 800px or more before the bottom padding, so 'all four framed apps fully visible' fails. (b) On the Home wall at 390px, 2x2 cards at 160px have 213px-tall windows plus a 56px icon, name, category and compact official badges. Apple and Google badges have minimum on-screen sizes, so two badges cannot fit side by side in 160px. The resulting stack exceeds the 1.1-viewport acceptance (928px).
   - **Correction:** Investors: below 900px viewport height, place the title and actions beside the showroom rather than above it, or reduce the windows to 200-220px with labels to the side, and validate on the P0 renders before committing the acceptance. Home mobile wall: drop the badges from the cards (the product page carries them) and keep a text 'App Store ↗ · Google Play ↗' line or none. State the 390px acceptance as all four windows visible within 1.1 viewports, measured.
9. **missing detail**: The motion layer ordering is incomplete. Adding a 'motion' layer between pages and accessibility requires changing the @layer order statement at design/system/foundation.css:2. Otherwise motion.css creates the layer last, after accessibility, and its rules would beat the accessibility layer, including forced-colors overrides of animated properties. The plan also does not confirm that optimize_styles retains @layer blocks that contain @media and @supports.
   - **Correction:** In P9, update foundation.css:2 to '@layer foundation, components, pages, motion, accessibility;'. Add a check_site assertion that this order statement exists. Add a test in test_optimize_styles.py showing that an @layer motion { @media (prefers-reduced-motion:no-preference) { @supports (animation-timeline:view()) { … } } } block, and an @view-transition rule inside @media, both survive route filtering.
10. **missing detail**: The header behavior while the mobile menu is open on Home is unspecified. With 'header-over-hero' active, the header is transparent and the new full-height menu overlay starts below it (inset var(--header-h) 0 0). The hero sky then shows behind a transparent header above an opaque menu, and the toggle and close states sit over bright sky. The plan also does not cover restoring Home with a scroll offset (back/forward or a #fragment): the class is added synchronously in the head, but the IntersectionObserver only removes it after DOMContentLoaded.
   - **Correction:** Add a rule: html.header-over-hero body.nav-open .site-header uses the solid background, with no transition under reduced motion. In the head script, add the class only when location.hash is empty and scrollY is 0, which the history state allows on restore. Add both cases to test-navigation.cjs.
11. **unaddressed problem**: T6-01 asks for a compact team or founder strip near the top of Investors, because 'no face appears anywhere on the page'. In the plan, the founder appears on Investors only in the booking close at the very bottom, as a 140px print. The ledger row 'Founder: Ata Turhan' is text. So the person investors back is still invisible for most of the page.
   - **Correction:** Add the existing treated founder print (about 96-120px, 4:5) to the 'At a glance' ledger's Founder row, linking to Company. Remove it from the booking close, which keeps one portrait per route. Alternatively keep the close portrait and add only a small round crop in the ledger, and document that one route uses two founder crops.
12. **inconsistency**: The Investors 'At a glance' ledger is a lit panel in the evidence register, yet it contains the row 'App factory: Engineering Max · Management Max · Marketing Max' with a vision chip. That breaks the plan's own principle 3 ('evidence is lit, vision is outlined') and duplicates the 'Ahead' card that directly follows.
   - **Correction:** Remove the app-factory row from the ledger and let the 'Ahead' card carry it. Alternatively, render that one row in the vision register (dashed rule, unfilled, .status.vision) and state that exception explicitly.
13. **inconsistency**: The P1 acceptance says 'No raised surface has G greater than R'. The plan's own cool tones, --tone-night #0d1014 and --tone-blue #12161b, have G > R and are used as scene backgrounds on every interior opening. An automated check applied to all surfaces would flag them, and a check limited to 'raised' surfaces is undefined.
   - **Correction:** Restate the acceptance as: neutral and warm tokens (--bg, --surface, --raised, --line, --ink, --tone-base, --tone-first, --tone-golden, --tone-footer) satisfy R ≥ G ≥ B, and the cool tones satisfy B ≥ G ≥ R (blue axis, not olive). Enforce it in check_site against the token values.
14. **risk**: Fixed-name static assets lose immutable caching and invite stale caches. grain-v1.webp sits at /assets/texture/ and the light-field derivative's path is not given. Neither is covered by the _headers immutable blocks (only /assets/optimized/*, /assets/runtime/* and the font URL are). The plan's reason for the fixed name is also not quite accurate: foundation.css already hard-codes the hashed font URL, so hashed literals in CSS sources are possible.
   - **Correction:** Emit both derivatives into /assets/optimized/ with content hashes. Write their URLs into foundation.css as custom properties the way the font URL is handled (or have build_site substitute a placeholder before bundling, so presentation.css equality still holds). They then inherit the immutable header and are pruned by the existing stale-file logic. Measure the grain tile after encoding: seeded noise compresses poorly, so try 64x64 or lossless with 2-4 grey levels if 4 KB is exceeded.
15. **missing detail**: The signature chapters (Looks 'Inside the scan', Sleep 'Soundscapes', Fitness meal crop) depend on detail crops of 600px sources displayed at half the source width or less. Until the P5a native re-fetch is confirmed, a full-width card crop of about 540px displays at about 270 CSS px, and smaller regions such as the master volume control are much smaller. The P7 chapters could ship small and soft, recreating T4-03 at the plan's showcase moment. The roadmap does not make P7 depend on the re-fetch.
   - **Correction:** Make P7's detail crops depend on the founder-confirmed P5a re-fetch. If it is not confirmed, build the signature chapters from whole plates at 340px or less with sticky copy, and defer the detail crops. Add to the P7 acceptance that each crop's rendered CSS width × 2 is no larger than the cropped region's source width.
16. **risk**: With font-display: swap, the display face can still cause layout shift on a first visit, and on interior pages the H1 is often the LCP element. The P2 acceptance (CLS 0.01 or less, LCP within 100ms) is tested only for Home's preload decision, while the plan preloads the display face on every route. With two font preloads plus the hero AVIF preload on Home, the hero image's bandwidth is contested on slow 4G.
   - **Correction:** Run the throttled first-visit test on /investors-partners/ and /apps/looks-max/ as well as Home. Verify the metric-matched Georgia fallback line by line (H1 line count equal before and after swap at 390px and 1440px). On Home, if the hero AVIF's LCP regresses, drop the display preload there, because the H1 is not LCP on Home.
17. **unaddressed problem**: T2-02 asks that the hero's bottom fade resolve exactly at the fold. The hero clamp tops out at 960px until the higher-resolution master arrives, so at 1920x1080 the next scene shows for 120px. The 1860px master is also upscaled at 1920 wide even at 1x (T2-05). The P3 acceptance only says 'within the clamp', which hides the 1920x1080 case the plan itself lists for review.
   - **Correction:** For viewports taller than 960px, make the 400-600px amber afterglow plus the credits row the designed bottom edge, so the extra 120px reads as composed. Add a 1920x1080 acceptance: no half-cut text strip below the hero. Record the 1920 softness as a known limitation until P10, and at that width use object-position so that cropping, rather than scaling, absorbs the extra width where possible.
18. **missing detail**: The founder 4:5 print and the IQ hero swap change contracts that check_site and the image manifest track, but the plan names only some of them. The hero_screen and crop_focus fields on APPS change which files are referenced, and dist/ fails check_site if a published original (for example iq-max-screen-1 used only in the dialog, or sleep-max-detail-screen-3 once it is removed) becomes unreferenced. Removing sleep-max-detail-screen-3 leaves a published original with no page referencing it.
   - **Correction:** In P5b and P7, list each original whose references change. For a removed image (sleep-max-detail-screen-3), move the original to source-assets/ and record the move in research-assets/deploy-separation.json, per CLAUDE.md, rather than deleting it. Run check_site's unreferenced-file rule in the same PR.
19. **risk**: Same-document view transitions for the screening-room dialog (startViewTransition plus showModal) and cross-document @view-transition are specified, but the plan does not cover top-layer, inert or scroll-lock interactions, or what happens when a transition is skipped. There is also no budget for the view-transition snapshot on long pages: the root crossfade snapshots the viewport, which is fine, but a named header and four icon names per page can produce visible jumps when the destination icon is off-screen.
   - **Correction:** Name an icon only when it is above the fold on both source and destination (for example the /apps lineup to the product hero icon), not wall or sibling icons below the fold. In gallery.js, call dialog.showModal() inside the update callback and await transition.finished before moving focus. Fall back to the @starting-style path when document.startViewTransition is undefined. Extend test-gallery.cjs with a stub that has startViewTransition and one without.

Repository root: `C:\Users\atatu\Desktop\Projects\Solarity-AI\solarity-ai-project`. Every path below is relative to it.

I read all three proposals against the problem register, the source (`design/system/*.css`, `build_site.py`, `check_site.py`, `optimize_images.py`, `optimize_styles.py`, `performance_build.py`, `scripts/navigation.js`), the design logs, and the screenshots. Every byte figure marked "measured" comes from the current `dist/`, with gzip -9 computed locally. These are artifact sizes, not HTTP or Lighthouse measurements. Display-font sizes are estimates until the font is subset.

---

## 1. Scores for the three directions

| Criterion | Solar cinema | Private editorial | Product protagonist |
|---|---|---|---|
| Investor impression | **8**: the ask closes in the warmest light, with a fact band and a showroom. The concept leads with the brand before the proof. | **7**: the ledger reads mature and trustworthy. The annual-report tone undersells a consumer AI company and keeps the products "at night". | **9**: proof, then vision, then founder is the order investors evaluate in. The four apps lead every key page. |
| Cinematic and premium quality | **9**: the strongest through-line (one day of light), plus title cards and a load sequence. The letterbox bars and flare streak risk looking gimmicky. | **6**: editorial rather than cinematic. The ivory spreads interrupt the dark film set the founder asked for. | **8**: lit product worlds and one key light from the sun's side. It has fewer signature gestures. |
| Coverage of critical and high problems | **9**: almost every id gets a specific treatment. | **8**: every id is addressed, but allowing one ivory spread per page reopens T1-02. | **9**: every critical and high id is addressed, and it is strongest on T4-01, T5-01, T5-03 and T6-02. |
| Constraint safety | **7**: at load, the letterbox bars would hide the credits row and the "Conceptual brand artwork" caption. The once-per-session gate adds pre-paint state. | **6**: Light 300 cuts fail check_site's 400/500/600 weight rule and double the font bytes. A full-width sunrise reprise overruns the 1860px master. | **8**: hard caps on hero and screenshot scale, recorded crops, no fabricated frames, and sticky layouts guarded by viewport height. |
| Feasibility in static Python and CSS | **7**: mostly CSS. A document-length gradient and a fixed scroll-linked key light behave differently on every page length and breakpoint. | **8**: the simplest layout and motion. Two token sets (ink and ivory) are easy to build. | **7**: a pinned stage that crossfades needs 3 or more distinct screens. Looks Max has 2 and Sleep Max 1 once the empty-profile frame goes. |
| Maintainability | **7**: many bespoke devices to keep tuned page by page. | **7**: every component needs ink and ivory variants and two contrast matrices. | **8**: one stage component and one set of `[data-product]` tokens, reused by Home, Apps, Investors and the product pages. |
| **Total (of 60)** | **47** | **42** | **49** |

**Verdict.** Product protagonist is the spine. Its proof-first structure and shared stage component fix the critical items, T4-01 and T5-01, and are the cheapest to maintain. Grafted onto it:

- **From Solar cinema:**
  - The "one day of light" through-line. It is implemented as scene tones per section, not a document-length gradient.
  - "Evidence is lit, vision is outlined."
  - One cinematic device per viewport.
  - The anamorphic horizon rule as the only divider.
  - Pillow-generated grain.
  - The load sequence, without the letterbox.
  - The interior arrival.
  - The named product light conditions.
  - The screening-room gallery.
- **From Private editorial:**
  - Ledger rows for the investor fact band.
  - The folio (a bronze rule plus a caps label, no numbers) in place of most eyebrows.
  - Its warning about Instrument Serif. The specimen leads with Newsreader instead.
  - A "print mat" frame for the founder portrait instead of a vignette over a white backdrop.
  - The single sunrise reprise at the Investors booking close, as a contained plate.
- **Rejected:**
  - The letterbox bars, because they delay a disclosure and the designed bottom edge.
  - The fixed scroll-linked key light and the document-length gradient, which are fragile.
  - The flare streak on the hero, which risks looking like an altered artwork.
  - Ivory spreads. Paper stays retired.
  - The pinned crossfade stage on product pages, because there are too few cleared screens. Sticky copy beside travelling screens does the same job.

---

## 2. Creative north star and principles

**North star: "Four worlds, one sun."** The approved sunrise is the opening shot. Each page then plays as one day of light, from pre-dawn at the top to golden hour at the close. The four shipped apps are the protagonists, and each stands in its own colored light on a warm, dark set, lit from the upper right where the hero sun sits. Verified evidence is lit and solid. The app factory is drawn in outline, clearly labelled as a vision and never brighter than the evidence. The founder and the investor ask arrive in the warmest light at the end. The work is restrained: authored type, motivated light and real assets reframed with care, so that four live apps and a named founder read as a company with taste.

**Principles**

1. **Proof leads, vision follows, the person closes.** Every corporate page follows this order. The products come first on Home, Apps and Investors.
2. **One sun.** There is one key light at about 85% across, from the upper right. Every glow is motivated, sits behind a focal object, is larger than its box, and is strong enough to see.
3. **Evidence is lit, vision is outlined.** Evidence gets filled, lit surfaces, real icons and screens, and the `.status` chip. Vision gets dashed hairlines, unfilled panels and the `.status.vision` chip. Evidence never sits on a dimmer surface than the vision.
4. **One cinematic device per viewport.** That device is the sunrise, a lit stage, a title card, a drawn horizon or a dawn close, and never two at once.
5. **Type is authored, not defaulted.** A display voice carries titles and statements, Manrope does the work, and each page has a crescendo: one title moment and one close.
6. **Authentic or absent.** Real assets are cropped, lit, scaled and framed, never invented. Missing content is handled by tightening the layout, not by enlarging placeholders.
7. **Nothing ships unseen.** A value is done only when it has been checked in rendered screenshots at 390 and 1440, with and without reduced motion. This is the step every earlier pass skipped (DESIGN_SYSTEM.md:13, CINEMATIC_REFINEMENT.md:52).

---

## 3. Design-system changes

All tokens live on `:root` in `design/system/foundation.css`. The existing `forced-colors` and `print` maps in `accessibility.css` get entries for every new token.

### 3.1 Typography (T3-01 to T3-13, T10-02)

**Families, weights and byte cost**

| Role | Family | Weights | Bytes | Loading |
|---|---|---|---|---|
| UI, body, deck, labels, section and sub headings, team names | Manrope variable (existing) | 400 reading, 500 headings, 600 labels and buttons | **26,292 bytes, measured** (`dist/assets/fonts/manrope-latin-variable.cfa570d7c3ee.woff2`) | Keep the preload and `font-display: optional`. Add a metric-matched "Manrope Fallback" `@font-face` with `src: local('Arial')`, `size-adjust`, and `ascent-override`/`descent-override` derived from the font-sources.json metrics (2132/−600 at 2000 UPM, each override = metric ÷ UPM ÷ size-adjust). |
| Title, chapter, statements, product-name H1s, large ledger values, platform numerals, founder quote | **Recommended (A1): Newsreader**, a static instance at opsz 72, wght 400, roman only | 400 only, which passes check_site's existing weight rule | **About 22–32 KB, estimated**, for a Basic Latin + Latin-1 Supplement + General Punctuation (’ “ ” – — … ·) subset with lining figures. Measure after subsetting. **Cap: 34 KB.** | `font-display: swap` with a metric-matched "Display Fallback" built on `local('Georgia')` (size-adjust plus overrides from the instance's metrics). Declare `unicode-range` so any missing glyph falls back per character. Preload on every route; Phase 2 tests Home with and without the preload. |
| Alternative (A2) | Instrument Serif Regular | 400 | About 18–26 KB, estimated, for the same subset | Same as A1 |
| Alternative (B) | Manrope only: display at weight 300 with tracking near zero | 300 is added to the check_site allowlist | 0 KB | No new file |

Why A1 is the default: Newsreader's display optical size gives real title-card contrast at 112px and still reads well at 40px. My view is that Instrument Serif has become a common choice on startup template sites, which works against "not average". The founder makes the final choice from the Phase 0 specimen. There is no italic cut: emphasis is a color change on one word, never a weight change. **Font budget: 60 KB or less per route.**

Production steps:
- Subset offline with fontTools, so it is not a build dependency.
- Commit the woff2 to `dist/assets/fonts/<name>.<sha12>.woff2` with its license as `dist/assets/fonts/OFL-<Family>.txt`.
- Record the source URL, sha256, instance axes, subset and bytes in `source-assets/fonts/font-sources.json`.
- Add the URL to the `_headers` immutable block in `build_site.py:146`.
- Add the license to `HOST_FILES` in `check_site.py:282`.

**Scale.** Five fluid tokens plus fixed small sizes. Values are given at 1440px and 390px.

| Token | Value | At 1440 / 390 | Face | Line-height | Tracking |
|---|---|---|---|---|---|
| `--type-title` | `clamp(3.25rem, 1.9rem + 5.6vw, 7.5rem)` | ≈111 / 52px | Display | .98 | −0.015em |
| `--type-chapter` | `clamp(2.5rem, 1.6rem + 3.6vw, 4.75rem)` | 76 / 40px | Display | 1.02 | −0.01em |
| `--type-section` | `clamp(2rem, 1.45rem + 1.9vw, 3.25rem)` | 52 / 32px | Manrope 500 | 1.08 | −0.015em |
| `--type-sub` | `clamp(1.375rem, 1.15rem + .75vw, 1.875rem)` | ≈29 / 22px | Manrope 500 | 1.2 | −0.005em |
| `--type-deck` | `clamp(1.1875rem, 1.05rem + .45vw, 1.4375rem)` | 23 / 19px | Manrope 400, `--text` | 1.42 | 0 |
| `--type-body` | `clamp(1.0625rem, 1rem + .15vw, 1.125rem)` | 18 / 17px | Manrope 400, `--muted` | 1.6 | 0 |
| `--type-meta` | `.875rem` | 14px | Manrope 500 | 1.5 | 0 |
| `--type-label` | `.75rem` | 12px | Manrope 600, uppercase via CSS | 1.5 | +0.12em |

Rules:
- **Headline tokens.** Every h1 and h2 maps to a token. A page has at most one title moment and one statement close. On product pages the product-name H1 sits one step above the story h2s.
- **Tracking.** No negative tracking below 28px or on capitals. Display headings get `word-spacing: .03em`, and the team credits use −0.02em or looser. The wordmark is Manrope 600 at 16px, +0.06em.
- **Retire.** Remove `--text-xs` (13), `--text-md` (15) and `--text-base` (16) from new code, so the small roles are label 12, meta 14 and body 17–18 (T3-11). Remove `--font-mono` from the thesis (T3-09).
- **Labels.** There are two label styles. The caps label (`--type-label`) is used for folios, footer groups and ledger keys. The meta label (14px, no tracking) covers product names in small contexts and categories. Product names are never tracked. Write strings in sentence case in Python and apply uppercase in CSS (T3-07, T3-08).
- **Numerals.** `font-variant-numeric: lining-nums tabular-nums` everywhere. Large display numerals appear only on Platform's real Build, Operate, Grow sequence. Remove numbering from the FAQ, partnership topics, principles and the 404 list (T3-09).
- **Wrapping.** `text-wrap: pretty` on `p, li, dd, figcaption, .deck`. Use `&nbsp;` in "iOS&nbsp;&amp;&nbsp;Android", "new&nbsp;tab" and "Ata&nbsp;Turhan" (T3-10).
- **Couplets.** The split couplet is kept only for the Home hero and the Home close. All other forced `<br>` couplets are removed (T3-04). Rename `.muted` inside headings to `.em`, which colors the one emphasized word `--sun-core` and never grey.
- **Measures.** Three tokens: `--measure-deck: 34ch`, `--measure-body: 52ch` (unchanged) and `--measure-heading: 18ch`. They replace the 38 one-off ch values.
- **check_site.** Reject any `font-size: clamp(` outside `foundation.css`. Reject `font-family: var(--font-mono)`. Allow only the token sizes for small text.

### 3.2 Color and light tokens (T1-01 to T1-06, T5-01, T10-07)

```css
/* neutrals on a warm ember axis (T1-04) */
--bg:#0f0d0b; --surface:#18140f; --raised:#221c16; --line:#3a3027; --line-soft:#2a231c;
--text:#f5f1e8; --muted:#c9c0b2; --dim:#a99f91; --ink:#1a140e;
/* solar ramp (T1-05) */
--sun-core:#ffcf7a;  /* one focal element per viewport: the primary CTA or one emphasized word */
--gold:#e9b56a;      /* active and current states, ghost-button labels on dark */
--sand:#d6bf9a;      /* caps labels, folios */
--bronze:#9c7446;    /* rules, control borders, decorative strokes; never small text */
--ember:#d9782f; --haze:#f5dfbb;
/* light (T1-03) */
--glow-sun:rgb(255 190 110 / .28); --glow-ember:rgb(217 120 47 / .18); --glow-haze:rgb(245 223 187 / .10);
--key-x:85%; --key-y:12%;
/* controls (T10-07) */
--control-border:var(--bronze); --control-border-hover:var(--gold); --focus:var(--sun-core);
/* product worlds (T5-01): deep stage, world glow, text-safe tint */
--looks-deep:#1e0f30; --looks-world:#7a35c9; --looks-tint:#e3c8ff;
--iq-deep:#0c1838;    --iq-world:#2a4fd0;    --iq-tint:#c3f2ee; --iq-rim:#9fe8dc;
--sleep-deep:#0f1230; --sleep-world:#3a42b0; --sleep-tint:#ccd0fb;
--fitness-deep:#160b06; --fitness-world:#ff5a1f; --fitness-tint:#ffc4a6;
```

Notes:
- Computed contrast on `--bg`: `--dim` ≈ 7.4:1 and `--muted` above 9:1. On the warmest tone (`--tone-golden`), `--dim` is ≈ 6.4:1. Ink on a `--sun-core` button is ≈ 12.6:1. `--bronze` against `--bg` is ≈ 4.6:1, which meets the 3:1 non-text requirement for control borders.
- `--sleep-world` is lifted from the proposed #262c78, which barely registers as a glow on #0f1230. Tune it in rendered review.
- **Apply product worlds** through `body[data-page='/apps/<slug>']` and `[data-product='<slug>']`, which set `--world-deep`, `--world` and `--world-tint`. Vivid hues appear only on stages, glows, rims, rules and focus within the world. Body text stays ivory. Company gold is reserved for investor and partner actions.
- **Retint hard-coded values:**
  - #727469, #64695a, #74796d and #80786b become `--control-border`.
  - #847359, #776a58, #50473a and #8c7859 become `--control-border` or `--line`.
  - The `.status` color #c8dccd becomes `--muted`.
  - Footer #e4dece/#b39d78 become `--text`/`--sand`.
  - The menu #171a14 and footer #0c0e0b become tokens.
  - `theme-color` in `build_site.py:82` becomes `#0f0d0b`.
- **Retire paper.** Remove `--paper*` from all four panels (T1-02). The skip link moves to `--sun-core` on `--ink`.

### 3.3 Scene tones ("one day of light") and texture

```css
--tone-night:#0d1014; --tone-blue:#12161b; --tone-base:var(--bg);
--tone-first:#17110c; --tone-golden:#24170c; --tone-footer:#0b0907;
```

- **Tones per scene, not per document.** Every section a page emits is a `.scene` with a tone. Python knows the scene order and writes `data-from="<previous tone>"`. CSS paints a 160px bridge, `linear-gradient(var(--from-tone) 0, var(--scene-tone) 160px)`. Interior pages open at blue hour and end golden. Product worlds replace the tone inside stage scenes.
- **Grain.** `optimize_images.py` generates a deterministic, seeded 128×128 luminance-noise WebP with the alpha baked in (about 8/255) at `dist/assets/texture/grain-v1.webp`. Its target size is 4 KB or less. A fixed, versioned name is used because CSS sources cannot carry content hashes without breaking check_site's bundle-equality check. Grain is the top background layer on scenes only. There is no fixed or blended overlay and no `backdrop-filter` after the hero.
- **Pre-blurred light field.** `optimize_images.py` derives a 480×210 WebP of 6 KB or less from the master's sun and horizon band: downscale to 64px, Gaussian-blur, upscale. It is unrecognizable as the scene, so it does not count against the sunrise image budget. It is recorded in the image manifest as a new treatment of the approved master. It is used at the bottom of interior openings, in closing scenes, on the 404 page and in the mobile menu.
- **Image budget.** The recognizable sunrise appears in the Home hero plus one reprise, at the Investors booking close (see §6). That reprise is a contained plate of 600 CSS px or less, captioned "Conceptual brand artwork".

### 3.4 Spacing and grid

- **Wraps.** Keep `.wrap` at 1264px. Add `--wrap-wide: 1440px` for stage bands, and `.bleed` for full-width scenes.
- **Grid.** 12 columns at 1150px and above, 8 at 561–1149px, 4 at 560px and below. `--col-gap: clamp(16px, 2vw, 32px)`. The breakpoints keep check_site's expected 1150/850/560.
- **Scene padding.** Use exactly one padding per scene, and never stack a margin on top of it. This removes the 228px gaps before the closing band (T8-03):

  | Token | Value | Use |
  |---|---|---|
  | `--scene-xl` | `clamp(120px, 12vw, 200px)` | Opening and close |
  | `--scene-l` | `clamp(96px, 9vw, 152px)` | Stages |
  | `--scene-m` | `clamp(64px, 6vw, 104px)` | Editorial and proof |
  | `--scene-s` | `clamp(40px, 4vw, 64px)` | Credits and ledger |

- **Spacing scale.** `--space-1…9` = 4, 8, 12, 16, 24, 32, 48, 64, 96px. `scroll-padding-top` stays the single contract (112px).

### 3.5 Radii (T10-07)

| Token | Value | Use |
|---|---|---|
| `--radius-control` | 10px | Inputs, dialog controls, chips |
| `--radius-plate` | 14px | Screenshot plates |
| `--radius-panel` | 20px | Lit panels, stages that are contained, the founder print |
| `--radius-pill` | 999px | Buttons only |
| `--radius-icon` | 24% | App icons |
| `50%` | | True circles |

`--radius` and `--radius-lg` are removed, with temporary aliases during migration. The check_site radius regex becomes `var\(--radius-(control|plate|panel|pill|icon)\)|0|50%`. No square panel remains.

### 3.6 Elevation, expressed as light

Drop shadows do not read on near-black, so elevation comes from light.

- `--elev-panel`: a gradient from #1f1913 to #120f0c, plus `inset 0 1px 0 rgb(255 220 170/.10)` and `0 0 0 1px rgb(214 191 154/.10)`. This is the lit panel.
- `--elev-stage`: the panel, plus a key-light pseudo-element (a radial at `--key-x`/`--key-y` in `--world` at 30–45%) and a floor glow (an ellipse 60%×18% at the bottom center).
- `--elev-object`, for plates and the print: `0 0 0 1px rgb(255 255 255/.08)`, a rim of `1px -1px 0 color-mix(in oklab, var(--world-tint) 35%, transparent)` on the upper-right edge, and a contact shadow of `0 30px 60px -24px rgb(0 0 0/.85)`.
- `--elev-overlay`, for the dialog and menu: a backdrop of `rgb(8 6 4/.9)`.
- Glows use `--glow-*` cores fading to transparent over 50–60% of the radius. They sit on a pseudo-element larger than the box and are masked with `closest-side` so there is never a visible edge.

---

## 4. Global components

Each component is one Python helper (in `visual_sections.py`, or a new `visual_scenes.py`) plus one CSS block. Pages compose them; they never restyle them.

**Header** (T2-01, T10-03, T10-04, T10-05)
- **Structure.** Unchanged: the toggle precedes `#site-nav`, and the Contact link stays outside the nav, which `check_site.py` requires. Heights stay 88px desktop and 76px mobile at every scroll position.
- **Interior pages.** Opaque `--bg` from first paint, with `box-shadow: 0 1px 0 var(--line-soft)` and no blur.
- **Home state switch.**
  - The inlined `navigation.js` adds `header-over-hero` to `<html>` synchronously when `location.pathname === '/'`, so it is set before paint.
  - On DOMContentLoaded, an IntersectionObserver on the hero (rootMargin `-88px 0 0 0`) removes the class once the hero leaves.
  - With no IntersectionObserver, the class is removed. With no JS, the class is never added, so the bar is solid.
  - Add the class to `DYNAMIC_CLASSES` in `optimize_styles.py` and add the cases to `test-navigation.cjs`.
  - Over the hero, the header is transparent with no `backdrop-filter`. The hero's top scrim, `linear-gradient(180deg, rgb(12 9 6/.55), transparent 160px)`, protects the nav.
  - The background transition is 180ms under no-preference and instant under reduced motion.
- **Wordmark.** The existing sun raster at 32px, a 10px gap, then "SOLARITY" in `--text` and "AI" in `--sand`. Both are Manrope 600 at 16px, +0.06em. Brand changes beyond this wait for the founder (T10-01).
- **Nav links.** 14px, weight 500, `--muted`. On hover or focus they turn `--text` and a 1px `--sun-core` underline draws in (scaleX). The current page keeps the underline.
- **Contact.** Becomes a ghost small button: 44px, a `--control-border` hairline and a `--gold` label. Over the hero, the label is `--text` on a fill of `rgb(12 9 6/.35)`. That combination was computed at ≈6:1 over the brightest sky beside the sun, whereas a gold label there is only ≈3.8:1. `.button[aria-current]` gets a `--raised` fill and the sun-core underline.
- **560px and below.** The lockup, a borderless two-line menu icon in `--text` (44px target), and Contact as a compact text link (44px target, no pill, no arrow). The DOM is unchanged, so the contract holds.

**Mobile navigation** (T9-08)
- A full-height overlay below the header (`position: fixed; inset: var(--header-h) 0 0`) on `--bg`, with the pre-blurred light field as a dawn glow at the bottom.
- Links are set in the display face at 28–32px, each with its one-line description in meta.
- Pinned at the bottom: "Investor inquiries" (primary) and "Book a conversation ↗", which keeps its sr-only "(opens in a new tab)".
- A `body.nav-open::after` scrim.
- Keep the disclosure semantics, `inert`, `aria-hidden`, Escape handling, focus return and every `test-navigation.cjs` contract.

**Buttons and links** (T10-06, T8-04)
- **Primary.** `--sun-core` fill, `--ink` label at 15px weight 600, 52px tall, with an inner top highlight. Hover and focus-visible add a bloom of `0 8px 30px rgb(236 160 80/.30)`. `:active` scales to .98 for 90ms. Use one primary per viewport.
- **Secondary (ghost).** A 1px `--control-border`, `--text` label. On hover the fill becomes `rgb(255 207 122/.08)` and the border `--gold`.
- **Tertiary.** An ivory text link with a 1px `--gold` underline at a .3em offset, and no arrow.
- **Arrows** stay Unicode glyphs, because check_site parses ↗. They are set at 1.1em, weight 500, so their stroke matches the label. They slide out and back in over 360ms. Arrows appear only on buttons and directional links.
- **Labels are standardized:** "Investor inquiries", "Partnership inquiries", "Book a conversation", "Email Ata".
- **Store badges** (T5-05):
  - Official, unmodified Apple and Google SVG badges, self-hosted at equal visual height, which means scaling the Google artwork to account for its built-in padding.
  - Each brand's minimum size and clear space is respected.
  - Trademark attribution lines go in the footer legal line.
  - Each badge link keeps its accessible name and the sr-only new-tab text.
  - Exempt only `a.store-badge` from check_site's "external link lacks ↗" rule (`check_site.py:279`), because the badge artwork cannot be modified and needs clear space. Document the exemption in CLAUDE.md's arrow conventions.

**Status chips** (T6-02, T6-12)
- `.status`: a filled `--sun-core` dot with "Available on iOS & Android" in `--muted`.
- `.status.vision`: a hollow ring dot (1px currentColor) with "Vision" in `--sand`.
- Both are 12px caps labels with no underline, and always carry text.

**Footer** (T8-02, T8-05, T8-06)
- **Lead-in.** A 160px dusk bridge into `--tone-footer`, with no rule. The intro slogan "Human potential. Thoughtfully built." is removed.
- **Directory.** Three groups with caps-label headings:
  - Portfolio: the four apps, which check_site requires.
  - Company: Apps, Platform, Company, Investors & Partners, Careers.
  - Contact: Investor inquiries, Partnership inquiries, Email Ata ↗ (with the arrow inline after the label via `justify-content: flex-start`), Book a conversation ↗.
  - Targets stay 44px.
- **Signature.** The footer is `container-type: inline-size`. The wordmark is sized in `cqi` so it spans 100% of the wrap at 1024, 1440 and 1920. Tune the value from renders; never use uncapped `vw`. It is Manrope 500 at 0 to +0.02em, with "AI" in `--sand` at the same weight. The sun mark sits at the baseline as a new 192/320px crop from `solarity-lockup-original.png` through the existing favicon-crop pipeline. A `--glow-ember` horizon sits below the baseline. It stays `aria-hidden`, and the forced-colors rule is kept.
- **Legal line.** One left-aligned line: "© 2026 Solarity AI LLC · Irving, Texas, United States · About this contact experience" followed by the store trademark lines. Privacy and Terms are added when supplied.

**Section transitions** (T8-01, T8-03)
- **Scene types:**
  - `horizon`: an opening with image or light.
  - `stage`: a product world.
  - `proof`: ledger, facts.
  - `editorial`: a statement or thesis.
  - `people`.
  - `close`.
- Each scene type has fixed padding and tone rules.
- **Divider.** The single divider is the horizon rule: 1px, `linear-gradient(90deg, transparent, var(--bronze) 20%, var(--sun-core) 50%, var(--bronze) 80%, transparent)`, with a 6:1 elliptical bloom at 20%. Use it at most twice per page.
- **Lists.** Inside lists, rules are `--line-soft` with faded ends. Structural hairlines between sections are removed.
- **Folio.** A 32px `--bronze` rule plus a caps label. It is used at most once per chapter, never repeats the heading, and is four words or fewer. It replaces about two-thirds of the eyebrows.

**Plate and stage (the screenshot frame)** (T4-01, T4-02, T4-05, T4-06)
- **No device frames are fabricated.**
- **`.plate`** wraps the real image: `--radius-plate`, `overflow: clip`, `--elev-object`, and an inner rim on `::after`.
- **`.plate--window`** is a 3:4 crop window. Its `object-position` is set per product from a new `crop_focus` field in each APPS record and aims at the UI region, not the poster headline.
- **`.stage[data-product]`** carries `--elev-stage` in the product world. Its edges are feathered with `mask-image` on the background pseudo-element only, never on the image. Its radius is `--radius-panel` when contained and 0 when it is a full-bleed band.
- **Size caps.** Screens are capped at **340 CSS px wide** (windows at 280px) until the native-resolution assets land (P5a). After that, hero screens may grow to 440–520px.

**Founder print** (T7-01)
- A 4:5 crop (`object-fit: cover`, `object-position: 50% 22%`), with new 320/480/640w variants generated from the 800px master.
- A 10px `--raised` mat, a 1px warm hairline, `--elev-object`, and a `--glow-sun` bloom from the upper right behind the mat.
- Displayed at 320–360 CSS px on desktop and 280px on mobile.
- The image itself is untouched: no grade, retouch or background replacement without founder approval. The mat makes the white studio backdrop read as a deliberate print rather than a pasted ID photo.
- It appears at most once per route.

**Closing horizon scene** (T8-02)
- One `closing_scene(statement, primary, secondary, variant)` helper.
- Background: `--tone-golden`, a dawn glow rising from the bottom edge (`--glow-ember` plus `--glow-sun` in an ellipse wider than the viewport), the pre-blurred light field and grain.
- One page-specific statement at chapter scale. One primary and one secondary action.
- Variants:
  - `corporate`: Investor inquiries and Partnership inquiries.
  - `product`: the product's world, its icon, the official badges, and a secondary "Ask about X".
  - `booking` (Investors): see §6.
- Drop its margin-top. The scene supplies its own padding.

**Caption helper** (T3-13, T4-08)
- One `provenance(scope)` function and one `.caption` class (meta style, `--dim`).
- Wording: "Official App Store imagery with sample content, cropped for layout. View listing ↗". It appears once per gallery or wall.
- Alt text is kept per image.
- The hero caption remains "Conceptual brand artwork".

**Rows and tiles** (T9-10, T10-09)
- One signature interaction:
  - A `--gold` hairline draws along the bottom edge (scaleX from the left, 420ms).
  - A 6–8% `--sun-core` wash enters from the left.
  - The arrow exits and re-enters.
  - The title shifts 4px.
- The same interaction runs on `:focus-visible`, and the wash shows on `:active` for touch.
- It applies to strategy rows, partnership tiles, contact tiles, related-app cards, recovery tiles and footer links.

**Ledger** (T6-01)
- A `<dl>` of rows: a caps-label key on the left and a display-face value at `--type-sub` on the right.
- Rules have faded ends.
- Optional `.status` or `.status.vision` chips sit inline with values.

---

## 5. Motion system (T9-01 to T9-11)

**Contract.** It is written into DESIGN_SYSTEM.md, replacing the "hidden-content entrances" ban, and enforced by check_site.

1. All `@keyframes`, `animation-timeline`, `@view-transition` and entrance transitions live in a new `design/system/motion.css`. That file is wrapped in `@media (prefers-reduced-motion: no-preference)`, sits in a new `motion` layer between `pages` and `accessibility`, and is added to `style_sources` in `build_site.py:117`. Update CLAUDE.md's stylesheet count from 8 to 9 and the DESIGN_SYSTEM.md table.
2. Scroll-linked motion is additionally inside `@supports (animation-timeline: view())`.
3. The static page is complete. The hero image and any H1 that is above the fold never start from `opacity: 0`.
4. Only `transform`, `opacity` and `clip-path` animate. There is at most one ambient loop on the whole site, and none is planned.
5. Every hover effect has `:focus-visible` and `:active` equivalents.
6. JS is optional and adds 1.5 KB minified or less in total. Classes it adds go into `DYNAMIC_CLASSES`.
7. Captions, disclaimers and "Conceptual strategy" legends are never revealed late.

**Tokens** (replacing `--motion-fast`, `--motion-detail` and `--motion-ease`, and the hard-coded durations at home.css:141, products.css:152, company.css:176 and accessibility.css:10):

- Easings: `--ease-out: cubic-bezier(.16,1,.3,1)`, `--ease-in-out: cubic-bezier(.65,0,.35,1)`, `--ease-sun: cubic-bezier(.22,1,.36,1)`.
- Durations: `--dur-press: 90ms`, `--dur-feedback: 180ms`, `--dur-move: 420ms`, `--dur-reveal: 720ms`, `--dur-scene: 1200ms`.
- `--stagger: 70ms`, and `--rise: 24px` (16px at 560px and below).

| Effect | Where | Specification | Reduced-motion fallback |
|---|---|---|---|
| Hero settle | Home art | `scale(1.05)` to 1 over 1600ms with `--ease-sun`, from the first frame. Transform only, so LCP is unaffected. | Static at scale 1 |
| Title-card rise | Home H1, 768px and wider | Each line is wrapped at build time in `.line{overflow:clip}`. The inner span goes `translateY(105%)` to 0 over 650ms with `--ease-out`, starting at 100ms with an 80ms stagger. The hero image is the LCP element on Home, so this is safe there. | Static |
| Lede, actions, credits | Home | The lede and actions move `translateY(10px)` to 0 from fully visible over 500ms, starting at 300ms. The credits icons move 12px to 0, starting at 650ms with a 70ms stagger. The whole sequence ends by about 1.2s. | Static |
| Interior arrival | All other routes | The H1 moves `translateY(12px)` to 0 from fully visible over 500ms. **No clip mask**, because a fully clipped H1 can delay text LCP. The folio rule draws in with scaleX over 600ms. | Static |
| Header state | Home | Background color changes over 180ms. | Instant |
| Reveal: rise | Blocks below the fold | `animation-timeline: view(); animation-range: entry 5% entry 40%`, from `translateY(var(--rise))` and opacity 0 to rest. Stagger uses a build-time `--i`. | Visible and static |
| Reveal: unfold | Lit panels, ledger | `clip-path: inset(0 0 100% 0)` to `inset(0)`, range entry 0–45%. | Static |
| Reveal: draw | Horizon rules, ledger rules, diagram connectors | scaleX, or `stroke-dashoffset` with `pathLength="1"`, range entry 10–60%. | Fully drawn |
| Plate settle | Stages, showroom, wall | Scale .96 to 1, while the key-light pseudo-element goes from opacity .55 to 1. | Full light, static |
| Hero depth | Home art | `animation-timeline: scroll(root)`, range 0 to 100vh, translateY 0 to 8% (4% at 768px and below), with the art overscaled to 1.1. | Static |
| Progress hairline | Investors, Platform, product pages | 2px `--sun-core`, scaleX driven by `scroll(root)`, `aria-hidden`. | Hidden |
| Platform active node | Platform, 1150px+ wide and 760px+ tall | View timelines with `timeline-scope` on the module sections drive an outline glow on the matching node. Pure CSS. | No highlight; the map is static |
| Fitness counter-motion | Fitness triptych | `view()` moves the columns −24px and +80px to −40px. | Offsets 0 |
| Page transitions | All routes | `@view-transition { navigation: auto; }` inside the guard. The root fades over 380ms with a 12px rise. `view-transition-name: site-header` keeps the header steady. Icons get build-time names from APPS (for example `looks-max-icon`) on exactly one element per page, which on Home is the wall icon, not the credits row. A screen is named only when source and destination render the same crop. | None |
| Mobile menu | 850px and below | `@starting-style`, `transition-behavior: allow-discrete`, a clip-path `inset(0 0 100% 0)` to `inset(0)` over 360ms, links rising 8px with a 35ms stagger, and a scrim fade. It closes in 200ms. | Instant |
| Screening room | Product pages | A same-document `startViewTransition` with a shared name from the thumbnail to the dialog image (about 0.3 KB in `gallery.js`). Fallback: `@starting-style` scale .96 to 1 plus a backdrop fade, with exit via allow-discrete. Previous and next crossfade over 220ms with a 12px directional slide. | Instant |
| FAQ | Investors | `interpolate-size: allow-keywords` and `::details-content` height over 420ms. The answer rises 6px and the marker rotates over 300ms. | Instant |
| Buttons, rows, cards | Everywhere | As specified in §4. Cards lift 4px over 420ms and their light rises 20%. | Color changes only, instant |

The global reduce rule (`animation: none!important; transition: none!important`) stays. The guard also covers `@view-transition`, because the reduce rule does not reach `::view-transition` pseudo-elements.

**Budgets**
- New JS: 1.5 KB minified or less in total. Of that, the header state is about 0.4 KB in the inlined `navigation.js` (its inline hash regenerates at build) and the gallery transition about 0.3 KB.
- `motion.css`: 6 KB or less of source, and 4 KB or less per route after filtering.
- No libraries. CLS stays at 0, which constant header heights and metric-matched fallbacks make possible.

---

## 6. Page by page

Each page lists its scenes in order, with tones in brackets. Proposed headline wording is marked *(copy)*. It uses facts the site already publishes, and the founder approves it before publication. It says "available", never "live".

**Home `/`**
1. **Opening** [horizon]
   - Height `clamp(640px, 100svh, 960px)` until the hi-res master arrives, then 1080px.
   - The header floats over the sky.
   - Warm umber scrims (`rgb(16 11 7)`) clear by 50% of the width. A local radial sits behind the copy, and the bottom fade resolves exactly at the fold.
   - The eyebrow is removed. The H1 is "Building for / human potential." on two lines at `--type-title`, ending left of the climber, with "potential" in `--sun-core`.
   - The deck (the current lede) is at most 34ch. Investor inquiries (primary) and Partnership inquiries (ghost) sit on one row.
   - The designed bottom edge is a credits row: four 36px icons with names (the `hero-product` links, which is the check_site contract), "Four apps · iOS & Android" in meta, and a scroll cue "Explore the portfolio ↓".
   - The caption "Conceptual brand artwork" sits bottom-right inside the scrim at 4.5:1 or better.
   - A 400–600px amber afterglow runs into the next scene.
   - Update `sizes` and the exact-match preload together. Fixes T2-01 to T2-04.
   - **Mobile:** the art grows to 560px, or 500px if a 3x device shows softness. The headline sits on its lower fade. The caption goes on a chip of `rgb(12 9 6/.55)` with `--text`, computed at ≈5.4:1 over the brightest cloud. One full-width primary, a text-link secondary, the cue, and no trailing gap (T2-06).
2. **Portfolio wall** [stage ×4] *(copy: "Four apps for appearance, mind, sleep and fitness.")*
   - Four world cards: a 3:4 window plate (260px on desktop; a 2×2 grid at about 160px on mobile, so all four are visible), a 56px icon, the name at `--type-sub`, the category in meta, compact badges, and a whole-card stretched link to the product page.
   - One provenance line.
   - It replaces both the hero-evidence strip and the explorer. Update the check_site explorer contract (`check_site.py:160–166`) in the same pull request.
   - The order is the APPS order unless the founder chooses otherwise. Fixes T5-03, T6-07, T5-13, T9-06.
3. **App factory** [blue hour, vision register] — the shared `platform_map(variant='home')` SVG:
   - The four icons on a horizon as the lit source, with `.status`.
   - An arc of light to three dashed nodes (Build: Engineering Max, Operate: Management Max, Grow: Marketing Max), each with `.status.vision`.
   - A legend: "Conceptual strategy. Connections are not deployed integrations."
   - One "Explore the app factory →".
   - The ring and the strategy closing link row are removed. Fixes T6-04, T1-03.
4. **Founder** [first light]
   - The founder print at 300px, with "Ata Turhan · Founder, Solarity AI · Irving, Texas" and one "Meet the company →".
   - The "Founder's perspective" eyebrow is removed and the row tightened until a statement exists. When a statement arrives, use the statement component (T7-02).
5. **Close** [golden] — `closing_scene('corporate')`, with the existing closing line kept as the couplet. Then the footer.

**Apps `/apps/`**
1. **Opening** [blue hour] *(copy: a fact-based title replacing "One ambition. Your next step.")*
   - A lineup of the four official icons at 112px, each on its world glow, with name and category. The lineup is the in-page anchor nav, with ↓.
   - Icon variants add 224 and 320w (T5-04).
2. **Four world bands** [stage ×4, alternating sides]
   - Each band: a 64px icon, the name at `--type-chapter`, the category, a deck summary, compact badges and "Explore Looks Max →".
   - The hero plate is capped at 340px.
   - The whole card is a stretched link to the product page, and the image no longer opens the lightbox (T5-11).
   - The status dot is removed (T5-16). The Only Fitness disclosure appears once, in its badge block (T5-15).
   - **Mobile:** compact cards with a window plate capped at 55svh, a per-product `object-position` and a one-line summary (T5-12).
3. **Close** [golden] — `closing_scene('corporate')`. Then the footer.

**Shared product-page frame (Looks, IQ, Sleep, Fitness)**
- **Opening** [world]:
  - Breadcrumbs.
  - A 104px icon with a world glow.
  - **H1 = the product name** at `--type-title`, with the current slogan demoted to the deck.
  - A body lede.
  - Badges directly under the deck, with the in-app purchase note under the badges.
  - A stage with the cropped hero plate (340px or less). The full poster opens in the screening room.
  - **Mobile:** badges come before the stage, and the "Get X ↓" quick link is removed (T5-08, T5-17).
- **Signature chapter**: see each product below. Feature rows are folded in, and "The product experience." is replaced (T5-02, T5-09).
- **Filmstrip**: a native scroll-snap rail of every claims-cleared screen, `role=region`, `tabindex=0`, `aria-label`. It renders only when 3 or more cleared screens exist (T5-07).
- **One "Product context" footnote.**
- **Closing band**: `closing_scene('product')` in the world colors.
- **Siblings**: three cards, each in its own world with its icon and window plate (T5-14).
- Story copy is sticky (`position: sticky; top: calc(88px + 8vh)`) at 1024px+ wide and 760px+ tall (T9-07).

**Looks Max** (violet dusk)
- The hero is `looks-max-screen-4`, cropped below its "Deep Scan / Real Insights" band, with its 2–3px blue edges trimmed (T4-02, T4-05).
- Signature chapter *(copy: "Inside the scan")*: a sticky `detail-screen-6`, with detail crops of the Overall Evaluation and Hair & Beard cards. Each crop displays at half its source width or less.
- No filmstrip until more screens are supplied.

**IQ Max** (cobalt morning)
- The hero is `iq-max-detail-screen-4`, a straight frame, so the glaring cyan poster no longer opens the page. `screen-1` moves to the filmstrip at a controlled size inside the cobalt stage with a `--iq-rim` mint rim. Keep the mascot (T4-06).
- Signature chapter *(copy: "From focus to routine")*: detail-screen-4, then detail-screen-6, joined by a drawn connector.
- The filmstrip has 3 screens.

**Sleep Max** (moonlit night)
- A full-bleed indigo opening, with the H1 and deck centered and the badges directly under them, so the CTA sits within 900px. `sleep-max-screen-4` rises from the bottom into the glow (T5-10).
- `detail-screen-3` (the empty profile) is removed (T5-06).
- Signature chapter *(copy: "Soundscapes")*: two distinct detail crops from screen-4, the master volume and fade-out, and the noise list, framed differently from the hero.
- A populated screen is requested from the founder.

**Fitness Max** (ember)
- The hero is `fitness-max-screen-2`, cropped below "Just Tell Your Coach", with its 2–3px white right strip trimmed.
- Signature chapter *(copy: "A day in the log")*: a triptych of chat (screen-2), meal (detail-3, with its ≈6px top band and ≈5px right strip trimmed) and streak (detail-5), using the counter-motion from §5.
- The disclosure appears once: "On the App Store and Google Play as Only Fitness."
- The story intro is rewritten to describe the chapter.

**Platform `/platform/`**
1. **Opening** [blue hour] *(copy: "The app factory: Engineering, Management and Marketing Max.")*
   - Copy is top-aligned on the left, with `.status.vision`.
   - On the right, the `platform_map(variant='platform')` SVG on a dark stage, with the four icons as the lit sun core.
   - The legend and caption are visible in the first viewport. The SVG has a text alternative: an ordered list in `<figcaption>`, connected with `aria-describedby`.
   - The arrows are bottom-pinned in a flex column (T6-10).
   - One partnership link. Fixes T6-03, T6-12.
2. **Modules**
   - At 1150px+ wide and 760px+ tall, the map is pinned in the left column while the three module sections scroll on the right. Each module has a display numeral, its name, `.status.vision`, and a large outlined, decorative, `aria-hidden` stage word (BUILD, OPERATE, GROW).
   - The panels stay unfilled, with hairlines.
   - The per-module "Discuss X Max" links are removed (T6-05).
   - **Mobile:** a compact vertical map (four icons, a glowing line, three outlined nodes) of 60svh or less, with each numeral inline above its label (T6-09).
3. **How products inform the direction** [editorial]
   - The canonical three-step sequence lives here only (T6-06).
   - The "Build ↓ Operate ↓ Grow ↓" row is removed (T6-11), and so is the outline pill that duplicated the close (T8-04).
4. **Close** — `closing_scene('corporate')`, with the partnership action as primary on this route. Then the footer.

**Company `/company/`**
1. **Opening** [first light] *(copy: "Solarity AI is led by founder Ata Turhan, based in Irving, Texas.")*
   - The founder print at 340px, the existing third-person paragraphs as deck and body, and one "Connect with Ata →".
   - The duplicate card link is removed.
2. **Team credits** [credits]
   - Names in Manrope 500 at 22–24px, in three columns (two on mobile), tracking −0.02em or looser, directly under the founder.
   - No roles, portraits or monograms (T7-03, T3-03).
3. **The story so far** [proof]
   - A four-icon strip, "Four apps, available on iOS & Android", linking to each product.
   - Dates render only when the founder confirms them. The © year is never presented as a founding year (T7-04).
4. **Principles**: one editorial statement at `--type-chapter`, condensed from the existing principles (T6-06).
5. **Close**: corporate, with no repeat portrait. Then the footer.

**Investors & Partners `/investors-partners/`**
1. **Opening "screening room"** [blue hour] *(copy: "Four AI self-improvement apps, available on iOS and Android.")*
   - On desktop, two columns: the title at `--type-chapter` on the left; the deck, both actions and a one-line index on the right.
   - Index: Portfolio ↓ · At a glance ↓ · Partnerships ↓ · Questions ↓ · Founder ↓. Each link has one continuous underline (T6-08).
   - Below, the **showroom**: four identical 3:4 window plates at 240–260px under a warm overhead elliptical spotlight, each with an under-glow in its world. Each frame has its icon, name, category and "App Store ↗ · Google Play ↗".
   - At 1440×900 and 1280×800, everything is fully visible, frames included. Full images open in Enlarge.
   - **Mobile:** the title plus one large plate of 200px or more in the first viewport, then a keyboard-operable rail of the four (T4-04, T6-01).
2. **At a glance** [proof, lit panel, ledger] — verified rows only:

   | Key | Value |
   |---|---|
   | Company | Solarity AI LLC · Irving, Texas |
   | Founder | Ata Turhan (links to Company) |
   | Portfolio | 4 apps on the App Store and Google Play (linked) |
   | Model | In-app purchases, as listed in the stores (reverify before publishing) |
   | App factory | Engineering Max · Management Max · Marketing Max, with the `.status.vision` chip |

   Team size, founding year, stage or raise, metrics and the deck request render only when supplied. No placeholder markup. The duplicate "4 store-listed apps" is removed.
3. **Today / Ahead** — two cards that replace the thesis list and the paper vision aside (T6-02, T1-02):
   - Today: lit, in the evidence register, with the four icons and the store availability.
   - Ahead: dashed and unfilled, with the vision chip and a link to Platform for the three-step argument.
4. **Partnerships**: 2×2 tiles with the signature interaction and no numbers. The heading is sticky in the split.
5. **Questions**: native `<details>`, unnumbered, animated in P9.
6. **Booking close** (the sunrise reprise):
   - Left column: the statement, a 140px founder print, "Ata Turhan, Founder", "View available times ↗" as the sun-core primary and "Email Ata ↗" as the secondary.
   - Right column: the one recognizable reprise, a 2.39:1 sunrise plate of 600 CSS px or less wide (served from the existing variants, about 1200w at 2x), lazy-loaded and captioned "Conceptual brand artwork".
   - The helper line becomes sr-only new-tab text. No meeting length or response time is stated (T8-07).

**Careers `/careers/`**
1. **Opening** [blue hour]
   - A single-line title replaces "Good work. Shared ambition." *(copy)*.
   - The repeated founder portrait is removed. The team credits block makes "people" plural.
   - "Explore opportunities ↓" is the primary action.
2. **Roles** [editorial]
   - Whole-row links with a caps discipline label, the title at `--type-sub` and tags in meta.
   - Apply appears on hover and `:focus-within` and is always visible on touch. Keep the careers.js role preselection.
   - "Full role descriptions (Google Drive) ↗" (T10-12).
   - The duplicate "Find your place" eyebrow is removed.
3. **Application** [first light]
   - The left column is sticky at `top: 112px`: the heading, the email with an inline copy icon button, and an honest "What happens next" that describes FormSubmit's verification and confirmation without promising delivery or a reply.
   - The form sits in a lit panel with 56px controls, `--radius-control` and `--control-border`, and a `--focus` ring.
   - Helper text appears only on the URL fields. The LinkedIn placeholder is shortened.
   - The disclosure stays adjacent to the button.
   - FormSubmit, the CAPTCHA, the honeypot and the email fallback are unchanged (T10-10).

**Contact `/contact/`**
1. **Meeting frame** [blue hour]
   - The headline at `--type-chapter` on the left *(copy)*.
   - On the right, a founder card in a lit panel: a 180px print, "Ata Turhan · Founder · Irving, Texas", and "Book a conversation ↗" (primary) beside the email address with a ghost "Email Ata ↗" and a copy icon button, all at equal height.
   - Both actions sit above the fold at 1440×900 and 1280×720 without a fragment.
   - The glow is masked so it has no edge (T10-08, T1-06).
2. **Topics**: a 2×2 grid of tiles on desktop, stacked on mobile, with Investment conversations first and the arrow beside each label (T10-09).
3. **One no-collection sentence** next to the email: "Email opens your mail app; this site does not collect messages." `#data-note` remains a quiet, visible closing note. The query-derived subject behavior in contact.js is unchanged.

**404**
- Content is aligned to the standard `.wrap` edge.
- A single-line title *(copy)* over a horizon backdrop: the pre-blurred light field, decorative, with `fetchpriority=low` and not lazy.
- Recovery links become tiles without numbers.
- The interior arrival applies.
- Remove the dead `recovery_art()` (ux_content.py:105) and its `.recovery-art` rule (T10-11).

---

## 7. Roadmap

Each phase is one pull request, or two where marked. Each follows `Commit Rules.md` (one logical change per commit), passes the site-checks workflow and the Cloudflare preview check, and is smoke-tested with `python deploy/smoke_test.py <preview>.pages.dev` before merge. **Every phase includes a contact sheet at 390 and 1440 for founder review.** The order is by investor impact, subject to dependencies.

### P0. Baseline, decisions and contracts (S; documentation and tooling only; no change to `dist/`)
- **Renders.** All 12 pages at 360, 390, 768, 1024 and 1440, plus 1280×800 and 1920×1080 for Home, Investors and the footer. One pass with reduced motion. Stored outside `dist/`.
- **Lighthouse baseline.** Mobile and desktop presets, median of 3 runs, on the branch preview for `/`, `/investors-partners/`, `/apps/looks-max/`, `/apps/iq-max/`, `/platform/` and `/company/`.
- **Founder specimen.** A local, unpublished HTML page with:
  - type options A1, A2 and B on three frames (Home hero, Investors opener, a product hero)
  - product world swatches on stages using the real screens
  - a mockup of the header floating over the sky
- **DESIGN_SYSTEM.md revisions:**
  - Motivated light is allowed. The rule that borders define structure is retired.
  - Scene types.
  - Evidence and vision registers.
  - The image budget.
  - The motion contract from §5.
- **Founder material request** sent (§9).
- **Acceptance:**
  - Decisions are recorded in DESIGN_SYSTEM.md: display face, world hues, the portfolio wall replacing the explorer, the header behavior, and the copy-approval process.
  - Baseline numbers are recorded in PRODUCTION_AUDIT.md.
  - `git diff dist/` is empty.

### P1. Light, color and materials (M)
- **Files:** `foundation.css`, `chrome.css`, `company.css`, `contact.css`, `careers.css`, `home.css`, `products.css`, `accessibility.css`, `build_site.py:82`, `optimize_images.py` (grain and light field), `check_site.py`.
- **Deliverables:**
  - The §3.2–3.6 tokens and all hard-coded colors retinted.
  - Paper retired from all four panels: they become lit panels, with the vision aside switched to the outline register.
  - The `.lit` glow mechanism applied at the existing focal points (explorer device, founder, CTAs, contact).
  - The ring removed. The contact glow edge fixed.
  - Grain and the light field.
  - The horizon rule.
  - The new button, chip and control-border components.
  - Radii migrated.
  - Forced-colors and print maps.
- **check_site changes:**
  - The radius regex updated.
  - Hex colors rejected in `border`, `outline` and `box-shadow` outside `foundation.css`.
  - A static contrast matrix over declared token pairs.
- **Acceptance:**
  - In 1440 and 390 renders, each glow core lifts the scene tone by 18 or more sRGB levels and falls to 2 levels or fewer at its box edge, with no visible step.
  - No raised surface has G greater than R.
  - Zero literal border hex values outside `foundation.css`.
  - The contrast matrix passes (text 4.5:1 or better; display headings and controls 3:1 or better).
  - All suites pass.

### P2. Type system (M)
- **Files:** `foundation.css` and every page CSS file, `build_site.py` (preload, `_headers`), `font-sources.json`, the font and license files, `check_site.py`, and all `visual_*.py` (couplets, eyebrows, numerals, captions).
- **Deliverables:**
  - The display face and both fallbacks.
  - The scale, tracking, deck and body tokens.
  - The two label styles.
  - Two-thirds of the eyebrows cut and the rest in sentence case.
  - The numeral system, with mono removed.
  - `text-wrap: pretty` and the `&nbsp;` set.
  - The caption helper.
  - Couplets removed outside the Home hero and close, with the `.em` class.
- **Acceptance:**
  - No raw `clamp()` font size outside `foundation.css` (check).
  - Font bytes are 60 KB or less per route.
  - No word collisions in renders: "Melik Kaplan", "Products today", "for a daily" and "shared ambition" read correctly at 390 and 1440.
  - No single-word last line in the ledes listed under T3-10.
  - On a throttled first visit (Slow 4G, cache disabled), CLS is 0.01 or less and mobile LCP is no more than 100ms above P0.
  - Home is decided with and without the display preload by measurement.

### P3. Opening frame and header (M)
- **Files:** `visual_home.py`, `home.css`, `chrome.css`, `visual_chrome.py`, `scripts/navigation.js`, `optimize_styles.py` (DYNAMIC_CLASSES), `test-navigation.cjs`, `check_site.py` (hero `sizes` and preload kept in exact agreement).
- **Deliverables:**
  - The Home opening, desktop and mobile, as in §6.
  - The header state switch.
  - Opaque interior headers.
  - The ghost Contact with an `[aria-current]` style.
  - The wordmark tracking.
  - The mobile bar.
  - The static design of the mobile menu overlay. Its motion comes in P9.
- **Acceptance:**
  - At 1024, 1280, 1440 and 1920, the hero's bottom edge equals the viewport bottom (within the clamp), the credits row is fully visible, and the H1 is two lines ending left of the climber.
  - At scrollY = 0 the header has no `backdrop-filter`, and sampled nav and Contact text is 4.5:1 or better against the darkest and lightest underlying sky pixels.
  - The header is solid once the hero has passed, with no layout shift.
  - The 390 caption chip is 4.5:1 or better.
  - The navigation tests pass, including no-JS and no-IntersectionObserver fallbacks.

### P4. Closing frame, footer and CTA hierarchy (M)
- **Files:** a new `closing_scene` helper, `build_site.py` (`cta()`), `visual_chrome.py`, `chrome.css`, `foundation.css`, `visual_home.py`, `visual_company_upgrade.py`, `visual_strategy.py`.
- **Deliverables:**
  - The closing scene on Home, Apps, Platform and Company.
  - The footer colophon, with the sun crop generated.
  - The labels standardized.
  - Duplicate CTAs removed: the hero "Explore our products", the strategy link row, the platform outline pill and the footer duplicates.
- **Acceptance:**
  - Each page closes once: no footer slogan, and a gap of 120px or less before the close at 1440.
  - Home `main` holds 4 or fewer links to `/contact/` and Platform's 3 or fewer.
  - The footer signature spans the wrap within ±2% at 1024, 1440 and 1920.
  - The mobile footer is 0.75 viewport or shorter.
  - Footer targets stay 44px.

### P5a. Product asset pipeline (M)
- **Files:** `optimize_images.py`, the image manifest, `research-assets/downloaded-assets.json` and its provenance, `asset-sources.json`.
- **Deliverables:**
  - Per-asset crop records (edge insets and headline-band removal) applied to derivatives only. The originals in `dist/assets/` are untouched.
  - `SCREEN_WIDTHS` set to 240/400/600 now, and 400/800/1200 after the re-fetch.
  - AVIF for screens.
  - `ICON_WIDTHS` gains 224/320.
  - Portrait 4:5 variants at 320/480/640.
  - Official store badge SVGs, stored as `dist/assets/` originals with their source recorded.
  - **The native-resolution re-fetch** of the same listing images. Compare each one perceptually against the current 600px files, record checksums, and have the founder confirm. If a listing has changed, keep the current files and fall back to founder exports.
  - An edge-sampling check that rejects any derivative whose outer 8px band differs from the adjacent interior by more than 40 levels.
- **Acceptance:**
  - The edge check passes on every derivative.
  - The crops are listed in the manifest.
  - No published file is unreferenced.
  - The display caps stay in force until the founder confirms the re-fetch.

### P5b. Product stage, Home wall, Apps index and product openings (L; may split into Home+Apps and Products)
- **Files:** a new `stage`/`plate` helpers module, `products.css`, `home.css`, `visual_catalog.py`, `visual_products.py`, `product_explorer.py` (retired), `build_site.py` (APPS gains `crop_focus` and `hero_screen`), `check_site.py`.
- **Deliverables:**
  - The plate and stage with product worlds.
  - The Home wall, replacing the explorer and the evidence strip. The new check_site contract: four product links in APPS order, each with an icon and a store-link pair, while the `hero-product` credits contract is kept.
  - The Apps lineup and world bands, with stretched links and compact mobile cards.
  - The product-page openings for all four apps: the name as H1, badges, the IQ hero swap, the Sleep night hero, and the status dot removed.
  - The ↗ exemption for `a.store-badge`.
- **Acceptance:**
  - Below the hero at 1440×900, all four apps are visible at once; at 390 the 2×2 grid fits within 1.1 viewports.
  - No stage shows a box edge.
  - Every screen has the same plate.
  - The store badges are within the first 900px on every product page (Sleep included).
  - IQ is no longer the brightest surface in its first viewport.
  - Rendered screens never exceed source pixels: rendered CSS width × DPR ≤ the width of the source variant used.

### P6. Investor narrative (L; 6a Investors, 6b Platform plus the Home diagram)
- **Files:** `visual_company_upgrade.py`, `visual_strategy.py`, `visual_sections.py` (`platform_map`), `ux_content.py` (FAQ), `company.css`, `home.css`, `visual_home.py`.
- **Deliverables:**
  - The showroom, ledger, Today/Ahead, partnership tiles, FAQ restyle and booking close with the reprise.
  - The shared `platform_map` SVG in its Home and Platform variants.
  - Module splits.
  - The mobile map.
  - The legend system replacing the scattered retractions.
  - The approved headline rewrites on Investors, Platform and Apps.
- **Acceptance:**
  - On Investors at 1440×900 and 1280×800, the title, actions, index and all four framed apps are fully visible. At 390, one plate of 200px or more is in the first viewport.
  - Vision surfaces are never brighter than evidence: compare the sampled mean luminance of the panels.
  - Every vision element carries `.status.vision`.
  - The three-step argument appears on Platform only.
  - At most one numbered sequence per page.
  - Platform's caption and legend are within the first viewport.
  - The SVG has a text alternative read correctly by a screen reader (VoiceOver and NVDA spot check).

### P7. Product signature chapters (L)
- **Files:** `product_story.py`, `visual_sections.py`, `products.css`, `ux_components.py`.
- **Deliverables:**
  - The four signature chapters and their detail crops.
  - The filmstrips (IQ and Fitness).
  - Sticky story copy.
  - The world-colored closing bands and sibling cards.
  - Sleep's detail-screen-3 removed.
  - Product-specific headings checked against `product-story-evidence.json`'s copy rules.
- **Acceptance:**
  - No chapter leaves a void taller than 50% of the viewport at 1440 (render check).
  - Every image used is listed as claims-cleared.
  - Each product page differs from the others in chapter structure, not only in nouns: verify side by side.
  - Filmstrips scroll by keyboard.

### P8. People and secondary routes (M)
- **Files:** `visual_team.py`, `visual_sections.py`, `visual_company_upgrade.py`, `visual_contact.py`, `visual_careers.py`, `ux_content.py`, `contact.css`, `careers.css`, `company.css`.
- **Deliverables:** Company, Contact, Careers and 404 as in §6, including the founder print everywhere and the credits block.
- **Acceptance:**
  - The founder portrait appears at most once per route and nowhere on Careers.
  - On Contact, both actions are above the fold at 1280×720.
  - On 404, content aligns to x = 88 at 1440.
  - The careers and contact Node tests pass unchanged, including FormSubmit, the honeypot and email encoding.

### P9. Motion layer (M; 9a arrival, reveals and progress; 9b view transitions, menu, screening room, FAQ, rows)
- **Files:** a new `design/system/motion.css`, `build_site.py` (`style_sources`, the `.line` wrappers, `--i`, view-transition names), `scripts/gallery.js`, `test-gallery.cjs`, `check_site.py`, CLAUDE.md, DESIGN_SYSTEM.md.
- **Deliverables:**
  - Everything in §5.
  - The screening-room dialog: full viewport, world-tinted, controls overlaid. Enlarge becomes a corner chip on the existing `a.screenshot-open`, which keeps its native href.
- **check_site:** assert that `@keyframes`, `animation-timeline`, `@view-transition` and `animation:` appear only inside the no-preference guard, and that no keyframe animates opacity on `.progress-hero-image` or an H1.
- **Acceptance:**
  - Reduced-motion renders match motion-complete renders pixel for pixel, within a 0.5% diff threshold.
  - Mobile LCP is no more than 150ms above P0. If it regresses, drop the H1 mask below 768.
  - CLS is 0.01 or less.
  - The JS delta is 1.5 KB or less.
  - The gallery tests pass: focus return, Escape, arrow keys, modified click.
  - Firefox shows a complete static page.

### P10. Founder-material upgrades (rolling; one PR per material)
- **Hi-res hero:** add `SUNRISE_WIDTHS` of 2400/3000/3720, update the check_site 1860×845 contract, the preload and `sizes`, and raise the hero clamp to 1080.
- **Native or clean screens:** raise the display caps (heroes to 440–520px) and add the screening room's native-width detail mode.
- **Populated Sleep screen.**
- **Founder statement, signature and profile:** the founder statement component.
- **Editorial portrait.**
- **Roles and portraits:** a uniform 3×2 roster.
- **Metrics and dates:** the proof band and dated story strip.
- **Vector logo:** one inline SVG lockup across header, footer, favicon and OG image.
- **Privacy and terms:** links in the footer.

**Medium and low items by phase:**
- P1: T1-03, T1-04, T1-05, T1-06, T10-07.
- P2: T3-06 (copy), T3-07, T3-08, T3-09, T3-10, T3-11, T3-12, T3-13, T10-02.
- P3: T2-04, T2-06, T10-03, T10-04, T10-05.
- P4: T8-03, T8-04, T8-05, T8-06.
- P5: T4-05, T4-06, T5-08, T5-10, T5-11, T5-12, T5-13 (superseded by the wall), T5-15, T5-16, T5-17.
- P6: T6-07, T6-08, T6-09, T6-10, T6-11, T6-12, T8-07.
- P7: T5-09, T5-14, T9-07.
- P8: T7-04, T10-08, T10-09, T10-10, T10-11, T10-12.
- P9: T4-07, T4-08 (Enlarge chip), T9-04, T9-05, T9-06 (superseded), T9-08, T9-09, T9-10, T9-11.
- P10: T2-05.

---

## 8. Critical and high problems mapped to phases

| Id | Severity | Fixed in | Note |
|---|---|---|---|
| T1-01 | Critical | P1 (system), applied P3–P8 | Light tokens and scene tones in P1; every page's scenes in their phase |
| T3-01 | Critical | P0 (decision), P2 | Display face chosen from the specimen |
| T4-01 | Critical | P5b | Lit stage and plate replace `.screenshot-stage` everywhere |
| T8-01 | Critical | P0 (scene types), P3–P8 | Checked page by page in each phase's contact sheet |
| T1-02 | High | P1 | Paper retired; vision moves to the outline register (finished in P6) |
| T2-01 | High | P3 | |
| T2-02 | High | P3 | |
| T2-03 | High | P2, P3 | |
| T3-02 | High | P2 | |
| T3-03 | High | P2 | |
| T3-04 | High | P2 (structure), P6 (copy) | |
| T3-05 | High | P2 | |
| T4-02 | High | P5a, P5b; complete in P10 | Crops now; matched clean exports later |
| T4-03 | High | P5a | Founder confirms the re-fetched assets |
| T4-04 | High | P6 | Showroom reuses the P5b stage |
| T5-01 | High | P1 (tokens), P5b | |
| T5-02 | High | P7 | |
| T5-03 | High | P5b | |
| T5-04 | High | P5b | |
| T5-05 | High | P5a (assets), P5b | |
| T5-06 | High | P7 (removal), P10 | |
| T5-07 | High | P7, P10 | |
| T6-01 | High | P6, P10 | Metrics render only when supplied |
| T6-02 | High | P1 (chips), P6 | |
| T6-03 | High | P6 | |
| T6-04 | High | P6 | |
| T6-05 | High | P6 | |
| T6-06 | High | P6, P8 | |
| T7-01 | High | P8 (interim print), P10 | |
| T7-02 | High | P8 (interim), P10 | |
| T7-03 | High | P8 (credits), P10 | |
| T8-02 | High | P4 | |
| T9-01 | High | P0 (contract), P1 (tokens), P9 (enforcement) | |
| T9-02 | High | P9 | |
| T9-03 | High | P9 | |
| T10-01 | High | P2/P4 (interim fixes), P10 | Logo is never redrawn without the brand owner |

---

## 9. Founder-supplied material and approvals

Nothing in this plan invents claims, metrics, UI, portraits or roles. These items are needed from the founder. Until each arrives, the layout closes the gap; it never shows a placeholder.

**Approvals (P0 and as each phase lands)**
- The display face (A1, A2 or B) and reversing the October 13 one-family decision.
- The product world hues.
- The portfolio wall replacing the explorer, and the app order.
- The DESIGN_SYSTEM.md rule changes (light, motion).
- Every proposed headline marked *(copy)*.
- The founder print crop, mat and any grade.
- Reverification of the business-model wording, "In-app purchases", before it appears as a ledger fact.

**Assets**
- A higher-resolution hero master of the same approved composition, at least 3720×1690. Later, a portrait crop of at least 1170×2530 for a full-bleed mobile hero.
- Confirmation that the re-fetched native-resolution screenshots match the current listings, or full-resolution official exports.
- Matched clean UI captures: same device and status bar, no marketing overlay, at least 1170px wide.
- A populated Sleep Max screen from a seeded demo account, with clearly labelled sample data.
- More claims-cleared screens for Looks Max and Sleep Max.
- An editorial founder portrait set: environmental, warm directional light, wide and tight crops, at least 1600px.
- Approved roles and a consistent portrait set for all six team members.
- The vector logo, a decision on the angular SOLARITY wordmark versus a refined horizontal logotype, and approval of a reduced-ray small mark.

**Content**
- A first-person founder statement of one to two sentences, a scanned signature and a public profile URL.
- Verifiable metrics with source and date: launch dates, store ratings, downloads, press or partners with permission.
- Founding year, stage or raise, and the deck-request policy, if they are to be published.
- How to state team size, if at all.
- Privacy and Terms documents, and official social profile URLs.
- Optional: job-poster content, so role descriptions can live on the page instead of the Google Drive link.

---

## 10. Verification

**Rendered review**, which is the definition of done for every phase:
- Widths **360, 390, 768, 1024, 1440**, plus 1280×800 and 1920×1080 for the Home hero, the Investors showroom and the footer signature.
- Two passes: one with `prefers-reduced-motion: reduce` (the static final frame), and one with motion, captured after the load sequence settles and while scrolling in steps.
- Real-device spot checks: iPhone at 3x (hero and screenshot softness) and a mid-range Android (scroll smoothness).
- Browsers: Chrome (view transitions and scroll timelines), Safari on iOS and macOS, and Firefox (static fallbacks).

**Performance budgets**
- Lighthouse, mobile and desktop presets, median of 3 runs, on the branch preview for the six routes in P0:
  - Performance: 95 or better on mobile, 98 or better on desktop.
  - Accessibility, Best Practices and SEO: 100.
  - Mobile LCP: 2.5s or less, and no more than 150ms above the P0 median.
  - CLS: 0.01 or less.
  - TBT: 50ms or less.
- Static byte budgets, added to check_site as errors:

  | Budget | Limit | Measured baseline |
  |---|---|---|
  | Inline route CSS, gzip | 14 KB or less on Home, 12 KB or less elsewhere | 5.8–9.3 KB |
  | HTML, gzip | 24 KB or less | 9.0–16.0 KB |
  | Fonts | 60 KB or less per route | |
  | New JS | 1.5 KB or less in total | |
  | Images above the fold on Home | Hero AVIF plus icons only | |

  Wall plates are lazy-loaded. The Investors showroom is eager, with accurate `sizes`.
- Paint: with 4x CPU throttling in Chromium, scrolling Home and Investors shows no paint over 4ms per frame. No fixed overlays and no `backdrop-filter` after the hero.

**Contrast**
- The static token-pair matrix in check_site: text 4.5:1 or better, display headings and non-text controls 3:1 or better.
- Rendered pixel sampling of the darkest and lightest pixels under the glyph box, at 1440 and 390, recorded per phase:
  - hero nav and Contact
  - hero lede and headline
  - caption chip
  - text near every glow core
  - world tints on their stages
  - vision chip text
  - text in the dawn close
  - text over the light field on 404 and in the menu
- Forced-colors and print spot checks on every page.

**Keyboard and assistive technology**
- A full tab pass on all 12 pages. The focus ring (`--sun-core`, 2px, 4px offset) is visible on every surface and world.
- Stretched-link cards are one tab stop, with badges as separate stops.
- Filmstrips and rails are focusable regions that scroll with the arrow keys.
- Sticky headers, rails and story columns never hide the focused element (WCAG 2.4.11); `scroll-padding-top` is updated if bars change.
- Menu: Escape, `inert` and focus return. Dialog: focus return, arrow keys, Escape. `<details>` opens with Enter and Space.
- The skip link works.
- VoiceOver and NVDA read the platform diagram's text alternative and the ledger as a definition list.

**Reduced motion**
- With reduce emulated, nothing animates or transitions and there is no view transition.
- Screenshots match the motion-complete state.
- The check_site guard assertion (P9) passes.

**Existing suites**, run after every change from the project root:
```sh
.venv\Scripts\python.exe build_site.py
.venv\Scripts\python.exe check_site.py
.venv\Scripts\python.exe -m unittest test_optimize_styles.py test_site_urls.py
node --test test-navigation.cjs test-contact.cjs test-gallery.cjs test-careers.cjs test-copy.cjs
```
Also required: the site-checks workflow (rebuild equals the committed `dist/`), the Cloudflare preview check, and `python deploy/smoke_test.py <branch>.solarityai-landing-page.pages.dev` before asking to merge. Whenever a contract moves (explorer radios, hero widths, the ↗ exemption, radii, weights, `HOST_FILES`), update check_site and the matching test in the same pull request, and replace each removed assertion with an equivalent one. Never claim a Lighthouse or rendered result that was not run.

---

## 11. Risks and mitigations

| Risk | Mitigation |
|---|---|
| Effects tip into gimmick (grain, glows, title cards) | One device per viewport, the letterbox and flares already rejected, grain at 4% or less, and founder review of each phase's contact sheet. |
| Light ends up too timid again, so the site reads as average again | Measured acceptance: glow cores at least 18 levels above the tone, and rendered review is mandatory. |
| Contrast fails over light, sky or color | A token matrix in check_site plus rendered sampling at fixed points. No strong glow core behind body copy. |
| The display face hurts LCP or swaps visibly | The subset is capped at 34 KB, the fallback is metric-matched, and the preload decision on Home is made by measurement. |
| Bigger stages expose soft 600px screenshots and the 1860px hero | Hard caps (340px screens, 960px hero, 560px mobile art) until P5a confirmation and P10 materials arrive, plus the render-time DPR check. |
| Founder decisions block the work | The P0 specimen offers defaults. Token and component work continues on defaults, which are cheap to reverse. Copy changes ship only after approval. |
| check_site contracts drift (explorer, hero, ↗ rule, radii, weights, licenses) | Contract and test change in the same PR. No assertion is removed without an equivalent replacement. |
| Uneven browser support (view transitions, view timelines, `interpolate-size`, `@starting-style`) | The static page is complete. Everything is behind `@supports` and the motion guard. Firefox and older Safari get instant cuts and the full content. |
| Sticky layouts on short laptops | Sticky splits only at 1024 or 1150px+ wide and 760px+ tall. Otherwise sections stack. |
| Store badge compliance | Official artwork unmodified, minimum size and clear space respected, trademark lines, and a documented, narrow ↗ exemption. |
| Copy drifts into implied traction or "live" | Copy review against CONTENT_REGISTER.md and product-story-evidence.json. "Available", never "live". The © year is never presented as a founding year. Ledger rows appear only when verified. |
| Low-end phone performance | No fixed or blended overlays. Grain baked into scene backgrounds. Scroll-linked effects limited to the hero drift (half strength on mobile) and the progress hairline. |
| Inline navigation hash and DYNAMIC_CLASSES regressions | The build regenerates the hashes, `header-over-hero` is registered, and test-navigation covers no-JS and no-IntersectionObserver. |
| Publish-set rules (`dist/` is deployed and must stay referenced) | Never delete `dist/` before a build. New textures, badges and fonts are referenced from pages or listed in `HOST_FILES`. The optimizer's stale-file pruning is relied on for hashed variants only. |
| Maintenance sprawl | Components as Python helpers (stage, plate, `closing_scene`, `platform_map`, ledger, provenance, scene), tokens only in `foundation.css`, motion only in `motion.css`, and check_site rules for each. |


## Appendix A: Full problem register


### T1 Light, color and atmosphere

The sunrise is the only light on the site. After about 800px every route becomes one near-black field divided by hairlines. The existing glows were specified without being seen and never render. The neutrals lean olive, one pale sand accent does every job, and cream paper slabs become the brightest surfaces at key moments. This theme sets up the light model that every other theme depends on.


#### T1-01: No light system after the hero: every route is one flat near-black field (critical)

- **Pages:** home, apps, apps-looks-max, apps-iq-max, apps-sleep-max, apps-fitness-max, platform, company, investors-partners, careers, contact, 404
- **Evidence:** home-desktop-01: the hero fades into flat (17,17,15) by y≈790-800. Later home backgrounds measure (17,17,15) for the explorer, (25,24,19) for the strategy band and (12,14,11) for the footer: four darks within 13 levels of each other. 5 of 6 desktop and 7 of 8 mobile home slices are flat near-black with text. platform-desktop-01, company-desktop-01 and investors-partners-desktop-01 open as type on #11120f, and solar-ascent is referenced only in visual_home.py:15. foundation.css:12 gives body a flat var(--bg). The faint exceptions (strategy band #191812, investor proof #1a1c17, contact and careers glows, footer #0c0e0b) lift pixels by only 5-9 levels. The no-decoration and borders-only rules come from DESIGN_SYSTEM.md:62-63. CINEMATIC_REFINEMENT.md:9 claims lighting continues across routes, but :52 admits no rendered review.
- **Problem:** The site's one cinematic idea, light rising over darkness, is used once and then dropped. After the first screen, every route renders as default dark mode: one flat value, 1px rules and text. Nothing visual ties the 'solar' brand to the products, the vision, the founder or the closing ask. The pages differ in layout but share one lifeless surface.
- **Investor impact:** Within one scroll the site reads as a stock dark SaaS theme. The drop is steepest on Investors, Company and Platform, the pages investors open next, so the hero looks borrowed rather than part of a considered brand world. This is the main reason the founder perceives the site as 'average'.
- **Fix direction:** Build a light model as tokens in foundation.css, with colors sampled from the hero:
- Sun core ≈#ffcf7a, ember ≈#d9782f and haze ≈#f5dfbb.
- A cool navy-slate taken from the image (≈(9,23,34) to (32,39,48)), not violet.

Apply it this way:
- A fixed key light from the upper right (≈85% x, matching the sun), plus large soft radials at 12-35% alpha placed only at focal points.
- An ember bounce light at the bottom of long pages.
- A deliberate dark-to-dawn tonal ramp in place of four near-identical darks.
- Fine grain as a 1-4 KB tiled noise background on the scene layers at 3-5%. Do not use a fixed, blended full-viewport overlay, which costs paint on low-end phones.

For the interior openings (Platform, Company, Investors), use a CSS horizon glow or a pre-blurred derivative of the master of a few KB, never the 1860px image.

Image budget: the recognizable sunrise appears in the home hero plus at most one reprise (see T8-02). Crops where the scene is recognizable stay under ≈600 CSS px and carry the 'Conceptual brand artwork' caption.

Other requirements:
- Revise DESIGN_SYSTEM.md:62-63 so that motivated light is an allowed system element.
- Tune every value from rendered 1440px and 390px screenshots.
- Recheck AA contrast wherever text sits over light.
- Give forced-colors and print a plain fallback.
- Keep check_site.py's home-only hero contract.

#### T1-02: Cream paper panels are the brightest surfaces on Platform, Investors and Company, and they come in two corner shapes (high)

- **Pages:** platform, investors-partners, company
- **Evidence:** The #f1ede3 paper panels are:
- the platform map (company.css:49, square corners)
- the investor vision aside (:142, square)
- the booking card (:183, square)
- the founder card (:13, --radius-lg)

In platform-desktop-01 the paper measures (241,237,226), about 16:1 against the page, and fills half of the first viewport. On mobile each panel becomes a full-width cream block (platform-mobile-01/02, investors-partners-mobile-04/07). DESIGN_SYSTEM.md defines --radius-lg for cards, so the square panels break the system's own rule. Text on paper is at least 5.6:1, so legibility is fine; the problem is mood and emphasis. The panels also appear as hard rectangles with no transition (M13).
- **Problem:** Large light rectangles read like a light-theme component library dropped onto a dark film set. On Investors they put the brightest surface on the vision and booking blocks rather than on the product evidence. The mixed radii show the panels were not designed as one system.
- **Investor impact:** The platform vision, the company's growth story, is presented as a beige worksheet, and the founder booking reads as a CMS callout. Both look low-budget at the moments that matter most.
- **Fix direction:** Retire paper as the default surface. Replace it with a lit dark material, warm smoked glass:
- a gradient from ≈#1f1913 to #120f0c
- a 1px inner top highlight, rgba(255,220,170,.10)
- a warm hairline
- a local amber bloom
- a single panel radius token

Use paper at most once on the site, as a deliberate contrast moment, if at all. If panels animate, unfold them with clip-path on entry, only under no-preference, and keep content readable once in view. Recheck AA for paper-label and paper-text on any paper that remains. Vision panels must use the outlined vision register and never be the brightest surface (T6-02).

#### T1-03: Existing glows, rings and hover light were specified unseen and never render (medium)

- **Pages:** home, careers, contact
- **Evidence:** - home.css:63: the explorer glow is #e8c18a13 fading to 06. It renders at (19-22,20-23,15-18) against (17,17,15) beside the phone in home-desktop-02, effectively invisible.
- careers.css:10: the #b8793322 glow is mostly hidden behind the portrait; samples read (14-15,14-15,12-13).
- home.css:89: the strategy ring is #e7c6961a with ≈1-2% shadows and lifts pixels only 2-6 levels. It shows as faint arcs, (31,28,21) on (25,24,19), crossing 'Build the product.' in home-desktop-03 and reads like a compression artifact.
- foundation.css:65: the primary hover glow is #edc78e14, about 8% alpha.
- --shadow-portrait (0 24px 60px #0007) does not show on near-black.
- CINEMATIC_REFINEMENT.md:52 and DESIGN_SYSTEM.md:13 confirm there was no browser rendering.
- **Problem:** The October cinematic pass specified light at 1-13% alpha without seeing the result, so it left no visible trace. The one motif that does show, the ring, reads as an artifact rather than a design element. This is the mechanism behind T1-01's flatness and the product sameness in T5-01.
- **Investor impact:** None of the intended warmth reaches the viewer, so the products and the founder sit on dead black with no emphasis. The faint ring looks like a rendering error.
- **Fix direction:** - Replace the existing values with --glow-sun and --glow-ember tokens at real strength: a core of ≈rgba(255,190,110,.28) fading out over 40-60% of the radius.
- Place glows only at focal points: behind the portfolio device, the founder, the primary CTA and the app rail.
- Make each glow larger than its box so it falls off naturally.
- Remove the ring, or redraw it as an intentional sun arc at 30-40% strength.
- Keep strong glow cores away from body copy, and verify AA wherever text sits over light.
- Add rendered review (screenshot sampling at 1440px and 390px) to the definition of done for every light value.

#### T1-04: Neutral tokens lean olive-green (medium)

- **Pages:** home, apps, platform, company, investors-partners, careers, contact, 404
- **Evidence:** In foundation.css:5, green is the top channel in:
- --surface #1a1c17, --surface-raised #252820, --line #373b31 and --ink #1c241c
- the footer #0c0e0b (chrome.css:25) and the mobile menu #171a14 (chrome.css:46)
- the outline border #727469 and the dialog greys #64695a/#74796d

Measured on screen: the investor proof panel is (26,28,23), a khaki-grey, and the 'View available times' button is (29,36,28), green-black on beige. The base #11120f is effectively neutral, so the cast shows on raised surfaces, lines, outline borders and ink.
- **Problem:** Raised surfaces, rules, outline borders and the ink color carry an olive cast. It dulls the warmth around the amber accents and puts a green-black button on the investor page's final action.
- **Investor impact:** The cast is felt more than seen: the site looks slightly dull and 'off' rather than rich. Premium brands are exact about their blacks.
- **Fix direction:** - Rebase the neutral ramp on a warm ember axis, for example bg #0f0d0b, surface #18140f, raised #221c16, line #3a3027 and ink #1a140e.
- Retint the hard-coded greys (#727469, #64695a, #74796d, #80786b).
- Update theme-color in build_site.py:82 so the browser chrome matches.
- Keep --muted and --dim as warm ivory-greys (≈#c9c0b2, #a99f91), verified at ≥4.5:1 on every surface.

One token change in foundation.css propagates through the cascade.

#### T1-05: One flat sand accent does every job, so nothing reads as light (medium)

- **Pages:** home, platform, company, investors-partners, careers, contact, 404
- **Evidence:** A single --accent #edc78e (foundation.css:5) drives eyebrows (:41), text links (:71), heading emphasis (:17), primary button fill (:64), focus rings (:34), numerals, step labels and arrows. In home-desktop-04, the eyebrow, the Build/Operate/Grow labels, the arrows, three links and the H2 second line are all the same sand. platform-desktop-02 and investors-partners-desktop-04 show the same even sprinkling.
- **Problem:** When every accent is the same pale value, the accent stops working as light. There is no hierarchy between the most important action and a list number, and the pale sand never reaches the luminous gold of the hero sun or the logo.
- **Investor impact:** Color is sprinkled evenly instead of directed, so the eye is not led to the investor CTA or the key claim.
- **Fix direction:** Build a solar tonal ramp:
- --sun-core ≈#ffcf7a: one focal element per viewport, such as the primary CTA or one key word. It also bridges to the logo's yellow (T10-01).
- --gold #e9b56a: active states.
- --sand #d6bf9a: small labels and eyebrows.
- --bronze ≈#9c7446: rules, numerals and decorative lines. Non-text only, because it is ≈4.4:1 and fails AA for small text.

Set body links in ivory with an amber underline, and AA-check every pair.

#### T1-06: The contact glow is clipped by its box, leaving a vertical edge, and the ambient glows are static (low)

- **Pages:** contact, careers, home
- **Evidence:** contact.css:15 places radial-gradient(ellipse at 72% 0, #bb814515, transparent 72%) on a box inset by the negative gutter, so the gradient is still ≈40% strength at the box edge. In contact-desktop-01, pixels step from (26,22,19) at x≈1410 to (17,17,15) at x≈1418, and the glow's top edge sits on a hard line at y≈620. The careers glow reaches transparent inside its box and shows no edge. The home strategy band's hard seams (y≈652 and y≈825) are a deliberate section step; feathering them is optional. The strategy rings are frozen decoration.
- **Problem:** A visible gradient edge near the right of the viewport, and ambient lights that add atmosphere without life.
- **Investor impact:** Small, but a discerning viewer notices this kind of edge and reads it as template work.
- **Fix direction:** - Size the contact gradient with closest-side or explicit radii, or feather it with mask-image, so it reaches transparent inside its box. Check at 1024px, 1440px and 1920px.
- Optional: let local glows rise once on section entry (opacity and scale on the pseudo-element, under 1.2s).
- Optional: drift the rings with scale or translate. Rotation is invisible on concentric circles.
- Use one composited layer per section, and no motion under reduced motion.

### T2 The opening frame (home hero)

The approved sunrise is strong art in an ordinary frame. A dark frosted header slab cuts the sky. A fixed 820px height lets the fold slice the next strip. The scrims grey the cloud sea. A narrow three-line headline sits over a 16px lede with three CTA styles. The master is too small for Retina. The mobile opening leads with a low-contrast disclaimer.


#### T2-01: The home header lays a dark frosted slab across the sunrise sky (high)

- **Pages:** home
- **Evidence:** chrome.css:4-5 sets body[data-page='/'] .site-header to #10120fcc/#10120f9e (≈62-80%) with backdrop-filter blur(12px) and margin-bottom -88px. In home-desktop-01 there is a hard seam at y=88: at x=1100, (66-73,50-52,32-41) at y≈85 jumps to (150-155,109-113,76-87) at y≈90-92, and at x=1300, #54361a jumps to #f0ad45. home-mobile-01 shows the same band at y0-153 (2x): (80,64,39) over (213,137,75). The hero's own overlay (home.css:17) does not darken the top, so the band comes from the header itself. CINEMATIC_REFINEMENT.md item 7 introduced this as the 'legible dark fallback'. navigation.js has no scroll handling.
- **Problem:** A cinematic opening needs the image edge to edge with the navigation floating on it. Here the navigation sits on a translucent slab that boxes in and dims the brightest part of the sky, the look of a default sticky-header template.
- **Investor impact:** The first impression on the most-visited page loses its film-still quality at the moment an investor decides whether the brand is premium.
- **Fix direction:** - On Home at scroll-top, make the header fully transparent with no blur.
- Protect legibility with a top-down scrim baked into the hero: ≈55% at y=0, fading over ≈140-160px.
- Without a scrim, the 13px #c4c3b9 nav links and the Contact pill over (155,109,76) sky are ≈2.6:1. Measure AA at nav-text height at 1440px, 1024px and 390px.
- Switch to the solid header once the hero leaves the viewport. Use ≈10 lines in the already-inlined navigation.js: an IntersectionObserver class toggle, with the class registered in optimize_styles DYNAMIC_CLASSES (inline-script hashes regenerate at build). Alternatively, use animation-timeline: scroll() inside @supports.
- The current solid bar is the fallback without JS or scroll-timeline support. The switch is instant under reduced motion, and the header height stays constant.
- While over the hero, render the header Contact as a ghost button (T10-03).

#### T2-02: A fixed 820px hero lets the fold slice the next strip (high)

- **Pages:** home
- **Evidence:** home.css:4 sets min-height:820px. At 1440x900 the image ends near y≈800 in flat (17,17,15). The 'From ambition / to everyday practice' strip and the app names are cut in half at y860-900 (home-desktop-01), and on taller monitors more of the next section shows. The only proof line on the page, 'Four apps. iOS & Android.', is 12px (home.css:21) and sits at or below the fold.
- **Problem:** The fold lands at an arbitrary point instead of a designed composition edge. The first frame looks accidental, and its only proof point is half cut off.
- **Investor impact:** The opening frame decides premium or template, and a sliced, letterboxed composition reads as unfinished.
- **Fix direction:** - Set min-height:100svh, clamped to ≈720-1080px, so the image's bottom fade resolves exactly at the fold.
- Replace the half-cut strip with a designed bottom edge inside the hero: a quiet credits row of the four authentic icons at 32-36px, plus a scroll cue.
- For the credits row, reuse verified wording ('Four apps. iOS & Android.' or 'Available on iOS & Android'). Do not write 'live' unless launch status is reverified (CLAUDE.md).
- Move 'Explore our products' into the scroll cue.
- Note that a taller hero increases the pressure on resolution (T2-05).

#### T2-03: Hero type and actions lack hierarchy: a three-line stack with a stranded word, a 16px lede, three CTA styles and duplicate gold pills (high)

- **Pages:** home
- **Evidence:** home-desktop-01 shows 'Building for / human / potential.':
- The forced br.hero-desktop-break (visual_home.py:21) plus max-width:13ch (home.css:7) leave 'human' alone in a ≈410-500px column at 88.6px (6.15vw).
- The second part is weight 400 in #f5dfbb against 500 in #f5f1e8 (home.css:7-8), which reads as an ambiguous half-step.
- Vestigial font-family/font-weight:400 span rules at home.css:8 and :92 remain from the removed Georgia emphasis.
- The 16px lede (home.css:9) leaves a ≈5.5:1 jump with no tier in between.
- The eyebrow 'SOLARITY AI · BUILT AROUND YOU' repeats the wordmark 130px above it.
- The actions use three treatments over two rows: a gold pill, a 14px 'Discuss a partnership →' and a 13px 'Explore our products ↓' (home.css:10-13).
- The header Contact pill (236,194,136) and the hero CTA (238,199,142) are two identical gold primaries.

The mobile hero already sets two lines.
- **Problem:** The approved cinematic artwork carries a conventional left-column SaaS hero: a ragged three-line headline, an ambiguous weight shift, a caption-sized lede and a split action cluster that competes with a second gold pill.
- **Investor impact:** This is the first typographic frame investors see, and it sets the 'average' impression. The investor path is less clear than it should be.
- **Fix direction:** - Remove the forced break and set 'Building for / human potential.' as two lines.
- Size it to ≈7-7.5rem (≈112-120px) at 1440, not 9-11vw, which reaches ≈900-1100px and overruns the climber at x≈1050. Verify at 1280px, 1440px and 1920px.
- Use one weight. Mark emphasis by color only, or by optical size or italic if a display face is approved (T3-01).
- Add a 20-22px lede tier with line-height ≈1.5, at most 34ch wide.
- Use one primary pill and one secondary ghost pill of the same height on one row. Move 'Explore our products' into the scroll cue (T2-02).
- Drop or rewrite the eyebrow.
- Delete the vestigial span rules.
- Keep the directional gradient for AA.

#### T2-04: The hero scrims dull the cloud sea and give the sky a cool cast, and the sunrise's warmth stops at the fold (medium)

- **Pages:** home
- **Evidence:** home.css:17 layers two scrims:
- a 90deg scrim of #101313: c7 (78%) at 0, a8 (66%) at 27%, 5e (37%) at 47%, clear at 70%
- a 0deg bottom fade over 25% of the height

The upper-left navy is dark by design: the source reads ≈(9,23,34) to (32,39,48), and solar-ascent-artwork.json records 'dark left space for headline'. Where the two scrims overlap, though, a source pixel of (252,160,64) in the glowing cloud sea renders as (66,48,28), about 25% brightness. Ridges at x≈390-1000 lose 20-40%. The cool #101313 casts a blue-grey of (15-19,20-24,23-27) behind the headline in an otherwise warm image. The app rail below then sits on flat (17,17,15) with no warm spill.
- **Problem:** The scrims protect the text but suppress the lower-left light and cool the warm sky. The handoff from sunrise to products is a fade to dead black with no afterglow.
- **Investor impact:** This wastes part of the strongest asset and pushes the hero toward a stock 'image right, text left' template.
- **Fix direction:** - Taper the horizontal scrim so it clears by ≈50% of the width.
- Add local protection behind the copy block: a radial gradient centered on the text plus a soft text-shadow.
- Change the scrim color to a warm umber matching the new base.
- Once the hero is 100svh (T2-02), shorten the bottom fade so it resolves at the fold.
- Extend a long amber afterglow (6-12% opacity, over 400-600px) under the next scene. A thin horizon line is optional.
- On the lightest underlying pixels, verify 4.5:1 for the 16px lede and the 13px links, and 3:1 for the headline.
- Keep the grading in CSS. An exported graded variant changes the approved master, whose provenance records only resizing and format conversion, so it needs founder approval.

#### T2-05: The approved hero master is too small for Retina and large displays (medium) *(needs founder material)*

- **Pages:** home
- **Evidence:** research-assets/solar-ascent-approved.png and source-assets/solar-ascent.webp are both 1860x845 (solar-ascent-artwork.json), and SUNRISE_WIDTHS stops at 1860 (optimize_images.py:34). Covering 1440x820 needs ≈1805 CSS px, which is ≈3610 device px on a 2x laptop, so the image renders at about half density. A 2560px monitor upscales it even at 1x. The 1x captures cannot show this; it follows from the source dimensions. Every proposed full-bleed or larger use (T2-02, T2-06, T8-02) makes it more pressing.
- **Problem:** The single most important image looks soft on the climber, the stair edges and the cloud detail on the screens investors typically use, such as Retina MacBooks and 4K monitors.
- **Investor impact:** Softness in the hero undercuts 'premium' before any copy is read.
- **Fix direction:** - The founder supplies or approves a higher-resolution export (≥3720x1690) of the same approved composition, by re-render or quality upscale, reviewed for fidelity.
- Add 2400, 3000 and 3720 AVIF/WebP variants.
- In the same change, update the optimize_images.py variants, the exact-match preload and sizes, and check_site.py's hero contract (1860x845 intrinsic size, eager loading, fetchpriority).
- Never change the composition or replace the art.

#### T2-06: Mobile opening: a short art strip, a low-contrast disclaimer as the first words, then flat black (medium)

- **Pages:** home
- **Evidence:** home-mobile-01:
- The art is only 460px tall (home.css:133) and fades to 87% black by 19% from the bottom.
- The first text under the header is 'Conceptual brand artwork' at top:106-114px (home.css:126, :133; y≈231 at 2x), over cloud ranging (100,72,55) to (245,166,61).
- The #e2dfd5 caption measures ≈6:1 at its left end but 1.1-2.7:1 under 'artwork', relying only on text-shadow 0 1px 5px #000 (home.css:18). That fails WCAG AA.
- Below the image, the lede and three stacked actions sit on flat black at y≈860-1340 (2x), followed by an ≈80-100 CSS px empty gap.
- The sunrise fills ≈40-45% of the first screen.

check_site.py requires the disclosure text but not its position.
- **Problem:** On phones the opening frame starts with a caveat that fails AA contrast, and its cinematic part ends at mid-height.
- **Investor impact:** Investors often first open shared links on a phone. The mobile first impression is noticeably cheaper than desktop and leads with a hedge, not the story.
- **Fix direction:** Now:
- Raise the art to ≈560-620px and overlay the headline and lede on its lower fade.
- Use one full-width primary button and one secondary link, and move 'Explore' into a scroll cue.
- Move the caption to the lower-right edge inside the bottom scrim, or just below the image, at 12px and ≥4.5:1. If it must stay in the sky, give it a dark-glass chip (rgba(12,9,6,.55)).
- Remove the trailing gap.
- Keep the sizes attribute and the preload in exact agreement.

Later, only once T2-05 delivers a larger master: export a portrait crop of the same composition centered on the climber and sun at ≥1170x2530, then move to a 100svh full-bleed frame. The current master is 845px tall, about a 3x upscale on a 3x phone.

### T3 Typography: voice, scale and setting

Manrope at weight 500 with heavy negative tracking does every job. Sixty-six one-off clamp() sizes converge on 56-70px. Fixed tracking collapses word spaces. Nearly every heading is the same two-line couplet with three emphasis colors. There is no deck tier. Eyebrows, labels, numerals, small sizes and captions drift from page to page. Type carries most of the premium signal on the text-led investor pages.


#### T3-01: One typeface in one weight: the site has no display voice (critical)

- **Pages:** home, apps, platform, company, investors-partners, careers, contact, 404, apps-looks-max, apps-iq-max, apps-sleep-max, apps-fitness-max
- **Evidence:** foundation.css:4-5: Manrope is the only face, and --font-display and --font-editorial alias --font-body. The CSS uses weight 500 in ≈31 declarations, 600 in 9 and 400 in 7-9; 200 exists only in the @font-face range. Every heading is weight 500, tracked -0.048 to -0.062em (foundation.css:14, 18-19; home.css:7, 35, 70, 91, 115; company.css:44 at -0.055em). CINEMATIC_REFINEMENT.md:10 replaced system Georgia, which was not a designed display face and looked cheap, with one family, and font-sources.json records 'One family for body and display'. That removed the inconsistency by removing all contrast. home-desktop-01, apps-desktop-01, company-desktop-01, careers-desktop-01 and investors-partners-desktop-01 all set headlines in the same medium-weight, tightly tracked sans as the nav, buttons, captions and body.
- **Problem:** Display, editorial and UI type all resolve to Manrope at weight 500. Headlines have no register of their own, which is the default voice of SaaS and Framer templates. The text-led scenes (vision, founder, investors, closing) have no headline that feels authored.
- **Investor impact:** Type is the main premium signal on a text-led corporate site. Investors see this typographic voice on many startup sites, so nothing signals craft, taste or a premium consumer brand.
- **Fix direction:** Make it a founder decision using a side-by-side specimen of the home hero, the investors opener and one product hero:
- A: one OFL display face for h1, statement h2s, chapter numerals and pull quotes only, with Manrope kept for UI and body. Candidates: Newsreader or Fraunces (variable with opsz; instance or limit the axes so a Latin subset stays ≈30-50 KB), or Instrument Serif (a static single cut).
- B: Manrope only, with separated registers: display at weight 250-300 with near-zero tracking, UI at 500-600.

Either way:
- Self-host, fingerprint, and preload only on routes where the face is above the fold.
- Add a metric-matched fallback with size-adjust and ascent/descent overrides (T3-12).
- Choose font-display deliberately. Optional can leave the LCP h1 in a fallback on a first visit, so prefer swap with a matched fallback for the display face, or test a throttled first visit.
- Record the choice in font-sources.json, the license file, DESIGN_SYSTEM.md and CINEMATIC_REFINEMENT.md, and update check_site.py's type and weight rules.
- Do not substitute the stacked lockup lettering.

This reverses the documented October 13 decision, so it needs founder sign-off but no new content.

#### T3-02: Headline scale is flat: 66 one-off sizes converge on 56-70px, and the product name outranks its section title (high)

- **Pages:** home, apps, apps-looks-max, apps-iq-max, apps-sleep-max, apps-fitness-max, platform, company, investors-partners
- **Evidence:** design/system has 66 distinct font-size clamp() declarations, and --type-display/--type-heading are used only by the h1/h2 defaults. At 1440:
- The product hero h1 (products.css:54) and the story h2 (products.css:78) both resolve to 63.4px (apps-looks-max-desktop-01/02).
- Home: explorer h2 63px (home.css:35), product h3 67.7px (home.css:70), which outranks its own section title; on mobile it is 44px against ≈38px (home.css:135-136, home-mobile-02).
- Strategy 60px, founder 64px, closing 56px, catalog h2 64px.
- The hero is 88.6px, only ≈1.4x a section heading.
- **Problem:** Page titles, chapter openers and mid-page sections all speak at the same volume, and hierarchy is inverted inside the portfolio. No moment reads as a title card, so the page has no crescendo and no quiet passages.
- **Investor impact:** Uniform loudness makes long pages feel like a stack of equal slides. Investors scanning get no signal of what matters most.
- **Fix direction:** Consolidate into ≈5 fluid tokens in foundation.css:
- title: the hero and one moment per page, capped near 7-7.5rem on Home so a two-line headline stays left of the climber
- chapter: ≈4-4.75rem
- section: ≈2.75-3.25rem
- sub: ≈1.75-2rem
- deck: see T3-05

Then:
- Map every h1 and h2 to a token.
- Allow at most two statement moments per page (opening and close).
- Set product h1s at least one step above the story h2s.
- Set the explorer's product name at sub size, or make it the deliberate display title and set the h2 as a deck.
- Add a check_site.py rule that rejects raw clamp() font sizes outside foundation.css.

#### T3-03: Fixed negative tracking collapses word spaces and crowds letters (high)

- **Pages:** company, investors-partners, apps-iq-max, home, contact, platform
- **Evidence:** Tracking values: h1 -.062em (foundation.css:18), h2 -.048em (:19), hero -.055em (home.css:7), team names -.045em (company.css:32), module numbers -.065em (company.css:74), footer -.065em. Mobile overrides change only size (company.css:266). Visible collisions:
- company-desktop-03 and company-mobile-03: 'Melik Kaplan', 'Eren Öz' and 'Ali Yılmaz' read as single words.
- investors-partners-mobile-01: 'Productstoday.' and 'Possibilityahead.'
- apps-iq-max-desktop-01: 'fora daily'.
- home-desktop-05: 'Build on a shared ambition.'
- contact-desktop-01 and contact-mobile-01 show the same collapse.
- **Problem:** One em value tuned for very large type crushes word spaces at 40-64px and on mobile. A pass meant to make the type feel premium makes it look over-compressed and hard to read.
- **Investor impact:** Collapsed word spaces in the team roster and the investor headline look like a rendering error and make the site feel less finished than it is.
- **Fix direction:** - Add tracking tokens tied to the scale: ≈-0.035em title, -0.025em chapter, -0.015em section, -0.005em sub, 0 for body and deck.
- Never use negative tracking under ≈28px or on uppercase.
- Add +0.02-0.04em word-spacing to display headings where tracking is tight.
- Keep the team roster at -0.02em or looser.
- A metric-matched fallback (T3-12) prevents an Arial fallback from making this worse.

#### T3-04: Nearly every heading uses the same two-line couplet, with three conflicting emphasis colors (high)

- **Pages:** home, apps, platform, company, investors-partners, careers, contact, 404
- **Evidence:** About 20 h1/h2 headings are two short period-terminated phrases split by a forced <br>:
- 'One ambition. / Your next step.' (apps-desktop-01)
- 'Products today. / Possibility ahead.'
- 'Good work. / Shared ambition.'
- 'The people. / The purpose.'
- 'Broad ambition. / Specific choices.'
- 'Build the product. / Learn from the work.'
- 'Tell us what / you bring.'
- 'This page / is not here.'
- 'Human potential. / Thoughtfully built.' in every footer (visual_chrome.py:60)

Company alone stacks five couplets plus the footer's. The second line is:
- gold on Platform, Investors, Careers, Contact and 404 (company.css:45; contact.css:52 recolors .muted to accent on 404)
- grey .muted #c4c3b9 on Apps (visual_catalog.py:43) and in the home explorer (product_explorer.py:35), where it reads as disabled
- plain white on Company
- #f5dfbb in the hero (home.css:8)
- **Problem:** One typographic beat repeats on almost every heading, and its emphasis color has no fixed meaning. The repetition becomes a template signature, and the gold loses meaning through overuse.
- **Investor impact:** Investors scanning several pages see the same headline shape again and again. It reads as formula, which makes Platform, Thesis and Team feel interchangeable.
- **Fix direction:** - Keep the split-line device for one or two signature moments: the home hero, and possibly the investors opener or the closing.
- Vary the other headlines: single-line statements, a deck above a shorter title, a display-size single word, the product name as the title, a question.
- Give gold emphasis one meaning, and never use grey for headline emphasis.
- Rename .muted inside headings to a semantic class.
- Changes to wording need founder approval but no new facts.

#### T3-05: There is no deck tier: openers drop to 16px, and body text is small, loosely leaded and grey (high)

- **Pages:** home, company, platform, investors-partners, apps-looks-max, apps-iq-max, apps-sleep-max, apps-fitness-max, careers, contact
- **Evidence:** The .lede token (foundation.css:42, up to 1.25rem) is overridden to 16px on Company (company.css:6), Platform (:46), Investors (:106) and the product heroes (products.css:58). The home hero lede is also 16px (home.css:9). Contact and Careers keep 20px, so the same element changes size between pages (contact-desktop-01 vs company-desktop-01). Body text is 14-16px in --muted #c4c3b9 at line-height 1.8 (22 declarations) or 1.85 (6). Next to 60-95px headlines there is nothing between 25px and 16px, so the thesis and platform module copy reads like fine print (home-desktop-04, platform-desktop-02).
- **Problem:** A premium editorial page needs a strong deck between the headline and the body. Here the type jumps from a 90px headline to faint 16px text with airy leading, so the texture looks thin and the argument gets lost.
- **Investor impact:** The substantive investor argument (thesis, platform explanation, founder context) sits in the weakest-looking text on the page, and readers skim past it.
- **Fix direction:** - Define --type-deck at ≈1.375-1.5rem on desktop and 1.15-1.25rem on mobile, weight 400, line-height 1.4-1.45, color var(--text).
- Use it for every opener and key thesis paragraph, and remove the per-page overrides.
- Raise desktop body text to 17-18px at line-height 1.55-1.6.
- Reserve --muted for secondary copy.

#### T3-06: Headline copy repeats abstract vocabulary instead of stating facts (medium)

- **Pages:** home, apps, company, careers, contact, investors-partners, apps-looks-max, apps-iq-max, apps-sleep-max, apps-fitness-max
- **Evidence:** Examples: 'Your ambition. Your daily practice.' (home-desktop-02), 'One ambition. Your next step.' (apps-desktop-01), 'Build on a shared ambition.' (home-desktop-05), 'Individual talent. Shared ambition.' and 'Broad ambition. Specific choices.' (company-desktop-02/03), 'Good work. Shared ambition.' (careers-desktop-01), 'A shared ambition. A real conversation.' (contact-desktop-01) and 'Another ambition in mind?' (apps-looks-max-desktop-04). 'Ambition' appears on ≈18-19 source lines across build_site.py, visual_*.py, product_explorer.py and ux_*.py.
- **Problem:** Most headings are aphorisms built on the same abstract words, so verbally they read as generated filler and dilute the few concrete facts the site has.
- **Investor impact:** Investors scan headlines, and lines that could belong to any company give them nothing to hold on to.
- **Fix direction:** - Keep aphorism for the hero and the final close only.
- Rewrite investor-critical headlines around facts the site already publishes. Examples:
  - Investors: 'Four AI self-improvement apps, available on iOS and Android.'
  - Apps: 'Four apps for appearance, mind, sleep and fitness.'
  - Company: 'Founded in Irving, Texas, by Ata Turhan.'
- Remove 'shared ambition' from at least two of its three places.
- The founder approves the copy. No new facts are needed. Use 'available' rather than 'live' unless launch status is reverified.

#### T3-07: Eyebrows are overused and often repeat the heading or the brand (medium)

- **Pages:** home, platform, company, investors-partners, careers, contact, apps-looks-max
- **Evidence:** Eyebrows per page: Investors 9, Platform 7, Company 6, Careers 6, Home 5 plus 2 strategy labels and the explorer category, product pages 4. Redundant examples:
- 'FIND YOUR PLACE' directly above 'Find your place.' (visual_careers.py:75, careers-desktop-02)
- 'SOLARITY AI · BUILT AROUND YOU' just below the wordmark (visual_home.py:20)
- 'CAREERS AT SOLARITY AI', 'THE COMPANY'
- the seven-word 'WHY THE TWO PRODUCT LINES BELONG TOGETHER' (platform-desktop-03)

Capitals are typed into about 30 strings (build_site.py:54 and others), and product_story.py:112 calls .upper().
- **Problem:** Nearly every section opens with the same gold all-caps line, and several repeat the heading. The repetition flattens the rhythm and pads the copy.
- **Investor impact:** Repeated gold labels give the pages a uniform, theme-like cadence that adds to the template impression.
- **Fix direction:** - Cut eyebrows by about two-thirds.
- Remove any that duplicate the heading or the wordmark, and keep the rest to 4 words or fewer.
- Write the strings in sentence case and apply uppercase in the base .eyebrow rule. check_site.py:335 already keeps size and tracking in the base style.
- Do not reintroduce chapter numerals site-wide. The October 13 pass removed redundant numbering.

#### T3-08: The label system uses seven tracking values, letter-spaced lowercase and two casings (medium)

- **Pages:** apps, apps-looks-max, apps-iq-max, apps-sleep-max, apps-fitness-max, home, all pages (footer)
- **Evidence:** Positive tracking values in use:
- .035em (products.css:83, home.css:18)
- .04em (products.css:13)
- .055em (chrome.css:31)
- .06em (company.css:22)
- .07em (home.css:96)
- .075em (home.css:69)
- .1em (foundation.css:41)

The product-identity eyebrow puts .1em on mixed-case names at 13px (products.css:53), giving spaced-out 'Looks Max' and 'IQ Max' (apps-looks-max-desktop-01, apps-iq-max-mobile-01). Footer group headings are tracked lowercase (home-desktop-06). Product categories are sentence case on /apps and uppercase in the home explorer (home.css:69). DESIGN_SYSTEM.md:56 claims 'One style'.
- **Problem:** Letter-spacing lowercase breaks word shapes. Seven near-identical values and two casings for the same data make the label layer look accidental.
- **Investor impact:** The labels sit next to product names and icons, the most important brand elements, so the spaced-out names read as amateurish.
- **Fix direction:** Allow only two label styles:
- Caps label: uppercase via CSS, 11-12px, weight 600, +0.1-0.14em.
- Meta label: mixed case, 13-14px, 0 tracking.

Set product names as meta labels, or as a 20-24px name, and never track them. Use one casing for categories everywhere. Footer group headings use the caps label.

#### T3-09: Numerals have no shared system: a system monospace on the investor thesis and six numbered sequences (medium)

- **Pages:** investors-partners, platform, company, 404
- **Evidence:** company.css:139 sets the investor thesis indices in --font-mono (ui-monospace, SFMono-Regular, Consolas), so they render as slashed-zero Consolas in investors-partners-desktop-02/03 and mobile-03, and differently on each platform. Elsewhere: partnership indices are Manrope 13px (company.css:160), FAQ numbers 12px dim (:174), and platform .module-num is clamp(2.5rem,4vw,4rem), ≈57.6px, accent, weight 400, -.065em (:74). Numbered sequences appear on Company principles, Platform modules and steps, the investor thesis, partnership topics, the FAQ (01-05) and the 404 recovery list. The .mono class appears unused.
- **Problem:** Numbering uses four unrelated styles, and the core of the investor narrative gets a platform-dependent code font. Six numbered lists, most with no real order, add to the kit feel.
- **Investor impact:** The thesis list gets the most off-brand typography on the page, and the page looks assembled from parts.
- **Fix direction:** - Remove --font-mono from the thesis list.
- Define one numeral voice in lining, tabular Manrope:
  - a large chapter numeral, kept for the platform modules where it already works
  - one small 12-13px index style with a single color rule
- Remove numbering where order means nothing (FAQ, partnership topics, principles).
- Keep numbering for real sequences only (Build, Operate, Grow).

#### T3-10: No line-break control on body copy, so single-word last lines recur (medium)

- **Pages:** investors-partners, apps-looks-max, apps-iq-max, apps-fitness-max, platform, apps
- **Evidence:** text-wrap:pretty is applied only to .vision-description (home.css:9); headings get balance (foundation.css:14). Single-word last lines:
- 'tab.' under the booking button (investors-partners-desktop-05)
- 'availability.' in the store fine print (apps-looks-max, apps-iq-max and apps-fitness-max desktop-01)
- 'suggestions.' (apps-looks-max-desktop-02)
- 'interests.' (investors-partners-desktop-04)
- 'products.' (platform-desktop-03)
- 'build.' (apps-mobile-01)
- 'audience.' (investors mobile-03)
- **Problem:** Single-word last lines under short paragraphs leave holes in otherwise clean text blocks. Premium typography treats this as a basic polish item.
- **Investor impact:** A discerning reader sees repeated single-word last lines as unfinished typesetting.
- **Fix direction:** - Add text-wrap:pretty globally to p, li, dd, figcaption and .lede in foundation.css. It degrades gracefully.
- Use non-breaking spaces where a phrase must not break ('new tab', 'iOS & Android').
- Optionally add a check_site.py rule for very short final lines in key ledes.

#### T3-11: Small-text sizes 1px apart and about 38 one-off measures (low)

- **Pages:** all pages
- **Evidence:** Small-text tokens: --text-2xs 12, --text-xs 13, --text-sm 14, --text-md 15, --text-base 16, --text-lg 18 and --text-xl 20px (foundation.css:5). Many 12px dim (#aaa99f) captions ('Enlarge', store fine print, status lines) sit 1-2px away from 14-15px body text (contact.css:40, careers.css:35). There are 38 distinct ch max-width values from 13ch to 58ch, many of them deliberate heading measures.
- **Problem:** Captions, labels, help text and body differ by size noise rather than clear roles, and column edges vary slightly between sections.
- **Investor impact:** Minor on its own, but it adds to the impression of a site assembled pass by pass.
- **Fix direction:** - Collapse the small sizes to three roles: caps label 12px, meta/caption 14px, body 17-18px (with T3-05).
- Replace the ch values with ≈3 measure tokens: deck/side column, body and heading.
- Keep every required disclosure verbatim, set in one consistent caption style.

#### T3-12: font-display: optional with an unmatched Arial fallback (low)

- **Pages:** all pages
- **Evidence:** foundation.css:4 uses font-display:optional, and the stack is 'Manrope',Arial,sans-serif. No fallback @font-face with size-adjust or ascent/descent overrides exists. The preload is at build_site.py:82. The 26 KB same-origin preload usually arrives within the block window, so a miss affects only a first view on a slow, high-latency connection. The screenshots rendered Manrope, so they cannot show the risk.
- **Problem:** When the font misses its window, the page renders in unmatched Arial with tracking tuned for Manrope, which exaggerates the collisions in T3-03.
- **Investor impact:** An investor opening an emailed link on mobile data could see a cramped Arial version of the site as their first impression.
- **Fix direction:** - Add a 'Manrope Fallback' @font-face using local('Arial') with size-adjust and ascent/descent overrides derived from the font-sources.json metrics, placed second in the stack.
- Keep the preload.
- Treat any added display face the same way.

#### T3-13: Repeated image captions use several wordings and casings (low)

- **Pages:** home, apps, investors-partners, apps-looks-max, apps-iq-max, apps-sleep-max, apps-fitness-max
- **Evidence:** Variants in use:
- 'Official app imagery · Sample content' (home-desktop-03)
- 'Official app imagery · sample content' and 'Official app imagery. Sample content.' (/apps and product pages)
- 'Official promotional imagery with sample content.' (visual_company_upgrade.py:53)
- 'Official App Store imagery.' (product_story.py:114)
- **Problem:** Casing and wording drift in a repeated disclosure shows there is no shared caption component.
- **Investor impact:** Minor, but it adds to the assembled-in-passes impression.
- **Fix direction:** Render every attribution caption from one shared Python helper, with one accurate wording in sentence case and one caption class using the meta-label style (T3-08). Combine this with the consolidation in T4-08.

### T4 Product imagery and staging

The four real apps are the strongest proof on the site, but they appear as 300-340px store posters in an inert brown box. The posters come in four clashing ad art directions with baked edge hairlines and soft 600px sources. IQ's poster glares, Enlarge shows images smaller than inline, and captions and Enlarge rows sit under every image. On Investors the four ads sit on a khaki shelf with no icons or store links.


#### T4-01: Product screenshots sit small inside one inert brown box on every product (critical)

- **Pages:** apps, apps-looks-max, apps-iq-max, apps-sleep-max, apps-fitness-max, home, investors-partners
- **Evidence:** products.css:31 applies one gradient (#24211d to #111210) to .screenshot-stage and .product-story-image for every product, with no stage radius. products.css:32-34 give a 5px image radius, 340px on detail pages and 320px on the index, and one shadow (0 20px 46px #0005) that does not show on near-black. In apps-desktop-02 a 600px stage (x88-688) surrounds a 320px poster (x228-548), leaving ≈140px of dead brown on each side; in apps-looks-max-desktop-01 the stage spans x784-1352 around a 340px poster. The stage measures (36,33,28) to (17,17,15), barely lighter than the page, so it reads as an empty well. The product accent only tints the 13px label (products.css:53), and nothing animates on arrival (products.css motion is only the hover block at 151-156). The same box appears in apps-iq-max-desktop-02/03, apps-sleep-max-desktop-03 and the mobile slices. CINEMATIC_REFINEMENT.md:21 calls this 'neutral staging'.
- **Problem:** The only staging device on five pages is a slightly lighter rectangle with hard edges and no light, depth or environment. The real apps read as exhibits in a document rather than shipping software.
- **Investor impact:** These are the pages where investors check that the products are real and polished. Thumbnail-in-a-box staging makes four live apps feel like a template portfolio, the main reason the product section reads as average.
- **Fix direction:** Replace .screenshot-stage with a lit product stage in each product's color world (T5-01):
- a large-radius panel or full-bleed band with no visible box edge (mask-image feathering, still using a --radius token per check_site.py:333)
- a deep product-tinted gradient with a radial key light behind the screen
- a soft contact shadow, and a 1px inner highlight plus warm rim on the screen
- the same radius and shadow on every image
- a faint reflection only as an option, since it can look dated

Scale: enlarge hero screens to 420-480px (440-520px on detail pages) only after native-resolution assets exist (T4-03). Until then, cap them at 340 CSS px or less.

Arrival motion is transform-only (T9-03). Change framing, light and scale only; never alter the UI pixels.

#### T4-02: Four unrelated store-ad art directions, with baked-in headlines, compete with the site's own type (high) *(needs founder material)*

- **Pages:** home, apps, apps-looks-max, apps-iq-max, apps-sleep-max, apps-fitness-max, investors-partners
- **Evidence:** - Looks Max screen-4: a purple-pink gradient with a heavy serif 'Deep Scan / Real Insights' and a device frame.
- IQ Max screen-1: a pale mint/cyan plate with an owl mascot and a tilted phone cropped off-frame ('Smarter Every Day').
- Sleep Max: raw dark UI captures with a status bar and no device or headline.
- Fitness Max: black, with heavy 'Just Tell Your Coach', 'One Photo Full Breakdown' and 'Keep The Chain Alive' and an orange-glow phone.

They sit side by side in apps-desktop-02/03 and investors-partners-desktop-01, and the page H1 competes with the poster headline in apps-looks-max-desktop-01. The site's weight-500 headlines look weaker than the poster type (Ty13). CINEMATIC_REFINEMENT.md item 13 and remaining dependency 2 list a matched set of clean UI exports as still unmet.
- **Problem:** Each hero has two headlines in two type systems, and the device language changes from product to product. The index and investor row read as a collage of unrelated App Store ads.
- **Investor impact:** Inconsistent product art reads as an unmanaged portfolio and weakens the app-factory claim of repeatable quality.
- **Fix direction:** Now:
- Put every image on one uniform plate (same radius, rim and shadow), with ambient light sampled from each image's dominant tone.
- For hero and story placements, make build-time crops in optimize_images.py, limited to the device or UI region so the page H1 is the only headline (for example, remove the top headline band of Looks screen-4 and Fitness screen-2). Record the crops in the image manifest and leave the originals untouched.
- Where a crop is not clean (IQ screen-1's tilted, edge-cut phone), stage the image uncropped on a darker matte, or use a straight official frame (detail-screen-4, or screen-2, which is marked usable).
- Keep the full posters in the Enlarge dialog with a link to the store listing, and say in captions and alt text that images are cropped from official App Store imagery.
- Strengthen the site's titles so they lead (T3-01, T3-02).

Later: the founder supplies matched, clean UI captures (same device, same status bar, no overlay, at least 900px wide). Never fabricate UI or device frames.

#### T4-03: Screenshots are 600px store thumbnails that render soft and visibly compressed on Retina (high)

- **Pages:** home, apps, apps-looks-max, apps-iq-max, apps-sleep-max, apps-fitness-max, investors-partners
- **Evidence:** All screens are 600x1298 (dist/assets/*-screen-*.webp). research-assets/downloaded-assets.json shows each one fetched from mzstatic at the '600x1300bb' thumbnail size, and SCREEN_WIDTHS stops at 600 (optimize_images.py:32). The srcset is 240w/400w/600w with sizes ending at 340px, while a 2x desktop needs 680px and a 390px phone at 3x needs ≈954px. File sizes are small: fitness-max-screen-2.webp is 22,398 bytes and detail-screen-5 is 20,800 bytes. WebP ringing shows on chat-bubble text (apps-mobile-06, apps-fitness-max-mobile-01), and UI text is soft in apps-mobile-02, investors-partners-mobile-02 and apps-sleep-max-desktop-03. The faded '25 days' card in detail-screen-5 is mostly the poster's own translucent overlay.
- **Problem:** The only proof that the products exist is shown upscaled and heavily compressed, so small UI text goes mushy on every Retina device. Brighter staging will draw even more attention to this.
- **Investor impact:** Soft screenshots read as low-effort or second-hand assets, and an investor on a MacBook or iPhone notices immediately.
- **Fix direction:** - Re-fetch the same official listing assets at native size. The recorded URLs accept a larger size suffix, such as 1290x2796bb. The founder confirms they match the approved listing, and provenance and checksums are updated.
- Generate 400w, 800w and 1200w AVIF/WebP at a quality that keeps UI text crisp, and widen sizes so 2x displays get ≈800w.
- Swap any frame that is soft at the source for another claims-cleared frame.
- If the listings changed, fall back to founder-supplied full-resolution exports.
- Until then, cap display size so device pixels never exceed the source width.

Every enlargement proposed elsewhere depends on this.

#### T4-04: The investor portfolio showcase is a flat khaki shelf of 216px ads with no icons or store links (high) *(needs founder material)*

- **Pages:** investors-partners
- **Evidence:** - .investor-opening-proof (company.css:116) is var(--surface), measuring (26,28,23) khaki, with a hairline top and square corners.
- Screens are capped at 216px (company.css:123) inside a 1264px panel with ≈44px gaps and wide gutters. The posters get a radius only: no shadow, glow or edge light.
- Each item shows only a name and an arrow, with no app icon, category or store link.
- The screens start at y=675 and are ≈467px tall, so about half of each is visible in the first desktop viewport (investors-partners-desktop-01).
- On mobile (investors-partners-mobile-02) the two-column layout makes the clash plain, with the bright IQ tile beside black Fitness.
- **Problem:** The first thing investors see on their own page is a utility shelf of mismatched ads that cannot be verified at a glance, cut in half by the fold.
- **Investor impact:** Evidence that looks inconsistent reads as less real, and the missing store links make investors work to confirm the apps are live.
- **Fix direction:** Make it a showroom:
- A deep ember stage with a warm overhead elliptical spotlight, a product-accent under-glow per frame and a shared floor gradient.
- Identical frames (aspect, radius, padding) with a frame-level inner shadow so IQ does not read as a white tile. Frame treatment only, no recoloring.
- The authentic icon, category, and 'App Store ↗ · Google Play ↗' links (or compact official badges, T5-05) from APPS on each item.

To fit all four fully in the first desktop viewport, reduce the hero height, tighten padding and gaps, and show cropped 3:4 UI windows at ≈240-280px. That is within the 600px sources at 2x. A full phone-ratio image cannot fit: 280px wide is 606px tall. Show the full images in Enlarge. Request matched clean UI exports.

#### T4-05: Baked-in blue and white edge hairlines on the store images (medium)

- **Pages:** home, apps, apps-looks-max, apps-fitness-max, investors-partners
- **Evidence:** Pixel checks of the published files:
- looks-max-screen-4: 2-3px edges of (5,155,250) left and (0,157,253) right, plus near-white top rows 0-5.
- looks-max-detail-screen-6: (1,153,252) on the right.
- fitness-max-screen-2: a 2-3px pure white right strip at x597-599.
- fitness-max-detail-screen-3: an ≈6px white top band and an ≈5px light-grey right strip.
- fitness-max-detail-screen-5: a 1-2px light right hairline.
- iq-max-screen-1: a 1-2px white right edge.

The white tops of the IQ detail images are the poster's own gradient, not artifacts. On screen, the Looks edges read as an electric-blue 'focus ring' in home-desktop-02 (x891/x1190, (77,128,173)), apps-desktop-02, apps-looks-max-desktop-01, apps-looks-max-mobile-01 and investors-partners-desktop-01. A white line runs down the right of Fitness in apps-fitness-max-desktop-01 (x≈1237), apps-mobile-06 and investors-partners-mobile-02.
- **Problem:** Export borders around the hero product images read as selection outlines or sloppy crops, most visible exactly where the product is largest.
- **Investor impact:** This is exactly the kind of detail-level sloppiness a discerning viewer notices on the proof images.
- **Fix direction:** - Crop measured per-asset insets in the optimize_images.py derivatives: ≈2-3px for Looks, and up to ≈8px on the affected sides of Fitness detail-3. Record each crop in the manifest and provenance.
- dist/assets holds the only full-size originals (CLAUDE.md), so crop only the derivatives, or use a per-asset clip-path: inset() in percentages as an immediate guard.
- Re-measure after any native-resolution re-download (T4-03).
- Add a check that samples poster edges for outlier colors.

#### T4-06: IQ Max's near-white cyan poster is a glare slab on the dark site (medium)

- **Pages:** apps, apps-iq-max, investors-partners
- **Evidence:** iq-max-screen-1 measures (224-225,255,254-255), the brightest surface anywhere on the site, inside the brown box (apps-iq-max-desktop-01). On a phone it becomes an ≈628x1360-device-pixel light slab covering most of the viewport (apps-mobile-03, apps-iq-max-mobile-01/02). Two more light cyan screens follow in the story (apps-iq-max-desktop-02/03), and it is the only light rectangle on the investor row.
- **Problem:** IQ Max breaks the dark cinematic mood more than any other product, and the bright, mascot-heavy poster dominates every page it appears on.
- **Investor impact:** It breaks the mood at the point where the product should feel most premium.
- **Fix direction:** - Stage IQ in a deep cobalt environment with a soft mint/cyan rim light, so the light screens read as lit objects rather than glare.
- Do not crop screen-1 to its tilted, edge-cut phone.
- Either use a straight official UI frame as the hero screen (detail-screen-4, or screen-2 after re-download) and move the full poster to the gallery, or keep the poster at a controlled size inside the cobalt stage.
- Keep the mascot; it is IQ's official brand.
- On mobile, cap the stage at ≈60-70svh with a per-product object-position aimed at the UI region, and keep the full image in the dialog.
- Frame treatment only, with no recoloring of store art.

#### T4-07: 'Enlarge' shows the screenshot smaller than inline, inside a boxed document-style dialog (medium)

- **Pages:** apps, apps-looks-max, apps-iq-max, apps-sleep-max, apps-fitness-max
- **Evidence:** foundation.css:94 sets max-height calc(100vh - 194px), and :100 tightens it to calc(100dvh - 250px) when previous/next show. They show on every page with two or more screenshots (gallery.js:19-20). At 900px tall that is 650px of height, so a 600x1298 image renders ≈300px wide, smaller than the 340px inline image (products.css:33). The dialog is a 760px bordered panel with a toolbar, 'Close preview ×' and Previous/Next buttons (foundation.css:88-101). It enters over 180ms from opacity .7 and translateY(5px) (accessibility.css:10-11), the backdrop appears instantly with no exit, and Previous/Next swap the src directly (gallery.js:22-29). Every image also carries a separate 'Enlarge' text row. Portrait images are height-bound on landscape screens, so even near-full-height chrome gives only ≈372px.
- **Problem:** The zoom on the key product imagery feels broken and utilitarian: smaller than inline, boxed, with stacked chrome and hard cuts.
- **Investor impact:** Enlarging real app screens is the closest an investor gets to the product, and the moment feels sloppy.
- **Fix direction:** Design:
- Make the dialog a full-viewport, product-tinted screening room with the close and previous/next controls overlaid rather than stacked.
- Once native-resolution assets exist (T4-03), add a detail mode that toggles between fit-to-height and native width with vertical scroll. Alternatively, drop Enlarge on desktop once inline stages reach 440-480px and keep it for mobile.
- Replace the 'Enlarge' row with a labelled corner control that is visible on hover, on focus, and always on touch.

Motion, instant under reduced motion:
- A same-document startViewTransition with a shared name, so the thumbnail zooms into the dialog.
- Fallback: @starting-style scaling .96 to 1 with a backdrop fade, and an exit via transition-behavior: allow-discrete.
- Previous/next as a 220ms crossfade with a 12px directional slide.

Keep the native href fallback that check_site.py requires, plus focus return, Escape, arrow keys, modified-click behavior and the test-gallery.cjs contracts.

#### T4-08: Captions, Enlarge rows and hedges repeat under every image (medium)

- **Pages:** home, apps, apps-looks-max, apps-iq-max, apps-sleep-max, apps-fitness-max, investors-partners
- **Evidence:** The Looks Max page alone shows:
- 'Official app imagery · sample content' (desktop-02, y≈143)
- 'Evaluation and suggestions · sample app content' (desktop-03, y≈617)
- 'Official App Store imagery. View the listing ↗' (y≈677)
- 'In-app purchases. See the stores for current plans and regional availability.' (visual_products.py:40)
- 'Product context…' (desktop-04, y≈369)
- two 'Enlarge' rows

On apps-looks-max-desktop-02 the Enlarge and caption rows sit alone above ≈120px of empty canvas. /apps repeats a caption and an Enlarge row under all four images (visual_products.py:27-29, product_story.py:106-114). Elsewhere, the booking card adds 'Opens Ata's booking page on Google Calendar in a new tab.', and every footer ends with 'About this contact experience' (visual_chrome.py:66).
- **Problem:** Truthful labelling is required, but repeating it under every image in small grey type creates a pattern of hedges and utility chrome. Together with the vision disclaimers (T6-02), the site feels like a cautious document viewer.
- **Investor impact:** Repeated qualifiers signal defensiveness. Premium sites keep provenance honest and quiet, so the product carries the visual weight.
- **Fix direction:** Keep every fact, but present them as one quiet system:
- One provenance line per gallery or page, adjacent to the imagery ('All screens: official App Store imagery with sample content · View listing ↗'), with per-image alt text kept.
- Per-image captions become short functional titles.
- The in-app purchase note sits directly under the store badges.
- 'Product context' becomes one refined footnote above the closing band.
- Enlarge becomes a control in the image corner (T4-07).
- The booking line shortens to the ↗ cue plus sr-only '(opens in a new tab)'. check_site.py enforces new-tab text, so keep it accessible.
- Optionally, 'About this contact experience' moves to Contact only, keeping #data-note.
- Keep the Only Fitness disclosure (T5-15). Use one shared caption helper (T3-13).

### T5 Product pages and portfolio identity

The four products do not feel like four brands. They share pale near-identical accents (Fitness uses the company gold), one page skeleton, a generic three-icon feature row, homemade gold store pills and a flat text tail. The apps index opens as text. Home lists the same apps twice and then hides three of them behind tabs. Sleep Max's only story image shows an empty account.


#### T5-01: No product color worlds: pale, near-identical accents on 12-13px labels, and Fitness shares the company gold (high)

- **Pages:** home, apps, apps-looks-max, apps-iq-max, apps-sleep-max, apps-fitness-max
- **Evidence:** Accent tokens (foundation.css:5):
- --looks-accent #dcc4e5 (pale lilac)
- --iq-accent #b5d3e6 (pale blue)
- --sleep-accent #c8c9e9 (pale periwinkle)
- --fitness-accent #edc78e, identical to the company --accent

--product-accent is used only at products.css:13, :17, :53 and :83. Everything else is site gold: feature icons (:104), related arrows (:127), the 'INSIDE X' eyebrow (product_story.py:112 uses .eyebrow), the App Store primary, 'PART OF SOLARITY AI', and the identical stage (products.css:31). On Home, choosing a product recolors only the category label, bullets, a 2px underline and a button border, while the panel glow is fixed gold (home.css:63); the Looks underline is a faint lilac (home-desktop-02). The official palettes are vivid and distinct: Looks violet and magenta, IQ cobalt with cyan and mint, Sleep navy and indigo starfield, Fitness black and ember orange.
- **Problem:** Product color identity never reaches any surface. Stages, icons, rules, store actions and closings are the same on all four product pages, and Fitness has no identity color at all.
- **Investor impact:** A portfolio company should feel like a house of distinct brands under one roof. Same-colored pages suggest one product cloned four times, which weakens both the product evidence and the app-factory quality claim.
- **Fix direction:** Derive a token set per product from its official icon and screens:
- a deep 'world' color for stages and glows. Starting points: Looks #7a35c9, IQ #2a4fd0, Sleep #262c78, Fitness #ff5a1f.
- a text-safe tint, AA-checked on the new base: Looks #e3c8ff, IQ #c3f2ee, Sleep #ccd0fb, Fitness #ffc4a6.
- a line color.

Apply them through body[data-page] or [data-product] to:
- the hero gradient and stage key light
- story phase rules, feature icons, bullets, focus and selection
- related cards and the closing band

On Home, drive the explorer glow and stage tint from the existing :checked selectors with color-mix (no JS), and fade only under no-preference. Use vivid hues on large surfaces and glows only, and keep body text ivory. Reserve company gold for Solarity-level actions. The store CTA stays the most prominent control on each product page.

#### T5-02: The four product pages are one template with different nouns (high)

- **Pages:** apps-looks-max, apps-iq-max, apps-sleep-max, apps-fitness-max
- **Evidence:** Every product page runs in the same order (visual_products.py:41-53, ux_components.py:26-28):
1. breadcrumbs
2. hero (icon, eyebrow, H1, lede, status dot, two store pills, fine print)
3. 'INSIDE X'
4. 'The product experience.' (hard-coded at visual_sections.py:62)
5. 'Product context.'
6. 'Let's talk about X.'
7. 'Another ambition in mind?'
8. footer

The only variation is hero grid-area swaps (products.css:66-73) and four story column arrangements (88-93), although CINEMATIC_REFINEMENT item 16 claims distinct arrangements. There are dead zones: in apps-sleep-max-desktop-01 the right column is empty to y≈810, and apps-looks-max-desktop-02 and apps-iq-max-desktop-02/03 leave large empty half-columns. Compare apps-looks-max-desktop-04, apps-iq-max-desktop-05, apps-sleep-max-desktop-04 and apps-fitness-max-desktop-04.
- **Problem:** Column swaps do not create distinct product worlds. Clicking through four apps feels like reloading one page.
- **Investor impact:** Templated product pages make the portfolio feel like volume rather than craft, which weakens the thesis that the company builds focused, considered products.
- **Fix direction:** Give each product one signature chapter shaped by its real UI, using authentic imagery only:
- Looks: a 'scan' chapter with a sticky screen and detail crops of the Overall Evaluation and Hair & Beard cards.
- IQ: a 'focus to routine' sequence from the focus-selection screen to the routine-toggle screen.
- Sleep: a full-bleed night chapter built on distinct Soundscapes detail crops (master volume and fade-out, the noise list).
- Fitness: a 'day log' triptych of chat, meal and streak.

Also:
- Replace 'The product experience.' with product-specific headings, checked against product-story-evidence.json's copy rules.
- Vary the rhythm between full-bleed and contained sections.
- Tighten the grid so copy never floats far from its image.
- Keep the shared components for maintenance, varying scale, light and order.

#### T5-03: Home portfolio: the app list appears twice, then three of the four products hide behind form-like tabs beside a half-empty frame (high)

- **Pages:** home
- **Evidence:** The hero-evidence strip (visual_home.py:6-12, 29; home.css:19-29: 16px heading, 38px icons, 14px/12px text) is sliced at the fold. Within one scroll it is followed by a four-tab chooser repeating the same icons, names and categories (product_explorer.py). On mobile the chips repeat ≈450-500 CSS px apart (home-mobile-01/02), and the headings repeat the same idea ('From ambition to everyday practice.' then 'Your ambition. Your daily practice.'). The explorer:
- shows one product at a time and defaults to Looks Max (product_explorer.py:13), whose screen reads 'symmetry, canthal tilt, harmony, and masculi…' (home-mobile-03)
- looks like a form: four equal tabs, 40px icons, 2px underlines, a ✓ at x≈371 and a visible legend 'Choose a product to preview' (product_explorer.py:18-22, 36; home.css:38, 42, 47)
- shows a 300px device (x891-1190, home.css:78-79; 220px on mobile, home.css:136)
- bottom-aligns its copy (home.css:68), leaving a ≈760x250px void at x88-850, y570-830, so the copy and button appear only in home-desktop-03

The white Fitness icon is the brightest chip in both lists.
- **Problem:** The most valuable scroll position after the hero lists the same four names twice, then shows one product, the most polarizing category, in a settings-panel layout with no scale or light.
- **Investor impact:** Skimming investors see one app instead of the breadth of a portfolio, and the duplication reads as unedited. Shipped products end up looking like a feature tab on a template site.
- **Fix direction:** Merge the rail and the explorer into one portfolio scene.

Preferred: a portfolio wall with all four apps visible at once:
- cropped UI windows at ≈240-280px (within the 600px sources at 2x)
- authentic icon, category and store link, each linking to its product page
- each lit in its product's color world
- the in-depth explorer content lives on the product pages
- the founder decides which app leads

If the explorer is kept:
- center the copy against the device, or set the product name at display scale beside it
- 56-64px icons and an sr-only legend
- keep the native radios and labels
- give the active state a non-hue cue at ≥3:1 against inactive (luminance plate, 1.08-1.12 scale, thicker indicator or heavier name; WCAG 1.4.1), and keep the focus outline
- add a rim light and floor shadow

Either way:
- Put the icons on a uniform plate so the white Fitness icon does not dominate.
- Keep the device at 300 CSS px or less until T4-03 lands.
- Update check_site.py's contracts (four native radios, Looks checked, four hero product links) in the same change.

#### T5-04: /apps opens as text, with no icons and no lineup, and the products only peek in at the fold (high)

- **Pages:** apps
- **Evidence:** apps-desktop-01: the slogan 'One ambition. Your next step.', a floating three-line description, and a text anchor row 'Looks Max ↓ IQ Max ↓ Sleep Max ↓ Fitness Max ↓'. The only imagery is the top 110px of two posters at y790-900. apps-mobile-01 is all text until the Looks poster starts. visual_catalog.py:107-113 builds the anchor nav as text spans only, and the catalog row mastheads are a category plus the name with no icon. The official 400x400 icons exist.
- **Problem:** The page that should present the portfolio at a glance opens with a slogan and a text menu, and the authentic app icons, the strongest 'real product' signal, never appear on it.
- **Investor impact:** The first impression of the product line is generic copy rather than a confident portfolio.
- **Fix direction:** Open with a portfolio lineup, either:
- the four official icons at 96-120px, each on its color-world glow, with name and category, acting as the anchor nav; or
- a staggered 'family portrait' of four cropped screens.

Put the icon in each row masthead next to the large name, and keep the slogan secondary to the products.

#### T5-05: Store actions are homemade gold pills without store marks, identical to the header Contact button (high)

- **Pages:** apps, apps-looks-max, apps-iq-max, apps-sleep-max, apps-fitness-max, investors-partners
- **Evidence:** apps-looks-max-desktop-01 shows a gold 'App Store / For iOS ↗' pill and an outline 'Google Play / For Android ↗' pill, 66px tall, with no Apple or Google marks (build_site.py:96 string-replaces a generic btn(); products.css:61-64). foundation.css:64 gives .button.primary and .button.small the same var(--accent) fill, so the download button matches the header Contact pill. Index cards offer only 'Explore X →' and a status dot, investor cards show availability as text, and product pages end with 'Ask about X' and 'All apps' without repeating the store action. CINEMATIC_REFINEMENT item 4 removed custom availability badges; official store badges are a different thing.
- **Problem:** The most concrete proof of shipping, a live store listing, is presented as anonymous buttons, and reusing the investor-contact gold for consumer downloads muddles the action hierarchy.
- **Investor impact:** Recognizable store badges instantly signal 'live on the App Store and Google Play'. Generic pills lose that signal.
- **Fix direction:** - Use the official 'Download on the App Store' and 'Get it on Google Play' badge artwork, unmodified from Apple's and Google's marketing resources, self-hosted as SVG.
- Show both at equal visual height, within each brand's minimum-size and clear-space rules, and add the Google Play trademark attribution line in the footer or fine print.
- Keep the accessible names, the sr-only new-tab text and the ↗.
- Place them under the hero H1, in a closing 'Get X' band in the product's color world, and in compact form on index cards (as separate links via a stretched-link card) and investor cards.
- Optionally add a static QR code to the real store URL for desktop visitors.
- Reserve the gold pill for investor and partner actions.

#### T5-06: The only Sleep Max story image shows an empty account (high) *(needs founder material)*

- **Pages:** apps-sleep-max
- **Evidence:** apps-sleep-max-desktop-03 and mobile-04 show 'Alex · Bronze' with '0 DAY STREAK', '0 VERIFIED NIGHTS', '0/8 BADGES', 'Discipline 0.0/10' and an all-empty grid labelled '0 nights', beside the heading 'Keep your activity in view.' The image is sleep-max-detail-screen-3.webp (product_story.py:49-63). product-story-evidence.json says it was the only extra Sleep screen that passed claims review, because the home and paywall shots carry clinical or CBT-I language.
- **Problem:** The one inside-the-product image for Sleep Max is a blank empty state that contradicts its own headline.
- **Investor impact:** An empty profile suggests an unused app, the opposite of the 'real, shipping software' impression these pages exist to create.
- **Fix direction:** - Ask the founder for an official screenshot of a seeded demo account with clearly labelled sample data, or a clean export of the populated Profile, Tonight or Insights screen.
- Until then, remove the frame and build the Sleep chapter on distinct Soundscapes detail crops, so it does not repeat the hero.
- Never invent values.
- Removing the frame leaves Sleep with one image, so prioritize this request (T5-07).

#### T5-07: Product stories are thin: 2-3 images over about 5,000px, with viewport-sized voids (high) *(needs founder material)*

- **Pages:** apps-looks-max, apps-iq-max, apps-sleep-max, apps-fitness-max
- **Evidence:** product_story.py:14-23 (Looks) and :49-63 (Sleep) contain one step and one screenshot each. Total screenshots are 2 on Looks and Sleep and 3 on IQ and Fitness, across pages of 4,892-5,784px (index.json). apps-looks-max-desktop-02 has an empty right half of ≈450px, -03 has copy at the top left with an ≈350px void, and IQ alternates copy with large empty areas (desktop-03/04). Permissible screens are unused: IQ screen-2 is marked usable in product-evidence.md, and the Looks screen-6 detail areas are not shown.
- **Problem:** Most of the scroll depth is black space and text, so the pages feel padded rather than rich.
- **Investor impact:** Thin product evidence suggests there is not much product to show.
- **Fix direction:** - Add an App Store-style filmstrip per product: a native horizontal scroll-snap rail of every claims-cleared official screen at matching height, with no JS. Make it keyboard-operable as a focusable region (tabindex=0, role=region, aria-label).
- Pair it with detail crops of real screens.
- Tighten spacing so no chapter leaves a viewport-sized void.
- Ask the founder for more clean screens for Looks Max and Sleep Max, which have the fewest usable store images.

#### T5-08: Product identity is footnote-sized: a 48px icon and a 13px name beside an interchangeable slogan (medium)

- **Pages:** apps-looks-max, apps-iq-max, apps-sleep-max, apps-fitness-max
- **Evidence:** products.css:52 sets .detail-icon to 48px, and :53 sets the name eyebrow to 13px. The H1s are four interchangeable wellness slogans: 'A more considered approach to self-care.', 'Make room for a daily mental challenge.', 'Bring intention to the end of your day.' and 'Build a routine you can follow.' On /apps the names are 64px (products.css:14), so the product name shrinks once you enter the product.
- **Problem:** Nothing in the first glance says 'this is Looks Max, a real app'.
- **Investor impact:** Weak product branding makes the apps feel less like owned, distinctive assets.
- **Fix direction:** - Lead with the product: show the official icon at 88-112px (up to ≈160-200 CSS px from the 400px masters) with a product-color glow.
- Set the product name as the H1 or as a 64-96px kicker, and demote the slogan to a subtitle.
- Mirror the index scale so the name stays dominant from index to detail page.

#### T5-09: 'The product experience' is a generic three-icon feature row in company gold (medium)

- **Pages:** apps-looks-max, apps-iq-max, apps-sleep-max, apps-fitness-max
- **Evidence:** apps-looks-max-desktop-04, apps-iq-max-desktop-05, apps-sleep-max-desktop-04 and apps-fitness-max-desktop-04 each show three columns of a 30px gold outline icon, an h3 and two lines of grey text under the same h2 (visual_sections.py:35-65). products.css:101-107 colors the icons with the site --accent regardless of product.
- **Problem:** It is a SaaS-template feature row that repeats the story and adds no product imagery.
- **Investor impact:** It reads as filler from a website kit rather than a product showcase.
- **Fix direction:** - Fold the features into each product's signature chapter (T5-02).
- Pair a detail crop with a feature only where a claims-cleared official screen actually shows it (Looks 'Scan Facial Structure', IQ routine toggles, Fitness meal macros).
- Keep the other features as concise text with product-tinted rules and no stand-in imagery. Flag them as candidates for founder-supplied screens: Looks activity calendar and journal, IQ adaptive difficulty, Sleep diary and coaching.
- Write product-specific headings within the product-story-evidence.json copy rules.

#### T5-10: On desktop, the Sleep Max hero pushes its store actions below the fold and leaves the top right empty (medium)

- **Pages:** apps-sleep-max
- **Evidence:** apps-sleep-max-desktop-01: the centered H1 spans y290-450, and the screenshot starts at y507 on the left. The right column is empty until the lede at y812-871, and the store buttons first appear at the top of desktop-02. products.css:67-71 sets the grid areas 'title title' / 'art copy' with the copy center-aligned against an ≈800px image.
- **Problem:** The variant meant to make Sleep distinct produces an unbalanced first view with no visible store action.
- **Investor impact:** The first viewport of a product page should show what the product is and that it is live. Here it shows a slogan, half a phone and a void.
- **Fix direction:** Either:
- make the Sleep hero a full-bleed night stage with a centered H1 and store badges directly under it, and the Soundscapes screen rising from the bottom into an indigo glow; or
- align the copy column to the start and place the badges beside the top of the screen, so the CTA lands within 900px.

#### T5-11: Clicking a product's main image on /apps opens a lightbox instead of the product page (medium)

- **Pages:** apps
- **Evidence:** visual_catalog.py:110 renders app_art(app, True), which resolves to product_art (visual_products.py:24-30; build_site.py:60-61): an a.screenshot-open whose href is the raw /assets/*.webp, which gallery.js turns into the zoom dialog. Only the h2 name and the small 'Explore X →' text link go to /apps/<slug>.
- **Problem:** On a portfolio index the image is the natural door into the product, but here it leads to a utility viewer.
- **Investor impact:** Visitors who click a product hit a dead-end preview, so the page feels like a file browser.
- **Fix direction:** - Make each index card a single product link using a stretched-link pattern, so compact store badges (T5-05) remain separate links with no nested interactive elements.
- Keep zoom for product pages only.
- On hover and focus, lift the screen and intensify the product glow, with motion only under no-preference.

#### T5-12: The mobile /apps page runs about eight screens, because each product shows a full-height poster (medium)

- **Pages:** apps
- **Evidence:** index.json: /apps on mobile is 6,477px over 8 slices. products.css:146 sets .store-screen to 318px wide at full poster height at 640px and below. Each product takes ≈1.5 viewports (name, a ≈628x1360-device-pixel poster, Enlarge, caption, summary, status, Explore) in apps-mobile-01 to 06. The IQ poster fills the whole screen (apps-mobile-03).
- **Problem:** A phone visitor scrolls through four tall ads to see a four-app portfolio, with no at-a-glance overview.
- **Investor impact:** Investors often first open the link on a phone, where the portfolio feels long and repetitive rather than curated.
- **Fix direction:** On mobile, use compact cards: icon, name, a crop of the screen capped at ≈55-60svh in its color-world stage, and a one-line summary. Use a per-product object-position aimed at the UI region rather than a pure top anchor, which would show mostly poster headlines. Alternatively, use a keyboard-operable horizontal scroll-snap rail of the four products. Keep full screens on the detail pages.

#### T5-13: The mobile portfolio selector misaligns, switches to centered alignment, and hides the change it makes (medium)

- **Pages:** home
- **Evidence:** home-mobile-02: in the 2x2 chip grid the 'Looks Max' label sits at y≈1055 and 'IQ Max' at y≈1071, because 'Appearance & self-care' wraps to two lines and 'Cognitive practice' to one. Icons are 29px with 13px/12px text and a ✓ (home.css:135). home-mobile-03: 'Available on iOS & Android' and 'Explore Looks Max' are centered (home.css:136 .explorer-panel-action{text-align:center}) while all other copy is left-aligned. The selector sits at ≈515-690 CSS px, so on tap only the changed panel's category and title show at the bottom of the viewport.
- **Problem:** Small misalignments, an alignment switch, and a selection change that happens mostly off-screen make the key mobile scene feel unfinished.
- **Investor impact:** A discerning viewer on a phone notices the jitter, and the product change barely registers.
- **Fix direction:** If the selector survives T5-03:
- Use a top-aligned grid with 40-44px icons and names on one line; drop the category or hold it to one line.
- Left-align throughout.
- Give the selected state a non-hue cue at ≥3:1 and keep the focus outline.
- Keep the change in view without moving the page: reorder so the screenshot sits directly under the selector, or make the selector sticky while the stage is on screen.
- Do not auto-scroll on tap.

#### T5-14: Product pages end with about 1.5 viewports of low-energy text bands (medium)

- **Pages:** apps-looks-max, apps-iq-max, apps-sleep-max, apps-fitness-max
- **Evidence:** apps-looks-max-desktop-04 to 06 and apps-sleep-max-desktop-04/05 end with:
- 'PART OF SOLARITY AI / Let's talk about X.' with an outline button and 'All apps'
- 'Another ambition in mind?' as three 44px-icon directory rows, each ending 'iOS & Android →'
- the footer slogan

Sources: visual_products.py:51, ux_components.py:26-28, products.css:111-127. There is no imagery or product color anywhere in this tail. This closing pattern also differs from the other routes' closing band.
- **Problem:** Each product page winds down through three similar text-heavy sections, and the cross-sell to sibling apps is a plain directory.
- **Investor impact:** The last impression of each product is flat, and the family-of-products story, a key investor point, is told as a table.
- **Fix direction:** - Merge the closing into one band in the product's color world: icon, official store badges, and a secondary 'Ask about X' for partners. This becomes the compact product variant of the shared closing system (T8-02).
- Make related apps three large sibling cards, each in its own color world with its icon and a cropped authentic screen.
- Shorten the tail.

#### T5-15: The Only Fitness store-name disclosure repeats three times, and the story intro is spent on it (low)

- **Pages:** apps-fitness-max, apps
- **Evidence:** The disclosure appears at:
- apps-fitness-max-desktop-01, y≈709: 'Listed in app stores as Only Fitness.' (visual_products.py:38)
- desktop-02, the story intro: 'See examples from Only Fitness, the store-listed app presented here as Fitness Max.' (product_story.py:67)
- desktop-04: 'Product context. Fitness Max is listed in app stores as Only Fitness…' (build_site.py:37)
- /apps (apps-desktop-04, y≈206)
- **Problem:** Repeating a required disclosure makes the naming mismatch feel like a caveat, and the story's only introduction describes the name rather than the product.
- **Investor impact:** Repetition draws attention to the inconsistency and weakens the product's identity.
- **Fix direction:** - State it once, designed into the store-badge block ('On the App Store and Google Play as Only Fitness').
- Keep it in the Product context footnote if required.
- Rewrite the story intro to describe what the chapter shows. Descriptive copy only, no new claims.

#### T5-16: The 'Available on iOS & Android' status dot duplicates the store actions (low)

- **Pages:** apps, apps-looks-max, apps-iq-max, apps-sleep-max, apps-fitness-max
- **Evidence:** apps-looks-max-desktop-01, y≈720: '• Available on iOS & Android' sits 30px above the store buttons that say the same thing. The identical line repeats under all four /apps cards (build_site.py:48-49 product_status, visual_catalog.py:111).
- **Problem:** Redundant microcopy adds noise without adding information.
- **Investor impact:** Minor clutter that adds to the template feel.
- **Fix direction:** Drop the status dot wherever official store badges are present. On index cards, replace it with compact badges as separate links beside the stretched card link. Keep the '.status' chip for the evidence register on corporate pages (T6-02).

#### T5-17: The mobile 'Get X ↓' quick link is a thin underlined text link with a detached arrow (low)

- **Pages:** apps-looks-max, apps-iq-max, apps-sleep-max, apps-fitness-max
- **Evidence:** apps-looks-max-mobile-01 (y≈810) and the equivalent IQ, Sleep and Fitness mobile-01 slices show 'Get Looks Max ↓' in gold, underlined, with the ↓ underlined separately about 20px away (products.css:136 .product-quick-link). The real store buttons appear only after the full-height poster (apps-looks-max-mobile-02).
- **Problem:** On mobile, the primary 'get the app' path is the weakest-looking element in the hero.
- **Investor impact:** Small, but it makes the mobile hero feel unfinished.
- **Fix direction:** On mobile, place the official store badges directly under the H1, before the staged screen, or make the quick link a compact pill with Apple and Google glyphs. Keep the in-page jump as a fallback.

### T6 Investor narrative: proof, evidence versus vision, and the platform

Investors cannot find concrete proof in ten seconds. The investor page opens with a slogan and utility links, its facts are set in 13px dim type, and the business model is the least prominent element. The unbuilt platform gets the brightest surfaces and product-style affordances, followed by scattered fine-print retractions. The platform visual is a beige org chart rooted in a slogan, and the same three-step argument repeats across three pages.


#### T6-01: Investors & Partners has no investor-grade structure and no proof in the first ten seconds (high) *(needs founder material)*

- **Pages:** investors-partners
- **Evidence:** investors-partners-desktop-01 to 05 run in this order:
1. headline
2. screenshots
3. three-step thesis list
4. two small 20px 'Consumer model' and 'Platform strategy' paragraphs between hairlines (desktop-03, y545-685)
5. partnership rows
6. FAQ
7. booking card

The opening is text only, beside a utility cluster of lede, two pills and a five-link 'On this page' index (company.css:110-115). The only number, '4 store-listed apps', appears twice within ≈1.5 screens (visual_company_upgrade.py:51 and :96), once in 13px --dim type (company.css:119). The legal entity and HQ appear only in the footer ('© 2026 Solarity AI LLC', 'Irving, Texas'), and no face appears anywhere on the page. The mobile first viewport is entirely headline, lede, buttons and index, with the first screenshot at the bottom edge (investors-partners-mobile-01).
- **Problem:** The page reads like a philosophy essay with contact links. It has none of the scannable facts an investor page uses to establish seriousness, and its verified facts are set in the smallest, dimmest type while slogans and hedges look primary.
- **Investor impact:** An investor skimming for ten seconds leaves without one concrete reason to believe, so the company looks less mature than it may be.
- **Fix direction:** - Lead with a concrete thesis line and an 'At a glance' fact band, using only verified facts:
  - Solarity AI LLC · Irving, Texas
  - Founder Ata Turhan
  - 4 apps available on the App Store and Google Play, linked
  - Business model: subscriptions and in-app purchases, reverified before it is promoted to a headline fact
  - App factory: Engineering, Management and Marketing Max, with a Vision chip
  - Team size only if the founder confirms how to state it
- Set values large and labels small.
- Delete the duplicate '4 store-listed apps'.
- Turn the business model into a two-card 'Today / Ahead' ledger in the evidence and vision registers (T6-02).
- Add a compact team strip with the founder portrait, linking to Company.
- Pair it with the showroom (T4-04), fully in the first desktop viewport, and show at least one large screen in the first mobile viewport.
- Reserve layout space for founding year, stage or raise, traction metrics and a deck request, but render them only once the founder supplies verified content. No placeholder markup.

#### T6-02: Evidence and vision have no visual register, and the vision gets the brighter treatment (high)

- **Pages:** home, platform, investors-partners
- **Evidence:** Vision outshines evidence:
- On Investors (desktop-02/03) the verified thesis sits in muted rows on black (x88-778), while 'THE PLATFORM VISION' gets the ivory paper card (company.css:142). Paper also carries the founder and booking cards, so the surface means nothing.
- On Home (home-desktop-04, mobile-05) the vision rows are linked, arrowed and labelled Build/Operate/Grow, the same affordance as products.
- On Platform the modules get 4rem numerals, ≈52px names and a 'Discuss X Max →' each (build_site.py:100-101; company.css:73-81).

The vision items are labelled, but only with small eyebrows in the same gold as everything else ('THE APP FACTORY VISION', the 'Platform vision' tag). The boundary is then carried by repeated fine print:
- 'Conceptual strategy. These relationships do not represent a deployed, integrated platform.' (visual_home.py:35-49)
- 'Connections shown do not represent deployed integrations.' (visual_strategy.py:45-47)
- 'They are not presented here as established platform services.' after 'Potential commercialization.' (visual_company_upgrade.py:103)

The existing chips are .status and .status.vision (foundation.css:80-82), rendered by product_status as 'Available on iOS & Android' or 'Product vision'.
- **Problem:** The line between live and next relies on small text and repeated hedges, and on Investors the unbuilt vision is styled more prominently than the verified evidence.
- **Investor impact:** Diligent investors notice when vision is styled above evidence, and confident-headline-then-disclaimer reads as overselling or nervousness. Ambitious companies are believed when they draw a clear line and present the vision with conviction, as a vision.
- **Fix direction:** Define two registers on top of the existing chips:
- Evidence: lit surfaces, authentic icons and imagery, the '.status' chip ('Available on iOS & Android') and direct store links.
- Vision: unfilled panels with a dashed warm hairline, outlined or ghosted nodes, and the '.status.vision' chip. Never the brightest surface.

Other rules:
- Chips carry text, so meaning never depends on color or dot shape, and vision type stays at AA.
- Open each vision section with one framing sentence, and use one concise legend per page stating that connections are conceptual, not deployed, in place of the scattered retractions.
- Keep the 'sample content' image disclosure beside the screenshots, and keep the precise FAQ answers.
- Replace the per-module contact links with one partnership CTA (T6-05).
- Any 'in development' or dated roadmap wording needs founder confirmation.

CLAUDE.md requires app-factory pages to keep strategy distinct from deployed capability.

#### T6-03: Platform's main visual is a static, light-mode org chart that starts from a slogan rather than the apps (high)

- **Pages:** platform
- **Evidence:** platform-desktop-01:
- A bright #f1ede3 card spans x708-1352 from y190 past the fold.
- A beige radial bubble reads 'Consumer portfolio / Human potential. / Focused mobile products' (visual_strategy.py:36; company.css:54) and feeds tree connectors into Build, Operate and Grow.
- The 'Conceptual company strategy' note is cut off at the fold (y857-900).
- align-items:center (company.css:42) leaves ≈285px of empty black above the eyebrow (y88 to 373).
- The built Platform page has no app icon or screenshot at all.

The diagram is fully static: the SVG path and dot (visual_strategy.py:38-42), a hover that only sets #e2d7c4 and moves the arrow 2px (company.css:66-68), and a :target that only recolors a top border (:82). platform-desktop-02 and platform-mobile-02 are equally static.
- **Problem:** The page's only visual reads like a slide, never shows the page's own argument that real products ground the vision, and depicts a flow that does not flow.
- **Investor impact:** The app factory is the big-upside part of the story, and a beige template diagram makes it look less ambitious than the consumer apps.
- **Fix direction:** Rebuild it as a luminous inline-SVG system on a dark stage, with the copy top-aligned:
- Source row: the four authentic app icons (source-assets/*-icon.webp, published on reference), linked to their pages, with the '.status' chip 'Available on iOS & Android', forming a solid sun core.
- Build, Operate and Grow as dashed or outlined vision nodes with '.status.vision'.
- Connectors that read as 'informs', never as the apps running on these systems. No solid integration lines.
- A two-item legend, and a caption visible in the first viewport that is never animated in late.
- A text alternative for the diagram.

Motion, only under no-preference:
- The connectors draw in (pathLength=1, stroke-dashoffset, 900ms), with a one-shot glow on the core, and the nodes rise in sequence.
- On a module jump, the accent border draws across (scaleX, 600ms).

#### T6-04: Home's app-factory vision is a three-row link list with an invisible ring motif (high)

- **Pages:** home
- **Evidence:** home-desktop-04 (y130-540) shows 'Build / Operate / Grow' as 12px labels with 21.6px names, one-line descriptions and an arrow per row (home.css:103-107). The product-to-factory relationship is carried by one 13px line, '↓ Experience informs workflow design' (visual_home.py:47; home.css:100; mobile-05), which reads like a stray link. The decorative ring (home.css:89, #e7c6961a) shows only as faint arcs, (31,28,21) on (25,24,19), crossing 'Build the product.' in home-desktop-03 at x≈600-800, y652-900. A platform_map component already exists (visual_sections.py:68).
- **Problem:** The idea that should make investors lean in, product experience feeding an app factory, has no visual form and reads as a navigation list.
- **Investor impact:** The scalable platform is the reason to invest beyond four apps, and rendered as text rows it lacks conviction.
- **Fix direction:** - Draw a 'sunrise diagram' in inline SVG that shares the redesigned platform map component (T6-03): the four authentic icons on a horizon as proven products, and a visible arc of light leading to three hollow or dashed vision nodes.
- Put a 'Conceptual strategy' tag inside the diagram and keep the existing disclaimer.
- Draw it in with stroke-dash on view, static under reduced motion.
- Use no solid connectors.
- Remove the ring, or redraw it as an intentional sun arc at 30-40%.

#### T6-05: The platform modules are three identical text rows, each with its own contact link (high)

- **Pages:** platform
- **Evidence:** platform-desktop-02/03: Engineering, Management and Marketing Max each use an identical ≈385px row: a sand numeral, eyebrow, name and tagline on the left, two paragraphs on the right, and 'Discuss X Max →'. The left column is empty below the tagline (≈120px per row). build_site.py:101 generates one template three times. The built /platform main content holds 7 contact links: the hero partnership link, three 'Discuss X Max', 'Discuss the platform direction' and the two closing buttons. The header Contact comes on top of that.
- **Problem:** The core of the vision page conveys no sense of system or ambition, and it asks for contact seven times before showing anything.
- **Investor impact:** Partners evaluating the platform see a company selling before it has shown anything.
- **Fix direction:** - Use a sticky split per module, sized to its content rather than 100vh: the numeral and name stay pinned while the copy scrolls.
- Add a large, low-contrast outlined stage word (BUILD, OPERATE, GROW) and the '.status.vision' chip.
- Atmosphere may deepen gently from module to module, but the panels stay in the vision register (unfilled, hairline) and never outshine the evidence.
- Never mock up module UI.
- Replace the three per-module links with one context-carrying partnership CTA after the modules, plus the closing band.

#### T6-06: The same three-step argument and numbered section recipe repeat across Platform, Investors and Company (high)

- **Pages:** platform, investors-partners, company
- **Evidence:** There are six numbered sequences:
- Platform module numerals
- Platform steps: 'Start with a specific human need / Learn from the work behind it / Develop patterns worth reusing' (visual_company_upgrade.py:66-68)
- the Investors thesis, nearly word for word: 'Start with an everyday ambition / Learn through focused products / Develop useful patterns' (:97)
- Investors partnership topics
- the Investors FAQ (01-05)
- Company principles (:115)

Each sits in the same layout: sand eyebrow, two-line headline, hairline list. This contradicts CINEMATIC_REFINEMENT item 4. Beside the partnership list there is a dead left column of ≈225px (investors-partners-desktop-04: the copy ends at y≈174, the list starts at y≈398).
- **Problem:** One section recipe repeats six times, and the same argument is said three times in slightly different words. This is a strong template tell.
- **Investor impact:** Readers notice the repetition, which suggests the company has less substance than it presents.
- **Fix direction:** - Give the three-step argument one home (Platform) and link to it from elsewhere.
- Replace the Investors thesis with the evidence and vision ledger (T6-01).
- Turn the Company principles into one editorial statement.
- Allow at most one numbered sequence per page (T3-09), and vary the compositions.
- Make headings sticky in split sections so the left column is never dead.
- Drop eyebrows that repeat the heading.

#### T6-07: Home has no proof beat between the vision and the ask (medium) *(needs founder material)*

- **Pages:** home
- **Evidence:** The home order (build_site.py:90) is hero, explorer, strategy, founder strip, closing band. The only availability signal is the 12px 'Four apps. iOS & Android.' (home.css:21), with no direct App Store or Google Play link anywhere on Home. No scene carries verifiable launch dates, ratings, downloads, press or partners. DESIGN_SYSTEM.md rules out animated counters.
- **Problem:** The closing ask arrives without visible evidence, so the page reads like a brochure rather than a company.
- **Investor impact:** Investors look for evidence before the ask.
- **Fix direction:** - Now: surface the verified store facts inside the portfolio scene (T5-03), with official badges or links per app at readable size. Do not add a thin numerals band.
- Later: add a dedicated proof band only once the founder supplies at least 2-3 verifiable figures with source and date (launch dates, store ratings, downloads, or press or partners with permission). Use large static display numerals, no counters, and never placeholders or estimates.

#### T6-08: The 'On this page' index looks like documentation and wraps one item onto a second line (medium)

- **Pages:** investors-partners
- **Evidence:** investors-partners-desktop-01: 'Portfolio ↓, Thesis ↓, Partnerships ↓, Questions ↓', with 'Talk with the founder ↓' wrapping alone onto a second line at y=486. Each link draws two underline segments, because .page-index a is an inline-flex container with text-decoration (company.css:113). The index sits in the hero column and pushes the proof down (visual_company_upgrade.py:10-15; company.css:110-115). On mobile, two lines are expected. The index is a deliberate UX_REFINEMENTS #3 feature with the targets #portfolio, #thesis, #conversation-paths, #investor-questions and #booking.
- **Problem:** An orphaned item, broken underlines and extra hero height make the first screen read as navigation rather than proposition.
- **Investor impact:** It weakens the opening impression of the most important page.
- **Fix direction:** - Keep the index and its targets.
- Fit it on one line with a shorter 'Founder' label or a full-width row beneath the hero.
- Draw one continuous underline per link (border-bottom or background on the link itself).
- Add no numbers, and keep the ↓ convention.
- An optional orientation rail is handled in T9-09.

#### T6-09: On mobile, the Platform diagram becomes a beige list taller than a screen, and module text loses about 52px (medium)

- **Pages:** platform
- **Evidence:** platform-mobile-01/02: the cream map runs from ≈566 to ≈1377 CSS px (≈810px tall). The connectors are hidden at 560px and below (company.css:273), so the diagram reduces to three ruled rows. Module copy starts at x≈74 CSS px because of the 34px numeral column plus an 18px gap (company.css:284), which narrows the measure on a 390px screen (platform-mobile-02/03).
- **Problem:** On phones the vision visual turns into a long list, and the module chapters become dense, indented text.
- **Investor impact:** Many investors open links on a phone first, and this is where the platform story looks weakest.
- **Fix direction:** - Render the redesigned map (T6-03) as a compact vertical sequence: four app icons, a glowing vertical line, then three outlined vision nodes, capped at ≈60svh.
- Put the module numeral inline above the eyebrow so the copy uses the full measure.
- Keep the step indices and the Vision chips.

#### T6-10: The platform diagram's columns misalign: the Build caption wraps and drops its arrow 19px (low)

- **Pages:** platform
- **Evidence:** platform-desktop-01: 'Requirements, implementation, review' wraps to two lines, so the Build arrow sits at y≈722 while Operate and Grow sit at y≈703, and the bottom rules differ (y≈755 vs 753). The cause is in-flow arrows in center-aligned blocks with min-height 184px (company.css:60).
- **Problem:** Uneven baselines inside the page's only diagram look careless up close.
- **Investor impact:** A small craft flaw in the most visible element on the vision page.
- **Fix direction:** Pin the arrows to the bottom with margin-top:auto in a flex column, or use a subgrid or fixed row tracks so the stage word, name, caption and arrow align across columns. Carry this over into the redesigned map.

#### T6-11: The 'Build ↓ Operate ↓ Grow ↓' links point down but jump up the page (low)

- **Pages:** platform
- **Evidence:** In platform-desktop-04 (x957-1160, y106) and platform-mobile-05 (y≈1283), the links sit under strategy step 03 and target #engineering-max, #management-max and #marketing-max (visual_company_upgrade.py:68), all of which are above that section. They are 13px and underlined (company.css:95). check_site.py enforces only the ↗ rules.
- **Problem:** The arrow promises a downward jump, the page moves up, and the tiny links read as leftover navigation.
- **Investor impact:** A minor point of confusion that adds to the link-heavy, unpolished feel.
- **Fix direction:** Remove these links; the sticky module treatment (T6-05) makes them unnecessary. If they stay, use an upward arrow, adding that convention to CLAUDE.md, and style them as one compact segmented control.

#### T6-12: The 'Platform vision' tag is underlined like a link but is not one (low)

- **Pages:** platform
- **Evidence:** In platform-desktop-01 (x1228-1310, y241) and platform-mobile-01 (y≈1200), 'Platform vision' is a span (visual_strategy.py:34) with a border-bottom underline (company.css:52).
- **Problem:** The most important honesty label reads as a clickable control that does nothing.
- **Investor impact:** Minor, but it blurs the one label that tells readers the diagram is a vision.
- **Fix direction:** Restyle it as the shared '.status.vision' chip (foundation.css:82): hollow dot, small caps, no underline. Every vision element then carries the same tag (T6-02).

### T7 Founder, team and company story

Investors back people, but the founder appears as one cool white studio headshot reused on three pages. On Company it is upscaled, and on Home it sits beside an empty half-row labelled 'Founder's perspective' with no perspective in it. The team is six bare names, and the Company page shows no products or trajectory. Most fixes here depend on material from the founder.


#### T7-01: The founder portrait is a cool white studio headshot, the brightest object on three pages, upscaled on Company (high) *(needs founder material)*

- **Pages:** home, company, careers, contact
- **Evidence:** - Home: a 300px square (home-desktop-05) whose background measures (239-248,240-249,242-251), a cool studio white and the brightest, coolest surface after the hero. Mobile shows a 160x180 thumbnail (home.css:138).
- Company: ≈582px square (company-desktop-01, with the fold at the mouth). With the cream card below it forms an ≈880px bright block (company.css:8, 13-14; aspect-ratio 1 with object-fit:contain).
- Resolution: the master source-assets/brand/ata-turhan-original.webp is 800x800, and the srcset stops at 640w with sizes 600px (visual_sections.py:103-107), about a 1.9x upscale on 2x displays.
- Careers: the same photo as a 340px white square at the top right (careers.css:9-11; visual_careers.py:63), captioned 'THE PEOPLE BEHIND THE WORK' over one person.
- --shadow-portrait does not show on dark backgrounds.
- CONTENT_REGISTER lists the portrait as a recovered official asset.
- **Problem:** A LinkedIn-style ID photo is pasted into a warm, low-key world. It is colder and brighter than everything around it, soft on Retina, and repeated three times.
- **Investor impact:** At this stage investors back the founder. A generic headshot undercuts the premium positioning at the moment they judge the person, and the repetition makes the company look thinly staffed.
- **Fix direction:** Interim, with the existing photo:
- A 4:5 head-and-shoulders crop (object-fit:cover, object-position ≈50% 22%), generated as an 800w variant.
- Cap it at ≈320-360 CSS px on desktop and ≈280px on mobile; a 4:5 crop of the 800px master gives at most ≈640x800.
- Present it on a lit dark plate rather than the cream card, with a warm rim light from the upper right, a CSS edge vignette or mask so the white backdrop falls off into the scene, and a thin warm hairline frame.
- Set the name over a gradient at the lower edge.
- Apply a global warm grade only with founder approval: a tone curve cannot darken the white backdrop without crushing the shirt and the facial highlights.
- No retouching, no cut-out, no background replacement.
- Treat each page differently: drop the Careers repeat, or make Careers plural with the roster (T7-03).

Ask the founder for an editorial portrait set: environmental, warm directional light, wide and tight crops, at least 1600px.

#### T7-02: 'Founder's perspective' contains no founder voice (high) *(needs founder material)*

- **Pages:** home, company
- **Evidence:** home-desktop-05: the eyebrow 'FOUNDER'S PERSPECTIVE' introduces a location-and-focus sentence (build_site.py:89), and the right ≈45% of the row (x≈900-1352) is empty. Company (build_site.py:106; company-desktop-01/02, mobile-02) shows a slogan headline and two third-person paragraphs ('Ata Turhan founded Solarity AI with a focus on AI-powered products…'), then a 'Connect with Ata' button that duplicates the card's own link (the card text link at y=456 and an outline button at y=285 both go to /contact). The card says only 'Founder of Solarity AI' and 'Based in Irving, Texas' (visual_sections.py:110-121). The site has no blockquote or pull-quote component, no signature and no profile link anywhere.
- **Problem:** A section labelled 'perspective' holds a byline. With no typographic set piece anywhere, the site has no emotional peak after the hero.
- **Investor impact:** Investors back people. The absence of the founder's own words makes the company feel anonymous despite the large portrait.
- **Fix direction:** - Ask the founder for a one- or two-sentence first-person statement on why Solarity exists, a scanned signature, a public profile URL such as LinkedIn, and any background he approves for publication.
- Build one founder-statement component: the display face at 2.5-3.5rem, hanging-punctuation:first with a manual fallback, a small-caps attribution 'Ata Turhan, Founder', on a generous lit dark field beside the treated portrait.
- Never draft the quote for him.
- Until the statement exists, drop the 'perspective' eyebrow and tighten the row so no empty half remains.
- Keep exactly one 'Connect with Ata' action.

#### T7-03: The team is six bare names that read as a placeholder (high) *(needs founder material)*

- **Pages:** company, careers
- **Evidence:** company-desktop-02/03 list Emrecan Özkan, Ali Yılmaz, Hasan Ak, Eren Öz, Batuhan Yücetürk and Melik Kaplan at clamp(1.6rem,2.6vw,2.65rem), ≈37px at 1440 (company.css:32), between hairlines. There are no roles or faces, and about 150px of empty space follows (y375-524). Word spaces collapse (T3-03). On mobile the roster takes ≈530 CSS px. visual_team.py TEAM_PORTRAITS holds identity-matched portraits for Emrecan, Ali and Hasan (source-assets/team/*-480-*.webp), but selected_team() renders names only. Monogram plates were tried before (REFERENCE_DESIGN_PASS.md) and replaced as inconsistent (CINEMATIC_REFINEMENT item 21). Careers says 'THE PEOPLE BEHIND THE WORK' over one person.
- **Problem:** Large type puts information that isn't there on display. Names without functions or faces look like filler and raise the obvious question of who does what.
- **Investor impact:** Team is a core diligence question, and a roster with no roles or faces feels unverified.
- **Fix direction:** - Ask the founder for approved roles and a consistent portrait set for all six, then design a uniform 3x2 roster of graded 4:5 plates with portrait, name and function.
- Until then, use a credits block: ≈20-24px names in two or three balanced columns, under one heading, directly beneath the founder, with no large section padding and tracking no tighter than -0.02em.
- Do not show the three existing portraits on their own, do not reintroduce monogram plates, and never invent roles.
- Careers can reuse the credits block so 'people' is plural.

#### T7-04: The Company page has no company story: no products, milestones or trajectory (medium) *(needs founder material)*

- **Pages:** company
- **Evidence:** company-desktop-01 to 05 and company-mobile-01 to 06 contain an intro, a portrait card, a name list, three principles and a CTA, with no app icon, screenshot, founding year or timeline (build_site.py:104-108). The intro mentions only 'self-improvement apps' and 'a vision'.
- **Problem:** An about-the-company page with no artifacts of what the company has done feels abstract.
- **Investor impact:** Investors look for momentum, and the page gives no sense of trajectory or output.
- **Fix direction:** - Add a horizontal 'The story so far' strip: the founding plus each app's store launch, each node carrying the authentic icon and linking to its page, along a sunrise line.
- Use only dates the founder confirms, and verify store listing dates before publication.
- If no dates are approved, use a four-icon portfolio strip ('Four apps, available on iOS & Android') as the evidence beat.

### T8 Composition, pacing and endings

After the hero every page follows one recipe, in one 1264px container, on one surface. Scenes are separated by empty black and hairlines. Every page ends on the same unlit two-pill CTA band, then a second footer slogan, an undersized giant wordmark and a loose directory. CTAs and arrows repeat so often that no action is primary.


#### T8-01: Every page uses the same template after the hero, so nothing feels directed (critical)

- **Pages:** home, apps, platform, company, investors-partners, careers, contact, 404
- **Evidence:** apps, company, investors, platform, careers, contact and 404 (desktop-01) all open with a 12px gold eyebrow, an 85-100px two-line Manrope headline (second line recolored on six of the seven) and a supporting element beside or below it, on #11120f inside the 1264px .wrap (foundation.css:37). The same split-heading grid recurs at company.css:3, :103, products.css:3 and home.css:34. Home repeats the formula across 8 labelled scenes (dist/index.html), with heading sizes between 56 and 68px. After the hero, the only full-bleed change is Home's faint strategy band, and later sections are separated by 1px hairlines (apps-desktop-04, company-desktop-03/04, platform-desktop-02/03). Why earlier passes still read as average:
- DESIGN_SYSTEM.md:13: routes were 'audited in source' and 'Browser rendering was unavailable'.
- DESIGN_SYSTEM.md:62-63: 'Borders define structure', shadows only on imagery, 'Do not add continuous decoration'.
- The 24- and 30-item passes fixed checklist items inside this one safe system and never set an art direction.
- **Problem:** The pages read as one template with different words. There are no scene types, no crescendo and no signature openings.
- **Investor impact:** Within seconds on a second page, investors recognize a dark landing-page kit. That reads as a small team using a theme rather than a company with taste, which undercuts the claim that the company builds polished consumer products.
- **Fix direction:** - Define scene types: horizon or image scene, product stage, proof scene, editorial thesis, people scene, statement close. Assign them deliberately, so each key page has a signature opening that is not eyebrow plus split headline.
- Let at least one moment per page break the 1264px container through light, full-bleed product staging or color fields rather than repeated photography.
- Vary section height and density.
- Allow at most two statement moments per page.
- Revise the DESIGN_SYSTEM.md 'Borders define structure' and no-decoration rules as an explicit, founder-approved system change, keeping the ban on hidden-content entrances only as amended by the motion contract (T9-01).
- Review every pass in rendered 1440px and 390px screenshots.

#### T8-02: Every page closes on the same unlit CTA band, followed by a second sign-off and a long footer (high)

- **Pages:** home, apps, platform, company, all pages (footer)
- **Evidence:** home-desktop-05, apps-desktop-04, platform-desktop-04 and company-desktop-04 use the identical conversation band: a 'THE NEXT CONVERSATION' eyebrow, a ≈56px/3.5rem headline on the left, two stacked pills on the right, on flat #11120f with one hairline (foundation.css:83-87; visual_home.py:55-56; build_site.py:71-72). DESIGN_REFINEMENTS item 7 once made it a warm ivory panel, and it was later flattened. Dead gaps appear before it:
- ≈228px on Platform (platform-desktop-04)
- ≈230px on Company (company-desktop-04)
- ≈150 CSS px on mobile (company-mobile-05)

They come from the band's margin-top var(--space-section) (≈115px) stacking on the section padding (company.css:33, :83). apps-desktop-04 shows ≈170px before the footer. The footer then opens with a second 43px statement, 'Human potential. Thoughtfully built.' (visual_chrome.py:60; chrome.css:25-28). It fills ≈880px on desktop and ≈1.05 screens on mobile. Investors (booking) and Careers (form) end differently.
- **Problem:** A story that opens at sunrise ends on a stock CTA row in darkness, repeated across four routes, and then the footer dilutes it with a second ending.
- **Investor impact:** The close is where an interested investor decides to reach out. A flat, repeated block followed by a competing slogan lowers both the conversion and the sense of a confident brand.
- **Fix direction:** Design one shared closing 'horizon' scene:
- Backdrop: a heavily blurred, graded light field from the already-cached hero variant or a tiny pre-blurred derivative (lazy-loaded below the fold, hero preload unchanged), or a pure-CSS dawn glow rising from the bottom edge.
- In front: one page-specific statement at display scale and the two existing inquiry actions, one solid primary ('Investor inquiries') and one quiet secondary.
- Keep direct email and booking, verify AA over the lit area, and allow slow light drift only under no-preference.

Image budget: the recognizable sunrise appears in the hero plus at most one reprise across the closing, footer and 404. A true second crop waits for T2-05.

Also:
- Add the founder portrait only on routes without a founder section just above (not Home).
- Collapse the stacked spacing by dropping the band's margin-top after a padded section.
- Drop the footer intro statement, or make it the closing line, so each page closes once.

#### T8-03: Scenes are separated by empty black, hard seams and structural hairlines (medium)

- **Pages:** home, platform, company, investors-partners, contact, 404, apps-looks-max
- **Evidence:** Empty bands:
- home-desktop-03, y520-652, then a flat step to (25,24,19)
- home-desktop-04, y700-825, then a step back
- home-desktop-05, y355-500 and y770-900
- home-mobile-04, y260-440 (2x)

Structural 1px rules: the explorer footer (y446), strategy closing (y611), closing band (y502), footer top, signature rule (y594) and legal rule (y819). The footer starts with a hard line (apps-looks-max-desktop-05 y≈443, investors-partners-desktop-05 y≈624). Spacing stacks the founder-strip padding, the band margin and the band padding. Long routes (Investors, Platform, Company, Contact, 404) stack identical numbered hairline lists in --line #373b31. Hover states fill with a flat --surface (products.css:120, contact.css:63). The only shadow token is --shadow-portrait.
- **Problem:** Scenes are separated by uniform padding and thin lines rather than by composition or light. Nothing is elevated, so key sections weigh the same as reference lists and the rhythm reads like a document.
- **Investor impact:** Long, empty dark stretches between modest content make the page feel thin rather than spacious, and skimming investors find nothing that stands out.
- **Fix direction:** - Compose the transitions: let the next scene's light or device rise into the previous one, using gradient bridges and feathered tonal bands of 120-200px (mask-image) instead of flat color steps.
- Remove structural hairlines and keep rules only inside lists, with faded ends.
- Set a vertical rhythm per scene type and collapse stacked paddings into one value.
- Raise one or two focal moments per page with a warm tonal surface, an inner top highlight and local light. Shadows do not read on near-black.
- Avoid generic card shells, which DESIGN_SYSTEM.md rules out.
- Give the footer a dusk gradient lead-in instead of the 1px rule.
- Keep all text contrast unchanged.

#### T8-04: CTAs and arrows repeat so often that no action is primary (medium)

- **Pages:** home, platform, all pages (footer)
- **Evidence:** In dist/index.html:
- 'Discuss a partnership' appears 3 times (hero, strategy closing, closing band) and 'Investor inquiries' 3 times (hero, closing, footer), plus the header Contact. /contact is linked six times, and main holds 20 '→' glyphs.
- The hero offers three arrowed actions.
- The strategy scene alone has 'Explore the company thesis →', three arrowed module rows (already whole-row links, visual_home.py:40), 'Explore the app factory →' and 'Discuss a partnership →' (visual_home.py:45, 51).
- home-desktop-05 has 'Meet the company →' and then both pills again.
- The footer adds 'Investor inquiries', 'Partnership inquiries', 'Contact' (three links to /contact) and 'Email Ata ↗'.

On Platform, platform-desktop-04 shows an outline 'Discuss the platform direction →' directly above the closing band's two pills, and the page has 7 contact links in all. Labels vary: 'Discuss a partnership', 'Partnership inquiries', 'Discuss the platform direction'.
- **Problem:** Every scene ends in more links, so the page reads like a sitemap with prose and the investor path competes with a dozen equal-weight asks.
- **Investor impact:** The single clear 'talk to the founder' path gets lost, and the repeated asks feel like a funnel template.
- **Fix direction:** - One solid primary per viewport (investor), one secondary (partnership), and plain links for exploration, with no arrow on tertiary links.
- At most one quiet link per middle scene. Module rows drop the arrow glyph and gain a hover light.
- Remove the strategy-closing link row and the platform outline pill that duplicates the closing band.
- Standardize the labels as 'Investor inquiries' and 'Partnership inquiries'.
- Collapse the footer contact group (T8-06). Platform per-module links: see T6-05.

#### T8-05: The giant footer signature is undersized for its frame, crowded, lacks the sun, and gives no closing beat (medium)

- **Pages:** all pages (footer)
- **Evidence:** chrome.css:37 sets clamp(2.65rem,11.5vw,10rem), capped at 160px, with letter-spacing -.065em. 'SOLARITY AI' spans ≈785px of the 1264px wrap (≈62%) and ends at x≈873, leaving ≈480px empty on the right (home-desktop-06, contact-desktop-03/04, platform-desktop-05, careers-desktop-05). On mobile it covers ≈60-64% (home-mobile-08, contact-mobile-04, careers-mobile-07). 'AI' is weight 400 in off-token #b39d78, beside 'SOLARITY' at 500 in #e4dece (chrome.css:38), so it reads as disabled, and the T and Y touch. There is no sun mark (visual_chrome.py:63). It sits flat on #0c0e0b (chrome.css:25). It is aria-hidden and already handled in forced colors (accessibility.css:19).
- **Problem:** An oversized closing wordmark works only when it is clearly intentional. At 62% width with crowded capitals and no mark, the last frame of every page looks unresolved.
- **Investor impact:** The footer is the last brand image on every page, and an unbalanced sign-off weakens the memory of the brand.
- **Fix direction:** - Fit the wordmark to the wrap rather than the viewport: container-query units (cqi) on a container footer, or SVG text with viewBox/textLength. An uncapped vw size overflows the 1264px wrap at 1920.
- Track 0 to +0.02em, one weight, with 'AI' set apart only by a token color.
- Add the existing sun mark at the baseline, or the founder-approved vector lockup once it exists (T10-01).
- Add a warm horizon glow below the baseline. An optional ivory-to-amber gradient fill via background-clip:text needs a solid fallback for forced colors and print.
- Optionally, a one-shot letter rise with 'AI' warming, under no-preference only and never scroll-scrubbed (REFERENCE_SITE_REVIEW #31).
- Or remove the signature in a compact footer.
- Do not add a hero-sky strip here if the closing scene uses the art.

#### T8-06: Footer directory: detached arrow, off-system labels, three contact links and an improvised legal row (medium) *(needs founder material)*

- **Pages:** all pages (footer)
- **Evidence:** - justify-content:space-between (chrome.css:33) pins the 'Email Ata' ↗ at x≈1347, ≈360-420px from its label (home-desktop-06). On mobile, home-mobile-08 shows the label at x≈410 and the arrow at 727.
- The group headings 'The portfolio', 'The company' and 'Start a conversation' are 12px, dim, sentence case and tracked (chrome.css:31), while every other label on the site is an uppercase gold eyebrow.
- Three links go to /contact.
- The legal row puts '© 2026 Solarity AI LLC' on the left, 'Irving, Texas, United States' floating in the center, and 'About this contact experience' on the right (chrome.css:39-40; visual_chrome.py:64-66).
- On mobile the footer runs ≈890 CSS px (≈1.05 screens), driven by the intro headline and the 44px rows.
- **Problem:** The directory is loosely composed and looks improvised at exactly the place diligence-minded visitors scan for legitimacy (legal entity, privacy, official profiles).
- **Investor impact:** Visitors doing diligence read the footer for legitimacy signals, and the current row looks unfinished.
- **Fix direction:** - Place the ↗ inline after the label (flex-start). It stays on the mailto link only, per CLAUDE.md.
- Style the group labels with the caps label (T3-08).
- Merge the contact group into 'Investor inquiries', 'Partnership inquiries', email and booking.
- Shorten the mobile footer by removing or folding the intro headline (T8-02) and reducing the link count, keeping 44px non-overlapping targets, which the check suite expects.
- Rebuild the legal row as one left-aligned line.
- Privacy and Terms links, or official social profiles, need founder-supplied documents and URLs and must not be invented.

#### T8-07: The investor booking closer is a flat, square-cornered cream slab with no founder face (medium)

- **Pages:** investors-partners
- **Evidence:** investors-partners-desktop-05: a #f1ede3 rectangle with square corners at x88-1352, y135-509 (company.css:183-191, no radius). It holds a dark green-black (29,36,28) pill, 'View available times ↗', and a helper line that wraps to an orphaned 'tab.'. investors-partners-mobile-07 shows the same tall hard-edged block. Ata's face never appears on the Investors page; the built main content holds only the four screenshots. align-items:center keeps the desktop composition balanced but sparse. The same square paper device is used for the vision aside and the platform map.
- **Problem:** The highest-value investor action, booking time with the founder, is a plain banner that invites a founder conversation without showing the founder, and its corners break the radius system.
- **Investor impact:** Seeing the person behind a booking link makes a call feel like a meeting with a real founder rather than a calendar form, which lifts trust and conversion.
- **Fix direction:** Either:
- fold booking into the shared closing system (T8-02) with a small treated founder portrait (a 4:5 crop or a circle at ≈120-160px, reusing T7-01), 'Ata Turhan, Founder', 'View available times' as the solid primary and email as the secondary; or
- keep paper deliberately as the site's single paper moment, with the panel radius, a subtle warm gradient or grain, the portrait, and text-wrap:pretty on the helper line.

State no meeting length or response time unless the founder confirms them. Drop the portrait here if the T6-01 team strip already shows it nearby.

### T9 Motion and interaction

Apart from hover nudges, the explorer fade and a 180ms dialog arrival, the site is a set of still frames. The current design policy bans entrances and limits motion to feedback, and the October 12 motion layer was removed. Pages hard-cut, the hero scrolls away like a banner, the explorer blinks, the mobile menu snaps open, long pages lose orientation and FAQs jump. Motion is a finishing layer: it comes after light, composition and type, and all of it must respect reduced motion.


#### T9-01: The motion policy forbids the effects that make a site feel cinematic, and the motion tokens stop at 320ms (high)

- **Pages:** all pages
- **Evidence:** - README.md:170-174 documents an October 12 design/motion.css with a hero solar-light accent, a button sheen, a mobile-menu entrance and an FAQ answer entrance. build_site.py:117 style_sources lists eight files and no motion source.
- DESIGN_SYSTEM.md:63 bans 'hidden-content entrances'. REFERENCE_DESIGN_PASS.md:32 limits motion to 'feedback and short transitions'. CINEMATIC_REFINEMENT row 6 settles on 'restrained image movement'.
- REFERENCE_SITE_REVIEW.md:128-156 marked the title reveal (#4), phone entrance (#5), reveals (#16), sticky device crossfade (#24), drawer (#29), reading progress (#30) and logo hover (#32) as Keep or Adapt, and none exists.
- What survives: the hamburger morph (chrome.css:20-24), arrow nudges (accessibility.css:4-9), the screen lift (products.css:152-153) and the dialog entrance.
- dist/index.html has one @keyframes and zero view-transition rules. check_site.py:339 only checks that a reduced-motion rule exists.
- Tokens: only --motion-fast 180ms, --motion-detail 320ms and one --motion-ease (foundation.css:5). Durations are hard-coded at home.css:141, products.css:152, company.css:176 and accessibility.css:10. The longest motion on the site is a 500ms, 4px hover lift.
- **Problem:** Within these rules, every later pass can only produce restrained hover polish, and any new motion would be stuck at feedback speed.
- **Investor impact:** Unless the rule changes, the next design pass will produce another polished but static site.
- **Fix direction:** Replace the ban with a written motion contract in DESIGN_SYSTEM.md, enforced by check_site.py:
1. Entrance and scroll motion live only inside prefers-reduced-motion: no-preference, and scroll-linked motion also inside @supports (animation-timeline: view()). The static baseline is the complete page.
2. Never fade the hero LCP image or an above-the-fold H1 from opacity 0. Animate transform, clip-path and opacity only.
3. Entrances are one-shot, with at most one ambient loop site-wide, paused offscreen.
4. Touch parity: every hover effect has :focus-visible and :active equivalents.
5. JS is optional, under ≈1.5 KB, with any classes it adds registered in optimize_styles DYNAMIC_CLASSES.
6. check_site asserts that @keyframes, animation-timeline and @view-transition appear only inside the no-preference guard.

Add tokens:
- easings: --ease-out cubic-bezier(.16,1,.3,1), --ease-in-out (.65,0,.35,1), --ease-sun (.22,1,.36,1)
- durations: press 90, feedback 180, move 420, reveal 720, scene 1200, ambient 2400ms
- --stagger 70ms, and --rise 24px (16px on mobile)

Replace the hard-coded durations, and extend the existing token enforcement to cover them. Re-implement the lost October 12 items with these tokens rather than restoring old files.

#### T9-02: Every page arrives as one static frame (high)

- **Pages:** home, apps, platform, company, investors-partners, careers, contact, 404, apps-looks-max, apps-iq-max, apps-sleep-max, apps-fitness-max
- **Evidence:** home-desktop-01 and home-mobile-01: the eyebrow, H1, description, CTAs, artwork and app rail all appear at once, and nothing moves. The only @keyframes (surface-arrive) serves #image-dialog, which optimize_page strips from Home (performance_build.py:49-51), so no animation runs on Home at all. The hero source (home.css:3-18, visual_home.py:13-29) has no animation hooks. Interior openings behave the same (platform, company, investors, careers, contact and apps desktop-01). The 'restrained image movement' that CINEMATIC_REFINEMENT.md:14 claims is the 4px hover lift.
- **Problem:** No page has an arrival beat, so the first two seconds have no tempo to signal craft.
- **Investor impact:** Investors judge premium versus template in the first two seconds, and a page that appears all at once reads as a well-typeset template.
- **Fix direction:** One CSS-only arrival sequence under 1.2s, inside no-preference:
- The hero art settles from scale(1.05) to 1 over ≈1.6s, or does a slow 1.00 to 1.04 push-in. Transform only, never delaying first paint, so LCP is unaffected.
- The eyebrow and H1 lines rise from clip masks (translateY(100%) to 0, 600-700ms, 80ms stagger). This needs a build-time wrapper for each visual line, because the current span spans two desktop lines.
- The description and CTAs are visible from the first frame, with at most an 8-12px transform and no opacity start (REFERENCE_SITE_REVIEW #4).
- The four app icons rise as the last beat.
- Interior pages get a lighter eyebrow and H1 variant.

Measure LCP and CLS before and after, and drop the H1 mask on small screens if mobile LCP regresses.

#### T9-03: Below the hero nothing responds to scrolling (high)

- **Pages:** home, apps, apps-looks-max, apps-iq-max, apps-sleep-max, apps-fitness-max, platform, company, investors-partners, careers, contact
- **Evidence:** A grep of design/system/*.css and scripts/*.js finds no animation-timeline, view(), IntersectionObserver or reveal class. The only sticky rules are the header (chrome.css:3) and the dialog bar (foundation.css:91). Pages are long: home 5,384px, IQ 5,784px and investors 5,073px on desktop, and up to 6,895px on mobile (index.json). Static stretches include company-desktop-03 (team rows), platform-desktop-02 (module rows), investors-partners-desktop-01/02 (proof panel), -03 (thesis), apps-desktop-02/03 (catalog) and careers-desktop-03 (roles). Product motion is only a translateY(-4px) hover (products.css:151-156), company.css has only hover transitions (:65, :164, :176, :311), and the connector SVG is static and hidden on mobile (company.css:273).
- **Problem:** Every section arrives the same way, already at full contrast, so numbered sequences read as tables and proof points never land as moments.
- **Investor impact:** A long scroll with no rhythm feels like reading a memo, and skimmers miss the proof.
- **Fix direction:** A small vocabulary of about three reveal types, in CSS inside @supports(animation-timeline: view()) and no-preference:
- animation: rise both var(--ease-out); animation-timeline: view(); animation-range: entry 5% entry 45%, with translateY(24px) plus opacity tied to the view timeline. Content is visible once in view and never hidden in browsers without support.

Signature moments:
- The investor portfolio frames rise with a 90ms stagger while a hairline draws under each name.
- The product hero screen rises 24-40px and scales 0.96 to 1 (transform only, since it is the LCP image).
- The stage key light brightens.
- Filmstrip frames stagger in.
- The platform connectors draw (T6-03), and panels unfold.

Set the stagger with a build-time --i. Disclaimers and 'Conceptual strategy' notes are never revealed late, and body copy or an H1 already in view on load never animates. Firefox currently ignores the block, which is acceptable.

#### T9-04: The sunrise hero has no depth as the visitor scrolls (medium)

- **Pages:** home
- **Evidence:** home.css:14-17: a single object-fit cover image (object-position 82%/87%/86%) under a fixed two-gradient ::after. Between home-desktop-01 and 02 it scrolls away with the page like a banner. The artwork itself already has natural rays and a halo around the sun.
- **Problem:** The site's one cinematic asset gets no dimensional treatment.
- **Investor impact:** A flat treatment wastes the brand's strongest signal and pulls the impression toward 'nice stock header'.
- **Fix direction:** - Add artwork-only scroll depth (REFERENCE_SITE_REVIEW #7): animation-timeline: scroll(root) over roughly the first 100vh translates .progress-hero-image down 6-10%, with a matching overscale so no edge is exposed.
- Copy scrolls normally and never fades.
- Transform only, on one composited layer, inside the @supports and reduced-motion guards, at half amplitude on phones.
- Do not deepen the bottom mask; that would reverse CINEMATIC_REFINEMENT #8.
- A sun-bloom overlay is optional and fragile, because cover-fit moves the sun. Check it at 390px, 768px, 1024px and 1440px.

#### T9-05: Page changes are hard cuts, so product identity never carries from overview to detail (medium)

- **Pages:** home, apps, apps-looks-max, apps-iq-max, apps-sleep-max, apps-fitness-max, investors-partners, platform, company, careers, contact
- **Evidence:** A grep of dist/*.html finds zero @view-transition or view-transition-name rules. Every page prefetches same-origin links on intent (performance_build.py:21-24, 146-148), so navigations are instant hard cuts. The same icon and screenshot appear in the home explorer (home-desktop-02), the catalog (apps-desktop-01/02), the investor proof (investors-partners-desktop-01) and the product hero (apps-looks-max-desktop-01), yet each page starts from scratch.
- **Problem:** There is no continuity between pages, which misses an easy premium signal between overview and detail.
- **Investor impact:** Continuity is one of the clearest signals of a premium product site, and hard cuts make the pages feel like separate templates.
- **Fix direction:** - Add @media (prefers-reduced-motion: no-preference) { @view-transition { navigation: auto; } } to foundation.css. optimize_styles keeps unknown at-rules (optimize_styles.py:166-168). The global reduce rule (accessibility.css:13) does not reach ::view-transition pseudo-elements, so the guard must wrap the at-rule itself.
- Give the header view-transition-name: site-header, and cross-fade the root with a 12px rise over 380ms.
- Emit unique names at build time from APPS (for example looks-max-icon, looks-max-shot) on exactly one source element per page and on the product page's .detail-icon and .store-screen. Home shows each icon twice, so name only one of them.
- Browsers without support stay instant. No JS is needed, and prefetch stays prefetch-only (no prerender).

#### T9-06: The home product explorer blinks instead of crossfading (medium)

- **Pages:** home
- **Evidence:** home.css:62 sets inactive panels to visibility:hidden and opacity:0, and :67 makes the active panel visible. home.css:141 transitions only opacity over 320ms, so the outgoing panel vanishes instantly while the incoming one fades up from 0, leaving the stage briefly empty. The ::before glow is hard-coded gold (home.css:63) even though each panel carries data-product-accent. home.css:48-52 recolors only each tab's own 2px border, so nothing travels between tabs.
- **Problem:** The homepage's only interactive product moment is mechanical.
- **Investor impact:** This is where investors first meet the four apps, and a blink-swap feels like a generic tab widget.
- **Fix direction:** If the explorer survives T5-03:
- Inactive panels get transition: opacity var(--dur-move), visibility 0s linear var(--dur-move); the active panel gets a 0s visibility delay.
- Incoming copy rises 12px with a 60ms stagger, and the screenshot settles.
- Tint the glow with color-mix(in oklab, var(--product-accent) 16%, transparent).
- Add a single travelling indicator via :has().
- Keep the native radios, labels and print layout, with no motion under reduced motion.

The mobile visibility issue is covered in T5-13.

#### T9-07: Product stories scroll past as static two-column rows (medium)

- **Pages:** apps-looks-max, apps-iq-max, apps-sleep-max, apps-fitness-max
- **Evidence:** apps-looks-max-desktop-02/03 show the story heading, a large empty band, then copy on the left beside one screenshot. apps-iq-max-desktop-03 places copy beside the screenshot with the second step below. In apps-fitness-max-desktop-03 the right-hand screen is offset by a fixed margin-top:100px (products.css:92). The layouts are in products.css:76-93, with variants in product_story.py, and products.css:81 uses align-items:center.
- **Problem:** The 'INSIDE …' stories play like a brochure, and the Fitness offset is a frozen version of parallax.
- **Investor impact:** It misses the chance to turn authentic screenshots into a guided product walkthrough.
- **Fix direction:** - From 1024px up, make the story copy position: sticky; top: calc(88px + 8vh), with align-self:start, so it holds while the screenshot travels past. This is native scroll, with no pinning or scroll-jacking (REFERENCE_SITE_REVIEW #20, #25).
- Cross-fade the phase label and title per step with view timelines.
- Fitness: replace the static 100px offset with scroll-linked counter-motion (left column -24px; right column +80px to -40px).
- IQ: draw a hairline connector from step 1 to step 2.
- Mobile keeps the stacked order and uses only the reveal vocabulary.

#### T9-08: The mobile menu snaps open as a plain dropdown with no backdrop (medium)

- **Pages:** all pages (mobile)
- **Evidence:** From source only; no screenshot captures the open menu. chrome.css:46-56: #site-nav is an absolutely positioned #171a14 panel under the 76px header, with 74px rows, 12px descriptions and → arrows. .nav-enhanced #site-nav switches from display:none to flex via .is-open (navigation.js:30-40) with no transition. There is no scrim (body.nav-open only sets overflow:hidden), so the page under the ≈410-420px panel stays visible and undimmed, and the panel is greener than --bg. The 'mobile menu entrance' listed in README.md:172 no longer exists.
- **Problem:** Opening navigation, one of the most frequent phone interactions, is abrupt and utilitarian.
- **Investor impact:** On mobile the menu is the main route between Company, Platform and Investors, and it feels cheap on the device most investors use first.
- **Fix direction:** Design:
- A full-height overlay on --bg with a faint warm dawn glow at the bottom edge.
- Labels in large display type (28-32px), keeping the one-line descriptions.
- 'Investor inquiries' and 'Book a conversation' pinned at the bottom. The booking link keeps the 'opens in a new tab' text that check_site.py enforces.

Motion, instant under reduced motion:
- @starting-style with a display allow-discrete transition. 'overlay' is unnecessary because the menu is not a top-layer element.
- A clip-path reveal from inset(0 0 100% 0) to inset(0) over 360ms ease-out.
- Links rise 8px with a 35ms stagger (:nth-child or a build-time --i).
- A body.nav-open::after scrim fades in; nav-open is already in DYNAMIC_CLASSES.
- Closing reverses in 200ms.

Keep the disclosure semantics, inert, aria-hidden, Escape and focus logic, and the test-navigation.cjs contracts.

#### T9-09: Long pages lose their chapter navigation after the first screen (medium)

- **Pages:** investors-partners, apps
- **Evidence:** The investors 'On this page' index (company.css:110-115; visual_company_upgrade.py:14-15) appears only in investors-partners-desktop-01. Slices 02-06 give no orientation on a page that is 5,073px on desktop and 6,549px on mobile (index.json). The Apps anchor row (products.css:6-9) shows only in apps-desktop-01. CINEMATIC_REFINEMENT item 4 removed added chrome, and a sticky rail would take laptop viewport height.
- **Problem:** Readers get no progress cue and no 'you are here' while scrolling long pages.
- **Investor impact:** Investors skim, and without orientation they tend to leave before reaching the founder booking at the bottom.
- **Fix direction:** - First, add a decorative 2px solar progress hairline driven by animation-timeline: scroll(root), aria-hidden.
- Optionally, add a slim sticky chapter rail on desktop for Investors that slides in only once the hero index scrolls out. Highlight the current chapter via scroll-target-group and :target-current where supported, with an ≈0.6 KB IntersectionObserver fallback that sets aria-current.
- Update the single scroll-padding-top contract (UX_REFINEMENTS) so anchors clear both bars, and validate the rail against laptop heights and item 4 before shipping.
- On /apps, a rail is optional.

#### T9-10: List rows share one faint hover: a color change and a 3px arrow nudge (low)

- **Pages:** home, investors-partners, contact, apps-looks-max, apps-iq-max, apps-sleep-max, apps-fitness-max, 404
- **Evidence:** The same pattern appears in home.css:103-108, 144 (.strategy-module), company.css:159-166 (.partnership-topic), contact.css:36-41, 63-64 (.contact-topic), products.css:119-120, 155 (related apps), contact.css:56, 63 (recovery rows) and chrome.css:33-35 (footer links). Related-app and recovery rows add a flat surface wash. All of it is gated on hover with a fine pointer.
- **Problem:** The main routes into deeper content have consistent but faint feedback and no branded interaction.
- **Investor impact:** Uniform, faint hovers make the site feel like a default theme.
- **Fix direction:** Define one signature row interaction:
- an accent hairline draws across the bottom border (scaleX 0 to 1 from the left, 420ms)
- a soft 6-8% accent wash comes in from the left
- the arrow exits right and re-enters, and the title shifts 4px

Show the same on :focus-visible, and the wash on :active for touch. Apply it consistently to all six row families.

#### T9-11: FAQ answers appear instantly (low)

- **Pages:** investors-partners
- **Evidence:** The native <details> (ux_content.py:62-69; company.css:170-182) opens instantly, and only the '+' marker rotates (180ms ease, company.css:176-177). investors-partners-desktop-04 shows the five closed questions. The 'FAQ answer entrance' in README.md:172 no longer exists.
- **Problem:** Answers jump into place and push the content below them abruptly.
- **Investor impact:** A small but noticeable roughness on the page investors read most closely.
- **Fix direction:** As progressive enhancement, use interpolate-size: allow-keywords with details::details-content { transition: height var(--dur-move) var(--ease-out), content-visibility var(--dur-move) allow-discrete; }. The answer rises 6px, the marker rotates over 300ms, and the row uses the signature hover. Other browsers stay instant, and the native semantics are unchanged.

### T10 Brand mark, chrome and components

The components that appear on every screen look kit-made:
- a saturated clip-art sun beside a squeezed typed wordmark
- a header Contact pill that ties with each page's primary action
- a translucent header that smears content while scrolling
- a crowded mobile bar
- flat buttons with invisible hover and no press state
- border colors and radii that drift

The secondary routes (Contact, Careers, 404) carry the same issues at lower stakes.


#### T10-01: Brand mark: a saturated lemon flame sun beside an improvised typed wordmark, in three different brand expressions (high) *(needs founder material)*

- **Pages:** all pages (header and footer)
- **Evidence:** - The header (home-desktop-01, x88-228, y28-60) places a raster sun webp (visual_chrome.py:6-12) at 34px (chrome.css:8). It samples as ≈#ffcd07, (224-248,192-216,24-48), against the #edc78e accent and the 'AI' set in it (chrome.css:10).
- An alpha dump of solarity-sun-96 shows the bolt is opaque yellow and the center disc transparent. The official mark's white disc therefore becomes a dark hole on the dark UI, which reads as an eclipse or a ring.
- At 26-34px on mobile, the ≈20 rays and the zigzag bolt blur into a spiky splat (home-mobile-01, contact-mobile-01).
- The wordmark is live Manrope text at 18px, weight 600/500, -0.055em (chrome.css:7-10).
- The footer signature is a third version: 160px Manrope in off-token #e4dece/#b39d78 with no sun (chrome.css:37-38; visual_chrome.py:63).
- The official lockup (source-assets/brand/solarity-lockup-original.png) is a stacked portrait mark: the flame sun, an angular orange 'SOLARITY' and an 'ALWAYS BETTER' tagline. It does not suit a horizontal header, and the repo has no horizontal or SVG wordmark.
- **Problem:** The mark fights the muted solar palette, reads as clip art at small sizes, and sits beside body text dressed as a logotype. The header, the footer and the official lockup are three different brand expressions.
- **Investor impact:** Investors judge craft from the top-left corner of every page. A clip-art mark and a squeezed type wordmark read as a small-studio template and undercut every cinematic treatment elsewhere.
- **Fix direction:** Treat this as a founder-approved brand task:
- Ask for the vector logo and a decision on whether the angular SOLARITY wordmark returns or a refined custom horizontal logotype replaces it. Do not mix the two.
- Build one inline SVG lockup and reuse it in the header, footer signature, favicon and OG image.
- With approval: fill the sun disc (ivory or warm gold) so it reads as a sun on dark, tone the yellow into the solar ramp or make it the --sun-core highlight (T1-05), and create a reduced-ray variant for 40px and below. Keep the full-color original where required.

Until approval, make only non-brand-altering fixes: the same sun in header and footer, token colors, and tracking (T10-02). Never redraw the logo without the brand owner.

#### T10-02: The uppercase wordmark is set with negative tracking, so its capitals crowd (medium)

- **Pages:** all pages (header and footer)
- **Evidence:** The header renders '<b>SOLARITY <span>AI</span></b>' (visual_chrome.py:12) at 18px, weight 600, -0.055em (chrome.css:7), and R-I-T-Y bunch together in every header slice. The footer signature is uppercase at -0.065em, and the T and Y touch (home-desktop-06, home-mobile-08). The official lockup pairs its mark with a widely spaced tagline, the opposite treatment.
- **Problem:** The most repeated brand element looks like default text with crowded capitals rather than a crafted mark.
- **Investor impact:** The brand name at the top left of every page is the most-viewed type on the site, and a cramped setting makes the company look less established.
- **Fix direction:** Immediately, set capitals with zero or positive tracking in one weight: ≈+0.04 to +0.1em at header size and 0 to +0.02em at signature size. The vector wordmark question is separate (T10-01).

#### T10-03: The header Contact pill duplicates every page's primary action and has no current-page state (medium)

- **Pages:** all pages, home, careers, contact, 404
- **Evidence:** home-desktop-01 shows two identical gold pills in the first viewport: the header 'Contact →' (x1229-1352, (236,194,136)) and the hero 'Investor inquiries →' (x88-292, (238,199,142)). The same doubling appears in careers-desktop-01 ('Explore opportunities') and 404-desktop-01 ('Back to home'). On /contact the pill looks the same: visual_chrome.py:25-26 adds aria-current, but no CSS styles .button[aria-current]. Nav labels are 13px #c4c3b9 weight 500 (chrome.css:12), ≈10.6:1, so small rather than faint. The header stays 88px at every scroll position (chrome.css:6), ≈10% of a 900px viewport.
- **Problem:** Two equal-weight gold pills compete in almost every first viewport, and on Home the generic 'Contact' ties with 'Investor inquiries'.
- **Investor impact:** The investor path visually ties with a generic Contact button, which dilutes the one action the site exists to drive.
- **Fix direction:** - Make the header action a ghost or outline button with a warm bronze border token and an accent label, keeping solid gold for the page's single primary.
- On Home, keep it ghost over the hero and fill it after (T2-01), with a static fallback.
- Add a .button[aria-current] style.
- Raise nav labels to 14-15px with an accent underline drawn on hover and focus (static under reduced motion).
- Optionally condense the header to ≈64px after the hero using the same state switch, with no layout shift.

#### T10-04: The translucent homepage header smears headings and the portrait while scrolling (medium)

- **Pages:** home, platform, company
- **Evidence:** home-desktop-04: the blurred 'Improve the way' headline shows behind the logo. home-desktop-05: a blurred grey portrait rectangle sits under the wordmark (x65-395, y50-90). home-desktop-02 shows blurred icons along the top edge, and home-mobile-07/08 a grey haze. chrome.css:5 keeps #10120f9e plus blur for the whole scroll, and navigation.js has no scroll handling. Inner pages at #11120ff5 show faint ghosts (platform-desktop-04, company-desktop-04), and the interior bar is identical at rest and mid-page.
- **Problem:** Blur meant for the hero stays on for the whole page, smearing large headings and the white portrait into dirty, out-of-focus blobs that look like rendering glitches.
- **Investor impact:** The chrome looks smudged and unfinished just as investors read the strategy and founder sections.
- **Fix direction:** - Use the same state switch as T2-01: after the hero, render the header opaque on --bg with a hairline and a soft shadow (0 1px 0 var(--line), 0 12px 32px #0006).
- Remove the residual 4% transparency on inner pages.
- Optionally, hide the header on scroll down and show it on scroll up, with no movement under reduced motion.
- Keep the header height constant.

#### T10-05: The mobile header crams three heavy shapes into a 390px bar (medium)

- **Pages:** all pages (mobile)
- **Evidence:** home-mobile-01, contact-mobile-01, careers-mobile-01, company-mobile-01 and investors-partners-mobile-01 (2x) show the wordmark at x44-276, a grey-ringed circular toggle at x422-509 (chrome.css:18, #727469) and a gold 'Contact →' pill at x526-736. The pill is almost as wide as the logo and is the loudest element on the screen. The bar is 76px (chrome.css:43), and chrome.css:66 and :71 only tighten padding.
- **Problem:** On phones the brand is squeezed and the chrome feels busy, with two button languages side by side.
- **Investor impact:** Many investors first open a shared link on their phone, and a crowded top bar reads as a generic mobile template.
- **Fix direction:** - On narrow screens, show only the lockup and a borderless two-line menu icon in --text, keeping a 44px target.
- Move Contact into the menu as its pinned primary action (T9-08), or reduce it to a compact text link.
- Let the header be transparent over the mobile hero, with the same scrim and solid-after-hero switch (T2-01).

#### T10-06: Buttons: a flat fill, invisible hover, no press state, a grey-green outline and arrows on everything (medium)

- **Pages:** all pages
- **Evidence:** foundation.css:62-70 defines:
- a flat #edc78e fill whose hover lightens to #f7d9ab with a 0 4px 24px #edc78e14 glow (≈8% alpha, invisible on #11120f)
- a #727469 grey-green outline border (also :76; chrome.css:18) that clashes with the warm palette
- --text-sm/600 labels with a Unicode → at 20px, weight 400, thinner than the label

Arrows nudge 3px (accessibility.css:4-9). No :active selector exists anywhere; grep finds only forced-colors:active. The 'button sheen' in README.md:172 is gone. Nearly all motion is gated on hover (products.css:151, home.css:143, company.css:310, careers.css:127, accessibility.css:5, 8, contact.css:63-64), so touch gets almost no feedback. Arrows sit on the hero, strategy, founder, closing, contact topics and 404 list actions; footer arrows were already removed apart from 'Email Ata ↗'. Flat pill CTAs are not a defect in themselves.
- **Problem:** The CTA system is clean but characterless: hover feedback that doesn't register, an outline that clashes with the warm palette, an arrow so common it signals nothing, and no tactile response on tap.
- **Investor impact:** 'Investor inquiries' is the most important click on the site, and it feels no more crafted than a standard button.
- **Fix direction:** - Primary: keep the fill flat or nearly flat, with a subtle top-lit gradient or a 1px inner highlight.
- Hover and focus-visible: a perceptible warm bloom (≈0 8px 28-32px rgba(236,160,80,.3)), an optional one-pass solar sheen (700ms), and an inline-SVG arrow whose stroke matches the label, sliding out and back in (360ms).
- :active at scale .98 for 90-120ms with a faint accent wash, applied to buttons, rows, explorer choices, investor frames and related-app rows.
- Outline buttons: a warm translucent bronze hairline, with a fill rising on hover.
- Keep ink on amber at 7:1 or better and the 52px height unchanged.
- Reserve arrows for buttons and directional links; drop them from tertiary links.
- Mirror every effect on :focus-visible. Reduced motion keeps color changes only.

#### T10-07: Ad-hoc border colors and three radius languages (medium)

- **Pages:** careers, contact, all pages
- **Evidence:** Two border families drift side by side:
- green-grey: #727469 (foundation.css:66, :76; chrome.css:18), #64695a and #74796d (foundation.css:88, :93)
- bronze: #847359 (careers.css:37), #776a58 (:41), #50473a (:48), #8c7859 (contact.css:26)

There is also #80786b (careers.css:57), and the footer uses off-token #e4dece/#b39d78 (chrome.css:37-38). Radii mix 5px inputs and dialog buttons (--radius), 12px form panels and portraits (--radius-lg), 999px pills, and 0 on .founder-booking (company.css:183), investor-evidence-vision and platform-opening-map. careers-desktop-03 and careers-mobile-05 show cool-grey, square-ish inputs inside a warm bronze rounded panel above a full-width pill.
- **Problem:** The tokens cover backgrounds and text but not control borders, glows or radii, so each pass added one-off values.
- **Investor impact:** Premium brands feel premium partly through rigor, and inconsistent edges signal a site assembled in passes.
- **Fix direction:** - Add tokens to foundation.css: --line-strong, --control-border (one warm bronze), --control-border-hover (accent), --glow-accent, --radius-control (≈10px) and --radius-panel (≈20px). Keep --radius-pill for CTAs only.
- Replace every hard-coded border hex with these tokens.
- Give all panels the panel radius.
- Extend check_site.py's token enforcement.

This is pure CSS with no runtime cost.

#### T10-08: On desktop, the Contact page shows a half-empty first screen and puts booking below the fold (medium)

- **Pages:** contact
- **Evidence:** contact-desktop-01: the headline fills the left ≈840px, and x840-1352 is empty down to y≈600-620. The founder appears only as the text 'Ata Turhan' at y≈752. 'Book a conversation' sits at page y≈985 (the top of contact-desktop-02, half under the header), styled as an outline secondary, while 'Copy address' is a separate small pill (contact.css:26-31; visual_contact.py:33). The glow box shows an edge (T1-06). UX_REFINEMENTS #1 verified arrival only up to 768px. 'Investor inquiries' and 'Partnership inquiries' deep links go to /contact/?type=…#prepare-inquiry and land booking at ≈y480, so only arrivals from the header Contact button or a bare /contact link see the sparse opening.
- **Problem:** The generic arrival has no founder presence, and its booking action is buried and styled as secondary.
- **Investor impact:** Visitors who reach Contact from the header or a shared link meet a sparse page and must scroll to find the founder conversation.
- **Fix direction:** - Compose the opening as a two-column meeting frame: the headline on the left, slightly smaller; on the right, a founder card with the treated portrait (T7-01), name, role and Irving, Texas, with email and 'Book a conversation' at comparable weight.
- Both actions must be above the fold at 1440x900 and 1280x720 without a fragment.
- Use a full-bleed or masked glow.
- Keep direct email, booking, the no-collection statement and the contact.js context behavior unchanged.

#### T10-09: The contact topic list reads like a settings menu with detached arrows (medium)

- **Pages:** contact
- **Evidence:** contact-desktop-02 shows four hairline rows ('Investment conversations', 'Strategic partnerships', 'Product questions', 'Something else in mind?') with 16px titles and 14px grey descriptions. Each ↗ is pinned at x≈1340-1344, about 380px from its text, and hover only recolors the title (contact.css:36-41, 63-64). The page ends on a 13px 'About this contact experience' note (contact.css:42-46), which every footer links to as #data-note. contact-mobile-02 shows the same.
- **Problem:** Investor-facing choices carry the visual weight of preference toggles, and the far-right arrows feel disconnected from their labels.
- **Investor impact:** Choosing 'Investment conversations' should feel like opening a door. Here it feels like a form option.
- **Fix direction:** - Turn the topics into a 2x2 grid of tall tiles on desktop (stacked on mobile), with larger titles, the arrow beside the label, and Investment conversations first.
- On hover and focus-visible, add a warm edge glow and a slight lift; static under reduced motion.
- Keep one visible no-collection sentence next to the email or the topics ('Email opens your mail app; this site does not collect messages').
- If the remaining fine print moves into a <details>, make sure #data-note opens it. Otherwise keep the section visible as a quiet closing note.

#### T10-10: Careers application area: an empty left column, boxy fields, helper-text clutter and the disclosure at the commit point (medium)

- **Pages:** careers
- **Evidence:** - careers-desktop-04: the left column is empty from y140 to 700 apart from a lone 'Copy address' pill, and ≈200px of dead space follows the form.
- careers-desktop-03: the inputs are #12120f boxes with a 1px #80786b border and a 5px radius, inside a 12px-radius #50473a panel (careers.css:48, 57).
- careers-mobile-05: all six fields carry a 12-13px helper line, the LinkedIn placeholder truncates to 'your-nam', and the select text renders larger and heavier than the input placeholders.
- The 12px dim FormSubmit disclosure with two underlined links sits directly above the full-width 'Continue application ↗' (careers.css:41-73; visual_careers.py:80-104).
- **Problem:** The form works but feels like a utility form, not a premium recruiting moment.
- **Investor impact:** Partners and investors also look at Careers to judge team-building maturity.
- **Fix direction:** - Make the left column sticky (top: 112px) so the heading, the email alternative and a short, honest 'What happens next' sequence travel with the form. The sequence describes the FormSubmit verification and confirmation flow without promising delivery or a reply.
- Restyle the controls: 56px tall, warm --control-border, an accent focus ring, and radii consistent with the panel (T10-07).
- Keep helper text only where it prevents errors, such as the URL fields, and shorten the LinkedIn placeholder (careers.js withScheme completes scheme-less input).
- Keep the disclosure immediately adjacent to the button as a quiet note, since it explains the third-party handoff before commit.
- Make 'Copy address' an inline icon button beside the email.
- Keep FormSubmit, the CAPTCHA, the honeypot and the email fallback unchanged.

#### T10-11: The 404 page is bare text on an inset grid that doesn't align with the site, and its art is gone (medium)

- **Pages:** 404
- **Evidence:** 404-desktop-01: the content starts at x=200, while the logo and footer align at x=88, because .not-found's max-width of 1040px narrows the wrap itself (contact.css:49). The right half of the first viewport is empty, holding only the headline, two pills and a numbered link list. 404-mobile-01 shows text and pills only. contact.css:54 hides .recovery-art, but recovery_art() (ux_content.py:105) is never called, so it is dead code and UI_REFINEMENTS item 6's orbital composition is gone. The headline uses the 'This page / is not here.' couplet (T3-04).
- **Problem:** The page's own metaphor, 'A different path', calls for the stair-climb imagery, yet it is the plainest page on the site and is visibly misaligned with the chrome.
- **Investor impact:** Broken links from decks and emails land here, and a bare page looks unfinished.
- **Fix direction:** - Align the content to the standard .wrap edge.
- Add an atmospheric backdrop: CSS light tokens, or a darkened, masked crop of the approved sunrise from the existing optimized variants. The crop counts against the image budget (T8-02) and keeps the 'Conceptual brand artwork' labelling if the scene is recognizable.
- Make the backdrop decorative (a CSS background or empty alt) with fetchpriority=low, not lazy, because it sits above the fold.
- Use the shared interior arrival variant (T9-02).
- Restyle the recovery links like the contact tiles.
- Remove the dead recovery_art() helper, and do not restore retired artwork.

#### T10-12: Careers roles: a plain ruled list and a raw Google Drive exit (low)

- **Pages:** careers
- **Evidence:** careers-desktop-02: role rows have a 12px gold discipline label, ≈30px titles, grey tags and an outlined 'Apply ↓' pill with a #847359 border (careers.css:31-38), under the duplicated eyebrow and heading 'FIND YOUR PLACE' / 'Find your place.' (T3-07). careers-desktop-03 and careers-mobile-04: 'Want to learn more before applying? View job posters ↗' links to a Google Drive folder (visual_careers.py:35, 78).
- **Problem:** The open roles get the same hairline-list treatment as everything else, and sending candidates to a raw Drive folder breaks the premium frame.
- **Investor impact:** A minor credibility leak suggesting the hiring surface hasn't had the same care as the product pages.
- **Fix direction:** - Make each role row a whole-row link with a larger title, a warm hover glow and the Apply action revealed on hover and :focus-within, staying visible on touch. Keep the careers.js role preselection.
- If the founder supplies the poster content, present full role descriptions in-page as native <details>. Otherwise label the link 'Full role descriptions (Google Drive)'.


## Appendix B: The three proposed directions


### Direction: solar-cinema

#### Solar cinema: a creative direction for solarityai.com

#### 1. Concept

Each page is shot as one day of light. Home opens on the climax, the approved sunrise, framed like a film's first shot. From there, every page moves through night, blue hour, first light and a golden horizon at the close. Scrolling raises the sun, so the investor ask always sits in the warmest light on the page. The idea fits a company whose products are about gradual ascent. Controlled light, confident title cards and restraint also signal taste to investors, which is the quality the four apps need to prove.

Three rules hold everywhere:
- Use one cinematic device per viewport.
- Light always comes from the sun's side, at the upper right.
- Evidence is lit. Vision is outlined.

**Solves:** T1-01, T1-03, T8-01, T8-03, plus the root cause that earlier passes were never reviewed in a browser. Every value here is tuned from rendered 1440px and 390px screenshots before it ships.

#### 2. Typography (T3-01 to T3-12, T10-02)

**Title face:** Instrument Serif Regular (OFL), self-hosted as one Latin-subset woff2.
- About 20-25 KB, to be measured after subsetting.
- `font-display: swap`, with a metric-matched "Title Fallback" built on `local(Georgia)` with size-adjust and ascent/descent overrides.
- Every route opens with a title card, so it is fingerprinted and preloaded on every route.
- An italic cut adds about 22 KB. Use it only if the founder's specimen chooses italic emphasis.
- Alternatives for the specimen: a static Newsreader Display instance (estimated 30-40 KB), or option B, a light-weight Manrope display at 0 KB.
- This reverses the October 13 one-family decision, so the founder must sign off.

**Manrope** (the existing 26 KB variable file) stays for UI, body, deck, labels and team names. Keeping names in Manrope also keeps the serif subset free of Turkish glyphs.

**Scale:** five tokens in foundation.css, with check_site rejecting raw clamp() sizes anywhere else:

| Token | Size | Face and setting |
|---|---|---|
| title | clamp(3.25rem, 1.6rem + 5.2vw, 7.5rem) | Serif, -0.015em, line-height .96 |
| chapter | 2.6–4.75rem | Serif, -0.01em |
| section | 2.1–3.25rem | Manrope 500, -0.015em |
| sub | 1.4–2rem | Manrope, -0.005em |
| deck | 1.15–1.5rem | Manrope 400, line-height 1.42, `--text` |

- Body text is 17-18px at line-height 1.58.
- No negative tracking below 28px.

**Treatments:**
- **Title card:** once per page, two lines at most. The split couplet appears only in the home hero and the closing statement.
- **Credits label:** Manrope 600, 12px, uppercase, +0.14em, in `--sand`. It is used for slates, the hero credits row and footer groups. A mixed-case meta label (14px, zero tracking) covers everything else. Product names are never tracked.
- **Slate:** a credits label over the anamorphic horizon rule (section 3). It replaces most eyebrows, which are cut by about two-thirds.
- **Numerals:** lining, tabular Manrope everywhere. Large serif numerals appear only on Platform's real Build, Operate, Grow sequence. The mono font is removed.
- `text-wrap: pretty` on paragraphs, list items and captions.
- The wordmark's capitals are tracked +0.06em.

#### 3. Color, light and texture

**Warm neutrals (T1-04):**
- `--bg` #0f0d0b, `--surface` #18140f, `--raised` #221c16, `--line` #3a3027, `--ink` #1a140e
- `--muted` #c9c0b2, `--dim` #a99f91

**Solar ramp (T1-05):**
- `--sun-core` #ffcf7a: one focal element per viewport
- `--gold` #e9b56a: active states
- `--sand` #d6bf9a: labels
- `--bronze` #9c7446: rules only, never text
- `--ember` #d9782f: bounce light
- `--haze` #f5dfbb

**Time of day (T1-01):** four stops sampled from the hero:
- `--night` #0b1118, from the art's upper-left slate
- `--blue-hour` #121821
- `--first-light` #1a140f
- `--golden` #2a1a0e

Each page's background is one document-length gradient through these stops, with no JS and no repaint on scroll. Computed against the lightest stop, `--muted` is about 9:1 and `--dim` about 6:1.

**Light tokens (T1-03, T1-06):**
- `--glow-sun`: rgba(255,190,110,.28) at the core, fading out over 55% of the radius.
- `--glow-ember`: rgba(217,120,47,.18).
- Glows sit only behind focal objects, always larger than their box and masked, so they never show an edge.

**Anamorphic horizon rule (T8-03):** a 1px line that feathers out at both ends, with a 6:1 elliptical bloom. It is the site's only divider and replaces the structural hairlines.

**Grain:** a 128px tiled noise WebP generated by Pillow in optimize_images.py (about 2 KB), at 4% on scene layers only. It is never a fixed, blended overlay.

**Surfaces (T1-02, T10-07, T6-02):**
- Paper is retired.
- Panels become smoked glass: a gradient from #1f1913 to #120f0c, an inner top highlight of rgba(255,220,170,.10), and one `--radius-panel` of 20px.
- Vision panels stay unfilled, with a dashed warm hairline and the `.status.vision` chip.

**Product light conditions (T5-01):**

| App | Light | World color | Text tint |
|---|---|---|---|
| Looks Max | Violet dusk | #7a35c9 | #e3c8ff |
| IQ Max | Cobalt morning | #2a4fd0 | #c3f2ee |
| Sleep Max | Moonlit night | #262c78 | #ccd0fb |
| Fitness Max | Ember | #ff5a1f | #ffc4a6 |

Vivid hues appear only on stages and glows. Body text stays ivory, and gold is reserved for company-level actions.

#### 4. Motion (contract in DESIGN_SYSTEM.md, enforced by check_site; T9-01)

**Tokens:**
- Easings: `--ease-out` (.16,1,.3,1) and `--ease-sun` (.22,1,.36,1).
- Durations: press 90ms, feedback 180ms, move 420ms, reveal 720ms, scene 1200ms.

**Home arrival (T9-02):** the first frame is complete and readable.
- Two matte letterbox overlays (about 150px at 1440×900, holding the nav) retract with scaleY over 1.2s. A 2.39:1 frame opens to full-bleed. The image itself is never clipped or faded.
- The art settles from scale 1.05 to 1 over 1.6s.
- On desktop only, the H1 lines rise from clip masks: 650ms with an 80ms stagger.
- The lede and actions move 10px by transform only, with no opacity start.
- The four credits-row icons arrive last.
- The sequence plays once per session, using about a 0.2 KB guarded sessionStorage check.

**Interior arrival:** the H1 is visible at first paint with a 12px rise, and the horizon rule draws in with scaleX over 600ms.

**Reduced motion:** no bars and no movement. Every page shows its static final frame.

**Scroll (T9-03, T9-04, T9-07, T9-09):** pure CSS, inside `@supports (animation-timeline: view())` and the no-preference guard.
- The hero art drifts 8% (half that on phones).
- On desktop only, one fixed key light rises and brightens with `scroll(root)`, using opacity and transform on one layer.
- Three reveal types (rise, unfold, draw), with entry ranges of 5-45%.
- Story copy is sticky on product pages, and the Platform connectors draw in.
- A 2px solar progress hairline runs across the top.
- Disclaimers never reveal late.
- Firefox gets the complete static page.

**Page transitions (T9-05):**
- `@view-transition { navigation: auto }`, inside the no-preference guard.
- The root dissolves through warm black over 380ms with a 12px rise, and the header persists.
- Unique names emitted at build time let the icon and hero screen morph from /apps or Home into the product page.
- Browsers without support stay instant.

**Interaction:**
- The header is transparent over the hero and turns solid after it, with about 0.5 KB of IntersectionObserver in navigation.js (T2-01, T10-04).
- The mobile menu becomes a full-height overlay with a clip-path reveal (T9-08).
- Buttons get a visible bloom on hover and focus, and a press state (T10-06).
- One shared row interaction (T9-10).
- FAQ answers animate their height (T9-11).
- The gallery becomes a screening room with a shared-element zoom (T4-07).

**Budget:**
- 1.5 KB or less of new JS in total.
- About 3-4 KB of CSS per route after gzip.
- CLS of 0: constant header height, metric-matched fallbacks, and only transform, opacity and clip-path animated.
- LCP and CLS measured in Lighthouse before and after. No result is claimed until it has been run.

#### 5. Imagery

**The sunrise (T2-01 to T2-06):**
- Full-bleed at 100svh, with the nav transparent over a baked 150px top scrim.
- Warm umber scrims that clear by 50% of the width, plus a local radial behind the copy.
- An anamorphic streak on the sun's horizon line, and a 500px amber afterglow into the next scene.
- Grading is done in CSS only.
- The credits row of four authentic icons forms the designed bottom edge.
- **Mobile:** 580px of art, with the headline set on its lower fade and the "Conceptual brand artwork" caption on a dark-glass chip at 4.5:1 or better.
- **Elsewhere:** only a pre-blurred light field of 3 KB or less, which is not recognizable as the scene. The single recognizable reprise is the 404 page.
- Needs from the founder: a master of at least 3720px wide.

**App Store screenshots ("screened"):**
- One plate for every image: uniform radius, a 1px inner rim, a rim light in the product hue from the upper right, and a soft floor glow instead of a drop shadow.
- Build-time crops remove the baked edge hairlines (T4-05) and, for hero and story placements, the poster headline bands (T4-02). Crops are recorded in the manifest, and full posters stay in the dialog.
- No recoloring and no fabricated device frames.
- Display size stays at 340 CSS px or less until the native-resolution re-fetch (T4-03), then rises to 440-520px.
- IQ Max sits on a deep cobalt stage so it reads as a lit object rather than glare (T4-06).

**Founder portrait (T7-01):**
- A 4:5 crop, a vignette mask into the scene, a warm rim light and a hairline frame.
- Any grade needs approval. The background is never replaced.

#### 6. Page by page

| Page | Scene | Treatment |
|---|---|---|
| Home | Cold open to golden close | Letterboxed sunrise and credits row. A portfolio wall of four lit, cropped screens, each with its icon and store link. A sunrise diagram of the app factory in the vision register. The founder plate (the statement is pending from the founder). One horizon close. T2-01–T2-06, T5-03, T6-04, T6-07, T8-04 |
| Apps | Lineup at first light | Title card, with the four icons at 112px on their glows serving as the anchor nav. Each product row is a full-bleed world band with a stretched-link card and compact official badges. Mobile cards stay at 60svh or less. T5-04, T5-11, T5-12, T5-16 |
| Looks Max | Violet dusk | Icon at 104px with the product name as the title. The slogan becomes the deck, with badges beneath it. A "scan" chapter with a sticky screen and detail crops. T5-02, T5-05, T5-08, T5-09 |
| IQ Max | Cobalt morning | A straight UI frame as the hero, with the poster moved to the gallery. A focus-to-routine sequence with a drawn connector. T4-06 |
| Sleep Max | Moonlit night | A full-bleed night hero with badges directly under the title, and Soundscapes rising from an indigo glow. The empty-profile frame is removed until the founder supplies a populated screen. T5-06, T5-10 |
| Fitness Max | Ember | A day-log triptych with scroll counter-motion. The Only Fitness name is stated once, in the badge block. T5-15 |
| Platform | Blueprint at first light | A luminous SVG: the four icons form a solid sun core, the vision nodes are dashed, and the connectors read as "informs", with a legend. Sticky module splits with outlined stage words. One partnership CTA. T6-03, T6-05, T6-09–T6-12 |
| Company | Portrait at dawn | The founder plate. The team as an end-credits block, names only, with no invented roles. A "story so far" strip only with dates the founder confirms; otherwise a four-icon strip. The principles become one statement. T7-03, T7-04, T6-06 |
| Investors & Partners | The screening room | A fact line and an at-a-glance band of verified facts. A four-frame showroom under an overhead spotlight, with icons and store links, fully in the first viewport. A Today/Ahead ledger. The close carries the booking with the founder's portrait. T6-01, T6-02, T4-04, T6-08, T8-07 |
| Careers | Call sheet | Roles as whole-row credit lines. The form in a smoked-glass panel with a sticky left column. No repeated portrait. T10-10, T10-12 |
| Contact | Meeting frame | The headline beside a founder card, with email and booking at equal weight above the fold. Topic tiles in a 2×2 grid. A masked glow. T10-08, T10-09, T1-06 |
| 404 | A different path | The one recognizable sunrise reprise: a darkened stair crop of 600 CSS px or less, captioned. Content aligned to the standard .wrap edge, with recovery tiles. T10-11 |

**Chrome:**
- A compact footer with a dusk lead-in. The wordmark is sized to its container with cqi and carries the sun mark. No second slogan. (T8-02, T8-05, T8-06)
- The header Contact becomes a ghost button, with a style for the current page. The mobile bar holds only the lockup and the menu icon. (T10-03, T10-05)

#### 7. What stays, risks and effort

**Unchanged:**
- The hero composition and its provenance.
- All authentic screenshots, icons and the portrait.
- The four app names and the Only Fitness disclosure.
- Direct email and booking, with no message collection.
- The Careers FormSubmit flow.
- Native radio, details and dialog semantics, focus handling and `inert`.
- The static Python build and Manrope.
- check_site contracts, each updated in the same change whenever a contract moves (hero widths, the explorer radios).

**Risks:**
- **Gimmick:** the letterbox, grain and flares must stay subtle, one device per viewport, and be tuned on rendered screenshots.
- **Contrast:** AA must be rechecked at every glow and on the hero's lightest pixels.
- **Browser support:** scroll timelines and cross-document view transitions are not universal, so the static page must be complete on its own.
- **Low-end phones:** the fixed key light is desktop-only.
- **Founder sign-off:** the display face, the product hues and the wall replacing the explorer all need approval.
- **Resolution:** larger stages expose the 1860px hero and the 600px screenshots until new assets arrive.

**Effort:**

| Element | Effort |
|---|---|
| Light, color and grain tokens, horizon rule | M |
| Display face, scale tokens, fallbacks | M |
| Home hero and arrival | M |
| Product worlds, stages and crops | L |
| Portfolio wall and Apps lineup | M |
| Four signature product chapters and filmstrips | L |
| Platform SVG and modules | M |
| Investors restructure | M |
| Company, Contact, Careers, 404 | S–M each |
| Closing horizon, footer, header | M |
| Motion contract, reveals, view transitions | M |
| Screening-room gallery | S–M |

**Needs founder-supplied material:**
- A higher-resolution hero master.
- Approval of re-fetched native-resolution screenshots, and clean UI exports.
- A populated Sleep Max screen.
- A first-person founder statement, signature and profile link.
- An editorial founder portrait.
- Team roles and portraits.
- Verified dates and metrics.
- The vector logo and a wordmark decision.
- Privacy and terms links.
- Sign-off on the type specimen and on any rewritten headlines.


### Direction: private-editorial

#### Solarity Review: a private-bank editorial direction

#### 1. Concept
The site becomes a privately printed annual review. The sunrise is the cover plate. The products and the vision sit in night-ink chapters, and each page gets at most one daylight ivory spread, kept for verified facts and for the founder. Display serif type, generous margins, hairline ledgers and one lit object per scene present four shipped apps and a named founder as solid assets rather than as a startup template. The brand promises disciplined self-improvement, and exact, unhurried presentation shows that same discipline to investors.

Earlier passes read as average because they made everything the same (one face, one weight, one surface, one accent) instead of choosing where to put emphasis, and because nobody reviewed them as rendered pages. Under this direction, no value counts as done until it has been checked in 1440px and 390px screenshots. Solves: T8-01, T1-01, root causes 2, 3 and 6.

#### 2. Typography
Solves: T3-01 to T3-13, T2-03, T10-02.

**Typefaces**
- **Display face:** Newsreader (OFL). Use two static Latin-subset cuts taken from the variable font at opsz 72: Light 300 and Light 300 Italic. I estimate 25-35 KB each as WOFF2; measure after subsetting.
- **Alternative:** the founder's specimen should also show Source Serif 4 Display (OFL) in the same two cuts. Avoid Instrument Serif, which has become the stock serif of startup templates.
- **UI and body:** keep Manrope variable (26.3 KB in `dist`). Use weight 400 for body and decks and 600 for labels and buttons. Headlines never use weight 500.
- **Font budget:** at most 70 KB of new font files. Preload the roman cut only on routes where a serif H1 is above the fold.
- **Loading:** use `font-display: swap` with metric-matched fallbacks: Georgia with `size-adjust` for the serif, Arial for Manrope.

**Scale (1440px / 390px):**

| Token | Size |
|---|---|
| Title | 112 / 52px |
| Chapter | 72 / 40px |
| Section | 48 / 32px |
| Sub | 30 / 24px |
| Deck | 22 / 19px |
| Body | 18 / 17px |
| Meta | 14px |
| Caps label | 12px |

`check_site.py` should reject raw `clamp()` font sizes outside `foundation.css`.

**Setting**
- Serif line-height 1.02-1.08.
- Tracking from -0.015em on titles to 0 on sub headings. No negative tracking below 28px or on capitals.
- Emphasis uses the italic cut only, never a second color or weight.
- Gold marks at most one focal word per page.
- Two-line couplet headlines appear only on the home cover and in the closing scene.

**Typographic devices**
- **Folio:** a 32px bronze rule plus a caps label, at most one per chapter, with no numbers. Eyebrows are cut by about two-thirds.
- **Ledger rows:** caps label on the left, serif value on the right.
- **Founder pull quote:** set with hanging punctuation.
- **Numerals:** lining tabular Manrope for indices. Serif lining figures only for large values and the three platform numerals.
- **Line breaks:** `text-wrap: pretty` on all running text.

#### 3. Color, light and texture
Solves: T1-01 to T1-06, T5-01, T10-07, T1-04, T1-05.

**Neutrals**

| Group | Tokens |
|---|---|
| Ink (warm axis) | `--ink-0` #0c0a08 (footer), `--ink` #12100d, `--ink-1` #1a1612, `--ink-2` #241e18, `--rule-ink` #3a3027 |
| Ivory | `--ivory` #f3ece0, `--vellum` #e9dfcc, `--ink-on-ivory` #1d1712, `--rule-ivory` #cbbfa9 |
| Ivory labels and accents | `--label-on-ivory` #6b5434 (about 6:1), `--ember-on-ivory` #8a4b1c (about 5.7:1) |
| Text on ink | #f3ece0, #c9c0b2, #a99f91 |

**Solar ramp**
- `--sun-core` #ffcf7a: one focal element per viewport, normally the primary CTA.
- `--gold` #e9b56a.
- `--sand` #d6bf9a: labels.
- `--bronze` #9c7446: rules only, never text.

**Other new tokens:** `--radius-control` 10px, `--radius-plate` 14px, `--radius-panel` 20px, and one bronze `--control-border`.

**Ink and ivory**
- A page may have at most one ivory spread. It is always full-bleed and never a boxed panel.
- Ivory carries evidence or people, never the vision.
- The way in is a 200px "daybreak bridge", a gradient from ink through ember #3a2214 and haze #f5dfbb to ivory, with grain over it to prevent banding. The way out is a clean cut, like turning a page.
- This departs on purpose from T1-02's advice to use paper once at most. What failed there were half-width, square-cornered boxes that carried the vision. If rendered review still shows glare, reduce ivory to the Investors ledger alone.

**Light**
- One key light from the upper right, at about 85% of the width to match the sun.
- Its radial core is rgba(255,190,110,.24-.28). Place it only behind each scene's lit object: a product plate, the founder or the primary CTA.
- Add an ember bounce light at the foot of long pages.
- Remove the ring motif.

**Texture:** a 2 KB tiled noise at 4% on ink, and a paper fiber at 2% on ivory. Never use a fixed full-viewport overlay.

**Product colors (stage / glow / text tint)**

| Product | Stage | Glow | Text tint (AA) |
|---|---|---|---|
| Looks Max | #1e0f30 | #7a35c9 | #e3c8ff |
| IQ Max | #0c1838 | #2a4fd0, with a #9fe8dc mint rim | #c3f2ee |
| Sleep Max | #0f1230 | #262c78 | #ccd0fb |
| Fitness Max | #160b06 | #ff5a1f | #ffc4a6 |

Vivid color appears only on stages and glows; body text stays ivory. Company gold is kept for investor and partner actions.

#### 4. Motion
Solves: T9-01 to T9-11, T2-01, T10-04.

**Motion contract.** Write it into DESIGN_SYSTEM.md, enforced by `check_site.py`:
- Easing `--ease-out` cubic-bezier(.16,1,.3,1).
- Durations 90, 180, 420, 720 and 1200ms.
- Stagger 80ms, and a 20px rise (12px on mobile).
- All motion sits inside `prefers-reduced-motion: no-preference`. Scroll-linked motion is also inside `@supports (animation-timeline: view())`. The static page is always complete.

**Load sequence** (CSS only, no JS, under 1.2s):
1. The cover art settles from scale 1.04 to 1 over 1.6s. Transform only, never opacity, so LCP is unaffected.
2. The headline lines unmask from a clip-path over 700ms, staggered 80ms.
3. The folio rule draws in (scaleX, 600ms).
4. The row of app icons rises last.

Interior pages animate only the folio and the H1. Under reduced motion everything is static. If mobile LCP regresses, drop the H1 mask on phones.

**Scroll**
- Only three reveal types:
  - **Rise:** content moves up into place.
  - **Rule draw:** ledger hairlines draw from left to right.
  - **Plate settle:** the screen scales from .97 to 1 while its key light brightens.
- The hero artwork alone moves at 6-8% parallax, half that on phones.
- Split sections use native sticky headings.
- Investors, Platform and the product pages get a 2px sun-core progress line.
- Disclaimers, and any H1 already on screen at load, never animate.

**Header.** Transparent over the home cover and solid ink after it. A roughly 0.4 KB IntersectionObserver in the already-inlined `navigation.js` toggles a class, registered in `DYNAMIC_CLASSES`. The header height never changes.

**Page transitions**
- Cross-document `@view-transition` inside the no-preference guard: a 280ms root crossfade with an 8px rise.
- The header is a named element that stays still.
- Each app's icon and plate get a shared name generated from APPS, on one element per page, so they carry over from /apps to the product page.
- Browsers without support keep instant cuts.

**Budget:** at most 1.5 KB of new JS, about 4 KB of motion CSS (estimated), and CLS 0, using only transform, clip-path and opacity. Measure LCP and CLS before and after.

#### 5. Imagery
Solves: T2-02 to T2-06, T4-01 to T4-08, T5-05, T7-01.

**Sunrise cover**
- 100svh, clamped to 720-1080px, edge to edge.
- Scrims retinted to warm umber, tapered so they clear by half the width, plus local protection behind the copy.
- The caption becomes a plate credit inside the bottom scrim. Its wording stays "Conceptual brand artwork", at 4.5:1 contrast or better.
- Grading happens in CSS only. A baked-in grade needs founder approval.

**Sunrise reprise.** The recognizable image appears once more on the whole site: a 2.39:1 letterboxed crop, at most 560px tall and captioned, behind the Investors booking close. Every other page uses CSS light or a pre-blurred derivative of a few KB.

**App Store screenshots as "plates"**
- **Plate treatment:** each sits on a matte in its product's stage color, lit by its key light, with:
  - the same radius on every image
  - a 1px inner highlight and a warm rim
  - a soft contact shadow
- **Build-time crops** in `optimize_images.py`:
  - Remove the baked-in edge hairlines.
  - On hero placements, remove the poster's headline band, so the page H1 is the only headline.
  - Leave the originals untouched, record every crop, and keep the full posters in Enlarge.
- **IQ Max** sits on cobalt with a mint rim and is never cropped to its tilted phone.
- **Captions:** one provenance line per gallery.
- **Size:** at most 340 CSS px until the native-resolution re-fetch (T4-03) lands, then 440-520px.
- UI pixels are never recolored or altered.

**Founder portrait**
- A 4:5 crop.
- On ivory it becomes a framed print with a 12px vellum mat and a 1px rule, so the white studio backdrop reads as paper rather than glare.
- On ink it gets a vignette mask and a warm rim light.
- The background is never replaced, and any grade needs founder approval.

**Store badges.** Official App Store and Google Play badges, unmodified, self-hosted as SVG.

#### 6. Page by page

- **Home:**
  1. The cover, with a row of four authentic icons and "Four apps · iOS & Android".
  2. A portfolio wall: four plates in their product colors, each with icon, category and store badges (T5-03, T6-07).
  3. An ink app-factory chapter in the vision register: the four icons, an arc of light, then three dashed nodes with the vision chip (T6-04).
  4. An ivory founder spread. The statement slot renders only once a statement is supplied (T7-01, T7-02).
  5. A closing horizon scene (T8-02).
- **Apps:**
  - A masthead of four 112px icons, each on its glow, acting as the anchor navigation.
  - Alternating spreads led by the serif product name. Each card is a stretched link, with the badges as separate links.
  - On mobile, compact cards no taller than 60svh (T5-04, T5-11, T5-12).
- **Looks Max, IQ Max, Sleep Max, Fitness Max:** no ivory; the products live at night.
  - **Opening:** a 104px icon, the product name as a serif H1 with the slogan as its deck, and badges directly under it. The Only Fitness disclosure appears once, inside the badge block.
  - **Signature chapter, one per app:**
    - Looks: crops of the scan cards.
    - IQ: the sequence from focus selection to routine.
    - Sleep: a full-bleed night chapter of Soundscapes crops, with the empty-profile frame removed.
    - Fitness: a day-log triptych.
  - **Then:** a filmstrip of claims-cleared screens, a closing band in the product color, and three sibling plates (T5-01 to T5-17, T9-07).
- **Platform:** all ink, in the vision register throughout.
  - The diagram: the four icons as the solid source, an arc of light leading to three outlined nodes, and a legend in the first viewport.
  - Sticky module splits with serif numerals, and one partnership CTA (T6-03, T6-05, T6-09 to T6-12).
- **Company:**
  - A factual headline (copy needs founder approval) and an ivory founder letter.
  - The team as two-column credits with 24px serif names. No roles until they are supplied.
  - A four-icon "story so far" strip, with dates only if confirmed (T7-03, T7-04).
- **Investors & Partners:**
  1. A one-line index.
  2. A showroom with all four plates in the first desktop viewport.
  3. An ivory "At a glance" ledger of verified rows only, with a Today / Ahead pair in which Ahead is dashed and chipped. Slots are reserved for metrics, but nothing renders until the founder supplies verified figures.
  4. Partnership tiles, and an FAQ that animates open.
  5. The sunrise reprise as the close, with the founder portrait and "View available times" as the primary action (T6-01, T6-02, T4-04, T8-07).
- **Careers:**
  - Roles as a serif index of whole-row links.
  - The application on ivory, like letterhead, with 56px warm controls.
  - FormSubmit, CAPTCHA, honeypot and email fallback unchanged (T10-10, T10-12).
- **Contact:**
  - A meeting frame: the serif headline on the left, and a founder card on the right with email and booking at equal weight, both above the fold.
  - Topics as a 2×2 grid of tiles (T10-08, T10-09).
- **404:** content aligned to the standard wrap, a CSS horizon, recovery links as tiles, and the dead `recovery_art()` removed (T10-11).
- **Header and footer (every page):**
  - **Header:** Contact becomes a ghost button, nav labels go to 14px, and the wordmark is tracked +0.06em.
  - **Footer:** a compact colophon with a fitted wordmark plus the existing sun, caps-label group headings, one legal line and no slogan (T8-04 to T8-06, T10-01 to T10-06).

#### 7. Unchanged, risks and effort

**Unchanged:**
- **Content and assets:** the approved hero composition, all authentic assets, the four app names, and the team list.
- **Contact and careers:** direct email and booking, and careers delivery.
- **Build:** the static Python build, prefetch-only speculation and the `email_off` wrapper.
- **Behavior and accessibility:** native semantics, focus and dialog behavior.
- **Checks:** `check_site.py` contracts are updated, never loosened.

**Risks:**
- Ivory may glare on phones at night, or read as a light theme. Mitigation: vellum on mobile, rendered review, and falling back to the single Investors ledger.
- The serif reverses the October 13 decision, so it needs founder sign-off from a specimen.
- If the light values are set too timidly, the site slips back to average. Mitigation: test light strengths in rendered screenshots.
- `view()` timelines and view transitions are not supported everywhere yet. Unsupported browsers get instant cuts and static content.
- Every pair of text over light needs an AA recheck.

**Effort:**

| Element | Effort |
|---|---|
| Tokens, light and texture | M |
| Type system and serif | M |
| Header states | S |
| Cover | M |
| Plates and crops | M |
| Native-resolution re-fetch | S |
| Portfolio wall | M |
| Product signature chapters | L |
| Platform diagram | M |
| Investors ledger and showroom | M |
| Founder spreads | S |
| Closing scene and footer | M |
| Motion layer | M |
| View transitions | S |
| Contact, Careers, 404 | M |
| `check_site.py` updates | M |

**Founder-supplied material needed:**
- **Approvals:** the serif specimen, the rewritten copy, any portrait or hero grade, and a reverified business model.
- **Hero:** a higher-resolution master.
- **Product screens:** clean matched UI exports and a populated Sleep Max screen.
- **Founder:** a first-person statement, a signature, a profile link and an editorial portrait set.
- **Team:** roles and portraits.
- **Facts:** verified metrics and dates.
- **Brand and legal:** the vector logo and wordmark decision, and privacy and terms documents.

No claims, metrics, UI or assets are invented here. Byte figures for the new font cuts are estimates; the only measured figure is the 26,292-byte Manrope file at `C:\Users\atatu\Desktop\Projects\Solarity-AI\solarity-ai-project\dist\assets\fonts\manrope-latin-variable.cfa570d7c3ee.woff2`.


### Direction: product-protagonist

#### Direction: "Four Worlds at Sunrise". The products carry the story

#### 1. Concept
The sunrise is the opening shot. After it, each of the four apps gets its own lit stage. The set is dark and warm, a single key light falls from the upper right at the same angle as the hero sun, and the app's own color shows as a rim light. The investor story then runs in three acts: proof (four lit products), vision (the app factory drawn in outline and left unlit), and the founder (a warm close). For an AI self-improvement company, the shipped apps are the only verifiable asset, so they lead and the vision follows behind them.

Solves T1-01, T4-01, T5-01, T8-01 and T6-02. This is the root fix for "average": there is light after the fold, and the four products look like four distinct brands.

#### 2. Typography
- **Display face (needs founder sign-off, because it reverses the October 13 decision to use one family; T3-01).**
  - Recommended: **Instrument Serif Regular** (OFL, one static file) for titles, chapter heads, product names and the one statement per page.
  - Byte cost: an estimated 20–28 KB as a Latin plus Latin Extended-A WOFF2 subset, to be measured after the fontTools subset. The Italic file (about the same size) is optional and used only for a single emphasized word.
  - Font budget: at most 55 KB including Manrope's 26.3 KB. Preload the display file only on routes where it is above the fold.
  - Fallback B costs zero bytes: Manrope at weight 250–300 for display. The founder chooses from a three-frame specimen (home hero, investors opener, a product hero).
- **Manrope stays** for UI, deck and body text: UI at 500–600, deck at 400. Add a metric-matched "Manrope Fallback" (size-adjust plus ascent and descent overrides from font-sources.json), and one for the display face, both using `swap` (T3-12).
- **Scale tokens (T3-02):** title clamp(3.5rem, 2rem + 5vw, 7.5rem), chapter 4–4.75rem, section 2.75–3.25rem, sub 1.75–2rem, deck 1.375–1.5rem (1.15rem on mobile). Body text becomes 17–18px at line-height 1.55 (T3-05).
- **Tracking (T3-03):** serif display −0.01em to 0. Sans tracking follows the token scale and is never negative below 28px. The wordmark gets +0.06em (T10-02).
- **Treatments:**
  - Product pages: the product name becomes the H1 at title scale and the slogan becomes the deck (T5-08).
  - The two-line split heading is kept only for the hero and the closing (T3-04).
  - Labels collapse to two styles: caps and meta (T3-08).
  - Numerals are lining, tabular Manrope (T3-09).
  - `text-wrap: pretty` applies to all body copy (T3-10).
  - Two-thirds of the eyebrows are cut (T3-07).

#### 3. Color, light and texture
- **Warm neutrals (T1-04):** --bg #0f0d0b, --surface #18140f, --raised #221c16, --line #3a3027, --ink #1a140e. Update theme-color to match.
- **Solar ramp (T1-05):**
  - --sun-core #ffcf7a: one focal element per viewport.
  - --gold #e9b56a: active states.
  - --sand #d6bf9a: labels.
  - --bronze #9c7446: non-text decoration only.
- **Light tokens (T1-01, T1-03):**
  - --glow-sun is a core of rgba(255,190,110,.28) fading out over 50% of its radius.
  - --glow-ember is used for the bounce light at the bottom of long pages.
  - A fixed key light at about 85% x, matching the sun.
  - Glows go only behind products, the founder and the primary CTA.
  - Every value is tuned from rendered screenshots at 1440px and 390px.
- **Product worlds (T5-01):** each product gets a set applied through `[data-product]`: `--world` for stages and glows, `--tint` for text-safe accents (AA-checked), and `--rim`.

| | world | tint |
|---|---|---|
| Looks Max | #7a35c9 | #e3c8ff |
| IQ Max | #2a4fd0 | #c3f2ee |
| Sleep Max | #262c78 | #ccd0fb |
| Fitness Max | #ff5a1f | #ffc4a6 |

  Strong hues appear only on large surfaces and in glows. Body text stays ivory. Company gold is reserved for investor and partner actions.
- **Materials:**
  - Retire the cream paper panels and replace them with warm smoked glass: a #1f1913→#120f0c gradient, a 1px top highlight at rgba(255,220,170,.10), and a single --radius-panel of 20px (T1-02, T10-07).
  - Grain is a 2–4 KB tiled noise image at 3–5% on scene layers only, not a fixed overlay.
  - Scenes are separated by feathered tonal bridges of 120–200px instead of hairlines (T8-03).
- **Registers (T6-02):**
  - Evidence is lit, filled and carries `.status`.
  - Vision uses a dashed warm hairline, stays unfilled, carries `.status.vision`, and is never the brightest surface.

#### 4. Motion
All motion follows a written motion contract in DESIGN_SYSTEM.md, enforced by check_site (T9-01). The static page is the complete baseline. Only transform, opacity and clip-path animate. CLS stays at 0.

- **Arrival choreography, CSS only, at most 1.2s (T9-02):**
  1. The hero art settles from scale(1.05) to 1.
  2. The H1 lines rise out of clip masks: 650ms with an 80ms stagger.
  3. The four-icon credits row rises last.
  - The LCP image and H1 never start from opacity 0. Interior pages get a lighter variant (eyebrow and H1 only).
  - Under reduced motion, the page is static.
- **Scroll behavior:**
  - **Reveals:** three types, run on `animation-timeline: view()` inside `@supports` and no-preference (T9-03). Disclaimers are never revealed late.
  - **Sticky product stories (T9-07):** from 1024px wide and at least 760px tall, the product stage is pinned (`position: sticky`, no scroll-jacking) while the chapters scroll past.
    - The authentic screens cross-fade as each chapter enters, using view timelines plus `timeline-scope`, with a fallback IntersectionObserver of about 0.8 KB that sets `data-active`.
    - Fallback, and under reduced motion: each chapter stacks with its own inline screen.
  - **Hero depth:** the artwork alone translates 6–10% on `scroll(root)`, at half amplitude on phones (T9-04).
  - **Progress hairline:** 2px, drawn in --sun-core, on long pages (T9-09).
- **Header state (T2-01, T10-04):** an IntersectionObserver class toggle of about 0.4 KB inside the inlined navigation.js switches the header from transparent over the hero to opaque after it. Register the class in DYNAMIC_CLASSES. Height stays constant.
- **Page-to-page transitions (T9-05):**
  - Cross-document `@view-transition` inside no-preference.
  - The header is a shared element. Each page's icon and hero screen get unique build-time names from APPS (for example `looks-max-icon` and `looks-max-shot`), so a product's icon carries over from the portfolio to its own page.
  - Browsers without support cut instantly.
- **Budget:**
  - New JS at most 1.5 KB minified in total.
  - Inline route CSS grows by at most about 6 KB.
  - At most one ambient loop on the whole site, paused while offscreen.
  - LCP and CLS are measured before and after. If mobile LCP regresses, drop the H1 mask.

#### 5. Imagery
- **Sunrise hero:**
  - 100svh, clamped between 720px and 1080px (T2-02).
  - Warm umber scrims that taper off by 50% of the width, plus local protection behind the copy block (T2-04).
  - The header floats over the sky.
  - A credits row of the four real icons forms the bottom edge.
  - Mobile: the art grows to 560–620px with the headline overlaid on it, and the caption is restyled to meet AA (T2-06).
  - The recognizable scene appears in the hero plus one reprise, on the 404 page. Every other page uses CSS light.
- **App Store screenshots:**
  - Every screen sits on one uniform plate: --radius-panel, a 1px inner highlight, a rim in its product color, and a contact shadow on a product-tinted floor.
  - Build-time crops in optimize_images.py cut each image down to the UI window, so the page's H1 is the only headline. They also trim the baked-in edge hairlines (T4-02, T4-05). Crops are recorded in the manifest, and the originals stay untouched.
  - Device frames and UI are never fabricated, and the images are never recolored.
  - Inline size stays capped at 340px until the native-resolution versions of the same listing images are fetched and confirmed by the founder. After that, hero screens go to 440–520px (T4-03).
  - IQ Max uses detail-screen-4 as its hero, staged in cobalt, with the full poster kept in the gallery (T4-06).
  - The enlarge dialog becomes a full-viewport "screening room" tinted in the product's world (T4-07).
- **Founder:**
  - A 4:5 crop with a lit dark plate, a warm rim light and an edge vignette. No regrade without approval, and the background is never replaced (T7-01).
  - Shown once per route context, not repeated three times.

#### 6. Page by page
1. **Home:**
   - The floating-header hero described above.
   - **Four Worlds wall:** four lit stages side by side with cropped UI windows at 240–280px, each with its authentic icon, category and store links, linking to its product page. It replaces both the app rail and the tab explorer (T5-03, T6-07).
   - A "sunrise diagram" built from the four icons on a horizon, with three dashed vision nodes (T6-04).
   - The founder on a plate, with a statement only once the founder supplies one (T7-02).
   - The shared closing horizon in CSS dawn light, with one primary and one secondary action (T8-02, T8-04).
2. **Apps:**
   - Opens on a lineup of the four official icons at 96–120px, each on its own world glow, doubling as the anchor nav (T5-04).
   - Each product follows as a full-bleed band in its world.
   - Whole cards link to the product page, with store badges as separate links (T5-11).
   - Mobile uses compact cards capped at 55–60svh (T5-12).
3. **Looks Max:**
   - Violet stage.
   - A "scan" signature chapter: the stage stays pinned while crops of the Overall Evaluation and Hair & Beard cards scroll past (T5-02).
4. **IQ Max:**
   - Cobalt stage with a mint rim.
   - A sticky sequence from focus selection to routine, using detail-screen-4 and detail-screen-6.
5. **Sleep Max:**
   - A full-bleed indigo night stage with the store badges placed directly under the H1 (T5-10).
   - A chapter built from Soundscapes crops.
   - The empty-profile frame is removed until the founder supplies a populated screen (T5-06).
6. **Fitness Max:**
   - Ember stage.
   - A "day log" triptych: chat, meal, streak.
   - The Only Fitness disclosure appears once, inside the badge block (T5-15).
   - **All four product pages:**
     - Official App Store and Google Play badges, shown at the same height, replace the gold pills, and the status dot is dropped (T5-05, T5-16).
     - A filmstrip of every claims-cleared screen (T5-07).
     - One closing band in the product's world, plus three sibling cards, each in its own world (T5-14).
7. **Platform:**
   - A sticky split. On the left, the map: the four app icons form a lit sun core, and Build, Operate and Grow are dashed nodes connected by "informs" lines that draw in.
   - On the right, the modules scroll past. The active node gains an outline glow and stays in the vision register (T6-03, T6-05).
   - One partnership CTA in total.
   - Mobile uses a vertical sequence capped at 60svh (T6-09).
8. **Company:**
   - The founder plate as the opening scene.
   - The team as a compact credits block (T7-03).
   - A "story so far" strip of the four icons. Dates appear only when the founder confirms them (T7-04).
   - The principles become a single editorial statement (T6-06).
9. **Investors & Partners:**
   - A showroom opening: four identical frames under a warm overhead spotlight, each with its icon and store links, all inside the first viewport (T4-04).
   - An "At a glance" fact band using verified facts only (T6-01).
   - A two-card Today / Ahead ledger.
   - A one-line page index (T6-08).
   - The booking close carries a small founder portrait (T8-07).
10. **Careers:**
    - A sticky left column with the heading, the email alternative and an honest "What happens next."
    - Warm 56px form controls (T10-10).
    - Role rows become whole-row links (T10-12).
11. **Contact:**
    - A two-column "meeting frame": a founder card, with email and booking at equal weight, both above the fold (T10-08).
    - Topic tiles laid out 2×2 (T10-09).
    - A masked glow, so its edge no longer shows (T1-06).
12. **404:**
    - The single sunrise reprise: a darkened, masked crop under about 600 CSS px, captioned.
    - Content aligned to the standard .wrap edge.
    - Recovery links styled as tiles (T10-11).
- **Chrome across all pages:**
  - Header Contact becomes a ghost button (T10-03).
  - Mobile bar shows only the lockup and a menu icon.
  - Full-height menu with a clip-path reveal (T10-05, T9-08).
  - Compact footer with no second slogan and the wordmark fitted to the wrap (T8-05, T8-06).

#### 7. What stays, risks and effort
**Unchanged:**
- The hero composition and master file.
- All official screenshots and icons; crops only, recorded in the manifest.
- The four app names.
- Direct email and booking; the site still collects no messages.
- Careers delivery through FormSubmit.
- Native semantics, focus behavior and dialog contracts.
- The static Python build.
- Prefetch only, never prerender.

**Risks:**
- AA contrast over colored light.
- `view()` and `timeline-scope` are limited to Chromium-family browsers, so others get the static layout, which is acceptable.
- Brighter stages expose the soft 600px sources until the native-resolution versions arrive.
- Sticky layouts on short laptop screens are guarded by a height query.
- A display face could hurt LCP.
- check_site contracts must change together with the code: the explorer radios, hero preload and token rules.
- The store-badge brand rules have to be followed.

**Effort per element:**

| Effort | Elements |
|---|---|
| S | Header state switch, solar and neutral tokens, store badges, view transitions, founder plate, footer |
| M | Light and world tokens with render tuning, display type and scale, hero frame, lit stage component, crop pipeline, Home wall, Apps index, Investors showroom, closing horizon, reveals and arrival, screening room, Contact, Careers, 404 |
| L | Four signature product chapters with sticky stories; Platform sticky map |

**Needs founder material or sign-off:**
- The display-face choice and changes to the design-system rules.
- Confirmation of native-resolution store assets, or clean UI exports.
- A populated Sleep Max screen.
- A founder statement, signature and editorial portrait.
- Team roles and portraits.
- Verifiable dates and metrics.
- The vector logo.
- A higher-resolution hero master.
- Privacy and terms links.

None of this invents a claim, metric, piece of UI or portrait.
