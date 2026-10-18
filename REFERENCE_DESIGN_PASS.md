# Reference-inspired design pass

October 13, 2026. Baseline: public Site version 19.

The founder authorized implementation of the preceding reference-site audit. The reference informed composition and feedback, while the company source register controlled product facts, people, destinations, and platform maturity. The public audience and production domain configuration are preserved.

## Implementation map

| Approved recommendation | Source implementation |
| --- | --- |
| Product-led hero | `visual_home.py`: two authentic, uncropped promotional images, genuine product links, explicit sample-content caption. |
| Confident headline composition | Homepage, Platform, Company, and Investors use deliberate heading measures and selective native serif contrast. No downloaded font dependency. |
| Earlier mobile product evidence | Homepage source places the compact product stage before the inquiry actions, with a dedicated narrow layout. |
| Large screenshots beside features | `visual_catalog.py`, `visual_products.py`, and `products.css` enlarge genuine evidence while maintaining original proportions and full-image access. |
| Distinct app stories | Looks: assessment and styling suggestions. IQ: focus and exercise selection. Sleep: soundscapes and participation records. Fitness: meal estimates and a sample consistency milestone. |
| Stronger product identities | Existing product accents apply to evidence stages, selected states, and small structural details. |
| Clear portfolio/platform relationship | `company_strategy()` replaces three repeated homepage sections with one labelled conceptual relationship. |
| Distinct Platform opening | `platform_opening()` pairs the company direction with three native Build / Operate / Grow anchor links. |
| Investor evidence near the thesis | `investor_opening()` presents the four authentic product images; the later section explains the thesis and platform boundary rather than duplicating the product list. |
| Varied compositions | Split introductions, a native product explorer, thin-rule sequences, an asymmetric Fitness story, and editorial company sections. |
| Thin-rule feature and partnership lists | Existing semantic lists are refined without adding repetitive card shells. |
| Intentional section spacing | Shared section tokens and maintained domain styles govern spacing. Removed homepage repetition shortens the narrative. |
| Readable company philosophy | Company and strategy copy stays visible immediately and does not depend on scrolling or animation. |
| Credible people presentation | Authentic founder and three member portraits, with intentional monograms for three members without verified photos. No invented roles. |
| Clear principles | Numbered product philosophy beside a concise editorial heading. |
| Route-specific invitations | Home, Apps, Platform, Company, and each app receive a context-specific closing invitation. Existing investor booking and inquiry context remain intact. |
| Surface details | Consistent pill actions, borders, product image frames, focus feedback, restrained accents, and readable secondary text. |
| Footer finish | Refined directory proportions, signature spacing, and small arrow feedback. Complete navigation remains available. |

## Motion and delivery

Motion is limited to feedback and short transitions. Essential content is immediately visible, native scrolling remains, and reduced-motion rules disable animation and transitions. No loading screen, custom cursor, magnetic targets, page curtain, forced horizontal scroll, autoplay, continuous particles, or animated counters were introduced.

The existing native four-product radio selector keeps all panels in the same grid cell so the largest intrinsic panel reserves stable space. Inactive panels remain unavailable for interaction. Images retain dimensions and responsive candidates. The homepage preloads only its primary genuine screenshot with the same candidate list and size hints used by the image.

No new runtime package, third-party script, or web font is required. The maintained seven-file CSS system remains the source of truth. Build output is route-specific inline CSS and conditional gallery/contact scripts.

## Verification boundary

The Sites managed-browser workflow requires `control-browser`, which was unavailable in this session. No preview server or alternative browser-control workflow was used. Static/source review can identify semantic, link, asset, and layout-contract defects; it does not prove rendered layout, keyboard behavior in a real browser, accessibility scores, or current Lighthouse scores.

Fresh build, structural audit, automated behavior test results, and source-byte comparisons are recorded after the completed implementation below.

### Completed checks

- `python3 build_site.py`: generated 10 content pages and the custom 404.
- `python3 check_site.py`: 11 pages, 332 internal links/fragments, and 324 local asset references; zero errors or warnings.
- `python3 -m unittest test_optimize_styles.py test_site_urls.py`: 19 tests passed.
- `node --test test-navigation.cjs test-contact.cjs test-gallery.cjs`: 32 tests passed.
- `git diff --check`: passed.
- Independent source geometry review covered 360, 390, 768, 1024, 1440px and breakpoint boundaries. No blocking source defect was identified. This does not replace rendered visual testing.
- Native radio relationships, image dimensions, exact primary-image preload matching, module anchors, inquiry context, sample-content captions, and the selected roster were checked.

JavaScript source size remains unchanged on every route. Homepage JavaScript is 2,798 bytes. The redesigned homepage HTML including inline CSS increases from 14,492 to 15,601 gzip-compressed source bytes. These are build-byte measurements, not actual network transfer or performance scores. Full per-route comparisons: `research-assets/reference-pass-byte-comparison.json`.

## Content dependencies

- Verified portraits remain missing for Eren Öz, Batuhan Yücetürk, and Melik Kaplan.
- Current approved public role descriptions remain missing for the six selected team members.
- Applicable corporate privacy and terms documents remain unsupplied. The existing honest contact-experience explanation is preserved.
- Platform integrations, external commercial availability, operational gains, and fundraising details remain unverified and are not represented as established facts.

Future product facts and destinations belong in `APPS` in `build_site.py`; screenshot narratives belong in `product_story.py`; team records belong in `visual_team.py`. Update `CONTENT_REGISTER.md` with evidence when changing public claims.
