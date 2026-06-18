---
schema_version: "1.0"
domain: honehealth.com
captured_at: 2026-06-18
source_capture: 2026-06-18
qa_status: exclusions-noted
---

## Visual & brand impression

Hone reads as a disciplined editorial health brand built on three values — electric yellow, near-black, white — with the single yellow accent deployed as a system: ticker, CTAs, full-bleed section grounds, even encoding the preferred pricing tier [color_01][color_02][color_03][color_04]. The serif type system does real work — three-level step headers pairing roman and italic display, hero legibility won by tonal placement, footer hierarchy by weight not size [typography_01][typography_02][typography_09]. Structure is the strength: a central-rule process spine, a repeated Q&A template, a hard 50/50 pricing split, a composed comparison table [layout_01][layout_03][layout_04][layout_05]. It frays at imagery — generic, ungraded stock across heroes, headshots, and ambassador cards [color_05][color_07][color_09], small text dissolving over photos [typography_08], a clipped rail and an orphaned mockup [layout_10][layout_11], and off-the-shelf icons with no custom illustration [iconography_01][iconography_04].

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: homepage — process steps section, Step 01 header
  tile_path: store/honehealth-com/captures/2026-06-18/tiles/homepage/tile-01-y01220.png
  claim: Step headers run a three-level system — small bold 'Step 01.' label, large roman serif display word ('Measure'), then a large italic serif complement ('& Assess') — giving real weight and style contrast within a single moment that most sites skip.
  visible_tells:
  - Small bold 'Step 01.' label sits above at roughly 12px
  - Display serif 'Measure' renders very large in roman weight
  - Italic serif '& Assess' directly below at matching size creates roman/italic style contrast
  confidence: high
  contrast_with: store/honehealth-com/captures/2026-06-18/tiles/how_it_works/tile-01-y01220.png
- id: typography_02
  family: typography_hierarchy
  polarity: strong
  page_or_region: homepage — hero headline
  tile_path: store/honehealth-com/captures/2026-06-18/tiles/homepage/tile-00-y00000.png
  claim: The hero serif headline ('Longevity engineered around your biology') sits in the lower-left over the lighter, lower-contrast band of the photo, holding legibility with no text shadow or scrim — legibility achieved by tonal placement rather than an overlay.
  visible_tells:
  - Serif headline placed in the lower-left quadrant where the image is light/neutral
  - No text shadow or darkening overlay used behind the type
  confidence: high
- id: typography_03
  family: typography_hierarchy
  polarity: strong
  page_or_region: consults — Q&A content sections
  tile_path: store/honehealth-com/captures/2026-06-18/tiles/consults/tile-01-y01220.png
  claim: Q&A sections use a two-column type hierarchy — a large serif question head left, regular-weight serif answers right separated by hairline rules — so scan order is unambiguous through column position and size rather than weight variation in the body.
  visible_tells:
  - 'Left: ''What''s covered during the consult?'' in large serif over two lines'
  - 'Right: answers in regular-weight serif, each separated by a 1px horizontal rule'
  - Spatial column split carries hierarchy independent of font size
  confidence: high
- id: typography_04
  family: typography_hierarchy
  polarity: mixed
  page_or_region: homepage — yellow mission statement band
  tile_path: store/honehealth-com/captures/2026-06-18/tiles/homepage/tile-01-y01220.png
  claim: The mission statement ('We empower you to take control of your health…') is set as a centered single-size serif block with no eyebrow, subhead, or secondary level, so hierarchy collapses to one level and it reads as a wall of headline.
  visible_tells:
  - Three-line centered serif fills the yellow band at one large size
  - No subheading, eyebrow, or secondary size accompanies it
  confidence: medium
- id: typography_05
  family: typography_hierarchy
  polarity: mixed
  page_or_region: how_it_works — step list
  tile_path: store/honehealth-com/captures/2026-06-18/tiles/how_it_works/tile-01-y01220.png
  claim: The how-it-works step list uses a plainer two-level system (medium serif step title over small bullet body) that is functional but markedly less composed than the homepage steps' roman/italic display pairing.
  visible_tells:
  - '''Consult with a licensed physician'' in medium serif'
  - Bullet body items in small text — size jump present but not dramatic
  - No italic or display-scale contrast used
  confidence: medium
  contrast_with: store/honehealth-com/captures/2026-06-18/tiles/homepage/tile-01-y01220.png
- id: typography_06
  family: typography_hierarchy
  polarity: mixed
  page_or_region: homepage — pricing section
  tile_path: store/honehealth-com/captures/2026-06-18/tiles/homepage/tile-05-y06100.png
  claim: Pricing figures ($25, $155) are set large in a display serif for strong hierarchy, but the '/month' suffix sits at near-headline scale rather than dropping in weight, softening the intended number-vs-unit contrast.
  visible_tells:
  - '''$155'' very large with ''/month'' alongside at a similar large scale on the yellow column'
  - '''$25 /month'' on the white column shows the same relative-scale mismatch'
  confidence: medium
- id: typography_07
  family: typography_hierarchy
  polarity: mixed
  page_or_region: hone_at_home — hero overlay
  tile_path: store/honehealth-com/captures/2026-06-18/tiles/hone_at_home/tile-00-y00000.png
  claim: The white serif hero ('Experience Personalized Wellness Right in Your Home.') holds in the center but its right edge bleeds into the lighter clothing of the second figure with no scrim, dropping contrast on the trailing words.
  visible_tells:
  - White serif headline crosses the mid-photo band where the right figure's light clothing reduces contrast
  - No darkening overlay behind the text
  confidence: medium
- id: typography_08
  family: typography_hierarchy
  polarity: poor
  page_or_region: consults — hero subhead
  tile_path: store/honehealth-com/captures/2026-06-18/tiles/consults/tile-00-y00000.png
  claim: The consults hero subhead is set very small over a mid-toned photo with no contrast treatment, dissolving into the background and reading as functionally illegible in the tile.
  visible_tells:
  - Body text under the hero headline appears at roughly 12px or smaller and merges with the photo
  - No overlay or scrim supports the small text
  confidence: high
  contrast_with: store/honehealth-com/captures/2026-06-18/tiles/homepage/tile-00-y00000.png
- id: typography_09
  family: typography_hierarchy
  polarity: strong
  page_or_region: footer — column header labels
  tile_path: store/honehealth-com/captures/2026-06-18/tiles/homepage/tile-09-y10233.png
  claim: The dark footer separates two levels with weight and tracking rather than size — tight uppercase column headers ('WHY HONE', 'OUR COMPANY', 'LEGAL') over regular-weight links — keeping a dense footer scannable.
  visible_tells:
  - Column headers in tight uppercase caps at small size
  - Link items in regular weight at similar size below each header
  - Weight/tracking contrast alone distinguishes the levels
  confidence: high
- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: homepage — process steps spine
  tile_path: store/honehealth-com/captures/2026-06-18/tiles/homepage/tile-01-y01220.png
  claim: A persistent full-height vertical rule at the horizontal midpoint anchors the two-column step layout across multiple scroll heights, giving the process section a clear structural spine.
  visible_tells:
  - Continuous thin vertical line at exact center-x running the full tile height, UI mockup pinned left and step copy pinned right
  confidence: high
  contrast_with: store/honehealth-com/captures/2026-06-18/tiles/homepage/tile-02-y02440.png
- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: homepage — process steps, Steps 2–3 mirror
  tile_path: store/honehealth-com/captures/2026-06-18/tiles/homepage/tile-02-y02440.png
  claim: Steps alternate sides of the central rule — mockup left for Step 2, mockup right for Step 3 — producing a deliberate zigzag rhythm while both columns stay locked to the same midline grid.
  visible_tells:
  - Step 02 UI card left with copy right; Step 03 UI card right with copy left, mirroring across the midline rule
  confidence: high
- id: layout_03
  family: layout_composition_components
  polarity: strong
  page_or_region: consults — repeated Q&A component
  tile_path: store/honehealth-com/captures/2026-06-18/tiles/consults/tile-01-y01220.png
  claim: A two-column Q&A component — large question left, divider-separated answer list right — repeats identically across at least three successive sections, evidencing a well-defined template applied with discipline.
  visible_tells:
  - Three stacked section blocks each with the same left-heading / right-answer-list structure separated by full-width hairline rules
  confidence: high
  contrast_with: store/honehealth-com/captures/2026-06-18/tiles/consults/tile-02-y02440.png
- id: layout_04
  family: layout_composition_components
  polarity: strong
  page_or_region: homepage — pricing split panel
  tile_path: store/honehealth-com/captures/2026-06-18/tiles/homepage/tile-05-y06100.png
  claim: The two-plan pricing block uses a hard 50/50 vertical split (white left, yellow right) to separate tiers while keeping identical internal structure — checklist rows, price display, italic subtext — across both halves.
  visible_tells:
  - Left half white, right half full-bleed yellow
  - Both halves share identical feature-row and price-display structure
  confidence: high
- id: layout_05
  family: layout_composition_components
  polarity: strong
  page_or_region: how_it_works — Premium vs Basic comparison table
  tile_path: store/honehealth-com/captures/2026-06-18/tiles/how_it_works/tile-02-y02440.png
  claim: The comparison table highlights the promoted Premium tier with a full-height yellow column fill, clean hairline row rules and centered checkmarks — a composed component rather than a default table.
  visible_tells:
  - Yellow fill runs the full height of the Premium column
  - Hairline horizontal row rules separate each feature
  - Checkmark glyphs aligned to column centers
  confidence: high
- id: layout_06
  family: layout_composition_components
  polarity: strong
  page_or_region: footer — nav grid + trust badges
  tile_path: store/honehealth-com/captures/2026-06-18/tiles/homepage/tile-09-y10233.png
  claim: The footer uses an evenly spaced multi-column nav grid sharing a common top baseline, a distinct 'Reach Out' column flush right, and LegitScript/Trustpilot badges anchored bottom-right as a terminal block.
  visible_tells:
  - Labeled nav columns (WHY HONE / OUR COMPANY / THE EDGE BLOG / LEGAL) span left to right at uniform spacing
  - LegitScript and Trustpilot badges sit bottom-right as a separate block
  confidence: high
- id: layout_07
  family: layout_composition_components
  polarity: mixed
  page_or_region: homepage — hero stack density
  tile_path: store/honehealth-com/captures/2026-06-18/tiles/homepage/tile-00-y00000.png
  claim: The hero stacks a full-bleed photo, overprinted heading, a dark 'Menopause Time Off' banner strip, and a yellow mission band in quick vertical sequence — intentional transitions but several distinct sections compressed into under one viewport with little breathing room.
  visible_tells:
  - Hero photo, dark banner strip, and yellow band all visible within one tile with minimal spacing between them
  confidence: medium
- id: layout_08
  family: layout_composition_components
  polarity: mixed
  page_or_region: homepage — brand ambassador grid
  tile_path: store/honehealth-com/captures/2026-06-18/tiles/homepage/tile-07-y08540.png
  claim: The ambassador grid runs three cards in row one and two offset cards in row two — an intentional stagger — but the row-two pair is not centered against the row above, leaving a large asymmetric gap.
  visible_tells:
  - Row two's two cards sit with a wide empty gap between them that does not align symmetrically with the three-card row above
  confidence: medium
- id: layout_09
  family: layout_composition_components
  polarity: mixed
  page_or_region: hone_at_home — offerings accordion + image split
  tile_path: store/honehealth-com/captures/2026-06-18/tiles/hone_at_home/tile-01-y01220.png
  claim: An expanded accordion panel (Botox, price, bullet list) is paired with a flush right-column photo, but the open state's height leaves the right image cropped tight mid-face with no padding, so the two columns fall out of compositional balance at this scroll position.
  visible_tells:
  - Left column Botox panel open with multi-line content; right-column face image cropped mid-face with no padding, the two heights clearly mismatched
  confidence: medium
- id: layout_10
  family: layout_composition_components
  polarity: mixed
  page_or_region: hone_at_home — testimonials row truncation
  tile_path: store/honehealth-com/captures/2026-06-18/tiles/hone_at_home/tile-02-y02440.png
  claim: The horizontal testimonial row hard-clips the rightmost card at the viewport edge with no fade, arrow, or partial-card reveal, so the truncation reads as an accident rather than a scroll affordance.
  visible_tells:
  - Fourth testimonial card is cut at the right viewport edge with no fade or partial-card cue
  confidence: medium
- id: layout_11
  family: layout_composition_components
  polarity: poor
  page_or_region: homepage — orphaned phone mockup
  tile_path: store/honehealth-com/captures/2026-06-18/tiles/homepage/tile-05-y06100.png
  claim: A small phone mockup floats in the lower-left with no containing section background or padding, leaving it compositionally unanchored relative to the CTA block beside it.
  visible_tells:
  - Small phone screenshot sits lower-left with no section background, padding, or grouping connecting it to the yellow 'GET STARTED' block to its right
  confidence: medium
- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: homepage — electric-yellow accent system
  tile_path: store/honehealth-com/captures/2026-06-18/tiles/homepage/tile-00-y00000.png
  claim: A single electric chartreuse-yellow is the sole accent — nav ticker, CTA buttons, and banner strip — applied with restraint so it reads as a deliberate system, not decoration.
  visible_tells:
  - Yellow scrolling ticker bar at top edge
  - Yellow 'GET STARTED' nav button
  - Yellow CTA buttons and banner strip lower in frame
  confidence: high
  contrast_with: store/honehealth-com/captures/2026-06-18/tiles/homepage/tile-01-y01220.png
- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: homepage — yellow as structural section ground
  tile_path: store/honehealth-com/captures/2026-06-18/tiles/homepage/tile-01-y01220.png
  claim: Yellow is used as a full-bleed section ground (not just a button), with an abrupt, intentional yellow-to-white edge and black text directly on yellow — showing the accent carries structural weight in the layout.
  visible_tells:
  - Full-width yellow panel occupying the top third of the tile
  - Hard edge transition to white below
  - Black text directly on yellow with no intermediate tone
  confidence: high
- id: color_03
  family: color_brand_imagery
  polarity: strong
  page_or_region: footer — three-value palette on near-black
  tile_path: store/honehealth-com/captures/2026-06-18/tiles/homepage/tile-08-y09760.png
  claim: The footer completes a disciplined three-value palette — yellow / white / near-black — with an oversized ghost 'HONE' letterform in slightly lighter dark and the yellow triangle as the only chromatic element on the near-black ground.
  visible_tells:
  - Near-black full-bleed footer background
  - Oversized ghost 'HONE' letterform in slightly lighter dark
  - Yellow triangle the only chromatic element on the dark ground
  confidence: high
  contrast_with: store/honehealth-com/captures/2026-06-18/tiles/homepage/tile-01-y01220.png
- id: color_04
  family: color_brand_imagery
  polarity: strong
  page_or_region: homepage — yellow encodes pricing hierarchy
  tile_path: store/honehealth-com/captures/2026-06-18/tiles/homepage/tile-05-y06100.png
  claim: Yellow is applied functionally to the preferred pricing tier as a full background fill, encoding hierarchy through the single brand color without introducing any secondary palette color.
  visible_tells:
  - Right pricing column filled entirely yellow, left column white
  - No third color or gradient introduced to mark the preferred tier
  confidence: high
- id: color_05
  family: color_brand_imagery
  polarity: mixed
  page_or_region: homepage — hero photography register
  tile_path: store/honehealth-com/captures/2026-06-18/tiles/homepage/tile-00-y00000.png
  claim: The hero photo (two people, studio-neutral light) is competent but generically graded — a standard front-lit health/wellness portrait with no branded color treatment, transferable to any competitor.
  visible_tells:
  - Studio-neutral gray background behind the subjects
  - No branded color overlay or grade on the image
  - Standard front-lit framing with no distinctive angle
  confidence: high
  contrast_with: store/honehealth-com/captures/2026-06-18/tiles/how_it_works/tile-00-y00000.png
- id: color_06
  family: color_brand_imagery
  polarity: mixed
  page_or_region: how_it_works — brand-in-image hero
  tile_path: store/honehealth-com/captures/2026-06-18/tiles/how_it_works/tile-00-y00000.png
  claim: The hero shows two people holding yellow-branded HONE boxes outdoors — a coherent brand-in-the-world moment where the accent appears on real packaging — though the candid outdoor-lifestyle setting still sits in a generic telehealth register.
  visible_tells:
  - Both subjects hold boxes with yellow 'HONE' branding visible
  - Warm outdoor light, candid lifestyle pose
  - Yellow appears in the physical product rather than only as UI
  confidence: high
- id: color_07
  family: color_brand_imagery
  polarity: mixed
  page_or_region: homepage — ambassador image-set incohesion
  tile_path: store/honehealth-com/captures/2026-06-18/tiles/homepage/tile-07-y08540.png
  claim: Ambassador portrait cards are white-on-white with only a faint shadow, barely separating from the page, and the five portraits vary widely in color temperature and treatment, breaking image-set cohesion.
  visible_tells:
  - Cards barely distinguishable from the white page background
  - Paul Wesley a cool dark-studio shot, Dan Churchill a warm outdoor shot, Brendan Fallis a warm street shot — no consistent grade
  - No yellow appears in any ambassador image
  confidence: high
- id: color_08
  family: color_brand_imagery
  polarity: mixed
  page_or_region: homepage — in-app UI color vs brand palette
  tile_path: store/honehealth-com/captures/2026-06-18/tiles/homepage/tile-03-y03660.png
  claim: In-app screenshots introduce teal, orange and green data colors absent from the strict yellow/black/white brand system — functionally necessary inside the product but creating chromatic noise against the marketing palette around them.
  visible_tells:
  - Multi-color dot-ring biomarker chart (teal, green, orange) inside the phone mockup
  - Orange/green segments on the Healthspan spectrum bar
  confidence: high
  contrast_with: store/honehealth-com/captures/2026-06-18/tiles/homepage/tile-05-y06100.png
- id: color_09
  family: color_brand_imagery
  polarity: poor
  page_or_region: how_it_works — physician headshots
  tile_path: store/honehealth-com/captures/2026-06-18/tiles/how_it_works/tile-03-y03660.png
  claim: Physician portraits are standard credentialing headshots — white coats, neutral backgrounds, front-lit — generic in treatment and untethered to the yellow/dark palette in any visible way.
  visible_tells:
  - Subjects in white medical attire against light neutral backgrounds
  - Consistent front-lit studio lighting
  - No yellow element or branded backdrop distinguishing them from any other provider's doctor grid
  confidence: high
- id: color_10
  family: color_brand_imagery
  polarity: poor
  page_or_region: hone_at_home — extreme close-up stock photo
  tile_path: store/honehealth-com/captures/2026-06-18/tiles/hone_at_home/tile-03-y03660.png
  claim: An extreme close-up of a face/neck with gloved hands, used as a split background behind FAQ text, sits squarely in generic beauty/health stock register with no palette link and crops awkwardly at the tile edge.
  visible_tells:
  - Tight crop of a face/neck with gloved hands and no contextual cues
  - Warm neutral skin tone with no yellow/black/white treatment
  - Image cropped mid-face at the tile boundary
  confidence: high
  contrast_with: store/honehealth-com/captures/2026-06-18/tiles/how_it_works/tile-00-y00000.png
- id: iconography_01
  family: iconography_illustration
  polarity: mixed
  page_or_region: how_it_works treatment grid + in-app category icons
  tile_path: store/honehealth-com/captures/2026-06-18/tiles/how_it_works/tile-03-y03660.png
  claim: A consistent thin-stroke, rounded-square icon system spans both the marketing treatment grid and the in-app category list — uniform container size and stroke weight — but the glyphs themselves (gender symbols, stethoscope, leaf, barbell, moon, downward curve) are off-the-shelf wellness shapes, not proprietary forms.
  visible_tells:
  - 8-icon treatment grid in a 4x2 layout, all sharing identical bounding-box size and stroke weight
  - In-app rows (Medications, Supplements, Diet/Nutrition, Exercise, Sleep) use the same rounded-square thin-line vocabulary
  - Glyph choices are recognizable generic health-app stock shapes
  confidence: high
  contrast_with: store/honehealth-com/captures/2026-06-18/tiles/homepage/tile-02-y02440.png
- id: iconography_02
  family: iconography_illustration
  polarity: strong
  page_or_region: site-wide — triangle logomark repetition
  tile_path: store/honehealth-com/captures/2026-06-18/tiles/homepage/tile-08-y09760.png
  claim: The single triangle/delta logomark is the only decorative mark, deployed identically as the centered anchor above every footer CTA ('Uncover what's possible with Hone.') and again as a small section divider above 'Formulas Built For You' — disciplined, unvarying repetition doing double duty as identifier and ornament.
  visible_tells:
  - Outlined yellow triangle centered above the footer CTA on dark ground
  - Same mark recurs identically across hone_at_home, how_it_works and consults footers at constant size/color
  - Mark reused at small scale as a section break above 'Formulas Built For You'
  confidence: high
  contrast_with: store/honehealth-com/captures/2026-06-18/tiles/homepage/tile-00-y00000.png
- id: iconography_03
  family: iconography_illustration
  polarity: poor
  page_or_region: homepage — in-app testosterone readout graphic
  tile_path: store/honehealth-com/captures/2026-06-18/tiles/homepage/tile-01-y01220.png
  claim: The testosterone card's only data graphic is a minimal horizontal gradient range bar with a single dot marker plus a red 'Warning' pill — a sparse, purely functional readout with no design ambition.
  visible_tells:
  - Single horizontal gradient bar from '000 ng/dL' to '900 ng/dL' with one dot marker
  - Red 'Warning' pill badge as the only additional graphic element
  confidence: high
  contrast_with: store/honehealth-com/captures/2026-06-18/tiles/homepage/tile-03-y03660.png
- id: iconography_04
  family: iconography_illustration
  polarity: poor
  page_or_region: site-wide — absence of custom illustration
  tile_path: store/honehealth-com/captures/2026-06-18/tiles/consults/tile-01-y01220.png
  claim: Across the five page types captured, no hand-drawn, editorial, or custom illustration appears anywhere — the entire graphic vocabulary is confined to the triangle logomark, a generic thin-line icon set, and product UI screenshots.
  visible_tells:
  - Consults sections are entirely text-and-divider layouts with no graphic elements beyond the logomark
  - No spot illustration, decorative motif, or diagram artwork on any page
  confidence: high
```

## Provenance

- **Tiles read** — native-resolution Tier-A tiles from the `2026-06-18` capture, across five pages that carry the visual system: `captures/2026-06-18/tiles/{homepage, how_it_works, consults, hone_at_home, mens_trt}/`. 24 active tiles mined by four blind family miners + judge.
- **Exclusions (`exclusions-noted`)** — two homepage tiles dropped at the QA gate for lazy-load contamination, never shown to the miners: `homepage/tile-04-y04880.png` (right half of the "Increase Testosterone" product card rendered as a grey placeholder) and `homepage/tile-06-y07320.png` ("Real People. Real Stories." testimonial media cards rendered as empty white boxes). The pricing split that tile-04 also carries is fully and cleanly captured on `tile-05`.
- **No Tier-B** — all cited tiles are cached Firecrawl payloads; no browser re-render was needed. `mens_trt` truncated to its hero only (one clean tile, not contaminated); it corroborates the brand system but no card uniquely depends on it.
- **Snapshot caveat** — this is a point-in-time read of the captured tiles; the live site changes. Cards are blind evidence (miners saw only tile images, never the dossier or live web).
