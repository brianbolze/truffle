---
schema_version: "1.0"
domain: telolife.com
captured_at: 2026-06-17
source_capture: 2026-06-04
qa_status: clean
---

# Telo Life - visual evidence

## Visual & brand impression

Telo Life reads as calm, controlled, and intentionally soft: oversized sans headlines pair with a recurring italic serif flourish, all held inside a narrow sage, cream, and deep-green system [typography_01][color_01]. The strongest pieces are the opening split hero, reusable six-step and pricing-card systems, and coherent bottle/product rendering [layout_01][layout_02][layout_03][iconography_01]. The restraint also makes the site feel thin in places: pricing and financing pages are very sparse, the package-benefit card leaves a visible orphaned item, and third-party payment marks puncture the otherwise quiet palette [layout_05][layout_06][color_05]. Trust and utility icons are consistent but generic, while the tiny stacked logo mark has weak recognizability at navigation scale [iconography_02][iconography_05].

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: homepage hero and repeated page headings
  tile_path: store/telolife-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png
  claim: The site uses a clear signature headline pairing: heavy rounded sans for the main phrase and a large italic serif for the emotional modifier, establishing a recognizable typographic motif immediately.
  visible_tells:
    - "'Weight loss,' appears in oversized bold sans, while 'made simple.' sits directly below in a contrasting italic serif."
    - The same sans-plus-italic formula appears again in the lower 'Start your journey in / under five minutes.' heading visible at the bottom of the tile.
  confidence: high
  contrast_with: store/telolife-com/captures/2026-06-04/tiles/packages/tile-00-y00000.png
- id: typography_02
  family: typography_hierarchy
  polarity: strong
  page_or_region: homepage hero
  tile_path: store/telolife-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png
  claim: The hero hierarchy is well separated, moving from a small uppercase pill to a dominant H1, a medium body paragraph, icon bullets, and two CTA levels without flattening the page.
  visible_tells:
    - The 'DOCTOR-GUIDED GLP-1 CARE' eyebrow is a small rounded capsule above the much larger headline.
    - Body copy is visibly smaller and lighter than the H1, while the bullet list uses heavier short lines and check icons for scannability.
    - Primary and secondary CTAs are separated by fill weight and placement.
  confidence: high
- id: typography_03
  family: typography_hierarchy
  polarity: strong
  page_or_region: pricing page hero
  tile_path: store/telolife-com/captures/2026-06-04/tiles/pricing/tile-00-y00000.png
  claim: The pricing page compresses its whole message into a disciplined center stack with clear type steps from badge to display heading, all-caps assertion, explanatory copy, and price line.
  visible_tells:
    - 'TRANSPARENT PRICING' appears in a small dark-green badge above the large 'Simple, honest / pricing.' heading pair.
    - The all-caps 'ALL-INCLUSIVE REGARDLESS OF DOSAGE.' block is smaller than the headline but heavier than the body copy.
    - The Semaglutide and Tirzepatide price line sits lower as a separate heavier row.
  confidence: high
- id: typography_04
  family: typography_hierarchy
  polarity: mixed
  page_or_region: package selector page heading
  tile_path: store/telolife-com/captures/2026-06-04/tiles/packages/tile-00-y00000.png
  claim: The sans-and-italic headline device is consistent, but by the package page it reads as a formula rather than adding new hierarchy because the italic phrase simply repeats the same second-line treatment.
  visible_tells:
    - 'Choose a plan that' is set in the same oversized sans style as the homepage and pricing headings.
    - 'fits your life.' repeats the same large italic serif treatment used on 'made simple.' and 'pricing.'
  confidence: high
  contrast_with: store/telolife-com/captures/2026-06-04/tiles/pricing/tile-00-y00000.png
- id: typography_05
  family: typography_hierarchy
  polarity: mixed
  page_or_region: package cards
  tile_path: store/telolife-com/captures/2026-06-04/tiles/packages/tile-00-y00000.png
  claim: The package cards make the price the clear focal point, but the plan metadata, totals, approval note, and bullet lists become a cluster of small green text that relies mostly on spacing rather than strong type hierarchy.
  visible_tells:
    - The '$26/mo' and '$53/mo' figures are much larger than every other card element.
    - '3-MONTH BUNDLE,' 'As low as,' total price, approval note, and bullet text all sit in similarly small green type.
    - The button becomes the second-strongest element because it is much heavier than the supporting text.
  confidence: high
- id: typography_06
  family: typography_hierarchy
  polarity: poor
  page_or_region: financing form helper text and footer legal
  tile_path: store/telolife-com/captures/2026-06-04/tiles/financing/tile-01-y00269.png
  claim: The lowest-level helper and legal text falls into very pale, small type, making important clarifying copy visually recede below the surrounding form and footer structure.
  visible_tells:
    - The consent line below 'Continue to Cherry' is small and light compared with the field labels and button text.
    - The bottom legal sentence in the dark-green footer is tiny and low-contrast relative to the footer columns.
  confidence: high
- id: typography_07
  family: typography_hierarchy
  polarity: mixed
  page_or_region: package FAQ card
  tile_path: store/telolife-com/captures/2026-06-04/tiles/packages/tile-03-y02703.png
  claim: The FAQ section has a strong title, but the individual questions are rendered as same-weight plain lines without visible dividers or icon affordances, so the interactive hierarchy feels understated.
  visible_tells:
    - 'Common questions about GLP-1 care.' is large and centered.
    - The six question rows below are same-size, same-weight dark-green lines with broad vertical spacing.
    - No plus icons, chevrons, row borders, or expansion indicators are visible beside the questions.
  confidence: high
- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: homepage hero
  tile_path: store/telolife-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png
  claim: The hero uses a polished two-column composition: left-side message stack and CTA system balanced against a large rounded product-render panel on the right.
  visible_tells:
    - Left column contains eyebrow, headline, paragraph, bullet list, CTAs, and compliance line in a single vertical stack.
    - Right column holds two angled vial renders inside one rounded cream panel with a soft shadow.
    - The columns occupy similar visual weight with generous negative space around both.
  confidence: high
- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: homepage six-step section
  tile_path: store/telolife-com/captures/2026-06-04/tiles/homepage/tile-01-y01220.png
  claim: The six-step process block is a disciplined component grid, with equal card sizing, consistent number placement, and repeated heading/body structure across all steps.
  visible_tells:
    - Six white cards form a clean 3-by-2 grid inside one larger rounded cream container.
    - Each card begins with a large italic green number, followed by a bold step title and smaller explanatory copy.
    - Gutters and card corner radii are consistent across the grid.
  confidence: high
- id: layout_03
  family: layout_composition_components
  polarity: strong
  page_or_region: package selector and pricing grid
  tile_path: store/telolife-com/captures/2026-06-04/tiles/packages/tile-00-y00000.png
  claim: The package page shows a mature conversion component system: segmented controls, matched pricing cards, active-state shadows, and a highlighted plan badge all follow one layout grammar.
  visible_tells:
    - Cash/Financing and Semaglutide/Tirzepatide controls share the same pill shape and green active state.
    - Four pricing cards align to a two-column grid with matching widths, padding, and button placement.
    - The 12-month card is distinguished by a green border and centered 'MOST POPULAR' tab.
  confidence: high
- id: layout_04
  family: layout_composition_components
  polarity: strong
  page_or_region: financing page form
  tile_path: store/telolife-com/captures/2026-06-04/tiles/financing/tile-00-y00000.png
  claim: The financing page is a clean task layout, with a short explanatory column on the left and a self-contained form card on the right.
  visible_tells:
    - The left column uses one large headline, one paragraph, and four check-bullet benefits.
    - The right column is a raised white rounded card with grouped fields, section dividers, and one full-width green submit button.
    - The two columns align near the top and leave clear whitespace between content and form.
  confidence: high
- id: layout_05
  family: layout_composition_components
  polarity: mixed
  page_or_region: pricing and financing short pages
  tile_path: store/telolife-com/captures/2026-06-04/tiles/pricing/tile-00-y00000.png
  claim: The short utility pages remain clean, but their layouts are so sparse that the footer becomes a major part of the first captured view, making the pages feel like thin panels rather than fully developed pages.
  visible_tells:
    - On pricing, the centered pricing stack ends before the lower half of the tile, after which the dark-green footer occupies a large band.
    - The only mid-page component is the payment-method strip; there are no additional explanatory cards or comparison sections before the footer.
  confidence: high
  contrast_with: store/telolife-com/captures/2026-06-04/tiles/financing/tile-00-y00000.png
- id: layout_06
  family: layout_composition_components
  polarity: poor
  page_or_region: packages benefit card
  tile_path: store/telolife-com/captures/2026-06-04/tiles/packages/tile-02-y02440.png
  claim: The 'Every plan, every time.' benefit panel breaks its own grid by leaving one final benefit orphaned at the lower-left, with a large empty field to its right.
  visible_tells:
    - Four benefit items form an even top row across the white panel.
    - The fifth 'Medications' item sits alone in the lower-left corner.
    - The lower-right three-quarters of the panel is blank, making the single item look stranded.
  confidence: high
- id: layout_07
  family: layout_composition_components
  polarity: mixed
  page_or_region: homepage testimonial section
  tile_path: store/telolife-com/captures/2026-06-04/tiles/homepage/tile-02-y02440.png
  claim: The testimonial block has an elegant left-image/right-quote split, but the composition depends on one very large stock-style portrait and leaves the metric row visually lighter than the quote.
  visible_tells:
    - Large rounded portrait fills the left side and is cropped tightly around the subject's face.
    - The quote sits right of the image in italic serif at large size.
    - The three metrics below are small compared with the portrait and quote, separated only by a thin horizontal rule.
  confidence: high
- id: layout_08
  family: layout_composition_components
  polarity: strong
  page_or_region: homepage CTA and footer transition
  tile_path: store/telolife-com/captures/2026-06-04/tiles/homepage/tile-03-y03527.png
  claim: The end-of-page CTA uses a simple high-contrast slab that creates a clean stopping point before the footer, avoiding the common problem of a weak final section dissolving into legal navigation.
  visible_tells:
    - A large dark-green rounded rectangle centers 'Ready when / you are.' with one white pill CTA.
    - The CTA block sits on the pale green page background with ample margin above the footer.
    - The footer begins as a separate full-width darker band below it.
  confidence: high
- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: site-wide palette across homepage
  tile_path: store/telolife-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png
  claim: The core palette is tightly controlled: pale sage page fields, cream cards, deep forest-green type and buttons, and muted olive accents stay consistent across the visible homepage.
  visible_tells:
    - Hero background is pale sage, while the content cards below use warm cream.
    - Headlines, bullets, buttons, and product labels all use deep forest green.
    - Secondary accents use a softer olive rather than introducing unrelated hues.
  confidence: high
  contrast_with: store/telolife-com/captures/2026-06-04/tiles/homepage/tile-03-y03527.png
- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: homepage product imagery
  tile_path: store/telolife-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png
  claim: The bottle render is color-matched to the interface, using deep green caps and labels that echo the buttons and headline color instead of appearing as pasted-in medical stock.
  visible_tells:
    - Both vial caps and labels use the same dark green family as the CTA buttons.
    - The cream render background matches the cream card surfaces elsewhere on the page.
    - Soft shadows under the render match the shadow treatment on cards and CTAs.
  confidence: high
- id: color_03
  family: color_brand_imagery
  polarity: strong
  page_or_region: homepage testimonial image and page field
  tile_path: store/telolife-com/captures/2026-06-04/tiles/homepage/tile-02-y02440.png
  claim: The testimonial portrait is warm and desaturated enough to sit inside the sage-green system rather than fighting it with saturated lifestyle color.
  visible_tells:
    - Portrait highlights are beige and peach rather than bright or high-saturation.
    - The image sits beside green text on the same pale sage page field without a color clash.
    - The portrait frame uses the same rounded-corner vocabulary as the product hero.
  confidence: high
- id: color_04
  family: color_brand_imagery
  polarity: mixed
  page_or_region: packages and pricing pages
  tile_path: store/telolife-com/captures/2026-06-04/tiles/packages/tile-00-y00000.png
  claim: The narrow green-and-cream palette is elegant but gives controls, headings, cards, and background few distinct semantic colors, so state changes rely heavily on shadow and border rather than hue.
  visible_tells:
    - Active segmented controls, CTA buttons, card outlines, headings, and body text are all variations of green.
    - Inactive controls and cards sit in cream/off-white against a pale sage page background.
    - The selected 12-month card is distinguished by border and badge shape more than by a new color.
  confidence: high
  contrast_with: store/telolife-com/captures/2026-06-04/tiles/pricing/tile-00-y00000.png
- id: color_05
  family: color_brand_imagery
  polarity: mixed
  page_or_region: pricing payment methods
  tile_path: store/telolife-com/captures/2026-06-04/tiles/pricing/tile-00-y00000.png
  claim: Third-party payment and financing logos introduce the only bright off-palette colors on the pricing page, which is useful for recognition but visually interrupts the otherwise quiet monochrome system.
  visible_tells:
    - Apple Pay and Google Pay marks appear beside Cherry, Affirm, Klarna, and Afterpay logos in a white rounded strip.
    - Pink, blue, yellow, and mint accents appear only inside those third-party marks.
    - The surrounding page otherwise uses sage, cream, and green.
  confidence: high
- id: color_06
  family: color_brand_imagery
  polarity: strong
  page_or_region: homepage final CTA and footer
  tile_path: store/telolife-com/captures/2026-06-04/tiles/homepage/tile-03-y03527.png
  claim: The dark-green CTA slab and darker footer create a controlled tonal descent at the end of the page, giving the close a clear brand-color endpoint.
  visible_tells:
    - The final CTA uses a saturated forest-green rectangle with white text and a cream button.
    - The footer below is an even darker green band with lighter green-gray text.
    - No new accent colors appear in the close; the palette remains restrained.
  confidence: high
- id: iconography_01
  family: iconography_illustration
  polarity: strong
  page_or_region: homepage product render
  tile_path: store/telolife-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png
  claim: The hero product graphics are polished, dimensional bottle renders with readable labels, glass highlights, cap shadows, and an angled overlap that gives the page a tangible product anchor.
  visible_tells:
    - Two vials are angled diagonally with transparent glass edges, cap highlights, and label curvature.
    - 'Compounded Semaglutide' and 'Compounded Tirzepatide' labels are readable on the bottles.
    - The larger vial overlaps the smaller one, creating depth inside the rounded panel.
  confidence: high
- id: iconography_02
  family: iconography_illustration
  polarity: mixed
  page_or_region: packages benefit icons
  tile_path: store/telolife-com/captures/2026-06-04/tiles/packages/tile-02-y02440.png
  claim: The benefit icons form a coherent lightweight line set, but the drawings are generic utility symbols rather than a distinctive illustration language.
  visible_tells:
    - Clinician care, 24/7 support, shipping, heart, and medication icons all use thin green strokes inside pale rounded-square containers.
    - The icons share stroke weight and container style.
    - The symbols are common line-icons rather than custom brand illustrations.
  confidence: high
- id: iconography_03
  family: iconography_illustration
  polarity: strong
  page_or_region: homepage and financing check bullets
  tile_path: store/telolife-com/captures/2026-06-04/tiles/financing/tile-00-y00000.png
  claim: Checkmark bullets are consistently styled as filled green circles with white checks, giving eligibility and benefit lists a recognizable visual rhythm across pages.
  visible_tells:
    - Financing page benefit list uses four identical filled green check circles.
    - Homepage hero uses the same filled check-circle style beside its benefit list.
    - Check icons align cleanly to the text baseline.
  confidence: high
  contrast_with: store/telolife-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png
- id: iconography_04
  family: iconography_illustration
  polarity: mixed
  page_or_region: footer certification badge
  tile_path: store/telolife-com/captures/2026-06-04/tiles/homepage/tile-03-y03527.png
  claim: The external certification badge adds credibility symbolism but does not belong to the site's visual system, bringing a dark-blue shield and dense micro-detail into an otherwise green, spare footer.
  visible_tells:
    - The LegitScript badge is a blue shield with multiple small white and yellow details.
    - It sits below the white footer logo in a section otherwise limited to green and muted gray-green.
    - Its shape, colors, and detail density differ from the site's rounded-pill and line-icon vocabulary.
  confidence: high
- id: iconography_05
  family: iconography_illustration
  polarity: poor
  page_or_region: navigation logo mark
  tile_path: store/telolife-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png
  claim: The primary logo mark is too small and fragmented at nav scale, reading as stacked letter fragments rather than a clear brand mark.
  visible_tells:
    - The top-left mark resolves as tiny stacked 'TE' over 'LO' letter pieces.
    - The mark occupies far less visual area than the nav links and sign-in pill.
    - At the captured resolution, the lower letters are visibly broken or faint.
  confidence: high
- id: iconography_06
  family: iconography_illustration
  polarity: mixed
  page_or_region: package controls and partner marks
  tile_path: store/telolife-com/captures/2026-06-04/tiles/packages/tile-01-y01220.png
  claim: The Cherry partner marks are integrated in rounded containers, but the repeated third-party logos act more like embedded payment widgets than native iconography.
  visible_tells:
    - The mid-page financing strip places the pink Cherry logo alone inside a small rounded pill.
    - The larger 'ALREADY CHERRY APPROVED' banner repeats the Cherry logo in a white rounded rectangle on a dark-green slab.
    - These marks differ in typography and color from the site's own icon system.
  confidence: high
```

## Provenance

Tiles read: homepage (4) + pricing (2) + packages (4) + financing (2) = 12 active tiles from `store/telolife-com/captures/2026-06-04/tiles/`. QA gate: clean. The page overviews and native tile spot-checks showed no modal, cookie banner, grey/WebGL hero, black media, lazy-load gap, or mid-animation capture; no exclusions and no Tier-B browser re-render were needed.

Mined as a blind tiles-only pass in Codex on 2026-06-17: no `profile.md`, dossier body, Notion, or live web consulted. The scripted `Workflow(...)` runner referenced by [`/visual-evidence`](../../skills/visual-evidence/SKILL.md) was not exposed in this session, so the cards were authored manually from the active native tiles against [`VISUAL.md`](../../modules/VISUAL.md); the same blinding boundary and lint contract were preserved. Every `poor` structural card was spot-checked against its native tile and reflects visible page state, not capture contamination. Snapshot caveat: reflects the 2026-06-04 cached capture; the live site changes.
