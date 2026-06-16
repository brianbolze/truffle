---
schema_version: "1.0"
domain: gethealthspan.com
captured_at: 2026-06-16
source_capture: 2026-06-04
qa_status: recapture-used
---

## Visual & brand impression

Healthspan reads as an art-directed longevity brand — strongest on what it owns, shakiest on what it borrows. The photography is genuinely cinematic: tightly cropped, single-key-light portraits on near-black grounds [color_03]. The commerce system is disciplined — a coherent amber product palette [color_04], color-matched app sections [color_05], regulated card grids and product rows [layout_02][layout_06], and a purpose-built UI icon set over a crafted biomarker dashboard [iconography_01][iconography_02]. Editorial headlines and a repeatable step-index system carry clear hierarchy [typography_04][layout_05]. It slips on borrowed assets and finish: stock-adjacent science and testimonial imagery [color_07][color_09], off-register advisory headshots [color_08], a dual yellow/blue accent with no rule [color_02], a wordmark-as-wallpaper footer [typography_07], and a pathway strip sliced like breakage [layout_12].

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: homepage — 'Transform your quality of living' band (lower page)
  tile_path: store/gethealthspan-com/captures/2026-06-16/tiles/homepage/tile-00-y12684.png
  claim: 'The ''Transform your quality of living'' band runs a clean three-level scale: large display
    headline, a small yellow CTA pill, and a thin nav/trust-bar tier, each clearly separated by size and
    weight.'
  visible_tells:
  - '''Transform your quality of living through the science of aging.'' is substantially larger than any
    surrounding text'
  - Yellow 'JOIN HEALTHSPAN' button sits as a distinct CTA tier against the dark image
  - Centered 'Healthspan' wordmark, small nav items, and the thin trust strip all sit well below headline
    weight
  confidence: high
- id: typography_02
  family: typography_hierarchy
  polarity: strong
  page_or_region: homepage — 'Programs built for your unique health goals' section
  tile_path: store/gethealthspan-com/captures/2026-06-16/tiles/homepage/tile-01-y00000.png
  claim: Section headers use a generous display heading over clearly lighter, smaller body copy, with
    card overlay labels forming a third tier — a readable three-step scale on white.
  visible_tells:
  - Large centered heading dwarfs the body paragraph directly beneath it
  - White card-overlay labels ('Longevity Optimization', 'Men's Hormone Health') are smaller, functioning
    as a third level
  - Body copy is noticeably lighter weight and smaller than the heading
  confidence: high
- id: typography_03
  family: typography_hierarchy
  polarity: strong
  page_or_region: homepage — 'Your journey to a longer, healthier life' section
  tile_path: store/gethealthspan-com/captures/2026-06-16/tiles/homepage/tile-04-y03660.png
  claim: A small spaced uppercase eyebrow ('BECOMING A PATIENT') over a large heading, with a blue-colored
    phrase used as the secondary differentiator instead of weight, produces a confident multi-tier headline.
  visible_tells:
  - Uppercase 'BECOMING A PATIENT' label in small caps sits above a much larger heading
  - Blue-colored phrase 'just a few steps away' differentiates the second line by color rather than weight
  confidence: high
- id: typography_04
  family: typography_hierarchy
  polarity: strong
  page_or_region: how_it_works — step hero / index rule
  tile_path: store/gethealthspan-com/captures/2026-06-16/tiles/how_it_works/tile-01-y00000.png
  claim: A page-wide editorial headline at very large scale carries the hierarchy alone, while a small
    numeric '01' and spaced 'ASSESSMENT' label form a minimal secondary index tier that doesn't compete.
  visible_tells:
  - Full-width display type at large scale, uncluttered, leading the section
  - Small '01' flush-left and spaced uppercase 'ASSESSMENT' flush-right sit at a clearly subordinate size
  confidence: high
- id: typography_05
  family: typography_hierarchy
  polarity: mixed
  page_or_region: homepage — treatments tab / product listing
  tile_path: store/gethealthspan-com/captures/2026-06-16/tiles/homepage/tile-02-y01220.png
  claim: The '(Medications) Supplements Labs' switcher uses parenthetical bracketing as a stylistic device,
    but active vs inactive states are not differentiated by weight, and product names sit at near-equal
    size to prices, leaving an ambiguous hierarchy.
  visible_tells:
  - Tab words mix parenthetical and roman at similar sizes — reads decorative rather than ranked
  - Product name labels and price figures beneath sit at near-equal size with little subordination
  confidence: medium
  contrast_with: store/gethealthspan-com/captures/2026-06-16/tiles/homepage/tile-01-y00000.png
- id: typography_06
  family: typography_hierarchy
  polarity: mixed
  page_or_region: our_company — values accordion (Current / Effective / Personal)
  tile_path: store/gethealthspan-com/captures/2026-06-16/tiles/our_company/tile-05-y04880.png
  claim: The accordion sizes the active row ('Personal') much larger than the collapsed rows, but the
    jump is abrupt and the numeric suffixes '(01)/(02)/(03)' sit at the same size as the inactive labels,
    flattening the lower tiers.
  visible_tells:
  - '''Personal'' heading is disproportionately large versus the small body text and the collapsed ''Current''/''Effective''
    rows'
  - Numeric '(03)' is sized like the inactive labels rather than as a distinct tier
  confidence: medium
- id: typography_07
  family: typography_hierarchy
  polarity: poor
  page_or_region: homepage — footer / oversized wordmark
  tile_path: store/gethealthspan-com/captures/2026-06-16/tiles/homepage/tile-11-y12200.png
  claim: A giant decorative 'Healthspan' wordmark spans the full viewport width below the footer columns,
    dwarfing them and the inline product card so no clear reading order survives — it reads as wallpaper,
    not hierarchy.
  visible_tells:
  - Cream/yellow 'Healthspan' wordmark runs full-width, far larger than any functional element
  - Footer link columns above are all set at similar small sizes with none clearly dominant
  confidence: high
  contrast_with: store/gethealthspan-com/captures/2026-06-16/tiles/homepage/tile-01-y00000.png
- id: typography_08
  family: typography_hierarchy
  polarity: poor
  page_or_region: homepage — '(Follow the science)' hero overlay
  tile_path: store/gethealthspan-com/captures/2026-06-16/tiles/homepage/tile-10-y10980.png
  claim: The yellow '(Follow the science)' headline overlays a close-up portrait where the upper-left
    type sits over lighter skin/highlight, weakening contrast, while a fairly large white body paragraph
    at right competes rather than reads as subordinate.
  visible_tells:
  - Yellow '(Follow the science)' type runs over the lighter highlight side of the face, reducing legibility
  - Right-side white body paragraph is large enough to rival, not support, the headline
  confidence: medium
- id: typography_09
  family: typography_hierarchy
  polarity: poor
  page_or_region: rapamycin — 'Cellular pathways are roads to peak performance'
  tile_path: store/gethealthspan-com/captures/2026-06-16/tiles/rapamycin/tile-02-y01220.png
  claim: 'The intended three-level headline collapses to two in practice: the ''GOING DEEPER'' eyebrow
    is set so small it barely registers, and the card captions below sit at a similar tiny size with no
    graduation from them.'
  visible_tells:
  - Eyebrow 'GOING DEEPER' is rendered so small it disappears before the headline registers
  - Card captions ('Metabolic Flexibility', 'Autophagy Activation', etc.) are at similarly small sizes,
    offering no step down
  confidence: medium
  contrast_with: store/gethealthspan-com/captures/2026-06-16/tiles/homepage/tile-04-y03660.png
- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: homepage — 'Transform your quality of living' band (lower page)
  tile_path: store/gethealthspan-com/captures/2026-06-16/tiles/homepage/tile-00-y12684.png
  claim: The 'Transform your quality of living' band sets its content over a full-bleed portrait, with
    the centered-wordmark nav above and a tidy two-button CTA cluster aligned to the headline column —
    clean alignment across wordmark, headline, and controls.
  visible_tells:
  - Wordmark centered in nav between left and right link groups
  - Two CTA buttons (yellow + outlined) sit flush-left on the headline column at consistent rhythm
  - Full-bleed background photo contains the subject without awkward cropping
  confidence: high
- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: homepage — program card row
  tile_path: store/gethealthspan-com/captures/2026-06-16/tiles/homepage/tile-01-y00000.png
  claim: Three program cards form a regulated three-column grid with matched height, lower-left label
    placement, and an identically positioned arrow badge on every card.
  visible_tells:
  - Card category tags + headlines align to the same baseline across all three cards
  - Circular arrow badge sits at the same corner on each card
  - Uniform gutters; no card overflows its container
  confidence: high
  contrast_with: store/gethealthspan-com/captures/2026-06-16/tiles/homepage/tile-06-y06100.png
- id: layout_03
  family: layout_composition_components
  polarity: strong
  page_or_region: homepage — four-column stat row
  tile_path: store/gethealthspan-com/captures/2026-06-16/tiles/homepage/tile-02-y01220.png
  claim: The four-stat block is evenly distributed with each cell identically structured (large numeral,
    label, sub-label), giving a clean horizontal scan rhythm with no ragged edge.
  visible_tells:
  - Identical internal hierarchy repeated in each of the four stat cells
  - Even column widths, no overflow or orphan column
  confidence: high
- id: layout_04
  family: layout_composition_components
  polarity: strong
  page_or_region: homepage — interactive product tab section
  tile_path: store/gethealthspan-com/captures/2026-06-16/tiles/homepage/tile-04-y03660.png
  claim: The tabbed feature section uses a dark pill-tab bar with a clearly highlighted active state (yellow
    fill on 'Labs Analysis'), centered content below, and a readable measure — a well-finished interactive
    component.
  visible_tells:
  - Active tab 'Labs Analysis' is a yellow filled pill versus ghost siblings
  - Tab row centered within the dark container; body copy below centered and constrained
  confidence: high
- id: layout_05
  family: layout_composition_components
  polarity: strong
  page_or_region: how_it_works — step divider rule + index
  tile_path: store/gethealthspan-com/captures/2026-06-16/tiles/how_it_works/tile-01-y00000.png
  claim: Step transitions use a full-width hairline rule with the step number flush-left and the step
    label flush-right, a repeatable indexing system applied consistently across steps.
  visible_tells:
  - Rule spans full viewport with '01' flush-left and 'ASSESSMENT' flush-right
  - Same rule + flush-left number recurs ('02' / 'CONNECT' on tile-02) at consistent spacing
  confidence: high
  contrast_with: store/gethealthspan-com/captures/2026-06-16/tiles/how_it_works/tile-02-y01220.png
- id: layout_06
  family: layout_composition_components
  polarity: strong
  page_or_region: medications — product listing rows
  tile_path: store/gethealthspan-com/captures/2026-06-16/tiles/medications/tile-02-y01220.png
  claim: Product rows are uniformly structured — photo left, then name + description + benefit bullets
    + price + two CTAs right — with consistent vertical rhythm down the list.
  visible_tells:
  - Every row aligns its product photo to the same left column width
  - Benefit lines use matching colored dots at consistent spacing
  - The two-button CTA pair (GET STARTED + LEARN MORE) is identically sized and placed in each row
  confidence: high
- id: layout_07
  family: layout_composition_components
  polarity: strong
  page_or_region: medications — left-rail category filter
  tile_path: store/gethealthspan-com/captures/2026-06-16/tiles/medications/tile-02-y01220.png
  claim: 'The left-rail filter is a coherent, finished component: a filled active pill (''METABOLISM''),
    plain-text inactive items at even spacing, and a distinct ''+FILTERS'' expander.'
  visible_tells:
  - Active category rendered as a filled pill with no overflow
  - Inactive items are plain text at consistent vertical spacing
  - '''+FILTERS'' at the bottom is visually distinct from the category list'
  confidence: high
- id: layout_08
  family: layout_composition_components
  polarity: mixed
  page_or_region: homepage — scattered image mosaic ('How it works' steps)
  tile_path: store/gethealthspan-com/captures/2026-06-16/tiles/homepage/tile-05-y04880.png
  claim: The step section drops the grid for scattered, varied-size images; the asymmetry is intentional
    but the large left-anchored phone image far outweighs three small ghosts at top, leaving a left-heavy,
    ambiguous composition.
  visible_tells:
  - Large phone image dominates the left at roughly 3x the size of the other thumbnails
  - Right-side images appear much smaller and compositionally weak
  - Step copy floats mid-section with no clear anchor to the image cluster
  confidence: medium
  contrast_with: store/gethealthspan-com/captures/2026-06-16/tiles/homepage/tile-01-y00000.png
- id: layout_09
  family: layout_composition_components
  polarity: mixed
  page_or_region: homepage — 'featured in' press row
  tile_path: store/gethealthspan-com/captures/2026-06-16/tiles/homepage/tile-07-y07320.png
  claim: The press-logo row is interrupted mid-line by a large yellow 'JOIN HEALTHSPAN' button that breaks
    the logo scan and reads as inserted rather than composed with the row.
  visible_tells:
  - WP, USA Today, Business Insider, WSJ logos sit left in a horizontal row
  - The yellow CTA button lands immediately after WSJ with no separation, at logo weight
  - A pull-quote at right is cut off at the tile edge, suggesting the row runs wide of comfortable width
  confidence: medium
- id: layout_10
  family: layout_composition_components
  polarity: mixed
  page_or_region: our_company — accordion 'Our promises' section
  tile_path: store/gethealthspan-com/captures/2026-06-16/tiles/our_company/tile-04-y03660.png
  claim: The promises accordion uses clean full-width bordered rows with an expanded state that insets
    an image at right, but a large empty band sits between the section headline and the first row, reading
    as an oversized gap.
  visible_tells:
  - Roughly half the tile above the first accordion row is empty white space
  - Expanded 'Effective' row insets an image right with body text — well structured internally
  - Collapsed rows are minimal (label left, number right), clean but sparse
  confidence: medium
- id: layout_11
  family: layout_composition_components
  polarity: poor
  page_or_region: how_it_works — 'The experts will see you now' scattered portraits
  tile_path: store/gethealthspan-com/captures/2026-06-16/tiles/how_it_works/tile-03-y02440.png
  claim: Six expert portraits scatter around centered text with no underlying grid, inconsistent sizes,
    and only plain rectangular crops, so the layout reads as informal rather than intentionally editorial.
  visible_tells:
  - Six thumbnails at noticeably different sizes with no row/column logic
  - All rectangular crops at arbitrary positions; no masking, rotation, or shape variety to signal intent
  - Center text sits isolated from the portrait cluster with no bridging element
  confidence: medium
- id: layout_12
  family: layout_composition_components
  polarity: poor
  page_or_region: rapamycin — cellular-pathway image strip
  tile_path: store/gethealthspan-com/captures/2026-06-16/tiles/rapamycin/tile-02-y01220.png
  claim: 'The pathway image strip overflows the viewport: the sixth card (''Metabolic Flexibility'') is
    sliced at the right edge with no scroll arrow, gradient fade, or other overflow affordance, so the
    cut looks like breakage.'
  visible_tells:
  - A sixth card is visibly cut at the right edge of the viewport
  - No scroll arrow, fade, or overflow indicator on either end of the strip
  confidence: high
- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: dark sections — teal-to-black-to-white gradient device
  tile_path: store/gethealthspan-com/captures/2026-06-16/tiles/how_it_works/tile-01-y00000.png
  claim: A deep teal-to-black-to-white gradient is used as a recurring structural divider across pages,
    giving dark sections an atmospheric mood rather than a flat fill.
  visible_tells:
  - Upper half pure black with display type; lower half bleeds through teal-midnight into white as a section
    divider
  - The same gradient recurs on homepage tile-04 and our_company tile-02, confirming intentional reuse
  confidence: high
  contrast_with: store/gethealthspan-com/captures/2026-06-16/tiles/homepage/tile-04-y03660.png
- id: color_02
  family: color_brand_imagery
  polarity: mixed
  page_or_region: site-wide — dual yellow + blue inline accent system
  tile_path: store/gethealthspan-com/captures/2026-06-16/tiles/homepage/tile-08-y08540.png
  claim: Two inline accents run in parallel — a warm yellow and a light steel-blue — both used as headline
    emphasis with no clear rule separating them, creating mild palette ambiguity rather than a single
    disciplined accent.
  visible_tells:
  - '''patients'' in ''Hear from our patients'' renders in light steel-blue; the same blue recurs on ''never
    wavers'' (our_company tile-03), ''8 years'' (rapamycin tile-03), and ''Cellular pathways'' (rapamycin
    tile-02)'
  - Yellow is used for the same job elsewhere — '(Follow the science)' (homepage tile-10) and the wordmark
    — so the two accents co-exist without hierarchy
  confidence: high
  contrast_with: store/gethealthspan-com/captures/2026-06-16/tiles/our_company/tile-03-y02440.png
- id: color_03
  family: color_brand_imagery
  polarity: strong
  page_or_region: homepage — full-bleed dark portrait photography
  tile_path: store/gethealthspan-com/captures/2026-06-16/tiles/homepage/tile-10-y10980.png
  claim: Hero and section portraits are tightly cropped, high-contrast close-ups on near-black grounds
    with a single warm key light, giving the photography a cinematic, art-directed register rather than
    generic wellness stock.
  visible_tells:
  - Face photographed against near-black surroundings with a warm key light raking across features
  - Same dark-ground cinematic register repeats in the how_it_works torso crop (tile-07) and Performance
    Coaching portrait (tile-09)
  confidence: high
  contrast_with: store/gethealthspan-com/captures/2026-06-16/tiles/how_it_works/tile-07-y07320.png
- id: color_04
  family: color_brand_imagery
  polarity: strong
  page_or_region: product photography — amber/warm-neutral palette
  tile_path: store/gethealthspan-com/captures/2026-06-16/tiles/homepage/tile-02-y01220.png
  claim: Oral product shots use a consistent amber-glass bottle with cream/ivory labels, giving the supplement
    line a coherent warm proprietary palette distinct from clinical white-on-white competitors.
  visible_tells:
  - Row of amber-glass bottles with matching cream labels bearing the Healthspan wordmark
  - The same amber bottle recurs on medications tile-02/03 and the rapamycin Protocol shot (tile-08)
  confidence: high
  contrast_with: store/gethealthspan-com/captures/2026-06-16/tiles/medications/tile-02-y01220.png
- id: color_05
  family: color_brand_imagery
  polarity: strong
  page_or_region: labs — app UI on black with warm amber gradient bleed
  tile_path: store/gethealthspan-com/captures/2026-06-16/tiles/labs/tile-03-y02440.png
  claim: The platform UI screenshot is presented on a black ground with a warm amber-to-brown gradient
    bleeding below it, deliberately color-matching the screenshot section to the product palette rather
    than using a neutral crop.
  visible_tells:
  - A warm amber-orange gradient fills the lower half of the tile beneath the dark app card
  - The dark app card uses the same small red/blue status dots seen in the homepage app screenshots, keeping
    UI color language consistent
  confidence: high
- id: color_06
  family: color_brand_imagery
  polarity: mixed
  page_or_region: homepage — program card photography
  tile_path: store/gethealthspan-com/captures/2026-06-16/tiles/homepage/tile-01-y00000.png
  claim: Program cards share the dark-ground portrait convention but lighting quality varies card to card
    — the lit male portrait reads editorial while the bearded man is flatter and more generic — so the
    set feels partly like hired stock.
  visible_tells:
  - 'Three cards: one high-contrast lit male portrait, one flatter-lit bearded man, one side-lit woman
    — uneven presence'
  - All share the dark-ground look but differ in lighting craft
  confidence: medium
  contrast_with: store/gethealthspan-com/captures/2026-06-16/tiles/homepage/tile-10-y10980.png
- id: color_07
  family: color_brand_imagery
  polarity: mixed
  page_or_region: rapamycin — cellular-science macro photography
  tile_path: store/gethealthspan-com/captures/2026-06-16/tiles/rapamycin/tile-06-y06100.png
  claim: The science section uses circular-cropped biological macro photography (warm orange, teal, organic
    forms) that is on-palette but recognizable as licensed science-stock for the longevity space rather
    than owned imagery.
  visible_tells:
  - Circular image crops show orange cellular textures and green/organic material with no diagram structure
  - Warm hues broadly match the brand amber, but the microscopy look is a common stock category
  confidence: medium
  contrast_with: store/gethealthspan-com/captures/2026-06-16/tiles/rapamycin/tile-08-y08540.png
- id: color_08
  family: color_brand_imagery
  polarity: poor
  page_or_region: our_company — medical advisory board headshots
  tile_path: store/gethealthspan-com/captures/2026-06-16/tiles/our_company/tile-07-y07320.png
  claim: Advisory-board headshots are shot on inconsistent backgrounds and flat ambient light, breaking
    the dark cinematic photography language used everywhere else on the site.
  visible_tells:
  - Dr. Rick Cohen on light-grey studio with flat light; Dr. Elana Miller and Dr. Scott Sanderson on different,
    warmer/outdoor-ish grounds
  - None matches the dark moody register of the hero, product, or editorial photography
  confidence: high
  contrast_with: store/gethealthspan-com/captures/2026-06-16/tiles/homepage/tile-10-y10980.png
- id: color_09
  family: color_brand_imagery
  polarity: mixed
  page_or_region: homepage — testimonial card backgrounds
  tile_path: store/gethealthspan-com/captures/2026-06-16/tiles/homepage/tile-08-y08540.png
  claim: Testimonial cards mix one literal action-sports photo with three abstract amber-to-brown color
    washes; the warm washes are on-brand but the sports image reads as generic stock out of step with
    the editorial tone elsewhere.
  visible_tells:
  - Leftmost card shows a documentary-style male-torso action photo
  - Remaining cards are dark amber-to-brown washes with no identifiable image — abstract and on-palette
  confidence: medium
- id: color_10
  family: color_brand_imagery
  polarity: strong
  page_or_region: rapamycin — couple portrait in circular vignette
  tile_path: store/gethealthspan-com/captures/2026-06-16/tiles/rapamycin/tile-03-y02440.png
  claim: A couple portrait is composited inside a soft circular vignette on white, a controlled presentation
    device that keeps the image from reading as a raw stock pull.
  visible_tells:
  - Circular crop with a soft white halo edge over a faint ring-chart background
  - Warm skin tones and soft natural light match the site's broader portrait register
  confidence: medium
- id: iconography_01
  family: iconography_illustration
  polarity: strong
  page_or_region: homepage — product dashboard tab bar icons
  tile_path: store/gethealthspan-com/captures/2026-06-16/tiles/homepage/tile-04-y03660.png
  claim: The five-tab UI bar (Labs Analysis, Protocols, Coaching, Optimizations, MySpan) carries a cohesive
    set of small line icons at a consistent stroke weight, each semantically distinct — reads as a purpose-built
    icon set, not an off-the-shelf grab-bag.
  visible_tells:
  - Five small icons at matching stroke weight inside the dark pill tab bar
  - Each glyph is distinct (search/flask, atom, heart, check-shield, anchor) with no redundancy
  confidence: medium
- id: iconography_02
  family: iconography_illustration
  polarity: strong
  page_or_region: homepage — biomarker dashboard data-viz
  tile_path: store/gethealthspan-com/captures/2026-06-16/tiles/homepage/tile-04-y03660.png
  claim: The biomarker table inside the app mockup pairs color-coded status dots (red/blue/green) with
    inline sparkline trend charts and reference bands — a crafted data-viz component, not a placeholder.
  visible_tells:
  - Rows show a status dot, label, numeric value with unit, and a miniature trend line with reference
    band
  - Color coding separates 'Above Range' (red), 'Optimal' (blue), 'In Range' (green)
  confidence: medium
  contrast_with: store/gethealthspan-com/captures/2026-06-16/tiles/labs/tile-02-y01220.png
- id: iconography_03
  family: iconography_illustration
  polarity: strong
  page_or_region: how_it_works — floating step chip component
  tile_path: store/gethealthspan-com/captures/2026-06-16/tiles/how_it_works/tile-01-y00000.png
  claim: A minimal floating step chip ('STEP 1 / Assessment' with a + affordance and small glyph) recurs
    at the same bottom-center position across steps, indicating a controlled component rather than ad
    hoc elements.
  visible_tells:
  - Pill chip with step label, small icon, and + affordance
  - The same chip recurs ('STEP 2 / Connect') at the identical bottom-center position on tile-02
  confidence: high
  contrast_with: store/gethealthspan-com/captures/2026-06-16/tiles/how_it_works/tile-02-y01220.png
- id: iconography_04
  family: iconography_illustration
  polarity: strong
  page_or_region: how_it_works — floating product-UI overlays
  tile_path: store/gethealthspan-com/captures/2026-06-16/tiles/how_it_works/tile-09-y09760.png
  claim: Circular UI overlays — a video-call interface and a 'Next Steps From Your Assessment Call' protocol
    card — are composited over full-bleed photography as designed product illustration, not generic device
    mockups.
  visible_tells:
  - Circular crop of a doctor video call overlaid on the lifestyle photo
  - Protocol card lists specific items (Rapamycin, Weight Lifting, Mediterranean Diet) each with a small
    avatar/icon
  confidence: medium
- id: iconography_05
  family: iconography_illustration
  polarity: mixed
  page_or_region: rapamycin — concept labels paired with macro photography
  tile_path: store/gethealthspan-com/captures/2026-06-16/tiles/rapamycin/tile-02-y01220.png
  claim: Biological concepts are illustrated with a strip of close-up macro photos labeled below ('Metabolic
    Flexibility', 'Autophagy Activation', 'AMPK-mTOR Regulation', etc.) — editorial stock dressed as illustration,
    not purpose-drawn diagrams.
  visible_tells:
  - Tiled close-up photos of biological material with concept captions beneath each
  - No original diagram or mechanism illustration — all imagery is photographic
  confidence: high
  contrast_with: store/gethealthspan-com/captures/2026-06-16/tiles/rapamycin/tile-06-y06100.png
- id: iconography_06
  family: iconography_illustration
  polarity: mixed
  page_or_region: medications — benefit-bullet dot markers
  tile_path: store/gethealthspan-com/captures/2026-06-16/tiles/medications/tile-02-y01220.png
  claim: Benefit lines open with small filled accent-color dots used as list markers — decorative color
    dots, not meaningful icons; they add rhythm but carry no semantic differentiation.
  visible_tells:
  - Each benefit line begins with a small filled dot in an accent color
  - Dots are identical in shape regardless of which benefit they mark — no icon differentiation
  confidence: high
- id: iconography_07
  family: iconography_illustration
  polarity: mixed
  page_or_region: homepage — comparison table check/cross icons
  tile_path: store/gethealthspan-com/captures/2026-06-16/tiles/homepage/tile-07-y07320.png
  claim: The Healthspan-vs-Others comparison uses standard checkmark and X icons — functional but entirely
    generic, with no custom illustration treatment.
  visible_tells:
  - Dark 'Healthspan' column with check icons beside a light 'Others' column with X icons
  - Icons are stock check/cross glyphs with no craft differentiation
  confidence: high
- id: iconography_08
  family: iconography_illustration
  polarity: poor
  page_or_region: labs — biomarker tag cloud (no icon system)
  tile_path: store/gethealthspan-com/captures/2026-06-16/tiles/labs/tile-02-y01220.png
  claim: The '(Types of tests)' section lists biomarker names as a plain variable-weight tag cloud with
    no supporting iconography, category markers, or illustration — purely typographic.
  visible_tells:
  - Biomarker names ('Total Cholesterol', 'Triglycerides', 'C-Reactive Protein') rendered as a weight-varied
    cloud
  - No icons, category markers, or illustrative elements anywhere in the section
  confidence: high
- id: iconography_09
  family: iconography_illustration
  polarity: poor
  page_or_region: rapamycin — bottom CTA trust badges
  tile_path: store/gethealthspan-com/captures/2026-06-16/tiles/rapamycin/tile-10-y10980.png
  claim: The bottom CTA strip uses four small icon+label trust badges (No hidden fees, Personalized Protocols,
    Free Shipping, Doctor & Clinical Team) that are interchangeable with generic e-commerce badge glyphs
    — no custom craft.
  visible_tells:
  - Four icon+text pairs at very small size with simple generic glyphs
  - Icons match standard SaaS/e-commerce trust-badge patterns
  confidence: medium
```

## Provenance

- **Tiles read.** 69 native-resolution tiles across 6 pages — homepage, medications, labs, how_it_works, our_company, rapamycin — **all Tier-B browser re-renders** captured `2026-06-16` (`captures/2026-06-16/tiles/`). No cached Firecrawl tiles were used.
- **Why a full Tier-B re-render (→ `qa_status: recapture-used`).** The `2026-06-04` cached capture was overlay-contaminated: a centered **"Get 10% Off Your Next Order" newsletter modal** (with a full-page dim) sat over the homepage, and a **custom bottom-right cookie banner** stamped onto every page. The prior `visual.md` excluded the modal hero and caveated the cookie banner across five pages. This run re-rendered all six pages in **system Chrome (real WebGL)**, dismissing the newsletter modal (Escape + "No, thanks") and hiding the cookie banner before tiling, so **no tile carries an overlay**. Zero exclusions.
- **Mining.** 4 blind family miners (Sonnet, tiles-only, no network) over the 69 tiles → 51 raw cards → Opus judge pruned/merged to **40 accepted** (10 rejected). Judge factual corrections: the site runs a **dual yellow+blue** inline-accent system (not a single accent); the `our_company` value panels are dark-translucent-on-teal (not light-gray); the `medications` filter active-state color is **per-category** (amber Metabolism / blue Senescence), not one brand token.
- **Synthesizer corrections (post-judge, tile-grounded).** (1) `typography_01` / `layout_01` cite `homepage/tile-00-y12684.png`, which the blind miners labeled the "hero / above fold" — it is actually the lower-page **"Transform your quality of living" telehealth band** (the true top is "Programs built for your unique health goals"); relabeled, tells unchanged. (2) `layout_11` portrait count corrected to **six** (not five). (3) **Artifact spot-check of all 8 `poor` cards** against their native tiles: all reflect genuine rendered design states (no mid-animation, lazy-load, or compositing artifacts) — none dropped.
- **Snapshot caveat.** Reflects the site as re-rendered `2026-06-16`; the live site changes, so treat it as a point-in-time read.
