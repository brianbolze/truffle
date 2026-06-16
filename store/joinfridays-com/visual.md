---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.0"
domain: joinfridays.com
captured_at: 2026-06-16
source_capture: 2026-06-04
qa_status: recapture-used
---

# joinfridays.com — visual evidence

## Visual & brand impression

Fridays presents as a systematized, on-brand telehealth site. Color works as a navigation code — each vertical owns a hue wash carried from section into its product cards [color_01], anchored by a custom lowercase-serif "fridays" wordmark used as an owned mark [color_03] over a reused section template across treatments [layout_03]. Product vials are high-quality 3-D renders, a clear step above stock pharma photography [iconography_01], peaking on the monochrome burgundy testosterone hero [color_02, iconography_02]. Typography holds a disciplined eyebrow-over-display rhythm [typography_02]. Friction clusters in three spots: the hero's coupon-code panel pulls the editorial fold toward bargain e-commerce [color_06, typography_05]; brand-name med cutouts sit a visible tier below the compound renders [iconography_03]; and the off-system Happy Sleep co-brand page drops the hue system [color_08]. Tiny low-contrast legal type recurs [typography_07].

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: Homepage hero — 'Spring reset starts now' headline
  tile_path: store/joinfridays-com/captures/2026-06-16/tiles/homepage/tile-00-y00000.png
  claim: The hero headline sets a clear top-of-scale with a heavy large-display serif that outranks everything
    else on the fold, and embeds the lowercase 'fridays' logotype as a second register inside the line.
  visible_tells:
  - '''Spring reset starts now'' rendered in a heavy serif at roughly 3-4x the nav text size'
  - '''starts now'' set in a lime accent color, ''Spring reset'' in white, within the same headline'
  confidence: high
  contrast_with: store/joinfridays-com/captures/2026-06-16/tiles/homepage/tile-01-y01220.png
- id: typography_02
  family: typography_hierarchy
  polarity: strong
  page_or_region: Homepage — section heads throughout scroll (weight loss, longevity, microdosing)
  tile_path: store/joinfridays-com/captures/2026-06-16/tiles/homepage/tile-05-y06100.png
  claim: A consistent two-level rhythm — small all-caps eyebrow label above a large display head — repeats
    reliably across every content section, establishing a disciplined hierarchy.
  visible_tells:
  - Small all-caps label 'GLP-1 MICRODOSING' sits above the display head 'Small doses. Big difference.'
  - Same eyebrow-over-head pattern visible for 'LONGEVITY / Feel better, age smarter' (tile-04) and 'GLP-1
    WEIGHT LOSS / Lose weight your way' (tile-01)
  confidence: high
  contrast_with: store/joinfridays-com/captures/2026-06-16/tiles/homepage/tile-04-y04880.png
- id: typography_03
  family: typography_hierarchy
  polarity: strong
  page_or_region: Testosterone landing page hero — 'No more excuses'
  tile_path: store/joinfridays-com/captures/2026-06-16/tiles/testosterone/tile-00-y00000.png
  claim: 'The testosterone hero shifts to white-on-dark-red but holds the same multi-step type scale:
    large headline, medium subhead, smaller offer line, then small benefit bullets — the system carries
    across color contexts.'
  visible_tells:
  - '''No more excuses'' headline in large weight, with ''excuses'' bolder than ''No more'''
  - '''Your testosterone didn''t ghost you — it moved out'' subhead is one clear step smaller and lighter'
  - '''Here''s $100 off to get it back'' reads as a third distinct level above the red CTA pill'
  confidence: high
- id: typography_04
  family: typography_hierarchy
  polarity: strong
  page_or_region: Pricing page — FAQ section 'Get the answers you need'
  tile_path: store/joinfridays-com/captures/2026-06-16/tiles/pricing/tile-05-y06100.png
  claim: 'The FAQ block uses a clean three-level hierarchy: large display head, a small grey sub-paragraph,
    then bold accordion questions in light bordered pills — visually distinct without relying on color
    alone.'
  visible_tells:
  - '''Get the answers you need'' is roughly 3x the accordion question size'
  - A small grey body paragraph below the head creates a mid level before the list
  - Accordion questions are bold dark text inside individually bordered rounded containers, grouping them
    as a fourth visual tier
  confidence: high
- id: typography_05
  family: typography_hierarchy
  polarity: mixed
  page_or_region: Homepage hero — right-panel promo / coupon-code block
  tile_path: store/joinfridays-com/captures/2026-06-16/tiles/homepage/tile-00-y00000.png
  claim: The promo panel stacks too many competing type levels — banner headline, 'BEST OFFER', dollar-off
    figures, month tiers, and coupon pills — at near-equal weight, producing local hierarchy confusion.
  visible_tells:
  - '''SAVE BIG! Up to $500 off!'' banner competes with the yellow ''BEST OFFER!'' tag and the ''$500
    OFF 12 MONTHS'' row at similar visual weight'
  - Dark coupon-code pills (NEWYOU12, NYNY12) sit at the same prominence as the dollar-off figures beside
    them
  confidence: high
  contrast_with: store/joinfridays-com/captures/2026-06-16/tiles/homepage/tile-05-y06100.png
- id: typography_06
  family: typography_hierarchy
  polarity: poor
  page_or_region: Whats_included (Happy Sleep) — 'WHAT'S INCLUDED' checklist
  tile_path: store/joinfridays-com/captures/2026-06-16/tiles/whats_included/tile-00-y00000.png
  claim: The 'WHAT'S INCLUDED' checklist is set in small, thin, low-contrast grey with no item emphasized
    — individual inclusions are uniform and not quickly scannable at reading distance.
  visible_tells:
  - Checklist lines ('Multiple nights of FDA-cleared testing', etc.) are uniform small grey type with
    no bold or size variation
  - No lead inclusion is differentiated to guide the eye down the list
  confidence: medium
  contrast_with: store/joinfridays-com/captures/2026-06-16/tiles/homepage/tile-05-y06100.png
- id: typography_07
  family: typography_hierarchy
  polarity: poor
  page_or_region: Homepage / pricing footer — legal & disclaimer copy
  tile_path: store/joinfridays-com/captures/2026-06-16/tiles/homepage/tile-09-y10980.png
  claim: Footer legal and disclaimer copy is set in very small grey-on-dark-green type that is effectively
    illegible at normal reading distance.
  visible_tells:
  - The 'Fridays whitepapers' disclaimer paragraph is the smallest text block on the page
  - Grey text on the deep forest-green footer further suppresses contrast
  confidence: high
- id: typography_08
  family: typography_hierarchy
  polarity: strong
  page_or_region: Whats_included (Happy Sleep) — 'No surprise costs' pricing table
  tile_path: store/joinfridays-com/captures/2026-06-16/tiles/whats_included/tile-02-y02440.png
  claim: 'The cost-comparison table carries the value read with type weight alone: the Fridays ''$199''
    total is set heavy while competitor totals stay light, and the ''Total Out-of-Pocket Costs'' summary
    row is bolded to signal the bottom line.'
  visible_tells:
  - '''$199'' is visibly heavier than the ''$4,500'' and ''$750'' in adjacent columns'
  - The 'Total Out-of-Pocket Costs' row sits on a highlighted band and reads as the summary, distinct
    from the 'Included / $500 / $200' rows above
  confidence: high
- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: Homepage hero — two-zone split
  tile_path: store/joinfridays-com/captures/2026-06-16/tiles/homepage/tile-00-y00000.png
  claim: The hero splits into two cleanly aligned zones — a before/after photo panel left and a structured
    promo-code table right — each on its own tight internal grid with no bleed between them.
  visible_tells:
  - 'Left: two portrait photos with yellow ''Before''/''After'' pills, caption line, and Klarna badge
    flush to a common left margin'
  - 'Right: promo table with alternating dark/light rows and right-justified coupon pills on an independent
    grid'
  confidence: high
- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: Homepage — 2x2 category card grid
  tile_path: store/joinfridays-com/captures/2026-06-16/tiles/homepage/tile-00-y00000.png
  claim: The four category cards form a consistent 2x2 grid with identical card height, pill label position,
    and trailing-edge product image.
  visible_tells:
  - GLP-1 Weight Loss, Longevity, Testosterone, GLP-1 Microdosing share the same rounded-rect container
    and image-at-right placement
  - Color-coded background per card (sage, teal, rose, olive) differentiates without breaking the grid
  confidence: high
- id: layout_03
  family: layout_composition_components
  polarity: strong
  page_or_region: Homepage — product category sections (template reuse)
  tile_path: store/joinfridays-com/captures/2026-06-16/tiles/homepage/tile-01-y01220.png
  claim: Each treatment category section reuses one layout module — eyebrow + headline, a checklist with
    a lifestyle photo, then a row of product cards below — indicating a disciplined template system across
    verticals.
  visible_tells:
  - 'Weight Loss section (tile-01) mirrors Longevity (tile-04) and Testosterone (tile-07): label / headline
    / checklist / photo / product-card row'
  - Product cards repeat identical anatomy (name, subline, vial render, dark CTA button) across categories
  confidence: high
  contrast_with: store/joinfridays-com/captures/2026-06-16/tiles/homepage/tile-04-y04880.png
- id: layout_04
  family: layout_composition_components
  polarity: strong
  page_or_region: Homepage — three-step process row
  tile_path: store/joinfridays-com/captures/2026-06-16/tiles/homepage/tile-05-y06100.png
  claim: The 'Better health, one Friday at a time' section is three equal-width columns with 01/02/03
    labels, short copy, and phone mockups at uniform scale and registration — evenly spaced, no crowding.
  visible_tells:
  - '''01 Take our quiz / 02 Meet your provider / 03 Begin your journey'' columns are equal width with
    phone mockups aligned on a common baseline'
  confidence: high
- id: layout_05
  family: layout_composition_components
  polarity: strong
  page_or_region: Pricing page — two-plan card comparison
  tile_path: store/joinfridays-com/captures/2026-06-16/tiles/pricing/tile-01-y01220.png
  claim: The Semaglutide and Tirzepatide plan cards are structurally identical — render, name, tag, price,
    checklist, CTA in the same sequence — with the Tirzepatide card gaining a green outline and 'MOST
    POPULAR / RATED FOR RESULTS' badge to elevate it without breaking the template.
  visible_tells:
  - Both cards share identical internal anatomy in the same order; Tirzepatide adds a green border and
    badge
  - Feature checklists are left-aligned with consistent checkmarks across both cards
  confidence: high
- id: layout_06
  family: layout_composition_components
  polarity: strong
  page_or_region: Pricing page — competitor comparison table (Fridays / ro / hims)
  tile_path: store/joinfridays-com/captures/2026-06-16/tiles/pricing/tile-03-y03660.png
  claim: The feature comparison is a clean three-column grid with the Fridays column tinted sage and competitor
    columns plain, check/X marks uniformly sized and centered — easy to scan with no ragged rows.
  visible_tells:
  - Row labels flush-left; check/X cells centered in each column with no orphaned or misaligned rows
  - Fridays column carries a sage highlight band that anchors the brand against the white 'ro' and 'hims'
    columns
  confidence: high
- id: layout_07
  family: layout_composition_components
  polarity: mixed
  page_or_region: Homepage hero — register collision across the split
  tile_path: store/joinfridays-com/captures/2026-06-16/tiles/homepage/tile-00-y00000.png
  claim: The hero split is structurally clean but tonally collides — the left half is editorial (dark-green
    photo panel) while the right is a transactional coupon table on light green, with no visual bridge
    tying the headline to the offer grid.
  visible_tells:
  - 'Left: dark green panel with before/after imagery and a ''real Fridays patient'' caption'
  - 'Right: light green panel densely packed with promo-code rows; the ''Spring reset starts now'' headline
    does not connect across the seam'
  confidence: medium
  contrast_with: store/joinfridays-com/captures/2026-06-16/tiles/homepage/tile-04-y04880.png
- id: layout_08
  family: layout_composition_components
  polarity: mixed
  page_or_region: Homepage — lead-gen split (protein cheat sheet + weight calculator)
  tile_path: store/joinfridays-com/captures/2026-06-16/tiles/homepage/tile-03-y03660.png
  claim: Two lead-gen widgets sit side by side but do not share a component language — the left is a green-backed
    card with image and email opt-in, the right is a bare white calculator with a slider and large number
    output and no matching container.
  visible_tells:
  - 'Left: green card, protein-guide image, checkbox, email field with CTA'
  - 'Right: borderless white box with a slider, ''200 lbs / 30 lbs'' figures, and a green button — no
    card background to match the left'
  confidence: medium
- id: layout_09
  family: layout_composition_components
  polarity: mixed
  page_or_region: Homepage — 'Fridays Portal' feature block
  tile_path: store/joinfridays-com/captures/2026-06-16/tiles/homepage/tile-06-y07320.png
  claim: The portal block is a sound two-column text-left / phone-right layout but compositionally thin
    — the phone floats ungrounded in a large empty right column and the text column carries far more whitespace
    than the dense product sections around it.
  visible_tells:
  - Small phone mockup centered in a large empty right column with no background treatment
  - Three lines of copy plus a CTA leave conspicuous empty space below, unlike the packed sections above
  confidence: medium
- id: layout_10
  family: layout_composition_components
  polarity: mixed
  page_or_region: Weight_loss page — medication card grid breaks to 2-up
  tile_path: store/joinfridays-com/captures/2026-06-16/tiles/weight_loss/tile-01-y01220.png
  claim: The weight-loss medication grid is 2-column with tall cards and large vial photos, versus the
    3-column product rows on the homepage — the system adapts but the column-count change reads as inconsistent
    rather than an intentional breakpoint.
  visible_tells:
  - Two wide cards (Tirzepatide, Semaglutide) each with a full-bleed vial render filling roughly half
    the card
  - Homepage product rows use three equal cards in the same viewport width
  confidence: medium
  contrast_with: store/joinfridays-com/captures/2026-06-16/tiles/homepage/tile-01-y01220.png
- id: layout_12
  family: layout_composition_components
  polarity: poor
  page_or_region: Homepage / pricing — footer nav and contact cluster
  tile_path: store/joinfridays-com/captures/2026-06-16/tiles/homepage/tile-09-y10980.png
  claim: The footer is a single dot-separated row of seven nav items with the contact links and social
    icons in a free-floating right cluster — it lacks the column grid discipline the product sections
    show.
  visible_tells:
  - Seven nav items (Blog, GLP-1 Weight Loss, Longevity, GLP-1 Microdosing, Merch, Fridays Meals, Contact
    Us) in one row with dot separators, no grouping
  - Contact links and social icons sit as a right-aligned cluster with no enclosing column aligned to
    the nav
  confidence: medium
- id: layout_13
  family: layout_composition_components
  polarity: poor
  page_or_region: Testosterone page — crowded hero left column
  tile_path: store/joinfridays-com/captures/2026-06-16/tiles/testosterone/tile-00-y00000.png
  claim: The testosterone hero packs headline, subhead, offer line, red CTA, benefit bullets, and a Klarna
    badge into a tight left column beside an oversized vial render, producing a dense stack of small elements
    against very spacious product imagery.
  visible_tells:
  - Below the 'Use code BEGIN100' CTA, two benefit lines and a Klarna badge stack with minimal leading
  - The cramped left column contrasts sharply with the large, airy Testosterone Cypionate render filling
    the right half
  confidence: medium
- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: Homepage + category pages — per-vertical color-coding system
  tile_path: store/joinfridays-com/captures/2026-06-16/tiles/homepage/tile-07-y08540.png
  claim: Each product vertical owns a dedicated hue applied as a full-bleed section wash and carried down
    into its product cards — sage for GLP-1/weight loss, blue-teal for longevity, dusty rose-red for testosterone
    — making color a consistent navigational code, not a spot accent.
  visible_tells:
  - 'Testosterone section: warm rose-red wash with deep-red vials and cards matching it'
  - 'Longevity section (tile-04): cool blue-green wash with cards inheriting the same hue'
  - Hue transitions between sections are sharp and deliberate, not gradient bleed
  confidence: high
  contrast_with: store/joinfridays-com/captures/2026-06-16/tiles/homepage/tile-04-y04880.png
- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: Testosterone page — monochrome burgundy hero
  tile_path: store/joinfridays-com/captures/2026-06-16/tiles/testosterone/tile-00-y00000.png
  claim: The testosterone hero sustains one deep burgundy-red across background, product vials, and CTA
    with no competing accent — object color and accent color are the same hue, tightening brand coherence
    on this vertical.
  visible_tells:
  - Dark crimson hero background, Testosterone Cypionate vials, and the 'Use code BEGIN100' CTA all share
    the same red family
  - No off-hue accent intrudes on the fold
  confidence: high
  contrast_with: store/joinfridays-com/captures/2026-06-16/tiles/homepage/tile-01-y01220.png
- id: color_03
  family: color_brand_imagery
  polarity: strong
  page_or_region: Footer + in-body — 'fridays' wordmark
  tile_path: store/joinfridays-com/captures/2026-06-16/tiles/homepage/tile-08-y09760.png
  claim: A controlled lowercase serif 'fridays' wordmark is used consistently — reversed white-on-forest-green
    at display scale in the footer and embedded inside body headlines — reading as an owned brand mark
    rather than a generic logotype.
  visible_tells:
  - Large white 'fridays' wordmark on a deep forest-green footer block
  - Same custom serif appears inside in-body callouts ('Your fridays feeling awaits', tile-08) and repeated
    in the pricing footer
  confidence: high
  contrast_with: store/joinfridays-com/captures/2026-06-16/tiles/pricing/tile-05-y06100.png
- id: color_04
  family: color_brand_imagery
  polarity: strong
  page_or_region: Homepage hero — before/after photography treatment
  tile_path: store/joinfridays-com/captures/2026-06-16/tiles/homepage/tile-00-y00000.png
  claim: The before/after patient photos share an identical dark olive-green backdrop and matching full-body
    crop with branded yellow 'Before'/'After' pills — a controlled image language, not raw user-generated
    content.
  visible_tells:
  - Both photos share the same dark green-tinted backdrop and centered full-body framing
  - Yellow 'Before' and 'After' labels in identical rounded-pill format
  confidence: high
- id: color_05
  family: color_brand_imagery
  polarity: mixed
  page_or_region: Homepage — testimonial carousel mixes formats
  tile_path: store/joinfridays-com/captures/2026-06-16/tiles/homepage/tile-02-y02440.png
  claim: The 'Our success stories' carousel mixes produced before/after pairs with a dark unbranded TikTok-style
    video panel ('Tati'), breaking the otherwise controlled image language against the pale sage section.
  visible_tells:
  - Two styled before/after pairs flank a dark phone-style video thumbnail
  - The video panel is unbranded and dark, incongruous with the pale section background and color-coordinated
    cards beside it
  confidence: medium
  contrast_with: store/joinfridays-com/captures/2026-06-16/tiles/homepage/tile-00-y00000.png
- id: color_06
  family: color_brand_imagery
  polarity: mixed
  page_or_region: Homepage hero — coupon palette pulls toward bargain e-commerce
  tile_path: store/joinfridays-com/captures/2026-06-16/tiles/homepage/tile-00-y00000.png
  claim: The hero's right half places a functional coupon-code panel — promo pills, dollar-off tiers,
    and an amber 'BEST OFFER' badge — directly beside editorial content, pulling the otherwise restrained
    palette toward a discount-store aesthetic.
  visible_tells:
  - Light-green promo panel with pill-shaped codes (NEWYOU12, NYNY12) and an amber/gold 'BEST OFFER!'
    tag
  - The bargain-styled right half seams against the muted editorial left half
  confidence: high
  contrast_with: store/joinfridays-com/captures/2026-06-16/tiles/homepage/tile-04-y04880.png
- id: color_07
  family: color_brand_imagery
  polarity: mixed
  page_or_region: Weight_loss page — uneven step-card tints
  tile_path: store/joinfridays-com/captures/2026-06-16/tiles/weight_loss/tile-02-y02440.png
  claim: The three 'We make it easy' step cards stay in the sage family but darken progressively — Step
    03 renders as a much deeper forest green than Steps 01-02 — reading like an active/selected state
    that is never labeled.
  visible_tells:
  - 'Step 01: pale sage fill; Step 02: mid-tone sage; Step 03: noticeably darker forest green'
  - The darkest card draws the eye as if selected though no such state exists
  confidence: medium
- id: color_08
  family: color_brand_imagery
  polarity: poor
  page_or_region: Whats_included (Happy Sleep) — co-brand drops the hue system
  tile_path: store/joinfridays-com/captures/2026-06-16/tiles/whats_included/tile-00-y00000.png
  claim: The Happy Sleep co-branded page runs on a flat white/neutral background with no per-vertical
    brand wash, breaking from the hue-coding system used everywhere else on the site and reading as a
    different, off-system template.
  visible_tells:
  - Full white background through the visible tile with no sage, rose, teal, or forest wash
  - Only color present is the Trustpilot star orange and neutral UI chrome
  confidence: medium
  contrast_with: store/joinfridays-com/captures/2026-06-16/tiles/homepage/tile-07-y08540.png
- id: iconography_01
  family: iconography_illustration
  polarity: strong
  page_or_region: Homepage + category pages — 3-D product vial renders
  tile_path: store/joinfridays-com/captures/2026-06-16/tiles/weight_loss/tile-01-y01220.png
  claim: Compound-medication vials are rendered as high-quality 3-D objects with specular highlights,
    soft drop shadows, and labels wrapped onto curved glass — consistent lighting and shadow hold across
    multiple cards, indicating a controlled render pipeline well above flat stock-bottle photography.
  visible_tells:
  - Tirzepatide and Semaglutide renders share the same warm-green gradient background, lighting direction,
    and shadow depth
  - Labels sit on the curved glass rather than as flat overlays; highlights read as a dedicated render
    pass
  - Same render quality recurs on the pricing cards (tile-01) and homepage hero vials
  confidence: high
  contrast_with: store/joinfridays-com/captures/2026-06-16/tiles/pricing/tile-02-y02440.png
- id: iconography_02
  family: iconography_illustration
  polarity: strong
  page_or_region: Testosterone page — oversized hero vial render
  tile_path: store/joinfridays-com/captures/2026-06-16/tiles/testosterone/tile-00-y00000.png
  claim: The testosterone hero uses an oversized, dramatically lit 3-D vial render with bokeh depth of
    field and a metallic cap catching directional light — the highest-production-value product graphic
    on the site.
  visible_tells:
  - Two Testosterone Cypionate vials rendered large with warm lighting and background-bottle blur
  - The deep burgundy background is purpose-built for the render rather than a generic tile
  confidence: high
- id: iconography_03
  family: iconography_illustration
  polarity: poor
  page_or_region: Weight_loss / pricing — flat brand-name pen cutouts beside 3-D renders
  tile_path: store/joinfridays-com/captures/2026-06-16/tiles/weight_loss/tile-01-y01220.png
  claim: Brand-name medication images (Ozempic pen, Zepbound auto-injector) are flat photographic cutouts
    at smaller scale, stylistically inconsistent with the high-quality 3-D compound renders beside them,
    creating a visible two-tier product presentation.
  visible_tells:
  - Ozempic blue pen and Zepbound injector appear as plain cutouts with no render treatment, smaller than
    the adjacent compound vials
  - Same flat brand-name cutouts recur on the pricing page (tile-02), undermining visual parity with the
    compound renders
  confidence: high
  contrast_with: store/joinfridays-com/captures/2026-06-16/tiles/pricing/tile-02-y02440.png
- id: iconography_04
  family: iconography_illustration
  polarity: mixed
  page_or_region: Homepage — checklist tick icons
  tile_path: store/joinfridays-com/captures/2026-06-16/tiles/homepage/tile-01-y01220.png
  claim: Feature-list checkmarks are generic filled-circle ticks with no house styling — they function
    but add no visual character, the same default glyph found in most UI kits.
  visible_tells:
  - Small solid-circle check icons beside 'Dietitians', 'Live workouts', 'Support groups'
  - No stroke, weight, or corner-radius treatment distinguishes them from a stock icon set
  confidence: medium
- id: iconography_05
  family: iconography_illustration
  polarity: mixed
  page_or_region: Homepage — process steps rely on app screenshots, not custom glyphs
  tile_path: store/joinfridays-com/captures/2026-06-16/tiles/homepage/tile-05-y06100.png
  claim: The three-step flow is carried by numbered labels plus cropped app screenshots rather than purpose-drawn
    icons or illustrations — functional but not distinctively crafted.
  visible_tells:
  - Step headers '01/02/03' are typographic with no accompanying pictogram
  - Each step's visual is a cropped smartphone screenshot, not an original illustration
  confidence: medium
- id: iconography_06
  family: iconography_illustration
  polarity: poor
  page_or_region: Whats_included (Happy Sleep) — low-fidelity partner logo icon in table
  tile_path: store/joinfridays-com/captures/2026-06-16/tiles/whats_included/tile-01-y01220.png
  claim: The Happy Sleep comparison table uses a small dotted/pixelated logo mark as its column-header
    icon, reading as low-fidelity at display size against the otherwise clean table.
  visible_tells:
  - Happy Sleep header icon is a small dashed/dotted motif, not a crisp mark at this scale
  - The 'Typical Sleep Labs' and 'Other Home Tests' columns are text-only, making the branded icon feel
    like an afterthought
  confidence: medium
```

## Provenance

Mined blind from native-resolution tiles of five pages — homepage, pricing, weight-loss, testosterone, and whats-included (Happy Sleep) — sliced from the 2026-06-04 capture.

**QA — `recapture-used`.** Every page's cached hero tile carried a fixed `#cookie-consent-dialog` consent widget pinned bottom-right (a custom container shoot.py's vendor list didn't cover; that selector was added). All five pages were Tier-B re-rendered in system Chrome on 2026-06-16 (`scripts/shoot.py`, real WebGL + warm-scroll + motion-settle, no Firecrawl spend) — the widget is gone and the heroes are clean. Re-rendered tiles live under `captures/2026-06-16/tiles/`; drift vs. the cached shots is negligible (identical heroes, only a rotating hero word differs). No tiles excluded.

One mined card was dropped at synthesis as a capture artifact: a "truncated stats ticker" (homepage) — the value clipped at the viewport edge is an auto-scrolling marquee frozen mid-scroll, not a broken component.

Point-in-time snapshot: the live site changes; this reflects the captured/re-rendered tiles, not today's site.
