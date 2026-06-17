---
schema_version: "1.0"
domain: marekhealth.com
captured_at: 2026-06-17
source_capture: 2026-06-04
qa_status: clean
---

## Visual & brand impression

Marek's homepage is a confident, tightly governed dark-mode system: a repeated eyebrow/headline/body stack [typography_03], stats and feature cards with clean internal hierarchy [typography_02][typography_04], and a single red-orange accent held with real discipline across CTAs and bullet badges [color_01][color_03][iconography_02]. Photography is art-directed studio work [color_02] and the in-card product UI is bespoke, not stock [iconography_03]. But the system doesn't survive past the flagship. About swaps in spaced all-caps headings, daylight stock photos, and clip-art icons [typography_08][color_07][iconography_04]; the testosterone page drops unstyled white boxes and off-brand green data accents [color_08][color_05]; Diagnostics is a separate light-mode identity [color_06]; a one-off red paint-splash sits on an outlier white card [color_09]. Polished flagship, inconsistent sub-properties.

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: homepage hero
  tile_path: store/marekhealth-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png
  claim: The hero headline uses a confident multi-level hierarchy and a controlled mixed-weight accent technique — white display copy with the emphasis word 'results.' flipped to orange-red — with body copy set clearly subordinate beneath. This same white-plus-accent technique recurs in later section headings, so it reads as a deliberate system, not a one-off.
  visible_tells:
  - Display-size 'We turn your data into' in white, then oversized orange-red 'results.' on its own line
  - Body paragraph below sits at a legibly smaller size with reduced contrast
  - The same white-then-accent split reappears on the comparison-section heading ('Know exactly what you're investing -') and 'The pros trust Marek.'
  confidence: high
- id: typography_02
  family: typography_hierarchy
  polarity: strong
  page_or_region: homepage — stats row
  tile_path: store/marekhealth-com/captures/2026-06-04/tiles/homepage/tile-01-y01220.png
  claim: Numeric stats ('130+', '1,000+', '500+') are set dramatically larger than their grey descriptor labels, producing a scannable three-cell rhythm that stands on its own as a skim layer.
  visible_tells:
  - Bold white numerals roughly 4-5x the size of the grey label lines beneath them
  - Label text ('Foundational biomarkers', etc.) in clearly reduced size and weight
  confidence: high
- id: typography_03
  family: typography_hierarchy
  polarity: strong
  page_or_region: homepage — section intros (eyebrow system)
  tile_path: store/marekhealth-com/captures/2026-06-04/tiles/homepage/tile-01-y01220.png
  claim: A small eyebrow label with a tiny circular glyph precedes each display heading, establishing a consistent eyebrow / headline / body three-level stack repeated across the homepage.
  visible_tells:
  - Caption-scale 'The process' eyebrow above the large heading 'Four steps. No waiting rooms.'
  - Same eyebrow pattern repeats on 'Backed by the best' → 'The pros trust Marek.' and 'FAQs' → 'Frequently asked questions.'
  confidence: high
  contrast_with: store/marekhealth-com/captures/2026-06-04/tiles/about/tile-00-y00000.png
- id: typography_04
  family: typography_hierarchy
  polarity: strong
  page_or_region: homepage — feature card grid
  tile_path: store/marekhealth-com/captures/2026-06-04/tiles/homepage/tile-01-y01220.png
  claim: Within each feature card the title is set noticeably heavier and larger than its supporting description, preserving internal hierarchy at small card scale.
  visible_tells:
  - '''One panel to start. Thousands of markers to build from.'' in semi-bold'
  - Supporting body copy beneath it visibly smaller and lighter
  confidence: high
- id: typography_05
  family: typography_hierarchy
  polarity: mixed
  page_or_region: homepage — pricing cards
  tile_path: store/marekhealth-com/captures/2026-06-04/tiles/homepage/tile-05-y06100.png
  claim: Pricing-card hierarchy is competent but the eyebrow labels are set in very small grey all-caps that disappear at a glance, and the bold price floated top-right competes with the card title for the eye, fragmenting reading order.
  visible_tells:
  - '''DISCOVERY CALL'' / ''GUIDED OPTIMIZATION'' in tiny grey all-caps above the card title'
  - Bold '$0' and '$299' float top-right, creating a second focal point against the card headline
  confidence: high
- id: typography_06
  family: typography_hierarchy
  polarity: strong
  page_or_region: homepage — testimonial pull quote
  tile_path: store/marekhealth-com/captures/2026-06-04/tiles/homepage/tile-06-y07320.png
  claim: The featured pull quote is set at display scale in italic with strong leading, clearly distinguished from its smaller attribution line and the secondary review cards, giving the social-proof section a natural reading hierarchy.
  visible_tells:
  - Italic display quote spans nearly full width across multiple lines
  - Attribution 'Sam · Verified Trustpilot client' set at roughly a quarter the size in normal weight
  confidence: high
- id: typography_07
  family: typography_hierarchy
  polarity: mixed
  page_or_region: testosterone page — hero
  tile_path: store/marekhealth-com/captures/2026-06-04/tiles/testosterone/tile-00-y00000.png
  claim: The testosterone hero headline ('What are the benefits of TRT?') is set well below homepage display scale, and the supporting copy on the dark ground is rendered in dim grey with noticeably reduced legibility.
  visible_tells:
  - Heading is moderate-sized, not display-scale, smaller than the homepage hero equivalent
  - Body copy on the dark background is dim grey, low contrast
  confidence: medium
  contrast_with: store/marekhealth-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png
- id: typography_08
  family: typography_hierarchy
  polarity: poor
  page_or_region: about page — hero
  tile_path: store/marekhealth-com/captures/2026-06-04/tiles/about/tile-00-y00000.png
  claim: The about page uses a different, less-polished typographic register than the main site — a spaced uppercase subhead and a heavy all-caps block heading stacked within one screen-height, both claiming prominence, with none of the homepage's eyebrow/headline/body system.
  visible_tells:
  - Spaced uppercase 'ABOUT MAREK HEALTH / PERFORMANCE. LONGEVITY. BALANCE.' over the photo
  - Immediately below, a large bold all-caps block 'MAREK IS A TELEHEALTH PLATFORM BUILT ON STREAMLINING HEALTH OPTIMIZATION.' — two competing heading treatments, no eyebrow
  confidence: high
  contrast_with: store/marekhealth-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png
- id: typography_09
  family: typography_hierarchy
  polarity: poor
  page_or_region: about page — lower body sections
  tile_path: store/marekhealth-com/captures/2026-06-04/tiles/about/tile-03-y03660.png
  claim: The about page mixes heading voices inconsistently across one page — spaced centered all-caps for 'OUR SPECIALTIES' but title-case for nearby section headings — indicating it was not typeset to the main site's system.
  visible_tells:
  - '''OUR SPECIALTIES'' in spaced all-caps, centered'
  - Adjacent headings 'We Work With The Best' and 'All To Say, Any Situation...' set in title case at varying weights — multiple distinct heading voices on one page
  confidence: high
- id: typography_10
  family: typography_hierarchy
  polarity: mixed
  page_or_region: diagnostics — shop listing
  tile_path: store/marekhealth-com/captures/2026-06-04/tiles/diagnostics_home/tile-04-y04880.png
  claim: The diagnostics shop listing uses a standard e-commerce type hierarchy, but the small-caps category labels sit close in visual weight to the product names directly above them, flattening the intended hierarchy.
  visible_tells:
  - '''KIDNEY HEALTH'' small-caps sits just under ''Comprehensive Metabolic Panel (CMP)'' with limited size separation'
  - Price text reads at roughly the same size as the product name
  confidence: medium
- id: typography_11
  family: typography_hierarchy
  polarity: strong
  page_or_region: diagnostics — 'Democratizing Precision Diagnostics'
  tile_path: store/marekhealth-com/captures/2026-06-04/tiles/diagnostics_home/tile-02-y02440.png
  claim: The section headline 'Democratizing Precision Diagnostics' applies the same single-word orange-red accent technique used on the main site, carrying brand typographic consistency into the diagnostics sub-property.
  visible_tells:
  - Large headline with the word 'Precision' in orange-red against the others in dark text
  - Smaller body paragraph clearly subordinate beneath it
  confidence: high
- id: typography_12
  family: typography_hierarchy
  polarity: poor
  page_or_region: testosterone page — 'Masculinity is in crisis' callout
  tile_path: store/marekhealth-com/captures/2026-06-04/tiles/testosterone/tile-02-y02440.png
  claim: The 'Masculinity is in crisis.' callout is set in a centered lighter-weight style on a white box, distinct from the surrounding dark-page sans type, reading as an unstyled stranded block rather than a deliberate accent.
  visible_tells:
  - Centered heading in a lighter weight/style than the surrounding page sections
  - No eyebrow or contextual label — the card reads as a typographic island on the dark page
  confidence: medium
- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: homepage hero
  tile_path: store/marekhealth-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png
  claim: The hero uses a disciplined two-column split — headline/CTA stack left, edge-bleeding model photo right — with confident negative space around the copy that prevents crowding.
  visible_tells:
  - Left text column terminates with deliberate breathing room, not packed to the fold
  - Right photo bleeds edge-to-edge without colliding with nav or headline alignment
  confidence: high
- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: homepage — four-step process cards
  tile_path: store/marekhealth-com/captures/2026-06-04/tiles/homepage/tile-02-y02440.png
  claim: The 2x2 process-card grid locks to a consistent internal structure — day badge top-left, oversized step ordinal top-right, headline + body, then a bespoke UI mockup — applied identically across all four cards.
  visible_tells:
  - Day/week badge and faint oversized ordinal number occupy the same corners in every card (01, 02, 03, 04)
  - Each card contains a distinct but card-width-inset UI mockup (scheduler, map, biomarker results, treatment plan)
  confidence: high
  contrast_with: store/marekhealth-com/captures/2026-06-04/tiles/about/tile-03-y03660.png
- id: layout_03
  family: layout_composition_components
  polarity: strong
  page_or_region: homepage — feature 2x2 grid
  tile_path: store/marekhealth-com/captures/2026-06-04/tiles/homepage/tile-01-y01220.png
  claim: The four feature cells inside a single rounded container hold uniform internal padding and a shared icon-size convention, composing as one unit rather than a loose list.
  visible_tells:
  - All four icon squares are the same size and margin from the card edge
  - A single container boundary wraps the full 2x2 block
  confidence: high
- id: layout_04
  family: layout_composition_components
  polarity: strong
  page_or_region: homepage — comparison table
  tile_path: store/marekhealth-com/captures/2026-06-04/tiles/homepage/tile-04-y04880.png
  claim: The competitor comparison table elevates the brand column with a distinct dark card and rounded border, consistent row heights and dividers, while the three competitor columns are visually de-emphasised with dashes for missing features.
  visible_tells:
  - Brand 'marek health' column sits in its own bordered card, separated from the greyed competitor columns
  - Competitor cells are mostly em-dashes; brand cells carry green checks and orange '130+' / '500+ therapies' highlights
  confidence: high
- id: layout_05
  family: layout_composition_components
  polarity: strong
  page_or_region: homepage — ambassador grid
  tile_path: store/marekhealth-com/captures/2026-06-04/tiles/homepage/tile-07-y08540.png
  claim: The 6-across, two-row ambassador grid is tightly controlled — equal-sized square portrait tokens, consistent name/title label treatment below each, zero gap variance across both rows.
  visible_tells:
  - All twelve portrait squares share the same width and corner radius
  - Name in the same weight/size beneath every portrait with the role line in a smaller muted weight
  confidence: high
- id: layout_06
  family: layout_composition_components
  polarity: mixed
  page_or_region: homepage — pricing cards
  tile_path: store/marekhealth-com/captures/2026-06-04/tiles/homepage/tile-05-y06100.png
  claim: The two pricing cards share a clean internal template (label, headline, price, copy, icon-bulleted list) but are badly unbalanced in fill — the left 'Free Consultation' card has three bullets and a large empty lower half while the right 'Marek Health Protocol' card runs seven-plus bullets, leaving the pair lopsided side by side.
  visible_tells:
  - Left card content ends high, leaving roughly the bottom 40% of the card empty
  - Right card is densely packed to the CTA with two bulleted sub-sections ('What's included', 'What comes next')
  confidence: high
- id: layout_07
  family: layout_composition_components
  polarity: mixed
  page_or_region: homepage — testimonial section
  tile_path: store/marekhealth-com/captures/2026-06-04/tiles/homepage/tile-06-y07320.png
  claim: The testimonial section is structurally sound but top-heavy — the oversized italic pull quote dominates the upper half while the three small review cards share the lower half, with little breathing room between them.
  visible_tells:
  - Pull quote occupies roughly the top 40% of the tile across multiple lines
  - Three review cards sit close beneath with no clear separator from the quote block
  confidence: medium
- id: layout_08
  family: layout_composition_components
  polarity: mixed
  page_or_region: testosterone page — statistics row
  tile_path: store/marekhealth-com/captures/2026-06-04/tiles/testosterone/tile-03-y03660.png
  claim: The three bottom stat cards break their own symmetry — the two left cards center a donut ring while the third substitutes a small US-map outline at a different scale, so the right card reads lighter than its siblings in an otherwise symmetric row.
  visible_tells:
  - 'Left two cards: donut graphic (70%, 35%) dominates the upper half; right card: small red US-map outline offset within the card'
  - All three share the same border and padding but the right card's content reads visually lighter
  confidence: high
- id: layout_09
  family: layout_composition_components
  polarity: mixed
  page_or_region: about page — alternating image/text sections
  tile_path: store/marekhealth-com/captures/2026-06-04/tiles/about/tile-02-y02440.png
  claim: The about page alternates image/text panels but without consistent column proportions — one split gives the photo roughly half the width, the adjacent split gives it a narrower slice — so the rhythm feels improvised rather than systematic.
  visible_tells:
  - 'Top split: photo occupies roughly 45% width; lower split: photo occupies a visibly smaller share'
  - Text-block widths differ across the two alternating panels
  confidence: medium
- id: layout_10
  family: layout_composition_components
  polarity: poor
  page_or_region: about page — specialties carousel
  tile_path: store/marekhealth-com/captures/2026-06-04/tiles/about/tile-04-y04224.png
  claim: The specialties carousel pairs flat clip-art-tier icons of uneven visual weight with spaced all-caps headers and a flat red 'START NOW' button, a coarser composition than the refined dark-mode sections elsewhere on the site.
  visible_tells:
  - Pill, syringe, battery, thermometer, and scale icons differ noticeably in footprint and stroke weight across the row
  - Spaced all-caps 'OUR SPECIALTIES' header and blocky 'START NOW' button read heavier and less refined than homepage equivalents
  confidence: high
  contrast_with: store/marekhealth-com/captures/2026-06-04/tiles/homepage/tile-02-y02440.png
- id: layout_11
  family: layout_composition_components
  polarity: poor
  page_or_region: testosterone page — 'Featured On' logo bar
  tile_path: store/marekhealth-com/captures/2026-06-04/tiles/testosterone/tile-02-y02440.png
  claim: The 'Featured On' logo marquee places logos at wildly different visual mass with no optical normalization, and the rightmost logo is clipped at the tile edge with no margin guard.
  visible_tells:
  - Joe Rogan circular badge carries far more visual mass than the flat 'IRONWORK' wordmark beside it
  - The rightmost 'Power Project' logo is cropped mid-mark at the right edge
  confidence: high
  contrast_with: store/marekhealth-com/captures/2026-06-04/tiles/homepage/tile-07-y08540.png
- id: layout_12
  family: layout_composition_components
  polarity: poor
  page_or_region: diagnostics — 'How it works' section
  tile_path: store/marekhealth-com/captures/2026-06-04/tiles/diagnostics_home/tile-01-y01220.png
  claim: The diagnostics 'How it works' three-step row sits on a white background with lighter, denser typography that is visually discontinuous from the dark-mode card style of Marek Health, reading as a different design language dropped in wholesale.
  visible_tells:
  - White-background section follows a darker hero band with no transition
  - Body text weight and leading is lighter and tighter than comparable sections on the main marekhealth.com pages
  confidence: high
  contrast_with: store/marekhealth-com/captures/2026-06-04/tiles/homepage/tile-01-y01220.png
- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: homepage hero
  tile_path: store/marekhealth-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png
  claim: The hero commits to a tight two-tone palette — near-black ground, white body text, a single red-orange accent — and holds it across headline emphasis word, CTA pill, and rating, with no tertiary colors introduced.
  visible_tells:
  - Near-black background fills the hero; headline primary words white, emphasis word 'results' in red-orange
  - Solid red-orange CTA pill matches the accent exactly; no fourth color appears in the field
  confidence: high
- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: homepage hero — photography
  tile_path: store/marekhealth-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png
  claim: The hero photograph is art-directed with hard directional studio light isolating two subjects against a dark void, placing it in the commissioned tier rather than generic health stock.
  visible_tells:
  - Deep shadow fills the right of the frame with no background detail
  - Both subjects are sharply edge-lit on one side, fully dark on the other; neutral athletic wear, no lab-coat/office cues
  confidence: high
- id: color_03
  family: color_brand_imagery
  polarity: strong
  page_or_region: homepage — pricing / CTA section
  tile_path: store/marekhealth-com/captures/2026-06-04/tiles/homepage/tile-05-y06100.png
  claim: The accent color is applied with real discipline across interactive elements — the filled CTA pill and every circular bullet badge share the identical red-orange, while the secondary CTA is deliberately left outline-only, showing intentional hierarchy rather than palette slippage.
  visible_tells:
  - All circular bullet badges down the 'What's included' / 'What comes next' lists use the same red-orange fill
  - Primary 'Get Started' pill matches those badges; the 'Book a free consultation' button is outline-only
  confidence: high
  contrast_with: store/marekhealth-com/captures/2026-06-04/tiles/about/tile-04-y04224.png
- id: color_04
  family: color_brand_imagery
  polarity: mixed
  page_or_region: testosterone page — treatment category cards
  tile_path: store/marekhealth-com/captures/2026-06-04/tiles/testosterone/tile-05-y06100.png
  claim: The silhouette-style treatment cards share a dramatic rim-lit lighting language but read as indistinct dark shapes on dark grounds, so individual services are hard to tell apart at a glance.
  visible_tells:
  - Cards share near-black backgrounds, near-black image zones, and white-on-dark headlines
  - Subjects are back/rim-lit silhouettes that blend into the card backgrounds with little distinguishing detail
  confidence: high
  contrast_with: store/marekhealth-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png
- id: color_05
  family: color_brand_imagery
  polarity: mixed
  page_or_region: testosterone page — statistics infographic
  tile_path: store/marekhealth-com/captures/2026-06-04/tiles/testosterone/tile-03-y03660.png
  claim: The infographic section introduces green as a data accent — body-silhouette fills and the chart's optimal-range band — a color absent from the primary red-orange / white / dark palette, creating a functional but off-brand presence.
  visible_tells:
  - Two of three body-silhouette figures are filled medium green; the chart's 'Optimal Test Range' band is green
  - Green appears in no other reviewed section of the site
  confidence: high
- id: color_06
  family: color_brand_imagery
  polarity: mixed
  page_or_region: diagnostics — sub-brand identity
  tile_path: store/marekhealth-com/captures/2026-06-04/tiles/diagnostics_home/tile-00-y00000.png
  claim: Marek Diagnostics presents a clearly distinct identity from Marek Health — light background, light type, brightly lit photography — confirming a real sub-brand split, though the two systems read as separate rather than one codified family.
  visible_tells:
  - White/light background replaces the dark base of every Marek Health page; wordmark reads 'marek diagnostics' in a lighter treatment
  - Hero is a brightly lit photo of a woman raising her fist — a completely different mood from the dark-studio Marek Health imagery
  confidence: high
  contrast_with: store/marekhealth-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png
- id: color_07
  family: color_brand_imagery
  polarity: poor
  page_or_region: about page — photography
  tile_path: store/marekhealth-com/captures/2026-06-04/tiles/about/tile-02-y02440.png
  claim: The about page swaps in ambient-daylight lifestyle photos — a man at a laptop by a window, a man on a city street — that break from the brand's controlled dark-studio image language and read as generic stock.
  visible_tells:
  - Natural window light and soft ambient tones replace the dark-studio lighting used elsewhere
  - The street image carries warm natural color and full background detail, sharing no visual grammar with the hero portraits or athlete grid
  confidence: high
  contrast_with: store/marekhealth-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png
- id: color_08
  family: color_brand_imagery
  polarity: poor
  page_or_region: testosterone page + performance page — white-box style breaks
  tile_path: store/marekhealth-com/captures/2026-06-04/tiles/testosterone/tile-02-y02440.png
  claim: A white-background block ('Masculinity is in crisis.') with black text drops into the otherwise dark testosterone page — a full inversion of the site's design language with no border, shadow, or relationship to the dark card system, reading as an unstyled content block. The same white-card-on-dark-page break recurs with the 'Guided Optimization' card on the performance page.
  visible_tells:
  - White fill box with black text amid dark sections that use white text
  - The box has no border, shadow, or visual tie to the dark card language used in every other module
  confidence: high
  contrast_with: store/marekhealth-com/captures/2026-06-04/tiles/homepage/tile-01-y01220.png
- id: color_09
  family: color_brand_imagery
  polarity: poor
  page_or_region: performance page — 'Guided Optimization' paint-splash card
  tile_path: store/marekhealth-com/captures/2026-06-04/tiles/performance/tile-01-y01220.png
  claim: The 'Guided Optimization' section places a bright red ink/paint-splash graphic behind a phone mockup on a white card — a one-off motif and an outlier white background that appear nowhere else, and the splash bleeds past the phone into the card with no separation.
  visible_tells:
  - Bright red ink-splash fills the area behind the phone and overflows across the white card
  - No other section uses an illustrative paint/ink element, and every other featured section uses a dark background
  confidence: high
  contrast_with: store/marekhealth-com/captures/2026-06-04/tiles/homepage/tile-05-y06100.png
- id: iconography_01
  family: iconography_illustration
  polarity: strong
  page_or_region: homepage — feature grid icons
  tile_path: store/marekhealth-com/captures/2026-06-04/tiles/homepage/tile-01-y01220.png
  claim: The four feature-card icons (pencil, figure, chart, truck) form a tight consistent set — identical dark rounded-square containers, uniform line weight, same muted fill — with no clip-art mixing or size drift.
  visible_tells:
  - All four icon badges share the same dark-grey rounded-square background and margin
  - Consistent line weight across the pencil, figure, bar-chart, and truck glyphs
  confidence: high
- id: iconography_02
  family: iconography_illustration
  polarity: strong
  page_or_region: homepage — pricing card bullet badges
  tile_path: store/marekhealth-com/captures/2026-06-04/tiles/homepage/tile-05-y06100.png
  claim: The red filled-circle bullet-badge system applies consistently across every pricing-card row — same diameter, same red-orange fill, same white glyph — extending the icon vocabulary into a new context with discipline.
  visible_tells:
  - A column of identical red circle badges runs down both bullet sub-sections at one size
  - The inner glyph (clipboard, person, flask, arrow, truck, tag) varies by meaning without breaking the container shape or color
  confidence: high
  contrast_with: store/marekhealth-com/captures/2026-06-04/tiles/homepage/tile-01-y01220.png
- id: iconography_03
  family: iconography_illustration
  polarity: strong
  page_or_region: homepage — process card UI mockups
  tile_path: store/marekhealth-com/captures/2026-06-04/tiles/homepage/tile-02-y02440.png
  claim: The in-card app UI mockups (calendar scheduler, map route, biomarker results dashboard, treatment plan) are bespoke product renders carrying the brand accent and dark-card aesthetic — custom illustration, not generic stock screenshots.
  visible_tells:
  - Calendar mockup uses the red-orange pill as the selected-day token, matching the CTA color
  - Biomarker mockup shows labeled gradient range bars for Total Testosterone, LH, and FSH — clearly purpose-built UI
  confidence: high
- id: iconography_04
  family: iconography_illustration
  polarity: poor
  page_or_region: about page — specialty icons
  tile_path: store/marekhealth-com/captures/2026-06-04/tiles/about/tile-04-y04224.png
  claim: The about-page specialty icons are flat two-color clip-art-tier illustrations (red-orange fill with heavy black outline) that clash with the thin-line monochrome icon language on the main site and vary in stroke weight and proportion across the row.
  visible_tells:
  - Pill, syringe, battery, thermometer, and scale icons use a cartoonish double-outline style with red-orange fill
  - Stroke weights and footprints differ visibly across the five visible items — a different icon system from the homepage feature grid
  confidence: high
  contrast_with: store/marekhealth-com/captures/2026-06-04/tiles/homepage/tile-01-y01220.png
- id: iconography_05
  family: iconography_illustration
  polarity: mixed
  page_or_region: testosterone page — stat-card graphics
  tile_path: store/marekhealth-com/captures/2026-06-04/tiles/testosterone/tile-03-y03660.png
  claim: The three stat cards mix illustration registers — the donut percentage rings carry a glassy gradient sheen while the third card uses a flat sketch-like orange US-map outline — and the body-figure silhouettes read as generic low-detail public-health icons rather than brand-grade assets.
  visible_tells:
  - Donut rings (70%, 35%) have a metallic/glass gradient not present elsewhere; the US map is flat orange linework
  - The '1 in 4 men' body figures are flat two-tone (green / grey) blocky shapes with no brand character
  confidence: high
  contrast_with: store/marekhealth-com/captures/2026-06-04/tiles/homepage/tile-02-y02440.png
- id: iconography_06
  family: iconography_illustration
  polarity: mixed
  page_or_region: testosterone page — testosterone-by-age line chart
  tile_path: store/marekhealth-com/captures/2026-06-04/tiles/testosterone/tile-02-y02440.png
  claim: The 'Average Testosterone Level Per Age Group' chart is legible but unpolished — plain default grid lines, an untheme'd floating tooltip, and a flat green optimal-range band — reading as a lightly styled charting-library default rather than a designed data graphic.
  visible_tells:
  - Horizontal grid lines are plain grey at uniform weight with no major/minor hierarchy
  - The 'Average By Age Group' tooltip uses a generic floating style; the 'Optimal Test Range' band is a flat color fill
  confidence: high
- id: iconography_07
  family: iconography_illustration
  polarity: mixed
  page_or_region: homepage hero — floating lab-result chips
  tile_path: store/marekhealth-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png
  claim: The floating lab-result chips in the hero ('870 Total Testosterone', '12.6') are on-brand micro-UI that reinforce the data proposition, but they sit as flat overlays on the photo without shadow or depth, reading as pasted-on rather than integrated.
  visible_tells:
  - Chips appear flat against the photo with no drop shadow or blur to sell depth
  - Dark-card style and orange accent are on-brand, but compositing reads as a flat z-index overlay
  confidence: medium
- id: iconography_08
  family: iconography_illustration
  polarity: poor
  page_or_region: homepage — section-label micro-icons
  tile_path: store/marekhealth-com/captures/2026-06-04/tiles/homepage/tile-01-y01220.png
  claim: The tiny circular glyphs prefixing section eyebrows ('The process', etc.) are rendered too small to register, contributing nothing to recognition at their displayed size.
  visible_tells:
  - The badge next to 'The process' is a roughly 10px indistinct shape
  - The same pattern recurs on other section eyebrows with a different but equally illegible glyph each time
  confidence: medium
```

## Provenance

- **Tiles read (Tier-A, cached — zero Firecrawl spend):** native-resolution tiles sliced from the `2026-06-04` capture's full-page screenshots across five pages — `homepage`, `testosterone`, `diagnostics_home`, `performance`, `about` (36 active tiles). Mined blind: four family miners (Sonnet) over tiles-only contexts → judge prune/merge (Opus). 49 raw cards → 41 kept.
- **Page selection:** `telehealth` was tiled but dropped before mining — it is a legal *informed-consent* page (dense body text), a weak carrier of the visual system, not a contamination exclusion. `about` was substituted to give the color/imagery family a brand-story page to read.
- **QA — `clean`:** no tile was excluded for contamination and no Tier-B browser re-render was used. Cookie-consent banners are present in the lower regions of some captures (`diagnostics_home` tile-00/01/02, `testosterone` shop tile), but every cited card's load-bearing tell sits **above** the banner; the one mined card whose tell sat under the banner (a diagnostics "Labwork without" icon row) was rejected by the judge.
- **Author correction:** `color_09`'s `tile_path` was repointed from `performance/tile-02` to `performance/tile-01` — the blind miners split the "Guided Optimization" paint-splash card across two adjacent tiles and the judge kept the wrong citation; the card's content was verified against `performance/tile-01`, where the splash actually renders.
- **Snapshot caveat:** this is a point-in-time read of the `2026-06-04` captured tiles. The live site changes; re-tile/re-mine to refresh.
