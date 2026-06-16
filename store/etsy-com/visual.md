---
schema_version: "1.0"
domain: etsy.com
captured_at: 2026-06-16
source_capture: 2026-05-31
qa_status: clean
---

## Visual & brand impression

Etsy's editorial pages carry real craft — confident serif/sans hierarchy on the press fact-grid, About hero, and impact stat block [typography_01][typography_02][typography_05]; disciplined repeating components (uniform tile rows, a sticky sell sub-nav, an identical global footer) [layout_02][layout_09][layout_15]; an owned navy/orange palette whose torn-paper motif bookends the sell page [color_01][color_02]; and bespoke folk-art and terracotta-hand illustration where Etsy invests [iconography_01][iconography_02][iconography_03]. But coherence frays: commerce surfaces compress hierarchy into dense same-size text [typography_09], real photography is un-art-directed [color_04][color_07], campaign color drifts off-palette [color_05], and four-plus illustration styles and disconnected icon sets run with no unifying logic [iconography_06][iconography_09]. Controlled where it owns the art; inconsistent where the marketplace meets many teams.

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: press / 3x2 fact grid
  tile_path: store/etsy-com/captures/2026-05-31/tiles/press/tile-01-y01220.png
  claim: The press fact-grid runs a deliberate three-level scale — large serif display numerals ('2005', '~2,400', '8.7M', '$11.9B'), small lighter all-caps labels beneath, and an even-smaller italic footnote at the bottom — a fully legible hierarchy with no body copy.
  visible_tells:
  - Large serif numerals dominate each cell
  - Sub-labels ('Founded', 'Employees', 'Active sellers') are visibly smaller and lighter than the numeral
  - Italic footnote disclaimer ('As of December 31, 2025...') is a distinct third, subordinate size
  confidence: high
- id: typography_02
  family: typography_hierarchy
  polarity: strong
  page_or_region: about / hero
  tile_path: store/etsy-com/captures/2026-05-31/tiles/about/tile-00-y00000.png
  claim: The About hero stacks a large serif headline ('Keep Commerce Human') clearly above comfortable sans body paragraphs, with inline underlined links forming a fourth register — a cleanly layered hierarchy.
  visible_tells:
  - Serif headline is substantially larger than the adjacent body paragraphs
  - Body copy reads as a separate, comfortable smaller size
  - Underlined inline links ('universe of special', 'community of sellers') form a distinct register within the body
  confidence: high
- id: typography_03
  family: typography_hierarchy
  polarity: strong
  page_or_region: sell / FAQ section
  tile_path: store/etsy-com/captures/2026-05-31/tiles/sell/tile-07-y08540.png
  claim: The FAQ holds a clean two-level hierarchy — question headings are visibly larger and darker than the answer paragraphs below them — without leaning on color or decoration.
  visible_tells:
  - Question lines ('How do fees work on Etsy?') are set larger and heavier than the answer body
  - Consistent spacing below each question before its answer reinforces the separation
  confidence: high
  contrast_with: store/etsy-com/captures/2026-05-31/tiles/sell/tile-02-y02440.png
- id: typography_04
  family: typography_hierarchy
  polarity: strong
  page_or_region: sell / tools section ('Simple, powerful tools')
  tile_path: store/etsy-com/captures/2026-05-31/tiles/sell/tile-03-y03660.png
  claim: The tools section runs a clean three-tier structure — large section heading, bold sub-feature label ('Manage your business anywhere', 'Save big on shipping'), regular descriptor beneath — with a clear size/weight jump at each level.
  visible_tells:
  - Bold sub-labels are distinctly heavier than their descriptor paragraphs
  - Section heading 'Simple, powerful tools' is larger still, forming a clear primary level
  confidence: high
- id: typography_05
  family: typography_hierarchy
  polarity: strong
  page_or_region: impact / dark-olive stat block ('We're more than a place to shop')
  tile_path: store/etsy-com/captures/2026-05-31/tiles/impact/tile-02-y02440.png
  claim: The dark-green impact stat block sets a large centered serif headline above three icon-label-descriptor triads, and within each triad the bold label sits above lighter paragraph text — a consistent three-level hierarchy across all columns.
  visible_tells:
  - Serif headline ('We're more than a place to shop. We're a community doing good.') is set largest
  - Stat labels ('A more inclusive place to work') are visibly bolder than the paragraph text below them
  confidence: high
- id: typography_06
  family: typography_hierarchy
  polarity: mixed
  page_or_region: sell / fee list ('Simple & secure')
  tile_path: store/etsy-com/captures/2026-05-31/tiles/sell/tile-02-y02440.png
  claim: Each fee row sets the fee name (e.g. '$0.20 Listing fee') only marginally larger than its descriptor line, so the two levels read as nearly the same weight — the per-row hierarchy is thin to scan.
  visible_tells:
  - Fee label and descriptor body are rendered at sizes that barely differ
  - Weight difference between fee name and descriptor is marginal, not a clear jump
  confidence: medium
- id: typography_07
  family: typography_hierarchy
  polarity: mixed
  page_or_region: homepage / section headers vs. card labels
  tile_path: store/etsy-com/captures/2026-05-31/tiles/homepage/tile-01-y01220.png
  claim: Section headers like 'Etsy-special gifts for Father's Day' and 'Shop our most-loved categories' sit only modestly larger than the category labels beneath the thumbnails, compressing the contrast between navigation-level and item-level text.
  visible_tells:
  - Section header is not dramatically larger than category labels ('Personalized Gifts for Dad', 'Graduation Gifts')
  - Heading and label levels blur on a fast scan
  confidence: medium
  contrast_with: store/etsy-com/captures/2026-05-31/tiles/press/tile-01-y01220.png
- id: typography_08
  family: typography_hierarchy
  polarity: mixed
  page_or_region: homepage & sell heroes / understated headline
  tile_path: store/etsy-com/captures/2026-05-31/tiles/homepage/tile-00-y00000.png
  claim: 'Both lead heroes set a legible but conservatively sized headline that reads as a mid-size callout rather than a commanding display statement: the homepage ''How to: Plan the best Father''s Day yet'' is no larger than the adjacent promo card, and the sell hero ''Millions of shoppers can''t wait...'' is plain medium-weight sans close to the nav-link weight.'
  visible_tells:
  - Homepage headline sits at modest display size and the right-side promo card uses a similar size, reading as two co-equal heroes rather than a clear primary/secondary
  - Sell hero headline (white, centered) has no distinctive weight or size anchor
  confidence: medium
  contrast_with: store/etsy-com/captures/2026-05-31/tiles/sell/tile-00-y00000.png
- id: typography_09
  family: typography_hierarchy
  polarity: poor
  page_or_region: homepage / product card grid ('Today's big deals')
  tile_path: store/etsy-com/captures/2026-05-31/tiles/homepage/tile-02-y02440.png
  claim: Inside each deal card the shop name, truncated title, price, crossed-out original price, discount badge and rating all sit at very small near-identical sizes, producing a dense cluster of same-weight text with no clear reading order.
  visible_tells:
  - Product title, price and discount text all compete at similar small sizes in the card footer
  - Green percentage badge and price stack are not visually differentiated from the product name above
  confidence: high
- id: typography_10
  family: typography_hierarchy
  polarity: poor
  page_or_region: footer / link columns (sell & about)
  tile_path: store/etsy-com/captures/2026-05-31/tiles/sell/tile-08-y09760.png
  claim: The footer column headers ('Shop', 'Sell', 'About', 'Help') carry only a faint weight bump over the links beneath them, so the footer reads as a near-undifferentiated list.
  visible_tells:
  - Column headers and sub-links share nearly the same small size
  - No uppercase, rule, or size step sets 'Shop' apart from 'Gift cards' beneath it
  confidence: medium
  contrast_with: store/etsy-com/captures/2026-05-31/tiles/press/tile-01-y01220.png
- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: homepage / hero two-column split
  tile_path: store/etsy-com/captures/2026-05-31/tiles/homepage/tile-00-y00000.png
  claim: The hero is a clean two-column split — teal editorial card left, product-photo card right — sharing top and bottom edges with an even gutter that matches the outer page margins.
  visible_tells:
  - Left and right cards share the same top and bottom edges
  - Gutter between them reads even and matches the page margins
  confidence: high
- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: homepage / uniform category & discount rows
  tile_path: store/etsy-com/captures/2026-05-31/tiles/homepage/tile-00-y00000.png
  claim: Recurring tile rows on the homepage (the four-up 'Jump into featured interests' row, the five-up 'Save now on standout styles' strip) hold uniform crops, equal gutters, and captions anchored at the same baseline beneath each tile.
  visible_tells:
  - All tiles in a row share identical width and height
  - Caption text sits at the same vertical offset below each tile
  confidence: high
  contrast_with: store/etsy-com/captures/2026-05-31/tiles/homepage/tile-03-y03660.png
- id: layout_03
  family: layout_composition_components
  polarity: mixed
  page_or_region: homepage / 'Etsy-special gifts' mixed-grid band
  tile_path: store/etsy-com/captures/2026-05-31/tiles/homepage/tile-01-y01220.png
  claim: Within one scroll band the page stacks three structurally different grids — a 3-up editorial card layout, a 6-up product thumbnail row, and a 5-up icon-label strip — with no visual buffer between them, creating rhythm choppiness.
  visible_tells:
  - 3-up promo cards run at roughly 2:3 aspect ratio
  - Directly below, a row of ~6 product thumbnails at different proportions
  - Then a 5-column icon-label strip — three distinct grid densities in one viewport
  confidence: high
- id: layout_04
  family: layout_composition_components
  polarity: strong
  page_or_region: homepage / 'Today's big deals' product grid
  tile_path: store/etsy-com/captures/2026-05-31/tiles/homepage/tile-02-y02440.png
  claim: The deals product grid uses consistent card sizing, with wishlist hearts, discount badges, and the price/strikethrough stack placed at identical offsets across every card — a mature component spec.
  visible_tells:
  - Wishlist heart appears in the same top-right corner of every card
  - Price text and strikethrough align to the same left edge across all cards
  confidence: high
- id: layout_05
  family: layout_composition_components
  polarity: mixed
  page_or_region: homepage / 'Find something special' mosaic
  tile_path: store/etsy-com/captures/2026-05-31/tiles/homepage/tile-03-y03660.png
  claim: The three editorial mosaic images sit at noticeably different heights with no shared top or bottom edge, so the section reads ad-hoc rather than composed to a baseline.
  visible_tells:
  - Left image is taller than the center, which is taller than the right
  - No shared top or bottom edge across the three images
  confidence: medium
- id: layout_06
  family: layout_composition_components
  polarity: strong
  page_or_region: homepage / 'Fresh from the blog' 3-up card row
  tile_path: store/etsy-com/captures/2026-05-31/tiles/homepage/tile-04-y04880.png
  claim: The three blog cards share identical image aspect ratios, a consistent 'Featured Shop' label placement, headline size, and body text, indicating a disciplined card component with no per-card overrides.
  visible_tells:
  - '''Featured Shop'' label sits at the same position above the headline in all three cards'
  - Headline and body align to a shared left margin across all three
  confidence: high
- id: layout_07
  family: layout_composition_components
  polarity: mixed
  page_or_region: homepage / 'Explore small shops' band
  tile_path: store/etsy-com/captures/2026-05-31/tiles/homepage/tile-04-y04880.png
  claim: The 'Explore small shops' block places a left text/button cluster and a 3-column shop thumbnail row in the same band with no shared baseline or column grid connecting them, leaving the pairing compositionally unresolved.
  visible_tells:
  - Text/button sits left while thumbnails sit right with no shared baseline
  - No obvious column grid ties the text block to the images
  confidence: medium
- id: layout_08
  family: layout_composition_components
  polarity: strong
  page_or_region: sell / hero (distinct compositional mode)
  tile_path: store/etsy-com/captures/2026-05-31/tiles/sell/tile-00-y00000.png
  claim: The sell hero switches to a full-bleed dark illustrated background with a centered text block and single CTA — a deliberate compositional mode distinct from the homepage's card grids, not an accident.
  visible_tells:
  - Geometric blob shapes bleed to all four edges with a torn-paper lower edge
  - Headline and 'Get started' CTA are center-aligned in the viewport
  confidence: high
- id: layout_09
  family: layout_composition_components
  polarity: strong
  page_or_region: sell / sticky sub-navigation
  tile_path: store/etsy-com/captures/2026-05-31/tiles/sell/tile-01-y01220.png
  claim: A persistent section sub-nav (Fees / Tools / Support / Stories / Selling / FAQ) with a right-aligned pill CTA sits at a fixed viewport position across multiple sell-page tiles — a coherent sticky-nav component used consistently down the page.
  visible_tells:
  - Identical sub-nav bar appears at the same viewport position across sell tiles 01-08
  - Pill CTA 'Open your Etsy Shop' is right-aligned in every instance
  confidence: high
  contrast_with: store/etsy-com/captures/2026-05-31/tiles/sell/tile-07-y08540.png
- id: layout_10
  family: layout_composition_components
  polarity: strong
  page_or_region: sell / 3-column value props & fee rows
  tile_path: store/etsy-com/captures/2026-05-31/tiles/sell/tile-01-y01220.png
  claim: The three-column value-prop block (Great value / Powerful tools / Support and education) is equal-width with icon, heading, body, and 'Learn more' link stacked in the same sequence per column; the fee rows below repeat a clean left-anchored icon + heading + body list with even row spacing.
  visible_tells:
  - All three value-prop icons share the same circular container and size
  - Each fee row's icon badge aligns to the same left edge with an identical vertical gap between rows
  confidence: high
  contrast_with: store/etsy-com/captures/2026-05-31/tiles/sell/tile-02-y02440.png
- id: layout_11
  family: layout_composition_components
  polarity: poor
  page_or_region: sell / closing CTA before footer
  tile_path: store/etsy-com/captures/2026-05-31/tiles/sell/tile-08-y09760.png
  claim: The 'Ready to start selling?' closing section repeats the navy torn-paper hero motif but leaves a large expanse of empty dark background above the torn divider, so the CTA text and button float small in unresolved negative space.
  visible_tells:
  - Roughly a third of the tile is empty dark background above the torn-paper divider
  - CTA text and button read small relative to the large decorative ground
  confidence: high
  contrast_with: store/etsy-com/captures/2026-05-31/tiles/sell/tile-00-y00000.png
- id: layout_12
  family: layout_composition_components
  polarity: strong
  page_or_region: about / hero split layout
  tile_path: store/etsy-com/captures/2026-05-31/tiles/about/tile-00-y00000.png
  claim: The About hero is a deliberate left-illustration / right-copy split with generous whitespace above and below the content block, landing as intentionally sparse rather than incomplete.
  visible_tells:
  - Hands illustration fills the left half; body copy column sits to the right with a comfortable margin
  - Wide, even whitespace frames the content block top and bottom
  confidence: high
- id: layout_13
  family: layout_composition_components
  polarity: mixed
  page_or_region: about / 'How Etsy Works' repeating blocks
  tile_path: store/etsy-com/captures/2026-05-31/tiles/about/tile-01-y01220.png
  claim: The 'How Etsy Works' sub-sections (Buy / Sell / Secure) reuse the exact same three-overlapping-circle illustration cluster across each context, so the layout reads as templated rather than crafted per section.
  visible_tells:
  - The same three-circle illustration cluster appears in identical form across vertically adjacent sections
  - Illustration does not change with the section topic
  confidence: high
  contrast_with: store/etsy-com/captures/2026-05-31/tiles/about/tile-02-y02440.png
- id: layout_14
  family: layout_composition_components
  polarity: poor
  page_or_region: about / FAQ carousel panel
  tile_path: store/etsy-com/captures/2026-05-31/tiles/about/tile-02-y02440.png
  claim: The red FAQ carousel panel is so heavily vertically padded that the cat illustration, question, and dot indicators float in an oversized colored slab, leaving the content cluster occupying a small fraction of the panel's height.
  visible_tells:
  - Top padding above the cat illustration is roughly equal to the illustration's own height
  - Content cluster occupies well under half the red panel's height
  confidence: high
- id: layout_15
  family: layout_composition_components
  polarity: strong
  page_or_region: global footer (about & sell)
  tile_path: store/etsy-com/captures/2026-05-31/tiles/sell/tile-09-y09875.png
  claim: The global footer is structurally identical across pages — same four-column link list (Shop / Sell / About / Help), same Etsy app-download button, same social icon row, same bottom legal bar — a strongly consistent component system.
  visible_tells:
  - Four link columns with identical labels appear in the same order on every page's footer
  - Legal bar (© 2026 Etsy, Terms of Use, Privacy) sits at the same bottom-edge position on every footer
  confidence: high
  contrast_with: store/etsy-com/captures/2026-05-31/tiles/about/tile-03-y03053.png
- id: layout_16
  family: layout_composition_components
  polarity: mixed
  page_or_region: impact / hero illustration + text
  tile_path: store/etsy-com/captures/2026-05-31/tiles/impact/tile-00-y00000.png
  claim: The impact hero pairs a large folk-art tree illustration with a left-aligned text block that is narrower than half the page, while the illustration extends well past center, leaving the weight distribution imbalanced and unresolved.
  visible_tells:
  - Illustration spans roughly two-thirds of the horizontal width
  - Text block left-aligns without a strong vertical anchor to the illustration
  confidence: medium
- id: layout_17
  family: layout_composition_components
  polarity: strong
  page_or_region: press / hero full-bleed photo
  tile_path: store/etsy-com/captures/2026-05-31/tiles/press/tile-00-y00000.png
  claim: The press hero is a full-bleed editorial office photograph with a single centered white 'Press' label — a disciplined composition that avoids the busier multi-element layouts elsewhere on the site.
  visible_tells:
  - Single word 'Press' centered within the photo
  - No overlapping CTA or secondary text element
  confidence: high
- id: layout_18
  family: layout_composition_components
  polarity: strong
  page_or_region: press / 3x2 fact grid ruling
  tile_path: store/etsy-com/captures/2026-05-31/tiles/press/tile-01-y01220.png
  claim: The 3x2 company-fact grid is tightly ruled with hairline horizontal dividers, consistent cell padding, and uniform numeral/label sizing across all six cells.
  visible_tells:
  - Hairline horizontal rules separate the rows at the same weight
  - Numeral and label sizing is uniform from cell to cell
  confidence: high
- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: sell / hero palette discipline
  tile_path: store/etsy-com/captures/2026-05-31/tiles/sell/tile-00-y00000.png
  claim: The sell hero runs a controlled palette — deep navy ground, warm orange, and a muted blue/teal — applied across the geometric blob shapes and the CTA with no fourth color introduced.
  visible_tells:
  - Large irregular orange and blue/teal polygons float against a navy ground
  - No additional hue enters the frame beyond the navy/orange/blue trio
  confidence: high
  contrast_with: store/etsy-com/captures/2026-05-31/tiles/homepage/tile-00-y00000.png
- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: sell / torn-paper navy footer bookend
  tile_path: store/etsy-com/captures/2026-05-31/tiles/sell/tile-08-y09760.png
  claim: The sell footer repeats the navy torn-paper hero treatment at reduced scale, bookending the page with the same orange-and-blue blobs and torn white edge — confirming the geometric-blob/torn-edge device is a deliberate structural motif, not a one-off.
  visible_tells:
  - Same orange and blue blob shapes plus torn white paper edge appear at page bottom, echoing the hero
  - Navy ground and color proportions match the top of the page
  confidence: high
  contrast_with: store/etsy-com/captures/2026-05-31/tiles/sell/tile-00-y00000.png
- id: color_03
  family: color_brand_imagery
  polarity: strong
  page_or_region: about / high-saturation red divider section
  tile_path: store/etsy-com/captures/2026-05-31/tiles/about/tile-02-y02440.png
  claim: A full-bleed deep-red section with an orange cat illustration is used as a structural divider, showing willingness to deploy high-saturation color blocks rather than defaulting to white or light grey.
  visible_tells:
  - Deep crimson field occupies the full viewport width
  - Orange cat illustration sits on the red — an accent-on-accent pairing that reads as intentional
  confidence: high
- id: color_04
  family: color_brand_imagery
  polarity: mixed
  page_or_region: homepage / seller-sourced product photography
  tile_path: store/etsy-com/captures/2026-05-31/tiles/homepage/tile-01-y01220.png
  claim: Homepage product photography is seller-sourced and un-art-directed — inconsistent backgrounds, lighting, and crops — which dilutes the disciplined brand palette of the editorial sections.
  visible_tells:
  - Cards mix white-background studio shots with lifestyle shots over varied props and light
  - No consistent aspect ratio or color-temperature harmony across cards
  confidence: high
  contrast_with: store/etsy-com/captures/2026-05-31/tiles/sell/tile-00-y00000.png
- id: color_05
  family: color_brand_imagery
  polarity: mixed
  page_or_region: homepage / campaign hero color off-system
  tile_path: store/etsy-com/captures/2026-05-31/tiles/homepage/tile-00-y00000.png
  claim: The homepage hero uses a dark teal campaign color that matches neither the sell-page navy nor the coral/orange illustration accents, and the adjacent promo card uses an unrelated warm beige — suggesting editorial campaigns introduce ad-hoc color rather than drawing from a fixed token set.
  visible_tells:
  - Dark teal/forest field for the Father's Day banner — not navy, not the coral/orange accent
  - Adjacent promo card uses a neutral warm beige with no relationship to the teal
  confidence: medium
  contrast_with: store/etsy-com/captures/2026-05-31/tiles/sell/tile-00-y00000.png
- id: color_06
  family: color_brand_imagery
  polarity: mixed
  page_or_region: impact / 'Shop what's important' editorial photo row
  tile_path: store/etsy-com/captures/2026-05-31/tiles/impact/tile-03-y03622.png
  claim: The impact page's bottom four-up editorial photo row uses real photography with inconsistent framing and no evident color-grade unity, undercutting the polish of the custom-illustration sections above it.
  visible_tells:
  - Four thumbnails show varied color temperatures and crop styles side by side
  - Shots range from overhead still-life to environmental scenes with no shared visual logic
  confidence: medium
- id: color_07
  family: color_brand_imagery
  polarity: poor
  page_or_region: press / office photography grid color
  tile_path: store/etsy-com/captures/2026-05-31/tiles/press/tile-02-y02440.png
  claim: The press 'Brand assets' office-photo grid shows inconsistent color temperatures, exposures, and aspect ratios — warm/amber frames next to cool/blue ones, portrait crops next to landscape — reading as images shot on different occasions without a unifying art-direction brief.
  visible_tells:
  - Some thumbnails are warm/amber, others cool/blue-shifted
  - Top-row images are portrait-ish while bottom-row images are landscape; no enforced crop or grade
  confidence: high
- id: iconography_01
  family: iconography_illustration
  polarity: strong
  page_or_region: about / custom hand-illustration system
  tile_path: store/etsy-com/captures/2026-05-31/tiles/about/tile-00-y00000.png
  claim: The About hero deploys a bespoke flat illustration of two stylized hands in a terracotta/salmon duotone with radiating tick marks — purpose-built and brand-specific, clearly not stock; the same two-tone hand vocabulary repeats in the 'How Etsy Works' three-circle cluster (hammer hand, gloves, storefront door), forming a coherent owned system.
  visible_tells:
  - Two-hand illustration in coral/brick and peach skin tones with patterned cuffs and radiating ticks
  - Three overlapping circles each hold a hand-centric illustration in the same palette and line style
  - Flat texture-fill rendering matches no generic icon library
  confidence: high
  contrast_with: store/etsy-com/captures/2026-05-31/tiles/sell/tile-01-y01220.png
- id: iconography_02
  family: iconography_illustration
  polarity: strong
  page_or_region: impact / hero folk-art narrative illustration
  tile_path: store/etsy-com/captures/2026-05-31/tiles/impact/tile-00-y00000.png
  claim: The impact hero is a dense folk-art narrative illustration — a large tree, multiple human figures, bees, animals, layered flora — the most craft-intensive artwork on the site, in a polychrome palette well beyond the two-tone accents elsewhere.
  visible_tells:
  - Full-width scene with richly overlapping botanical and figurative elements
  - Multiple human figures with stylized garments and diverse skin tones
  - Deep greens, amber, coral, and blues exceed the two-tone brand accents
  confidence: high
  contrast_with: store/etsy-com/captures/2026-05-31/tiles/about/tile-01-y01220.png
- id: iconography_03
  family: iconography_illustration
  polarity: strong
  page_or_region: impact / Etsy Uplift cyclist illustration
  tile_path: store/etsy-com/captures/2026-05-31/tiles/impact/tile-02-y02440.png
  claim: A large flat illustration of a Black woman on a bicycle carrying stacked patterned packages shows confident, character-driven editorial illustration with deliberate representation and a handcrafted sketch-outline quality.
  visible_tells:
  - Full figure with braided hair, sunglasses, and polka-dot clothing in bold flat color
  - Stacked packages covered in repeating dot and stripe patterns add visual rhythm
  - Visible pencil-sketch outline gives a handmade quality
  confidence: high
- id: iconography_04
  family: iconography_illustration
  polarity: mixed
  page_or_region: sell / hero geometric-blob device
  tile_path: store/etsy-com/captures/2026-05-31/tiles/sell/tile-00-y00000.png
  claim: The sell hero relies on large flat geometric blobs (orange polygon, speckled navy oval, orange circle) plus a torn-paper edge as its decorative device — a recognizable brand element but one carried by shape and color rather than illustration craft.
  visible_tells:
  - Oversized orange irregular polygon at upper left bleeding off the edge
  - Speckled navy-blue oval at center-left
  - Torn white paper-texture edge dividing the illustrated upper half from the white below
  confidence: high
  contrast_with: store/etsy-com/captures/2026-05-31/tiles/impact/tile-00-y00000.png
- id: iconography_05
  family: iconography_illustration
  polarity: mixed
  page_or_region: sell / device-mockup line illustrations
  tile_path: store/etsy-com/captures/2026-05-31/tiles/sell/tile-03-y03660.png
  claim: The app/browser device mockups are drawn in a loose flat outline style with schematic, minimally detailed screens (dashed placeholder boxes, squiggle text) — charming but visibly lighter in craft than the about/impact illustrations.
  visible_tells:
  - Phone and tablet/desktop frames drawn in outline with flat orange/yellow UI blocks
  - Browser mockup uses dashed placeholder boxes and squiggle lines instead of real UI content
  confidence: medium
  contrast_with: store/etsy-com/captures/2026-05-31/tiles/impact/tile-02-y02440.png
- id: iconography_06
  family: iconography_illustration
  polarity: poor
  page_or_region: sell / generic UI icon sets (value-prop, fee, support)
  tile_path: store/etsy-com/captures/2026-05-31/tiles/sell/tile-01-y01220.png
  claim: 'The sell page''s functional icons read as generic library glyphs disconnected from the custom illustration system and from each other: pale blue-grey circles holding monochrome price-tag/calculator/book icons in the value-prop row, dark near-black circle badges for the fee rows, and small dark circles for the support options — three inert utilitarian sets with no shared treatment or brand color.'
  visible_tells:
  - Value-prop icons sit in flat blue-grey circles with no accent color, line style resembling default icon libraries
  - Fee rows use a run of identical flat near-black circle badges (storefront, card, megaphone, globe, lock)
  - Stroke weight, fill, and container shape differ across the value-prop, fee, and support sets
  confidence: high
  contrast_with: store/etsy-com/captures/2026-05-31/tiles/about/tile-00-y00000.png
- id: iconography_07
  family: iconography_illustration
  polarity: mixed
  page_or_region: impact / stat-band thin outline icons
  tile_path: store/etsy-com/captures/2026-05-31/tiles/impact/tile-02-y02440.png
  claim: The three white thin-stroke outline icons (people group, hand holding coin, shield with leaf) in the dark-green stat band are yet another distinct icon style — minimal, fill-free, and more generic than the rich illustration work directly above them.
  visible_tells:
  - Three small outline-only icons at equal size in the dark-green band
  - No fill, texture, or color — pure stroke, thinner than the fee badges and unlike the hand illustrations
  confidence: high
- id: iconography_08
  family: iconography_illustration
  polarity: mixed
  page_or_region: about / FAQ cartoon cat (style break)
  tile_path: store/etsy-com/captures/2026-05-31/tiles/about/tile-02-y02440.png
  claim: The chunky cartoon cat above the FAQ carousel is markedly simpler and flatter than the terracotta hand-system illustrations one section up, signaling a style break rather than a unified illustration language.
  visible_tells:
  - Cartoonish cat with minimal detail and basic flat orange fill
  - No linework or texture detail consistent with the hand illustrations above it
  confidence: high
  contrast_with: store/etsy-com/captures/2026-05-31/tiles/about/tile-01-y01220.png
- id: iconography_09
  family: iconography_illustration
  polarity: poor
  page_or_region: site-wide / illustration-system incoherence
  tile_path: store/etsy-com/captures/2026-05-31/tiles/impact/tile-00-y00000.png
  claim: Across pages at least four visually distinct illustration styles run simultaneously — folk-art narrative (impact hero), flat terracotta hands (about), cartoon mascot cat (about FAQ), and loose device line-art (sell) — with no unifying stylistic logic tying them together.
  visible_tells:
  - Polychrome folk-art tree scene cannot be reconciled with the flat two-tone terracotta hand circles
  - The cartoon orange cat has no stylistic kinship with the cyclist illustration
  - Multiple separate icon systems appear across sell, about, and impact with no shared stroke weight or fill treatment
  confidence: high
  contrast_with: store/etsy-com/captures/2026-05-31/tiles/about/tile-01-y01220.png
```

## Provenance

Tiles read: homepage (6) + sell (10) + about (4) + impact (4) + press (4) = 28 active tiles from `captures/2026-05-31/tiles/`, all cited tiles straight from the cached Firecrawl payloads — no exclusions, **no Tier-B re-render** (the capture was clean: no overlays, grey/WebGL heroes, black media, or lazy-load gaps at native resolution). The `categories` page was tiled but set aside from mining — a clean but low-signal text directory, not a contamination exclusion. Mined blind + judged per [`/visual-evidence`](../../skills/visual-evidence/SKILL.md): four family miners saw only the tile paths (no dossier, no web), the judge kept 44 of 67 raw cards (mostly cross-family / duplicate-tell merges; a handful of marginal, unverifiable layout calls pruned). Every `poor` structural card was spot-checked against its native tile — all reflect fully-rendered real content, no capture artifacts. Snapshot caveat: reflects the 2026-05-31 capture; the live site changes (e.g. the seasonal Father's Day campaign in the homepage hero).
