---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.0"
domain: agentislongevity.com
captured_at: 2026-06-25
source_capture: 2026-06-25
qa_status: clean
---

## Visual & brand impression

A premium, editorial brand with real craft in its marketing layer: confident serif-display headlines over spaced small-caps overlines build clean multi-level hierarchy [typography_01, typography_03, typography_04], carried by a disciplined layout system — split hero, staggered photo mosaic, contained two-column panels, and a reusable dark CTA/footer [layout_01, layout_02, layout_03, layout_04]. A cohesive teal accent unifies site and product, where the Longevity Quotient dial and input-to-domain flow diagram are the craft high point [color_01, iconography_01, iconography_02]. It slips in the denser dark sections: hierarchy flattens as sizes converge [typography_06, typography_07], clinic cards set low-contrast text on teal [typography_08], and the icon set, metric charts, and a cliche dark-forest fill read generic [iconography_05, iconography_06, color_06].

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: homepage hero
  tile_path: store/agentislongevity-com/captures/2026-06-25/tiles/homepage/tile-00-y00000.png
  claim: 'Hero sets a clear two-level type hierarchy: a large serif display headline (''Driving the standard
    in longevity care.'') roughly 3-4x the size of the lighter body copy beneath, with strong size and
    weight contrast.'
  visible_tells:
  - Large serif headline dominates the lower-left of the hero
  - Body copy sits visibly smaller and lighter directly below with a clear size gap
  confidence: high
  contrast_with: store/agentislongevity-com/captures/2026-06-25/tiles/homepage/tile-03-y03660.png
- id: typography_02
  family: typography_hierarchy
  polarity: strong
  page_or_region: homepage dark CTA + footer
  tile_path: store/agentislongevity-com/captures/2026-06-25/tiles/homepage/tile-07-y07804.png
  claim: 'On the dark CTA panel a three-level hierarchy holds cleanly: large centered display headline
    (''Ready to see what the platform looks like for your practice?''), a smaller body line, and a spaced
    small-caps stat row at the bottom, none competing.'
  visible_tells:
  - Display headline clearly dominant and centered
  - Body subtitle noticeably smaller with comfortable leading
  - Spaced small-caps stat row ('PE-BACKED BY SHORE CAPITAL', '$17M+ COMMITTED CAPITAL', etc.) reads as
    a distinct subordinate level
  confidence: high
- id: typography_03
  family: typography_hierarchy
  polarity: strong
  page_or_region: homepage 'How It Works' section
  tile_path: store/agentislongevity-com/captures/2026-06-25/tiles/homepage/tile-01-y01220.png
  claim: 'Section runs a deliberate three-level system: a spaced small-caps overline (''HOW IT WORKS''),
    a large display headline (''Your path to a longer, healthier life starts here.''), and small step
    labels beneath the cards, guiding scan without noise.'
  visible_tells:
  - Spaced all-caps overline clearly distinguished from the headline below
  - Step card labels sit at a third, noticeably smaller size
  confidence: high
- id: typography_04
  family: typography_hierarchy
  polarity: strong
  page_or_region: longevity_quotient hero
  tile_path: store/agentislongevity-com/captures/2026-06-25/tiles/longevity_quotient/tile-00-y00000.png
  claim: White serif headline ('Your annual physical can't tell you how fast you're aging.') over the
    dark lifestyle photo reads instantly with strong contrast; the subhead drops in size and weight in
    one controlled step.
  visible_tells:
  - White headline against dark photo is fully legible with no legibility issues
  - Subhead is visibly smaller and lighter, cleanly separated
  confidence: high
- id: typography_05
  family: typography_hierarchy
  polarity: strong
  page_or_region: about page 'How We Work' values list
  tile_path: store/agentislongevity-com/captures/2026-06-25/tiles/about/tile-01-y01220.png
  claim: The 'How We Work' values list uses single-letter initials (I, M, P, A, C...) at display size
    paired with regular-weight labels ('Integrity in Practice', 'Mission for Excellence', etc.), creating
    a distinct typographic pattern for the content type.
  visible_tells:
  - Single-letter initials read at display size as left-column anchors
  - Adjacent label text is clearly body weight, not competing with the initials
  confidence: high
- id: typography_06
  family: typography_hierarchy
  polarity: mixed
  page_or_region: boundless_protocols dark intro stack
  tile_path: store/agentislongevity-com/captures/2026-06-25/tiles/boundless_protocols/tile-01-y01220.png
  claim: On the dark intro, the stacked menu ('The Score / The Domains / Your status / Tracking') renders
    all four lines at near-identical size and weight, collapsing the intended primary-vs-secondary distinction
    between levels.
  visible_tells:
  - Four stacked items share similar size and weight with no clear lead level
  - Overline label ('YOUR LONGEVITY QUOTIENT') is small and faint, weak as a section anchor
  confidence: medium
  contrast_with: store/agentislongevity-com/captures/2026-06-25/tiles/homepage/tile-07-y07804.png
- id: typography_07
  family: typography_hierarchy
  polarity: mixed
  page_or_region: homepage 'Our Approach' feature list
  tile_path: store/agentislongevity-com/captures/2026-06-25/tiles/homepage/tile-03-y03660.png
  claim: The left feature column sets the lead label ('Founder-Focused Approach') and the sibling items
    ('Actionable Clinical Data', 'Integrated Care Platform') at near-equal size and weight, weakening
    the step between the section lead and the items it introduces.
  visible_tells:
  - Lead feature label and the list items are set at near-equal size
  - No clear weight or size step separates the active item from the muted ones below
  confidence: medium
- id: typography_08
  family: typography_hierarchy
  polarity: mixed
  page_or_region: partners page clinic location cards (dark)
  tile_path: store/agentislongevity-com/captures/2026-06-25/tiles/partners/tile-03-y03660.png
  claim: Clinic location cards set city names and description copy in low-contrast light-on-dark-teal,
    so the label-to-description hierarchy is faint and the blurb nearly blends into the card background
    at reading distance.
  visible_tells:
  - City names ('Orlando, FL', 'Lake Mary, FL') are small light text on dark teal with reduced legibility
  - Description text below blends into the dark background
  confidence: medium
- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: homepage hero
  tile_path: store/agentislongevity-com/captures/2026-06-25/tiles/homepage/tile-00-y00000.png
  claim: 'Hero uses a confident split composition: full-bleed editorial photo, headline and CTA anchored
    bottom-left, three stat counters stacked top-right, with no crowding or alignment drift between zones.'
  visible_tells:
  - Headline flush to a clear left margin with generous breathing room
  - Three stat counters (14, 10+, 3,300+) in a clean right-column vertical stack
  - Nav items and CTA pill evenly spaced with no collision
  confidence: high
- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: homepage photo mosaic section
  tile_path: store/agentislongevity-com/captures/2026-06-25/tiles/homepage/tile-01-y01220.png
  claim: The editorial photo mosaic uses deliberate size variation and asymmetric staggering for rhythm
    while holding structural order; the centered headline-and-body block floats cleanly within it without
    touching any image edge.
  visible_tells:
  - Multiple image sizes arranged in an offset grid, not a uniform gallery
  - Center text block sits in a clean reserved gutter between image clusters
  - Gutter spacing between tiles is consistent across rows
  confidence: high
  contrast_with: store/agentislongevity-com/captures/2026-06-25/tiles/about/tile-04-y04880.png
- id: layout_03
  family: layout_composition_components
  polarity: strong
  page_or_region: homepage 'Our Approach' two-column panel
  tile_path: store/agentislongevity-com/captures/2026-06-25/tiles/homepage/tile-03-y03660.png
  claim: The 'Our Approach' section is a disciplined two-column split (left feature list, right editorial
    image with an inline +84% data card) inside a contained off-white rounded panel inset from the page
    edges.
  visible_tells:
  - Feature labels align to a consistent left text margin
  - Image panel with the +84% overlay card sits flush to the right column boundary
  - Rounded-corner container is inset from both page edges
  confidence: high
- id: layout_04
  family: layout_composition_components
  polarity: strong
  page_or_region: CTA + footer system (homepage)
  tile_path: store/agentislongevity-com/captures/2026-06-25/tiles/homepage/tile-07-y07804.png
  claim: 'The dark CTA block and footer read as a reusable, pixel-consistent component system: centered
    CTA with a metrics strip, then a well-structured multi-column footer separated by generous whitespace.'
  visible_tells:
  - Stat strip (PE-backed / capital / clinics / markets / patients) evenly spaced with pipe dividers
  - Footer columns (Explore / More / Get in Touch) align on a shared baseline with uniform gaps
  - '''Great Place to Work Certified'' badge contained in its own bordered pill'
  confidence: high
- id: layout_05
  family: layout_composition_components
  polarity: strong
  page_or_region: boundless_protocols domain-score grid (dark UI card)
  tile_path: store/agentislongevity-com/captures/2026-06-25/tiles/boundless_protocols/tile-02-y02440.png
  claim: 'The 8-domain score grid inside the dark UI card is tightly structured: a 2-column layout with
    consistent card heights and a repeated label + status-tag pattern across all eight cells with no visible
    misalignment.'
  visible_tells:
  - Eight domain cells (Hormone, Metabolic, Nutrition, Cognitive, Physical, Cardiovascular, Organ, Emotional
    Wellness) in an even grid with matching gutters
  - Each cell repeats the same label + tag layout
  - Card borders and corner radii consistent across all cells
  confidence: high
- id: layout_06
  family: layout_composition_components
  polarity: strong
  page_or_region: boundless_protocols 'What you receive' 6-panel grid
  tile_path: store/agentislongevity-com/captures/2026-06-25/tiles/boundless_protocols/tile-06-y07320.png
  claim: The six-panel feature grid uses a systematic card layout with consistent numbered badges, content
    blocks, and left-aligned title/body across all panels, reading as a mature component rather than one-off
    sections.
  visible_tells:
  - Six panels in a 2x3 grid with matching internal padding
  - Numbered badges consistently placed at the top-left of each panel
  - Titles align to the same left margin across all six cards
  confidence: high
- id: layout_07
  family: layout_composition_components
  polarity: mixed
  page_or_region: homepage testimonial / social-proof collage
  tile_path: store/agentislongevity-com/captures/2026-06-25/tiles/homepage/tile-05-y06100.png
  claim: The testimonial section layers overlapping quote cards, portraits, and a floating +84% stat card
    in a collage that reads energetic but loosens grid discipline; some cards sit at differing sizes and
    offsets with no shared anchor.
  visible_tells:
  - Quote cards and portrait photos overlap at uneven offsets
  - Floating +84% bar-chart card has no clear anchor to surrounding content
  - Portrait/card sizes are not uniform
  confidence: medium
- id: layout_08
  family: layout_composition_components
  polarity: mixed
  page_or_region: partners page clinic-listing stretch
  tile_path: store/agentislongevity-com/captures/2026-06-25/tiles/partners/tile-03-y03660.png
  claim: Across the clinic-listing scroll the cards are constrained to the right ~45% of a wide dark canvas,
    leaving the left half an empty dark void with no balancing element, producing a lopsided composition.
  visible_tells:
  - Location cards (Orlando, Lake Mary, etc.) sit only in the right portion of the tile
  - Left half is undifferentiated dark background with no content
  - No visible left-column element explains the asymmetry on this tile
  confidence: high
  contrast_with: store/agentislongevity-com/captures/2026-06-25/tiles/partners/tile-05-y06100.png
- id: layout_09
  family: layout_composition_components
  polarity: mixed
  page_or_region: about page leadership team grid
  tile_path: store/agentislongevity-com/captures/2026-06-25/tiles/about/tile-04-y04880.png
  claim: The leadership grid uses consistent card structure (photo, name, title) but the 7-person count
    breaks 4+3, leaving the second row left-aligned with roughly a card-width of empty space on the right.
  visible_tells:
  - Top row has four equal-width portrait cards filling the container
  - Bottom row has only three cards aligned left with visible empty space on the right
  confidence: high
  contrast_with: store/agentislongevity-com/captures/2026-06-25/tiles/boundless_protocols/tile-06-y07320.png
- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: teal accent system across hero, dark CTA, and LQ product UI
  tile_path: store/agentislongevity-com/captures/2026-06-25/tiles/homepage/tile-00-y00000.png
  claim: 'A single teal-green accent is introduced in the hero CTA/nav pill and then sustained as a system:
    deployed at section-fill scale in the dark forest-teal CTA module and footer, and carried into product
    UI on the LQ score interface, always the same hue stepped in lightness with no competing color introduced.'
  visible_tells:
  - Hero 'Find a Clinic' pill is the only saturated element in a near-monochrome hero; nav CTA echoes
    the same teal
  - Dark CTA + footer fill use the same dark-teal as a structural color, with the 'Start the Conversation'
    button a lighter step of the same hue
  - On the LQ panel the circular score arc uses that same lighter teal on dark-teal, extending the palette
    into UI
  confidence: high
  contrast_with: store/agentislongevity-com/captures/2026-06-25/tiles/homepage/tile-07-y07804.png
- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: homepage mosaic image grid
  tile_path: store/agentislongevity-com/captures/2026-06-25/tiles/homepage/tile-01-y01220.png
  claim: 'The multi-image mosaic is tightly color-graded: every thumbnail shares a desaturated cool-green-to-teal
    tonal range, reading as curated rather than an assembled stock dump.'
  visible_tells:
  - Forest, skin, water, and fabric thumbnails all share the same muted-cool grade
  - No image introduces a warm yellow, red, or vibrant blue that would break the tonal contract
  confidence: high
- id: color_03
  family: color_brand_imagery
  polarity: mixed
  page_or_region: coral/salmon secondary status color (boundless dashboard + partners stat card)
  tile_path: store/agentislongevity-com/captures/2026-06-25/tiles/boundless_protocols/tile-02-y02440.png
  claim: A muted salmon/coral surfaces as the only secondary hue beyond teal, used narrowly for status
    tags in the protocol dashboard and for one bar chart on the partners page, but its appearances are
    isolated enough that it reads as an ad hoc accent rather than a system color.
  visible_tells:
  - Small status tags in the eight-domain dashboard appear in a muted coral against teal
  - On partners the bar chart uses a single salmon bar among grey while the sibling stat cards carry no
    such color
  confidence: medium
  contrast_with: store/agentislongevity-com/captures/2026-06-25/tiles/partners/tile-02-y02440.png
- id: color_04
  family: color_brand_imagery
  polarity: mixed
  page_or_region: longevity_quotient test photography
  tile_path: store/agentislongevity-com/captures/2026-06-25/tiles/longevity_quotient/tile-03-y03660.png
  claim: Clinical test photography is near black-and-white and fits the editorial tone, but adjacent test
    entries are full-color gym and grip-strength shots, so the page mixes monochrome and color imagery
    without a unifying grade.
  visible_tells:
  - Blood-draw and cognitive-test images render near black-and-white
  - Neighboring tile has full-color InBody/gym and warm-lit grip-strength shots without the same treatment
  confidence: medium
  contrast_with: store/agentislongevity-com/captures/2026-06-25/tiles/longevity_quotient/tile-04-y04880.png
- id: color_05
  family: color_brand_imagery
  polarity: mixed
  page_or_region: about page leadership headshots
  tile_path: store/agentislongevity-com/captures/2026-06-25/tiles/about/tile-04-y04880.png
  claim: Leadership headshots are plainly lit on neutral light studio backgrounds with no brand-consistent
    grade, reading as standard corporate portraits that drop the cool, cinematic register the rest of
    the site holds.
  visible_tells:
  - Headshots use warm-neutral / light studio backdrops, no teal or brand treatment
  - Marked contrast with the hero and LQ pages where imagery shares a cool cinematic grade
  confidence: high
  contrast_with: store/agentislongevity-com/captures/2026-06-25/tiles/longevity_quotient/tile-00-y00000.png
- id: color_06
  family: color_brand_imagery
  polarity: poor
  page_or_region: about page dark-forest full-bleed section
  tile_path: store/agentislongevity-com/captures/2026-06-25/tiles/about/tile-02-y02440.png
  claim: A moody dark-forest photo runs full-bleed behind 'Our platform is built for scale.' but has no
    subject or compositional link to the copy, reading as a generic wellness/premium nature texture fill
    rather than an owned brand visual.
  visible_tells:
  - Tall dark tree canopy fills the section with no focal subject tied to the headline
  - The dark-forest texture is a common premium-brand cliche with no distinctive ownership
  confidence: medium
- id: iconography_01
  family: iconography_illustration
  polarity: strong
  page_or_region: longevity_quotient LQ score dial
  tile_path: store/agentislongevity-com/captures/2026-06-25/tiles/longevity_quotient/tile-01-y01220.png
  claim: 'The circular LQ score dial is a bespoke on-brand product graphic: a clean arc with a large central
    ''78'' in white on near-black with a teal accent arc, no charting-library tick marks or labels crowding
    the face.'
  visible_tells:
  - Circular arc gauge with centered '78' numeral in white on dark, teal accent arc, no default chart
    decoration
  confidence: high
  contrast_with: store/agentislongevity-com/captures/2026-06-25/tiles/boundless_protocols/tile-00-y00000.png
- id: iconography_02
  family: iconography_illustration
  polarity: strong
  page_or_region: longevity_quotient input-to-domain flow diagram
  tile_path: store/agentislongevity-com/captures/2026-06-25/tiles/longevity_quotient/tile-05-y06100.png
  claim: The curved-line mapping diagram connecting five inputs (Blood panel, Cardiometabolic, Cognivue,
    InBody, Grip-strength) to eight output domains is a custom, purposefully sparse data visualization,
    not a chart-library default.
  visible_tells:
  - Fine white curved lines on near-black fan from left input labels to right domain labels with no axes,
    gridlines, or decoration; purely topological routing
  confidence: high
- id: iconography_03
  family: iconography_illustration
  polarity: mixed
  page_or_region: longevity_quotient LQ benchmark key
  tile_path: store/agentislongevity-com/captures/2026-06-25/tiles/longevity_quotient/tile-01-y01220.png
  claim: The three-tier benchmark key (70+, 70, Below 70) uses consistent pill-shaped rows with teal left-edge
    accents, a small but legible designed component rather than plain list text.
  visible_tells:
  - Three horizontal pill rows on dark, each with a teal left-bar accent and right-aligned label, evenly
    spaced and weighted
  confidence: medium
- id: iconography_04
  family: iconography_illustration
  polarity: mixed
  page_or_region: longevity_quotient body-systems grid
  tile_path: store/agentislongevity-com/captures/2026-06-25/tiles/longevity_quotient/tile-02-y02440.png
  claim: The eight body-system markers are small square photographic crops (skin, cells, tissue) rather
    than a drawn icon system; each cell is a different macro photo, so it is photographic texture, not
    an icon-system design decision.
  visible_tells:
  - Eight square cells each hold a photographic insert above a text label; no unified drawn iconography,
    each crop differs
  confidence: high
- id: iconography_05
  family: iconography_illustration
  polarity: mixed
  page_or_region: generic line-glyph icon set (boundless stat row, domain cards, feature grid; partners
    benefits)
  tile_path: store/agentislongevity-com/captures/2026-06-25/tiles/boundless_protocols/tile-06-y07320.png
  claim: Across the recurring icon sets the glyphs are small, consistent, but undistinguished outline
    icons that read as generic SaaS/health-app stock and add no custom illustration character; the same
    competent-but-anonymous treatment repeats on the boundless stat row, domain cards, the six feature
    panels, and the partner-benefit cards.
  visible_tells:
  - Boundless feature-grid icons are elementary outline shapes (dial, flask, watch, clipboard, person)
    with no custom styling
  - Boundless stat-row and domain-card glyphs and the four partner-benefit glyphs are the same minimal
    stroke style, swappable from any icon library
  confidence: high
  contrast_with: store/agentislongevity-com/captures/2026-06-25/tiles/longevity_quotient/tile-01-y01220.png
- id: iconography_06
  family: iconography_illustration
  polarity: poor
  page_or_region: partners 'scale' metric-card graphics (dot grid, US map, bar chart)
  tile_path: store/agentislongevity-com/captures/2026-06-25/tiles/partners/tile-01-y01220.png
  claim: The three 'scale' metric graphics - a patient dot grid, a flat US state-outline map, and a same-store-growth
    bar chart - are low-craft and read as default chart output, the map and bar chart in particular with
    no annotation or styling refinement.
  visible_tells:
  - US map in flat teal fill with no annotations
  - Bar chart with a single colored bar among grey bars, no axis labels or visual refinement beyond default
    output
  confidence: high
- id: iconography_07
  family: iconography_illustration
  polarity: mixed
  page_or_region: partners clinic-card location thumbnails
  tile_path: store/agentislongevity-com/captures/2026-06-25/tiles/partners/tile-02-y02440.png
  claim: Per-clinic cards use a moody cinematic photo as the card thumbnail (rather than a logo or map
    pin), giving the cards a mood-driven identity, though the card container itself is plain.
  visible_tells:
  - Rounded dark-teal card frames each hold a high-contrast moody photograph with a small numbered badge
    and white city label overlaid
  confidence: medium
- id: iconography_08
  family: iconography_illustration
  polarity: mixed
  page_or_region: boundless_protocols phase-timeline connector
  tile_path: store/agentislongevity-com/captures/2026-06-25/tiles/boundless_protocols/tile-03-y03660.png
  claim: The 'How you'll feel week by week' timeline uses numbered teal circle markers connected by a
    thin vertical line - functional and clean but a near-default UI pattern with no custom graphic treatment.
  visible_tells:
  - Small teal circle with a white number at each phase card, connected by a thin vertical line, no embellishment
    beyond the circle/number
  confidence: medium
- id: iconography_09
  family: iconography_illustration
  polarity: mixed
  page_or_region: about page decorative four-pointed star motif
  tile_path: store/agentislongevity-com/captures/2026-06-25/tiles/about/tile-00-y00000.png
  claim: The about hero carries a large pale four-pointed star/diamond motif as a low-opacity background
    graphic - geometrically clean and on-brand, functioning as decorative illustration without competing
    with the headshots.
  visible_tells:
  - Large pale grey four-pointed star at the left of the team-photo section, symmetrical and minimal,
    set at low opacity behind the content
  confidence: medium
```

## Provenance

- **Tiles:** mined native-resolution tiles from 5 cached Firecrawl page screenshots — homepage, longevity_quotient, boundless_protocols, about, partners (`store/agentislongevity-com/captures/2026-06-25/tiles/`). 45 tiles handed to the blind fan-out (4 family miners → judge).
- **QA:** `clean` — all five pages rendered faithfully from cached payloads; no modals, grey/WebGL heroes, black media, or stuck count-ups. The pervasive dark spruce is the brand's intentional palette, not a render failure. No exclusions; **no Tier-B re-render** needed.
- **Post-judge correction:** dropped one card (`layout_10`, partners "dead zone") on the author spot-check — its "two-thirds empty before footer" read is substantially a tile-boundary/section-end whitespace artifact, not a pure design defect; the genuine sparse-listing signal is retained by `layout_08`.
- **Snapshot caveat:** a point-in-time read of the 2026-06-25 captured tiles; the live site may change.
