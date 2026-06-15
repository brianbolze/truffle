---
schema_version: "1.0"
domain: gethealthspan.com
captured_at: 2026-06-15
source_capture: 2026-06-04
qa_status: exclusions-noted
---

## Visual & brand impression

Healthspan reads as a polished, system-driven longevity brand — strongest on the assets it owns, weakest on the ones it borrows. Product photography is genuinely cohesive: every SKU shot on one grey ground at matched scale and shadow [color_04][iconography_02][iconography_03]. The proprietary dot-grid biomarker graphic [iconography_01], floated brand-vs-others comparison table [layout_04][iconography_05], and repeating component grids [layout_01][layout_02][layout_05] all hold their discipline, while a restrained dark-gradient palette with one blue/amber accent per section [color_01][color_03] and an oversized cream wordmark footer [color_06] signal real brand intent. It slips on borrowed or atmospheric content: stock-adjacent people and team photography [color_08][color_10], a gridless image mosaic [layout_07], near-empty dark "sphere/blob" transition frames that read unfinished [layout_10][iconography_10], and a watermark-faint section heading [typography_08].

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: "homepage — hero heading with blue accent phrase"
  tile_path: store/gethealthspan-com/captures/2026-06-04/tiles/homepage/tile-04-y04880.png
  claim: "A two-tone heading pattern — black run plus a same-size blue accent phrase on the same line — builds hierarchy without leaning on scale, with a tracked-caps label as a distinct third level."
  visible_tells:
    - "\"Your journey to a longer, healthier life is\" in black, then \"just a few steps away\" in blue at identical size on the same line"
    - "Small spaced-caps \"BECOMING A PATIENT\" sits flush-left above the heading as a third level"
  confidence: high
  contrast_with: store/gethealthspan-com/captures/2026-06-04/tiles/homepage/tile-06-y07320.png
- id: typography_02
  family: typography_hierarchy
  polarity: strong
  page_or_region: "medications — product detail layout"
  tile_path: store/gethealthspan-com/captures/2026-06-04/tiles/medications/tile-02-y02440.png
  claim: "Product rows hold a clean four-level hierarchy — section header, large product name, regular body, bulleted benefit lines — each step visually distinct, with a medium-weight price line cleanly separated from body and buttons."
  visible_tells:
    - "\"SGLT2 Protocol\" set large/bold above a one-sentence body at clearly smaller size"
    - "\"Starting at $99/mo\" price line sits at its own weight, separated from the three icon-bullets and the GET STARTED / LEARN MORE labels"
  confidence: high
- id: typography_03
  family: typography_hierarchy
  polarity: strong
  page_or_region: "rapamycin — product detail page hero"
  tile_path: store/gethealthspan-com/captures/2026-06-04/tiles/rapamycin/tile-00-y00000.png
  claim: "The detail-page hero carries the most complete type hierarchy in the set: nav wordmark, large h1, two-sentence body, icon-feature rows with smaller sub-copy, a price line, and CTA — every level sized distinctly and legible."
  visible_tells:
    - "\"The Rapamycin Protocol\" h1 is the largest block in the right column"
    - "Benefit sub-copy (e.g. \"Resets hyperactive mTOR signaling...\") is visibly smaller and lighter than the benefit header above it (\"Reset cellular aging\")"
  confidence: high
- id: typography_04
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "homepage — stat / social-proof strip"
  tile_path: store/gethealthspan-com/captures/2026-06-04/tiles/homepage/tile-01-y01220.png
  claim: "The four-stat credibility strip uses a number-then-label structure, but the number is only modestly larger than its label and all four columns are typographically identical, so no primary stat anchors the quick scan."
  visible_tells:
    - "Stat numbers sit only slightly larger/bolder than the label text directly beneath them"
    - "All four columns share one treatment with no visual anchor distinguishing the lead stat"
  confidence: medium
  contrast_with: store/gethealthspan-com/captures/2026-06-04/tiles/medications/tile-02-y02440.png
- id: typography_05
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "labs — biomarker word cloud"
  tile_path: store/gethealthspan-com/captures/2026-06-04/tiles/labs/tile-02-y02440.png
  claim: "The \"(Types of tests)\" biomarker cloud varies term size and opacity to suggest depth, but the steps follow no editorial principle and long clinical strings wrap mid-item, interrupting the rhythm."
  visible_tells:
    - "Biomarker names appear in several sizes with no clear rule for which is largest"
    - "Long strings like \"MCHC (Mean Crp Hgb Concentration)\" and \"MCH (Mean Corpuscular Hemoglobin)\" wrap awkwardly next to short terms"
  confidence: medium
- id: typography_06
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "how_it_works — numbered step labels"
  tile_path: store/gethealthspan-com/captures/2026-06-04/tiles/how_it_works/tile-01-y01220.png
  claim: "The step-label system (\"01 — ASSESSMENT\" on a hairline rule) is legible but understated — split across the full width and separated by heavy padding from its heading, so the label competes with whitespace rather than anchoring the eye."
  visible_tells:
    - "\"01\" small at far left, \"ASSESSMENT\" small spaced-caps at far right, joined by a thin full-width rule"
    - "Heading \"No clipboards or waiting rooms.\" sits with large top padding below the rule, delaying the connection to the step label"
  confidence: medium
- id: typography_07
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "our_company — founder story block"
  tile_path: store/gethealthspan-com/captures/2026-06-04/tiles/our_company/tile-02-y02440.png
  claim: "The founder-story block runs only two levels — a spaced-caps label and the body paragraph — with no mid-level subheads or weight pulls to break the prose, making it a heavier read than the product-page copy."
  visible_tells:
    - "\"OUR STORY\" spaced-caps label, then \"Our quest for longer lives started with a fight\" jumps to display size"
    - "The multi-paragraph body that follows has no internal subheads, bold pulls, or weight variation"
  confidence: medium
- id: typography_08
  family: typography_hierarchy
  polarity: poor
  page_or_region: "homepage — \"Featured In\" section heading"
  tile_path: store/gethealthspan-com/captures/2026-06-04/tiles/homepage/tile-06-y07320.png
  claim: "The \"Featured In\" heading is set at an outsized display scale in a light gray close to the page background, so it reads as a watermark rather than a section anchor — and the darker spaced-caps label above it inverts the usual label-vs-heading weighting."
  visible_tells:
    - "\"Featured In\" occupies roughly a third of the tile height in very light gray, near the white background value"
    - "\"AHEAD OF THE FIELD\" label above is smaller but darker than the heading it introduces"
  confidence: high
  contrast_with: store/gethealthspan-com/captures/2026-06-04/tiles/homepage/tile-04-y04880.png
- id: typography_09
  family: typography_hierarchy
  polarity: poor
  page_or_region: "how_it_works — \"experts will see you now\" portrait grid"
  tile_path: store/gethealthspan-com/captures/2026-06-04/tiles/how_it_works/tile-03-y03660.png
  claim: "A medium heading and small gray body sit centered in a large white field ringed by floating portraits, so the type reads as undersized and adrift while the photo grid pulls the eye first."
  visible_tells:
    - "\"The experts will see you now.\" heading is smaller than the portrait thumbnails framing it"
    - "The supporting body line is very small and low-contrast gray in the whitespace-heavy layout"
  confidence: medium
- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: "homepage — program card row"
  tile_path: store/gethealthspan-com/captures/2026-06-04/tiles/homepage/tile-01-y01220.png
  claim: "A three-column grid of equal-width portrait cards repeats with disciplined consistency — same corner radius, same label baseline, same arrow-in-circle CTA position on every card."
  visible_tells:
    - "Three cards share identical corner radius and dimensions"
    - "Arrow-in-circle CTA sits at the same lower-left spot on each card"
    - "Category labels (e.g. \"Longevity Optimization\") align to the same vertical baseline across all three"
  confidence: high
- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: "medications — product listing rows"
  tile_path: store/gethealthspan-com/captures/2026-06-04/tiles/medications/tile-02-y02440.png
  claim: "Product rows lock to an image-left / text-right split with a consistent light-grey image card, a three-bullet icon list, a price line, and a paired filled/outlined button set — the same component repeats with no measurable variation across products."
  visible_tells:
    - "Image card keeps identical light-grey ground and proportions across the SGLT2 and Acarbose rows"
    - "Three orange circle-arrow bullet icons align to the same left margin each time"
    - "Paired GET STARTED (filled) / LEARN MORE (outlined) buttons hold identical widths and spacing"
  confidence: high
  contrast_with: store/gethealthspan-com/captures/2026-06-04/tiles/supplements/tile-02-y02440.png
- id: layout_03
  family: layout_composition_components
  polarity: strong
  page_or_region: "how_it_works — step sections"
  tile_path: store/gethealthspan-com/captures/2026-06-04/tiles/how_it_works/tile-02-y02440.png
  claim: "Each step pins a step-number to the far-left margin and a category tag to the far-right on a full-width hairline rule, a precise horizontal anchor that recurs verbatim across the steps with a centered device mockup floating below."
  visible_tells:
    - "Full-width hairline rule with \"02\" left and \"CONNECT\" right"
    - "Centered iPad mockup floats in generous whitespace beneath the rule"
    - "The same scaffold repeats from step 01 through 04"
  confidence: high
- id: layout_04
  family: layout_composition_components
  polarity: strong
  page_or_region: "homepage — feature comparison table"
  tile_path: store/gethealthspan-com/captures/2026-06-04/tiles/homepage/tile-07-y08540.png
  claim: "The brand-vs-others comparison uses a dark pill-shaped column to float the brand over five evenly-spaced rows, with hairline separators and centered check/x glyphs — an internally consistent custom table with no visible alignment breaks."
  visible_tells:
    - "Dark rounded column extends above and below the row band, centering the \"Healthspan\" header"
    - "Five row separators are evenly spaced and match across both columns"
    - "Check glyphs are vertically centered in every brand-column cell"
  confidence: high
- id: layout_05
  family: layout_composition_components
  polarity: strong
  page_or_region: "rapamycin — product detail hero"
  tile_path: store/gethealthspan-com/captures/2026-06-04/tiles/rapamycin/tile-00-y00000.png
  claim: "The detail hero holds a confident ~45/55 two-column split: feature-image panel with a MOST EFFECTIVE badge on the left, and a structured right column stacking heading, body, hairline-separated benefit rows, a utility list, pricing, full-width CTA, and a star rating — all left-aligned to one margin."
  visible_tells:
    - "MOST EFFECTIVE badge pinned top-left of the image panel"
    - "Right column stacks heading → description → three icon benefit rows → HSA/FSA utility list → pricing → CTA → \"4.9 ... 12,000+ patients served\", all to the same left margin"
    - "Hairline separators between benefit rows are consistent width"
  confidence: high
- id: layout_06
  family: layout_composition_components
  polarity: strong
  page_or_region: "footer — site-wide"
  tile_path: store/gethealthspan-com/captures/2026-06-04/tiles/homepage/tile-10-y12075.png
  claim: "The footer organizes nav into labeled column groups with consistent heading weight and list spacing, plus an inset featured-treatment card and a newsletter input — clean column structure at a density appropriate to a content-heavy footer."
  visible_tells:
    - "Multiple column groups (Treatments, Top Treatments, About, Science, Support) share matching all-caps label weight and spacing"
    - "Inset Rapamycin Protocol card with product image and CTA sits in a defined panel"
    - "Email input and submit button align in a left column at matching height to the nav columns"
  confidence: high
- id: layout_07
  family: layout_composition_components
  polarity: mixed
  page_or_region: "homepage — \"personal care\" floating-image section"
  tile_path: store/gethealthspan-com/captures/2026-06-04/tiles/homepage/tile-05-y06100.png
  claim: "The scattered-image composition around the centered copy reads as arbitrary rather than purposefully tensioned — items vary in scale and offset with no visible grid, and the cluster doesn't frame the text block cleanly."
  visible_tells:
    - "Six-plus image tiles at different scales and x/y offsets with no visible grid or rhythm"
    - "Pill/product image and the blue-orb hand photo differ markedly in size with no apparent ratio logic"
    - "Centered \"Personal care for optimal health\" block sits in open space the surrounding cards don't enclose"
  confidence: medium
  contrast_with: store/gethealthspan-com/captures/2026-06-04/tiles/homepage/tile-01-y01220.png
- id: layout_08
  family: layout_composition_components
  polarity: mixed
  page_or_region: "our_company — hero photo strip"
  tile_path: store/gethealthspan-com/captures/2026-06-04/tiles/our_company/tile-00-y00000.png
  claim: "The hero is a staggered horizontal strip of portrait photos at varying widths, intended as a mosaic — but no rule governs which photos are wider and the central older-man photo is markedly larger without a supporting anchor, so it reads as assembled rather than designed."
  visible_tells:
    - "Multiple photos with several distinct widths in no discernible alternating pattern"
    - "Central older-man photo is taller/wider than its neighbors with nothing else justifying the prominence"
    - "Strip abuts the dark nav above with no padding"
  confidence: medium
- id: layout_09
  family: layout_composition_components
  polarity: mixed
  page_or_region: "programs — program card blocks"
  tile_path: store/gethealthspan-com/captures/2026-06-04/tiles/programs/tile-01-y01220.png
  claim: "Program cards pair a dark dashboard-style image composite on the left with a consistent text block on the right, but the image composites vary in internal density between programs — one shows a single metric, the next shows multiple stacked UI panels — so the image column lacks a shared composition rule."
  visible_tells:
    - "GLP-1 card's left panel shows a single metric (\"5.4\"); the Hormone card's left panel stacks multiple UI panels (\"7.25\")"
    - "Right column structure (title, description, bullets, price, buttons) stays consistent while the left image column does not"
    - "Section headers reuse the same parenthetical face (\"(Metabolism)\", \"(Hormone)\") seen on the medications page"
  confidence: medium
- id: layout_10
  family: layout_composition_components
  polarity: poor
  page_or_region: "how_it_works — dark section-break transition"
  tile_path: store/gethealthspan-com/captures/2026-06-04/tiles/how_it_works/tile-04-y04880.png
  claim: "The dark blurred-sphere transition between step modules is mostly empty dark gradient with only a small label — it adds no compositional value and breaks the scroll pacing, with low-resolution blurred shapes that look unfinished."
  visible_tells:
    - "Tile is roughly 80% dark gradient with no content but a thin step label near the bottom edge"
    - "Blurred spherical shapes lack edge definition and read as unfinished"
    - "No typographic or structural element anchors the center"
  confidence: high
  contrast_with: store/gethealthspan-com/captures/2026-06-04/tiles/how_it_works/tile-02-y02440.png
- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: "homepage — dark hero / section transition"
  tile_path: store/gethealthspan-com/captures/2026-06-04/tiles/homepage/tile-03-y03660.png
  claim: "A controlled near-black-to-off-white gradient is used as a structural transition device, with a single yellow accent reserved for one headline phrase — deliberate accent discipline rather than decorative scatter."
  visible_tells:
    - "Blurred dark orb dissolves into the white page background across the full tile height"
    - "Yellow accent appears only on \"your long-term health\"; no other yellow in the tile"
  confidence: high
  contrast_with: store/gethealthspan-com/captures/2026-06-04/tiles/homepage/tile-04-y04880.png
- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: "homepage — headline accent system"
  tile_path: store/gethealthspan-com/captures/2026-06-04/tiles/homepage/tile-04-y04880.png
  claim: "A cornflower-blue accent is introduced for headline emphasis alongside the yellow seen elsewhere, forming a two-accent system used with restraint — one accent per heading, never stacked in the same section."
  visible_tells:
    - "Blue accent on \"just a few steps away\" in the hero heading"
    - "No yellow present in this tile; the accents are not mixed"
  confidence: high
  contrast_with: store/gethealthspan-com/captures/2026-06-04/tiles/homepage/tile-03-y03660.png
- id: color_03
  family: color_brand_imagery
  polarity: strong
  page_or_region: "labs — dark section hero"
  tile_path: store/gethealthspan-com/captures/2026-06-04/tiles/labs/tile-00-y00000.png
  claim: "On dark sections a warm amber/gold gradient is introduced as a contextual third color, keeping the dark canvas from feeling monolithic while staying earthy-scientific; a yellow CTA and yellow headline accent confirm it as a deliberate extension, not a one-off."
  visible_tells:
    - "Full-bleed amber-to-dark-brown gradient fills the hero background"
    - "Yellow GET STARTED pill and yellow accent on \"see your results\" in the headline"
  confidence: high
- id: color_04
  family: color_brand_imagery
  polarity: strong
  page_or_region: "medications — product photography"
  tile_path: store/gethealthspan-com/captures/2026-06-04/tiles/medications/tile-02-y02440.png
  claim: "Product photography is tight and owned: every bottle is shot on the same light-grey ground at the same angle with a matching soft shadow, reading as a cohesive in-house catalog rather than assembled stock."
  visible_tells:
    - "SGLT2 and Acarbose bottles both centered on identical light-grey card grounds"
    - "Matching soft drop-shadow and scale across both visible cards"
  confidence: high
- id: color_05
  family: color_brand_imagery
  polarity: strong
  page_or_region: "our_company — principles accordion detail photography"
  tile_path: store/gethealthspan-com/captures/2026-06-04/tiles/our_company/tile-04-y04880.png
  claim: "Editorial accordion photography (eye-with-microscope macro, glass petri-dish macro) is shot on atmospheric cool dark backgrounds, extending the brand's dark-science palette into interior pages and showing discipline beyond the homepage."
  visible_tells:
    - "Extreme eye/microscope crop on a navy-to-dark gradient, clinical but not generic-lab"
    - "Petri-dish macro in soft blue-grey with a specular highlight — both share a precision-in-low-light feel"
  confidence: high
- id: color_06
  family: color_brand_imagery
  polarity: strong
  page_or_region: "footer — oversized wordmark"
  tile_path: store/gethealthspan-com/captures/2026-06-04/tiles/homepage/tile-10-y12075.png
  claim: "The footer renders the wordmark at full viewport width in cream-on-near-black as a brand-confidence moment — a footer-as-canvas move that signals a deliberate brand perspective beyond pure information."
  visible_tells:
    - "\"Healthspan\" wordmark set at oversized display scale across the full page width at the bottom"
    - "Cream/off-white on near-black, with nothing competing at that scale"
  confidence: high
- id: color_07
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "homepage — \"personal care\" floating image mosaic"
  tile_path: store/gethealthspan-com/captures/2026-06-04/tiles/homepage/tile-05-y06100.png
  claim: "The floating-card mosaic mixes lifestyle photos, product renders, UI cards, macro textures, and a disembodied hand — variety that signals richness but with an inconsistent tonal range, a warm-orange card clashing against cool-blue app cards and grey product shots."
  visible_tells:
    - "Orange-tinted card sits beside a dark-blue app-UI card with no shared color logic"
    - "Hand holding a luminous blue orb appears next to a plain product-on-white render — three distinct visual idioms in one cluster"
  confidence: high
  contrast_with: store/gethealthspan-com/captures/2026-06-04/tiles/medications/tile-02-y02440.png
- id: color_08
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "homepage — program portrait cards"
  tile_path: store/gethealthspan-com/captures/2026-06-04/tiles/homepage/tile-01-y01220.png
  claim: "The three program cards use neutral studio-grey portraits with dark overlays and plain label text, reading as stock-adjacent lightly-directed shoots rather than a branded lighting or location concept — which dilutes the distinctiveness the card format implies."
  visible_tells:
    - "Neutral studio-grey backgrounds on all three portraits"
    - "Label text (\"Longevity Optimization\", \"Men's Hormone Health\", \"Women's Hormone Health\") is plain overlay with no graphic system tying it to the photos"
  confidence: medium
  contrast_with: store/gethealthspan-com/captures/2026-06-04/tiles/our_company/tile-02-y02440.png
- id: color_09
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "rapamycin — couple hero portrait"
  tile_path: store/gethealthspan-com/captures/2026-06-04/tiles/rapamycin/tile-03-y03660.png
  claim: "The couple portrait on a light circular/radial-chart ground is well-lit and aspirational, but the circular-mask crop and grey gradient reuse a template seen elsewhere rather than a bespoke treatment for this SKU page."
  visible_tells:
    - "Circular soft-edged crop on the couple mirrors the doctor/product circular thumbnails used elsewhere"
    - "Light grey radial background carries no color cue specific to rapamycin"
  confidence: medium
  contrast_with: store/gethealthspan-com/captures/2026-06-04/tiles/labs/tile-00-y00000.png
- id: color_10
  family: color_brand_imagery
  polarity: poor
  page_or_region: "our_company — team headshots"
  tile_path: store/gethealthspan-com/captures/2026-06-04/tiles/our_company/tile-06-y07320.png
  claim: "The co-founder headshots are basic three-quarter portraits on inconsistent backgrounds with no shared lighting or crop, reading as individually sourced rather than a commissioned brand shoot."
  visible_tells:
    - "Three co-founder portraits (Daniel Tawfik, Aman Fahimullah, Fazil Azhar) sit on inconsistent background tones — one warmer, two neutral-white"
    - "No framing device, color wash, or graphic element unifies the three"
  confidence: medium
- id: iconography_01
  family: iconography_illustration
  polarity: strong
  page_or_region: "labs — biomarker dot-grid dashboard"
  tile_path: store/gethealthspan-com/captures/2026-06-04/tiles/labs/tile-03-y03660.png
  claim: "The progress visualization is a purpose-built data graphic — a dot matrix keyed by three statuses (Optimal/In Range/Out of Range) plotted across Day-1 to Day-365 columns with large aggregate counts — not a stock chart or generic infographic."
  visible_tells:
    - "Three-color legend with parenthetical labels \"( OPTIMAL )\", \"( IN RANGE )\", \"( OUT OF RANGE )\""
    - "Five labeled time columns (DAY 1 through DAY 365) anchor the x-axis"
    - "Aggregate counts 130 / 24 / 26 set large distinguish it from a screenshot"
  confidence: high
  contrast_with: store/gethealthspan-com/captures/2026-06-04/tiles/rapamycin/tile-05-y06100.png
- id: iconography_02
  family: iconography_illustration
  polarity: strong
  page_or_region: "homepage — product render carousel"
  tile_path: store/gethealthspan-com/captures/2026-06-04/tiles/homepage/tile-02-y02440.png
  claim: "The carousel of Rx bottles and a spray bottle is staged on a clean white ground with consistent bottom shadow, uniform label orientation, and matched scale — a deliberate product-imaging system rather than mixed stock pulls."
  visible_tells:
    - "Five SKUs (Rapamycin, SGLT2, Oxytocin spray, Oxytocin Troche, Methylene Blue) share angle, lighting, and shadow"
    - "Branded \"Healthspan\" label visible on each bottle at consistent size and proportion"
  confidence: high
- id: iconography_03
  family: iconography_illustration
  polarity: strong
  page_or_region: "supplements — supplement product renders"
  tile_path: store/gethealthspan-com/captures/2026-06-04/tiles/supplements/tile-02-y02440.png
  claim: "The amber AMPK glass bottle and the Creatine + Electrolytes stand-up pouch are shot with the same lighting and floating-on-white presentation, extending the product-photography system from the medications page."
  visible_tells:
    - "Amber glass AMPK bottle with label set in the same typeface as the other SKU bottles"
    - "White flexible Creatine pouch with a lime-green graphic accent and the branded wordmark centered"
  confidence: high
  contrast_with: store/gethealthspan-com/captures/2026-06-04/tiles/medications/tile-04-y04880.png
- id: iconography_04
  family: iconography_illustration
  polarity: strong
  page_or_region: "how_it_works — tablet device mockup"
  tile_path: store/gethealthspan-com/captures/2026-06-04/tiles/how_it_works/tile-02-y02440.png
  claim: "The step-1 section uses a high-fidelity tablet device frame with an even bezel and cast shadow, containing a live assessment UI — the product screen is treated as the illustration rather than adding a separate graphic, and it composites cleanly with no visible seam."
  visible_tells:
    - "Rounded tablet bezel with accurate corner radius and a thin even border"
    - "Soft drop-shadow on white ground places the device in space without a compositing seam"
    - "Screen shows a live assessment UI — progress bar, Yes/No buttons, and LegitScript / HIPAA / Surescripts certification logos"
  confidence: high
- id: iconography_05
  family: iconography_illustration
  polarity: strong
  page_or_region: "homepage — comparison table check/cross glyphs"
  tile_path: store/gethealthspan-com/captures/2026-06-04/tiles/homepage/tile-07-y08540.png
  claim: "The comparison table runs a controlled two-glyph system — a filled circular check in the brand column and a bare X in the competitors column — at consistent size and alignment across all five rows."
  visible_tells:
    - "Five rows each with a dark circular badge holding a white check in the brand column"
    - "Five matching bare X marks at the same vertical alignment in the Others column, with no background treatment"
  confidence: high
- id: iconography_06
  family: iconography_illustration
  polarity: strong
  page_or_region: "homepage — app dashboard screenshot"
  tile_path: store/gethealthspan-com/captures/2026-06-04/tiles/homepage/tile-03-y03660.png
  claim: "The dashboard mockup inside the dark section is a composed product-UI screen — labeled bottom tabs, numeric score widgets, and a trend chart — reading as a real application screen cleanly composited on the dark ground rather than a placeholder."
  visible_tells:
    - "Labeled bottom tabs (Labs Analysis, Protocols, Coaching, Optimizations, MySpan) at the card foot"
    - "Two numeric scores (83, 99) and a small multi-line trend chart in the card body"
    - "Dark card floats on the dark full-bleed background with no white halo"
  confidence: high
- id: iconography_07
  family: iconography_illustration
  polarity: mixed
  page_or_region: "rapamycin — feature-list icons"
  tile_path: store/gethealthspan-com/captures/2026-06-04/tiles/rapamycin/tile-05-y06100.png
  claim: "Feature rows are prefixed with a small blue rounded-square badge icon, but at render size the glyph interior is illegible — it reads as a generic badge while the text carries the meaning."
  visible_tells:
    - "Four rows (Prescription & delivery, Lab testing, Clinical support, Longevity experts) each lead with a small blue badge whose interior detail is unreadable"
    - "The label text, not the icon, conveys each item"
  confidence: medium
  contrast_with: store/gethealthspan-com/captures/2026-06-04/tiles/labs/tile-03-y03660.png
- id: iconography_08
  family: iconography_illustration
  polarity: mixed
  page_or_region: "homepage — journey step thumbnails"
  tile_path: store/gethealthspan-com/captures/2026-06-04/tiles/homepage/tile-04-y04880.png
  claim: "Steps 2–4 of the journey are represented by small circular-cropped images that flatten into indistinct grey thumbnails, while step 1 gets a full rectangular photo — an inconsistent treatment within the same component that loses the intended meaning at a glance."
  visible_tells:
    - "Three small grey-circle thumbnails (video-call, shipping box, dashboard) cropped with no border or number overlay"
    - "Step 1 uses a full-bleed rectangular photo while steps 2–4 shrink to circles"
  confidence: medium
- id: iconography_09
  family: iconography_illustration
  polarity: mixed
  page_or_region: "medications — GLP-1 collage cards"
  tile_path: store/gethealthspan-com/captures/2026-06-04/tiles/medications/tile-04-y04880.png
  claim: "The GLP-1 cards combine an Rx bottle render, a tablet video-call screenshot, and a branded pill per card, but the compositing is uneven — element scales and tablet crops differ between cards and one card omits the bottle entirely."
  visible_tells:
    - "Zepbound card pairs a bottle with a tablet UI; Foundayo card shows a tablet and pill but no bottle; Wegovy card is partly cut off at the tile edge"
    - "Tablet screenshots are cropped at different zoom levels across the three cards"
  confidence: medium
- id: iconography_10
  family: iconography_illustration
  polarity: poor
  page_or_region: "how_it_works — \"Delivered to your door\" transition frame"
  tile_path: store/gethealthspan-com/captures/2026-06-04/tiles/how_it_works/tile-06-y07320.png
  claim: "A section-break frame is a near-black full-bleed fill with only a faint vertical light-ray and a step label — it contributes no illustrative or iconographic content and reads as placeholder atmosphere rather than intentional graphic work."
  visible_tells:
    - "Full-bleed black frame with a faint vertical stripe; \"Delivered to your door.\" is the only foreground element"
    - "Step indicator \"04\" and label \"DELIVERED\" are the only structural marks on the otherwise empty dark canvas"
  confidence: high
  contrast_with: store/gethealthspan-com/captures/2026-06-04/tiles/labs/tile-03-y03660.png
```

## Provenance

- **Tiles read.** 76 active native-resolution tiles across 8 pages — homepage, how_it_works, labs, medications, our_company, programs, rapamycin, supplements — sliced from the `2026-06-04` cached capture (`captures/2026-06-04/tiles/`).
- **Exclusion (→ `qa_status: exclusions-noted`).** `homepage/tile-00-y00000.png` was excluded: a "Get 10% Off Your Next Order" newsletter modal sits centered over the hero headline and CTA. A Tier-B browser re-render was attempted to recover a clean hero; the **timed modal re-fired** (landing over the program cards instead), so the page's clean lower tiles were kept from the cached capture and the hero was excluded rather than recaptured. The hero's brand treatment is independently covered by the clean full-bleed heroes on `our_company`, `how_it_works`, and `labs`.
- **Cookie-banner caveat (non-blocking).** A small lower-corner "We use cookies" overlay appears on `rapamycin/tile-00`, `labs/tile-00`, `our_company/tile-00`, `medications/tile-00`, and `rapamycin/tile-03`. In each case it sits in dead space and does not obscure the content the cited cards rely on (hero splits, product renders, pricing, badges all fully legible), so the judge kept those tiles — no card depends on the banner.
- **Mining.** 4 blind family miners (Sonnet, tiles-only, no network) over the 76 tiles → 49 raw cards → Opus judge pruned/merged to **40 accepted** (9 rejected for misattributed evidence, within-tile duplication across families, or soft taste-word reads with no falsifiable tell). One factual tightening: the `how_it_works/tile-02` device-mockup claim dropped an unverifiable "Dynamic Island" detail, keeping the verifiable bezel / cast-shadow / live-assessment-UI tells.
- **Snapshot caveat.** This reflects the captured tiles as of `2026-06-04`; the live site changes, so treat it as a point-in-time read.
