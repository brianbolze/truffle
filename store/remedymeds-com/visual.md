---
schema_version: "1.0"
domain: remedymeds.com
captured_at: 2026-06-15
source_capture: 2026-06-01
qa_status: exclusions-noted
---

## Visual & brand impression

Remedy reads as a confident, editorial DTC brand built on one distinctive move — a two-voice headline system pairing a roman-sans declaration with an italic blue-serif kicker, carried from hero through section heads [typography_01][color_07]. The marketing pages are disciplined: an asymmetric hero over a uniform image mosaic [layout_01], staggered process cards sharing one component structure [layout_03], navy and green doing the persuasive work in the comparison [color_02], art-directed peach-field product renders [iconography_03], a coherent monoline icon set [iconography_01]. Finish is the weak spot — stock-feeling, tonally mismatched testimonial photos [color_04], per-SKU backgrounds drifting from the brand color [color_03], badges outside the icon language [iconography_07], flat secondary hierarchy [typography_05]. The system then collapses on utility pages: a lopsided quiz [layout_10] and a bare, template-grade safety page [color_06].

## Evidence cards

```yaml
- id: typography_01
  family: 'typography_hierarchy'
  polarity: 'strong'
  page_or_region: 'homepage hero — headline treatment'
  tile_path: 'store/remedymeds-com/captures/2026-06-01/tiles/homepage/tile-00-y00000.png'
  claim: 'The hero uses a deliberate two-voice headline system — roman sans for the declarative line, italic blue serif for the emotional kicker — creating a clear typographic identity with strong size contrast against nav and body.'
  visible_tells:
  - '''Your weight isn''t a willpower problem.'' in large black sans-serif'
  - '''It''s a medical one.'' in italicized blue serif directly below'
  - 'noticeable size gap between headline and sub-copy'
  confidence: 'high'
- id: typography_02
  family: 'typography_hierarchy'
  polarity: 'strong'
  page_or_region: 'homepage — repeated section headline pattern'
  tile_path: 'store/remedymeds-com/captures/2026-06-01/tiles/homepage/tile-03-y03660.png'
  claim: 'The roman-plus-italic-serif couplet recurs across sections (''What''s in the vial matters. / So does where it comes from.''), confirming an intentional two-voice scale rather than a one-off hero choice.'
  visible_tells:
  - 'Black sans-serif first line, blue italic serif second line'
  - 'Matching weight and size cadence to the hero'
  - 'Centered alignment preserved across instances'
  confidence: 'high'
  contrast_with: 'store/remedymeds-com/captures/2026-06-01/tiles/safety/tile-00-y00000.png'
- id: typography_03
  family: 'typography_hierarchy'
  polarity: 'strong'
  page_or_region: 'homepage — stats section'
  tile_path: 'store/remedymeds-com/captures/2026-06-01/tiles/homepage/tile-06-y07320.png'
  claim: 'The stat cards establish a clear three-level hierarchy — small all-caps label, oversized numeral, small supporting sentence — giving each metric instant scannability without size collisions.'
  visible_tells:
  - '''FASTER RESULTS'' in small caps above oversized ''2x'' numeral'
  - '''AVG. WEIGHT LOSS'' above ''-14lbs'' in display size'
  - 'Supporting sentence at much smaller weight below each figure'
  confidence: 'high'
- id: typography_04
  family: 'typography_hierarchy'
  polarity: 'strong'
  page_or_region: 'homepage — editorial body copy cards'
  tile_path: 'store/remedymeds-com/captures/2026-06-01/tiles/homepage/tile-01-y01220.png'
  claim: 'Card sub-headings (''The hunger that never shuts off.'', ''Your metabolism turned on you.'') sit at a clearly heavier weight than the body copy below, with adequate leading so neither level bleeds into the other.'
  visible_tells:
  - 'Bold card titles vs. lighter body paragraph beneath each'
  - 'Consistent inter-card whitespace separating each block'
  - 'Body text visibly smaller and lighter than the card title'
  confidence: 'high'
- id: typography_05
  family: 'typography_hierarchy'
  polarity: 'mixed'
  page_or_region: 'homepage — guarantee section'
  tile_path: 'store/remedymeds-com/captures/2026-06-01/tiles/homepage/tile-07-y08540.png'
  claim: 'The ''Lose weight or / Get refunded'' headline applies the two-voice system correctly, but the benefit bullets below run at one uniform small weight, and the caveat line (''*Terms apply…'') nearly vanishes — secondary content has no internal hierarchy.'
  visible_tells:
  - 'Headline: correct roman + italic-serif split'
  - 'Bullet items at identical size and weight regardless of importance'
  - 'Tiny ''*Terms apply on Weight Loss Warranty'' line at near-minimum size below the bullets'
  confidence: 'medium'
- id: typography_06
  family: 'typography_hierarchy'
  polarity: 'poor'
  page_or_region: 'quiz landing page'
  tile_path: 'store/remedymeds-com/captures/2026-06-01/tiles/quiz/tile-00-y00000.png'
  claim: 'The quiz page collapses the headline system to a single small-format headline over the navy panel, with four answer-option rows all in identical body weight — there is no typographic tier above the option labels to anchor the page.'
  visible_tells:
  - '''Lose weight without thinking about it.'' headline much smaller than equivalent homepage section heads'
  - 'Four answer-option rows in identical weight and size with no visual leader'
  - 'Sub-copy under the option labels sits at near-identical size to the option titles'
  confidence: 'medium'
- id: typography_07
  family: 'typography_hierarchy'
  polarity: 'strong'
  page_or_region: 'homepage — scrolling trust ticker'
  tile_path: 'store/remedymeds-com/captures/2026-06-01/tiles/homepage/tile-04-y04880.png'
  claim: 'The continuous trust bar subordinates its copy — small uniform label + icon on a yellow band — so it reads as ambient infrastructure and does not compete with surrounding section headings.'
  visible_tells:
  - 'All ticker items (''250,000+ members'', ''FSA & HSA eligible'', etc.) in small uniform weight on a yellow band'
  - 'No size escalation within the ticker items'
  - 'Clear vertical gap separates the ticker from headlines above and below'
  confidence: 'high'
- id: layout_01
  family: 'layout_composition_components'
  polarity: 'strong'
  page_or_region: 'homepage hero — split layout with mosaic image grid'
  tile_path: 'store/remedymeds-com/captures/2026-06-01/tiles/homepage/tile-00-y00000.png'
  claim: 'The hero uses a deliberate asymmetric split — narrow left text column with headline, CTA, and social proof against a right-side mosaic of uniform image cards — and the two halves hold a clean vertical axis without crowding.'
  visible_tells:
  - 'Left text block and CTA button sit flush to a consistent left margin'
  - 'Right mosaic cards are uniform-width and stack with equal gutters'
  - 'Breathing room between the headline block and the pane edge — no content collision'
  confidence: 'high'
- id: layout_02
  family: 'layout_composition_components'
  polarity: 'strong'
  page_or_region: 'homepage — 4-up editorial card grid'
  tile_path: 'store/remedymeds-com/captures/2026-06-01/tiles/homepage/tile-01-y01220.png'
  claim: 'The four editorial cards sit on a uniform grid with matching column widths, consistent image-to-copy proportions, and identical internal padding — the system looks engineered, not assembled ad hoc.'
  visible_tells:
  - 'All four card images share the same aspect ratio and a common top edge'
  - 'Headline, body, and check-list rows track the same left margin inside each card'
  - 'Gutter widths between cards appear equal across all three breaks'
  confidence: 'high'
- id: layout_03
  family: 'layout_composition_components'
  polarity: 'strong'
  page_or_region: 'homepage — 4-step staggered process cards'
  tile_path: 'store/remedymeds-com/captures/2026-06-01/tiles/med_semaglutide/tile-01-y01220.png'
  claim: 'The four-step flow uses offset card placement (left/right alternating columns) that creates vertical rhythm without losing grid discipline — each card shares the same internal structure: step pill + timing tag, title, bullet list, CTA button, supporting micro-mockup.'
  visible_tells:
  - 'Step 1 occupies the left column; Step 2 is offset to the right at a lower y-position — a deliberate zigzag continuing through Steps 3 and 4'
  - 'Step badge pill (''Step 1'' / ''Today'') styling is identical across all four cards'
  - 'Internal CTA buttons are consistent full-width within each card column'
  confidence: 'high'
- id: layout_04
  family: 'layout_composition_components'
  polarity: 'strong'
  page_or_region: 'homepage — comparison table (Remedy vs Others)'
  tile_path: 'store/remedymeds-com/captures/2026-06-01/tiles/homepage/tile-05-y06100.png'
  claim: 'The two-column comparison uses a dark filled card for Remedy against a bare white card for Others, with each feature row aligned horizontally across both columns — no vertical drift or misaligned baselines.'
  visible_tells:
  - 'Green check rows (left) and grey minus rows (right) share the same vertical positions per feature'
  - 'Feature text wraps consistently without breaking cross-column alignment'
  - 'Both columns share identical top and bottom padding'
  confidence: 'high'
- id: layout_05
  family: 'layout_composition_components'
  polarity: 'strong'
  page_or_region: 'homepage — stats 2x2 grid'
  tile_path: 'store/remedymeds-com/captures/2026-06-01/tiles/homepage/tile-06-y07320.png'
  claim: 'The four stat cards form a tight 2x2 grid where every card shares border radius, internal padding, label-caps treatment, numeral size, and top-right icon position — a reused component, not four hand-built cells.'
  visible_tells:
  - 'Icon anchors to the top-right corner of each card at identical position'
  - 'Small-caps label tracks the same top margin across all four cards'
  - 'Card borders and corner rounding consistent across both rows'
  confidence: 'high'
- id: layout_06
  family: 'layout_composition_components'
  polarity: 'mixed'
  page_or_region: 'homepage — treatment plan carousel'
  tile_path: 'store/remedymeds-com/captures/2026-06-01/tiles/homepage/tile-02-y02440.png'
  claim: 'The product carousel cards share a common structure but the far-right ''Ozempic / Zepbound — Start name brand'' card is visibly clipped at the frame edge, and the carousel offers no clear overflow affordance to signal more cards off-screen.'
  visible_tells:
  - 'The rightmost name-brand card is cut off at the right edge of the row'
  - 'No partial-peek shadow or arrow control visible on this tile to communicate scroll/overflow'
  - 'Active vs. inactive cards differ only by header color, with uneven whitespace below the CTAs'
  confidence: 'medium'
- id: layout_07
  family: 'layout_composition_components'
  polarity: 'mixed'
  page_or_region: 'homepage — FAQ accordion section'
  tile_path: 'store/remedymeds-com/captures/2026-06-01/tiles/homepage/tile-11-y13420.png'
  claim: 'The accordion rows are structurally consistent but sit in a narrow centered column that leaves wide empty margins on both sides — the whitespace reads as uncontrolled rather than designed, and forces long questions to wrap at short line lengths.'
  visible_tells:
  - 'Accordion rows capped at roughly the center half of the viewport, with large blank grey margins on either side'
  - 'Plus affordance flush-right within each row (correct), but the two-line question wraps unnecessarily early given the available page width'
  confidence: 'medium'
  contrast_with: 'store/remedymeds-com/captures/2026-06-01/tiles/homepage/tile-06-y07320.png'
- id: layout_09
  family: 'layout_composition_components'
  polarity: 'strong'
  page_or_region: 'product page (semaglutide) — hero PDP layout'
  tile_path: 'store/remedymeds-com/captures/2026-06-01/tiles/med_semaglutide/tile-00-y00000.png'
  claim: 'The PDP hero uses a clean left-image / right-content split: the product image fills a warm peach panel that separates it from the white chrome, and the right column stacks rating, description, billing toggle, price, CTA, and trust bullets at a consistent left margin.'
  visible_tells:
  - 'Peach image panel is bounded cleanly with no bleed into the content column'
  - 'Description, Monthly/1-Month toggle, $299 price, and CTA are left-aligned at a consistent margin'
  - 'Forbes/Trustpilot laurel badges sit below the rating with appropriate vertical separation'
  confidence: 'high'
- id: layout_10
  family: 'layout_composition_components'
  polarity: 'poor'
  page_or_region: 'quiz page — split layout balance'
  tile_path: 'store/remedymeds-com/captures/2026-06-01/tiles/quiz/tile-00-y00000.png'
  claim: 'The quiz layout is lopsided: a large hand-and-vial photo dominates the right, the navy headline panel is mostly empty negative space, and the white options card floats narrow and short between them with no countervailing content mass.'
  visible_tells:
  - 'Hand-holding-vial photo occupies the full right portion of the frame and bleeds over the split'
  - 'Navy panel headline fills only the top fraction; the rest is empty navy'
  - 'White options card is narrow and ends well short of the photo''s vertical extent'
  confidence: 'medium'
- id: layout_11
  family: 'layout_composition_components'
  polarity: 'strong'
  page_or_region: 'homepage — weight-loss calculator 3-column widget'
  tile_path: 'store/remedymeds-com/captures/2026-06-01/tiles/homepage/tile-08-y09760.png'
  claim: 'The three-panel calculator (input / social-proof avatars / projected result) uses equal-width cards that hold a shared top edge and card treatment, with the result panel''s slider aligned to the same margin as the input fields.'
  visible_tells:
  - 'All three white panels share the same elevation, border radius, and top edge on the light-grey ground'
  - 'Input fields (Height/Weight) and the result-panel slider align to a consistent left margin'
  - 'Center avatar-strip panel is centered within its column without colliding with neighbors'
  confidence: 'high'
- id: layout_12
  family: 'layout_composition_components'
  polarity: 'mixed'
  page_or_region: 'safety page — accordion column vs footer width'
  tile_path: 'store/remedymeds-com/captures/2026-06-01/tiles/safety/tile-00-y00000.png'
  claim: 'The safety page''s accordion list is centered in a narrow column with large lateral margins, while the wider multi-column footer directly below spans the full width — the width mismatch makes the content area look undersized.'
  visible_tells:
  - 'Four accordion rows centered in a narrow column with broad empty margins left and right'
  - 'Footer below uses a wide four-column grid spanning the full page width'
  - 'The width step between the two is visible within the same tile'
  confidence: 'medium'
- id: color_01
  family: 'color_brand_imagery'
  polarity: 'strong'
  page_or_region: 'homepage hero — mosaic photo grid'
  tile_path: 'store/remedymeds-com/captures/2026-06-01/tiles/homepage/tile-00-y00000.png'
  claim: 'The hero mosaic holds a tight warm-neutral palette — sand/peach product grounds, soft blue-grey lifestyle cards — at a single low-saturation light value, so the grid reads as one composed unit rather than assembled stock.'
  visible_tells:
  - 'Product/vial cards sit on continuous peach-sand grounds'
  - 'Cooler blue-grey lifestyle cards create deliberate temperature contrast without breaking value'
  - 'No loud or high-saturation card disrupts the shared light register'
  confidence: 'high'
  contrast_with: 'store/remedymeds-com/captures/2026-06-01/tiles/homepage/tile-06-y07320.png'
- id: color_02
  family: 'color_brand_imagery'
  polarity: 'strong'
  page_or_region: 'homepage — comparison card (Remedy vs Others)'
  tile_path: 'store/remedymeds-com/captures/2026-06-01/tiles/homepage/tile-05-y06100.png'
  claim: 'The brand''s deep navy is used purposefully as the owned/active card fill while ''Others'' sits in unstyled white — color carries the argument, with green checks appearing only inside the Remedy column as a secondary brand signal.'
  visible_tells:
  - 'Remedy card: navy fill, white italic logo, green circle checkmarks'
  - 'Others card: no fill, grey minus icons'
  - 'Green accent confined to the Remedy column'
  confidence: 'high'
- id: color_03
  family: 'color_brand_imagery'
  polarity: 'mixed'
  page_or_region: 'product pages — per-SKU background color divergence'
  tile_path: 'store/remedymeds-com/captures/2026-06-01/tiles/med_tirzepatide/tile-00-y00000.png'
  claim: 'The tirzepatide PDP swaps to a saturated cobalt-blue studio ground against the semaglutide page''s peach — the highest-saturation background in the set, and a brighter blue than the brand navy, so it reads as a per-SKU color cue that diverges from the system token rather than extending it.'
  visible_tells:
  - 'Vial sits on a solid, fully saturated cobalt field — the most saturated background across all tiles'
  - 'That cobalt differs from the navy used in the comparison card and header'
  - 'Semaglutide PDP uses peach for the same component, confirming the per-SKU swap'
  confidence: 'high'
  contrast_with: 'store/remedymeds-com/captures/2026-06-01/tiles/med_semaglutide/tile-00-y00000.png'
- id: color_04
  family: 'color_brand_imagery'
  polarity: 'mixed'
  page_or_region: 'med_semaglutide — before/after testimonial strip'
  tile_path: 'store/remedymeds-com/captures/2026-06-01/tiles/med_semaglutide/tile-02-y02440.png'
  claim: 'The before/after testimonial cards use real-people photography that is tonally inconsistent — varied backdrops (street, gym, outdoors), mixed lighting and color balance, and inconsistent crops, unified only by the card frame and green ''Verified Remedy Members'' badge.'
  visible_tells:
  - 'Each person photographed in a different location with a different camera color balance'
  - 'Crops vary (full-body vs. waist-up) across the row'
  - 'No shared filter or background treatment unifies the set; only the green verified badge repeats'
  confidence: 'high'
  contrast_with: 'store/remedymeds-com/captures/2026-06-01/tiles/homepage/tile-00-y00000.png'
- id: color_05
  family: 'color_brand_imagery'
  polarity: 'mixed'
  page_or_region: 'homepage — contact support section'
  tile_path: 'store/remedymeds-com/captures/2026-06-01/tiles/homepage/tile-12-y14640.png'
  claim: 'The support photo (headset woman at a desk, generic office plant, polka-dot blouse, daylight-neutral balance) reads as licensed stock and sits outside the brand''s warm-peach/clinical palette, with no brand-color accent contextualizing it.'
  visible_tells:
  - 'Generic indoor-office setting with a decorative plant'
  - 'Bright daylight-neutral color temperature unrelated to the product photography palette'
  - 'No brand-color background treatment around the image'
  confidence: 'high'
  contrast_with: 'store/remedymeds-com/captures/2026-06-01/tiles/med_semaglutide/tile-00-y00000.png'
- id: color_06
  family: 'color_brand_imagery'
  polarity: 'poor'
  page_or_region: 'safety page — full page'
  tile_path: 'store/remedymeds-com/captures/2026-06-01/tiles/safety/tile-00-y00000.png'
  claim: 'The safety page is a stripped utility page — white field, blue text accordion links, dark footer — with no brand imagery or color identity in the body, indistinguishable from a generic compliance template aside from the header logo.'
  visible_tells:
  - 'Page body entirely white with no background accent, illustration, or photography'
  - 'Accordion items (Zepbound, Ozempic, Compounded-Semaglutide, Compounded-Tirzepatide) carry only link-style blue text'
  - 'Header logo is the only brand element above the footer'
  confidence: 'high'
- id: color_07
  family: 'color_brand_imagery'
  polarity: 'strong'
  page_or_region: 'homepage — italic blue serif heading system'
  tile_path: 'store/remedymeds-com/captures/2026-06-01/tiles/homepage/tile-08-y09760.png'
  claim: 'The italic-blue second-line heading is applied with one consistent hue across many sections (''And how fast.'', ''with Remedy.'', ''Life-changing results''), functioning as a repeating brand cadence rather than a decorative one-off.'
  visible_tells:
  - '''And how fast.'' italic blue serif under ''How it works.'' in near-black sans'
  - 'Same hue and construction recurs across multiple section heads in the capture'
  - 'Upright sans line always near-black; the split-color pairing is the system'
  confidence: 'high'
  contrast_with: 'store/remedymeds-com/captures/2026-06-01/tiles/safety/tile-00-y00000.png'
- id: color_08
  family: 'color_brand_imagery'
  polarity: 'strong'
  page_or_region: 'homepage footer — oversized ghosted wordmark'
  tile_path: 'store/remedymeds-com/captures/2026-06-01/tiles/homepage/tile-13-y15047.png'
  claim: 'The footer closes on a several-hundred-pixel ghosted ''Remedy'' wordmark in charcoal-on-dark-charcoal — a restrained two-value finishing move that signals brand confidence without adding color complexity.'
  visible_tells:
  - 'Wordmark spans the full footer width, reversed in a low-contrast charcoal value'
  - 'No additional color introduced in the footer beyond the two-value dark palette'
  - 'Visible but recessive enough not to compete with the functional footer links above'
  confidence: 'high'
- id: iconography_01
  family: 'iconography_illustration'
  polarity: 'strong'
  page_or_region: 'homepage — stats dashboard card icons'
  tile_path: 'store/remedymeds-com/captures/2026-06-01/tiles/homepage/tile-06-y07320.png'
  claim: 'Each stat card pairs one thin-stroke monoline icon (bar chart, downward trend, percent, person) with its numeral, and the four icons are consistent in weight, size, and stroke style and uniformly anchored top-right.'
  visible_tells:
  - 'All four icons render at the same apparent size with the same thin monoline stroke'
  - 'Icons sit flush in the top-right corner of each card at uniform alignment'
  - 'No icon deviates in style or weight from the others'
  confidence: 'high'
- id: iconography_02
  family: 'iconography_illustration'
  polarity: 'strong'
  page_or_region: 'homepage — circled-check icon across benefit lists'
  tile_path: 'store/remedymeds-com/captures/2026-06-01/tiles/homepage/tile-07-y08540.png'
  claim: 'The circled-checkmark glyph used across benefit lists is a single consistent icon — same circle diameter, stroke, and brand-blue color — deployed identically from the batch-testing list through the guarantee bullets.'
  visible_tells:
  - 'Guarantee bullets (''365-Day Money-Back Guarantee'', ''No returns required'', etc.) all use the same blue circled check'
  - 'Identical circle diameter and check stroke across every row'
  - 'Color matches the brand blue with no fill or weight variation'
  confidence: 'high'
- id: iconography_03
  family: 'iconography_illustration'
  polarity: 'strong'
  page_or_region: 'med_semaglutide — product hero render'
  tile_path: 'store/remedymeds-com/captures/2026-06-01/tiles/med_semaglutide/tile-00-y00000.png'
  claim: 'The semaglutide vial is art-directed on a clean warm-peach field with soft grounding shadow and a legible branded label — a considered product image, not a generic white-cyclorama stock shot.'
  visible_tells:
  - 'Uniform warm-peach background distinct from the site''s white/blue chrome'
  - 'Vial is the sole element, cleanly lit with a soft cast shadow'
  - 'Label text (''Semaglutide / Compounded / GLP-1'') legible on the vial'
  confidence: 'high'
  contrast_with: 'store/remedymeds-com/captures/2026-06-01/tiles/med_tirzepatide/tile-00-y00000.png'
- id: iconography_04
  family: 'iconography_illustration'
  polarity: 'mixed'
  page_or_region: 'homepage — comparison table glyphs'
  tile_path: 'store/remedymeds-com/captures/2026-06-01/tiles/homepage/tile-05-y06100.png'
  claim: 'The comparison table differentiates columns with green filled-circle checks vs. grey filled-circle minus signs — color-coded and clear, but both are plain filled circles differing only by inner glyph, with no custom iconography to reinforce the contrast.'
  visible_tells:
  - 'Green check circles (Remedy) vs grey minus circles (Others) are the only differentiator'
  - 'Minus icon is identical in form to the check except for the internal symbol'
  confidence: 'high'
- id: iconography_05
  family: 'iconography_illustration'
  polarity: 'mixed'
  page_or_region: 'homepage — marquee trust/feature strip icons'
  tile_path: 'store/remedymeds-com/captures/2026-06-01/tiles/homepage/tile-04-y04880.png'
  claim: 'The yellow feature strip uses small outline icons (badge, pill bottle, package, shield, headset) that are readable but appear to be near-stock UI glyphs, lighter and less custom than the heavier stat-card icons directly above.'
  visible_tells:
  - 'Strip icons are very small and several are generic UI shapes (pill bottle, shield, headset)'
  - 'Their stroke weight reads thinner/different from the stat-card icon set higher on the page'
  confidence: 'medium'
- id: iconography_06
  family: 'iconography_illustration'
  polarity: 'poor'
  page_or_region: 'safety page — content area'
  tile_path: 'store/remedymeds-com/captures/2026-06-01/tiles/safety/tile-00-y00000.png'
  claim: 'The safety page content area carries no icons or illustration — just four text links each ending in a generic right-chevron — making it the most graphically bare page in the set and inconsistent with the icon-rich homepage.'
  visible_tells:
  - 'Only a small right chevron at the end of each accordion row — a default UI affordance, not a designed icon'
  - 'No icons beside the drug names, no illustration, no certification graphic in the content area'
  confidence: 'high'
  contrast_with: 'store/remedymeds-com/captures/2026-06-01/tiles/homepage/tile-06-y07320.png'
- id: iconography_07
  family: 'iconography_illustration'
  polarity: 'mixed'
  page_or_region: 'homepage footer — trust badges'
  tile_path: 'store/remedymeds-com/captures/2026-06-01/tiles/homepage/tile-12-y14640.png'
  claim: 'The footer places a flat bitmap US flag beside a third-party LegitScript Certified badge — neither is a designed brand icon, and both sit outside the site''s monoline icon language.'
  visible_tells:
  - 'LegitScript badge is a recognizable third-party shield graphic in its own green/navy colorway'
  - 'US flag is a flat bitmap, not stylized to match the site''s monoline icon set'
  confidence: 'high'
```

## Provenance

Tiles read: homepage (14) + med_semaglutide (7) + med_tirzepatide (7) + quiz (1) + safety (2) = 31 native-resolution tiles from `captures/2026-06-01/tiles/` (the 06-04 capture was logos-only; 06-03 stored no screenshots).

QA exclusion: the homepage batch-testing quality-cards region (`homepage/tile-04`) was caught mid-reveal-animation — top row settled (Potency/Sterility, "Passed"), bottom row showing double-rendered overlapping text, floating cards mid-flight, and a blank "Every result verified" icon. A miner card built on that garbled region (a `poor` layout claim) was excluded as a capture artifact, not design evidence; the same tile's settled yellow trust-strip region was unaffected. No Tier-B re-render — the quality-cards section is not load-bearing (component discipline is already covered by clean tiles), so re-shooting the page for one card was unwarranted.

Mined blind + judged per [`/visual-evidence`](../../skills/visual-evidence/SKILL.md): four family miners (Sonnet) saw only the tile paths — no dossier, no Notion, no web — and the judge (Opus) pruned 49 raw cards to 34, correcting two miner mis-reads (a claimed PDP-header hierarchy defect and a safety-page h1 defect that the tiles contradict) and rejecting letterboxed/shrunken thumbnail tiles and a mid-scroll marquee frame as capture caveats. One further card (`layout_08`) was dropped at write time per the QA exclusion above, leaving 33. Snapshot caveat: reflects the 2026-06-01 capture; the live site changes.
