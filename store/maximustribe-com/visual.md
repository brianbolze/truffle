---
schema_version: "1.0"
domain: maximustribe.com
captured_at: 2026-06-15
source_capture: 2026-05-31
qa_status: clean
---

## Visual & brand impression

Premium and disciplined wherever Maximus owns the surface. A two-pole palette — saturated royal blue against deep navy — holds site-wide [color_03] across custom-lit product renders [color_02][iconography_01] and a recurring periwinkle gradient hero [color_01]. Type is confident and multi-tiered, with an italic-serif accent recurring as a brand device across heroes [typography_02][typography_04], and a real component system repeats cleanly across product grids, accordions, and data tables [layout_02][layout_03][layout_07]. Finish slips on sourced inputs — advisory headshots and customer-testimonial stills read assembled, not art-directed [color_06][color_07] — and the weight-loss page goes off-template: a looser hero [layout_11], an off-system black 'stat shock' band [color_08], icon-absent ingredient cards [iconography_06]. Generic +/- toggles and stock medical glyphs are the weakest layer [iconography_07][iconography_04].

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: "Homepage hero"
  tile_path: store/maximustribe-com/captures/2026-05-31/tiles/homepage/tile-00-y00000.png
  claim: "The hero pairs an oversized serif wordmark with a single subordinate sans subtitle and small nav labels, a clear multi-step size hierarchy."
  visible_tells:
  - "\"Maximum wei|\" renders as a large serif at roughly 3-4x the subtitle size"
  - "Subtitle \"The leading edge of personal performance medicine...\" sits at body scale, clearly subordinate"
  - "Nav items are the smallest legible layer, set apart from the heading block"
  confidence: high
- id: typography_02
  family: typography_hierarchy
  polarity: strong
  page_or_region: "Testosterone hero / homepage testosterone section — italic serif accent"
  tile_path: store/maximustribe-com/captures/2026-05-31/tiles/homepage/tile-01-y01220.png
  claim: "An italic serif accent set mid-phrase inside the upright serif display heading creates an emphasis tier without adding a size level — a recurring brand device across heroes."
  visible_tells:
  - "\"Next-generation\" and \"optimization.\" are upright serif; \"testosterone\" is italic, visually distinct"
  - "Body copy beneath is smaller and lighter, a clear second tier"
  - "Same italic-accent pattern recurs on the testosterone hero (\"Raise your game.\") and weight-loss banner (\"Lose weight.\")"
  confidence: high
  contrast_with: store/maximustribe-com/captures/2026-05-31/tiles/homepage/tile-00-y00000.png
- id: typography_03
  family: typography_hierarchy
  polarity: strong
  page_or_region: "Homepage — doctor credentialing section"
  tile_path: store/maximustribe-com/captures/2026-05-31/tiles/homepage/tile-05-y06100.png
  claim: "A four-level hierarchy reads cleanly in one viewport: institution logos, centered serif display heading, sans body paragraph, and caption-scale doctor name/title."
  visible_tells:
  - "\"Designed by leading doctors and professors\" is a large centered serif heading"
  - "Body paragraph below is noticeably smaller normal-weight sans"
  - "Doctor names (\"Dr. Cameron Sepah, CEO\") and multi-line titles under each portrait are caption-scale — a distinct fourth tier"
  confidence: high
- id: typography_04
  family: typography_hierarchy
  polarity: strong
  page_or_region: "Testosterone page — product cards"
  tile_path: store/maximustribe-com/captures/2026-05-31/tiles/testosterone/tile-01-y01220.png
  claim: "Product cards sustain a five-level type stack — caps pill-labels, serif product name, bold \"Best for:\" lead-in, regular bullet body, and large bold price — each level visually distinct."
  visible_tells:
  - "Pill tags (\"PATENTED FORMULATION\", \"FERTILITY-FRIENDLY\") are all-caps small text, the top label tier"
  - "Product name (\"Enclomiphene + Testosterone Cream\") is the larger serif heading"
  - "\"Best for:\" is bold inline within body-size text; bullets are regular weight"
  - "Price \"$189.99\" is large bold, typographically distinct from prose"
  confidence: high
- id: typography_05
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "Weight loss page — ingredient feature cards"
  tile_path: store/maximustribe-com/captures/2026-05-31/tiles/weight_loss/tile-02-y02440.png
  claim: "The 'Clinically studied ingredients' cards lean almost entirely on size for hierarchy — the small-caps category label and the oversized 'GLP-1' heading are the same black sans weight and hue, so the two tiers read as one block on a quick scan."
  visible_tells:
  - "'BODY WEIGHT SUPPORT (SEMAGLUTIDE)' caps label and the giant 'GLP-1' heading are both black sans on a light-grey card, with no weight or hue contrast"
  - "The body paragraph below is the only clearly differentiated tier; the label-to-heading distinction relies on size alone"
  confidence: medium
  contrast_with: store/maximustribe-com/captures/2026-05-31/tiles/testosterone/tile-01-y01220.png
- id: typography_06
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "Growth hormone peptides page — hero eyebrow label"
  tile_path: store/maximustribe-com/captures/2026-05-31/tiles/growth_hormone_peptides/tile-00-y00000.png
  claim: "The GHP hero adds a small-caps eyebrow tier (\"GROWTH HORMONE PEPTIDES\") above the display heading that the testosterone and homepage heroes omit, a mild cross-page inconsistency in the hero hierarchy model."
  visible_tells:
  - "\"GROWTH HORMONE PEPTIDES\" sits as a small all-caps eyebrow above the heading — absent on the testosterone hero (\"Raise your testosterone.\") and homepage hero"
  - "The rest of the stack (display heading -> italic serif accent -> body -> CTA) follows the site template"
  confidence: medium
  contrast_with: store/maximustribe-com/captures/2026-05-31/tiles/testosterone/tile-00-y00000.png
- id: typography_07
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "Labs page — biomarker list rows"
  tile_path: store/maximustribe-com/captures/2026-05-31/tiles/labs/tile-04-y04880.png
  claim: "In the biomarker list the serif category headings are clearly larger than rows, but the supporting sub-copy under each heading sits close in size to the row labels, flattening the lower tiers in a data-dense context."
  visible_tells:
  - "Serif category headings (\"Heavy Metals\", \"Hormone Health\", \"Immune Health\") are distinctly larger than the sans biomarker rows"
  - "The descriptive sub-copy beneath each heading is nearly the same size and weight as the biomarker row labels (\"% Free PSA\", \"Cortisol\"), compressing that lower hierarchy"
  confidence: medium
  contrast_with: store/maximustribe-com/captures/2026-05-31/tiles/homepage/tile-05-y06100.png
- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: "Homepage hero — image cards + category strip"
  tile_path: store/maximustribe-com/captures/2026-05-31/tiles/homepage/tile-00-y00000.png
  claim: "The hero stacks a two-card editorial image row over a horizontal category strip of identical thumbnail-plus-label pills, evenly gutter-separated under a clean nav bar — disciplined grid and a reusable component."
  visible_tells:
  - "Two image cards (\"Boost testosterone\", \"Lose weight\") with matching radius and even gutter fill the hero"
  - "Five identically-sized category pills below with uniform thumbnail height and label alignment; NEW badges placed identically top-left"
  - "Nav items evenly spaced at one baseline, \"Get Started\" CTA right-aligned with no crowding"
  confidence: high
- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: "Testosterone page — product card grid (2-col and 3-col)"
  tile_path: store/maximustribe-com/captures/2026-05-31/tiles/testosterone/tile-01-y01220.png
  claim: "Product cards repeat a tight component — image zone, pill row, title, 'Best for' line, bullets, inline upsell, price, dual-button CTA — aligned consistently across a 2-column grid, then re-flowed into an equal-width 3-column TRT row with the same internal structure, confirming a real component system."
  visible_tells:
  - "Pill tags and dual-button (filled + ghost) rows sit at identical vertical positions across both cards in the 2-col grid"
  - "The 3-col TRT row (Injectable / Cream / Injectable+hCG) keeps the same image-pill-headline-bullet-price-button structure with visually equal gutters"
  confidence: high
  contrast_with: store/maximustribe-com/captures/2026-05-31/tiles/testosterone/tile-03-y03660.png
- id: layout_03
  family: layout_composition_components
  polarity: strong
  page_or_region: "Homepage — FAQ accordion"
  tile_path: store/maximustribe-com/captures/2026-05-31/tiles/homepage/tile-06-y07320.png
  claim: "The FAQ is a clean full-width single-column accordion with hairline dividers and a right-aligned circular +/- toggle on every row at a consistent x-position."
  visible_tells:
  - "Even hairline dividers between every item, consistent row spacing"
  - "Circle-minus (open) / circle-plus (closed) toggles right-aligned at the same x on every row"
  - "Two-level type: larger question labels over clearly smaller answer body under \"What is Maximus?\""
  confidence: high
- id: layout_04
  family: layout_composition_components
  polarity: strong
  page_or_region: "Homepage — bottom two-panel CTA"
  tile_path: store/maximustribe-com/captures/2026-05-31/tiles/homepage/tile-07-y08315.png
  claim: "The paired CTA panels (Discord join + Testosterone 101 lead capture) fill the viewport as a 50/50 split on a shared light-blue background with mirrored headings and CTAs at matching vertical positions."
  visible_tells:
  - "Both panels share one light-blue swatch with a vertical midpoint divider"
  - "Serif headings (\"Join the Maximus Discord.\" / \"All your testosterone questions answered.\") sit at the same height; blue CTA button and email field mirror across the split"
  confidence: high
- id: layout_05
  family: layout_composition_components
  polarity: strong
  page_or_region: "Footer — all pages"
  tile_path: store/maximustribe-com/captures/2026-05-31/tiles/homepage/tile-07-y08315.png
  claim: "The footer is a disciplined multi-column link grid with spaced-caps category headers, even line-height, and a bottom strip separating social icons (left) from trust badges (right)."
  visible_tells:
  - "Evenly-spaced footer columns (TESTOSTERONE / WEIGHT LOSS / MORE TREATMENTS / RESOURCES / COMPANY) with no ragged left edges"
  - "Social icons left, Inc. 5000 + LegitScript trust badges right in the same bottom strip"
  confidence: high
- id: layout_06
  family: layout_composition_components
  polarity: strong
  page_or_region: "Labs page — biomarker master-detail listing"
  tile_path: store/maximustribe-com/captures/2026-05-31/tiles/labs/tile-05-y06100.png
  claim: "The biomarker listing holds a two-column master-detail layout — fixed-left category heading+description, fixed-right expandable row list — sustained across many categories with no drift in column widths or gutter."
  visible_tells:
  - "Category heading column stays left-aligned at the same x across Heavy Metals, Hormone Health, Immune Health, etc."
  - "Biomarker rows always begin at the same left edge in the right column, each with consistent OPTIMAL/MAXIMAL/ADD-ON pills and a + toggle"
  confidence: high
- id: layout_07
  family: layout_composition_components
  polarity: strong
  page_or_region: "Growth hormone peptides page — comparison table"
  tile_path: store/maximustribe-com/captures/2026-05-31/tiles/growth_hormone_peptides/tile-04-y04880.png
  claim: "The 3-column comparison table (Ser-morelin / Tesa-morelin / Synthetic HGH) is cleanly structured — light header row, alternating row fills, consistent cell padding, bold row-label column — well-executed data presentation in a rounded card."
  visible_tells:
  - "Alternating light/white row shading maintained across all 7 data rows"
  - "Bold row labels (GH Source, Release Pattern, Feedback Loops...) consistently left-aligned in column 1; three value columns evenly partitioned"
  confidence: high
- id: layout_08
  family: layout_composition_components
  polarity: mixed
  page_or_region: "Homepage — three-card info row (formats / make optimal / why boost)"
  tile_path: store/maximustribe-com/captures/2026-05-31/tiles/homepage/tile-02-y02440.png
  claim: "The three nominally equal-width info cards carry very uneven content density — the center card holds a tall bar chart while the flankers hold only text/pill lists — leaving the row visually unbalanced."
  visible_tells:
  - "Middle card filled with a tall blue bar-chart graphic; left card shows a small product cluster + pills, right card shows only a stacked option list"
  - "Equal card frames but uneven content weight leaves the row lopsided toward the center"
  confidence: medium
- id: layout_09
  family: layout_composition_components
  polarity: mixed
  page_or_region: "Weight loss page — product listing vs. testosterone grid"
  tile_path: store/maximustribe-com/captures/2026-05-31/tiles/weight_loss/tile-01-y01220.png
  claim: "Weight-loss product cards (Tirzepatide, Semaglutide) break the established component pattern: they are single-column stacked with a left text-intro / right card split and black CTAs, rather than the testosterone page's side-by-side two-up grid with navy CTAs."
  visible_tells:
  - "Cards stack one per viewport width with an explanatory text column to their left, not a 2-up grid"
  - "CTA buttons are black (\"Start Treatment\") with a green SAVE pill, unlike the navy \"Start assessment\" buttons on the testosterone cards"
  confidence: medium
  contrast_with: store/maximustribe-com/captures/2026-05-31/tiles/testosterone/tile-01-y01220.png
- id: layout_10
  family: layout_composition_components
  polarity: mixed
  page_or_region: "Labs page — 'How it works' four-step strip"
  tile_path: store/maximustribe-com/captures/2026-05-31/tiles/labs/tile-07-y08540.png
  claim: "The four-step 'How it works' strip runs steps 1-3 with consistent thumbnail+label treatment, but the fourth step ('Get your...') is cropped at the right edge of the viewport with no wrap or scroll affordance."
  visible_tells:
  - "Step 4 label/content cut at the right tile edge; steps 1-3 (Choose your panel / Schedule your test / Complete your draw) share identical photo-plus-caption treatment"
  - "No horizontal scroll indicator visible"
  confidence: medium
- id: layout_11
  family: layout_composition_components
  polarity: mixed
  page_or_region: "Weight loss page — hero composition"
  tile_path: store/maximustribe-com/captures/2026-05-31/tiles/weight_loss/tile-00-y00000.png
  claim: "The weight-loss hero is a competent 50/50 split — vertically-centered copy left, full-height photo right — but looser and off-template: a narrow copy column with wide empty margins, and it drops the brand's signature serif/italic display device for a plain sans headline."
  visible_tells:
  - "Headline 'GLP-1 weight loss treatments, backed by science.' plus subtitle and one CTA occupy a narrow left strip with notable empty space above and below"
  - "Plain sans headline with no serif or italic accent, unlike the testosterone hero's serif/italic 'Raise your testosterone.' treatment"
  - "Right half is a full-bleed floor-workout photo running edge to edge"
  confidence: medium
  contrast_with: store/maximustribe-com/captures/2026-05-31/tiles/testosterone/tile-00-y00000.png
- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: "Hero background gradient across pages"
  tile_path: store/maximustribe-com/captures/2026-05-31/tiles/testosterone/tile-00-y00000.png
  claim: "A periwinkle-to-warm gradient hero surface recurs across pages as a signature brand backdrop rather than a generic fill."
  visible_tells:
  - "Testosterone hero: blue-to-warm gradient behind the male athlete"
  - "Homepage testosterone section repeats the same gradient behind the male portrait"
  - "GHP hero repeats the identical gradient behind the couple"
  confidence: high
  contrast_with: store/maximustribe-com/captures/2026-05-31/tiles/weight_loss/tile-00-y00000.png
- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: "Product packaging color across categories"
  tile_path: store/maximustribe-com/captures/2026-05-31/tiles/testosterone/tile-01-y01220.png
  claim: "A single saturated royal blue is applied uniformly to all product packaging across every treatment category, giving the physical product a cohesive owned identity."
  visible_tells:
  - "Testosterone Cream, Enclomiphene, Oral Testosterone jars are all the same deep royal blue"
  - "Weight-loss vials carry the same blue cap; GHP vial shows a matching blue label; At-Home Test box repeats the blue"
  confidence: high
  contrast_with: store/maximustribe-com/captures/2026-05-31/tiles/growth_hormone_peptides/tile-01-y01220.png
- id: color_03
  family: color_brand_imagery
  polarity: strong
  page_or_region: "Navy footer + blue CTA accent — palette control"
  tile_path: store/maximustribe-com/captures/2026-05-31/tiles/homepage/tile-07-y08315.png
  claim: "The palette holds a controlled two-pole system — saturated blue accent and deep navy anchor — with the navy footer keeping the white MAXIMUS wordmark legible and no competing hues introduced."
  visible_tells:
  - "Deep navy footer background behind the full-width nav and wordmark; white text/CTAs hold contrast with no new colors"
  - "Interactive accent (Get Started pill, Join the conversation button, blue tag chips) stays one saturated blue site-wide"
  confidence: high
  contrast_with: store/maximustribe-com/captures/2026-05-31/tiles/homepage/tile-00-y00000.png
- id: color_04
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "Weight Loss hero — photographic temperature shift"
  tile_path: store/maximustribe-com/captures/2026-05-31/tiles/weight_loss/tile-00-y00000.png
  claim: "The weight-loss hero drops the cool brand gradient for a white split layout with a warm, documentary-style workout photo, a noticeable temperature break from the cool-blue testosterone and GHP heroes."
  visible_tells:
  - "Left panel is plain white with a sans headline; right is a warmly lit indoor floor-workout scene with warm wood tones"
  - "No gradient surface — the warm grade contrasts sharply with the cool heroes elsewhere"
  confidence: high
  contrast_with: store/maximustribe-com/captures/2026-05-31/tiles/testosterone/tile-00-y00000.png
- id: color_05
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "Growth hormone peptides — composited illustration vs. photography"
  tile_path: store/maximustribe-com/captures/2026-05-31/tiles/growth_hormone_peptides/tile-03-y03660.png
  claim: "The 'How it works' strip mixes straight photography with digitally-composited biology graphics (glowing peptide/pituitary overlays) that don't match the naturalistic photographic language."
  visible_tells:
  - "Step 2 'Pituitary activation' and step 3 'GH -> IGF-1' show rendered orange/blue glow composites over portraits and tissue"
  - "They sit beside a straight injection-site photo (step 1) and an outdoor running shot (step 4)"
  confidence: high
- id: color_06
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "Homepage — doctor advisory headshots"
  tile_path: store/maximustribe-com/captures/2026-05-31/tiles/homepage/tile-05-y06100.png
  claim: "The five advisory-team portraits are shot inconsistently — background tint, framing, and lighting vary across the row, revealing assembled rather than art-directed imagery."
  visible_tells:
  - "Dr. Sepah on a neutral/white background, close crop; Dr. Hellstrom on a different background tint with a more formal pose"
  - "Shoulder-to-head ratios and crops differ noticeably across the five portraits in one row"
  confidence: high
- id: color_07
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "Testosterone page — testimonial video stills"
  tile_path: store/maximustribe-com/captures/2026-05-31/tiles/testosterone/tile-05-y06100.png
  claim: "The four customer video-testimonial stills show inconsistent backgrounds and color grades with burned-in caption bars — clearly user-generated/casually filmed, not brand-produced."
  visible_tells:
  - "Joey on a light grey background; Sammy in a darker outdoor setting; Daniel in a patterned shirt under different ambient light"
  - "Blue burned-in caption chips (\"AND SINCE\", \"I FEEL\", \"THERE\", \"IT HAS\") sit over four different shooting environments in one row"
  confidence: high
- id: color_08
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "Weight loss page — black 'stat shock' / weight-loss-calculator band"
  tile_path: store/maximustribe-com/captures/2026-05-31/tiles/weight_loss/tile-03-y03660.png
  claim: "A full-width black 'stat shock' band — a 74%-of-adults statistic beside a dark weight-loss calculator — interrupts the site's blue/navy-and-white system with an off-palette register and an abrupt, transition-less edge."
  visible_tells:
  - "Full-bleed black section: white headline 'Nearly 74% of adults in the U.S. are overweight or obese' left, a dark calculator card ('270' current weight / '45' projected loss) right"
  - "No blue accent anywhere in the band; it sits directly between a light section above and a white 'Optimize your long-term health' section below with no transitional element"
  confidence: high
  contrast_with: store/maximustribe-com/captures/2026-05-31/tiles/homepage/tile-07-y08315.png
- id: iconography_01
  family: iconography_illustration
  polarity: strong
  page_or_region: "Testosterone — product renders (jars and vials)"
  tile_path: store/maximustribe-com/captures/2026-05-31/tiles/testosterone/tile-01-y01220.png
  claim: "Product renders are custom-lit studio objects on a clean neutral ground with consistent shadows, styled pill/cream scatter, and a coherent jar-to-vial render system across sections — clearly invested, not stock pharma imagery."
  visible_tells:
  - "Royal-blue jar renders (Testosterone Cream, Enclomiphene, Oral Testosterone) shot at a matched 3/4 angle with rim lighting, ground shadow, and identical white pill scatter"
  - "TRT section shifts to frosted glass vials with bright blue caps and the same specular lighting and prop styling across the row"
  confidence: high
  contrast_with: store/maximustribe-com/captures/2026-05-31/tiles/testosterone/tile-03-y03660.png
- id: iconography_02
  family: iconography_illustration
  polarity: strong
  page_or_region: "Labs — Maximus Score dashboard mockup"
  tile_path: store/maximustribe-com/captures/2026-05-31/tiles/labs/tile-00-y00000.png
  claim: "The Maximus Score dashboard UI in the hero is a polished, designed product artifact — scored dial, color-coded biomarker rows, named values — not a placeholder screenshot."
  visible_tells:
  - "Circular score widget showing '89' with a status label and a small trend line"
  - "Stacked biomarker rows (Testosterone 142, Vitamin D 4.4, Magnesium 84) with color-coded indicator bars in a compact card"
  confidence: high
  contrast_with: store/maximustribe-com/captures/2026-05-31/tiles/labs/tile-02-y02440.png
- id: iconography_03
  family: iconography_illustration
  polarity: strong
  page_or_region: "Homepage — '3.1x Free Testosterone' bar chart"
  tile_path: store/maximustribe-com/captures/2026-05-31/tiles/homepage/tile-02-y02440.png
  claim: "The '3.1x Free Testosterone' data viz is a restrained, purpose-built bar chart with branded fill and a before/after pair — readable rather than generic charting-library output."
  visible_tells:
  - "Two bars labeled '382' (dark navy baseline) and '1180' (brand-blue outcome) with an up-arrow '3.1x' callout"
  - "No gridlines, axes, or chart junk — stripped to the essential comparison"
  confidence: high
- id: iconography_04
  family: iconography_illustration
  polarity: mixed
  page_or_region: "Labs — biomarker category filter tabs"
  tile_path: store/maximustribe-com/captures/2026-05-31/tiles/labs/tile-02-y02440.png
  claim: "The biomarker-category tabs carry small inline glyphs (droplet, DNA helix, heart, shield, etc.) that are recognizable but read as a generic medical icon library rather than a bespoke system."
  visible_tells:
  - "Droplet (Blood Health), double-helix (Genetics), heart (Heart Health), shield, and other common medical glyphs in the tab row"
  - "Stroke weight and style look inconsistent across the set at this scale"
  confidence: medium
- id: iconography_05
  family: iconography_illustration
  polarity: mixed
  page_or_region: "Labs — 'Before you start' utility illustrations"
  tile_path: store/maximustribe-com/captures/2026-05-31/tiles/labs/tile-10-y12200.png
  claim: "The 'Check availability' US-map silhouette and the 'Blood draw prep' fasting ring are functional utility illustrations but neither rises above generic craft."
  visible_tells:
  - "Flat dark-navy US map with state outlines and no detail beyond borders"
  - "Simple donut/progress-ring graphic with '10-12hr of fasting' text centered — basic, not bespoke"
  confidence: medium
- id: iconography_06
  family: iconography_illustration
  polarity: poor
  page_or_region: "Weight loss — ingredient cards (icon absence)"
  tile_path: store/maximustribe-com/captures/2026-05-31/tiles/weight_loss/tile-02-y02440.png
  claim: "The three GLP-1 ingredient cards are pure text blocks with no icon, diagram, or visual differentiator — the iconographic surface is absent at a decision point where a symbol would reduce cognitive load."
  visible_tells:
  - "Three bordered cards with oversized 'GLP-1' / 'GLP-1 + GIP' / 'GLP-1' headlines and body text only — no symbol or graphic"
  - "All three are structurally identical; differentiation is carried entirely by the abbreviation text"
  confidence: high
- id: iconography_07
  family: iconography_illustration
  polarity: poor
  page_or_region: "Homepage — FAQ accordion toggle icons"
  tile_path: store/maximustribe-com/captures/2026-05-31/tiles/homepage/tile-06-y07320.png
  claim: "The FAQ toggles are bare thin-stroke minus/plus circle glyphs identical to a default utility pattern — no brand-distinct iconographic treatment."
  visible_tells:
  - "Thin circle-minus (open) and circle-plus (closed) glyphs on the right edge of each row"
  - "Generic affordance icons with no styling that ties them to the brand"
  confidence: high
  contrast_with: store/maximustribe-com/captures/2026-05-31/tiles/labs/tile-11-y13420.png
```

## Provenance

- **Tiles read:** native-resolution tiles from `captures/2026-05-31/tiles/` for five pages that carry the visual system — homepage (8), testosterone (9), weight_loss (7), labs (13), growth_hormone_peptides (9), 46 tiles total. Blind fan-out: four family miners (Sonnet) over the tiles only, then an Opus judge prunes/merges to 33 cards.
- **QA:** `clean` — all five pages rendered fully from the cached Firecrawl full-page screenshots (no modals, cookie banners, grey/WebGL heroes, or broken media); no tiles excluded and no Tier-B browser re-render needed. The page's intentional dark sections (the Discord band, the weight-loss BMI band, the labs 'Maximus Difference' section) are brand design, not capture defects.
- **Post-mine spot-check (not blind):** three cards were corrected where a native tile contradicted the blind read. `color_08` and `typography_05` described the 'Clinically studied ingredients' GLP-1 cards as black-background / white-text — the cards are actually light-grey with black text; the black register is the *adjacent* weight-loss-calculator band, so `color_08` was re-anchored to `weight_loss/tile-03` and re-scoped to that band (poor→mixed). `layout_11`'s weight-loss hero is a competent split, so its 'poor' was recalibrated to 'mixed' (looser/off-template, not broken).
- **Snapshot caveat:** a point-in-time read of the 2026-05-31 captured tiles; the live site changes.
