---
schema_version: "1.0"
domain: agelessrx.com
captured_at: 2026-06-14
source_capture: 2026-05-31
qa_status: clean
---

## Visual & brand impression

A controlled wellness-brand system: forest-green and ice-blue fields with a single amber CTA, held from hero to footer [color_01][color_03], over a serif-headline / sans-body hierarchy that reads confidently top-down [typography_01][typography_02]. The standout is an owned product-render language — amber bottles, teal caps, uniform angle and shadow on matching tiles [iconography_01] — backed by disciplined components: a clean three-up product grid, mirrored explainer cards, and in-palette custom charts [layout_01][layout_03][iconography_05]. It frays where third-party assets intrude: partner packshots break the render grid [iconography_02], and stock lab photos plus a grayscale logo wall sit off-system [color_02][color_04]. Smaller weaknesses are low-contrast type over photos and a broken comparison table [typography_04][layout_04]. Competent and coherent, let down at the edges.

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: Homepage hero headline
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/homepage/tile-00-y00000.png
  claim: The hero pairs a high-contrast serif headline with a roman/italic switch on 'more' for emphasis, set well above a small sans subhead, giving an immediate three-step read.
  visible_tells:
  - Serif headline 'What would you do with more healthy years?' with 'more' in italic
  - subhead in a much smaller sans weight directly under it
  - clear size jump from headline to subhead to amber pill CTA
  confidence: high
- id: typography_02
  family: typography_hierarchy
  polarity: strong
  page_or_region: BioAge test hero
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/bioage_test/tile-00-y00000.png
  claim: An all-caps tracked eyebrow ('BIOAGE TESTS') sits over a large serif headline with an italic 'really?', then a centered sans paragraph, producing a confident, legible four-level hierarchy on a dark ground.
  visible_tells:
  - Tracked all-caps teal eyebrow above the headline
  - serif headline 'How old are you really?' with italicized final word
  - white body copy stays legible over the flat dark-green field
  confidence: high
  contrast_with: store/agelessrx-com/captures/2026-05-31/tiles/about/tile-00-y00000.png
- id: typography_03
  family: typography_hierarchy
  polarity: mixed
  page_or_region: Homepage stats row
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/homepage/tile-01-y01220.png
  claim: The three big teal stats ('82.7%', '30+', '5,200+') establish clear emphasis, but their captions sit in tiny grey sans and the dense footnote beneath drops to a hard-to-read micro size.
  visible_tells:
  - Large teal numerals far outweigh their grey caption lines
  - multi-line footnote under the stats set in very small grey type
  confidence: medium
- id: typography_04
  family: typography_hierarchy
  polarity: poor
  page_or_region: About hero body copy
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/about/tile-00-y00000.png
  claim: Below the serif hero headline the mission paragraph is set in tiny low-contrast type over a dark foliage photo, rendering it close to illegible at this scale; the lower 'Science has given us a new perspective' paragraph repeats the problem over a blurred photo.
  visible_tells:
  - Multi-line paragraph under 'We believe aging is a puzzle that can be solved' is very small and dim
  - lower paragraph set in tiny low-contrast white type over a soft blurred photo rather than a solid field
  confidence: medium
  contrast_with: store/agelessrx-com/captures/2026-05-31/tiles/bioage_test/tile-00-y00000.png
- id: typography_05
  family: typography_hierarchy
  polarity: poor
  page_or_region: About 'Designing a future' timeline overlay labels
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/about/tile-01-y01220.png
  claim: The 'Now' vs 'Future' timeline bars carry tiny inline labels ('Well / Transition / Sick', age ranges) crammed into colored segments, where the type is too small to scan and competes with the body paragraph beside it.
  visible_tells:
  - Micro labels inside the two horizontal gradient bars
  - age annotations ('~80 years', '100+ years') in faint small type at the bar ends
  confidence: medium
- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: Treatments catalog grid (top of listing)
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/treatments/tile-00-y00000.png
  claim: The treatments listing runs a disciplined three-column product-card grid where every card shares the same pale-blue image panel, white text well, title-description-'Learn More' stack, and gutter, producing clean horizontal and vertical alignment across rows.
  visible_tells:
  - Three columns of equal-width cards with identical image-panel top and matching title baselines (NAD+ Injection / Women's Hormone Care / Microdosing GLP-1) in row one
  - consistent gutter spacing and a left filter rail aligned to the same top edge as the first card row
  confidence: high
- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: Global footer (repeated across pages)
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/homepage/tile-03-y03024.png
  claim: The dark four-column footer (Treatments / Product Science / Learn / Contact) is rendered identically across homepage, about, and bioage pages with consistent column alignment, link spacing, and a tidy bottom legal row.
  visible_tells:
  - Four evenly spaced heading columns with left-aligned link lists and matching baseline grid
  - identical copyright row, social icon set, and legal disclaimer block repeated verbatim on multiple tiles
  confidence: high
  contrast_with: store/agelessrx-com/captures/2026-05-31/tiles/about/tile-06-y06536.png
- id: layout_03
  family: layout_composition_components
  polarity: strong
  page_or_region: BioAge — 'Methylation vs Phenotypic' paired cards
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/bioage_test/tile-03-y02871.png
  claim: Two side-by-side explainer cards mirror each other exactly — image cap, centered heading, and a bulleted list — set against a dark-green band so the comparison reads as a deliberate, balanced pair.
  visible_tells:
  - Both cards share identical width, rounded corners, image-header height, and bullet indentation
  - headings 'How Methylation works' and 'How Phenotypic age works' sit at the same baseline
  confidence: high
- id: layout_04
  family: layout_composition_components
  polarity: poor
  page_or_region: BioAge — 'Which BioAge test is right for you?' comparison table
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/bioage_test/tile-01-y01220.png
  claim: The comparison table's Accuracy, Emailed Results, Portal Access, and Level of Detail rows render as broken-image placeholders (empty boxes and overlapping garbled fragments) instead of the intended rating glyphs, leaving several cells visually unresolved.
  visible_tells:
  - Tiny broken-image icons with garbled 'stista' alt-text overlaps in the Accuracy and Level of Detail rows
  - empty bordered placeholder squares in the Emailed Results and Portal Access cells across all three columns
  confidence: medium
- id: layout_05
  family: layout_composition_components
  polarity: poor
  page_or_region: Treatments grid — cross-row card-height inconsistency
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/treatments/tile-03-y03660.png
  claim: Within the catalog, cards in the same row settle at unequal heights because descriptions vary widely in length, so neighboring white wells end at different baselines and leave ragged bottom edges down the grid.
  visible_tells:
  - Glucose Biosensors card body runs many lines while the Glucose Control and Glutathione Nasal Spray cards beside it end higher
  - misaligned 'Learn More' link positions and uneven white-space gaps below shorter cards in the row
  confidence: medium
  contrast_with: store/agelessrx-com/captures/2026-05-31/tiles/treatments/tile-00-y00000.png
- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: Site-wide palette
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/homepage/tile-01-y01220.png
  claim: The palette is disciplined to three roles — deep forest green, pale ice-blue, and a single amber CTA — held consistent across hero, stats, and footer bands, with teal stats drawn from the same green family.
  visible_tells:
  - Deep green section bands top and bottom
  - amber 'See the science' / 'Explore' buttons as the lone warm accent
  - teal stat numerals (82.7%, 5,200+) drawn from the same green family
  confidence: high
  contrast_with: store/agelessrx-com/captures/2026-05-31/tiles/treatments/tile-00-y00000.png
- id: color_02
  family: color_brand_imagery
  polarity: mixed
  page_or_region: Homepage 'research' / lifestyle imagery
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/homepage/tile-01-y01220.png
  claim: Photography leans on generic stock tropes (blue-gloved hands pipetting, man reading a pill bottle) that carry no brand-specific styling and a neutral grade untied to the green/amber system.
  visible_tells:
  - Blue-nitrile-glove lab pipette image
  - stock-style man-with-supplement-bottle photo
  - neutral grading not tied to the green/amber system
  confidence: medium
  contrast_with: store/agelessrx-com/captures/2026-05-31/tiles/treatments/tile-00-y00000.png
- id: color_03
  family: color_brand_imagery
  polarity: strong
  page_or_region: Footer / logo lockup
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/homepage/tile-03-y03024.png
  claim: The footer carries a consistent brand lockup — the lowercase 'a' mark with teal accent dot and a tidy teal-on-green link system — closing the page in the same palette it opened with.
  visible_tells:
  - White 'a' monogram with teal dot on dark-green footer
  - teal column links over the forest-green field
  - single-weight monochrome social icons aligned in a row
  confidence: high
- id: color_04
  family: color_brand_imagery
  polarity: mixed
  page_or_region: About page — partner logo wall
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/about/tile-06-y06536.png
  claim: The partner logo row is a grayscale assembly of mismatched marks at inconsistent visual weight, reading as collected third-party assets rather than a unified band.
  visible_tells:
  - 'FIGHT AGING!' shown as a heavy black-box knockout among thin line logos
  - wildly varying logo weights (Betterhumans script vs. serif 'Age Reversal Network')
  - uneven sizing across the six marks
  confidence: medium
- id: iconography_01
  family: iconography_illustration
  polarity: strong
  page_or_region: Treatments grid — AgelessRx-branded product bottles
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/treatments/tile-01-y01220.png
  claim: The own-brand product renders form a tightly consistent system: amber pill bottles with dark-teal caps and white 'agelessrx' labels, all shot at the same angle, lighting, and drop-shadow on identical pale-blue tiles.
  visible_tells:
  - Low Dose Naltrexone, B12/MIC, B12, and Metformin bottles share identical cap color, label layout, angle, and shadow direction
  - uniform pale-blue tile background behind every render
  confidence: high
- id: iconography_02
  family: iconography_illustration
  polarity: mixed
  page_or_region: Treatments grid — third-party packshots inside own-brand grid
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/treatments/tile-01-y01220.png
  claim: Third-party regulatory packshots are dropped into the otherwise uniform render grid and break it, sitting at a different scale, sharpness, and lighting than the house bottles around them.
  visible_tells:
  - Wegovy 2.4mg carton-and-pen composite looks photographic and busy next to the clean matte house bottles
  - scale and shadow of the Wegovy box differ from adjacent cards
  confidence: high
  contrast_with: store/agelessrx-com/captures/2026-05-31/tiles/treatments/tile-04-y04880.png
- id: iconography_03
  family: iconography_illustration
  polarity: strong
  page_or_region: Homepage — 'Slowing aging has never been easier' three-up icons
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/homepage/tile-02-y02440.png
  claim: The three benefit icons (clipboard with pencil, shipping box, chat bubbles) read as one custom line-icon set with a consistent stroke weight and a single muted tan/coral fill accent.
  visible_tells:
  - all three icons share the same outlined style, corner radius, and tan fill accent
  - no clip-art mismatch in weight or perspective between the trio
  confidence: medium
- id: iconography_04
  family: iconography_illustration
  polarity: mixed
  page_or_region: About — biological-vs-chronological-age scatter plot
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/about/tile-03-y03660.png
  claim: The biological-vs-chronological-age scatter plot is custom-built and on-brand in color, but its craft is generic: a plain stippled point cloud with thin unlabeled axes and no legend or trend line.
  visible_tells:
  - green-to-orange dot gradient plotted on bare X/Y axes labeled only 'Chronological age' and 'Biological age'
  - no trend line, gridlines, or callouts to guide reading
  confidence: medium
- id: iconography_05
  family: iconography_illustration
  polarity: strong
  page_or_region: BioAge test — 'Tracking your BioAge over time' line chart
  tile_path: store/agelessrx-com/captures/2026-05-31/tiles/bioage_test/tile-02-y02440.png
  claim: The Calendar-Age vs Biological-Age line chart is a clean custom diagram with year columns, numbered node markers, and a dashed projection to a '?' future point that communicates the diverging-gap concept clearly.
  visible_tells:
  - two labeled crossing lines with circular age-number nodes (40/41/39/42) across 2022-2024 columns
  - dashed teal segment ending in a '?' node to imply the next reading
  confidence: high
```

## Provenance

Tiles read: homepage (4) + treatments (8) + about (7) + metformin (7) + glp1_support (5) + bioage_test (4) from `captures/2026-05-31/tiles/` — all 35 active, no exclusions, no Tier-B re-render (the capture was clean; the `2026-06-03` and `2026-06-04` captures hold product-catalog and logo refreshes with no homepage, so the homepage-bearing `2026-05-31` set was tiled). Of 54 raw mined cards the judge accepted 38; this file ships a curated 19 spanning all four families and a strong/mixed/poor mix, dropping redundant strong cards while keeping every weak-edge tell. Run provenance: generated from **Claude Code on macOS with Claude Opus 4.8, Extra effort**, on 2026-06-14, from the active tiles only — no `profile.md`, dossier, Notion, or live web was consulted (the read is blind by construction). Snapshot caveat: reflects the 2026-05-31 capture; the live site changes.
