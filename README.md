# Solarity AI corporate site

Investor and strategic partner website, created October 12, 2026.

## Maintain content

- **Shared content and product records:** edit `build_site.py` for shared page content, company contact destinations and the `APPS` records.
  - `saas_products.py` holds the three web apps (Engineering Max, Management Max, Marketing Max).
  - `visual_saas.py` renders them on Home, Apps, Platform and Investors.
- **Where the markup lives:** in Jinja templates under `templates/`, one folder per module (`templates/visual_contact/page.html.j2`, `templates/build_site/shell.html.j2` and so on). Each module keeps the data and logic and calls `templating.render()`. To find any text, run `git grep -n "the words" templates/`. The repository wiki's "Templates" page has the escaping and whitespace rules.
- **`seo.py`:** search and AI answer-engine metadata (schema.org, robots.txt, sitemap dates, `llms.txt`, IndexNow).
- **Product fields:** name, purpose, features, store URLs, screenshot and contextual note. Store badges render only when a verified store destination is configured.
- **Styles:** maintain them only in the eight files under `design/system/`. `DESIGN_SYSTEM.md` defines their responsibilities, tokens and verification limits.
  - `style_sources` in `build_site.py` is authoritative.
  - The build writes the combined `design/presentation.css` (used for hashing), then filters and inlines CSS per route. Do not edit generated styles.
  - Shared control states live in `foundation.css`, navigation and footer in `chrome.css`, and alternate accessibility modes in `accessibility.css`.
  - Page composition belongs in `home.css`, `products.css`, `company.css`, `contact.css` or `careers.css`.
- **Interactions:** maintain them in `scripts/navigation.js`, `scripts/gallery.js`, `scripts/contact.js`, `scripts/careers.js` and `scripts/copy.js`.
  - Navigation is inlined in the head before styles, so the mobile layout is stable before first paint.
  - The other scripts are fingerprinted external files, loaded only on routes that need them.
  - Every page also carries prefetch-only speculation rules from `performance_build.py`.
- **Images:** `optimize_images.py` creates uncropped responsive variants with content-hashed filenames. Edit the source images, then run the build; never edit generated optimized assets. Screenshot enlargement links keep the original full-size image.
- **Assets:** keep build-only masters in `source-assets/`. The build publishes a file to `dist/assets/` once a page references it (see CLAUDE.md). Record provenance before publishing.
- **Build and checks:** run `python build_site.py` to regenerate `dist/`, then `python check_site.py`, `python -m unittest test_optimize_styles.py test_site_urls.py test_seo.py` and `node --test test-navigation.cjs test-contact.cjs test-gallery.cjs test-careers.cjs test-copy.cjs`.
- **URLs:** `site_urls.py` normalizes page anchors, canonical and Open Graph URLs, and sitemap entries to the host's final trailing-slash URLs. Keep route keys and `data-page` attributes unchanged when editing components.

## Routes

Home, Apps, Looks Max, IQ Max, Sleep Max, Fitness Max, Platform, Company, Investors & Partners, Careers, Contact, and an error page.

## Contact behavior

- **Contact page:** links open the visitor's email app, addressed to `ata.turhan@solarityai.com` with a subject chosen by topic, or open the founder's Google Calendar booking page. The site does not collect or submit contact messages and never claims a message was delivered. A copy button copies the address.
- **Careers:** the form posts to FormSubmit, with direct email as a fallback (see `CAREERS_DELIVERY.md`).
- **Analytics:** the Cloudflare zone injects its cookieless Web Analytics beacon; the site itself adds none.

## Access and publication

- **Origin:** https://solarityai.com, served by Cloudflare Pages from the `main` branch. The earlier GPT Sites origin was https://solarity-company.the-ata-turhan.chatgpt.site.
- **Public access:** the founder authorized public access on October 12, 2026. Future deployments must preserve it unless the founder changes that instruction.
- **Indexing:** content pages allow indexing, and the 404 page asks not to be indexed.
- **robots.txt:** welcomes search engines and AI assistants, including AI crawlers it blocked before October 19, 2026 (see `CONTENT_REGISTER.md`), and advertises the sitemap. DNS is not managed by this project.

## Outstanding items

- **Fitness Max** is listed in the App Store and Google Play as Only Fitness. Keep that naming disclosure beside its product and store actions.
- **The three web apps** are real products with their own statuses (`saas_products.py`). Their mobile versions are a founder-stated plan and stay labeled as planned. No customers, usage or revenue are claimed.
- **Motivation Max, Productivity Max and Hair Max** are omitted pending sufficient public-facing details.
- **No privacy policy or terms page.** The site has none. The careers form links to FormSubmit's privacy policy. Obtain the company's own policies; none has been invented.
- **Team.** The company sun and the founder portrait come from the earlier solarityai.com (`research-assets/brand-evidence.json`). The founder-selected six-member roster lives in `visual_team.py`, with portrait evidence in `research-assets/team-evidence.json`. Add no other people without approval.
- **Verification.**
  - Browser, accessibility and Lighthouse checks are recorded in `UX_REFINEMENTS.md`, `PRODUCTION_AUDIT.md` and `DESIGN_SYSTEM.md`.
  - Cloudflare Pages applies `dist/_headers`.
  - After a header change, the zone's edge cache keeps serving older static files with their old headers until a purge (Caching → Configuration → Purge Everything).

## Asset note

- **Hero:** the approved natural-sunrise artwork. The master is `source-assets/solar-ascent.webp`, upscaled from `research-assets/solar-ascent-approved.png`, and `research-assets/solar-ascent-artwork.json` records it. It is conceptual brand artwork and does not depict the founder, company facilities or product UI.
- **Earlier artwork** remains under `source-assets/retired/` and is never republished.
- **Product visuals and icons** are authentic store assets; their sources are in `research-assets/downloaded-assets.json`.

## Historical implementation log

Entries below describe earlier versions. `DESIGN_SYSTEM.md` supersedes their stylesheet references and visual instructions. Current product, evidence, and access rules above remain authoritative.

## UI refinement, October 12, 2026

1. Homepage portfolio cards show authentic app screenshots.
2. Mobile product cards use a full-width layout and larger text.
3. Mobile hero is tighter and includes direct store-listed app discovery links.
4. Product availability and product vision labels follow one consistent system.
5. Persistent header keeps navigation and contact accessible.
6. Upright app screenshots include an accessible native enlargement dialog and direct-image fallback.
7. Sticky section links make the portfolio and platform easier to scan.
8. Investor overview separates store-listed products, platform vision and collaboration paths.
9. Visible inquiry choices adapt contact headings and preserve relevant product context.
10. Touch targets, body text, focus treatment and link arrows are more consistent.

Validation: static audit checks routes, anchors, asset references, metadata, form labels and ARIA ID references. Node tests exercise email encoding, query context and injection resistance. Actual browser interaction, measured responsive layout and Lighthouse testing remain unverified.

## UX refinement, October 12, 2026

1. Explicit prepare, review, and email handoff with a full draft preview.
2. Less form effort: name and message required, optional reply email and organization grouped in a disclosure.
3. Inquiry-specific message guidance and product/topic suggestions.
4. In-memory category topic preservation with related product context carried between product and partner inquiries.
5. Persistent field errors and a linked error summary with accessible focus recovery.
6. Readable copy fallback, manual text selection, truthful handoff states and long-draft guidance.
7. Four-goal app chooser before the large portfolio screenshots.
8. Sibling-app navigation and contextual return to the portfolio.
9. No-JavaScript mobile navigation, semantic breadcrumbs and a focusable main target.
10. Evidence-grounded investor FAQs and explicit 404 recovery paths.

Drafts are never saved in local/session storage or sent to a site backend. Editing inputs invalidates the displayed review so a stale draft cannot be handed off as current. Clipboard feedback ignores stale asynchronous completions. The available tests cover pure inquiry logic, static integration contracts and JavaScript syntax. Browser interaction, measured layouts and performance remain unverified.

## Second UI refinement, October 12, 2026

1. Meaningful hero art representing the four portfolio ambitions and shared platform strategy.
2. Dedicated split hero composition with HTML labels and a mobile stack that preserves the full artwork.
3. Consistent app-specific accents across product headings, feature symbols, notes and actions.
4. Purpose-specific SVG feature symbols and clearer heading hierarchy.
5. Conceptual Build, Operate, Grow platform sequence with a visual rail into module details.
6. Editorial founder identity card with verified role/location and no invented portrait.
7. Distinct visual treatment for store-listed product evidence and platform vision.
8. Authentic app icons across goal selection and related-app navigation.
9. Grouped inquiry composer and clearly differentiated paper-style draft preview.
10. Separate investor and partner invitation panels replacing repeated centered closing blocks.

This earlier symbolic hero was superseded by the third UI refinement below. Do not draw new evidence or product capability claims from conceptual imagery.

## Third UI refinement, October 12, 2026

1. Cinematic hero combines the original architectural atmosphere with authentic Looks Max, IQ Max and Sleep Max screenshots, clear product purposes and a separate app factory vision link.
2. A consistent charcoal palette replaces mixed olive/gray surfaces, including screenshot dialogs.
3. Fluid secondary-page headings, balanced line lengths and tighter page openings improve hierarchy.
4. Shared navigation gains clear active states, a persistent Contact action and an accessible mobile toggle order.
5. Shared product accent tokens keep product cards, icons, headings and discovery links consistent.
6. Portfolio rows stack at tablet widths, with proportionate, uncropped screenshots and an enlargement toolbar outside the image.
7. A single decorative Voice Max waveform appears consistently across its product and discovery surfaces.
8. Investor product evidence includes three authentic app icons, distinct names and direct product links.
9. Direct email and booking have distinct contact cards with clear destinations.
10. A complete footer directory exposes every core app, company page and conversation path.

This earlier backdrop composition was superseded by the fourth UI refinement below. Actual app imagery remains separate and unchanged. Voice Max remains a product vision without a launch badge.

## Fourth UI refinement, October 12, 2026

1. A human-centered cinematic hero restores the original architectural style and gives the scene a clear subject and direction.
2. Real app evidence moves into a distinct rail below the hero, keeping the headline and image uncluttered.
3. The company focus strip explicitly names consumer apps and the app factory vision, with concise explanations.
4. The homepage portfolio becomes an editorial gallery of authentic screens, with a separate Voice Max vision entry and readable stacked mobile layouts.
5. The Apps page removes its repeated chooser block, retaining a single native anchor navigation and substantive product stories.
6. The platform opening replaces large repeated cards and duplicate navigation with a compact Build, Operate, Grow index.
7. The investor opening consolidates product evidence and platform direction into one editorial overview, removing the repeated lower evidence band.
8. Company imagery and founder content gain better tablet proportions; the image and narrative stack at 850px.
9. Shared closing invitations use one concise horizontal band and two clear actions instead of repeated multi-card endings.
10. Contact uses a shorter introduction, compact direct-contact links and clear numbered Topic, Introduction and Message groups.

The hero uses 768, 1200 and 1672px WebP variants; the largest is 116,324 bytes. Product headings also use fluid type, and remaining olive recovery/identity surfaces are neutralized. Contact logic, inquiry context and source facts were preserved. Access was owner-private at this historical refinement; the later public-access authorization below supersedes it. The static audit checks 11 pages, route and asset references, metadata, labels, ARIA references, navigation ordering, product identity and screenshot fallbacks. Contact logic and JavaScript syntax pass separately. Browser rendering, viewport overflow and Lighthouse scores remain unverified because the supported browser workflow is unavailable.

## Performance optimization, October 12, 2026

The supplied PageSpeed screenshots display the ChatGPT sign-in screen, not the Solarity AI homepage. Their mobile scores (89/100/96/82) and desktop scores (100/100/96/82) therefore do not establish scores for this site's application. That initial optimization preserved owner-private access and crawler exclusions under the original brief. The founder subsequently authorized public access for all GPT Sites on October 12, 2026, superseding that restriction.

Implemented improvements:

- Inline, route-specific CSS removes selectors requiring absent classes while preserving source order, declarations, functional pseudo selectors, animation definitions and dynamic states. The homepage sends about 39.4 KB of CSS instead of 161.9 KB, with no separate blocking stylesheet request.
- Homepage JavaScript initially dropped from 20,084 to 2,335 bytes. The subsequent layout-shift fix inlines navigation with a small DOM-readiness wrapper. Gallery code is delivered only to screenshot pages; contact code only to Contact. External scripts use content-hashed filenames; the inline navigation carries a source hash for build verification.
- Hero AVIF variants save about 29 to 31% over WebP and retain WebP fallbacks. The preload and image use matching responsive candidates. Screenshots have 240/400/600px variants and app icons 48/96/144px variants.
- Opening product screenshots use eager/high-priority loading. Other lower-page screenshots remain lazy loaded. Image dimensions and full-size native gallery links are preserved.
- Long-lived public caching is configured only for content-hashed image/runtime folders following the public-access authorization. Provider header behavior has not been measured through HTTP.

Reports: `research-assets/performance-baseline.json`, `research-assets/performance-build.json`, and `research-assets/image-optimization.json`. Byte counts are build measurements, not Lighthouse scores or measured HTTP transfers. Validation includes 12 optimizer safety tests, 9 contact logic tests, JavaScript syntax, route/asset/metadata checks and comparison of all page text and anchor destinations against the prior deployed source. Browser layout and actual PageSpeed results for the application remain unverified.

## Public access and indexing, October 12, 2026

The founder instructed: "make all my gpt sites always public, all the time, especially this one, nothing should be private". Public access is the current instruction for this site and replaces the former private-access preservation rule. Valid pages now use `index,follow`, `robots.txt` permits crawling and points to the deployment-origin sitemap, and the global noindex response directive has been removed. The error document keeps `noindex,follow` metadata and path-specific header rules because an error page should not appear as a search result; it is still publicly accessible. Content-hashed images and scripts use public immutable cache directives.

The static audit verifies page indexing rules, sitemap coverage without the 404 page, crawler access, deployment-origin URLs and cache/header scope. Search indexing is permitted, not guaranteed. Native Sites settings confirmed public access for all seven owned Sites, and an unauthenticated HTTP request returned 200 for the Solarity homepage without a sign-in wall. The public PageSpeed API request returned HTTP 429 with a daily-quota-exceeded response, so no new Lighthouse scores were obtained. The previously deployed global X-Robots-Tag was absent from the HTTP response despite being present in its source _headers file; provider application of the generated header rules remains unverified. Recheck crawler metadata and performance after deploying these source changes.

## Mobile layout stability, October 12, 2026

The founder supplied a public mobile PageSpeed report captured at 14:14 CDT: performance 88, accessibility 100, best practices 100, SEO 100, FCP 0.8s, LCP 0.9s, TBT 0ms, CLS 0.237 and Speed Index 0.8s. The founder also reported desktop scores of 100. These are user-supplied pre-fix results, not a fresh automated measurement from this checkout.

The mobile header initially displayed its expanded no-JavaScript fallback, then collapsed when the deferred navigation file arrived. Below 850px this changed the height above the hero after painting; desktop did not use those fallback rules. The complete navigation code now executes inline in the head before styles and body parsing. It selects the compact mobile layout immediately and attaches interactions after the DOM is ready, without a separate navigation download. JavaScript-disabled visitors retain the visible fallback navigation. No image, content, or desktop design changes were made.

Validation checks every page for the exact inline source and synchronous pre-style execution, and rejects external navigation downloads. Eleven Node navigation tests cover startup with no body, DOM readiness, menu interactions, focus behavior, breakpoint transitions, late execution and missing controls. Static route checks and existing optimizer/contact tests also pass. These checks establish the delivery and interaction contracts, not a measured CLS or Lighthouse score. A fresh mobile PageSpeed run is required to confirm the resulting score; the supported managed browser remains unavailable.

## Sixth UI refinement, October 12, 2026

The founder confirmed all PageSpeed scores reached 100 after the navigation startup correction. The following refinement preserves that startup sequence and all existing imagery. It adds no JavaScript, fonts, image requests or external homepage scripts.

1. Consistent button corners, focus and pressed states; stable hover feedback without moving whole buttons or reflowing investor conversation rows.
2. Stronger active-page navigation treatment and a clear open-menu state, preserving header dimensions.
3. A compact product identity row and clearer breadcrumbs, with the authentic 64px icons retained.
4. Product-colored portfolio trim, readable availability capsules and distinct product-vision borders.
5. Balanced store actions with equal tap areas and a single column on narrow phones.
6. Clearer screenshot enlargement controls, provenance captions and product context notes, preserving image dimensions and stages.
7. Compact mobile feature cards with an icon beside the complete text instead of a tall stacked composition.
8. Visible platform anchor destinations and aligned commercial-comparison actions, keeping evidence distinct from vision.
9. Clear FAQ open, hover and focus states with a contained plus control and readable answer widths.
10. Persistent contact topic selection markers, clearer optional/error states, and stronger email-draft review hierarchy.

Verification: 11 generated pages, 324 internal links/fragments and 165 local asset references passed with no errors or warnings. All 32 existing navigation, contact and CSS optimizer tests passed. An independent source review found no material cascade or mobile wrapping issue. All 11 pages retain the same visible copy, anchor destinations, image attributes and external script URLs. Homepage CSS increases from 39,420 to 41,257 bytes; estimated gzip HTML increases from 13,810 to 14,180 bytes. These are build-time byte counts, not measured transfer sizes. The new UI has not been measured with Lighthouse or viewed in a live browser because the supported managed browser is unavailable; the previously reported 100 scores must not be presented as new measurements.

## Premium motion pass, October 12, 2026

`design/motion.css` is the final shared style source. It adds a single two-second solar-light accent over the existing hero artwork, button sheen, directional arrow feedback, gentle product-screen lift, platform edge lighting, footer link underlines, a hamburger-to-close morph, mobile menu entrance, native screenshot-dialog entrance, FAQ answer entrance, and contact selection/draft transitions.

Motion uses opacity and transforms, with no new JavaScript, fonts, images, network requests, scroll listeners, or hidden-content reveal system. Pointer effects require a fine pointer with hover support and have keyboard focus equivalents. The reduced-motion preference disables animation and transitions; menu state and focus indicators remain clear. Initial text and hero-image visibility, image dimensions, mobile navigation's pre-paint initialization, contact semantics, and all content/links remain unchanged. Autoplay decoration ends after two seconds; no continuous loops or persistent `will-change` layers are added.

Validation: 11 routes, 324 internal links/fragments and 165 assets pass static validation. All 32 existing navigation/contact/optimizer tests pass. Comparing generated HTML before and after confirms every non-style element, text, attribute and script is unchanged. Independent source review caught and corrected an arrow display override that would have affected the tablet product rail. The homepage still contains 2,798 bytes of navigation JavaScript and no external JavaScript. The CSS addition is under 1 KB of estimated compressed homepage HTML. These are build-time estimates. Live browser animation checks and fresh Lighthouse scores are unavailable because the supported managed browser is not exposed. The user's previously confirmed 100 scores are historical, not a measurement of this deployment.

## Full-site QA, October 12, 2026

Confirmed application defects fixed:

1. Contact topics ending at an emoji boundary could create malformed UTF-16 and crash email draft review. Bounded Unicode text and defensive URL encoding now preserve valid pairs and handle malformed input safely.
2. Contact field and draft control borders had insufficient contrast. Updated boundaries exceed 3:1 against adjacent surfaces while retaining focus, error, and disabled states.
3. A decorative Voice Max visual used an H3 directly after the page H1. It is now a styled paragraph with equivalent typography.
4. Internal links and canonical/Open Graph/sitemap URLs used paths that the host redirects. They now use the final slash URLs, preserving inquiry queries and fragments.

The static audit additionally checks skipped heading levels, exact canonical/Open Graph URLs, redirect-free internal page anchors, browser referrer policy, and every current stylesheet source. Browser referrer policy is explicit in HTML because custom response headers are not applied by the host.

Verification: all 11 pages pass static checks covering 324 internal links/fragments and 165 local asset references. All 51 tests pass: 12 contact, 11 navigation, 9 gallery, 12 CSS optimizer and 7 public-URL cases. Gallery tests cover focus return, close behavior, modified clicks, fallback paths, backdrop clicks, and cross-origin rejection in a Node event harness. Independent before/after review of all 353 anchors confirms only intended page-URL changes. All image attributes, initial navigation behavior, product facts, and destination query/fragment values are preserved.

Live HTTP audit before publication found all 11 existing page artifacts public and available, all 6 store destinations and the founder booking URL responding 200 with the expected titles, and an unknown route returning 404 with the custom recovery page. Robots, sitemap, social artwork, favicon, and sampled optimized image/runtime assets were available. The standalone `/404` artifact responds 200 with noindex metadata; actual missing routes return 404.

Performance guardrails: homepage JavaScript remains 2,798 bytes with no external script. Estimated gzip HTML changes from 15,106 to 15,128 bytes. Only the contact script grows, by 398 source bytes for Unicode handling. Responsive CSS was reviewed at the 360/390/768/1024/1440 breakpoint contexts, but no browser layout, screen-reader, or Lighthouse run was available. Do not describe these checks as visual or measured performance certification.

## Thirty UI refinements, October 12, 2026

See `UI_REFINEMENTS.md` for the complete 30-change checklist and verification scope. The pass covers six shared/home refinements, ten portfolio/product refinements, eight company/platform/investor refinements, and six contact refinements. It adds no runtime JavaScript, fonts, or raster artwork. Current routing, factual copy, inquiry behavior, native interactions, existing image sizing/loading, and the pre-paint navigation fix remain intact. The added catalog-index images reuse existing optimized icons with explicit dimensions. Four compact, route-filtered finishing stylesheets contain the new presentation rules.

## Thirty design improvements, October 12, 2026

See `DESIGN_REFINEMENTS.md` for the next 30 changes and verification scope. This pass emphasizes editorial page composition, larger authentic product evidence, clearer strategy presentation, and a roomier contact composer. Eight shared/home changes, eight product changes, eight strategy changes, and six contact changes are implemented in four route-filtered `*-design.css` sources. No fonts, raster assets, dependencies, or runtime JavaScript are added. Image `sizes` declarations track the enlarged home screenshots and panoramic company artwork. All destinations, headings, and runtime script bytes are preserved. Browser rendering and fresh PageSpeed measurements remain unavailable.

## Thirty further design improvements, October 12, 2026

See `DESIGN_DETAILS.md` for this additional 30-change checklist and verification scope: eight shared/adaptive improvements, eight product improvements, eight strategy improvements, and six contact improvements. Four route-filtered `*-details.css` files refine reading hierarchy, mobile wayfinding, authentic product presentation, inquiry controls, forced-color support, and print layout. Keep `adaptive-details.css` last for alternate-view overrides. The existing hero, product facts, destinations, image attributes, native controls, and runtime scripts are preserved. Static validation and all 51 existing tests pass. Independent source review found and resolved autofill text-color and dialog scroll-lock issues in print styles. No new browser-rendering or PageSpeed claims are made.

### Fitness Max portfolio replacement, October 12, 2026

The current four-app portfolio is Looks Max, IQ Max, Sleep Max, and Fitness Max. Fitness Max replaces Voice Max, with verified Apple and Google Play links, authentic store icon and promotional screenshot, and proportionate fitness/nutrition copy. The store name, Only Fitness, is disclosed on discovery, detail and investor surfaces. Earlier references to Voice Max in this README and revision checklists document superseded versions.

Maintain product facts, names, availability and store URLs in `build_site.py` (`APPS`), source evidence in `CONTENT_REGISTER.md`, and screenshot/icon sources in `research-assets/downloaded-assets.json`. `design/fitness-portfolio.css` adapts the store-listed gallery to four entries. No proposed reference-site redesign was implemented in this change.

Verification for this replacement: 11-page static audit passed with 325 internal links/fragments and 228 local asset references; 19 Python tests and 32 Node tests passed. Fitness store URLs, visible store-name disclosure, image dimensions and removal of retired Voice Max references were checked in generated output. The opening navigation JavaScript remains 2,798 bytes. Browser rendering, measured layout and fresh PageSpeed scores were not tested in this change.

## Reference-informed implementation, October 13, 2026

See `REFERENCE_IMPLEMENTATION.md` for the approved changes, retained evidence boundaries and validation results. The historical review remains in `REFERENCE_SITE_REVIEW.md`. Maintain app records in `build_site.py`, supplementary stories in `product_story.py`, and company/investor story structure in `visual_company_upgrade.py`. The homepage explorer is native HTML/CSS and adds no JavaScript.

## Selected team, October 13, 2026

`visual_team.py` holds exactly the six founder-selected additional members. `design/team.css` presents responsive static cards with three authentic official portraits and three typographic monograms. Keep unverified roles and biographies absent. Only update the portrait map when the identity is established, and record provenance in `research-assets/team-evidence.json`. The existing Ata Turhan founder profile is separate.


## Consolidated design system, October 13, 2026

All 11 routes now use seven maintained stylesheet sources instead of 34 stacked legacy files. The refactor includes distinct page compositions, an intrinsic-height product explorer, stronger founder/team presentation, a simpler investor close, and refined contact/recovery states. See `DESIGN_SYSTEM.md` for the complete audit, current maintenance rules, browser-support references, and verification scope. `research-assets/design-system-byte-comparison.json` records artifact sizes against deployed version 18. Runtime JavaScript remains unchanged.
# Latest reference-inspired refinement

The October 13 reference-inspired update adds the authentic product hero, distinct app evidence layouts, consolidated company strategy, new Platform and Investor openings, refined team presentation, and restrained feedback. See `REFERENCE_DESIGN_PASS.md` for the complete implementation map, actual verification results, and remaining content dependencies. This pass preserves public access, the Sites origin, current product facts, and existing contact functionality. Browser QA and fresh Lighthouse scores were unavailable; 51 automated tests and all static route/link/asset checks passed.

## Careers page, October 13, 2026

`/careers/` adapts the company's published careers page to the maintained design system. It contains three roles, the original work-culture themes, the linked job posters, an accessible application form, and a direct recruiting-email alternative. Careers is discoverable through the header, footer, Company introduction, and sitemap.

Maintain roles, job-poster URL, copy, and native form fields in `visual_careers.py`; presentation in `design/system/careers.css`; progressive validation and role selection in `scripts/careers.js`. Changes to role slugs and work types must update the markup and JS allowlists together. The careers script is loaded only on this route; the page adds no images, fonts, or dependencies.

The form uses native FormSubmit POST and CAPTCHA. The founder-selected destination is `careers@solarityai.com`, including the disclosure and recruiting email alternatives. It discloses the third-party handoff and leaves confirmation to the provider. No application data is stored in the browser or placed in URLs, and no local success query is accepted as delivery evidence. No test application was sent; receiver activation and delivery remain unverified. The recipient may need to activate this new address with FormSubmit.

Verification: static checks passed across 12 pages, 383 internal links/fragments, and 332 local asset references, with no errors or warnings. All 59 automated tests passed: 19 Python and 40 Node, including eight new application-validation cases. Independent source review covered the 360, 390, 768, 1024, and 1440 pixel layouts and navigation breakpoint; it found and resolved minimum-name-length and malformed-URL mismatches. This was source geometry review, not rendered browser testing. Browser QA, live submission, and fresh Lighthouse measurements were unavailable or intentionally not performed.

The founder requested approval before installing a proposed new hero. The proposal was generated and displayed in the conversation, but the current homepage hero source and assets are unchanged. Publication of Careers does not approve or install the proposal.

## Approved natural-sunrise hero, October 13, 2026

The founder subsequently approved the corrected sunrise artwork and requested installation. The homepage now displays the approved scene of a person ascending toward a natural sun in Earth's atmosphere. `visual_home.py` and `design/system/home.css` own its composition. The desktop hero overlays copy on the dark left; tablet and mobile stack the copy above unobstructed art. A reserved 4:3 mobile image viewport uses an 82% horizontal focal position to retain the person and sun. The four-app evidence rail and authentic product explorer remain directly below the hero.

Maintain the exact approved source in `research-assets/solar-ascent-approved.png` and provenance in `research-assets/solar-ascent-artwork.json`. The existing image pipeline generates five widths in AVIF and WebP, with content-addressed filenames, matching responsive preload, high priority, and explicit intrinsic dimensions. The homepage social image also uses the approved artwork. No new runtime script, font, dependency, or animation was added.

Verification: all 59 existing automated tests pass, and the 12-page static audit reports no errors or warnings across 381 internal links/fragments and 335 asset references. Source geometry was reviewed at 360, 390, 768, 1024, and 1440 pixels. This is not rendered-browser QA; browser rendering and fresh Lighthouse measurements remain unavailable. Careers retains `careers@solarityai.com` and its existing verification flow.


## Cinematic design refinement, October 13, 2026

The current implementation and all 24 audit dispositions are documented in `CINEMATIC_REFINEMENT.md`. This coordinated pass replaces the previous route compositions and direct-contact composer; earlier sections above describe historical versions. Contact now uses native email and booking. Careers retains the provider-confirmed native POST flow, accepts general email addresses, and makes LinkedIn/portfolio optional. The exact approved solar hero and verified product records are preserved.

The generated output uses eight maintained stylesheet sources, one compact self-hosted font, route-specific scripts, responsive image variants, and no animation library. Browser/PageSpeed scores and careers inbox delivery were not reverified.
