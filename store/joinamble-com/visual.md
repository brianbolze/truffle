---
schema_version: "1.0"
domain: joinamble.com
captured_at: 2026-06-15
source_capture: 2026-06-13
qa_status: clean
---

## Visual & brand impression

A confident roman/italic type signature runs as a deliberate system — upright lead clause, serif-italic tail — across hero, section and product headlines [typography_01][typography_02]. Beneath it sits a real component system: product heroes, step strips, 'Why Amble?' rows, FAQ and closing bands template verbatim page to page [layout_01][layout_05][layout_07], and a product-matched solid-color scheme (amber GLP-1, lavender NAD+) with a single composited-person-on-color convention gives coherent brand color [color_01][color_02], anchored by a custom 'Your Treatment' product-UI asset [iconography_02]. The finish lags the system: off-the-shelf and near-invisible spec icons [iconography_01][iconography_04], flat grey category cards that break the palette [color_05], a cramped undifferentiated trust bar [typography_05], and user-submitted before/after snapshots clashing with the polished imagery [color_03]. Controlled and templated; let down at the detail layer.

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: Roman/italic headline split — site-wide system (hero, section headings, FAQ heading)
  tile_path: store/joinamble-com/captures/2026-06-13/tiles/homepage/tile-00-y00000.png
  claim: 'A two-voice roman/italic split runs as a deliberate site-wide signature: the hero (''Anti-aging'' upright / ''made easy'' italic), section headings (''Doctor-trusted treatments, priced for you''), and the FAQ heading (''Your questions, answered.'') all italicize the closing phrase while the lead clause stays upright — a serif italic against an upright cut, repeated as a system rather than a one-off hero flourish.'
  visible_tells:
  - 'Hero headline splits mid-phrase: ''Anti-aging'' upright, ''made easy'' in lighter serif italic'
  - Same device recurs in 'priced for you' (section) and 'answered.' (FAQ heading), at a clear mid-display step below the hero
  - Italic phrase reads lighter, creating emphasis by style contrast rather than weight increase
  confidence: high
  contrast_with: store/joinamble-com/captures/2026-06-13/tiles/homepage/tile-05-y06100.png
- id: typography_02
  family: typography_hierarchy
  polarity: strong
  page_or_region: Product-page hero headline — GLP-1 / NAD+ / Sermorelin
  tile_path: store/joinamble-com/captures/2026-06-13/tiles/glp1/tile-00-y00000.png
  claim: Every product hero pairs a bold upright word ('Compounded GLP-1' / 'NAD+' / 'Sermorelin') with a large serif-italic word ('injections' / 'injection') at the same point size, so the contrast is style-only, not scale-based — a controlled two-register signature that repeats verbatim across all three product pages.
  visible_tells:
  - '''GLP-1'' upright vs ''injections'' italic render at matching display size — no scale step between them'
  - Identical upright/italic pairing recurs on NAD+ ('injection') and Sermorelin ('injection') heroes
  confidence: high
  contrast_with: store/joinamble-com/captures/2026-06-13/tiles/nad/tile-00-y00000.png
- id: typography_03
  family: typography_hierarchy
  polarity: mixed
  page_or_region: Homepage — stat callouts inside 'backed by data' banner
  tile_path: store/joinamble-com/captures/2026-06-13/tiles/homepage/tile-03-y03660.png
  claim: The four stat callouts ('Drop a clothing size', '33 lbs lost on average', etc.) pair a metric phrase with a small italic sub-label, but the metric-to-label hierarchy nearly collapses — the italic labels sit at almost the same visual weight as the figures, and a near-identical gray disclaimer line directly below competes with both.
  visible_tells:
  - Stat phrase and its italic sub-label sit close with insufficient size differential
  - Fine-print disclaimer immediately beneath uses the same gray tone as the labels, flattening three levels into one
  confidence: medium
- id: typography_04
  family: typography_hierarchy
  polarity: mixed
  page_or_region: Homepage — 'How it works' step cards
  tile_path: store/joinamble-com/captures/2026-06-13/tiles/homepage/tile-01-y01220.png
  claim: Step-card titles ('Free quiz, 100% online', 'Prescription') are bold but only marginally larger than their body copy, so weight carries all the differentiation and card-level hierarchy reads thin; the 'Step 1 / Step 2' ordinal labels are tiny mid-gray and recede to near-invisibility.
  visible_tells:
  - Card title and body copy are close in point size; bold alone separates them
  - '''Step N'' labels are small and low-contrast against the lavender card'
  confidence: medium
- id: typography_05
  family: typography_hierarchy
  polarity: poor
  page_or_region: Homepage — top trust/announcement bar
  tile_path: store/joinamble-com/captures/2026-06-13/tiles/homepage/tile-00-y00000.png
  claim: The top trust bar renders every item ('Free expedited delivery', 'No hidden fees', '100,000+ members', etc.) at identical small size, weight, and color with icon separators — zero internal hierarchy, and it sits flush above the nav with no breathing room, making the very top of the page feel cramped and undifferentiated from the nav.
  visible_tells:
  - All bar items share one type size, weight, and gray tone; no item elevated
  - Bar abuts the nav directly with no vertical separation
  confidence: high
- id: typography_06
  family: typography_hierarchy
  polarity: strong
  page_or_region: Footer — across all pages
  tile_path: store/joinamble-com/captures/2026-06-13/tiles/nad/tile-05-y05855.png
  claim: Footer column headers ('Treatments', 'Tools', 'Amble') sit a step heavier than the link lists beneath them, giving a clean two-level hierarchy that holds as white-on-near-black; links are evenly leaded and legible.
  visible_tells:
  - Headers visibly heavier than the link items below
  - Both levels hold adequate contrast on the dark footer ground
  confidence: high
- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: Product-detail hero — GLP-1 / NAD+ / Sermorelin
  tile_path: store/joinamble-com/captures/2026-06-13/tiles/glp1/tile-00-y00000.png
  claim: The product hero is a consistent two-column split — large rounded color-field product image left (~55%), structured purchase panel right (~45%) carrying title, feature-icon grid, pricing table and CTA — holding identical proportions, padding and component order across all three product pages. A real component system, not page-by-page layout.
  visible_tells:
  - Same left/right proportions, 'HSA & FSA eligible' pill top-left, payment-badge row, 2x2 feature icons, 4-row price table, dark CTA — in the same order on GLP-1, NAD+ and Sermorelin
  - Spatial layout is pixel-equivalent across the three heroes with only product/copy swapped
  confidence: high
  contrast_with: store/joinamble-com/captures/2026-06-13/tiles/nad/tile-00-y00000.png
- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: Homepage — category card row (Weight loss / Anti-aging / Skin)
  tile_path: store/joinamble-com/captures/2026-06-13/tiles/homepage/tile-00-y00000.png
  claim: The three category cards sit in a uniform three-column grid with matched card height, even gutters, and an identical dark circular arrow badge in each bottom-right corner — disciplined card-component reuse above the fold.
  visible_tells:
  - Three equal-width cards with matched circular arrow badges bottom-right
  - Gutters and card heights visually even across all three
  confidence: high
- id: layout_03
  family: layout_composition_components
  polarity: strong
  page_or_region: Homepage + product pages — 'How it works' step strip
  tile_path: store/joinamble-com/captures/2026-06-13/tiles/homepage/tile-01-y01220.png
  claim: The 'How it works' step strip (quiz / prescription / delivery / support) deploys as a matched card row with consistent icon position, 'Step N' label placement, body copy and inline CTA on both the homepage and each product page — a shared reusable section.
  visible_tells:
  - Same card height, lavender icon tile, and 'Step N' label placement across homepage and the sermorelin step strip
  - Consistent rounded-square icon containers and 'Get started' affordance across instances
  confidence: high
  contrast_with: store/joinamble-com/captures/2026-06-13/tiles/sermorelin/tile-01-y01220.png
- id: layout_04
  family: layout_composition_components
  polarity: strong
  page_or_region: Homepage — full-bleed metric banners (orange / purple / green sequence)
  tile_path: store/joinamble-com/captures/2026-06-13/tiles/homepage/tile-02-y02440.png
  claim: The stacked full-bleed stat banners share one compositional template — italic-accented headline top-left, 'Get Started' pill top-right, composited person at center/right, and a row of stat pills along the bottom — producing a coherent scrollable sequence rather than ad-hoc sections.
  visible_tells:
  - '''Weight loss, backed by data'' headline anchored top-left; pill CTA top-right'
  - Same headline/CTA/photo/stat-pill arrangement carries into the adjacent green and purple bands
  confidence: high
  contrast_with: store/joinamble-com/captures/2026-06-13/tiles/homepage/tile-03-y03660.png
- id: layout_05
  family: layout_composition_components
  polarity: strong
  page_or_region: Product pages — 'Why Amble?' three-card trust row
  tile_path: store/joinamble-com/captures/2026-06-13/tiles/glp1/tile-04-y04880.png
  claim: '''Why Amble?'' presents three equal-height cards (Doctor-trusted medication / Licensed physicians / On-going support) each with a top label, a nested UI-mockup illustration, and body copy — pixel-equivalent structure across GLP-1, NAD+ and Sermorelin with only the product-specific mockup swapped.'
  visible_tells:
  - Card borders, title position, illustration zone and body area align across all three product pages
  - Three equal-width columns with consistent internal padding; only the 'Your Treatment' mockup name changes (GLP-1 / NAD+ / Sermorelin)
  confidence: high
  contrast_with: store/joinamble-com/captures/2026-06-13/tiles/sermorelin/tile-02-y02440.png
- id: layout_06
  family: layout_composition_components
  polarity: strong
  page_or_region: All pages — FAQ accordion section
  tile_path: store/joinamble-com/captures/2026-06-13/tiles/homepage/tile-05-y06100.png
  claim: The FAQ accordion is identical across pages — full-width pale rows, left-aligned question, right-aligned '+' affordance, even row height, with a 'Still have questions? / Send us a message' dark pill beneath — a tightly controlled shared component.
  visible_tells:
  - Row height, fill, and '+' alignment match across homepage, GLP-1 and Sermorelin FAQ tiles
  - Same 'Send us a message' pill below the list on every instance
  confidence: high
  contrast_with: store/joinamble-com/captures/2026-06-13/tiles/glp1/tile-06-y07320.png
- id: layout_07
  family: layout_composition_components
  polarity: strong
  page_or_region: All pages — closing CTA band + dark footer
  tile_path: store/joinamble-com/captures/2026-06-13/tiles/nad/tile-05-y05855.png
  claim: Every page closes with the same floating rounded-corner color band (heart-icon top-left, italic-accented tagline + sub-line bottom-left, white 'Get Started' pill bottom-right, composited woman emerging from the field) followed by the same dark three-column footer with logo and payment-icon row — end-to-end template consistency even though the band's hue and copy change per page.
  visible_tells:
  - Identical band geometry, heart icon, tagline placement and white CTA pill on NAD+ and Sermorelin closers (coral 'Ready to recharge…')
  - 'Footer: Treatments/Tools/Amble columns + logo + payment icons at the same proportions on every page'
  confidence: high
  contrast_with: store/joinamble-com/captures/2026-06-13/tiles/sermorelin/tile-04-y04880.png
- id: layout_08
  family: layout_composition_components
  polarity: mixed
  page_or_region: Homepage — 'Doctor-trusted treatments' product carousel
  tile_path: store/joinamble-com/captures/2026-06-13/tiles/homepage/tile-01-y01220.png
  claim: The treatment carousel shows four equal-width cards with paired 'Get started' / 'Learn more' CTAs, but the vial photos sit at noticeably different crop heights and visual weights within the cards, slightly undermining the uniformity the grid promises.
  visible_tells:
  - Vial images vary in vertical position and size from card to card
  - Inconsistent whitespace above the CTA pair across cards
  confidence: medium
- id: layout_09
  family: layout_composition_components
  polarity: mixed
  page_or_region: Homepage — 'Real people, real results' testimonial row
  tile_path: store/joinamble-com/captures/2026-06-13/tiles/homepage/tile-04-y04880.png
  claim: The before/after testimonial cards force equal height over photos of inconsistent crop and framing, so portraits range from tight chin-crops to full torso and quoted copy of varying length leaves uneven bottom padding across the row.
  visible_tells:
  - Some portraits cropped tight, others show full torso — uneven visual weight across the row
  - Testimonial quotes of different lengths produce ragged bottom padding
  confidence: medium
- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: Product pages — product-matched solid color field
  tile_path: store/joinamble-com/captures/2026-06-13/tiles/glp1/tile-00-y00000.png
  claim: 'Each product hero uses a flat solid background that matches its vial: GLP-1 on amber/orange (vial label amber), NAD+ and Sermorelin on lavender (vial label lavender) — an intentional color-coding system where the product is the color, with no gradient or photography diluting it.'
  visible_tells:
  - Amber vial on a flat amber field; the lavender NAD+/Sermorelin vials sit on matching lavender fields
  - Background is untextured solid, reading as a deliberate system not filler
  confidence: high
  contrast_with: store/joinamble-com/captures/2026-06-13/tiles/nad/tile-00-y00000.png
- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: Section banners — composited-person-on-color convention
  tile_path: store/joinamble-com/captures/2026-06-13/tiles/homepage/tile-02-y02440.png
  claim: 'Imagery follows one consistent convention site-wide: a single person, cut from their original background and composited onto a flat brand-color field with a faint radial-line texture behind them — repeated across violet, amber, green and coral bands. A controlled palette of solid hues, each reserved to one banner role.'
  visible_tells:
  - Man in grey shirt composited onto an amber field with visible radial-line texture
  - Same treatment recurs on the green band (sermorelin) and coral band (nad/sermorelin closer), each hue used in one role only
  confidence: high
  contrast_with: store/joinamble-com/captures/2026-06-13/tiles/nad/tile-05-y05855.png
- id: color_03
  family: color_brand_imagery
  polarity: mixed
  page_or_region: Homepage — 'Real people, real results' before/after grid
  tile_path: store/joinamble-com/captures/2026-06-13/tiles/homepage/tile-04-y04880.png
  claim: The before/after section breaks from the controlled brand image language with unretouched user-submitted snapshots of variable lighting, angle and quality — selfies and candid mirror shots — which clash against the polished composited photography used everywhere else.
  visible_tells:
  - Portrait pairs differ in lighting, camera angle and image quality card to card
  - No consistent background or staging — stark break from the solid-field composites above and below
  confidence: high
  contrast_with: store/joinamble-com/captures/2026-06-13/tiles/homepage/tile-02-y02440.png
- id: color_04
  family: color_brand_imagery
  polarity: mixed
  page_or_region: Product photography — studio vial render
  tile_path: store/joinamble-com/captures/2026-06-13/tiles/glp1/tile-00-y00000.png
  claim: The vial-and-syringe render is clean and templated but is a generic category composition — identical angle, shadow style and syringe placement across GLP-1, NAD+ and Sermorelin (only the tint changes), competent but not a distinctive owned visual vocabulary.
  visible_tells:
  - GLP-1 vial+syringe on amber repeats verbatim as lavender NAD+ and Sermorelin shots — same angle, same shadow, same syringe position
  - Composition is the common telehealth vial-prop convention
  confidence: medium
  contrast_with: store/joinamble-com/captures/2026-06-13/tiles/sermorelin/tile-00-y00000.png
- id: color_05
  family: color_brand_imagery
  polarity: poor
  page_or_region: Homepage — category cards on plain grey
  tile_path: store/joinamble-com/captures/2026-06-13/tiles/homepage/tile-00-y00000.png
  claim: The three above-the-fold category cards show bottles on plain light-grey fields with no color treatment, no person, and no link to the vivid brand palette used everywhere below — they read as e-commerce default styling, a flat opening note against the saturated bands that follow.
  visible_tells:
  - '''Weight loss'', ''Anti aging'', ''Skin'' each on a flat grey-white field — no banner color, no texture, no model'
  - Stark contrast with the solid-color composites immediately below
  confidence: high
  contrast_with: store/joinamble-com/captures/2026-06-13/tiles/homepage/tile-02-y02440.png
- id: iconography_01
  family: iconography_illustration
  polarity: mixed
  page_or_region: Outline icon set — top trust bar and 'How it works' steps
  tile_path: store/joinamble-com/captures/2026-06-13/tiles/homepage/tile-00-y00000.png
  claim: The system-level glyphs — the trust-bar set (truck, dollar, lock, diamond, globe, cross) and the 'How it works' step icons (clipboard, Rx pill, box, headset) in lavender rounded-square tiles — are consistent in stroke weight and container but read as off-the-shelf library icons dropped in, not drawn to fit.
  visible_tells:
  - Six evenly spaced outline icons in the trust bar, uniform stroke; diamond/globe are stock metaphors
  - Step glyphs sit in matching lavender rounded-square tiles but the forms match common UI icon libraries
  confidence: high
- id: iconography_02
  family: iconography_illustration
  polarity: strong
  page_or_region: Product pages — 'Your Treatment' UI-mockup illustration inside 'Why Amble?' card
  tile_path: store/joinamble-com/captures/2026-06-13/tiles/glp1/tile-04-y04880.png
  claim: The 'Doctor-trusted medication' card holds a purpose-built product-UI graphic — a white 'Your Treatment / GLP-1 Injection' card with a brand-tinted vial and a green 'Received' check badge — a custom asset, not a generic icon, and it templates cleanly with the product name swapped (NAD+ Injection, Sermorelin) per page.
  visible_tells:
  - Nested white mockup with tinted vial, 'Received' check badge and label copy
  - Same mockup re-rendered as 'NAD+ Injection' and 'Sermorelin' on respective pages, confirming a templated component
  confidence: high
  contrast_with: store/joinamble-com/captures/2026-06-13/tiles/sermorelin/tile-02-y02440.png
- id: iconography_03
  family: iconography_illustration
  polarity: mixed
  page_or_region: NAD+ / Sermorelin — translucent ghost-glyph benefits strip
  tile_path: store/joinamble-com/captures/2026-06-13/tiles/sermorelin/tile-02-y02440.png
  claim: 'The benefits strip layers large semi-transparent glyphs behind the label text on a deep-purple band (Sermorelin: heartbeat, dumbbell, flame, clock; NAD+: equivalent set) — a deliberate depth treatment beyond flat icon placement, but the glyphs vary in line weight (the heartbeat/waveform reads noticeably thinner than its neighbors), showing minor system inconsistency.'
  visible_tells:
  - Four benefit panels each with a large ghosted glyph watermarked behind the label
  - Waveform glyph is visibly thinner-stroked than the dumbbell/flame/clock beside it
  confidence: medium
  contrast_with: store/joinamble-com/captures/2026-06-13/tiles/nad/tile-02-y02440.png
- id: iconography_04
  family: iconography_illustration
  polarity: poor
  page_or_region: Product pages — tiny low-contrast outline icons (spec grid + card corners)
  tile_path: store/joinamble-com/captures/2026-06-13/tiles/glp1/tile-00-y00000.png
  claim: 'The functional outline icons are generic and near-invisible: the 2x2 spec grid (headset / circle / shield / dollar beside ''Unlimited 24/7 support'', ''No hidden fees'', etc.) and the top-right corner glyphs on the ''Why Amble?'' cards are tiny light-gray strokes that add no design energy and are indistinguishable from any free icon library at reading distance.'
  visible_tells:
  - Four small gray spec icons in a 2x2 grid under the product title, headset/dollar glyphs are library defaults
  - Top-right card icons (cross, badge, headset) are ~16px light-gray and nearly disappear on white
  confidence: high
  contrast_with: store/joinamble-com/captures/2026-06-13/tiles/glp1/tile-04-y04880.png
- id: iconography_05
  family: iconography_illustration
  polarity: mixed
  page_or_region: Homepage — stat overlays on the 'backed by data' banner
  tile_path: store/joinamble-com/captures/2026-06-13/tiles/homepage/tile-02-y02440.png
  claim: The stat overlays on the amber banner are purely typographic pill/badge labels (e.g. '222 lbs > 189 lbs', '33 lbs') with minimal iconography and no charted data encoding — the approach sidesteps chart-craft entirely rather than attempting a data graphic.
  visible_tells:
  - Numeric values shown in pill/badge shapes over the orange field, no bar or line chart
  - Before/after rendered as a simple '> ' arrow pill, not a visual encoding
  confidence: high
```

## Provenance

Tiles read: homepage (7) + glp1 (8) + nad (6) + sermorelin (6) from `captures/2026-06-13/tiles/` — all 27 active, no exclusions, no Tier-B re-render (the cached Firecrawl capture was clean). Mined blind + judged per [`/visual-evidence`](../../skills/visual-evidence/SKILL.md): four family miners (Sonnet) saw only the tiles (no dossier, no web), the judge (Opus) pruned 41 raw cards to 26 — 11 merges plus corrections for three tile misattributions (a misplaced typography card, a "locked cross-page CTA" that is actually coral-and-different per page, and a "plain white" section that sits on a gradient) and weak/duplicate tells. One further card dropped at synthesis — a layout card whose "model cropped at the tile edge" tell was a tiling-cut artifact, not a design defect — leaving 25. Capture caveat: the homepage metric banners (tile-02/03) render with faint radial-line texture and motion-state overlays; tells were drawn only from stable, clearly visible structure. Snapshot caveat: reflects the 2026-06-13 capture; the live site changes.
