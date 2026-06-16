---
schema_version: "1.0"
domain: agelessrx.com
captured_at: 2026-06-16
source_capture: 2026-05-31
qa_status: clean
---

## Visual & brand impression

A disciplined wellness system built on two tokens — a dominant deep teal and an amber reserved strictly for CTAs, held page to page over a controlled white / pale-blue / teal section structure [color_01][color_02][color_03]. Its strongest asset is owned craft: a uniform amber-bottle / teal-cap product-render language that extends from catalog to product hero [iconography_03], and genuinely custom, on-brand data illustrations — a Now-vs-Future healthspan bar chart, a biological-age scatter, a 70% donut, a BioAge timeline [iconography_05][iconography_06][iconography_07][iconography_08] — over a confident serif-headline hierarchy [typography_01][typography_02]. It frays at the seams: third-party packshots break the render grid [iconography_04], off-palette pink / magenta / lavender intrusions creep in [color_04][color_06][color_09], stock photos and library icons read generic [color_05][iconography_01], a core comparison table renders broken [layout_11], and the partner-logo strip is un-normalized [iconography_09]. Competent and coherent, let down at the edges.

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: homepage hero
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/homepage/tile-00-y00000.png
  claim: "The hero headline is a large serif with an italic 'more' set against a dark teal band, sitting clearly above one small sans-serif subtitle line — a confident, legible two-level entry."
  visible_tells:
  - "Serif headline 'What would you do with more healthy years?' with 'more' in italic, set noticeably larger than all surrounding type"
  - "Single small sans-serif subtitle sits directly below, establishing a clean two-level hierarchy"
  confidence: high
- id: typography_02
  family: typography_hierarchy
  polarity: strong
  page_or_region: homepage — section headings + 3-up feature subheads
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/homepage/tile-02-y02440.png
  claim: "Section titles ('Slowing aging has never been easier', 'Real people, real results') are a consistent large serif sitting above bold sans-serif feature subheads and lighter body, sustaining a legible three-level hierarchy down the scroll."
  visible_tells:
  - "Serif h2 headings are clearly larger and a different face than the sans-serif body below"
  - "Feature subheads ('Simple online assessments', 'Fast, free shipping') sit at a distinct mid-weight level between title and description"
  confidence: high
- id: typography_03
  family: typography_hierarchy
  polarity: strong
  page_or_region: bioage_test — page header (eyebrow / headline / subhead)
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/bioage_test/tile-00-y00000.png
  claim: "The header runs a small spaced all-caps eyebrow ('BIOAGE TESTS'), a large serif headline mixing roman and italic ('How old are you really?'), and a sans subhead — a practiced three-tier entry pattern."
  visible_tells:
  - "All-caps spaced eyebrow 'BIOAGE TESTS' sits a full size-level below the headline"
  - "Italic 'really?' creates emphasis within the headline without a typeface change"
  confidence: high
- id: typography_04
  family: typography_hierarchy
  polarity: strong
  page_or_region: metformin — product detail info card
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/metformin/tile-00-y00000.png
  claim: "The info card stacks four readable levels in a compact space — display-serif product name 'Metformin', a small 'Pill' badge, sans body copy, and a price with the numeral '$25' set larger than the 'Starting at' label."
  visible_tells:
  - "Product name at display serif size, small pill badge below, body paragraph in small sans, price with bold larger numeral — four distinct levels"
  - "Price numeral '$25' is visually larger than the surrounding 'Starting at' label"
  confidence: high
  contrast_with: store/agelessrx-com/captures/2026-05-31/tiles/treatments/tile-00-y00000.png
- id: typography_05
  family: typography_hierarchy
  polarity: mixed
  page_or_region: treatments — product card grid titles vs body
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/treatments/tile-00-y00000.png
  claim: "Product card titles are legible but only modestly larger than their description copy, and 'Learn More' links carry the same weight as body text, so the card's levels stack loosely rather than crisply."
  visible_tells:
  - "Card titles ('NAD+ Injection', 'Women's Hormone Care') are only slightly larger than the 2-3 line description below, with little weight contrast"
  - "'Learn More' links read at the same weight as body copy, adding an undifferentiated level"
  confidence: high
  contrast_with: store/agelessrx-com/captures/2026-05-31/tiles/metformin/tile-00-y00000.png
- id: typography_06
  family: typography_hierarchy
  polarity: mixed
  page_or_region: about — 'Your genes are not your destiny' section
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/about/tile-03-y03660.png
  claim: "This section leans on weight alone as its only hierarchy lever — bolded inline words ('Lifespan', 'Healthspan') inside body copy, with the heading and explanatory paragraph at roughly the same size."
  visible_tells:
  - "'Lifespan' and 'Healthspan' are bolded inline without any size change, reading as emphasis rather than a true level"
  - "Section head and the paragraph below share roughly the same size, separated only by weight"
  confidence: medium
- id: typography_07
  family: typography_hierarchy
  polarity: mixed
  page_or_region: metformin — safety-information block
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/metformin/tile-05-y06100.png
  claim: "The dense safety block uses bolded inline labels ('Most common Metformin side effects', 'Note:') and same-size bullet lists as its only structure, giving the section a flat, document-like density."
  visible_tells:
  - "Bolded inline lead-ins sit within running paragraphs with no size distinction from body text"
  - "Side-effect bullet lists share the body type size, leaving the long block visually dense"
  confidence: high
- id: typography_08
  family: typography_hierarchy
  polarity: poor
  page_or_region: about — 'Letter from our co-founder'
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/about/tile-02-y02440.png
  claim: "The founder letter is a wall of near-uniform body text under one heading, with a single bolded mission sentence as the only internal break — minimal scannable structure for its length."
  visible_tells:
  - "Heading 'Letter from our co-founder' sits above paragraphs that are all the same small body size"
  - "Only one bolded sentence mid-block; no subheads, pull quotes, or size breaks to skim by"
  confidence: high
- id: typography_09
  family: typography_hierarchy
  polarity: poor
  page_or_region: homepage — footer column headers vs links
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/homepage/tile-03-y03024.png
  claim: "Footer column headers ('Treatments', 'Product Science', 'Learn', 'Contact') are only marginally heavier than the teal links beneath them, with no spacing or rule to reinforce the column structure — parseable but barely."
  visible_tells:
  - "White headers sit just slightly heavier than the teal link text below, with negligible size difference"
  - "No divider, rule, or extra spacing separates header from link list beyond the small weight shift"
  confidence: medium
- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: treatments — 3-column product card grid
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/treatments/tile-00-y00000.png
  claim: "The 3-column product grid holds consistent internal structure — image zone, title, body, and 'Learn More' align reliably across cards with uniform borders and rounded corners."
  visible_tells:
  - "Top-row cards (NAD+ Injection, Women's Hormone Care, Microdosing GLP-1) share image height, title position, body start-point, and CTA placement"
  - "Card borders and corner radius are uniform across the grid"
  confidence: high
- id: layout_02
  family: layout_composition_components
  polarity: mixed
  page_or_region: treatments — promotional card injected mid-grid
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/treatments/tile-00-y00000.png
  claim: "A dark-teal 'Not sure what product is right for you?' CTA card occupies the center cell of row 2, flanked by standard product cards, and runs taller than its neighbors — an uneven break in the otherwise uniform grid."
  visible_tells:
  - "Dark teal card sits in the exact center cell of row 2, between Sermorelin (left) and PT-141 (right)"
  - "Its longer copy and 'Get started' button make it taller than the flanking product cards, leaving the row uneven"
  confidence: high
- id: layout_03
  family: layout_composition_components
  polarity: strong
  page_or_region: treatments — left filter sidebar + main grid
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/treatments/tile-00-y00000.png
  claim: "A clean two-column document structure pairs a narrow left filter rail with the wide product grid; the 'By Need' and 'By Treatment Type' checkbox lists are consistently sized and spaced, and the rail width holds across the tile."
  visible_tells:
  - "Filter checkboxes use identical label sizing and line spacing across both filter groups"
  - "Left-column width stays constant relative to the grid down the full tile"
  confidence: high
- id: layout_04
  family: layout_composition_components
  polarity: strong
  page_or_region: homepage — 3-column value-prop strip
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/homepage/tile-02-y02440.png
  claim: "The three-column icon + heading + body strip ('Simple online assessments / Fast, free shipping / Ongoing support') is evenly spaced with equal column widths, matched icon sizing, and centered alignment — one of the cleaner sections on the site."
  visible_tells:
  - "Icons sit at identical vertical positions within each of the three columns"
  - "Body text is centered and each column terminates at roughly the same depth"
  confidence: high
- id: layout_05
  family: layout_composition_components
  polarity: mixed
  page_or_region: homepage — testimonials row ('Real people, real results')
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/homepage/tile-02-y02440.png
  claim: "The three testimonial columns are structurally consistent but the right quote ('Jeff') is far shorter than the others, leaving a visible vertical gap with no card fill or border to equalize the columns."
  visible_tells:
  - "Left and center columns carry multi-sentence quotes; the right column is a single short sentence"
  - "No card background or border is used to balance the unequal column heights"
  confidence: high
- id: layout_06
  family: layout_composition_components
  polarity: strong
  page_or_region: homepage — hero composition
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/homepage/tile-00-y00000.png
  claim: "The hero is tightly composed on one center axis: headline, one-line subhead, single amber CTA, a row of four equal category cards, and a Trustpilot badge — clear top-to-bottom order with no clutter."
  visible_tells:
  - "Four category cards (Live healthier longer, Manage weight, Support heart health, Boost energy) sit in one even row, equal widths, matched rounded crop"
  - "CTA, headline, and subhead are all center-aligned on the same axis"
  confidence: high
- id: layout_07
  family: layout_composition_components
  polarity: mixed
  page_or_region: homepage — stat row ('Treatments you can feel, backed by science')
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/homepage/tile-01-y01220.png
  claim: "The stat split (82.7% / 30+ / 5,200+ text block left, product photo right) crams stats, body, and a fine-print disclaimer into a dense left column while the right image side sits in generous empty space — an unbalanced split."
  visible_tells:
  - "Stats, body paragraph, and asterisked disclaimer stack tightly in the left half with little vertical breathing room"
  - "Right side is a single product image with large empty space above and below it"
  confidence: medium
- id: layout_08
  family: layout_composition_components
  polarity: strong
  page_or_region: footer — consistent across all captured pages
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/homepage/tile-03-y03024.png
  claim: "The four-column footer (Treatments / Product Science / Learn / Contact) is identically structured and column-aligned across every page captured — a reliable shared component with no collisions or mis-stacking."
  visible_tells:
  - "Column headers and link lists hold the same x-positions across homepage, about, and metformin footer tiles"
  - "Social icons, address, and legal row keep an identical layout in every captured footer"
  confidence: high
  contrast_with: store/agelessrx-com/captures/2026-05-31/tiles/about/tile-06-y06536.png
- id: layout_09
  family: layout_composition_components
  polarity: strong
  page_or_region: metformin — product hero split layout
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/metformin/tile-00-y00000.png
  claim: "The product hero is a clean 50/50 split — oversized bottle photo left, structured info card right — with the card's pill badge, price, compare-aside callout, and full-width CTA each well separated by padding."
  visible_tells:
  - "Right card holds clearly delineated tiers (name, pill badge, description, price, compare callout box, CTA) with visible padding between each"
  - "Bottle photo fills the left half with generous top/bottom breathing room on a pale-blue field"
  confidence: high
- id: layout_10
  family: layout_composition_components
  polarity: mixed
  page_or_region: metformin — 'How it works' + pricing card density shift
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/metformin/tile-03-y03660.png
  claim: "The 'How it works' icons render notably smaller than the homepage equivalent and the heading sits top-left while content is centered; below, the generously padded 'Quarterly' pricing card abuts a dense small-type disclaimer row, creating a jarring density change with no transition."
  visible_tells:
  - "Icons here are visibly smaller than the homepage triptych, and 'How it works' is left-aligned over centered content"
  - "Padded pricing card sits directly above a cramped row of small icon + fine-print blocks with no spacing break"
  confidence: medium
  contrast_with: store/agelessrx-com/captures/2026-05-31/tiles/homepage/tile-02-y02440.png
- id: layout_11
  family: layout_composition_components
  polarity: poor
  page_or_region: bioage_test — 'Which BioAge test is right for you?' comparison table
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/bioage_test/tile-01-y01220.png
  claim: "In the BioAge comparison table the Accuracy, Emailed Results, Portal Access, and Level of Detail rows show broken-image placeholders (alt-text stubs like 'st:st:' / 'st:fi') instead of icons or checkmarks — a visible render failure in a core decision-support component."
  visible_tells:
  - "Multiple cells display broken-image boxes with 'st:' alt-text artifacts instead of icons"
  - "'Emailed Results' and 'Portal Access' rows show empty broken-image slots across all three columns, while text rows render fine"
  confidence: high
- id: layout_12
  family: layout_composition_components
  polarity: strong
  page_or_region: bioage_test — test-type category cards
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/bioage_test/tile-00-y00000.png
  claim: "The three test-type cards (At-Home Saliva, Lab-Based Blood, Online Calculator) share a clean layout — image zone, title, body, price — with uniform card height and corner radius, more polished than the general catalog grid."
  visible_tells:
  - "All three cards hold identical image zones and proportions"
  - "Price lines ('Starting at $170 / $75 / FREE') land at matching vertical positions near each card bottom"
  confidence: high
  contrast_with: store/agelessrx-com/captures/2026-05-31/tiles/treatments/tile-00-y00000.png
- id: layout_13
  family: layout_composition_components
  polarity: mixed
  page_or_region: about — expert headshots carousel
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/about/tile-01-y01220.png
  claim: "The 'Meet our experts' carousel shows four headshot cards with a visible left chevron, but the rightmost card clips at the tile edge with no right chevron shown — the scroll affordance reads incomplete in the static capture."
  visible_tells:
  - "Four headshot cards with a left '<' chevron; no matching right '>' chevron visible"
  - "Rightmost card clips at the tile boundary, signaling more content that the static layout doesn't surface"
  confidence: medium
- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: site-wide — deep teal as the dominant brand color
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/homepage/tile-00-y00000.png
  claim: "A deep teal is applied with discipline as the single dominant brand color — the hero band, nav bar, and category-card arrows all share it on the homepage, and interior pages reuse the same teal hero fill, confirming it as a structural token rather than an editorial choice."
  visible_tells:
  - "Full-width teal hero band behind the category cards plus a teal nav bar at top"
  - "Category card arrows are teal; the bioage_test interior hero uses the identical teal fill"
  confidence: high
  contrast_with: store/agelessrx-com/captures/2026-05-31/tiles/bioage_test/tile-00-y00000.png
- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: site-wide — amber accent reserved for primary CTAs
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/homepage/tile-00-y00000.png
  claim: "A warm amber-orange is used as a single accent reserved for primary CTA buttons ('Explore all Treatments', 'Take the quiz', 'See the science', 'Start online visit'), recurring across pages at a consistent hue and never appearing decoratively — a defined token."
  visible_tells:
  - "'Explore all Treatments' is the only amber element in the hero tile"
  - "The same amber button shape and hue recur as 'Take the quiz' / 'See the science' in teal sections elsewhere"
  confidence: high
  contrast_with: store/agelessrx-com/captures/2026-05-31/tiles/homepage/tile-02-y02440.png
- id: color_03
  family: color_brand_imagery
  polarity: strong
  page_or_region: about — three-value section background structure
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/about/tile-02-y02440.png
  claim: "Sections alternate among white/off-white, a pale blue-grey tint, and deep teal fills — a controlled three-value color structure that recurs across pages as the primary section-separation device."
  visible_tells:
  - "Pale blue-grey field behind the value-prop section, deep teal fill on the CTA panel, lighter tinted footer band"
  - "All three background values appear within a single scroll"
  confidence: high
- id: color_04
  family: color_brand_imagery
  polarity: mixed
  page_or_region: treatments — magenta 'NEW' badge outside the palette
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/treatments/tile-00-y00000.png
  claim: "The 'NEW' product badge uses a hot-pink/magenta that sits outside the teal+amber system, acting as an unintegrated third accent."
  visible_tells:
  - "Magenta 'NEW' pill-badge on multiple cards in this tile"
  - "No other magenta element appears in the surrounding palette"
  confidence: high
- id: color_05
  family: color_brand_imagery
  polarity: mixed
  page_or_region: about — lifestyle people photography (stock register)
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/about/tile-00-y00000.png
  claim: "The people photography (smiling woman outdoors, circular crop) is clean and aspirational but reads as stock — no distinctive lighting signature, setting, or color grade marks it as owned imagery."
  visible_tells:
  - "Circular-cropped portrait of a smiling woman on a light background in the mid-section"
  - "No identifiable lighting, setting, or grade that differentiates it from category-default stock"
  confidence: medium
  contrast_with: store/agelessrx-com/captures/2026-05-31/tiles/about/tile-03-y03660.png
- id: color_06
  family: color_brand_imagery
  polarity: poor
  page_or_region: metformin — off-palette lavender-field photograph
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/metformin/tile-01-y01220.png
  claim: "A purple lavender-field photograph illustrating Metformin's plant origin introduces a purple-dominant image unrelated to the teal/amber palette, with no art direction tying it back to the brand."
  visible_tells:
  - "Purple flowering-plant photo fills the right of the 'Background and history' section"
  - "Its color temperature and subject are unrelated to the amber/teal system used elsewhere"
  confidence: high
  contrast_with: store/agelessrx-com/captures/2026-05-31/tiles/metformin/tile-00-y00000.png
- id: color_07
  family: color_brand_imagery
  polarity: mixed
  page_or_region: bioage_test — comparison-section editorial photos
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/bioage_test/tile-02-y02440.png
  claim: "The two photos in the Methylation-vs-Phenotypic comparison (cool blue DNA close-up, warm elderly-hands shot) differ in color temperature and mood, reading as separate stock sources rather than a curated shoot."
  visible_tells:
  - "DNA-strand image carries a cool blue cast; the clasped-hands image carries a warm tone"
  - "The two sit side by side with no grading bridge between them"
  confidence: medium
- id: color_08
  family: color_brand_imagery
  polarity: mixed
  page_or_region: metformin — gold DNA image as palette nod on teal
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/metformin/tile-02-y02440.png
  claim: "A gold/amber-toned DNA-strand photo on the teal 'science of Metformin' band reads as an intentional palette nod (amber rhymes with the CTA hue) but is a repurposed stock image, not commissioned."
  visible_tells:
  - "Warm golden DNA close-up on a teal field, its amber tone echoing the CTA color"
  - "Generic scientific-stock quality with no brand-specific differentiation"
  confidence: medium
- id: color_09
  family: color_brand_imagery
  polarity: mixed
  page_or_region: metformin — pink stat icons outside the brand palette
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/metformin/tile-02-y02440.png
  claim: "The four statistics-row icons (line chart, droplet-with-plus, apple, declining bar chart) are drawn in a pink/salmon outline that matches neither the teal nor the amber token, leaving them detached from the brand palette."
  visible_tells:
  - "Apple and droplet icons render in pink/salmon stroke above the stat percentages"
  - "No teal or amber is applied to any icon in the row"
  confidence: high
- id: iconography_01
  family: iconography_illustration
  polarity: mixed
  page_or_region: site-wide — outline process-icon set (clipboard / box / chat)
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/homepage/tile-02-y02440.png
  claim: "The three-step process icons (clipboard-with-check, shipping box, speech bubble) are a matched thin-outline set reused verbatim on the metformin 'How it works' row — consistent across pages, but generic library shapes with no distinctive twist and a limited depth that doesn't extend beyond a small stock set."
  visible_tells:
  - "Outline-only icons at equal size with a shared stroke weight, stacked above labels"
  - "The same clipboard / box / speech-bubble trio reappears on the metformin page at matching scale and color"
  confidence: high
  contrast_with: store/agelessrx-com/captures/2026-05-31/tiles/metformin/tile-03-y03660.png
- id: iconography_02
  family: iconography_illustration
  polarity: mixed
  page_or_region: metformin — stat icons use off-brand health clichés
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/metformin/tile-02-y02440.png
  claim: "The four statistics icons share the thin-outline style of the process set but lean on generic health-app tropes (an apple for 'appetite control', a droplet) that read as clichés for a clinical longevity product, and are arranged at identical size/spacing — templated rather than composed."
  visible_tells:
  - "Apple icon used for appetite control; droplet-with-plus for blood sugar — stock health-app shapes"
  - "All four icons sit at identical size and spacing, evenly templated"
  confidence: high
- id: iconography_03
  family: iconography_illustration
  polarity: strong
  page_or_region: treatments + metformin — own-brand product photography system
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/treatments/tile-00-y00000.png
  claim: "Own-brand product renders share a tight system — amber-glass bottles with teal caps and a white label (teal footer band, agelessrx wordmark), all on the same pale powder-blue card with matched lighting and shadow — and the metformin hero shot extends the identical system, giving the catalog catalog-level cohesion."
  visible_tells:
  - "Amber bottle + teal cap + white label repeated across 10+ catalog cards on one pale-blue background"
  - "The enlarged metformin hero bottle uses the same pale-blue field, label system, and lighting direction"
  confidence: high
  contrast_with: store/agelessrx-com/captures/2026-05-31/tiles/treatments/tile-03-y03660.png
- id: iconography_04
  family: iconography_illustration
  polarity: mixed
  page_or_region: treatments — third-party packaging breaks the product system
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/treatments/tile-03-y03660.png
  claim: "Third-party products (Galleri, Wegovy box, Metagenics) drop into the same card template but their real retail packaging — multicolor logos, foreign palettes — visibly breaks the amber/teal/pale-blue language the own-brand bottles establish."
  visible_tells:
  - "Galleri box shows a multicolor butterfly-style logo on white packaging, unlike the amber-cap bottles"
  - "Wegovy/Metagenics appear as full-color retail packs in the same card slot, visually dissonant"
  confidence: high
  contrast_with: store/agelessrx-com/captures/2026-05-31/tiles/treatments/tile-00-y00000.png
- id: iconography_05
  family: iconography_illustration
  polarity: strong
  page_or_region: about — 'Now vs Future' healthspan bar chart
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/about/tile-01-y01220.png
  claim: "The 'Now vs Future' healthspan bar chart is a custom-composed diagram in brand teal and the site's type — segmented horizontal bars with clean labels and no chart junk — above-average data-illustration craft for the category."
  visible_tells:
  - "Segmented horizontal bars in teal/salmon/grey using the brand palette"
  - "Labels ('Now', 'Future', '80 years', '100+ years') set in the site sans, no gridlines or axis ticks"
  confidence: high
- id: iconography_06
  family: iconography_illustration
  polarity: strong
  page_or_region: about — biological-vs-chronological scatter plot
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/about/tile-03-y03660.png
  claim: "The biological-vs-chronological-age scatter plot is a custom data illustration — color-coded dot cloud on clean labeled axes, floated on a white card over a blurred landscape — a deliberate editorial presentation, not a spreadsheet export."
  visible_tells:
  - "Multi-color dot cloud (orange/green/grey) on clean axes with minimal labeling"
  - "Axis labels ('Biological age', 'Chronological age') typeset in the brand font on a card floated over a scenic photo"
  confidence: high
- id: iconography_07
  family: iconography_illustration
  polarity: strong
  page_or_region: about — '70% factors we can control' donut
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/about/tile-03-y03660.png
  claim: "The '70% factors we can control' donut is a well-composed data callout — large white bold '70%' inside a teal/white arc against a dark microscopy background — working as both data and visual anchor."
  visible_tells:
  - "Partial donut arc in white/teal over a dark purple-blue micrograph"
  - "'70%' in large bold white numerals centered in the arc, with a small '30% genetics' label outside it"
  confidence: high
- id: iconography_08
  family: iconography_illustration
  polarity: strong
  page_or_region: bioage_test — 'Tracking your BioAge over time' line chart
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/bioage_test/tile-02-y02440.png
  claim: "The BioAge tracking chart is a custom illustration: two diverging line paths (Calendar Age vs Biological Age) with numbered teal node circles across 2022-2024 year columns and a '?' future node — compositionally clear and on-brand."
  visible_tells:
  - "Solid and dashed teal line paths diverging rightward with numbered nodes (40, 41, 42) in teal-outlined circles"
  - "'Calendar Age' / 'Biological Age' labels in the brand type, with a '?' node marking the future state"
  confidence: high
- id: iconography_09
  family: iconography_illustration
  polarity: poor
  page_or_region: about — partner / advocacy logo strip (un-normalized)
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/about/tile-06-y06536.png
  claim: "The six partner logos sit in a loose 3+3 grid with no normalization — 'FIGHT AGING!' is a heavy dark-filled slab box dominating its row while neighbors are lightweight wordmarks, and the set mixes text-only marks, icon lockups, and a detailed seal at unequal sizes with no common plate, padding, or grayscale treatment."
  visible_tells:
  - "'FIGHT AGING!' renders as a heavy dark box at far greater visual weight than the surrounding wordmarks"
  - "SENS, Age Reversal Network (plain serif), Betterhumans, and the Alliance seal all sit at different sizes/styles with no unifying treatment"
  confidence: high
```

## Provenance

Tiles read: homepage (4) + treatments (8) + about (7) + bioage_test (4) + metformin (7) from `captures/2026-05-31/tiles/` — **30 native tiles, all active, no exclusions, no Tier-B re-render**. The cached Firecrawl capture rendered statically correct (no grey/WebGL hero, black media, lazy-load gaps, or unsettled count-ups), so Tier-A native crops sufficed; `qa_status: clean`. The `2026-06-03` and `2026-06-04` captures hold a deep product-catalog crawl with no homepage, so the system-bearing `2026-05-31` set was tiled (the `--capture` date was pinned, since the auto-newest default would otherwise pick the homepage-less `2026-06-03`).

Mining: blind fan-out — **4 Sonnet family miners → Opus judge**. Of 59 raw mined cards the judge accepted 41 (merging cross-family duplicates and dropping two cards factually falsified by the tiles). One accepted card was then **dropped in the post-judge structural spot-check**: a homepage typography card praised the "You're investing in movement / in clarity / in presence…" copy-stack as deliberate weight rhythm, but that band is a **scroll-driven animation captured mid-reveal** (one line highlighted, the rest fading by opacity) — an animation frame, not a stable design tell. Its tile (`homepage/tile-00`) is otherwise clean and stays cited by other cards, so no tile was excluded and `qa_status` remains `clean`. **40 cards ship** — 9 typography, 13 layout, 9 color, 9 iconography; 19 strong / 16 mixed / 5 poor.

Run provenance: generated from **Claude Code on macOS with Claude Opus 4.8 (1M context)** on 2026-06-16, from the active tiles only — no `profile.md`, dossier, Notion, or live web was consulted (the read is blind by construction). Snapshot caveat: reflects the 2026-05-31 capture; the live site changes.
