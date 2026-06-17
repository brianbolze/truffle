---
schema_version: "1.0"
domain: nurx.com
captured_at: 2026-06-17
source_capture: 2026-06-04
qa_status: clean
---

## Visual & brand impression

Nurx reads warm, approachable, and highly systematized: cream fields, orange accents, black CTAs, and close-cropped patient photography repeat across the homepage, directory, and condition pages [color_01][color_02][layout_01]. The strongest pages use big, calm split heroes and simple data/benefit cards [typography_02][layout_02][iconography_04]. The system is less graceful when it becomes a catalog: carousels, repeated filter bars, eligibility tags, and full-width FAQ rows add mechanical weight [layout_04][layout_06][iconography_05]. Product imagery is controlled but partly manufacturer-led [color_04]. Overall: friendly consumer health with disciplined components, warmed by human photography, but dense lower-page modules and legal copy flatten the polish [typography_06].

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: "homepage hero"
  tile_path: "store/nurx-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"
  claim: "The homepage hero creates a clear three-tier type hierarchy: oversized white headline, smaller centered support line, then compact uppercase navigation and promo text above."
  visible_tells:
    - "Large white headline spans two lines over the darkened green photo."
    - "Support copy sits centered beneath the headline at a noticeably smaller size."
    - "The orange promo strip and nav use small uppercase labels separate from the hero copy."
  confidence: high
- id: typography_02
  family: typography_hierarchy
  polarity: strong
  page_or_region: "weight management hero"
  tile_path: "store/nurx-com/captures/2026-06-04/tiles/weight_management/tile-00-y00000.png"
  claim: "The weight-management hero uses a clean landing-page hierarchy, stepping from an uppercase eyebrow to a large two-line headline, bold subhead, bullet list, and CTA."
  visible_tells:
    - "The eyebrow '100% ONLINE TREATMENT' is letter-spaced and much smaller than the headline."
    - "The headline is the largest element in the left column and breaks cleanly over two lines."
    - "Bullets and the black CTA sit below the bold subhead with generous spacing."
  confidence: high
- id: typography_03
  family: typography_hierarchy
  polarity: strong
  page_or_region: "services directory header"
  tile_path: "store/nurx-com/captures/2026-06-04/tiles/our_services/tile-00-y00000.png"
  claim: "The services directory opens with a simple centered hierarchy: large title, restrained explanatory line, then smaller filter controls before the image grid."
  visible_tells:
    - "'Explore your options' is centered and dramatically larger than the paragraph below."
    - "The filter row is visually secondary, using pill outlines and compact uppercase text."
    - "The six category labels sit below images at a consistent size."
  confidence: high
- id: typography_04
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "services carousel cards"
  tile_path: "store/nurx-com/captures/2026-06-04/tiles/our_services/tile-01-y01220.png"
  claim: "The carousel-card hierarchy is readable, but the small eligibility labels add a third micro-tier that competes with card copy and buttons."
  visible_tells:
    - "Card titles are clearly larger than the descriptive body text."
    - "The 'INSURANCE' and 'FSA/HSA ELIGIBLE' labels use tiny uppercase text and small orange checks."
    - "The black Learn More buttons have more visual weight than the eligibility row."
  confidence: high
- id: typography_05
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "acne pricing table"
  tile_path: "store/nurx-com/captures/2026-06-04/tiles/acne/tile-02-y02440.png"
  claim: "The pricing table uses a strong orange header to clarify columns, but the row labels below are small, underlined, and visually closer to body links than to a tabular data system."
  visible_tells:
    - "The table header is a saturated orange band with letter-spaced uppercase labels."
    - "Medication names in the first column are underlined and much smaller than the section heading."
    - "The table sits beneath a paragraph block, creating a dense text-heavy handoff."
  confidence: medium
- id: typography_06
  family: typography_hierarchy
  polarity: poor
  page_or_region: "weight management disclosure block"
  tile_path: "store/nurx-com/captures/2026-06-04/tiles/weight_management/tile-06-y07320.png"
  claim: "The lower-page disclosure collapses into a dense small-type band, with very long line lengths and no internal hierarchy to help scanning."
  visible_tells:
    - "The paragraph begins at the far left of a wide text measure and runs across most of the page."
    - "The disclosure type is much smaller than the FAQ rows and recommendation heading above it."
    - "There are no subheads, bullets, or spacing breaks inside the visible disclosure block."
  confidence: high

- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: "services directory category grid"
  tile_path: "store/nurx-com/captures/2026-06-04/tiles/our_services/tile-00-y00000.png"
  claim: "The directory category grid is disciplined: six equal image tiles align in a centered 3-by-2 structure with consistent gaps and matching label placement."
  visible_tells:
    - "Three columns repeat across the first row and again on the second row."
    - "Each rounded image tile has the same width and height."
    - "Every category label is centered directly under its image."
  confidence: high
- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: "weight management split hero"
  tile_path: "store/nurx-com/captures/2026-06-04/tiles/weight_management/tile-00-y00000.png"
  claim: "The split hero gives the page a stable composition: text occupies a quiet left half, photography fills the right half, and the next cream section starts cleanly beneath both."
  visible_tells:
    - "The hero is divided almost exactly into a left copy panel and right image panel."
    - "The CTA and bullets stay inside the left column without colliding with the image."
    - "The cream section below begins on a single horizontal boundary across the full viewport."
  confidence: high
- id: layout_03
  family: layout_composition_components
  polarity: strong
  page_or_region: "birth control comparison cards"
  tile_path: "store/nurx-com/captures/2026-06-04/tiles/birthcontrol/tile-01-y01220.png"
  claim: "The online-vs-in-person comparison resolves into two large balanced cards, each using the same internal rhythm of heading, icon row, and sentence."
  visible_tells:
    - "The two cream comparison cards are equal width and height."
    - "Each card uses a letter-spaced heading at the same top offset."
    - "Rows align horizontally across the two cards, pairing check and X states."
  confidence: high
- id: layout_04
  family: layout_composition_components
  polarity: mixed
  page_or_region: "services carousel sections"
  tile_path: "store/nurx-com/captures/2026-06-04/tiles/our_services/tile-01-y01220.png"
  claim: "The carousel system is consistent but busy: arrow controls, partial offscreen cards, and repeated filter bars make the directory feel more mechanical than the opening grid."
  visible_tells:
    - "Grey and black circular arrows sit above each carousel row."
    - "Cards extend beyond the right viewport edge, revealing clipped next cards."
    - "A cream filter band repeats below the carousel before the next section starts."
  confidence: high
- id: layout_05
  family: layout_composition_components
  polarity: mixed
  page_or_region: "acne treatment and pricing handoff"
  tile_path: "store/nurx-com/captures/2026-06-04/tiles/acne/tile-02-y02440.png"
  claim: "The acne page stacks product cards, a pricing intro, a CTA, and a table in a logical order, but the section becomes text-heavy before the reader reaches the tabular content."
  visible_tells:
    - "Three product cards span the top row with equal spacing."
    - "The treatment-pricing section uses a wide paragraph block before the table begins."
    - "A right-aligned black CTA shares the row with the paragraph, adding another focal point."
  confidence: medium
- id: layout_06
  family: layout_composition_components
  polarity: mixed
  page_or_region: "FAQ accordion rows"
  tile_path: "store/nurx-com/captures/2026-06-04/tiles/weight_management/tile-06-y07320.png"
  claim: "The FAQ accordion is clear and repeatable, but the large black plus buttons create a heavy vertical column that dominates the otherwise quiet row layout."
  visible_tells:
    - "Each FAQ row spans the page with a thin horizontal divider."
    - "A black circular plus button appears at the far right of every row."
    - "The repeated black circles are darker and more prominent than the question text."
  confidence: high
- id: layout_07
  family: layout_composition_components
  polarity: strong
  page_or_region: "weight management benefit panel"
  tile_path: "store/nurx-com/captures/2026-06-04/tiles/weight_management/tile-05-y06100.png"
  claim: "The benefit panel pairs a checklist stack with a phone photo in a controlled two-column card, using dividers to keep each row readable."
  visible_tells:
    - "Benefit rows are separated by thin horizontal rules inside the left card."
    - "The phone image fills the right card with matching height and rounded corners."
    - "Both cards sit on the same cream background with consistent outer margins."
  confidence: high

- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: "homepage palette and stat band"
  tile_path: "store/nurx-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"
  claim: "The homepage establishes a tight palette of cream, orange, black, and white, with the orange accent carrying both the promo strip and the stat icons."
  visible_tells:
    - "The top promo bar is saturated orange with black text."
    - "The stat band uses pale cream grid texture and orange icons."
    - "Black CTAs and nav text contrast with the otherwise warm background."
  confidence: high
- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: "services directory photography"
  tile_path: "store/nurx-com/captures/2026-06-04/tiles/our_services/tile-00-y00000.png"
  claim: "The directory photography feels coherent: warm close-ups, soft outdoor light, and product-in-hand crops sit inside the same rounded image treatment."
  visible_tells:
    - "Skin, hair, and product images share warm highlights and muted shadows."
    - "All six category images use rounded rectangles with matching crop proportions."
    - "The cream background keeps the varied photographs in one visual field."
  confidence: high
- id: color_03
  family: color_brand_imagery
  polarity: strong
  page_or_region: "weight management data cards"
  tile_path: "store/nurx-com/captures/2026-06-04/tiles/weight_management/tile-00-y00000.png"
  claim: "The data cards extend the brand palette into simple graphic motifs, using orange shapes, pale grid texture, cream cards, and black rules rather than introducing a separate chart style."
  visible_tells:
    - "The dot matrix and pie shape are both orange on pale cream."
    - "Each card uses the same thin black top and bottom rules."
    - "The grid texture echoes the homepage stat band."
  confidence: high
- id: color_04
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "acne product cards"
  tile_path: "store/nurx-com/captures/2026-06-04/tiles/acne/tile-02-y02440.png"
  claim: "The product-card backgrounds are controlled, but manufacturer package colors pull blue, red, green, and orange into an otherwise narrow warm palette."
  visible_tells:
    - "Spironolactone appears as a white bottle on a pale cream card."
    - "Tretinoin introduces a bright orange tube and Azelaic acid introduces red and green packaging."
    - "All product images sit on matching pale cards with faint triangular shadows."
  confidence: high
- id: color_05
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "app promo and footer"
  tile_path: "store/nurx-com/captures/2026-06-04/tiles/homepage/tile-06-y06406.png"
  claim: "The footer sequence separates itself with lavender and black blocks, which gives the app and email areas clear contrast but feels cooler and less integrated than the cream/orange body system."
  visible_tells:
    - "The app promo background is lavender rather than cream."
    - "The email footer shifts abruptly to a full black block."
    - "Cream callout bubbles on the phone mockup reconnect the area to the main palette."
  confidence: medium
- id: color_06
  family: color_brand_imagery
  polarity: strong
  page_or_region: "birth control hero"
  tile_path: "store/nurx-com/captures/2026-06-04/tiles/birthcontrol/tile-00-y00000.png"
  claim: "The birth-control hero makes the brand palette feel more energetic by pairing the cream copy panel with a saturated orange photo field and black utility bars."
  visible_tells:
    - "The hero photo sits against a large orange field on the right."
    - "The left copy area remains cream with black type and CTA."
    - "A black feature strip runs beneath the hero, echoing the black CTA and nav accents."
  confidence: high

- id: iconography_01
  family: iconography_illustration
  polarity: strong
  page_or_region: "homepage stat icons"
  tile_path: "store/nurx-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"
  claim: "The homepage stat icons are compact, bold, and consistently orange, giving the credibility band a recognizable visual shorthand without adding illustration clutter."
  visible_tells:
    - "The patient, heart, and card-like icons are all orange."
    - "Each icon sits directly before a bold stat label."
    - "Thin vertical dividers separate the three stat items."
  confidence: high
- id: iconography_02
  family: iconography_illustration
  polarity: strong
  page_or_region: "birth control comparison icons"
  tile_path: "store/nurx-com/captures/2026-06-04/tiles/birthcontrol/tile-01-y01220.png"
  claim: "The comparison cards use a tidy state-icon system: orange check circles for the online column and grey X circles for the in-person column."
  visible_tells:
    - "Every online row starts with the same orange circular check icon."
    - "Every in-person row starts with the same grey circular X icon."
    - "Icon size and left alignment match across both columns."
  confidence: high
- id: iconography_03
  family: iconography_illustration
  polarity: strong
  page_or_region: "acne condition illustrations"
  tile_path: "store/nurx-com/captures/2026-06-04/tiles/acne/tile-03-y03660.png"
  claim: "The acne condition icons are specific and custom-feeling, using the same orange fill and black linework to distinguish faces, torso, and shoulder marks."
  visible_tells:
    - "Four icons share orange fill, black outlines, and simple facial/body details."
    - "The face icons differ by dot placement and expression."
    - "The torso and back icons use the same stroke weight and acne-dot motif."
  confidence: high
- id: iconography_04
  family: iconography_illustration
  polarity: strong
  page_or_region: "weight management data illustrations"
  tile_path: "store/nurx-com/captures/2026-06-04/tiles/weight_management/tile-00-y00000.png"
  claim: "The weight-management data cards translate claims into simple abstract graphics, with an orange dot progression and an orange pie wedge over a pale grid."
  visible_tells:
    - "The left card uses orange and pale dots arranged in a stepped pattern."
    - "The right card uses a large orange wedge inside a pale grid circle."
    - "Both illustrations are large enough to read before the text."
  confidence: high
- id: iconography_05
  family: iconography_illustration
  polarity: mixed
  page_or_region: "carousel and FAQ controls"
  tile_path: "store/nurx-com/captures/2026-06-04/tiles/weight_management/tile-06-y07320.png"
  claim: "The interaction icons are familiar but generic: black circular plus buttons and arrow controls are easy to parse, yet visually heavier than the surrounding content."
  visible_tells:
    - "FAQ rows repeat identical black plus buttons down the right side."
    - "Carousel controls elsewhere use black and grey circular arrows."
    - "The controls rely on common symbols rather than a distinctive branded icon shape."
  confidence: high
- id: iconography_06
  family: iconography_illustration
  polarity: mixed
  page_or_region: "app promo feature chips"
  tile_path: "store/nurx-com/captures/2026-06-04/tiles/homepage/tile-06-y06406.png"
  claim: "The app-promo chips are useful but visually louder than the phone mockup: black icons in cream bubbles float around the device and compete with the large wordmark on screen."
  visible_tells:
    - "Three cream bubbles float around the phone mockup."
    - "Each bubble contains a black icon plus a short feature label."
    - "The phone screen also carries a large Nurx wordmark, creating multiple focal points."
  confidence: medium
```

## Provenance

Mined from cached Tier-A screenshot tiles under `store/nurx-com/captures/2026-06-04/tiles/`: `homepage` (7 tiles), `our_services` (9), `weight_management` (9), `birthcontrol` (8), and `acne` (9), 42 active tiles total. QA gate: clean. No exclusions; no Tier-B browser re-render used.

Snapshot caveat: this is visual evidence from the 2026-06-04 captured screenshots, tiled and mined on 2026-06-17. The live site may have changed since the source capture.
