---
schema_version: "1.0"
domain: mydrhank.com
captured_at: 2026-06-16
source_capture: 2026-06-03
qa_status: recapture-used
---

## Visual & brand impression

A tight navy-and-cream two-tone governs the whole site — cream fields, navy CTAs, navy-label vials, and a navy footer that closes every page [color_01] — with a single amber accent held strictly to benefit-list dots [color_02]. The real strength is system discipline: reusable card grids [layout_01], alternating 50/50 splits [layout_02], a "How it works" strip reused verbatim across page types [layout_03], and a repeatable outsized-stat typographic module that recurs across both PDPs [typography_02], anchored by an italic-accented serif hero [typography_01] and restrained, editorial science charts [iconography_01]. It thins on the image and icon layer: stock-assembled photos with clashing color temperatures [color_04][color_05], no real icon vocabulary [iconography_02], a flat product-card stack [typography_03], and illegible footer legal type [typography_05]. Disciplined template, shallow imagery.

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: 'Homepage hero — main headline'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/homepage/tile-00-y00000.png
  claim: 'The hero headline is a large serif with select words set in italic (''weight'', ''longevity & sexual wellness''), giving a clear top-of-scale anchor and intra-headline rhythm beyond size alone.'
  visible_tells:
  - 'Oversized serif headline dwarfs the nav text and the smaller sans subhead beneath it by several size steps'
  - 'Italic treatment falls on specific words within the headline while others stay roman, adding contrast inside the headline itself'
  confidence: high
  contrast_with: store/mydrhank-com/captures/2026-06-03/tiles/homepage/tile-01-y01220.png
- id: typography_02
  family: typography_hierarchy
  polarity: strong
  page_or_region: 'PDPs — science-section stat callouts (semaglutide ~15%/24%, NAD+ 50%/6x)'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/pdp-compounded-semaglutide/tile-02-y02440.png
  claim: 'An outsized numeral + lighter inline qualifier + prose-explanation pattern, under a small-caps section label, builds a sharp four-tier hierarchy that repeats verbatim across two different PDPs — a deliberate system, not a one-off.'
  visible_tells:
  - '''~15%'' and ''24%'' are set at display scale with a smaller-weight descriptor on the same baseline, prose beneath'
  - 'Identical treatment recurs on the NAD+ PDP (''50%'', ''6x''), confirming a repeatable typographic module'
  - 'Small-caps labels (''SCIENCE'', ''RESULTS TIMELINE'') sit above the section heads as a distinct micro-tier'
  confidence: high
  contrast_with: store/mydrhank-com/captures/2026-06-03/tiles/pdp-nad-injection/tile-01-y01220.png
- id: typography_03
  family: typography_hierarchy
  polarity: mixed
  page_or_region: 'Homepage — product card grid (MDH Drive, Generic Sildenafil, etc.)'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/homepage/tile-03-y03660.png
  claim: 'Product cards collapse their three-line stack (category label / product name / form factor) to nearly uniform small size with little weight contrast, so the rows read as one block rather than a hierarchy.'
  visible_tells:
  - 'Product name (''MDH Drive'') is barely larger than the all-caps category label and the ''TABLET'' form line beneath it'
  - 'Price line and the ''Get Started'' / ''Learn more'' links sit undersized relative to the card''s footprint'
  confidence: high
  contrast_with: store/mydrhank-com/captures/2026-06-03/tiles/pdp-compounded-semaglutide/tile-02-y02440.png
- id: typography_04
  family: typography_hierarchy
  polarity: mixed
  page_or_region: 'PDP compounded semaglutide — FAQ accordion'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/pdp-compounded-semaglutide/tile-01-y01220.png
  claim: 'FAQ question rows are set at a single modest weight with only a chevron to signal interactivity, leaving the closed accordion typographically flat relative to the bold science heads right below it.'
  visible_tells:
  - 'Question text (''How do I take it?'', ''What are the side effects?'') reads at near-body weight with no bold or size step'
  - 'Right below, ''How Injectable Semaglutide Works'' is markedly heavier/larger — the contrast highlights how plain the FAQ rows are'
  confidence: medium
- id: typography_05
  family: typography_hierarchy
  polarity: poor
  page_or_region: 'Footer legal disclaimer — all pages'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/category-longevity/tile-01-y00669.png
  claim: 'The footer''s legal disclaimer is set so small against the deep-navy field that it renders as a near-illegible low-contrast grey band beneath the nav links.'
  visible_tells:
  - 'Bottom legal text (''Compounded medications are not FDA-approved...'') is a faint grey on navy, far below comfortable reading size'
  - 'No size, weight, or color step separates the disclaimer from the footer nav links above it'
  confidence: high
- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: 'Card grids — 3-col product row and 4-col care-plan row (homepage)'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/homepage/tile-01-y01220.png
  claim: 'Product and category card grids hold consistent column widths, equal gutters, centered product imagery, and identical label/price/CTA placement, evidencing a disciplined, reusable card component.'
  visible_tells:
  - 'Three GLP-1 cards (Tirzepatide, Semaglutide, Oral Semaglutide) share identical height, vial size, price position, and button placement with even gutters'
  - 'Four-up care-plan row repeats the same structure on a unified card background with Learn More at a constant vertical position'
  confidence: high
  contrast_with: store/mydrhank-com/captures/2026-06-03/tiles/homepage/tile-02-y02440.png
- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: 'Homepage — alternating split sections (Sermorelin, NAD+, Hair Growth)'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/homepage/tile-04-y04880.png
  claim: 'A 50/50 image / content split repeats across multiple category sections with matching proportions and consistent photo-column alignment, a steady editorial cadence down the page.'
  visible_tells:
  - 'NAD+ section pairs a left rounded-corner lifestyle photo with a right text block of amber-dot bullets and CTA'
  - 'Same split proportion and top alignment recur for Hair Growth (tile-05) and Sermorelin (tile-03)'
  confidence: high
  contrast_with: store/mydrhank-com/captures/2026-06-03/tiles/homepage/tile-05-y06100.png
- id: layout_03
  family: layout_composition_components
  polarity: strong
  page_or_region: '''How it works'' process strip — reused across homepage, category, and PDP pages'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/homepage/tile-06-y07320.png
  claim: 'A numbered-circle process strip with equally spaced columns and identical text hierarchy is reused verbatim across multiple page types, confirming a global component.'
  visible_tells:
  - 'Numbered circles 1-4 above step titles, equal column widths and aligned body copy'
  - 'The identical strip appears on the longevity category page (category-longevity/tile-01) and at the foot of the weight-loss and PDP pages'
  confidence: high
  contrast_with: store/mydrhank-com/captures/2026-06-03/tiles/category-longevity/tile-01-y00669.png
- id: layout_04
  family: layout_composition_components
  polarity: mixed
  page_or_region: 'Homepage — hero section composition'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/homepage/tile-00-y00000.png
  claim: 'The hero is clean and well-spaced but compositionally template-grade: a centered headline over an inline feature card and a tab row, with no distinctive spatial move or brand anchor.'
  visible_tells:
  - 'Centered headline floats above a single feature card sitting in a wide open cream field with large empty margins'
  - 'Tab row (Weight Loss / Longevity / Hair / Sexual Health) below the card is functional but visually unremarkable'
  confidence: high
- id: layout_05
  family: layout_composition_components
  polarity: mixed
  page_or_region: 'PDP — Compounded Semaglutide above-the-fold split'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/pdp-compounded-semaglutide/tile-00-y00000.png
  claim: 'The PDP hero splits a left product image against a right content panel, but the columns feel misweighted — the vial sits in a large neutral zone while the right stacks selector, bullets, price, and CTA in tight succession.'
  visible_tells:
  - 'Product vial occupies a wide light-grey panel with little visual interest'
  - 'Right column packs formulation tabs, bullet list, price, and CTA button with minimal breathing room between elements'
  confidence: medium
- id: layout_06
  family: layout_composition_components
  polarity: mixed
  page_or_region: 'Homepage / PDP — ''Your health is personal'' 2x2 card grid'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/homepage/tile-07-y08047.png
  claim: 'The 2x2 ''personalized care'' grid is internally consistent but undifferentiated — all four cards share the same warm-grey background, photo size, and text weight, so the block reads as density rather than hierarchy.'
  visible_tells:
  - 'Four cards (''Your doctor not an algorithm'', ''1-on-1 patient support'', ''Personalized to you'', ''Ongoing not transactional'') are identical in card color, image size, and text weight'
  - 'No card is elevated or weighted despite differing content'
  confidence: high
  contrast_with: store/mydrhank-com/captures/2026-06-03/tiles/pdp-nad-injection/tile-03-y03660.png
- id: layout_07
  family: layout_composition_components
  polarity: poor
  page_or_region: 'PDPs — ''3 simple steps'' section rhythm'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/pdp-compounded-semaglutide/tile-03-y03660.png
  claim: 'The ''3 simple steps'' row floats three small rounded-corner photos in a near-empty band with excess white space above and below, giving the page an unresolved break in vertical rhythm.'
  visible_tells:
  - 'Three step photos (phone, doctor, package) sit in a sparse section bracketed by large empty gaps top and bottom'
  - 'The thin row of small images carries little visual weight relative to the whitespace around it'
  confidence: medium
- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: 'Site-wide palette — navy + cream two-tone'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/homepage/tile-00-y00000.png
  claim: 'The site holds a tight two-tone system — warm cream/off-white body with a single deep navy as the structural color — extended into the products (navy-label vials) and the full-width navy footer that closes every page.'
  visible_tells:
  - 'Cream background fills the hero with navy reserved for CTA and login buttons; no competing hue intrudes'
  - 'All product vials (Tirzepatide, Semaglutide, NAD+) carry the same navy-label styling, making the products an extension of the palette'
  - 'Identical deep-navy footer block with white wordmark closes the homepage, category, and PDP pages'
  confidence: high
  contrast_with: store/mydrhank-com/captures/2026-06-03/tiles/category-longevity/tile-01-y00669.png
- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: 'Feature-list bullets — amber/gold accent dots across sections'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/homepage/tile-03-y03660.png
  claim: 'A warm amber/gold dot is the one accent allowed outside navy and cream, held to a single function (benefit-list markers) and never drifting to another hue across sections.'
  visible_tells:
  - 'Small amber circular markers precede each benefit bullet in the Sermorelin ''growth hormone'' section'
  - 'Same amber dot recurs in the NAD+ split section and elsewhere, always in the same bullet role'
  confidence: high
  contrast_with: store/mydrhank-com/captures/2026-06-03/tiles/homepage/tile-04-y04880.png
- id: color_03
  family: color_brand_imagery
  polarity: mixed
  page_or_region: 'Homepage — care-plan card backgrounds (lavender-blue tint)'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/homepage/tile-02-y02440.png
  claim: 'The care-plan category cards introduce a pale lavender-blue card fill distinct from the cream/white used elsewhere, but this surface does not recur in the same role on category or PDP pages — it reads as a mild local inconsistency.'
  visible_tells:
  - 'Sexual Health / Sermorelin / NAD+ / Hair Loss cards sit on a muted lavender-blue tint while the product cards just below them are plain white'
  - 'The lavender surface does not reappear in the same role elsewhere in the captures'
  confidence: medium
  contrast_with: store/mydrhank-com/captures/2026-06-03/tiles/homepage/tile-03-y03660.png
- id: color_04
  family: color_brand_imagery
  polarity: mixed
  page_or_region: 'Lifestyle photography — color-temperature mismatch (weight-loss mosaic + split-section photos)'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/category-weight-loss/tile-00-y00000.png
  claim: 'Lifestyle imagery looks sourced rather than commissioned as a set: the weight-loss header mosaic mixes warm, cool-green, and neutral cells with no shared color grade, and adjacent homepage split-section photos carry different color temperatures.'
  visible_tells:
  - 'Six portrait tiles in the weight-loss header sit warm-lit cells beside cooler greenish and neutral cells, backgrounds varying (white, warm studio, outdoor)'
  - 'Homepage couple photo is warm-interior while the gym-man photo is cooler ambient — no unifying grade across images'
  confidence: high
  contrast_with: store/mydrhank-com/captures/2026-06-03/tiles/homepage/tile-04-y04880.png
- id: color_05
  family: color_brand_imagery
  polarity: poor
  page_or_region: '''Personalized care'' 2x2 and ''3 simple steps'' — stock photo color incoherence'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/pdp-compounded-semaglutide/tile-03-y03660.png
  claim: 'The templated care/process photo blocks pair clinician and patient shots with clashing backgrounds — sage-green, white, warm tan, outdoor — and no shared color grade, pointing to stock assembly with no art direction; the same blocks recur verbatim across homepage and PDPs.'
  visible_tells:
  - 'In the 2x2 block, the female-doctor card has a sage-green backdrop, the male-doctor neutral grey, the patient card warm tan — three distinct background colors in one grid'
  - 'The ''3 simple steps'' photos (warm-amber phone shot, cool-green doctor, neutral box) mismatch in the same way and repeat identically on the NAD+ PDP'
  confidence: high
  contrast_with: store/mydrhank-com/captures/2026-06-03/tiles/homepage/tile-07-y08047.png
- id: iconography_01
  family: iconography_illustration
  polarity: strong
  page_or_region: 'PDP science charts — semaglutide and NAD+ line charts'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/pdp-nad-injection/tile-01-y01220.png
  claim: 'The inline science charts share a consistent, restrained visual grammar — thin navy strokes, sparse gridlines, muted axis labels, a dashed-placebo vs solid-treatment convention — that reads as intentional editorial design across two PDPs, not a library default.'
  visible_tells:
  - 'NAD+ tile shows two stacked charts with matching off-white containers, identical axis-label sizing, and a dashed/solid line legend (Treatment vs Placebo)'
  - 'Semaglutide PDP (''Average weight loss trajectory'', ''Reduction in caloric intake'') uses the same thin single-color line on light-grey card with no fill, shadow, or gradient'
  confidence: high
  contrast_with: store/mydrhank-com/captures/2026-06-03/tiles/pdp-compounded-semaglutide/tile-01-y01220.png
- id: iconography_02
  family: iconography_illustration
  polarity: mixed
  page_or_region: 'Process strip and category cards — absence of an icon system'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/homepage/tile-06-y07320.png
  claim: 'The site carries no real icon/pictogram vocabulary: the ''How it works'' strip leans on bare numbered circles, and category cards rely entirely on product photography, leaving navigation and process flat next to the editorial-quality charts.'
  visible_tells:
  - 'Four-step strip uses plain numbered circles (1-4) with text only — no pictograms or micro-illustrations'
  - 'Care-plan category cards carry only a product photo and text label, no category icon or graphic mark to aid scanning'
  confidence: medium
  contrast_with: store/mydrhank-com/captures/2026-06-03/tiles/pdp-nad-injection/tile-01-y01220.png
- id: iconography_03
  family: iconography_illustration
  polarity: mixed
  page_or_region: 'Homepage footer — LegitScript certification badge'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/category-longevity/tile-01-y00669.png
  claim: 'The footer centers an ornate shield-style LegitScript certification badge whose graphic density is out of step with the site''s otherwise flat, minimal graphic vocabulary.'
  visible_tells:
  - 'Circular green-and-white shield badge sits above the wordmark in the navy footer'
  - 'Its detailed ornamentation contrasts with the flat numbered circles, plain check bullets, and minimal charts used everywhere else'
  confidence: medium
- id: iconography_04
  family: iconography_illustration
  polarity: poor
  page_or_region: 'PDP semaglutide — ''What to expect'' results timeline'
  tile_path: store/mydrhank-com/captures/2026-06-03/tiles/pdp-compounded-semaglutide/tile-02-y02440.png
  claim: 'The ''What to expect'' timeline relies only on small colored marker dots over date labels — no connecting line, milestone icons, or progression graphic — making it the weakest-illustrated section on an otherwise chart-heavy PDP.'
  visible_tells:
  - 'Three milestone columns (Month 2-5, Weeks 8-16, Month 6+) each headed by a single small colored dot and a date, with no connecting diagram'
  - 'No icon or visual progression ties the three stages together'
  confidence: medium
```

## Provenance

Tiles read: homepage (8) + category-weight-loss (4) + category-longevity (2) + pdp-compounded-semaglutide (5) + pdp-nad-injection (5) = 24 from `captures/2026-06-03/tiles/` — all 24 active, no exclusions. **Tier-B re-render used for all five pages** via `scripts/shoot.py --dismiss`: the cached Firecrawl payloads carried a site-wide "We use cookies" consent strip stamped over high-value regions (hero, product grids, PDP calculator/FAQ). `--dismiss` cleared it affordance-only — Escape + a click on the strip's own "Reject all" control (no vendor denylist, no CSS-hide) — leaving the sticky nav intact; the page never scroll-locked, and `shoot.py` emitted an `overview-480w.png` per page for the QA gate (`dismissed: true`, `scroll_locked: false` in every manifest). Every cited tile is therefore a clean system-Chrome re-render (`qa_status: recapture-used`). Mined blind + judged per [`/visual-evidence`](../../skills/visual-evidence/SKILL.md): four family miners (Sonnet) saw only the tiles (no dossier, no web); the judge (Opus) consolidated 39 raw cards to 21 accepted, merging duplicate tells (the cross-PDP stat-callout system, the 3-col/4-col card component, the reused "How it works" strip, the navy+cream two-tone incl. navy-label vials + footer, the lifestyle/stock-photo incoherence pair, and the shared chart system) and rejecting three as unverifiable in-tile (the weight-loss "ad-hoc mosaic", "clipped card labels", and a feature-heading "diluted authority" taste-judgment) — no capture-caveat rejections, since the dismissed renders carried no overlay/blank/black/lazy contamination. Every `poor` structural card was spot-checked against its native tile — all genuine (sparse "3 simple steps" rhythm, dot-only results timeline, stock-photo color incoherence, footer-legal illegibility), none capture artifacts. Snapshot caveat: tiles reflect the live site re-rendered 2026-06-16; the cached source capture is 2026-06-03. The site changes.
