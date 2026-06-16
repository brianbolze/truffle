---
schema_version: "1.0"
domain: rugiet.com
captured_at: 2026-06-16
source_capture: 2026-06-07
qa_status: clean
---

## Visual & brand impression

A confident, owned editorial system: dark maroon and black grounds [color_01], a single amber-orange accent doing triple duty as footer, banner, and star color [color_02], and a bespoke "TR" wordmark deployed from nav to giant footer [iconography_04][typography_03]. Studio pill-renders are color-coded per SKU into a genuine icon system [iconography_01][color_03], a reused product-card component holds grid discipline across pages [layout_01][layout_02], and the high-fidelity 3D cube and restrained onset chart are real craft peaks [iconography_02][iconography_03]. The slips are imagery and consistency: generic stock medical renders and clip-art molecules break the proprietary look [color_06][color_07], the reviews page defects to a light-mode system [color_08], the comparison table is one-sided [layout_08], the nav reads thin [layout_10], and stat-overlay and blog imagery look unvetted [layout_11][color_10].

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: homepage hero — headline over dark image
  tile_path: store/rugiet-com/captures/2026-06-07/tiles/homepage/tile-00-y00000.png
  claim: Hero runs a clear three-step type ramp — an oversized vertical wordmark down the left edge, a mid-weight headline center-right, and smaller lighter body copy beneath — all legible white-on-dark.
  visible_tells:
  - "Oversized vertical 'RUGIET' wordmark in heavy condensed display fills the full left column"
  - "Headline 'This is the science of never settling' clearly dominant over the subhead"
  - Body line below the headline is visibly smaller and lighter, completing a three-tier ramp
  confidence: high
- id: typography_02
  family: typography_hierarchy
  polarity: strong
  page_or_region: reviews page — review card grid
  tile_path: store/rugiet-com/captures/2026-06-07/tiles/reviews/tile-00-y00000.png
  claim: "Review cards hold a consistent three-tier hierarchy across the whole grid: heavy all-caps headline, lighter mixed-case body, and a small 'VERIFIED PATIENT' label at the foot."
  visible_tells:
  - "Review titles ('ALL I CAN SAY IS WOW', 'GREAT PRODUCT!') in heavy all-caps grotesque, clearly dominant"
  - Body copy in a monospace-like lighter, smaller face creates an unambiguous content tier
  - "'VERIFIED PATIENT' in small bold caps anchors a third, badge-level tier in every card"
  confidence: high
- id: typography_03
  family: typography_hierarchy
  polarity: strong
  page_or_region: homepage footer — 'PERFORMANCE MEDICINE FOR MEN' orange bar
  tile_path: store/rugiet-com/captures/2026-06-07/tiles/ed-ready/tile-13-y15490.png
  claim: The orange footer deploys ultra-bold condensed all-caps display type at huge scale as a visual full stop, with footer nav links at a fraction of the size — a deliberate, dramatic scale jump.
  visible_tells:
  - "'PERFORMANCE MEDICINE FOR MEN' set in ultra-bold condensed caps at display scale on solid orange"
  - Footer nav links immediately below are small regular weight — roughly a 5x size ratio
  - Same display treatment recurs on the homepage footer tile, confirming it is systematic
  confidence: high
  contrast_with: store/rugiet-com/captures/2026-06-07/tiles/homepage/tile-10-y11450.png
- id: typography_04
  family: typography_hierarchy
  polarity: strong
  page_or_region: ed-ready — RD-37 annotated-diagram callouts
  tile_path: store/rugiet-com/captures/2026-06-07/tiles/ed-ready/tile-06-y07320.png
  claim: Diagram callout boxes carry a tidy micro-hierarchy — numbered orange pip, bold label line, then lighter explanatory sentence — that stays readable at small size in frosted-grey boxes.
  visible_tells:
  - "Callout header 'Targeted sublingual absorption' bold; explanation beneath is regular weight and smaller"
  - Numbered orange square pip sits above each label as a distinct entry tier
  - "Section headline 'RD-37 is the future of ED medication' is the largest tier, anchoring the page"
  confidence: high
- id: typography_05
  family: typography_hierarchy
  polarity: mixed
  page_or_region: homepage — product card strip (Ready, Go Long, Daily Boost, Grower)
  tile_path: store/rugiet-com/captures/2026-06-07/tiles/homepage/tile-01-y01220.png
  claim: Homepage product cards use a compressed hierarchy where the bold product name sits very close in weight and size to the descriptor line beneath it, weakening tier separation.
  visible_tells:
  - "Product name ('Ready', 'Go Long') is bold but only marginally larger than its descriptor line"
  - "Small pill badges ('Popular', 'End-to-End') sit close in scale to the name, softening badge-vs-name contrast"
  confidence: medium
  contrast_with: store/rugiet-com/captures/2026-06-07/tiles/ed-ready/tile-12-y14640.png
- id: typography_06
  family: typography_hierarchy
  polarity: mixed
  page_or_region: homepage — testimonial carousel with editorial type tiles
  tile_path: store/rugiet-com/captures/2026-06-07/tiles/homepage/tile-05-y06100.png
  claim: The carousel sets editorial words ('TAKE CONTROL', 'MIND AND MUSCLE') at the same display scale as quoted patient text, so at a glance it is unclear which tile is a slogan and which is a testimonial.
  visible_tells:
  - "Orange tile renders the quote 'WE ARE TRULY HAVING SOME OF THE BEST SEX...' at a scale comparable to the slogan word 'CONTROL' on the adjacent tile"
  - No consistent size relationship distinguishes the editorial-word tiles from the review-quote tiles
  confidence: medium
- id: typography_07
  family: typography_hierarchy
  polarity: mixed
  page_or_region: ed-ready — left-edge scrolling claim captions
  tile_path: store/rugiet-com/captures/2026-06-07/tiles/ed-ready/tile-01-y01220.png
  claim: Left-edge claims ('3-in-1 ED med with up to 3x the power of generics') float at a single bold weight with no supporting subtext or size step, so each caption reads as an isolated label rather than part of a flowing hierarchy.
  visible_tells:
  - Bold claim text floats at left with no sub-label and no body copy beneath it
  - "The next caption ('Primes the brain for arousal, boosts blood flow') gets the identical monotone treatment"
  confidence: medium
  contrast_with: store/rugiet-com/captures/2026-06-07/tiles/ed-ready/tile-02-y02440.png
- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: homepage — four-column product card grid
  tile_path: store/rugiet-com/captures/2026-06-07/tiles/homepage/tile-01-y01220.png
  claim: Four product cards sit in a strict equal-width grid with even gutters, matched image bands, and aligned dual-CTA rows pinned to the card foot — no card breaks the baseline.
  visible_tells:
  - Four cards of identical width with equal gutters between them
  - Product pill render occupies the same vertical band in each card
  - Two-button row (GET STARTED / Learn More) aligns at the bottom across all four
  confidence: high
  contrast_with: store/rugiet-com/captures/2026-06-07/tiles/ed-ready/tile-12-y14640.png
- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: ed-ready — 'You may also like' cross-sell grid
  tile_path: store/rugiet-com/captures/2026-06-07/tiles/ed-ready/tile-12-y14640.png
  claim: The four-column cross-sell grid reuses the exact homepage card component — same tag-pill position, heading style, centered product render, and dual-CTA footer — showing a disciplined reusable component across pages.
  visible_tells:
  - "Tag pills ('Popular / 2-in-1 PE', '2-in-1 ED', 'Testosterone / Labs Required', 'Sleep') sit at a consistent top-left slot in every card"
  - Dual CTA buttons at the card foot match the homepage grid's sizing and labels
  - Column gutters are equal and card heights uniform
  confidence: high
- id: layout_03
  family: layout_composition_components
  polarity: strong
  page_or_region: reviews page — review card grid
  tile_path: store/rugiet-com/captures/2026-06-07/tiles/reviews/tile-00-y00000.png
  claim: The reviews page runs a four-column card grid with a fixed internal anatomy — stars top-left, all-caps headline, body copy, 'VERIFIED PATIENT' foot stamp — repeated across all eight visible cards with no outliers.
  visible_tells:
  - Orange star rows hold a consistent top-left position across every card
  - All-caps headline sits in the same slot directly below the stars
  - "'VERIFIED PATIENT' anchors the foot of each card in identical placement"
  confidence: high
- id: layout_04
  family: layout_composition_components
  polarity: strong
  page_or_region: ed-ready — RD-37 annotated 3D product diagram
  tile_path: store/rugiet-com/captures/2026-06-07/tiles/ed-ready/tile-06-y07320.png
  claim: The annotated diagram uses a clean leader-line system — thin white lines run from numbered pip anchors on the cube to frosted-grey callout boxes placed on opposite diagonals with no overlap or crowding.
  visible_tells:
  - Thin white leader lines terminate precisely at points on the cube surface
  - Two callout boxes sit on opposite corners, avoiding visual collision
  - Numbered orange pip icons anchor each box at consistent size
  confidence: high
  contrast_with: store/rugiet-com/captures/2026-06-07/tiles/ed-ready/tile-01-y01220.png
- id: layout_05
  family: layout_composition_components
  polarity: strong
  page_or_region: ed-ready — stat bar above the onset chart
  tile_path: store/rugiet-com/captures/2026-06-07/tiles/ed-ready/tile-05-y06100.png
  claim: Four stats ('85%', '80%', '10M+', '36 HRS') read as a structured data row — equal-width blocks with baseline-aligned labels — sharing left/right margins with the chart below to maintain grid continuity.
  visible_tells:
  - Four stat blocks occupy visually equal horizontal zones with matching label treatment
  - Big-number / small-label pairing is consistent across all four
  - Margins carry straight down into the onset chart beneath
  confidence: high
- id: layout_06
  family: layout_composition_components
  polarity: strong
  page_or_region: footer — multi-column link grid
  tile_path: store/rugiet-com/captures/2026-06-07/tiles/ed-ready/tile-13-y15490.png
  claim: The footer is a fully-populated multi-column link grid with even inter-column spacing, an oversized brand glyph at far left, and a horizontal rule separating the legal strip below — a clean, complete structure.
  visible_tells:
  - Link columns (All Treatments, Get Started, Blog, social, app) are evenly spaced with top-aligned bold headings
  - App store badges sit in their own column at the right with no overflow
  - A horizontal rule cleanly separates the main footer from the legal/contact strip
  confidence: high
- id: layout_07
  family: layout_composition_components
  polarity: strong
  page_or_region: homepage — three-step process strip + section whitespace
  tile_path: store/rugiet-com/captures/2026-06-07/tiles/homepage/tile-03-y03660.png
  claim: The process strip ('Complete a health assessment', 'Doctor review', 'Medication ships') runs as a tidy three-column icon-text row with generous vertical padding around it — whitespace is used to punctuate sections, not just pad.
  visible_tells:
  - Three equal columns each with a small icon, label, and descriptor
  - Clear vertical gaps separate the strip from the full-bleed photo above and content below
  - Left edges of all three items align to a shared column gutter
  confidence: high
- id: layout_08
  family: layout_composition_components
  polarity: mixed
  page_or_region: ed-ready — 'Feel the difference' comparison table
  tile_path: store/rugiet-com/captures/2026-06-07/tiles/ed-ready/tile-08-y09760.png
  claim: The comparison table shows only the brand column of checks with no competitor column header or marks — structurally functional but truncated, reading as a one-sided checklist rather than a true comparison.
  visible_tells:
  - Only one icon column header (the brand) appears above a single column of checkmarks
  - Row labels are left-aligned but there is no second column showing competitor absence
  - A 'Qualify Now' CTA is embedded inside the table border, blurring the component boundary
  confidence: medium
- id: layout_09
  family: layout_composition_components
  polarity: mixed
  page_or_region: homepage — 'Your goals, our treatments' category grid
  tile_path: store/rugiet-com/captures/2026-06-07/tiles/homepage/tile-05-y06100.png
  claim: The treatment-category thumbnail row reads as equal-width image tiles, but the rightmost tile is visibly cropped at the container edge, signalling a horizontally-scrolling track rather than a count that divides cleanly into the column.
  visible_tells:
  - Six thumbnail tiles with label overlays sit in a row of equal-width images
  - The rightmost tile is cut off at the right edge rather than ending flush
  confidence: medium
- id: layout_10
  family: layout_composition_components
  polarity: poor
  page_or_region: homepage — top nav bar over hero
  tile_path: store/rugiet-com/captures/2026-06-07/tiles/homepage/tile-00-y00000.png
  claim: The nav reads thin against the bold hero — plain small text links with only the 'All Treatments' pill differentiated, and no rule, shadow, or background anchoring the bar to the full-bleed image below.
  visible_tells:
  - "Nav links ('Sex', 'Testosterone', 'Sleep', 'Weight') are small with no visible active-state treatment"
  - The boxed 'All Treatments' label is the only differentiated nav element
  - No horizontal rule or shadow separates the transparent nav from the hero image
  confidence: medium
- id: layout_11
  family: layout_composition_components
  polarity: poor
  page_or_region: reviews page — bottom stat-overlay image pair
  tile_path: store/rugiet-com/captures/2026-06-07/tiles/reviews/tile-04-y04880.png
  claim: The two stat-overlay photos at the page foot sit flush at noticeably different brightness with captions floating directly on the images and no shared container, reading as two separate editorial images rather than one designed component.
  visible_tells:
  - Left photo (couple, warm light) is markedly brighter than the right photo (man in a dark bedroom)
  - The two images sit flush edge-to-edge with no shared border, rounded corner, or bounding box unifying them
  - Stat captions float on each photo with no plate, so the pair reads as two separate editorial images rather than one component
  confidence: medium
- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: homepage hero — crimson-maroon field
  tile_path: store/rugiet-com/captures/2026-06-07/tiles/homepage/tile-00-y00000.png
  claim: The hero rests on a deliberate deep crimson-maroon field rather than black or an ambient photo tone, reading as an owned brand color behind the lit male subject.
  visible_tells:
  - Full-bleed background is a saturated dark red, not neutral black/grey
  - Headline and nav render white-on-maroon
  - Warm maroon recurs in the sex-page hero treatment
  confidence: high
- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: footer / site-wide — amber-orange accent
  tile_path: store/rugiet-com/captures/2026-06-07/tiles/ed-ready/tile-13-y15490.png
  claim: A single high-saturation amber-orange does triple duty as the full footer fill, the top promo-banner stripe, and the star-rating color — a disciplined one-color accent system with no competing bright hue.
  visible_tells:
  - Footer fills entirely with amber-orange on the ed-ready and homepage footer tiles
  - The same amber is the top banner stripe and the review-page star color
  - No second bright hue competes anywhere — the accent stays single-color
  confidence: high
  contrast_with: store/rugiet-com/captures/2026-06-07/tiles/reviews/tile-00-y00000.png
- id: color_03
  family: color_brand_imagery
  polarity: strong
  page_or_region: homepage / ed-ready — per-SKU pill color coding
  tile_path: store/rugiet-com/captures/2026-06-07/tiles/homepage/tile-01-y01220.png
  claim: Each product SKU is color-coded by a distinct pill hue — teal, mint, blush, gold — and the same hues carry across the homepage grid and the ed-ready cross-sell, functioning as consistent product identity.
  visible_tells:
  - Four homepage cards each show a different pill hue (teal square, mint disc, blush disc, gold oval) on identical dark backgrounds
  - Blush and grey discs reappear in the ed-ready 'You may also like' carousel
  - The teal cube reappears at full scale on the ed-ready product pages
  confidence: high
- id: color_04
  family: color_brand_imagery
  polarity: strong
  page_or_region: homepage — testimonial carousel amber accent break
  tile_path: store/rugiet-com/captures/2026-06-07/tiles/homepage/tile-05-y06100.png
  claim: The carousel drops a single solid amber-orange quote card among light, dark, and photo cards as an intentional color break, tying the row to the footer accent system rather than treating every tile alike.
  visible_tells:
  - One card background is solid amber-orange while flanking cards are light grey, photo, or dark
  - The amber card carries a white bold quote, matching the footer's hue-and-type pairing
  confidence: high
- id: color_05
  family: color_brand_imagery
  polarity: strong
  page_or_region: sex / homepage / ed-ready heroes — warm low-key intimacy photography
  tile_path: store/rugiet-com/captures/2026-06-07/tiles/sex/tile-00-y00000.png
  claim: Intimacy and portrait photography is consistently shot in warm, low-key studio light with tight crops and no lifestyle clutter, giving the image library a cohesive editorial voice rather than a stock look.
  visible_tells:
  - Sex-page hero shows an embracing couple in warm amber-bronze light, close crop, no background context
  - Homepage hero uses the same warm directional light on a single male subject
  - Ed-ready tile-04 and tile-08 repeat the tight-crop, warm-lit couple treatment
  confidence: high
- id: color_06
  family: color_brand_imagery
  polarity: mixed
  page_or_region: ed-ready — stock medical illustrations (x-ray body, blood cells, x-ray brain)
  tile_path: store/rugiet-com/captures/2026-06-07/tiles/ed-ready/tile-02-y02440.png
  claim: The x-ray body silhouette, red blood-cell macro, and lateral x-ray brain read as generic stock medical renders — none carry the warm brand treatment or embossed mark — breaking the otherwise proprietary image language used for the product cube.
  visible_tells:
  - X-ray full-body figure with blue-white organ glow is the category-generic medical stock style
  - Red blood-cell close-up is standard microscopy stock with a saturated crimson that clashes with the cooler editorial palette
  - The x-ray skull-and-brain render (tile-09) is the same stock register, not custom art-direction
  confidence: high
  contrast_with: store/rugiet-com/captures/2026-06-07/tiles/ed-ready/tile-06-y07320.png
- id: color_07
  family: color_brand_imagery
  polarity: mixed
  page_or_region: ed-ready — 'Three medications' molecule-overlay cards
  tile_path: store/rugiet-com/captures/2026-06-07/tiles/ed-ready/tile-07-y08540.png
  claim: The three medication cards composite white wireframe molecules over greyscale photos — a competent device, but the backgrounds break parity (two body close-ups, one couple embrace) and the molecule line-art is generic clip-art that ignores the amber/teal accent system.
  visible_tells:
  - Sildenafil and Tadalafil cards use torso/body photography; Apomorphine uses a couple-embrace shot
  - Hexagonal ring-bond diagrams are identical white line art across all three — generic chemistry-clip-art treatment
  - No brand accent color appears in the overlays
  confidence: high
  contrast_with: store/rugiet-com/captures/2026-06-07/tiles/ed-ready/tile-06-y07320.png
- id: color_08
  family: color_brand_imagery
  polarity: mixed
  page_or_region: reviews page — light-mode break from the dark system
  tile_path: store/rugiet-com/captures/2026-06-07/tiles/reviews/tile-00-y00000.png
  claim: The reviews page abandons the dark editorial palette for a white background with flat light-grey cards, so it reads like a different design system from the dark content pages — only the orange banner and stars carry the brand through.
  visible_tells:
  - Page background is white where the home/PDP pages use black or dark charcoal
  - Review tiles are flat light grey against white with no amber or dark-mode framing
  - Only the top orange promo banner and the star ratings retain the brand accent
  confidence: high
  contrast_with: store/rugiet-com/captures/2026-06-07/tiles/homepage/tile-00-y00000.png
- id: color_09
  family: color_brand_imagery
  polarity: mixed
  page_or_region: testosterone page — hero photography register
  tile_path: store/rugiet-com/captures/2026-06-07/tiles/testosterone/tile-00-y00000.png
  claim: The testosterone hero (wet, shirtless, arms-up male on a cool near-black ground) is well-shot but sits in a fitness/sportswear register, distinct from the warm intimate-couple mood of the sex and homepage heroes — suggesting uneven photo briefs across pages.
  visible_tells:
  - Subject is backlit with wet skin and dramatic lighting — a fitness-ad convention
  - Background is cool near-black versus the warm maroon of the homepage hero
  confidence: medium
  contrast_with: store/rugiet-com/captures/2026-06-07/tiles/homepage/tile-00-y00000.png
- id: color_10
  family: color_brand_imagery
  polarity: poor
  page_or_region: homepage — 'Learn more, live healthier' article teaser row
  tile_path: store/rugiet-com/captures/2026-06-07/tiles/homepage/tile-09-y10980.png
  claim: The three blog teaser images share no visual treatment — a cold blurred intimacy shot, a plainly-lit man in a white tank, and a seated fitness figure — reading as unvetted pulls rather than curated brand imagery.
  visible_tells:
  - Left card is a heavily blurred motion photo with a cold cast
  - Center card is a flat, plainly-lit studio portrait inconsistent with the warm editorial heroes elsewhere
  - Right card uses a seated fitness format absent from the rest of the site
  confidence: medium
- id: iconography_01
  family: iconography_illustration
  polarity: strong
  page_or_region: homepage / ed-ready — pill renders as a per-SKU icon system
  tile_path: store/rugiet-com/captures/2026-06-07/tiles/ed-ready/tile-12-y14640.png
  claim: Every product is rendered as a studio-lit pill carrying the same embossed 'TR' mark, with shape vocabulary (square vs disc) and hue mapping to product line — a coherent render-as-icon system rather than ad-hoc photography.
  visible_tells:
  - Four pills (mint disc, blush disc, grey disc, lavender disc) each show the embossed TR mark at consistent scale on matching off-white grounds
  - The homepage grid shows the same render system including a distinct teal square for Ready
  - Lighting angle and ground are near-identical across SKUs and across pages
  confidence: high
  contrast_with: store/rugiet-com/captures/2026-06-07/tiles/homepage/tile-01-y01220.png
- id: iconography_02
  family: iconography_illustration
  polarity: strong
  page_or_region: ed-ready — high-fidelity 3D cube render
  tile_path: store/rugiet-com/captures/2026-06-07/tiles/ed-ready/tile-06-y07320.png
  claim: The teal Ready cube is rendered as a high-fidelity 3D object — studio specular, tonal depth on rounded edges, crisp embossed logo — and used as owned product imagery, a clear craft step above stock pharma photography.
  visible_tells:
  - Two angled cubes with photorealistic surface texture and specular highlight on the embossed mark
  - Material shine and edge tonality read as a deliberate 3D render, not a flat photo
  - Same render appears isolated on a neutral grey ground as the ed-ready product hero (tile-00)
  confidence: high
  contrast_with: store/rugiet-com/captures/2026-06-07/tiles/ed-ready/tile-02-y02440.png
- id: iconography_03
  family: iconography_illustration
  polarity: strong
  page_or_region: ed-ready — onset comparison line chart
  tile_path: store/rugiet-com/captures/2026-06-07/tiles/ed-ready/tile-05-y06100.png
  claim: The onset chart uses an amber area-fill curve against thin dashed comparator lines with labeled 'Minutes' and 'Effect' axes — competent, restrained data-viz that avoids chartjunk.
  visible_tells:
  - Amber-filled curve for the brand contrasted with thin dashed grey lines for sildenafil/tadalafil
  - X-axis labeled 'Minutes' with numeric ticks (5–30); Y-axis labeled 'Effect'
  - Small orange product marker sits at the curve peak as a legend cue
  confidence: high
  contrast_with: store/rugiet-com/captures/2026-06-07/tiles/ed-ready/tile-06-y07320.png
- id: iconography_04
  family: iconography_illustration
  polarity: strong
  page_or_region: footer / product pills — custom 'TR' logomark
  tile_path: store/rugiet-com/captures/2026-06-07/tiles/ed-ready/tile-13-y15490.png
  claim: The oversized 'TR' logomark — an upward-arrow stacked over an R — is a custom brand glyph, not a typeface character, and is deployed at every scale: huge in the footer, embossed on product pills, and as the nav mark.
  visible_tells:
  - Large black TR glyph on the amber footer shows the arrow-over-R construction at full resolution
  - The same mark appears embossed on the product pills and as the small nav mark
  - The arrow element is bespoke, not a standard unicode arrow
  confidence: high
- id: iconography_05
  family: iconography_illustration
  polarity: mixed
  page_or_region: homepage — process step icons
  tile_path: store/rugiet-com/captures/2026-06-07/tiles/homepage/tile-03-y03660.png
  claim: The three process-step icons are tiny and indistinct at this scale, reading as generic line glyphs whose craft cannot be assessed from the tile.
  visible_tells:
  - Three small icons sit beside the step labels at roughly micro scale
  - No distinctive style or weight is resolvable at the tile resolution
  confidence: low
```

## Provenance

Tiles read: homepage (11) + ed-ready (14) + sex (8) + testosterone (7) + reviews (6) from `captures/2026-06-07/tiles/` — all 46 active, no exclusions, no Tier-B re-render (the capture was clean: heroes, the 3D/medical renders, and the onset chart all rendered statically correct). Mined blind + judged per [`/visual-evidence`](../../skills/visual-evidence/SKILL.md): four family miners saw only the tiles (no dossier, no web), the judge pruned 16 of 46 raw cards — mostly cross-family merges to one-card-per-tell, plus one outright fact rejection (an ed-ready tile-10 "four B&W headshots" card that contradicted its tile — a single color physician portrait). Author spot-check of the `poor` structural cards against native tiles confirmed all three are genuine design, not capture artifacts; the `layout_11` caption-placement tell was corrected to match the tile. Snapshot caveat: reflects the 2026-06-07 capture; the live site changes.
