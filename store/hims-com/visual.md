---
schema_version: "1.0"
domain: hims.com
captured_at: 2026-06-15
source_capture: 2026-05-30
qa_status: exclusions-noted
---

## Visual & brand impression

Hims runs a confident, well-tokened brand system that frays at the seams. A controlled warm-brown/caramel palette anchors the heroes [color_01] and recurs unchanged across pages [color_10], closing on a full-black footer where the oversized 'hims' wordmark carries the identity with no color noise [color_08]. Typography is disciplined where it counts — large size-contrast heroes [typography_01], clean multi-level card scaffolding [typography_03] — and the core components (the feature-comparison table [layout_04], product-card rows [layout_05], a consistent check/dash icon vocabulary [iconography_04]) plus custom medical illustration [iconography_02][iconography_03] read as a maintained system. But the finish slips: catalog and doctor photography break the warm palette [color_05][color_11], mid-hierarchies flatten [typography_05][typography_08], components clip or collide [layout_11][layout_06][layout_10], and some diagrams turn crude [iconography_07][iconography_08].

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: homepage / hero
  tile_path: store/hims-com/captures/2026-05-30/tiles/homepage/tile-00-y00000.png
  claim: The hero deploys a clean two-level hierarchy — a large-weight display headline over small, unbolded nav and pill labels — so size contrast alone carries the read order without color or decoration.
  visible_tells:
  - '"The care you''ve always deserved" renders at roughly 3-4x the weight and size of any surrounding copy'
  - Nav items and category pills sit at caption scale, creating a wide size gap that is immediately readable at a glance
  confidence: high
  contrast_with: store/hims-com/captures/2026-05-30/tiles/homepage/tile-05-y06100.png
- id: typography_03
  family: typography_hierarchy
  polarity: strong
  page_or_region: labs / three-step process section
  tile_path: store/hims-com/captures/2026-05-30/tiles/labs/tile-01-y01220.png
  claim: A three-level hierarchy — display headline, card title, card body — is held consistently across three parallel cards with no orphaned levels, demonstrating disciplined typographic scaffolding.
  visible_tells:
  - '"Turn your body''s data into a clear plan" is the largest text, with the italic orange accent on "clear plan"'
  - Card titles (e.g. "Set a quick appointment") are medium-weight at a middle size, card bodies are light and smaller — all three tiers visually distinct
  confidence: high
  contrast_with: store/hims-com/captures/2026-05-30/tiles/labs/tile-02-y02440.png
- id: typography_05
  family: typography_hierarchy
  polarity: mixed
  page_or_region: homepage / doctor team section
  tile_path: store/hims-com/captures/2026-05-30/tiles/homepage/tile-05-y06100.png
  claim: The medical-team grid stacks several type levels — section headline, title badge, doctor name, role descriptor, bio — without enough size or weight differentiation between the doctor name and the role descriptor, making the mid-hierarchy ambiguous.
  visible_tells:
  - '"The best care by the best in medicine" headline is correctly prominent'
  - Doctor name and title-badge text (e.g. "Dr. Craig Primack, MD" / "Head of Weight Loss...") are close in weight and size; scanning five cards in a row exposes the flattening
  confidence: medium
- id: typography_08
  family: typography_hierarchy
  polarity: poor
  page_or_region: testosterone / supplement cards
  tile_path: store/hims-com/captures/2026-05-30/tiles/testosterone/tile-03-y03660.png
  claim: The supplement cards (Zinc, Vitamins B6 & B12, L-Arginine) flatten to a two-level system — card title and a single footnote-scale benefit line — with no mid-tier copy, reading as typographically thin rather than deliberately minimal.
  visible_tells:
  - Card title "Zinc" is the only substantial text; "to support healthy T levels" sits at footnote scale below with no size/weight transition that reads as intentional hierarchy
  - All three cards repeat the same collapse, so the pattern reads as omission, not design choice
  confidence: medium
  contrast_with: store/hims-com/captures/2026-05-30/tiles/testosterone/tile-06-y07320.png
- id: layout_04
  family: layout_composition_components
  polarity: strong
  page_or_region: labs / comparison table
  tile_path: store/hims-com/captures/2026-05-30/tiles/labs/tile-04-y04880.png
  claim: The feature-comparison table uses strict row-height uniformity, consistent column widths, and a two-state icon system (filled check vs. muted dash) that reads as a finished UI component.
  visible_tells:
  - Row heights are identical across all visible rows
  - Check and dash icons align precisely to the column centerline in every row
  confidence: high
- id: layout_05
  family: layout_composition_components
  polarity: strong
  page_or_region: testosterone / product card row
  tile_path: store/hims-com/captures/2026-05-30/tiles/testosterone/tile-01-y01220.png
  claim: 'The product card row — Testosterone Rx+, Injectable TRT, Oral TRT — is a tightly systemized component: badge, product image, name, subhead, and CTA repeat at the same vertical positions across all three cards.'
  visible_tells:
  - Badge pill sits at the identical top-left corner position on each card
  - Product render floats at center with equal negative space above and below across cards
  confidence: high
- id: layout_06
  family: layout_composition_components
  polarity: mixed
  page_or_region: sexual_health / product card carousel
  tile_path: store/hims-com/captures/2026-05-30/tiles/sexual_health/tile-03-y03660.png
  claim: The product carousel crops the rightmost card mid-bleed without a clear scroll affordance, leaving an unresolved right edge that reads as accidental truncation rather than intentional peek composition.
  visible_tells:
  - Rightmost product card is cut off at roughly 60% of its width with no fade or scroll indicator
  - The 'Buy now' / 'Learn more' CTAs on the cut card are partially hidden
  confidence: medium
- id: layout_10
  family: layout_composition_components
  polarity: poor
  page_or_region: labs / condition-disease text section
  tile_path: store/hims-com/captures/2026-05-30/tiles/labs/tile-02-y02440.png
  claim: The large stacked disease-name block has the 'Out of range' badge composited over it with no consistent anchor point, producing a visually unresolved collision between the badge and the flowing text.
  visible_tells:
  - '''Out of range'' badge overlaps the running disease text mid-block with no clear spatial logic'
  - The flowing disease-name block has no grid containment — line breaks appear arbitrary
  confidence: medium
- id: layout_11
  family: layout_composition_components
  polarity: mixed
  page_or_region: sexual_health / 'Why men choose Hims' tab section
  tile_path: store/hims-com/captures/2026-05-30/tiles/sexual_health/tile-05-y06100.png
  claim: The horizontal tab row clips its fourth label before the viewport edge, suggesting the tab component was not built with overflow handling for its actual content length.
  visible_tells:
  - Fourth tab label 'A simple process with' is truncated mid-phrase at the right edge
  - No ellipsis or scroll indicator is shown
  confidence: high
  contrast_with: store/hims-com/captures/2026-05-30/tiles/labs/tile-01-y01220.png
- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: homepage / hero
  tile_path: store/hims-com/captures/2026-05-30/tiles/homepage/tile-00-y00000.png
  claim: The homepage opens on a controlled warm-brown palette — the hero panels share the same deep caramel ground — creating an immediate tonal identity rather than a generic white field.
  visible_tells:
  - 'Left panel: product shot on a solid warm-brown ground'
  - 'Right panel: man photographed against an identically toned warm-brown environment — same hue family, not coincidental'
  confidence: high
- id: color_05
  family: color_brand_imagery
  polarity: mixed
  page_or_region: sexual_health / product catalog
  tile_path: store/hims-com/captures/2026-05-30/tiles/sexual_health/tile-01-y01220.png
  claim: The sexual-health catalog presents pill and product imagery as studio cut-outs on flat white card backgrounds — competent but generic, with none of the warm-brown tonal carry seen across the rest of the site.
  visible_tells:
  - '''h'' mint, coral pill, and gray ''hims'' tablet photographed on pure white — no environmental color carry from the brand palette'
  - Flat studio cut-outs with no tonal warmth from the dominant brown system used elsewhere
  confidence: high
  contrast_with: store/hims-com/captures/2026-05-30/tiles/labs/tile-00-y00000.png
- id: color_08
  family: color_brand_imagery
  polarity: strong
  page_or_region: homepage / footer brand statement
  tile_path: store/hims-com/captures/2026-05-30/tiles/homepage/tile-07-y08487.png
  claim: The footer closes on a full-black field with the 'hims' wordmark rendered in near-black charcoal at massive scale — a confident brand-statement moment that withholds color and lets letterform and scale carry the identity.
  visible_tells:
  - Full-bleed black field — nothing else on the page uses pure black at this scale
  - Wordmark 'hims' fills the viewport width in a slightly lighter charcoal, creating depth with no color noise
  confidence: high
  contrast_with: store/hims-com/captures/2026-05-30/tiles/labs/tile-00-y00000.png
- id: color_10
  family: color_brand_imagery
  polarity: strong
  page_or_region: weight_loss / hero
  tile_path: store/hims-com/captures/2026-05-30/tiles/weight_loss/tile-00-y00000.png
  claim: The weight-loss hero repeats the warm-sand-to-ochre gradient used on homepage and labs, confirming this is a cross-page palette constant rather than per-section art direction.
  visible_tells:
  - 'Gradient field: same warm-sand tone as the labs hero, on a different page and product category'
  - Typography color (dark on warm ground) matches the homepage type treatment
  confidence: high
  contrast_with: store/hims-com/captures/2026-05-30/tiles/sexual_health/tile-01-y01220.png
- id: color_11
  family: color_brand_imagery
  polarity: mixed
  page_or_region: homepage / medical staff section
  tile_path: store/hims-com/captures/2026-05-30/tiles/homepage/tile-05-y06100.png
  claim: The doctor grid uses neutral white cards with cool-toned headshot photography, creating a visual-temperature break from the warm-brand sections above and below it.
  visible_tells:
  - 'White card backgrounds: zero warm-palette carry'
  - 'Doctor headshots: neutral-to-cool ambient light, no tonal alignment with the amber lifestyle photography in hero sections'
  confidence: high
  contrast_with: store/hims-com/captures/2026-05-30/tiles/homepage/tile-03-y03660.png
- id: iconography_02
  family: iconography_illustration
  polarity: strong
  page_or_region: labs / three-step process illustration cards
  tile_path: store/hims-com/captures/2026-05-30/tiles/labs/tile-01-y01220.png
  claim: The three-step section uses custom spot illustrations — an appointment-confirmation UI mockup, a cholesterol chart, and a habit-tracking graphic — that are stylistically cohesive and purpose-built rather than generic stock.
  visible_tells:
  - Each card holds a distinct product-UI illustration (calendar chip; bar chart labeled 'Cholesterol/HDL Ratio'; habit icons for Medication/Habits/Exercise/Nutrition/Sleep) in the same warm-neutral palette
  - Icons within the habit card use consistent circular framing and identical stroke weight
  confidence: high
  contrast_with: store/hims-com/captures/2026-05-30/tiles/sexual_health/tile-04-y04880.png
- id: iconography_03
  family: iconography_illustration
  polarity: strong
  page_or_region: labs / cancer-screening body diagram
  tile_path: store/hims-com/captures/2026-05-30/tiles/labs/tile-05-y06100.png
  claim: The cancer-screening section uses a custom translucent body silhouette with a warm-orange glow and a 'No cancer signal detected' badge, a purpose-built medical diagram rather than a licensed stock illustration.
  visible_tells:
  - Semi-transparent human figure with a warm-orange radial glow centered on the torso, not a clip-art outline
  - Green checkmark badge overlaid on the figure uses the same rounded-rectangle brand-green token as comparison-table checkmarks elsewhere
  confidence: high
  contrast_with: store/hims-com/captures/2026-05-30/tiles/labs/tile-04-y04880.png
- id: iconography_04
  family: iconography_illustration
  polarity: strong
  page_or_region: labs / comparison table check & dash icons
  tile_path: store/hims-com/captures/2026-05-30/tiles/labs/tile-04-y04880.png
  claim: The feature-comparison table applies a disciplined two-icon vocabulary — filled brown-circle check for included, grey dash-in-circle for excluded — consistently across every row without visual drift.
  visible_tells:
  - Many consecutive rows each use exactly the same filled-circle check in the left column and the same grey dash-circle in the right, with no size or alignment variation
  confidence: high
- id: iconography_07
  family: iconography_illustration
  polarity: poor
  page_or_region: homepage / SNAC mechanism diagram
  tile_path: store/hims-com/captures/2026-05-30/tiles/homepage/tile-02-y02440.png
  claim: The 'SNAC technology' diagram illustrates drug absorption with a scatter-dot particle graphic over a body-section silhouette, but the silhouette reads as undifferentiated dark blobs with no legible anatomical structure.
  visible_tells:
  - A dark silhouette with white/grey particle scatter and a small 'SNAC technology' label — the body-section art is crude and the particle dispersion lacks directional clarity
  confidence: high
  contrast_with: store/hims-com/captures/2026-05-30/tiles/labs/tile-05-y06100.png
- id: iconography_08
  family: iconography_illustration
  polarity: poor
  page_or_region: labs / 'Doctor-trusted treatment plans' spot illustration
  tile_path: store/hims-com/captures/2026-05-30/tiles/labs/tile-07-y08540.png
  claim: The 'Doctor-trusted treatment plans' cell uses a minimal abstract two-shape illustration that is too generic to carry iconographic meaning and risks reading as clip-art filler.
  visible_tells:
  - The cell shows two small soft-edged organic shapes in muted warm tones — no readable icon, product shape, or diagram logic
  confidence: medium
  contrast_with: store/hims-com/captures/2026-05-30/tiles/labs/tile-01-y01220.png
```

## Provenance

Tiles read: homepage (7; tile-01 excluded) + sexual_health (10) + weight_loss (9) + labs (12) + testosterone (10) from `captures/2026-05-30/tiles/` — 48 active tiles.

**Exclusion:** `homepage/tile-01` — a cookie-consent banner overlays the GLP-1 product-card row. The same consent banner recurs across most homepage/sexual_health tiles, but on every kept card the load-bearing evidence sits in clean bands above or below it; no accepted claim depends on a banner-obscured region. A duplicate capture (the `how_it_works` URL rendered the weight-loss page) was dropped before tiling.

**Tier-B not used:** a browser re-render of the homepage hero was attempted to recover a banner-free capture but was blocked by Cloudflare bot protection, so the cached 2026-05-30 capture stands → `qa_status: exclusions-noted`.

Mined blind + judged per [`/visual-evidence`](../../skills/visual-evidence/SKILL.md): four family miners (Sonnet) saw only the tile paths — no dossier, no web. The Opus judge verified each card against its cited tile and pruned 52 raw → 42 accepted, rejecting tile mis-citations, a hallucinated "teal glow" (the tile is warm-orange), and a card judging the cookie banner itself. This file curates the 19 most distinct, non-redundant of those accepted cards across the four families (10 strong / 5 mixed / 4 poor), collapsing claim-clusters (e.g. five "warm palette is consistent" cards → two).

Snapshot caveat: reflects the 2026-05-30 capture; the live site changes.
