---
schema_version: "1.0"
domain: sermorelin.com
captured_at: 2026-06-17
source_capture: 2026-06-16
qa_status: clean
---

## Visual & brand impression

Sermorelin.com reads as a tidy direct-response healthcare storefront: large italic headlines, blue section heads, and a tight two-column product/pricing hero establish a clear buying path [typography_01][layout_01]. The brand system is coherent but conventional, leaning on navy/light-blue fields, teal CTAs, and repeated vial renders for continuity [color_01][color_02]. Its cards and step modules are strongest when the grid stays simple [layout_02][layout_04], while dense research/testimonial copy and borrowed-looking trust graphics make some sections feel assembled rather than designed from first principles [typography_03][iconography_02]. Generic lifestyle/provider photography and heterogeneous article thumbnails dilute the otherwise consistent product story [color_03][color_04].

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: "homepage hero"
  tile_path: store/sermorelin-com/captures/2026-06-16/tiles/homepage/tile-00-y00000.png
  claim: The opening type stack creates a legible three-level hierarchy with a large italic headline, smaller grey support line, and bold product-section header below.
  visible_tells:
    - "Restore your peak performance is much larger than the subhead and set in italic."
    - "The subhead is smaller and grey, separating it from the headline."
    - "Sermorelin Therapy below returns to a bold upright section-title style."
  confidence: high
- id: typography_02
  family: typography_hierarchy
  polarity: strong
  page_or_region: "process panel"
  tile_path: store/sermorelin-com/captures/2026-06-16/tiles/homepage/tile-01-y01220.png
  claim: The process panel keeps its instructional hierarchy clean by pairing one large blue heading with numbered step labels and smaller body copy.
  visible_tells:
    - "How Sermorelin Therapy Works is the largest element in the right column."
    - "The 1, 2, and 3 circles anchor each step label at the same left edge."
    - "Body copy sits below each label in a lighter, smaller text tier."
  confidence: high
- id: typography_03
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "research band"
  tile_path: store/sermorelin-com/captures/2026-06-16/tiles/homepage/tile-01-y01220.png
  claim: The research band has a clear centered headline and three-column structure, but the supporting paragraphs are long and low-contrast for white text on a saturated blue ground.
  visible_tells:
    - "The main research headline is large and bright at the top of the blue band."
    - "Each of the three columns carries a dense paragraph block beneath a logo."
    - "The paragraph text is much smaller and lighter than the headline."
  confidence: high
- id: typography_04
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "guarantee band and testimonial carousel"
  tile_path: store/sermorelin-com/captures/2026-06-16/tiles/homepage/tile-05-y06100.png
  claim: The page repeatedly uses centered white-on-blue headings effectively, but the testimonial cards switch into dense paragraph blocks that reduce scanability.
  visible_tells:
    - "They Felt the Shift. You Will Too. is centered and bright against the blue panel."
    - "SERMORELIN THERAPY REVIEWS is a smaller uppercase tier beneath it."
    - "The review cards contain long multi-line paragraphs with tight line lengths."
  confidence: high
- id: typography_05
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "FAQ and article rail"
  tile_path: store/sermorelin-com/captures/2026-06-16/tiles/homepage/tile-06-y07320.png
  claim: The FAQ questions are easy to scan as large accordion rows, while the article cards below introduce chunkier multi-line titles and category badges competing for attention.
  visible_tells:
    - "FAQ rows use large bold labels inside wide white accordions."
    - "Article cards below use bright blue category pills above black multi-line titles."
    - "Several card titles wrap to three lines."
  confidence: high
- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: "homepage product and pricing hero"
  tile_path: store/sermorelin-com/captures/2026-06-16/tiles/homepage/tile-00-y00000.png
  claim: The hero resolves into a clear two-column buying layout, with product imagery on the left and price, plan selection, and purchase actions stacked on the right.
  visible_tells:
    - "The large vial image occupies a single rounded panel on the left."
    - "The right column stacks savings banner, price, plan rows, and Buy Now CTA."
    - "Both columns sit on the same horizontal band beneath the product toggle."
  confidence: high
- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: "how it works card"
  tile_path: store/sermorelin-com/captures/2026-06-16/tiles/homepage/tile-01-y01220.png
  claim: The how-it-works module is a disciplined split card, using a hard vertical image/text division and a repeated step component in the text half.
  visible_tells:
    - "The left image and right copy share one rounded card container."
    - "The split between image and copy is a straight vertical boundary."
    - "Each step repeats the same circle-number, heading, body, dotted-connector rhythm."
  confidence: high
- id: layout_03
  family: layout_composition_components
  polarity: mixed
  page_or_region: "research band"
  tile_path: store/sermorelin-com/captures/2026-06-16/tiles/homepage/tile-01-y01220.png
  claim: The research band is orderly as a three-column proof block, but its equal columns pack long text into narrow measures and make the section heavier than surrounding modules.
  visible_tells:
    - "Three columns are evenly spaced across the blue band."
    - "Each column has a logo above a centered paragraph block."
    - "The paragraphs fill much of the vertical space beneath each logo."
  confidence: high
- id: layout_04
  family: layout_composition_components
  polarity: strong
  page_or_region: "Sermorelin Injection product section"
  tile_path: store/sermorelin-com/captures/2026-06-16/tiles/homepage/tile-03-y03660.png
  claim: The mid-page product section uses generous whitespace and a simple text-left/image-right grid, giving the product offer a calmer rhythm than the denser hero.
  visible_tells:
    - "The left column contains a title, short benefit list, and two CTAs with ample surrounding space."
    - "The right column holds one large vial image inside a pale-blue rounded rectangle."
    - "The full section sits inside a broad white card with soft shadow and large margins."
  confidence: high
- id: layout_05
  family: layout_composition_components
  polarity: mixed
  page_or_region: "Peptide therapy simplified cards"
  tile_path: store/sermorelin-com/captures/2026-06-16/tiles/homepage/tile-04-y04880.png
  claim: The four-column card row repeats a clear component pattern, but the lower imagery varies from form mockup to lifestyle photo to doctor photo to package render, weakening the row as a single system.
  visible_tells:
    - "Four equal-width cards repeat title, paragraph, CTA, and image zones."
    - "The bottom images differ sharply in subject and crop style."
    - "All four CTAs use the same dark-blue pill placement."
  confidence: high
- id: layout_06
  family: layout_composition_components
  polarity: mixed
  page_or_region: "testimonial carousel"
  tile_path: store/sermorelin-com/captures/2026-06-16/tiles/homepage/tile-05-y06100.png
  claim: The testimonial carousel is neatly framed by a blue panel and centered controls, but the visible third card is clipped at the right edge, making the component read like a partly exposed horizontal scroll state.
  visible_tells:
    - "Two full review cards sit inside the blue panel."
    - "A third review card is cut off along the right edge."
    - "The arrow controls are centered below the cards."
  confidence: high
- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: "site-wide palette"
  tile_path: store/sermorelin-com/captures/2026-06-16/tiles/homepage/tile-00-y00000.png
  claim: The site maintains a coherent blue-and-teal palette, using deep navy for trust bands, pale blue for panels, and teal for primary CTAs.
  visible_tells:
    - "The pricing and purchase buttons use saturated teal."
    - "The research and footer sections use deep blue or navy grounds."
    - "Product and process panels sit on pale blue backgrounds."
  confidence: high
  contrast_with: store/sermorelin-com/captures/2026-06-16/tiles/homepage/tile-08-y08592.png
- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: "product renders"
  tile_path: store/sermorelin-com/captures/2026-06-16/tiles/homepage/tile-03-y03660.png
  claim: The repeated vial render gives the page a consistent product image language across the hero, mid-page offer block, and footer CTA.
  visible_tells:
    - "The blue-labeled vial appears large in the product section."
    - "The same vial form appears again in the hero image."
    - "The footer CTA reuses the vial at an angled crop against a blue panel."
  confidence: high
  contrast_with: store/sermorelin-com/captures/2026-06-16/tiles/homepage/tile-08-y08592.png
- id: color_03
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "lifestyle and provider imagery"
  tile_path: store/sermorelin-com/captures/2026-06-16/tiles/homepage/tile-04-y04880.png
  claim: The page uses bright healthcare and fitness photography, but the bodybuilder, doctor, smiling patient, and package shots feel like separate image sources rather than one owned photographic system.
  visible_tells:
    - "A doctor portrait, fitness model, and package render appear in adjacent benefit cards."
    - "The guarantee band uses a cropped smiling woman against a blue gradient."
    - "The quote panel above uses another doctor portrait on a pale yellow ground."
  confidence: high
- id: color_04
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "article thumbnail rail"
  tile_path: store/sermorelin-com/captures/2026-06-16/tiles/homepage/tile-06-y07320.png
  claim: The article rail has consistent white cards and blue category labels, but the thumbnails mix infographic, dark clinical graphic, beauty close-up, and peach skincare treatments with little shared image direction.
  visible_tells:
    - "The first visible thumbnail is an orange pulse-chart infographic."
    - "The second is a dark blue clinical graphic with chart elements."
    - "Later thumbnails use pale cosmetic close-ups and peach-toned skin imagery."
  confidence: high
- id: color_05
  family: color_brand_imagery
  polarity: strong
  page_or_region: "footer guide CTA"
  tile_path: store/sermorelin-com/captures/2026-06-16/tiles/homepage/tile-08-y08592.png
  claim: The footer guide CTA is one of the most coherent branded moments, combining the vial render, blue gradient field, white headline, and teal action button in a single contained panel.
  visible_tells:
    - "The angled vial sits on the same blue gradient as the surrounding panel."
    - "The large white headline is paired with smaller white explanatory copy."
    - "The email field uses a teal button matching other CTAs on the page."
  confidence: high
- id: iconography_01
  family: iconography_illustration
  polarity: strong
  page_or_region: "top benefit strip"
  tile_path: store/sermorelin-com/captures/2026-06-16/tiles/homepage/tile-00-y00000.png
  claim: The top benefit strip uses a consistent light-outline icon style, giving the utility claims a tidy shared visual vocabulary.
  visible_tells:
    - "Recovery, muscle, heart, shield, and truck marks all use thin grey outlines."
    - "Each icon sits to the left of a short label on the same baseline."
    - "The strip repeats spacing and icon scale across the full width."
  confidence: high
- id: iconography_02
  family: iconography_illustration
  polarity: mixed
  page_or_region: "research logos and trust marks"
  tile_path: store/sermorelin-com/captures/2026-06-16/tiles/homepage/tile-01-y01220.png
  claim: The trust graphics create recognizable proof points, but the section relies on borrowed institutional logo marks rather than a custom illustration or diagram system.
  visible_tells:
    - "Mayo Clinic, NIH, and MDPI marks appear as separate white logo lockups."
    - "The logos differ in shape and density from one another."
    - "No custom explanatory diagram accompanies the three-column proof block."
  confidence: high
- id: iconography_03
  family: iconography_illustration
  polarity: mixed
  page_or_region: "benefit icons in product offer"
  tile_path: store/sermorelin-com/captures/2026-06-16/tiles/homepage/tile-03-y03660.png
  claim: The benefit-list icons are aligned and legible, but their medical, headset, and truck symbols read as generic line icons with little brand-specific character.
  visible_tells:
    - "Four small line icons align to the same left column beside the benefit text."
    - "The symbols use thin outline strokes with no filled brand color."
    - "The icon subjects are standard fee, plan, support, and shipping metaphors."
  confidence: high
- id: iconography_04
  family: iconography_illustration
  polarity: mixed
  page_or_region: "verification and carousel controls"
  tile_path: store/sermorelin-com/captures/2026-06-16/tiles/homepage/tile-05-y06100.png
  claim: The testimonial module uses recognizable quote, verification, and arrow symbols, but they function as stock UI accents rather than an owned icon set.
  visible_tells:
    - "Large yellow quote marks repeat at the top of each review card."
    - "Verified Patient appears as a teal pill badge."
    - "The carousel controls are simple circular arrow buttons."
  confidence: high
```

## Provenance

Tiles read: `store/sermorelin-com/captures/2026-06-16/tiles/homepage/` (`tile-00-y00000.png` through `tile-08-y08592.png`, plus `overview-480w.png` for QA).

QA note: cached homepage tiles were clean; no modal, blank hero, black media block, lazy-load gap, or compositing artifact was found in cited regions. No exclusions. Tier-B browser re-render was not used.

Scope caveat: this layer is mined from the cached homepage screenshot only. The capture includes additional non-screenshot page payloads, but those pages were not used for visual evidence.
