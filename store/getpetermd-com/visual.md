---
schema_version: "1.0"
domain: getpetermd.com
captured_at: 2026-06-17
source_capture: 2026-06-04
qa_status: exclusions-noted
---

## Visual & brand impression

PeterMD reads like a commerce-first health catalog: a bright yellow accent and polished medication/app assets anchor the brand [color_01][color_02][color_03]. Its strongest surfaces are reusable systems - card grids, product heroes, comparison tables, and pricing grids [layout_01][layout_08][layout_10][layout_11]. Typography is mostly clear and scan-friendly, especially in heroes and process sections, but small callouts and dense comparison tables expose the limits of the system [typography_01][typography_03][typography_07][typography_09]. The palette sprawls when green commerce CTAs, badge colors, and service tints pile onto yellow [color_04][color_05][color_06]. The weak spots are generic instructional photos and gimmicky carousel illustrations that undercut the polished product renders [color_08][iconography_06][iconography_07].

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: homepage hero
  tile_path: store/getpetermd-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png
  claim: The hero establishes a clear primary hierarchy with a large headline, smaller subhead, compact CTA, and secondary credibility proof.
  visible_tells:
  - The headline "Your Solution For / Weight Loss" is much larger than the supporting "Modern men's healthcare" line below it.
  confidence: high
- id: typography_02
  family: typography_hierarchy
  polarity: mixed
  page_or_region: homepage labs promo cards
  tile_path: store/getpetermd-com/captures/2026-06-04/tiles/homepage/tile-01-y01220.png
  claim: The promo cards keep their headings readable, but the smallest background and biomarker text competes with the foreground copy.
  visible_tells:
  - The "Test 133+ Biomarkers" card places white label text over a repeated biomarker word field and a person image.
  confidence: medium
- id: typography_03
  family: typography_hierarchy
  polarity: poor
  page_or_region: homepage sexual wellness product card
  tile_path: store/getpetermd-com/captures/2026-06-04/tiles/homepage/tile-06-y07320.png
  claim: Tiny callout labels around the product render fall below the page's otherwise readable text scale.
  visible_tells:
  - Labels such as "Be ready anytime" and "Boost blood flow" are very small white text on the dark blue product graphic.
  confidence: high
  contrast_with: store/getpetermd-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png
- id: typography_04
  family: typography_hierarchy
  polarity: strong
  page_or_region: homepage How It Works cards
  tile_path: store/getpetermd-com/captures/2026-06-04/tiles/homepage/tile-10-y12200.png
  claim: The step layout uses strong scale contrast between the step label, oversized heading, and bullet list.
  visible_tells:
  - "STEP 1. GET BLOODWORK" is small and gray while "Start With A Complete Picture Of Your Health" is oversized black type.
  confidence: high
- id: typography_05
  family: typography_hierarchy
  polarity: strong
  page_or_region: TRT product hero
  tile_path: store/getpetermd-com/captures/2026-06-04/tiles/trt_injectable/tile-00-y00000.png
  claim: The product hero uses a clear purchase hierarchy from headline to product name, body copy, benefit bullets, and pricing rows.
  visible_tells:
  - The monthly price rows use large prices with smaller plan pills and savings badges.
  confidence: high
- id: typography_06
  family: typography_hierarchy
  polarity: strong
  page_or_region: TRT journey timeline
  tile_path: store/getpetermd-com/captures/2026-06-04/tiles/trt_injectable/tile-03-y03660.png
  claim: The journey section stages a clear narrative hierarchy with month badges, larger step headings, and smaller supporting text.
  visible_tells:
  - "Month 1", "Month 2", and "Month 3" badges align with step headings such as "Set The Stage" and "Build Momentum".
  confidence: high
- id: typography_07
  family: typography_hierarchy
  polarity: mixed
  page_or_region: TRT comparison table
  tile_path: store/getpetermd-com/captures/2026-06-04/tiles/trt_injectable/tile-04-y04880.png
  claim: The comparison table is readable but dense because many row labels and icons repeat with similar visual weight.
  visible_tells:
  - Rows such as "Veteran & Faith Based Values", "Medications Included", and "High Patient Satisfaction" repeat down the left column.
  confidence: high
- id: typography_08
  family: typography_hierarchy
  polarity: strong
  page_or_region: sildenafil explainer panel
  tile_path: store/getpetermd-com/captures/2026-06-04/tiles/sildenafil/tile-01-y01220.png
  claim: The dark explainer panel maintains legible type over a solid color field with clear scale contrast.
  visible_tells:
  - "What Is Sildenafil and How Does It Work?" appears as large white type above smaller white paragraph blocks and a yellow CTA.
  confidence: high
- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: homepage hero service-card mosaic
  tile_path: store/getpetermd-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png
  claim: The homepage opens with a disciplined service-card grid that keeps mixed card sizes aligned and visually related.
  visible_tells:
  - Two wide cards sit on the same top row, while three smaller cards below share consistent gutters and top-aligned labels.
  confidence: high
- id: layout_02
  family: layout_composition_components
  polarity: mixed
  page_or_region: homepage labs feature cards
  tile_path: store/getpetermd-com/captures/2026-06-04/tiles/homepage/tile-01-y01220.png
  claim: The labs feature area has an ambitious layered composition, but the right card becomes visually crowded.
  visible_tells:
  - The athlete cutout overlaps the biomarker-word field inside the "Test 133+ Biomarkers" card.
  confidence: medium
- id: layout_03
  family: layout_composition_components
  polarity: strong
  page_or_region: homepage program-section system
  tile_path: store/getpetermd-com/captures/2026-06-04/tiles/homepage/tile-02-y02440.png
  claim: The large program modules use a repeatable section system with a clear hero layer above nested content cards.
  visible_tells:
  - The testosterone panel uses a wide rounded color field, left title block, central human figure, and two aligned lower cards.
  confidence: high
  contrast_with: store/getpetermd-com/captures/2026-06-04/tiles/homepage/tile-04-y04880.png
- id: layout_04
  family: layout_composition_components
  polarity: mixed
  page_or_region: homepage How It Works cards
  tile_path: store/getpetermd-com/captures/2026-06-04/tiles/homepage/tile-10-y12200.png
  claim: The How It Works card system is orderly, but the modules are much taller than their visible content.
  visible_tells:
  - Step 1 leaves a large empty lower half inside the bordered card after the text list and image.
  confidence: high
- id: layout_05
  family: layout_composition_components
  polarity: mixed
  page_or_region: homepage testimonial band
  tile_path: store/getpetermd-com/captures/2026-06-04/tiles/homepage/tile-12-y14640.png
  claim: The testimonial block has clean centering, but the review card feels underfilled for its width.
  visible_tells:
  - A single short review snippet occupies the top-left of a very wide white card with large unused interior space.
  confidence: high
- id: layout_06
  family: layout_composition_components
  polarity: strong
  page_or_region: about trust-stat row
  tile_path: store/getpetermd-com/captures/2026-06-04/tiles/about/tile-01-y01220.png
  claim: The trust-stat row is a tidy repeated component system.
  visible_tells:
  - Four icon-and-label blocks share the same baseline and are separated by evenly spaced vertical rules.
  confidence: high
- id: layout_07
  family: layout_composition_components
  polarity: mixed
  page_or_region: about health journey timeline
  tile_path: store/getpetermd-com/captures/2026-06-04/tiles/about/tile-03-y03660.png
  claim: The journey timeline is legible, but its density is lopsided.
  visible_tells:
  - The left half holds only a headline and button while all numbered step content is stacked on the right side of the vertical line.
  confidence: high
- id: layout_08
  family: layout_composition_components
  polarity: strong
  page_or_region: TRT product hero
  tile_path: store/getpetermd-com/captures/2026-06-04/tiles/trt_injectable/tile-00-y00000.png
  claim: The TRT product hero is a disciplined commerce layout with clear hierarchy and aligned purchase controls.
  visible_tells:
  - The product image occupies the left column while headline, benefits, pricing rows, CTA, and reviews stack cleanly in the right column.
  confidence: high
  contrast_with: store/getpetermd-com/captures/2026-06-04/tiles/sildenafil/tile-00-y00000.png
- id: layout_09
  family: layout_composition_components
  polarity: poor
  page_or_region: sildenafil benefit carousel
  tile_path: store/getpetermd-com/captures/2026-06-04/tiles/sildenafil/tile-02-y02440.png
  claim: The benefit carousel looks underbuilt because the content occupies only a small part of a large panel.
  visible_tells:
  - A small banana-and-icon graphic sits near the center-left of a huge light-gray rounded panel with wide empty space around it.
  confidence: high
  contrast_with: store/getpetermd-com/captures/2026-06-04/tiles/tirzepatide/tile-02-y02440.png
- id: layout_10
  family: layout_composition_components
  polarity: strong
  page_or_region: tirzepatide comparison table
  tile_path: store/getpetermd-com/captures/2026-06-04/tiles/tirzepatide/tile-03-y03660.png
  claim: The medication comparison table handles a dense matrix with strong column discipline.
  visible_tells:
  - Five product columns align their rounded vertical panels, check/x icons, and row dividers against one shared left label column.
  confidence: high
- id: layout_11
  family: layout_composition_components
  polarity: strong
  page_or_region: sildenafil pricing grid
  tile_path: store/getpetermd-com/captures/2026-06-04/tiles/sildenafil/tile-05-y06100.png
  claim: The sildenafil pricing grid is a finished repeated card system.
  visible_tells:
  - Four product cards share equal image blocks, title placement, price bands, divider rules, and green add-to-cart buttons.
  confidence: high
  contrast_with: store/getpetermd-com/captures/2026-06-04/tiles/trt_injectable/tile-07-y08540.png
- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: homepage hero and treatment cards
  tile_path: store/getpetermd-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png
  claim: The core brand accent is tightly established as neon yellow across primary actions, product packaging, and small UI marks.
  visible_tells:
  - The yellow buttons match the yellow vial caps, vial labels, and check icons.
  confidence: high
- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: TRT product hero
  tile_path: store/getpetermd-com/captures/2026-06-04/tiles/trt_injectable/tile-00-y00000.png
  claim: The product-render system feels ownable, with a PeterMD-labeled vial staged as the main visual asset.
  visible_tells:
  - A large branded testosterone vial floats through a water splash on a controlled teal background.
  confidence: high
  contrast_with: store/getpetermd-com/captures/2026-06-04/tiles/tirzepatide/tile-00-y00000.png
- id: color_03
  family: color_brand_imagery
  polarity: strong
  page_or_region: dashboard and app imagery
  tile_path: store/getpetermd-com/captures/2026-06-04/tiles/homepage/tile-01-y01220.png
  claim: Digital product imagery extends the brand system beyond medication packshots with consistent yellow data accents.
  visible_tells:
  - Dashboard cards, phone UI, charts, and biomarker modules all reuse yellow graph and icon accents over pale cards.
  confidence: high
- id: color_04
  family: color_brand_imagery
  polarity: mixed
  page_or_region: homepage service bands
  tile_path: store/getpetermd-com/captures/2026-06-04/tiles/homepage/tile-04-y04880.png
  claim: Service color coding is useful but stretches the palette beyond a tight brand range.
  visible_tells:
  - A rose-brown weight-loss panel transitions immediately into a blue performance panel, separate from the yellow core accent.
  confidence: high
- id: color_05
  family: color_brand_imagery
  polarity: mixed
  page_or_region: tirzepatide product purchase area
  tile_path: store/getpetermd-com/captures/2026-06-04/tiles/tirzepatide/tile-00-y00000.png
  claim: Bright commerce green competes with the yellow-first accent system in purchase modules.
  visible_tells:
  - A green Add To Cart button sits directly below a yellow offer bar and near teal review stars.
  confidence: high
- id: color_06
  family: color_brand_imagery
  polarity: mixed
  page_or_region: TRT plan cards
  tile_path: store/getpetermd-com/captures/2026-06-04/tiles/trt_injectable/tile-06-y07320.png
  claim: Pricing cards introduce too many secondary badge colors for a disciplined accent hierarchy.
  visible_tells:
  - Green value, blue popularity, yellow savings chips, and green cart buttons appear in the same pricing section.
  confidence: high
- id: color_07
  family: color_brand_imagery
  polarity: strong
  page_or_region: comparison tables
  tile_path: store/getpetermd-com/captures/2026-06-04/tiles/tirzepatide/tile-03-y03660.png
  claim: Comparison graphics form a disciplined reusable subsystem.
  visible_tells:
  - The table uses a pale-yellow frame, black field, white selected column, and consistent green/red outcome symbols.
  confidence: high
  contrast_with: store/getpetermd-com/captures/2026-06-04/tiles/sildenafil/tile-03-y03660.png
- id: color_08
  family: color_brand_imagery
  polarity: mixed
  page_or_region: product three-step process photos
  tile_path: store/getpetermd-com/captures/2026-06-04/tiles/tirzepatide/tile-05-y06100.png
  claim: Instructional imagery looks generic and visually mismatched.
  visible_tells:
  - The blood-draw closeup, laptop consultation scene, and gray-wall portrait use unrelated lighting and settings.
  confidence: high
- id: color_09
  family: color_brand_imagery
  polarity: strong
  page_or_region: founder story block
  tile_path: store/getpetermd-com/captures/2026-06-04/tiles/about/tile-06-y07320.png
  claim: The founder block feels more brand-controlled than the surrounding lifestyle photography.
  visible_tells:
  - A black-and-white portrait sits inside a pale-yellow editorial panel with oversized translucent background lettering.
  confidence: medium
- id: color_10
  family: color_brand_imagery
  polarity: strong
  page_or_region: sildenafil product identity
  tile_path: store/getpetermd-com/captures/2026-06-04/tiles/sildenafil/tile-00-y00000.png
  claim: The sildenafil page establishes a coherent blue/purple product sub-identity.
  visible_tells:
  - Blue PMD tablets are staged on a purple card that matches the sexual-wellness color family.
  confidence: high
  contrast_with: store/getpetermd-com/captures/2026-06-04/tiles/sildenafil/tile-01-y01220.png
- id: iconography_01
  family: iconography_illustration
  polarity: strong
  page_or_region: homepage category cards
  tile_path: store/getpetermd-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png
  claim: The homepage category cards use product graphics as a coherent navigation motif rather than relying on generic category icons.
  visible_tells:
  - Each cream card pairs a category label with a floating product object and a small arrow affordance.
  confidence: high
- id: iconography_02
  family: iconography_illustration
  polarity: mixed
  page_or_region: homepage hero proof points
  tile_path: store/getpetermd-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png
  claim: The supporting icon system is usable but not tightly unified.
  visible_tells:
  - Filled black proof icons sit near green review stars, yellow check badges, and tiny card arrows in the same viewport.
  confidence: high
- id: iconography_03
  family: iconography_illustration
  polarity: mixed
  page_or_region: homepage How It Works biomarker mockups
  tile_path: store/getpetermd-com/captures/2026-06-04/tiles/homepage/tile-10-y12200.png
  claim: The biomarker graphics have brand polish but mostly function as decorative props.
  visible_tells:
  - The "133+" card and Month 01 chart are visually crisp, but their labels and axes are too small to read as explanatory data.
  confidence: high
- id: iconography_04
  family: iconography_illustration
  polarity: mixed
  page_or_region: about trust icon row
  tile_path: store/getpetermd-com/captures/2026-06-04/tiles/about/tile-01-y01220.png
  claim: The trust icons read as competent stock outline pictograms rather than a distinctive brand set.
  visible_tells:
  - The row uses generic hand-money, chat-star, headset, and crossed-eye outlines.
  confidence: high
- id: iconography_05
  family: iconography_illustration
  polarity: mixed
  page_or_region: about values cards
  tile_path: store/getpetermd-com/captures/2026-06-04/tiles/about/tile-02-y02440.png
  claim: The values section repeats one icon treatment across unrelated ideas.
  visible_tells:
  - Faith-centered care, quality, and affordability all use the same yellow check-in-circle badge.
  confidence: high
- id: iconography_06
  family: iconography_illustration
  polarity: poor
  page_or_region: tirzepatide modern approach carousel
  tile_path: store/getpetermd-com/captures/2026-06-04/tiles/tirzepatide/tile-02-y02440.png
  claim: The body-effect illustration drops below the finish of the product renders.
  visible_tells:
  - A gray torso silhouette with a yellow chest glow and simple gauge sits in a mostly empty pale panel.
  confidence: high
  contrast_with: store/getpetermd-com/captures/2026-06-04/tiles/tirzepatide/tile-00-y00000.png
- id: iconography_07
  family: iconography_illustration
  polarity: poor
  page_or_region: sildenafil erectile-support carousel
  tile_path: store/getpetermd-com/captures/2026-06-04/tiles/sildenafil/tile-02-y02440.png
  claim: The visual metaphor feels gimmicky compared with the surrounding pharmaceutical product polish.
  visible_tells:
  - A cartoon hand grips a banana beneath a small stopwatch icon in a sparse gray carousel panel.
  confidence: high
  contrast_with: store/getpetermd-com/captures/2026-06-04/tiles/sildenafil/tile-00-y00000.png
```

## Provenance

Tiles read: homepage (15) + about (8 active) + how_it_works (2) + trt_injectable (10) + tirzepatide (7) + sildenafil (7) = 49 active tiles from `captures/2026-06-04/tiles/`. **Exclusions:** `store/getpetermd-com/captures/2026-06-04/tiles/about/tile-05-y06100.png` - probable lazy-load/team-card gap; the tile is almost entirely blank white space between the team heading and the founder block, so it is unusable as design evidence. **Tier-B:** not used; the cached Tier-A tiles were otherwise clean enough, with no modal/cookie overlay, black media block, or grey hero requiring browser re-render. Mined blind + judged per [`/visual-evidence`](../../skills/visual-evidence/SKILL.md): four family miners saw only the tiles, not the dossier or live web; the judge pruned duplicate and capture-scope cards, especially the thin `how_it_works` page calls and cross-family repeats around product heroes, comparison tables, and carousel illustrations. Every `poor` structural/illustration card was spot-checked against its native tile; the cited defects are visible page states, not the excluded lazy-load gap. Snapshot caveat: visual evidence reflects the 2026-06-04 captured tiles; the live site may have changed.
