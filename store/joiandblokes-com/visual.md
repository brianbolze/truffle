---
schema_version: "1.0"
domain: joiandblokes.com
captured_at: 2026-06-15
source_capture: 2026-06-04
qa_status: clean
---

## Visual & brand impression

Reads as a controlled, premium men's-health system — owned art over stock. The brand runs two deliberate palettes, dark studio renders for men and a light-grey inversion for women [color_02], with product shots showing real material craft [color_01] and a periwinkle accent carried from the nav into the comparison grid [layout_02]. Custom data graphics — an optimization-score donut [iconography_01] and a bespoke testosterone-decline chart [iconography_02] — signal in-house design, and hierarchy is clean in heroes and cards [typography_01, layout_01]. Where it slips is finish: generic stock feature icons [iconography_03], a wireframe-like phone mockup [iconography_04], a cramped all-caps labs headline [typography_03], weak carousel affordances [layout_03], and tonal seams where warm borrowed imagery meets the cool palette [color_03, color_04].

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: "homepage hero"
  tile_path: "store/joiandblokes-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"
  claim: "The hero sets a clear three-level hierarchy — serif display headline 'Not just another telemedicine company', lighter regular-weight body beneath, and a two-button CTA row — each level differentiated by size and weight."
  visible_tells:
    - "Serif display headline is the dominant text element, distinctly larger than the body line"
    - "Body copy beneath is light-weight and visually subordinate"
    - "Two CTAs ('Shop Women'/'Shop Men') anchor the bottom at matched width without competing with the headline"
  confidence: high
- id: typography_02
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "trt_men — competitor comparison table headers"
  tile_path: "store/joiandblokes-com/captures/2026-06-04/tiles/trt_men/tile-03-y03660.png"
  claim: "The comparison table sets all-caps row labels and column brand headers at near-identical size with no weight differentiation, so distinguishing row category from column brand takes deliberate scanning."
  visible_tells:
    - "Row labels ('TRT AVAILABLE', 'ENCLOMIPHENE AVAILABLE', 'HAIR MEDS ADD-ON') are all-caps tracked, same size as column brand names ('MAXIMUS', 'HONE HEALTH', 'HIMS')"
    - "No weight or size break separates the row-header level from the column-header level"
    - "Section title 'Experience the Difference' above is larger and mixed-case — the only clear level break in the module"
  confidence: high
- id: typography_03
  family: typography_hierarchy
  polarity: poor
  page_or_region: "mens_labs — hero headline (all-caps display)"
  tile_path: "store/joiandblokes-com/captures/2026-06-04/tiles/mens_labs/tile-00-y00000.png"
  claim: "The hero headline 'TEST SMARTER — LABS THAT MATCH YOUR GOALS' is set in wide all-caps with very tight leading, making the two-line block feel dense and harder to scan than the headline size warrants."
  visible_tells:
    - "All-caps treatment at large size with narrow interline space compresses the two lines"
    - "The em-dash mid-phrase adds a pause the tight leading fights against"
    - "Wide tracking plus tight leading gives the block a compressed, monolithic shape"
  contrast_with: "store/joiandblokes-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"
  confidence: high
- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: "shop_men — product grid"
  tile_path: "store/joiandblokes-com/captures/2026-06-04/tiles/shop_men/tile-01-y01220.png"
  claim: "The three-column product card system is internally consistent: each card holds image zone, name, descriptor, price, and an 'ADD' pill — all aligned at identical heights with badge chips pinned uniformly to the top-right."
  visible_tells:
    - "All 'ADD' pill buttons sit at the same vertical position across the row"
    - "Badge chips ('Best Seller', 'Lab Required') are pinned identically to the top-right of each image"
    - "Card image zones share a common size and dark-grey background"
  confidence: high
- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: "trt_men — competitor comparison table"
  tile_path: "store/joiandblokes-com/captures/2026-06-04/tiles/trt_men/tile-03-y03660.png"
  claim: "The comparison table holds clean column alignment across multiple rows with a deliberate two-tone fill (periwinkle for the brand and positive cells, black for competitor negatives), producing a scannable grid without cell collapse or alignment drift."
  visible_tells:
    - "Positive cells render in muted periwinkle, negative cells in solid black — a consistent two-tone system"
    - "Row labels left-align to a fixed inset; check/X marks center within each cell"
    - "Four brand columns (Joi+Blokes, Maximus, Hone Health, Hims) stay aligned across every row"
  confidence: high
- id: layout_03
  family: layout_composition_components
  polarity: mixed
  page_or_region: "homepage — 'Women's best sellers' product row"
  tile_path: "store/joiandblokes-com/captures/2026-06-04/tiles/homepage/tile-03-y03660.png"
  claim: "The women's best-sellers row shows three product cards with a partially-filled progress bar but no arrows or visible scroll controls, and leaves dead whitespace on the right rather than hinting at overflow — the carousel affordance is weak."
  visible_tells:
    - "A horizontal progress bar below the row is roughly half-filled, implying more items, but no next/prev control is visible"
    - "Three cards sit at equal width with notable empty margin on the right side"
  contrast_with: "store/joiandblokes-com/captures/2026-06-04/tiles/shop_men/tile-01-y01220.png"
  confidence: medium
- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: "shop_men hero"
  tile_path: "store/joiandblokes-com/captures/2026-06-04/tiles/shop_men/tile-00-y00000.png"
  claim: "The men's shop hero is a near-black branded flat-lay built from logo-embossed packaging at converging angles — owned art, not stock, with the wordmark legible directly on the product surfaces."
  visible_tells:
    - "Deep charcoal background with no lifestyle elements"
    - "'Joi + Blokes' wordmark repeated across multiple angled faceted surfaces"
  contrast_with: "store/joiandblokes-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"
  confidence: high
- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: "homepage — women's best sellers"
  tile_path: "store/joiandblokes-com/captures/2026-06-04/tiles/homepage/tile-03-y03660.png"
  claim: "The women's best-sellers products sit on a flat light-grey studio field — a deliberate tonal inversion from the men's dark cards — showing the brand runs two controlled palettes (light for women, dark for men) rather than one undifferentiated scheme."
  visible_tells:
    - "Vials, the amber 'Balance' jar, and the cream canister float on a near-white grey field"
    - "No lifestyle or hand-held elements — same stripped-back studio logic as the men's cards, inverted in value"
  contrast_with: "store/joiandblokes-com/captures/2026-06-04/tiles/shop_men/tile-01-y01220.png"
  confidence: high
- id: color_03
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "trt_men — Joe Rogan social-proof thumbnails"
  tile_path: "store/joiandblokes-com/captures/2026-06-04/tiles/trt_men/tile-03-y03660.png"
  claim: "The podcast social-proof thumbnails are external video stills with warm-amber studio lighting that clashes with the brand's otherwise cool-dark palette, creating an unresolved tonal seam in the section."
  visible_tells:
    - "Two square thumbnails show warm-amber podcast-studio ambient glow"
    - "Surrounding page background stays cool charcoal, so the warm stills sit against the cool field as a seam"
  contrast_with: "store/joiandblokes-com/captures/2026-06-04/tiles/shop_men/tile-00-y00000.png"
  confidence: high
- id: color_04
  family: color_brand_imagery
  polarity: poor
  page_or_region: "trt_men — testosterone-decline chart over torso photo"
  tile_path: "store/joiandblokes-com/captures/2026-06-04/tiles/trt_men/tile-01-y01220.png"
  claim: "The light-grey bar chart composited over a warm-toned male-torso photograph creates a tonal mismatch — the desaturated bars and floating labels sit awkwardly over the warm skin tones rather than feeling integrated into the photo."
  visible_tells:
    - "Light-grey and darker-grey bars float over a warm reddish-skin torso photograph"
    - "The chart's cool/neutral bars contrast against the warm photographic ground beneath them"
  confidence: medium
- id: iconography_01
  family: iconography_illustration
  polarity: strong
  page_or_region: "trt_men — 'Optimization Score' donut gauge"
  tile_path: "store/joiandblokes-com/captures/2026-06-04/tiles/trt_men/tile-02-y02440.png"
  claim: "The donut-ring 'Optimization Score' gauge is a custom branded data graphic — a segmented arc in green/amber/grey with a 61.7% readout — and recurs both as a standalone card and inside a phone mockup, indicating a designed system asset rather than a default chart widget."
  visible_tells:
    - "61.7% centered in the ring with 'in Optimal Range' beneath"
    - "Three-segment arc in distinct green/amber/grey rather than a default library palette"
    - "Same gauge appears in the standalone card and as a phone-screen mockup in the same row"
  contrast_with: "store/joiandblokes-com/captures/2026-06-04/tiles/trt_men/tile-01-y01220.png"
  confidence: high
- id: iconography_02
  family: iconography_illustration
  polarity: strong
  page_or_region: "trt_men — testosterone-decline bar chart"
  tile_path: "store/joiandblokes-com/captures/2026-06-04/tiles/trt_men/tile-01-y01220.png"
  claim: "The declining-T bar chart is a bespoke branded data illustration — two era columns (1987–1989 vs 2002–2005), dual bars per era with ng/dl callouts, a legend, and pill-tag era labels matching the site badge system — styled to fit the dark aesthetic rather than dropped from a generic generator."
  visible_tells:
    - "Bar pairs carry exact ng/dl values (501, 237, 391, 130) as floating labels"
    - "Era date-range labels are styled as pill tags matching the site's badge system"
    - "A two-item legend ('Total testosterone' / 'Bioavailable testosterone') is integrated into the dark card"
  confidence: high
- id: iconography_03
  family: iconography_illustration
  polarity: mixed
  page_or_region: "trt_men — 'What's Included' feature icons"
  tile_path: "store/joiandblokes-com/captures/2026-06-04/tiles/trt_men/tile-02-y02440.png"
  claim: "Feature icons sit in uniform pale-blue circle badges but the glyphs themselves are generic line-art (stethoscope, wand, camera, laptop-person, chat bubble, atom) that read as off-the-shelf icon-library assets rather than custom-drawn marks."
  visible_tells:
    - "Six icons share identical badge size and fill with no character variation"
    - "Stethoscope, chat-bubble, and atom glyphs are recognizable stock outline forms"
    - "No bespoke illustrative detail distinguishes them from common icon libraries"
  contrast_with: "store/joiandblokes-com/captures/2026-06-04/tiles/shop_men/tile-00-y00000.png"
  confidence: high
- id: iconography_04
  family: iconography_illustration
  polarity: poor
  page_or_region: "homepage — process strip phone mockup"
  tile_path: "store/joiandblokes-com/captures/2026-06-04/tiles/homepage/tile-02-y02440.png"
  claim: "The middle phone mockup in the journey strip floats a clinician avatar and a 'Personalized Medicine' pill onto a phone with a blank white screen — the composite reads as an unfinished wireframe annotation rather than polished product illustration."
  visible_tells:
    - "Circular avatar photo floats detached from the phone with no clear spatial relationship"
    - "'Personalized Medicine' pill badge is superimposed at an arbitrary angle"
    - "The phone screen beneath shows no app UI — just a blank white area — making the composite feel incomplete"
  contrast_with: "store/joiandblokes-com/captures/2026-06-04/tiles/trt_men/tile-02-y02440.png"
  confidence: medium
```

## Provenance

- **Tiles read** — native-resolution Tier-A tiles sliced from the 2026-06-04 cached full-page screenshots, four pages: `homepage` (9), `shop_men` (10), `trt_men` (10), `mens_labs` (9) — 38 tiles. Pages chosen for the men's-side visual system (hero/brand, product grid, a PDP, a labs/data page); women's and GLP-1 pages in the capture were not mined.
- **QA note** — `qa_status: clean`: all cited tiles came straight from the cached payloads, no tiles excluded. One known capture artifact is present in the cached screenshots: Firecrawl's full-page stitching re-composites the fixed nav bar at each scroll segment, so a white nav band intermittently overlays content mid-tile (e.g. across the `trt_men` comparison table). The blind miners are instructed to treat compositing artifacts as capture caveats, not design evidence, and the judge rejected artifact-derived cards; no accepted card cites the band.
- **Tier-B reverted** — a browser re-render was attempted to remove the nav-band artifact but was discarded: the live site fired a "Stay Connected" newsletter modal over the content and the renders collapsed (homepage 1 tile, shop_men/mens_labs 2 tiles each), i.e. worse contamination than the cached tiles. Final evidence is Tier-A only.
- **Snapshot caveat** — a point-in-time read of the 2026-06-04 captured tiles; the live site changes. Mining was blind (tiles only; no `profile.md`, dossier, Notion, or live web).
