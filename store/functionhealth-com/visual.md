---
schema_version: "1.0"
domain: functionhealth.com
captured_at: 2026-06-14
source_capture: 2026-06-01
qa_status: recapture-used
---

## Visual & brand impression

Function Health reads like a controlled editorial health brand: large serif headlines, rust italic emphasis, and quiet sans support repeat across the homepage, pricing, and scans pages [typography_01][typography_02][color_01]. The strongest execution is structural: the three-step cards and comparison table use generous spacing, aligned rows, and one clear rust highlight column [layout_01][layout_02]. The image system feels owned rather than stock-generic, especially the restored cinematic homepage hero and the dark scan portrait with rust orbit lines [color_02][iconography_03]. The caveats are mostly density problems: tiny disease/biomarker labels, scan-card copy, and footer disclosures push legibility below the polish of the main sections [typography_03][layout_03][typography_04]. Net: warm, restrained, clinically premium, with detail density as the weak point [color_01][typography_03].

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: "homepage hero"
  tile_path: "store/functionhealth-com/captures/2026-06-01/tiles/homepage_browser/tile-00-y00000.png"
  claim: "The restored homepage hero establishes a clear editorial hierarchy: large white serif headline, smaller sans support copy, pill CTA, and a compact stats row over a darkened cinematic image."
  visible_tells:
    - "'Check your health.' is the largest text element and sits in white serif type over the dark lower-left image area."
    - "The support line is smaller sans text directly below the headline."
    - "The CTA and three-stat row are separated into distinct lower tiers."
  confidence: high
- id: typography_02
  family: typography_hierarchy
  polarity: strong
  page_or_region: "pricing hero and membership intro"
  tile_path: "store/functionhealth-com/captures/2026-06-01/tiles/pricing/tile-00-y00000.png"
  claim: "The pricing page repeats the brand's type system cleanly, using a large serif headline, rust italic price emphasis, small sans explanatory line, and a single rust CTA."
  visible_tells:
    - "'Test twice a year for' is oversized serif type while 'just $365 annually' switches to rust italic."
    - "The support sentence beneath is smaller sans text with a clear line break."
    - "The rust 'Start testing' button is visually subordinate to the headline but easy to find."
  confidence: high
- id: typography_03
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "homepage lab-test section"
  tile_path: "store/functionhealth-com/captures/2026-06-01/tiles/homepage_browser/tile-02-y02440.png"
  claim: "The lab-test section keeps its main display headline legible, but the disease ticker and biomarker lists push secondary information into low-contrast, edge-clipped microcopy."
  visible_tells:
    - "Disease names run in two long rows that continue off both viewport edges."
    - "The 'PAUSE MOTION' control is tiny and isolated on the left."
    - "Several biomarker rows fade to pale gray at the bottom of each category column."
  confidence: medium
- id: typography_04
  family: typography_hierarchy
  polarity: poor
  page_or_region: "pricing footer disclosures"
  tile_path: "store/functionhealth-com/captures/2026-06-01/tiles/pricing/tile-06-y06254.png"
  claim: "The footer disclosure block drops below the site's normal typographic discipline, becoming a dense wall of tiny sans text with little visible grouping."
  visible_tells:
    - "Multiple full-width disclosure paragraphs run beneath the polished footer card."
    - "The disclosure type is much smaller than the footer links above it."
    - "Long lines continue with minimal whitespace or section breaks."
  confidence: high
- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: "homepage 'Testing is easy' cards"
  tile_path: "store/functionhealth-com/captures/2026-06-01/tiles/homepage_browser/tile-01-y01220.png"
  claim: "The three-step explanation is composed as a disciplined, evenly spaced card row with matching card heights, centered numbering, and balanced CTAs beneath."
  visible_tells:
    - "Three cream cards share equal width and height across the row."
    - "The 01/02/03 numbers, titles, and mini product graphics align to the same vertical rhythm."
    - "Two centered CTA buttons sit directly below the card group with generous surrounding whitespace."
  confidence: high
- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: "pricing comparison table"
  tile_path: "store/functionhealth-com/captures/2026-06-01/tiles/pricing/tile-01-y01220.png"
  claim: "The comparison table creates a clear decision surface by floating the rust Function column over pale rows while keeping checks, crosses, and row labels aligned."
  visible_tells:
    - "The rust Function column is vertically centered and visually raised above the cream table."
    - "Every row rule spans cleanly across the label, Function, and standard-checkup columns."
    - "White check icons and black x icons line up consistently down their columns."
  confidence: high
- id: layout_03
  family: layout_composition_components
  polarity: mixed
  page_or_region: "scans CT cards"
  tile_path: "store/functionhealth-com/captures/2026-06-01/tiles/scans/tile-03-y03660.png"
  claim: "The CT scan cards are structurally consistent but heavy: two matched cards, long body paragraphs, prices, stacked buttons, metadata, and inclusion rows compete inside one component."
  visible_tells:
    - "Heart CT Scan and Lungs CT Scan cards mirror each other in width, padding, and button placement."
    - "Each card contains a long paragraph, large price, two full-width buttons, time metadata, and included/not-included rows."
    - "The lower half of each card becomes mostly text and controls rather than open space."
  confidence: high
- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: "pricing page palette"
  tile_path: "store/functionhealth-com/captures/2026-06-01/tiles/pricing/tile-00-y00000.png"
  claim: "The pricing page holds a restrained warm palette: cream ground, charcoal text, rust accents, and soft health-app imagery all stay in one color register."
  visible_tells:
    - "The page background is warm cream rather than pure white."
    - "Rust appears in the logo, italic price phrase, CTA, and membership card accents."
    - "The phone photo uses soft peach and beige tones that match the surrounding palette."
  confidence: high
- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: "scans hero"
  tile_path: "store/functionhealth-com/captures/2026-06-01/tiles/scans/tile-00-y00000.png"
  claim: "The scans hero extends the brand into a darker cinematic mode without losing the rust accent system or serif editorial feel."
  visible_tells:
    - "The hero is near-black with a low-key portrait on the right."
    - "Rust orbit lines wrap around the subject's head and echo the top banner and CTA color."
    - "The large white serif headline preserves the same display language used on lighter pages."
  confidence: high
- id: iconography_01
  family: iconography_illustration
  polarity: strong
  page_or_region: "homepage product mini-graphics"
  tile_path: "store/functionhealth-com/captures/2026-06-01/tiles/homepage_browser/tile-01-y01220.png"
  claim: "The three-step cards use product-like mini-graphics instead of generic icons, giving the process explanation a concrete interface language."
  visible_tells:
    - "The first card shows calendar and appointment chips with a rust-selected date and time."
    - "The second card shows a small biomarker chart with range bands and plotted points."
    - "The third card shows stacked food, supplement, and daily-health rows with matched rust icon blocks."
  confidence: high
- id: iconography_02
  family: iconography_illustration
  polarity: strong
  page_or_region: "pricing lab network metrics"
  tile_path: "store/functionhealth-com/captures/2026-06-01/tiles/pricing/tile-02-y02440.png"
  claim: "The lab-network proof points use branded data graphics that feel custom to the system: a dotted U.S. map and a muted rust bar chart."
  visible_tells:
    - "The U.S. map is built from evenly spaced rust dots inside a bordered metric card."
    - "The neighboring '75M+' card uses large gray numerals above a small rust bar chart."
    - "Both cards share the same rounded border, cream fill, and small rust label treatment."
  confidence: high
- id: iconography_03
  family: iconography_illustration
  polarity: strong
  page_or_region: "scans hero and scan explanation"
  tile_path: "store/functionhealth-com/captures/2026-06-01/tiles/scans/tile-00-y00000.png"
  claim: "The scans page turns medical imaging into a consistent visual motif through rust orbit lines and body-scan overlay labels rather than isolated clip-art."
  visible_tells:
    - "Rust elliptical lines encircle the hero portrait's head."
    - "The next section image uses translucent rings over the back and rounded labels such as 'Neck' and 'Spine.'"
    - "Both motifs use thin linework over photography instead of standalone stock icons."
  confidence: high
```

## Provenance

Tiles read: `store/functionhealth-com/captures/2026-06-01/tiles/homepage_browser/` (10 Tier-B browser viewport tiles), `store/functionhealth-com/captures/2026-06-01/tiles/pricing/` (7 cached tiles), and `store/functionhealth-com/captures/2026-06-01/tiles/scans/` (8 cached tiles).

QA note: `qa_status: recapture-used`. The cached Firecrawl homepage render under `store/functionhealth-com/captures/2026-06-01/tiles/homepage/` was excluded from active evidence because its first viewport rendered the hero as a flat grey block. The active homepage evidence uses the verified real-browser viewport restoration copied into `homepage_browser/`; pricing and scans use the cached 2026-06-01 screenshots.

Run note: generated in Codex with GPT-5.5.

Snapshot caveat: this is a point-in-time visual read of the cited tiles; later site changes are not reflected here.
