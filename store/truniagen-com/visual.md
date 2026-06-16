---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.0"
domain: truniagen.com
captured_at: 2026-06-16        # own freshness — when these tiles were mined
source_capture: 2026-06-16     # captures/2026-06-16/ the tiles derive from
qa_status: exclusions-noted
---

## Visual & brand impression

A disciplined navy-and-white system [color_01] that skips the generic supplement gradient and holds one two-tone identity from announcement bar through hero [color_01]. Craft peaks in the imagery: a coherent off-white product-photography system [color_03], a packaging taxonomy — navy / gold / teal / pink — legible at thumbnail [iconography_03], and custom soft-3D organ/cell illustrations [iconography_01]. Type hierarchy is clean where it counts — hero [typography_01], stat numerals [typography_02], testimonial stack [typography_05] — and layout stays grid-disciplined across product rows [layout_01], benefit cards [layout_02], and footer [layout_03]. It slips in connective tissue: mixed photo grading [color_04], a utilitarian chart [iconography_02], an inert stats bar [iconography_04], a generic amber CTA band [color_07], and a grid-orphan collections finish [layout_09].

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: "homepage hero — headline over dark navy background"
  tile_path: "store/truniagen-com/captures/2026-06-16/tiles/homepage/tile-00-y00000.png"
  claim: "The hero headline establishes a clear primary level with a large, heavy sans-serif at high contrast against the dark navy hero, and the subhead drops visibly in both size and weight, making the two-level relationship unambiguous at a glance."
  visible_tells:
    - "Headline 'The #1 NAD+ booster for the #1 Dad' is noticeably larger and heavier than the body copy beneath it"
    - "White text on dark navy gives high contrast with no legibility issues"
  confidence: high
  contrast_with: "store/truniagen-com/captures/2026-06-16/tiles/homepage/tile-03-y03660.png"
- id: typography_02
  family: typography_hierarchy
  polarity: strong
  page_or_region: "homepage — social proof / stats band ('Backed by 25+ years…')"
  tile_path: "store/truniagen-com/captures/2026-06-16/tiles/homepage/tile-01-y01220.png"
  claim: "In the stats band, large bold numerals (45+, 60+, 500+, 300+) dominate their cells while the descriptive label beneath each sits in noticeably smaller, lighter text — a deliberate size contrast doing the hierarchy work."
  visible_tells:
    - "Numerals are roughly 2–3x the cap-height of the label text below them"
    - "A medium-weight intro line bridges the heading and the stat cells"
  confidence: high
- id: typography_03
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "homepage — category card grid (Foundational / Pro / Immune / Beauty)"
  tile_path: "store/truniagen-com/captures/2026-06-16/tiles/homepage/tile-02-y02440.png"
  claim: "Category card titles ('Foundational', 'Pro') read as a level above their body copy, but the size step between title and body is modest — hierarchy functions but lacks snap."
  visible_tells:
    - "Card titles are slightly heavier than body text but the point-size differential is small"
    - "All four cards use the identical type treatment with no differentiation by importance"
  confidence: medium
- id: typography_04
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "homepage — science split section ('Every cell in your body is fueled by NAD+')"
  tile_path: "store/truniagen-com/captures/2026-06-16/tiles/homepage/tile-02-y02440.png"
  claim: "The overline label 'THE SCIENCE BEHIND NAD+' is set tiny and light above a large bold headline, so the intended third hierarchy level registers as faint decoration rather than a clear navigational tier."
  visible_tells:
    - "Overline text above the headline is visibly tiny and light, near-illegible at this scale"
    - "The headline beneath it is large and bold, dwarfing the overline's contribution"
  confidence: medium
- id: typography_05
  family: typography_hierarchy
  polarity: strong
  page_or_region: "homepage — testimonial pullquote ('It's made all the difference…')"
  tile_path: "store/truniagen-com/captures/2026-06-16/tiles/homepage/tile-06-y07320.png"
  claim: "The testimonial uses a clean three-level stack — large navy pullquote down to a small light attribution line — with generous, intentional size stepping."
  visible_tells:
    - "Pullquote text is substantially larger than the attribution line '— Iris, 70 years old, Verified Customer'"
    - "The quote-to-attribution ratio is generous, subordinating authorship without hiding it"
  confidence: high
- id: typography_06
  family: typography_hierarchy
  polarity: strong
  page_or_region: "collections page — page header"
  tile_path: "store/truniagen-com/captures/2026-06-16/tiles/collections-all/tile-00-y00000.png"
  claim: "The collections headline 'Experience the Difference with Patented, Proven NAD+ Technology' is the largest type on screen and sits clearly above the grid, giving the page a single primary entry point before products begin."
  visible_tells:
    - "Page heading is the largest type at the top of the tile, with a smaller subline beneath it"
    - "Blue color plus size distinguishes it from the smaller blue product-name labels below"
  confidence: high
- id: typography_07
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "collections page — product card grid"
  tile_path: "store/truniagen-com/captures/2026-06-16/tiles/collections-all/tile-01-y01220.png"
  claim: "Within each product card the name, variant pills, and price line are visually close in size, flattening intra-card hierarchy so the product name doesn't assert itself above the supporting metadata."
  visible_tells:
    - "Product name, variant chips, and price line occupy similar vertical weight"
    - "Strike-through original price and sale price are close in size, reducing price scannability"
  confidence: medium
  contrast_with: "store/truniagen-com/captures/2026-06-16/tiles/collections-all/tile-00-y00000.png"
- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: "homepage — product card row"
  tile_path: "store/truniagen-com/captures/2026-06-16/tiles/homepage/tile-01-y01220.png"
  claim: "The product card row runs a consistent multi-column grid with uniform card height, aligned star ratings, and matched price-block position across all visible cards — a disciplined repeating component."
  visible_tells:
    - "All visible product cards share identical image-to-text vertical rhythm"
    - "Price strings and star ratings land on the same horizontal baseline across columns"
    - "Card gutters are visually equal across the row"
  confidence: high
  contrast_with: "store/truniagen-com/captures/2026-06-16/tiles/collections-all/tile-02-y02440.png"
- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: "homepage — 'Whole-body benefits' icon-card carousel"
  tile_path: "store/truniagen-com/captures/2026-06-16/tiles/homepage/tile-04-y04880.png"
  claim: "The benefit cards (Healthy Aging, Brain, Heart, Muscle, Cellular Health) each use the same square-image-over-headline-over-body-over-link layout with uniform width and consistent spacing — a well-executed repeating tile."
  visible_tells:
    - "Illustration images are the same dimensions in each card"
    - "Headline and body text start at the same vertical position in every card"
    - "Blue 'Learn More' links align to the same baseline row"
  confidence: high
- id: layout_03
  family: layout_composition_components
  polarity: strong
  page_or_region: "homepage footer"
  tile_path: "store/truniagen-com/captures/2026-06-16/tiles/homepage/tile-06-y07320.png"
  claim: "The footer deploys a clean five-column link grid (Products, About Us, Resources, Support, Social) with consistent column widths, uniform left-aligned type, and a clearly delimited email-signup row above it."
  visible_tells:
    - "Five column headers are horizontally distributed at even intervals"
    - "Link items within each column share consistent line-height without crowding"
    - "The 'Join our community' email + CTA row above is separated by whitespace and a rule"
  confidence: high
- id: layout_04
  family: layout_composition_components
  polarity: strong
  page_or_region: "collections page — product grid"
  tile_path: "store/truniagen-com/captures/2026-06-16/tiles/collections-all/tile-00-y00000.png"
  claim: "The collections grid holds a consistent four-column layout with equal gutters, uniformly sized product images, and aligned text blocks below each image across both visible rows."
  visible_tells:
    - "Product images occupy identical bounding boxes in every cell"
    - "Name, variant pills, and price appear in the same stacking order per card"
    - "Column gutters are visually equal across all four columns"
  confidence: high
  contrast_with: "store/truniagen-com/captures/2026-06-16/tiles/collections-all/tile-02-y02440.png"
- id: layout_05
  family: layout_composition_components
  polarity: mixed
  page_or_region: "homepage hero — right-side photo collage"
  tile_path: "store/truniagen-com/captures/2026-06-16/tiles/homepage/tile-00-y00000.png"
  claim: "The hero pairs a cleanly left-aligned text/CTA block with an informal Polaroid photo cluster on the right whose irregular angles and front-placed product bottle sit in mild tension with the structured grid below."
  visible_tells:
    - "Text and CTA are cleanly left-aligned on the dark field"
    - "The polaroid photo cluster on the right has no clear grid anchor — images overlap at irregular angles"
    - "The product bottle in front of the collage adds layered depth but extra visual weight to an already busy right side"
  confidence: medium
- id: layout_06
  family: layout_composition_components
  polarity: mixed
  page_or_region: "homepage — 'Discover the best NAD-boosting solution' category-card row"
  tile_path: "store/truniagen-com/captures/2026-06-16/tiles/homepage/tile-02-y02440.png"
  claim: "The four category cards are structurally consistent but the product images above them vary in scale, crop, and framing (single bottles vs. boxed packaging), breaking the visual rhythm across the row."
  visible_tells:
    - "Product images above each category differ in height and crop ratio"
    - "Some include packaging/box context, others are isolated bottle shots"
    - "Aligned text/CTA below sit under unevenly weighted images, creating an uneven top-of-card"
  confidence: medium
- id: layout_07
  family: layout_composition_components
  polarity: mixed
  page_or_region: "homepage — researchers section ('Backed by world-leading researchers')"
  tile_path: "store/truniagen-com/captures/2026-06-16/tiles/homepage/tile-05-y06100.png"
  claim: "The researchers section sets a left headshot, a narrower center quote column, and a right headshot in an asymmetric arrangement; the left-aligned quote and left-aligned section heading create competing left axes that leave the composition slightly unresolved."
  visible_tells:
    - "Left and right headshots are roughly equal in size but the quote block between them is narrower"
    - "The quote text is left-aligned rather than centered within its column"
    - "The section heading sits left-aligned above, adding a second left axis competing with the three-column logic"
  confidence: medium
- id: layout_08
  family: layout_composition_components
  polarity: mixed
  page_or_region: "homepage — NAD-decline chart + science copy split"
  tile_path: "store/truniagen-com/captures/2026-06-16/tiles/homepage/tile-02-y02440.png"
  claim: "The two-column split puts a narrower NAD-decline chart left against wider science copy right with no clear proportional rationale, and the two halves don't share a bottom baseline, leaving the section edge ragged."
  visible_tells:
    - "Chart occupies roughly 40% of the section width while text occupies ~60%"
    - "The overline above the text column is very small and easily missed, leaving no shared visual anchor"
    - "Bottoms of the chart and the text column do not align on a baseline"
  confidence: medium
- id: layout_09
  family: layout_composition_components
  polarity: poor
  page_or_region: "collections page — bottom of grid (final row)"
  tile_path: "store/truniagen-com/captures/2026-06-16/tiles/collections-all/tile-02-y02440.png"
  claim: "The grid terminates with only two left-aligned cards in the final row, leaving two empty columns to the right — a grid-orphan gap that makes the page bottom feel unresolved."
  visible_tells:
    - "Two product cards sit in columns one and two of a four-column grid"
    - "Columns three and four are empty white space beside them"
    - "The centered 'You're viewing 1-14 of 14 products' line below draws further attention to the gap"
  confidence: high
  contrast_with: "store/truniagen-com/captures/2026-06-16/tiles/collections-all/tile-00-y00000.png"
- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: "homepage hero — navy chrome and announcement bar"
  tile_path: "store/truniagen-com/captures/2026-06-16/tiles/homepage/tile-00-y00000.png"
  claim: "The brand runs a disciplined two-tone palette — navy and white — held consistently from announcement bar through nav and hero background, giving a unified primary identity rather than a generic supplement gradient."
  visible_tells:
    - "Announcement bar, nav bar, and hero background share the same navy tone with no hue drift"
    - "White is the only other structural color; no tertiary accents appear in the UI chrome"
  confidence: high
  contrast_with: "store/truniagen-com/captures/2026-06-16/tiles/collections-all/tile-01-y01220.png"
- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: "homepage hero — Polaroid-style photo collage"
  tile_path: "store/truniagen-com/captures/2026-06-16/tiles/homepage/tile-00-y00000.png"
  claim: "The hero uses a deliberate Polaroid-snapshot collage — warm-toned lifestyle photos with white borders at slight rotations — instead of a single full-bleed stock image, reading as purposeful art direction."
  visible_tells:
    - "Multiple photos with white Polaroid-style borders at varying angles overlapping each other"
    - "Subjects are lifestyle/people (a dad with kids) with consistent warm grading across the collage"
  confidence: high
- id: color_03
  family: color_brand_imagery
  polarity: strong
  page_or_region: "homepage — product photography across SKU grid"
  tile_path: "store/truniagen-com/captures/2026-06-16/tiles/homepage/tile-01-y01220.png"
  claim: "Product shots use a consistent neutral off-white studio ground with identical lighting across all SKUs, producing a coherent product-image system rather than mismatched backgrounds."
  visible_tells:
    - "All visible product cards share the same clean off-white/light-gray background"
    - "No visible shadow or color-cast inconsistencies between units"
  confidence: high
- id: color_04
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "homepage — lifestyle photography across mid-page sections"
  tile_path: "store/truniagen-com/captures/2026-06-16/tiles/homepage/tile-03-y03660.png"
  claim: "Lifestyle photography is competent and warm but spans two noticeably different color temperatures — a cooler grey-blue editorial split above versus a much warmer amber quiz-CTA section below — indicating mixed grading rather than one unified treatment."
  visible_tells:
    - "Upper section shows a man in a cool, bluish-grey ambient room"
    - "Lower full-width CTA band shows a distinctly warm amber-brown light cast"
  confidence: high
  contrast_with: "store/truniagen-com/captures/2026-06-16/tiles/homepage/tile-05-y06100.png"
- id: color_05
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "homepage — researcher endorsement portraits"
  tile_path: "store/truniagen-com/captures/2026-06-16/tiles/homepage/tile-05-y06100.png"
  claim: "Researcher portraits are simple head-and-shoulders editorial shots on mismatched backgrounds (one light, one teal/grey) with no shared grading or crop, reading as credentialing content laid out generically rather than photographically designed."
  visible_tells:
    - "Two portraits: one man on a light background, one on a teal/grey background — different backdrops across the pair"
    - "No consistent color grading, framing crop, or backdrop treatment unifying the series"
  confidence: medium
- id: color_06
  family: color_brand_imagery
  polarity: strong
  page_or_region: "collections page — product catalog grid palette discipline"
  tile_path: "store/truniagen-com/captures/2026-06-16/tiles/collections-all/tile-00-y00000.png"
  claim: "The collections grid uses blue as the only link/interactive color against a white ground, holding palette discipline on a utility page where many DTC brands leak stray accent colors through badges, sale flags, or rating stars."
  visible_tells:
    - "Product titles and links are all the same medium blue; no red/orange/green accents in interactive elements"
    - "Card and page backgrounds stay white/very light grey with no color-filled card backgrounds"
  confidence: high
- id: color_07
  family: color_brand_imagery
  polarity: poor
  page_or_region: "homepage — 'Small daily choices' dark CTA band"
  tile_path: "store/truniagen-com/captures/2026-06-16/tiles/homepage/tile-04-y04880.png"
  claim: "The full-width dark CTA band uses a blurred, undifferentiated warm-amber background photo with no identifiable subject — visually interchangeable with a generic dark overlay on any wellness stock image."
  visible_tells:
    - "Background photo is a blurred warm amber wash with no clearly identifiable subject or scene"
    - "The band communicates no branded imagery beyond the centered text overlay"
  confidence: medium
- id: iconography_01
  family: iconography_illustration
  polarity: strong
  page_or_region: "homepage — 'Whole-body benefits' organ/cell illustration row"
  tile_path: "store/truniagen-com/captures/2026-06-16/tiles/homepage/tile-04-y04880.png"
  claim: "The five organ/cell icons (DNA helix, brain, heart, muscle tissue, cell) are soft-rendered 3D scientific illustrations sharing one pinkish-neutral palette and lighting — a custom illustration system, not stock clip-art."
  visible_tells:
    - "Each icon uses volumetric, anatomically plausible rendering — the DNA helix twists with depth, the brain shows sulci, the heart is realistically shaped"
    - "Shared warm pink/salmon palette and similar object scale unify the row as a designed set"
  confidence: high
  contrast_with: "store/truniagen-com/captures/2026-06-16/tiles/homepage/tile-02-y02440.png"
- id: iconography_02
  family: iconography_illustration
  polarity: mixed
  page_or_region: "homepage — NAD+ decline line chart"
  tile_path: "store/truniagen-com/captures/2026-06-16/tiles/homepage/tile-02-y02440.png"
  claim: "The NAD+ decline chart is legible but utilitarian — a plain shaded area/line plot with no branded axis styling or annotation craft, well below the polish of the illustration work elsewhere on the page."
  visible_tells:
    - "Axis labels and the declining curve use generic styling, only a blue line/fill for brand color"
    - "No custom tick marks, grid styling, or annotation design — a basic chart dropped into the layout"
  confidence: high
  contrast_with: "store/truniagen-com/captures/2026-06-16/tiles/homepage/tile-04-y04880.png"
- id: iconography_03
  family: iconography_illustration
  polarity: strong
  page_or_region: "homepage / collections — multi-SKU packaging color system"
  tile_path: "store/truniagen-com/captures/2026-06-16/tiles/homepage/tile-02-y02440.png"
  claim: "Product packaging deploys a coherent color-coded line taxonomy — navy, gold/yellow, teal, pink label bands — that signals Foundational / Pro / Immune / Beauty at thumbnail scale and carries consistently across homepage and collections."
  visible_tells:
    - "Four distinct label color bands cleanly distinguish product lines without reading the text"
    - "The same color system recurs on the collections grid and bundle photography, indicating a designed identity"
  confidence: high
  contrast_with: "store/truniagen-com/captures/2026-06-16/tiles/collections-all/tile-01-y01220.png"
- id: iconography_04
  family: iconography_illustration
  polarity: poor
  page_or_region: "homepage — statistics bar (45+, 60+, 500+, 300+)"
  tile_path: "store/truniagen-com/captures/2026-06-16/tiles/homepage/tile-01-y01220.png"
  claim: "The four credibility stats are plain large-number text with no supporting icon, badge, or data-viz treatment — visually inert and indistinguishable from a boilerplate stats block."
  visible_tells:
    - "Each number sits above a small label with no accompanying icon, badge, or graphic"
    - "The row carries no visual craft beyond the type itself"
  confidence: high
- id: iconography_05
  family: iconography_illustration
  polarity: mixed
  page_or_region: "homepage footer — social icon row"
  tile_path: "store/truniagen-com/captures/2026-06-16/tiles/homepage/tile-06-y07320.png"
  claim: "Footer social icons are standard platform glyphs at a small consistent size in navy on white — competent utility execution with no brand-integrated styling."
  visible_tells:
    - "Instagram, Facebook, LinkedIn, Pinterest, TikTok, X, and YouTube appear as off-the-shelf glyphs in navy"
    - "No bounding shape, size variation, or color treatment to integrate them with the brand palette"
  confidence: medium
- id: iconography_06
  family: iconography_illustration
  polarity: mixed
  page_or_region: "collections page — product card 'New' badge"
  tile_path: "store/truniagen-com/captures/2026-06-16/tiles/collections-all/tile-00-y00000.png"
  claim: "The 'New' badge on product cards is a minimal rounded-rectangle label — functional but generic, with no custom shape or character reinforcing the brand's scientific premium positioning."
  visible_tells:
    - "Small pill-shaped 'New' label in the top-right corner of product cards, default e-commerce treatment"
    - "No custom icon language, no brand color beyond basic navy"
  confidence: medium
```

## Provenance

- **Tiles read:** homepage (tiles 00–06) + collections-all (tiles 00–02) — 10 active tiles from `captures/2026-06-16/tiles/`, mined blind (4 family miners → Opus judge) over the Tier-A cached Firecrawl screenshots. No Tier-B browser re-render needed (no WebGL/grey-hero/black-media/lazy-load contamination on the design regions).
- **Exclusions (`qa_status: exclusions-noted`):** `homepage/tile-07-y08462.png`, `collections-all/tile-03-y03660.png`, `collections-all/tile-04-y03973.png` — each is the trailing **email-capture modal (“Unlock 10/30% off”) floating over a grey void**, a capture artifact, not page design. Excluded from mining; **zero accepted cards cite them**. (collections-all/tile-02 is the real grid-bottom + footer, kept.)
- **Cards:** 29 accepted across all four families (7 typography · 9 layout · 7 color/brand/imagery · 6 iconography), from 39 raw — the judge merged cross-family duplicates (e.g. the benefits-illustration row's color+iconography reads → one `iconography_01`; the packaging-taxonomy + amber-accent reads → one `iconography_03`) and dropped a footer `poor` card whose tell the tile contradicted. Calibrated mix: ~14 `strong`, 12 `mixed`, 3 `poor` (a `poor` in three of four families).
- **Spot-check:** the one `poor` *structural* card (`layout_09`, collections grid-orphan) was verified against its native tile — a genuine 2-card final row in a 4-col grid (14 of 14 products), not a compositing artifact.
- **Point-in-time:** a snapshot of the 2026-06-16 tiles — the homepage hero/promo is seasonal (Father’s Day) and rotating, so hero-specific reads (e.g. the Polaroid collage [color_02], the “#1 Dad” headline [typography_01]) may differ next capture.
