---
schema_version: "1.0"
domain: mydrhank.com
captured_at: 2026-06-16
source_capture: 2026-06-03
qa_status: recapture-used
---

## Visual & brand impression

A locked navy-and-white palette governs every page — wordmark, lone CTA, and footer one dark family [color_01][color_03] — and every product render carries the same cobalt label [color_02], so it reads disciplined. The type system is the real strength: a clean hero hierarchy [typography_01] plus a repeatable PDP pattern of all-caps labels, serif headings, and jumbo clinical-stat callouts [typography_02][typography_03], on consistent grids and reusable components — floated hero card [layout_01], two-column feature template [layout_02], a purposeful navy line-chart [iconography_01]. It falls on imagery and icons: recycled multi-source stock with mismatched grading [color_06][color_08], a clipboard among people-photos [layout_09], an unanchored powder-blue card fill [color_04], and no bespoke iconography — photos and bare numerals stand in [iconography_04][iconography_03]. Competent template, shallow image layer.

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: 'Homepage hero'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/homepage/tile-00-y00000.png
  claim: 'The hero establishes a clear three-level hierarchy — large italic-serif display headline, smaller sans-serif subhead, and lighter body copy in the product card — with confident size and weight contrast at each step.'
  visible_tells:
  - 'Large italic serif headline (''Personalized care for weight, longevity & sexual wellness'') dominates the viewport'
  - 'Smaller sans-serif line below (''Clinically tracked treatment plans...'') reads as a distinct subhead tier'
  - 'Body copy in the GLP-1 product card beneath is visibly smaller and lighter again'
  confidence: high
  contrast_with: store/mydrhank-com/captures/2026-06-03/tiles/homepage/tile-02-y02440.png
- id: typography_02
  family: typography_hierarchy
  polarity: strong
  page_or_region: 'PDP science sections (semaglutide, NAD+)'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/pdp-compounded-semaglutide/tile-01-y01220.png
  claim: 'Science content uses a disciplined four-part pattern — small all-caps ''SCIENCE'' label, large serif heading, bolded bullet sub-heads, regular body — applied consistently across PDPs and legible without imagery.'
  visible_tells:
  - 'All-caps ''SCIENCE'' label in small tracking above ''How Injectable Semaglutide Works'''
  - 'Serif heading is substantially larger than the body text beneath it'
  - 'Bullet sub-heads (e.g., ''Activates GLP-1 receptors'') are bolded and sit as a distinct mid-tier above their explanatory lines'
  confidence: high
  contrast_with: store/mydrhank-com/captures/2026-06-03/tiles/pdp-nad-injection/tile-01-y01220.png
- id: typography_03
  family: typography_hierarchy
  polarity: strong
  page_or_region: 'PDP data callouts (semaglutide and NAD+)'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/pdp-compounded-semaglutide/tile-02-y02440.png
  claim: 'Jumbo percentage/numeral callouts (''~15%'', ''24%'', ''50%'', ''6x'') with smaller inline descriptor labels create a deliberate stat tier reserved for clinical figures, applied identically across both PDPs.'
  visible_tells:
  - '''~15%'' set at display scale with ''average body weight loss at 68 weeks'' in small text beside it'
  - 'Same treatment repeated for ''24%'' on the semaglutide PDP and ''50%'' / ''6x'' on the NAD+ PDP'
  confidence: high
  contrast_with: store/mydrhank-com/captures/2026-06-03/tiles/pdp-nad-injection/tile-03-y03660.png
- id: typography_04
  family: typography_hierarchy
  polarity: strong
  page_or_region: 'Category longevity — ''How it works'' process section'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/category-longevity/tile-01-y00669.png
  claim: 'The process section uses a consistent three-level reading order — small all-caps ''PROCESS'' label, medium serif ''How it works'' title, then heavier step headings over lighter body — signalling a type system rather than ad-hoc sizing.'
  visible_tells:
  - 'Small all-caps ''PROCESS'' label above the ''How it works'' serif heading'
  - 'Step titles (e.g., ''Complete your intake'', ''Provider review'') are heavier than their supporting body copy'
  - 'Numbered circles anchor each step without competing with the type'
  confidence: high
- id: typography_05
  family: typography_hierarchy
  polarity: mixed
  page_or_region: 'Homepage ''Find your care plan'' category cards (mid-page)'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/homepage/tile-02-y02440.png
  claim: 'Category cards stack a small all-caps label, serif card title, and one-line descriptor, but the size jump between label and title is narrow and the descriptor is only marginally smaller, compressing scannable contrast at a glance.'
  visible_tells:
  - 'Category labels (''WELLNESS'', ''STRENGTH'', ''LONGEVITY'') sit close in size to the card headline below'
  - 'One-line descriptor under each headline is only slightly smaller, flattening the scale'
  confidence: medium
  contrast_with: store/mydrhank-com/captures/2026-06-03/tiles/homepage/tile-00-y00000.png
- id: typography_06
  family: typography_hierarchy
  polarity: mixed
  page_or_region: 'Homepage mid-section feature blocks (growth hormone, NAD+, hair)'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/homepage/tile-03-y03660.png
  claim: 'Feature sections reuse the same large serif headline face as the hero (''Optimize your body''s natural growth hormone''), so secondary feature blocks carry no typographic signal that they are subordinate to the page-level headline.'
  visible_tells:
  - '''Optimize your body''s natural growth hormone'' is set in the same large serif weight as the hero headline'
  - 'No size or weight step differentiates a mid-page feature heading from a top-level page heading'
  confidence: medium
  contrast_with: store/mydrhank-com/captures/2026-06-03/tiles/homepage/tile-00-y00000.png
- id: typography_07
  family: typography_hierarchy
  polarity: poor
  page_or_region: 'Category weight-loss — disclaimer/footnote block below product grid'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/category-weight-loss/tile-02-y02440.png
  claim: 'Disclaimer copy below the product grid is set at a scale that resolves as an undifferentiated grey mass — no internal hierarchy separates the lead disclaimer from the run-on qualifications.'
  visible_tells:
  - 'Dense paragraph of disclaimer copy reads as one continuous grey block with no line or sentence differentiation at native resolution'
  - 'No weight, spacing, or size cue separates the opening disclaimer from the legal qualifications that follow'
  confidence: medium
- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: 'Homepage hero — floated GLP-1 product card'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/homepage/tile-00-y00000.png
  claim: 'The hero''s floated GLP-1 card is cleanly inset with even internal padding, left-aligned checklist rows, and a contained product image — the component reads as finished, not assembled.'
  visible_tells:
  - 'Card sits in a light inset box with even padding on all four sides'
  - 'Checklist rows use consistent left-aligned check glyphs with uniform line spacing'
  - 'GLP-1 vial image sits to the right within the card without clipping or overflow'
  confidence: high
- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: 'Homepage — repeating two-column feature template (Sexual Health, Growth Hormone, NAD+, Hair)'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/homepage/tile-03-y03660.png
  claim: 'Sequential feature sections hold a stable two-column split — text/CTA one side, rounded editorial photo the other — with matched column widths, equal-height photo crops, and alternating white/grey backgrounds for rhythm without layout change.'
  visible_tells:
  - 'Growth-hormone section mirrors the Sexual Health and NAD+ sections: text column beside a rounded-corner photo of equal height'
  - 'Section backgrounds alternate white and pale grey across instances while the column structure stays fixed'
  confidence: high
  contrast_with: store/mydrhank-com/captures/2026-06-03/tiles/homepage/tile-04-y04880.png
- id: layout_03
  family: layout_composition_components
  polarity: strong
  page_or_region: 'Homepage — 4-up Sexual Health product card grid'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/homepage/tile-03-y03660.png
  claim: 'The four sexual-health product cards sit on a strict equal-width grid with uniform gutters, vertically centered product renders, and ''Get Started'' buttons aligned to a shared bottom edge.'
  visible_tells:
  - 'All four cards share equal column width with even gutters'
  - 'Product bottle renders are centered at the same vertical position in each card'
  - '''Get Started'' buttons align along the bottom edge across all four cards'
  confidence: high
- id: layout_04
  family: layout_composition_components
  polarity: strong
  page_or_region: 'PDP / category / homepage — shared 4-step ''How it works'' strip'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/homepage/tile-06-y07320.png
  claim: 'The numbered 4-step process strip is a reusable component executed consistently — equal-sized circle badges on a shared baseline, same-size step titles, and body copy that never overflows or collides between columns.'
  visible_tells:
  - 'Four numbered circle badges are equal-sized and aligned to the same vertical baseline'
  - 'Step titles share size and weight across all four columns'
  - 'No step text overflows its column or collides with the adjacent step'
  confidence: high
- id: layout_05
  family: layout_composition_components
  polarity: strong
  page_or_region: 'PDP Compounded Semaglutide — science content stack'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/pdp-compounded-semaglutide/tile-01-y01220.png
  claim: 'The science section stacks heading, bolded bullet rows, a contained chart, and a jumbo-stat callout on a single consistent left margin with clear vertical rhythm between units.'
  visible_tells:
  - 'Heading, bullet sub-heads, chart card, and the ''~15%'' stat all align to the same left edge'
  - 'The ''Average weight loss trajectory'' chart is a full-width bordered card with its title above, matching the second chart card below it'
  confidence: high
  contrast_with: store/mydrhank-com/captures/2026-06-03/tiles/pdp-nad-injection/tile-01-y01220.png
- id: layout_06
  family: layout_composition_components
  polarity: mixed
  page_or_region: 'Homepage ''Find your care plan'' 4-up category cards'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/homepage/tile-02-y02440.png
  claim: 'The four care-plan cards hold consistent widths and card frames, but product-image sizing is uneven — the Sexual Health pill sits tiny in a large empty card while the Sermorelin and NAD+ vials fill most of their card height, breaking visual baseline parity.'
  visible_tells:
  - 'Sexual Health card shows a small pill floating in a large empty card area'
  - 'Sermorelin and NAD+ vials occupy roughly 60-70% of their card height'
  - 'Hair Loss ''Custom Formulations'' bottle is boxed at a different scale again'
  confidence: medium
- id: layout_07
  family: layout_composition_components
  polarity: mixed
  page_or_region: 'Category Weight Loss — top-of-page portrait mosaic'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/category-weight-loss/tile-00-y00000.png
  claim: 'The top portrait mosaic uses a 3-over-2 photo arrangement whose two rows have unequal heights and non-aligned column edges, producing a loose rather than locked composition.'
  visible_tells:
  - 'Top row has three photos; the bottom row has two wider photos that don''t share column boundaries with the top row'
  - 'Bottom-row photo heights read taller than the top row, so the grid feels unstuck'
  confidence: medium
- id: layout_08
  family: layout_composition_components
  polarity: mixed
  page_or_region: 'Homepage / category — weight calculator widget beside stat blocks'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/homepage/tile-01-y01220.png
  claim: 'The calculator widget sits in a white card on the right while the left ''20.9% / 72 wks'' stat blocks have no card background, and the two start at different vertical baselines — they read as separate layers rather than a composed two-column unit.'
  visible_tells:
  - 'Left stat-block text begins lower than the calculator card''s top edge'
  - 'Calculator has a distinct white card background; the stat blocks sit directly on the page with none'
  confidence: medium
- id: layout_09
  family: layout_composition_components
  polarity: poor
  page_or_region: 'Homepage — ''Your health is personal'' 2x2 photo grid'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/homepage/tile-07-y08047.png
  claim: 'The 2x2 editorial grid mixes image types — three people-photos plus one clipboard/document image in the bottom-left cell — breaking the visual consistency of an otherwise symmetrical four-up grid.'
  visible_tells:
  - 'Bottom-left ''Personalized to you'' cell uses a flat clipboard/document image while the other three cells show people photos'
  - 'The clipboard image sits on a pale tint that differs from the photographic cells, making it read as a different asset class'
  confidence: medium
- id: layout_10
  family: layout_composition_components
  polarity: poor
  page_or_region: 'Category Longevity — product card row baseline alignment'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/category-longevity/tile-00-y00000.png
  claim: 'Across the four longevity cards the spray-bottle and injection-vial renders are different heights, so product images do not share a baseline within the row even though the card frames and buttons do.'
  visible_tells:
  - 'NAD+ Injection vial renders visibly taller in its card than the NAD+ Nasal Spray bottle beside it'
  - 'Product names therefore sit at different vertical positions relative to each image''s top edge'
  confidence: medium
- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: 'Homepage hero / nav / CTA'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/homepage/tile-00-y00000.png
  claim: 'The palette is locked to navy and white site-wide, with no decorative tertiary color in the hero, nav, or CTA — the wordmark, single CTA button, and nav links all read as one dark family.'
  visible_tells:
  - 'Navy wordmark logo top-left'
  - 'Single navy CTA button (''Begin Your GLP-1 Plan'') in the hero card'
  - 'Nav links rendered in one dark weight with no color variance'
  confidence: high
- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: 'Homepage / category / PDP — product packaging color'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/homepage/tile-02-y02440.png
  claim: 'Every product render carries the same cobalt-blue label, binding the product image system to the brand palette rather than relying on generic packaging across vials, spray bottles, and pill bottles.'
  visible_tells:
  - 'Sermorelin vial, NAD+ vial, and ''Custom Formulations'' bottle all share the same cobalt-blue label'
  - 'The same cobalt recurs on the longevity spray bottles and the GLP-1 hero vial'
  confidence: high
  contrast_with: store/mydrhank-com/captures/2026-06-03/tiles/category-longevity/tile-00-y00000.png
- id: color_03
  family: color_brand_imagery
  polarity: strong
  page_or_region: 'Footer (homepage, category, and PDP pages)'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/category-longevity/tile-01-y00669.png
  claim: 'The navy footer band — centered white MyDrHank logotype above a certification shield badge — appears identically across homepage, category, and both PDP captures, showing disciplined structural color consistency site-wide.'
  visible_tells:
  - 'Navy footer band with centered white MyDrHank logotype and shield certification badge'
  - 'Same layout and navy fill recurs on the longevity, weight-loss, and PDP footer tiles'
  confidence: high
- id: color_04
  family: color_brand_imagery
  polarity: poor
  page_or_region: 'Homepage — pale-blue product card backgrounds'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/homepage/tile-02-y02440.png
  claim: 'The ''Find your care plan'' cards sit on a pale powder-blue fill that appears nowhere else on the site — not in the footer, hero, buttons, or charts — making it an unanchored accent against the otherwise strict navy/white palette.'
  visible_tells:
  - 'Sexual Health, Sermorelin, NAD+, and Hair Loss cards each sit on a pale blue-grey card background'
  - 'No other UI surface across the captured tiles uses this same fill hue'
  confidence: medium
  contrast_with: store/mydrhank-com/captures/2026-06-03/tiles/homepage/tile-00-y00000.png
- id: color_05
  family: color_brand_imagery
  polarity: mixed
  page_or_region: 'Homepage / category — lifestyle photography'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/homepage/tile-03-y03660.png
  claim: 'Lifestyle photos (man in a gym, couple on a couch) are competently shot and warmly lit but read as generic telehealth stock — bright, softly lit, racially diverse subjects with no owned visual treatment.'
  visible_tells:
  - 'Man touching his hair in a gym setting (tile-03) — could belong to any men''s wellness brand'
  - 'Smiling couple in athletic wear for the NAD+ section (tile-04) is a standard stock typology'
  confidence: high
  contrast_with: store/mydrhank-com/captures/2026-06-03/tiles/homepage/tile-04-y04880.png
- id: color_06
  family: color_brand_imagery
  polarity: mixed
  page_or_region: 'Homepage / PDP — recycled care-team photos'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/homepage/tile-07-y08047.png
  claim: 'The same care-team photos recur across pages with identical crops — the white-coat doctor and the Asian woman holding a phone both appear on the homepage ''Your health is personal'' grid and on the PDP versions of the same block — confirming a shallow reused stock pool rather than original photography.'
  visible_tells:
  - 'Female doctor in a white coat appears in both the homepage grid and the PDP ''Your doctor, not an algorithm'' card with the same crop'
  - 'Smiling woman in a light-blue top holding a phone is reused across the homepage and PDP grids'
  confidence: high
  contrast_with: store/mydrhank-com/captures/2026-06-03/tiles/pdp-nad-injection/tile-03-y03660.png
- id: color_07
  family: color_brand_imagery
  polarity: mixed
  page_or_region: 'Category Weight Loss — portrait-mosaic hero'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/category-weight-loss/tile-00-y00000.png
  claim: 'The weight-loss hero replaces a single image with a five-photo portrait mosaic of diverse faces — a distinctive choice that breaks single-hero convention but reads as assembled stock, since the background treatments and color temperatures differ noticeably across frames.'
  visible_tells:
  - 'Five face portraits tiled above the fold with no copy overlay'
  - 'Background tints and color temperatures differ visibly across the portraits, indicating separate sources'
  confidence: high
- id: color_08
  family: color_brand_imagery
  polarity: poor
  page_or_region: 'PDP — ''How it works: 3 simple steps'' photo row'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/pdp-compounded-semaglutide/tile-03-y03660.png
  claim: 'The three-step row uses un-styled stock crops — a hand holding a phone, a doctor, a cardboard box — with visibly mismatched color grading, breaking palette coherence in a high-visibility template zone repeated across PDPs.'
  visible_tells:
  - 'Step 1: cool-toned phone-in-hand on a light background'
  - 'Step 2: warmer-toned provider photo; Step 3: warm cardboard-box product shot — three different color temperatures in a row'
  - 'The identical three-photo row recurs on the NAD+ PDP, so the mismatch is systematic'
  confidence: high
  contrast_with: store/mydrhank-com/captures/2026-06-03/tiles/pdp-nad-injection/tile-04-y03923.png
- id: iconography_01
  family: iconography_illustration
  polarity: strong
  page_or_region: 'PDP — reusable navy line-chart component (both PDPs)'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/pdp-compounded-semaglutide/tile-02-y02440.png
  claim: 'The PDP data charts are the most purposeful graphics on the site — clean navy data lines, minimal labeled axes, no chart-junk, and a two-series solid/dashed legend (Treatment vs Placebo) on the caloric-intake chart — and the same component recurs on the NAD+ PDP, reading as deliberately designed rather than embedded.'
  visible_tells:
  - '''Reduction in caloric intake'' chart uses solid vs dashed lines with a Treatment/Placebo legend'
  - 'Single descending navy line on a minimal week-based axis for ''Average weight loss trajectory'', each chart in a lightly bordered card'
  - 'NAD+ PDP reuses the identical card size, axis style, and line rendering'
  confidence: medium
  contrast_with: store/mydrhank-com/captures/2026-06-03/tiles/pdp-nad-injection/tile-01-y01220.png
- id: iconography_02
  family: iconography_illustration
  polarity: mixed
  page_or_region: 'PDP — Compounded Semaglutide benefit-list checkmarks'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/pdp-compounded-semaglutide/tile-00-y00000.png
  claim: 'Benefit-list bullets use consistent brand-blue circle-check icons, but the form is a default UI-kit checkmark with no distinctive character — competent and uniform, not crafted.'
  visible_tells:
  - 'Blue circle-check icons repeat identically down the PDP benefit list'
  - 'Icon shape is indistinguishable from a stock UI-kit checkbox glyph'
  confidence: high
- id: iconography_03
  family: iconography_illustration
  polarity: mixed
  page_or_region: 'Process / timeline sections — numerals and dots as the only graphic device'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/homepage/tile-06-y07320.png
  claim: 'The recurring process and ''What to expect'' sections rely entirely on plain circled numerals and small colored dots as their only graphic device — functional anchors with zero illustrative or iconographic lift.'
  visible_tells:
  - '''How it works'' steps use bare circled numerals 1-4 with no accompanying icons'
  - 'PDP ''What to expect'' timeline phases are marked only by a small navy dot before each label'
  confidence: high
  contrast_with: store/mydrhank-com/captures/2026-06-03/tiles/pdp-compounded-semaglutide/tile-02-y02440.png
- id: iconography_04
  family: iconography_illustration
  polarity: poor
  page_or_region: 'PDP — ''3 simple steps'' uses photos in place of icons'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/pdp-compounded-semaglutide/tile-03-y03660.png
  claim: 'The PDP ''3 simple steps'' section substitutes small stock photos (phone, doctor, package) for any iconography — a pattern-library default that sidesteps the icon problem rather than solving it; no bespoke icon or illustration appears anywhere on the site.'
  visible_tells:
  - 'Three small cropped photographs serve as the only graphic element per step'
  - 'No line-art, custom icons, or illustration present in the section'
  confidence: high
- id: iconography_05
  family: iconography_illustration
  polarity: poor
  page_or_region: 'Homepage hero — process-step icon row below CTA'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/homepage/tile-00-y00000.png
  claim: 'The four tiny icons in the trust row beneath the hero CTA are barely distinguishable at rendering size and show no shared stroke weight or bounding grid — they read as placeholder glyphs rather than a considered icon set.'
  visible_tells:
  - 'Four small icons sit in a horizontal row below the CTA, indistinct from each other at tile resolution'
  - 'No visible consistency in stroke weight or icon size across the set'
  confidence: medium
- id: iconography_06
  family: iconography_illustration
  polarity: poor
  page_or_region: 'Footer — single third-party certification badge'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/category-longevity/tile-01-y00669.png
  claim: 'The footer''s only graphic element is a third-party certification shield badge above the logotype — no brand icon, illustration, or decorative divider, indicating zero invested graphic identity in the footer.'
  visible_tells:
  - 'A certification shield badge is the sole graphic above the white MyDrHank logotype'
  - 'No brand icons, illustrated dividers, or decorative elements anywhere in the footer band'
  confidence: high
```

## Provenance

Tiles read: homepage (8) + category-weight-loss (4) + category-longevity (2) + pdp-compounded-semaglutide (5) + pdp-nad-injection (5) from `captures/2026-06-03/tiles/` — all 24 active, no exclusions. **Tier-B re-render used for all five pages**: the cached Firecrawl payloads carried a site-wide "We use cookies" consent overlay stamped over high-value regions (hero, product grids, PDP calculator/FAQ); `scripts/shoot.py` drove system Chrome, dismissed the banner via its "Accept all" click, settled motion, and re-tiled — so every cited tile is a clean browser re-render (`qa_status: recapture-used`). Mined blind + judged per [`/visual-evidence`](../../skills/visual-evidence/SKILL.md): four family miners saw only the tiles (no dossier, no web); the judge consolidated 38 raw cards to 31 accepted, merging duplicate tells (notably the four PDP-chart cards into one component card, plus the recycled-stock and footer-badge pairs) with no factual rejections. Every `poor` structural card was spot-checked against its native tile — all are genuine (clipboard-among-photos grid, uneven product-render baselines, disclaimer mass), none capture artifacts. Snapshot caveat: tiles reflect the live site re-rendered 2026-06-16; the cached source capture is 2026-06-03. The site changes.
