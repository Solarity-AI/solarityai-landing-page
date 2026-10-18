# Thirty further design improvements

Implemented October 12, 2026, America/Chicago. This pass follows `DESIGN_REFINEMENTS.md` and retains the existing hero artwork, verified product evidence, contact behavior, and public access.

## Shared presentation and adaptive layouts

1. Move the mobile hero artwork caption into a dedicated reading rail, preserving its conceptual-art label.
2. Give the homepage product evidence links restrained product-colored rules and directional cues.
3. Add concise destination descriptions to the expanded mobile navigation.
4. Mark the current page in the footer and align its destination arrows.
5. Arrange the 404 recovery choices as a numbered destination directory with readable descriptions.
6. Allow the expanded mobile menu to scroll on short viewports while preserving the established header height.
7. Add forced-color control boundaries, current-page indicators, focus outlines, and non-color selection cues.
8. Add a light print reading layout, remove decorative/navigation clutter, and reset dialog scroll locks and autofill text colors for printing.

## Portfolio and product pages

9. Separate the breadcrumb rail from product category context.
10. Present product features as numbered reading rows with a clear heading and description hierarchy.
11. Give product context and limitations a labeled annotation treatment.
12. Align related products in a comparison directory with identity, category, availability, and directional cues.
13. Clarify verified store actions with iOS and Android sublabels and grouped availability.
14. Give the native screenshot dialog an ivory toolbar, matte image surround, and separate provenance panel.
15. Arrange the Voice Max explanatory essay in two columns on wider screens.
16. Give the portfolio chooser a concise directory label and consistent divider, hover, and focus treatments.

## Company, platform, and investor narrative

17. Align investor product rows into stable identity, category, and availability tracks.
18. Strengthen the typographic hierarchy of the Build, Operate, and Grow ledger.
19. Arrange partnership pathways in two desktop columns with full-width mobile rows.
20. Turn company principles into a numbered title-and-meaning register.
21. Strengthen the founder narrative lead and distinguish its closing action.
22. Separate the platform strategy-boundary label from its explanation without changing the wording.
23. Give module intended-focus paragraphs a distinct annotation treatment and separate their actions.
24. Number the native investor FAQ and align questions, answers, and open-state markers.

## Contact composer

25. Align inquiry selection markers, titles, and descriptions.
26. Reinforce selected inquiry states with a visible tick and text weight, and clarify disabled states.
27. Refine keyboard, autofill, text-selection, and readonly draft styling.
28. Clarify focus and open states for the optional native disclosure.
29. Add decorative utility icons and responsive alignment to copy, select, and edit actions.
30. Separate the email-send reminder from the manual webmail fallback.

## Maintenance

The four finishing sources are `design/product-details.css`, `design/strategy-details.css`, `design/contact-details.css`, and `design/adaptive-details.css`, registered in that order at the end of `style_sources` in `build_site.py`. The adaptive stylesheet stays last so print and forced-color overrides remain effective. Edit source components and styles, then regenerate `dist` with `python3 build_site.py`; do not edit generated HTML directly.

Product facts, availability, destinations, and source evidence remain in the existing content model and source register. This pass does not establish new product capabilities, launch states, metrics, or company claims. The email composer still creates an email draft and does not claim delivery.

## Verification

- Static validation passes all 11 pages, 324 internal links/fragments, and 177 local asset references without errors or warnings.
- All 51 existing tests pass: 12 contact, 11 navigation, 9 gallery, 12 CSS optimizer, and 7 public-URL cases.
- Before/after parsing of all 11 routes confirms unchanged destinations, target/rel values across 353 anchors, heading order and text, native control attributes, image attributes, and runtime script bytes. Intentional additions are footer current-page states and homepage product accent data attributes.
- Independent source/cascade review covers responsive rules for 360, 390, 768, 1024, and 1440 pixels; menu geometry; store-label and arrow interactions; related product alignment; FAQ columns; contact states; forced colors; and print. Two concrete alternate-view issues were fixed: autofill text colors and the screenshot dialog's print scroll lock.
- No new JavaScript, fonts, raster assets, or dependencies are added. The homepage retains 2,798 bytes of inline navigation JavaScript and no external scripts. Build-time byte estimates are recorded in `research-assets/performance-build.json`.
- These are source, logic, and static-output checks. Live browser rendering, actual viewport overflow, assistive-technology operation, print/high-contrast rendering, and fresh Lighthouse/PageSpeed scores were not measured because the supported browser workflow is unavailable. Historical user-reported scores are not new measurements.

Public deployment verification is recorded in the delivery response after publication.
