# Solarity AI: 30 design improvements

Implemented October 12, 2026. This pass prioritizes page composition, product evidence, reading hierarchy, and a more coherent visual identity. It preserves the current hero artwork and builds on the earlier checklist in `UI_REFINEMENTS.md`.

| # | Area | Implemented improvement | Design purpose |
|---|---|---|---|
| 1 | Shared header | Flat desktop navigation with one active baseline marker and a separated Contact action | Give the content and primary action clearer prominence. |
| 2 | Corporate introductions | Split title and supporting-copy columns on Company and Investors & Partners | Make the opening proposition and next actions easier to read together. |
| 3 | Homepage product lines | Paired editorial statements with numbered margin rules | Explain consumer apps and the app factory vision as two related directions. |
| 4 | Homepage platform | One aligned module register replaces staggered module cards | Present Engineering, Management, and Marketing as equal focus areas. |
| 5 | Homepage thesis | Large statement beside a distinct reading column | Give the strategic rationale its own composition and comfortable measure. |
| 6 | Homepage founder | Typographic byline and signature treatment | Emphasize the real founder without implying an authentic portrait. |
| 7 | Shared invitation | Warm ivory conclusion with dark investor action and outlined partnership action | Create a clear visual endpoint and deliberate conversion hierarchy. |
| 8 | Shared footer | Larger wordmark and aligned company sign-off | Balance the site directory with a stronger brand conclusion. |
| 9 | Homepage portfolio | Unified editorial gallery with shared rules | Reduce repeated box framing around the three store-listed products. |
| 10 | Homepage evidence | Larger, consistently scaled authentic screenshots | Make product evidence more legible without cropping the screens. |
| 11 | Homepage Voice Max | Distinct, quieter product-vision ribbon | Keep the unverified release state separate from the store-listed apps. |
| 12 | Portfolio introduction | Headline and supporting explanation in an editorial composition | Give the portfolio a more considered opening. |
| 13 | Portfolio stories | Full-width product mastheads above the copy and imagery | Make each app story distinct and easy to locate. |
| 14 | Product introductions | Compact identity band and rebalanced hero columns | Put app identity, purpose, and installation actions in a clear hierarchy. |
| 15 | Product screenshots | Product-labeled evidence sheets with restrained accent borders | Identify real App Store imagery while preserving native enlargement controls. |
| 16 | Voice Max concept | A waveform study with explicit concept labeling | Communicate the direction without resembling a shipped application screen. |
| 17 | Platform introduction | Editorial lead with a separated action column | Give the platform vision and partnership invitation room to breathe. |
| 18 | Platform index | One ruled three-part spread | Unify Build, Operate, and Grow without implying deployed integration. |
| 19 | Platform modules | Large margin numerals and selected-section treatment | Make each detailed brief and anchor destination easy to recognize. |
| 20 | Platform rationale | Two-part essay beside its introduction | Explain the relationship to consumer products with less repeated card framing. |
| 21 | Company imagery | Panoramic artwork above a separate editorial caption band | Give the brand image space while keeping all explanatory text readable. |
| 22 | Founder profile | Typographic identity sheet with separate role and location areas | Make the verified founder information the focal point. |
| 23 | Investor thesis | Margin label, prominent statement, and offset explanation | Create a stronger strategic reading sequence. |
| 24 | Commercial direction | A continuous evidence-versus-vision spread | Make current product evidence and platform ambition easier to compare. |
| 25 | Contact composition | Wider composer beside a quieter consultation column | Prioritize the visitor's working area. |
| 26 | Contact introduction | Unified composer masthead with truthful email handoff guidance | Explain the process before visitors fill out the form. |
| 27 | Form typography | Clearer field labels, requirement qualifiers, and spacing | Make long-form reading and completion less demanding. |
| 28 | Correction states | Coordinated error summary and inline correction language | Help visitors find and resolve invalid fields. |
| 29 | Draft review | Full-width paper-style review with less nested padding | Give email content more usable space, especially on phones. |
| 30 | Contact conclusion | Separate action, feedback, and data-handling areas | Distinguish preparing a draft from sending it through an email app. |

## Verification scope

All 11 generated pages pass the static audit, covering 324 internal links and fragments and 177 local asset references. All 51 existing automated tests pass across navigation, gallery, contact, CSS optimization, and URL handling.

Before/after comparison checks all 353 anchor attribute sets, heading tags and text, external script URLs, and inline script bytes. These remain unchanged. Image counts and attributes remain unchanged except for the intentional responsive `sizes` corrections for the enlarged homepage screenshots and panoramic company artwork. No new images, fonts, dependencies, or runtime JavaScript are introduced.

Independent source review checks the cascade, responsive rules, readable colors, focus states, and reduced-motion behavior. It identified and corrected overlapping active-navigation markers and an older selector overriding the new portfolio introduction. The company image's responsive sizing also follows the actual 560px and 1150px gutter breakpoints.

The current hero, synchronous navigation initialization, native gallery fallback, and truthful email-only inquiry behavior remain intact. Homepage navigation is still 2,798 bytes with no external JavaScript. Byte-size comparisons are build estimates, not measured network transfers or Lighthouse scores.

Estimated compressed homepage HTML is 18,329 bytes, up from 16,127 bytes. The increase is 2,202 bytes. This includes the route-filtered design changes and does not add a blocking stylesheet request.

Live browser rendering, measured responsive overflow, screen-reader behavior, and fresh PageSpeed scores remain unverified because the supported managed browser is unavailable. Source checks do not establish pixel-perfect rendering or guarantee a score.

## Maintenance

The presentation rules live in `design/shared-design.css`, `design/portfolio-design.css`, `design/strategy-design.css`, and `design/contact-design.css`, registered after the previous finishing styles in `build_site.py`.

Portfolio mastheads live in `visual_catalog.py`, screenshot labels in `visual_products.py`, and the composer masthead wrapper in `ux_components.py`. Responsive image sizing lives in `performance_build.py`. Product facts, statuses, and official destinations remain in the `APPS` records in `build_site.py`.
