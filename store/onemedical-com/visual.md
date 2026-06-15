---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.0"
domain: onemedical.com
captured_at: 2026-06-15
source_capture: 2026-06-15
qa_status: clean
---

## Visual & brand impression

One Medical presents a controlled, mature consumer-health system. The palette holds to two colors — deep forest teal and amber-gold — across nav, type, and brand mark with no stray accent [color_01], and its signature asset is an owned hand-painted watercolor illustration language [iconography_01]. Serif display type sets clean hero and stat hierarchies [typography_03, typography_04], and core components — the membership comparison table, the FAQ accordion — are tidy and scannable [layout_04, layout_12]. The cracks are in the connective tissue: dense grids and category sections flatten to one type level [typography_06, typography_11], illustration rhythm drifts row to row [layout_05], a kids icon register and generic app icons sit a tier below the watercolors [iconography_05, iconography_07], some photography reads assembled rather than art-directed [color_06, color_07], and the Fast Facts stats float adrift [layout_09].

## Evidence cards

```yaml
- id: typography_03
  family: typography_hierarchy
  polarity: strong
  page_or_region: "membership page — hero"
  tile_path: "store/onemedical-com/captures/2026-06-15/tiles/membership/tile-00-y00000.png"
  claim: "White serif display type over a full-bleed photo stays legible against the dark garment, with a muted eyebrow label and subordinate CTA — disciplined copy-over-image handling."
  visible_tells:
    - "'Healthcare, without the headaches' in white serif sits over the dark teal sweater, giving contrast"
    - "Small 'Personal Membership' eyebrow above acts as a separate label tier"
    - "CTA button is visually subordinate to the headline"
  confidence: high
- id: typography_04
  family: typography_hierarchy
  polarity: strong
  page_or_region: "about page — 'Fast Facts' stats"
  tile_path: "store/onemedical-com/captures/2026-06-15/tiles/about/tile-05-y05312.png"
  claim: "The stats use a deliberate two-level split — very large serif numerals over a smaller label line — functioning as a clean standalone legibility system."
  visible_tells:
    - "'90+', '8,500+', '45%' set at display scale, roughly 3-4x the label size"
    - "Labels ('Net Promoter Score', 'Employer Clients') are compact and clearly subordinate"
    - "'Fast Facts' head sits as an intermediate tier above the numbers"
  confidence: high
- id: typography_06
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "services hub — service category sections"
  tile_path: "store/onemedical-com/captures/2026-06-15/tiles/services_hub/tile-01-y01220.png"
  claim: "Each service-category heading and body paragraph share the same type treatment block to block, producing a consistent but monotonous scroll with only two tiers and no escalation."
  visible_tells:
    - "'Everyday care' and 'Chronic conditions' headings appear at identical size and weight in one tile"
    - "Body paragraphs are the same point size across both blocks"
    - "No subheads or tertiary labels differentiate content within any block"
  confidence: high
- id: typography_11
  family: typography_hierarchy
  polarity: poor
  page_or_region: "kids page — feature icon grid"
  tile_path: "store/onemedical-com/captures/2026-06-15/tiles/kids/tile-01-y01220.png"
  claim: "The six-cell icon grid collapses to a single type level — each cell's label and two-line body are nearly identical in size — making the grid hard to skim."
  visible_tells:
    - "Cell labels ('24/7 peace of mind', 'Kid-approved offices') are barely larger than the body copy beneath"
    - "All six cells share identical type sizing with no weight variation"
    - "The 'See why families love One Medical' head uses the same scale as the cell heads, failing to re-anchor at section level"
  confidence: high
- id: layout_04
  family: layout_composition_components
  polarity: strong
  page_or_region: "membership / comparison table"
  tile_path: "store/onemedical-com/captures/2026-06-15/tiles/membership/tile-01-y01220.png"
  claim: "The comparison table is a well-built two-panel component — a tinted green 'Included' panel and a blue 'Copay & fees' panel with dark sub-column headers — sharing one row grid that stays scannable across all visit types."
  visible_tells:
    - "Tinted panels with rounded corners separate 'Included' from 'Copay & fees' while keeping the shared row grid"
    - "Dark sub-column headers (Direct Message Care, Video Care, In-Person, Video Visit) sit at the same height"
    - "Row dividers run full width with consistent spacing"
  confidence: high
- id: layout_12
  family: layout_composition_components
  polarity: strong
  page_or_region: "kids / FAQ accordion"
  tile_path: "store/onemedical-com/captures/2026-06-15/tiles/kids/tile-06-y07320.png"
  claim: "The FAQ accordion is a clean, well-spaced component — hairline dividers per row, left-aligned questions on consistent indentation, and plus icons locked to a single right-hand rail."
  visible_tells:
    - "Divider lines run edge-to-edge at the same weight for every row"
    - "Plus icons sit flush right on a consistent vertical column"
    - "Row heights appear equal despite varying question length"
  confidence: high
- id: layout_05
  family: layout_composition_components
  polarity: mixed
  page_or_region: "services hub / alternating content rows"
  tile_path: "store/onemedical-com/captures/2026-06-15/tiles/services_hub/tile-01-y01220.png"
  claim: "The alternating text/illustration rows follow a consistent pattern, but illustration scale and section padding vary noticeably between blocks, creating an irregular vertical rhythm."
  visible_tells:
    - "The 'Everyday care' illustration sits much smaller relative to its text than the 'Chronic conditions' illustration in the same tile"
    - "Vertical padding above 'Everyday care' is tighter than above 'Chronic conditions'"
  confidence: medium
- id: layout_09
  family: layout_composition_components
  polarity: poor
  page_or_region: "about / Fast Facts section"
  tile_path: "store/onemedical-com/captures/2026-06-15/tiles/about/tile-04-y04880.png"
  claim: "The Fast Facts trio floats centered on plain white with a large empty gap above it and no containing card or band, leaving the section feeling adrift on the page."
  visible_tells:
    - "A wide blank gap precedes the 'Fast Facts' heading with nothing filling it"
    - "Stat numbers and labels float center with no card, band, or rule to anchor them"
    - "The accolades below fall into an asymmetric 3+2 layout"
  confidence: medium
- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: "homepage — hero and nav"
  tile_path: "store/onemedical-com/captures/2026-06-15/tiles/homepage/tile-00-y00000.png"
  claim: "The palette is held to two colors — deep forest teal and a warm amber-gold — applied with discipline across nav, headline type, and brand mark, with no stray third accent."
  visible_tells:
    - "Nav wordmark and headline both render in the same deep teal"
    - "Amber-gold appears only as a controlled accent (the underline on 'Amazon')"
    - "No secondary accent (blue, red, purple) appears in the hero band"
  confidence: high
- id: color_03
  family: color_brand_imagery
  polarity: strong
  page_or_region: "membership — hero"
  tile_path: "store/onemedical-com/captures/2026-06-15/tiles/membership/tile-00-y00000.png"
  claim: "The hero photo — a tight crop of a person in a dark teal top against a powder-blue backdrop — is keyed to the brand palette, reading as art-directed rather than stock-assembled."
  visible_tells:
    - "The subject's clothing is the brand teal, not incidental"
    - "Background is a flat powder blue matching the secondary tint used in app mockups"
    - "Subject framed off-center with generous white text space"
  confidence: medium
- id: color_06
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "homepage — photography grid"
  tile_path: "store/onemedical-com/captures/2026-06-15/tiles/homepage/tile-00-y00000.png"
  claim: "The three thumbnail photos (meditation, exam, woman on phone) share warm ambient light but differ in framing, depth, and color cast enough to read as assembled rather than shot as one set."
  visible_tells:
    - "Leftmost (yoga) is brighter and greener; center (exam) is darker and cooler; right (phone) is warmer and more commercial"
    - "No consistent crop ratio or focal distance across the three"
  confidence: medium
  contrast_with: "store/onemedical-com/captures/2026-06-15/tiles/membership/tile-00-y00000.png"
- id: color_07
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "about — leadership photography"
  tile_path: "store/onemedical-com/captures/2026-06-15/tiles/about/tile-02-y02440.png"
  claim: "The leadership portrait on a warm-beige studio backdrop is competent but generic — it reads as a standard headshot and does not visually connect to the teal-keyed photography elsewhere."
  visible_tells:
    - "Subject shot against a plain blurred beige backdrop with no environmental context"
    - "Grade is cooler and more neutral than the warm inhabited shots elsewhere"
    - "No stylistic link to the membership-hero photography"
  confidence: medium
  contrast_with: "store/onemedical-com/captures/2026-06-15/tiles/membership/tile-00-y00000.png"
- id: iconography_01
  family: iconography_illustration
  polarity: strong
  page_or_region: "services hub — editorial illustration row"
  tile_path: "store/onemedical-com/captures/2026-06-15/tiles/services_hub/tile-01-y01220.png"
  claim: "The editorial illustrations use a consistent hand-painted watercolor technique — limited warm palette, loose linework, intentional negative space — clearly not stock or clip-art."
  visible_tells:
    - "The reclining figure with flowing teal ribbon shows visible wet-edge brush strokes"
    - "The doctor-patient scene uses the same warm tan/teal palette and unfinished contours"
    - "No hard outlines or vector fills — paint texture is consistent across figures"
  confidence: high
- id: iconography_05
  family: iconography_illustration
  polarity: mixed
  page_or_region: "kids — feature benefit icon grid"
  tile_path: "store/onemedical-com/captures/2026-06-15/tiles/kids/tile-01-y01220.png"
  claim: "The kids page uses a separate icon register — thin-outline icons with smiley faces and flat fills — friendlier but stylistically distinct from the watercolor illustrations elsewhere on the site."
  visible_tells:
    - "The moon-and-sun icon uses a thin stroke and solid fill, no painterly texture"
    - "The house icon is a flat orange fill with no shading — vector-style, not watercolor"
    - "The location pin is a basic filled teardrop, close to a generic glyph"
  confidence: high
  contrast_with: "store/onemedical-com/captures/2026-06-15/tiles/services_hub/tile-01-y01220.png"
- id: iconography_07
  family: iconography_illustration
  polarity: mixed
  page_or_region: "homepage — app UI mockup icons"
  tile_path: "store/onemedical-com/captures/2026-06-15/tiles/homepage/tile-02-y02440.png"
  claim: "The app-mockup icons (Office, Remote, Routine Visit) are rounded-square container icons with simple pictograms — functional but visually generic and lower-craft than the editorial illustration system."
  visible_tells:
    - "Three icons share an identical rounded-square container with low-detail pictograms"
    - "Building and stethoscope glyphs are basic line art with no tonal variation"
    - "The amber background on the schedule icon sits apart from the teal-dominant illustration palette"
  confidence: medium
```

## Provenance

- **Tiles read:** 32 native-resolution tiles across 5 pages (homepage, membership, services_hub, about, kids), Tier-A sliced from the cached 2026-06-15 Firecrawl full-page screenshots (`captures/2026-06-15/tiles/`).
- **QA note:** `clean` — all tiles came straight from cached payloads; no contamination (no modals, grey heroes, black media, or mid-animation artifacts), so no exclusions and no Tier-B browser re-render. The only artifact (the sticky-header repeat down the full-page composites) is benign and not cited.
- **Mining:** blind fan-out — 4 family miners (Sonnet, tiles-only, no dossier/web) → 48 raw cards → judge (Opus) accepted 42. **15 curated here** for the evidence layer (the contract's 8–14 target; 4 families, 7 strong / 6 mixed / 2 poor), selecting the highest-signal, non-redundant cards and dropping near-duplicate strong-hierarchy/watercolor cards.
- **Scope:** mined **onemedical.com** pages only — the brand's own visual system. The Amazon storefront (`health.amazon.com/onemedical`) is a different host's design (Amazon's), excluded here for a coherent per-domain read; its co-brand lockup is noted in `profile.md`'s Visual section.
- **Snapshot caveat:** a snapshot of the 2026-06-15 tiles; the live site changes.
