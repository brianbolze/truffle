---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.0"
domain: functionhealth.com
captured_at: 2026-06-16
source_capture: 2026-06-16
qa_status: recapture-used
---

## Visual & brand impression

Function reads as a controlled editorial health brand: one terracotta-rust accent on warm cream, held with discipline from the hero into data-heavy UI [color_01][color_05], plus a recurring two-font system that rust-italicizes the emphasis word of each headline [typography_02][color_04]. Hierarchy is clean where designed — heroes and the lab-test grid run distinct, legible tiers [typography_01][typography_03][typography_05] — and the components are genuinely repeatable: numbered step cards, the raised comparison column, matched MRI cards [layout_02][layout_03][layout_04]. Photography is cinematic and art-directed, extended to a near-black scans variant [color_02][color_03]. The weak points cluster in utility zones — a flattened, dense footer [typography_08][layout_09], an edge-clipped conditions ticker [layout_10], and assembled third-party imagery (press logos, advisory portraits, a low-fi user video) that breaks the warm register [color_08][color_09][color_10].

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: homepage hero
  tile_path: store/functionhealth-com/captures/2026-06-16/tiles/homepage/tile-00-y00000.png
  claim: The hero runs a clear three-level hierarchy — a tiny all-caps label ('HSA/FSA Eligible'), a large italic serif display headline ('Check your health.'), and a small sans descriptor — each level distinct in size, weight, and style, and white type stays legible over the dark portrait.
  visible_tells:
  - Italic serif headline 'Check your health.' at roughly 3x the body descriptor beneath it
  - Tiny uppercase 'HSA/FSA Eligible' label above the headline as a discrete third tier
  - White type reads cleanly over the dark-toned portrait photograph
  confidence: high
  contrast_with: store/functionhealth-com/captures/2026-06-16/tiles/homepage/tile-09-y10850.png
- id: typography_02
  family: typography_hierarchy
  polarity: strong
  page_or_region: homepage — section headlines throughout
  tile_path: store/functionhealth-com/captures/2026-06-16/tiles/homepage/tile-01-y01220.png
  claim: A recurring two-font headline system — roman serif for anchor words, italic serif in terracotta for the emphasis word — creates consistent, immediately readable contrast without relying on size alone.
  visible_tells:
  - '''Testing is easy'': ''Testing is'' in dark roman, ''easy'' in terracotta italic — same size, differentiated by style and color'
  - Pattern repeats in 'Monitor early indicators of 1000s of diseases' lower in the same tile
  confidence: high
- id: typography_03
  family: typography_hierarchy
  polarity: strong
  page_or_region: homepage — lab category grid
  tile_path: store/functionhealth-com/captures/2026-06-16/tiles/homepage/tile-02-y02440.png
  claim: 'The lab-test category section holds a tight four-level hierarchy: large section headline, medium serif category label, small terracotta count chip, and fine grey test-name body copy — each step legible and proportionally sized.'
  visible_tells:
  - Category labels ('Hormones & thyroid', 'Cancer & other silent risks') in medium-weight serif
  - Orange 'Biomarkers' count chips as a distinct tertiary level
  - Fine grey test names below as the clearly subordinate fourth level
  confidence: high
- id: typography_04
  family: typography_hierarchy
  polarity: strong
  page_or_region: pricing page — hero
  tile_path: store/functionhealth-com/captures/2026-06-16/tiles/pricing/tile-00-y00000.png
  claim: 'The pricing hero stacks three distinct levels cleanly: a large dark sans/serif primary line, a large terracotta italic serif emphasis phrase (''just $365 annually''), and a compact descriptor, with generous space before the CTA.'
  visible_tells:
  - '''Test twice a year for'' in large dark type'
  - '''just $365 annually'' immediately below in large terracotta italic — same line-height, differentiated by color and style'
  - Short descriptor paragraph below at noticeably smaller size
  confidence: high
- id: typography_05
  family: typography_hierarchy
  polarity: strong
  page_or_region: scans page — hero
  tile_path: store/functionhealth-com/captures/2026-06-16/tiles/scans/tile-00-y00000.png
  claim: On the near-black full-bleed hero, 'MRI & CT scans for early detection' stays legible in white serif at adequate size, with the italic 'for' carrying the same emphasis system seen sitewide and a small 'Function x ezra' co-brand label held at a clear subordinate scale.
  visible_tells:
  - Large white serif headline over the dark portrait, italic 'for' embedded mid-phrase
  - Small 'Function x ezra' co-brand lockup above the headline at subordinate scale
  confidence: high
- id: typography_06
  family: typography_hierarchy
  polarity: mixed
  page_or_region: homepage — comparison table
  tile_path: store/functionhealth-com/captures/2026-06-16/tiles/homepage/tile-05-y06100.png
  claim: The comparison-table headline ('Not your average checkup') uses the italic/roman split well, but the row labels and the two column headers below sit at near-identical sizes, flattening hierarchy at the detail level.
  visible_tells:
  - Section headline in italic terracotta 'Not your average' + roman black 'checkup' reads clearly
  - Row labels and the 'Standard checkup' / 'Function' column headers share roughly the same type size, differentiated mainly by the column fill, not by scale
  confidence: medium
- id: typography_07
  family: typography_hierarchy
  polarity: mixed
  page_or_region: pricing page — affordability argument section
  tile_path: store/functionhealth-com/captures/2026-06-16/tiles/pricing/tile-03-y03660.png
  claim: The section headline uses the italic serif system well, but the two explanatory panels below present body copy at one uniform small size with only a bold 'THE BOTTOM LINE' label for structure — the inner hierarchy is under-differentiated.
  visible_tells:
  - Headline 'The real question isn't whether you can afford Function — it's whether you can afford not to' uses the terracotta italic split
  - Below, the bullet lists and 'THE BOTTOM LINE' callouts sit at similar small body sizes with no prominent sub-heading scale
  confidence: medium
- id: typography_08
  family: typography_hierarchy
  polarity: poor
  page_or_region: homepage / pricing — footer
  tile_path: store/functionhealth-com/captures/2026-06-16/tiles/homepage/tile-09-y10850.png
  claim: The footer collapses column headings and link text to nearly the same size and weight — 'Company', 'Explore', 'Community' are barely distinguishable from the links beneath them; only the newsletter headline ('Subscribe and get 9 health guides') steps up in scale.
  visible_tells:
  - Footer column headers and link items appear at the same size and weight, separated only by spacing
  - Within the link columns there is essentially zero size or weight differentiation between heading and links
  confidence: high
  contrast_with: store/functionhealth-com/captures/2026-06-16/tiles/homepage/tile-02-y02440.png
- id: typography_09
  family: typography_hierarchy
  polarity: poor
  page_or_region: homepage — doctor/advisory board grid
  tile_path: store/functionhealth-com/captures/2026-06-16/tiles/homepage/tile-07-y08540.png
  claim: Each portrait's name and credential line sit at nearly identical small sizes with only light weight variation, so individual names don't scan — weakening the credibility the section is built to convey.
  visible_tells:
  - Name (e.g. 'JoAnn E. Manson, M.D., MPH, DrPH') and the credential line below it share the same tight size range
  - No step-up in size or weight between name and title; only a slightly darker name treatment separates them
  confidence: medium
- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: homepage — hero
  tile_path: store/functionhealth-com/captures/2026-06-16/tiles/homepage/tile-00-y00000.png
  claim: The hero uses deliberate asymmetry — full-bleed portrait filling the frame, headline anchored bottom-left, and three stat callouts pinned as a horizontal strip bottom-right — balancing weight without a symmetric grid.
  visible_tells:
  - Full-bleed portrait occupies the frame with the subject weighted right
  - Headline and CTA sit bottom-left over the image
  - Three stats (160+ lab tests / Whole body / $1 per day) form a compact horizontal strip bottom-right rather than a stack
  confidence: high
- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: homepage — 'Testing is easy' three-step cards
  tile_path: store/functionhealth-com/captures/2026-06-16/tiles/pricing/tile-04-y04880.png
  claim: The three numbered step cards form an equal-width three-column grid with identical corner radius, background tone, and internal padding, top-aligned step numbers (01/02/03), and a distinct embedded UI mockup per card — a repeatable card system, not one-off boxes.
  visible_tells:
  - Cards share identical corner radius, cream-tint background, and internal top-padding
  - Step numbers 01/02/03 typeset in the same terracotta weight and position across all three
  - Each card holds a distinct but equally-weighted UI artifact (calendar picker, range chart, recommendation list)
  confidence: high
- id: layout_03
  family: layout_composition_components
  polarity: strong
  page_or_region: pricing — comparison table
  tile_path: store/functionhealth-com/captures/2026-06-16/tiles/pricing/tile-01-y01220.png
  claim: The comparison table anchors its product column with a raised, terracotta-tinted card that extends above and below the row grid, while filled-check vs. outlined-X icons keep the columns legible — a structurally competent component that avoids the flat-table problem.
  visible_tells:
  - Function column rendered as a raised terracotta card extending above the table rows
  - Filled check-circles (Function) vs. outlined X-circles (Standard checkup) make column hierarchy readable at a glance
  - Row dividers are hairline-thin and consistent
  confidence: high
- id: layout_04
  family: layout_composition_components
  polarity: strong
  page_or_region: scans — MRI/CT pricing cards
  tile_path: store/functionhealth-com/captures/2026-06-16/tiles/scans/tile-02-y02440.png
  claim: The three MRI pricing cards hold strict internal structure — title, description, crossed-out price above member price, two stacked CTAs, time field, checklist — in matching vertical rhythm across all three columns with no visible alignment drift.
  visible_tells:
  - Crossed-out non-member price ($999/$1699/$3999) sits above the member price in the same position in each card
  - Two CTAs ('Join Function to book' filled + 'Book directly with Ezra' outlined) stack identically across cards
  - Checklist items share left-alignment and icon style across all columns
  confidence: high
- id: layout_05
  family: layout_composition_components
  polarity: strong
  page_or_region: scans — 'Don't wait for symptoms' split layout
  tile_path: store/functionhealth-com/captures/2026-06-16/tiles/scans/tile-01-y01220.png
  claim: 'The two-column split (annotated body image left, structured copy right) is cleanly aligned: the text column top matches the image-card top, and three feature bullets (Safe / Fast / Powerful) hold uniform left-indent and leading.'
  visible_tells:
  - Image card and text block share a common top baseline
  - Three feature bullets (Safe / Fast / Powerful) use uniform left-indent and matching icon style
  - Body copy and CTA sit in even vertical rhythm beside the image
  confidence: high
- id: layout_06
  family: layout_composition_components
  polarity: mixed
  page_or_region: homepage — social proof / press grid
  tile_path: store/functionhealth-com/captures/2026-06-16/tiles/homepage/tile-03-y03660.png
  claim: The social-proof band mixes portrait testimonial cards of varying crop ratios with press-logo lockups (TIME 100, Fast Company, LinkedIn) at a different aspect ratio in the same row, producing uneven card heights that undercut the grid discipline seen elsewhere.
  visible_tells:
  - Portrait testimonial cards appear at different crop ratios (some tight, some wider)
  - Press-logo cards sit in the same band as portrait photos but at a clearly different aspect ratio
  - The row reads as loosely assembled rather than a designed grid
  confidence: medium
  contrast_with: store/functionhealth-com/captures/2026-06-16/tiles/scans/tile-02-y02440.png
- id: layout_07
  family: layout_composition_components
  polarity: mixed
  page_or_region: pricing — two-column cost-justification panels
  tile_path: store/functionhealth-com/captures/2026-06-16/tiles/pricing/tile-03-y03660.png
  claim: The two inset panels ('Many illnesses…' / 'Illness is expensive…') have unequal content density — the left runs longer — with no device to equalize them, so the cards end at different vertical points despite a shared boundary.
  visible_tells:
  - Left panel carries header, subhead, bullet list, and a shaded 'PREVENTIVE CARE MATTERS' callout
  - Right panel has a header and shorter bullet list with a 'THE BOTTOM LINE' callout, ending higher than the left
  - The two cards terminate at different vertical points
  confidence: medium
- id: layout_08
  family: layout_composition_components
  polarity: mixed
  page_or_region: homepage — lab category listing
  tile_path: store/functionhealth-com/captures/2026-06-16/tiles/homepage/tile-02-y02440.png
  claim: The lab-category columns share consistent heading and list format, but a distinctly styled terracotta '+More / All-in-one' card in the bottom-right breaks the column grid by occupying a visually heavier block that draws asymmetric attention.
  visible_tells:
  - Multiple text columns share consistent heading size and sub-item list format
  - Bottom-right holds a filled coral '+More / All-in-one lab testing' card that does not align to the same column width
  - The card interrupts the cadence of the column scan
  confidence: medium
- id: layout_09
  family: layout_composition_components
  polarity: poor
  page_or_region: homepage / pricing — footer
  tile_path: store/functionhealth-com/captures/2026-06-16/tiles/homepage/tile-09-y10850.png
  claim: The footer is dense and under-separated — a small multi-column link directory, QR code, app-store badges, social icons, newsletter form, and several paragraphs of fine-print legal text packed with inadequate spacing or dividers to navigate the sections.
  visible_tells:
  - Legal disclaimer spans the full footer width in multiple dense paragraphs at very small size
  - Link columns, app-badge row, and legal block are not separated by whitespace or dividers
  - QR code and newsletter form compete in the same band without clear priority
  confidence: high
  contrast_with: store/functionhealth-com/captures/2026-06-16/tiles/homepage/tile-00-y00000.png
- id: layout_10
  family: layout_composition_components
  polarity: poor
  page_or_region: homepage — scrolling conditions ticker
  tile_path: store/functionhealth-com/captures/2026-06-16/tiles/homepage/tile-02-y02440.png
  claim: The horizontal conditions ticker at the top of the tile is clipped mid-word at both viewport edges with no fade mask or containing frame, reading as unfinished rather than designed.
  visible_tells:
  - Condition names are abruptly cut at the left and right edges with no fade or mask
  - No containing background or separator distinguishes the ticker from the content below it
  confidence: medium
- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: homepage hero
  tile_path: store/functionhealth-com/captures/2026-06-16/tiles/homepage/tile-00-y00000.png
  claim: 'The palette is tightly controlled from the first pixel: a single terracotta-rust accent (promo banner, ''Start testing'' CTA) against a warm off-white field, with no competing hues in the hero.'
  visible_tells:
  - Rust banner strip at top matches the 'Start testing' pill button color
  - No second accent hue appears anywhere in the hero
  - Field color is warm cream, not pure white — consistent across subsequent tiles
  confidence: high
- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: homepage hero
  tile_path: store/functionhealth-com/captures/2026-06-16/tiles/homepage/tile-00-y00000.png
  claim: The hero photograph is cinematic and art-directed — warm golden side-lighting on a profile against an arid rocky landscape — tonally matched to the ochre-brown palette, clearly shot for the brand rather than generic wellness stock.
  visible_tells:
  - Low-key directional light sculpts the face in warm earthy tones
  - Outdoor rocky terrain background sits in the brand's ochre-brown range
  - Contemplative profile framing reads as purposeful art direction, not stock
  confidence: high
  contrast_with: store/functionhealth-com/captures/2026-06-16/tiles/homepage/tile-07-y08540.png
- id: color_03
  family: color_brand_imagery
  polarity: strong
  page_or_region: scans page hero
  tile_path: store/functionhealth-com/captures/2026-06-16/tiles/scans/tile-00-y00000.png
  claim: The scans hero carries the same warm-skin-on-dark-field art direction as the homepage but on a near-black ground, adding glowing terracotta orbital rings around the figure — showing the visual system extends deliberately across product verticals.
  visible_tells:
  - Near-black background (distinct from the cream body pages) isolates the warm-lit face
  - Rust orbital rings drawn over the figure match the CTA button color used sitewide
  - Warm side-lighting on the subject is consistent with homepage hero photography
  confidence: high
  contrast_with: store/functionhealth-com/captures/2026-06-16/tiles/homepage/tile-00-y00000.png
- id: color_04
  family: color_brand_imagery
  polarity: strong
  page_or_region: homepage — recurring italic-accent headline pattern
  tile_path: store/functionhealth-com/captures/2026-06-16/tiles/homepage/tile-01-y01220.png
  claim: A recurring color-plus-style signal — rust italic for the loaded word in each headline — is applied consistently across section headings, functioning as a controlled brand gesture rather than ad hoc decoration.
  visible_tells:
  - '''easy'' in ''Testing is easy'' is rust italic'
  - The same rust italic recurs on 'diseases', 'top doctors', 'for health', 'short?', and 'baseline' across subsequent tiles
  confidence: high
  contrast_with: store/functionhealth-com/captures/2026-06-16/tiles/homepage/tile-05-y06100.png
- id: color_05
  family: color_brand_imagery
  polarity: strong
  page_or_region: homepage — comparison table
  tile_path: store/functionhealth-com/captures/2026-06-16/tiles/homepage/tile-05-y06100.png
  claim: The branded column uses the rust accent as a column-highlight fill while the competitor column stays neutral grey — strict one-accent discipline held even in a data-heavy UI context.
  visible_tells:
  - Function's column is filled terracotta; the 'Standard checkup' column is neutral
  - No second accent color is introduced in the table
  - Checkmarks in the Function column use the same rust icon color
  confidence: high
- id: color_06
  family: color_brand_imagery
  polarity: strong
  page_or_region: scans page — body photography
  tile_path: store/functionhealth-com/captures/2026-06-16/tiles/scans/tile-01-y01220.png
  claim: The back-of-body scan photograph is graded to the same warm cinematic standard as the homepage hero — skin tones, light direction, and the rust spot-annotation overlays all sit in the rust-cream palette on a warm off-white ground.
  visible_tells:
  - Warm side-light on the bare back yields skin tones in the brand's ochre-amber range
  - Spot-annotation labels (Neck, Spine, Pelvis) and their connecting rings are drawn in the rust accent
  - Background is warm off-white, not clinical white
  confidence: high
- id: color_07
  family: color_brand_imagery
  polarity: strong
  page_or_region: pricing page — hero
  tile_path: store/functionhealth-com/captures/2026-06-16/tiles/pricing/tile-00-y00000.png
  claim: The pricing hero's hand-holding-phone product shot keeps the same warm golden grading and cream field as the homepage — confirming the photography standard extends to a commerce-focused page with no new hues introduced.
  visible_tells:
  - Phone/hand image is warm-toned with amber ambient light
  - Background beige-cream matches the site's standard field color
  - No additional hues despite the page being commerce-focused
  confidence: high
- id: color_08
  family: color_brand_imagery
  polarity: mixed
  page_or_region: homepage — social proof / testimonial image mix
  tile_path: store/functionhealth-com/captures/2026-06-16/tiles/homepage/tile-03-y03660.png
  claim: The social-proof grid mixes art-directed portrait photography with press logos on plain white and an editorial cover on a yellow ground, producing an uneven image register and small tonal breaks against the warm-cream field within one scroll section.
  visible_tells:
  - Three portraits are lit and cropped consistently (editorial, neutral backgrounds)
  - A yellow-background publication cover ('Global Daily Self-Care') clashes with the warm-cream palette
  - Press logos sit on plain white, not the site's cream, creating visible tonal breaks
  confidence: medium
  contrast_with: store/functionhealth-com/captures/2026-06-16/tiles/homepage/tile-00-y00000.png
- id: color_09
  family: color_brand_imagery
  polarity: mixed
  page_or_region: homepage — doctor portrait grid
  tile_path: store/functionhealth-com/captures/2026-06-16/tiles/homepage/tile-07-y08540.png
  claim: The advisory-board portraits are cropped consistently but are supplied images, not a unified shoot — backgrounds, lighting setups, and color temperatures vary noticeably across the eight headshots and break from the site's warm palette.
  visible_tells:
  - Multiple different background colors/contexts across the portraits (grey, white, blurred office, outdoor)
  - Lighting warmth differs — some subjects cool-lit, others warm-lit
  - Consistent crop partly compensates, but tone variation reads as assembled, not commissioned
  confidence: high
  contrast_with: store/functionhealth-com/captures/2026-06-16/tiles/homepage/tile-00-y00000.png
- id: color_10
  family: color_brand_imagery
  polarity: mixed
  page_or_region: scans page — patient video testimonial
  tile_path: store/functionhealth-com/captures/2026-06-16/tiles/scans/tile-06-y07320.png
  claim: The 'Long Live Holly' video thumbnail is a candid, flatly-lit user frame that breaks from the site's controlled warm photography — cooler, greyer color temperature and lower production value, visible next to the structured editorial copy.
  visible_tells:
  - Frame shows a smiling woman in flat ambient light, not a brand photoshoot
  - Color temperature is cooler and greyer than other photography on the page
  - Quality gap is immediately visible beside the editorial copy block
  confidence: high
  contrast_with: store/functionhealth-com/captures/2026-06-16/tiles/scans/tile-00-y00000.png
- id: color_11
  family: color_brand_imagery
  polarity: poor
  page_or_region: homepage — US map / bar-chart data graphics
  tile_path: store/functionhealth-com/captures/2026-06-16/tiles/homepage/tile-05-y06100.png
  claim: The US dot-map and the adjacent bar chart use rust tones that drift from the main accent — the map a lighter/pinker rust, the bars an orange-brown — neither precisely color-matched to the CTA swatch, and the drift is visible in one frame.
  visible_tells:
  - Dot-map fill is a lighter, pinker rust versus the deeper terracotta CTA
  - Bar-chart bars read orange-brown, distinct from the red-brown rust used elsewhere
  - Both graphics sit side by side, making the tonal drift visible at once
  confidence: medium
  contrast_with: store/functionhealth-com/captures/2026-06-16/tiles/homepage/tile-01-y01220.png
- id: iconography_01
  family: iconography_illustration
  polarity: strong
  page_or_region: homepage — 'Testing is easy' step-card UI mockups
  tile_path: store/functionhealth-com/captures/2026-06-16/tiles/pricing/tile-04-y04880.png
  claim: The three UI mockups inside the process cards are purpose-built product illustrations — a calendar/time picker, a labeled range chart ('ABOVE RANGE / IN RANGE / BELOW RANGE' with plotted points), and a recommendation list with custom icon badges — all in the warm palette, sharing the surrounding UI's radius and stroke weight, not stock components.
  visible_tells:
  - Card 02 shows a line chart with labeled range bands and plotted data points in rust
  - Card 03 shows three list items (Foods, Supplements, Daily health) each with a small rounded terracotta icon badge
  - All three illustrations share corner radius, background tint, and stroke weight with the surrounding UI
  confidence: high
- id: iconography_02
  family: iconography_illustration
  polarity: strong
  page_or_region: scans page — hero orbital rings
  tile_path: store/functionhealth-com/captures/2026-06-16/tiles/scans/tile-00-y00000.png
  claim: The hero uses a bespoke motion-graphic device — concentric terracotta elliptical rings orbiting the figure's head — that reads as custom composited illustration, not a stock graphic or photographic element.
  visible_tells:
  - Several sweeping elliptical rust arcs drawn around the model's head, clearly composited rather than photographed
  - Ring strokes match the exact brand color used on buttons and chart lines
  - Asymmetric arcs suggest movement rather than a simple decorative frame
  confidence: high
- id: iconography_03
  family: iconography_illustration
  polarity: strong
  page_or_region: scans page — location map
  tile_path: store/functionhealth-com/captures/2026-06-16/tiles/scans/tile-04-y04880.png
  claim: The US location map is a custom dot-matrix illustration in brand terracotta on cream — no state borders, labels, or standard cartographic conventions — reading as an illustrative silhouette rather than a generic choropleth or third-party embed.
  visible_tells:
  - Map rendered entirely as a uniform rust dot-grid on cream
  - No state borders, labels, or map chrome — purely illustrative form
  - Dot scale is consistent with other typographic elements on the page
  confidence: high
  contrast_with: store/functionhealth-com/captures/2026-06-16/tiles/homepage/tile-05-y06100.png
- id: iconography_04
  family: iconography_illustration
  polarity: mixed
  page_or_region: homepage — '75M+ results' bar chart
  tile_path: store/functionhealth-com/captures/2026-06-16/tiles/homepage/tile-05-y06100.png
  claim: The bar chart beside the '75M+' stat is brand-colored but carries no axis, scale markers, or data annotation — it reads as decorative rather than an actual data visualization.
  visible_tells:
  - Ascending terracotta bars with no Y-axis, tick marks, or values
  - No chart title or source label
  - Bars read as pure illustration rather than a rendered chart
  confidence: high
  contrast_with: store/functionhealth-com/captures/2026-06-16/tiles/pricing/tile-04-y04880.png
- id: iconography_05
  family: iconography_illustration
  polarity: mixed
  page_or_region: scans page — CT scan organ icons
  tile_path: store/functionhealth-com/captures/2026-06-16/tiles/scans/tile-03-y03660.png
  claim: The heart and lungs icons heading the CT cards are small terracotta anatomical outlines — consistent with each other but simplified, clip-art-adjacent line work that doesn't demonstrate illustration craft beyond basics.
  visible_tells:
  - Heart icon in the card header is a small anatomical outline in terracotta, generic form
  - Lungs icon is similarly sized and style-matched but not visually complex
  - Both consistent with each other yet only basic line work
  confidence: medium
  contrast_with: store/functionhealth-com/captures/2026-06-16/tiles/scans/tile-00-y00000.png
- id: iconography_06
  family: iconography_illustration
  polarity: mixed
  page_or_region: homepage / pricing — comparison table icons
  tile_path: store/functionhealth-com/captures/2026-06-16/tiles/pricing/tile-01-y01220.png
  claim: The comparison table uses two icon types — a solid terracotta check-circle for the brand column and an outlined X-circle for the competitor — functionally clear and on-brand but standard UI icon primitives, not custom iconography, repeated unchanged across every row.
  visible_tells:
  - Check-circles are filled terracotta matching the column header
  - Competitor column uses a conventional outlined circle-with-X denial glyph
  - Same two glyphs repeat across all rows with no variation
  confidence: high
```

## Provenance

Tiles read: all three pages were **Tier-B browser re-renders** (`scripts/shoot.py`, system Chrome with real WebGL + warm-scroll lazy-load + motion settle), captured today and tiled to native resolution:
- `store/functionhealth-com/captures/2026-06-16/tiles/homepage/` (10 tiles)
- `store/functionhealth-com/captures/2026-06-16/tiles/pricing/` (7 tiles)
- `store/functionhealth-com/captures/2026-06-16/tiles/scans/` (8 tiles)

QA note: `qa_status: recapture-used`. The cached 2026-06-01 Firecrawl Tier-A renders were contaminated — a flat grey WebGL homepage hero and black/blank lazy-loaded media cards — so all three pages were re-rendered in a real browser rather than mined from the cached payloads. No tiles were excluded from the active set; every cited tile is a clean Tier-B render. The dark scans and MRI/CT heroes are intentional art direction (near-black grounds with warm-lit portraits), not capture failures.

Snapshot caveat: this is a point-in-time visual read of the cited 2026-06-16 tiles; later site changes are not reflected here.
