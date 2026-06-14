---
schema_version: "1.0"
domain: goinfusive.com
captured_at: 2026-06-14
source_capture: 2026-06-09
qa_status: clean
---

## Visual & brand impression

A single purple-to-magenta gradient governs both pages and the primary CTA is reserved consistently [color_01][color_02], so the surface reads cohesive — but the polish outruns the finish. Hierarchy is manufactured by bolding individual words rather than clean size steps [typography_01], and the smallest copy sits near the contrast floor over particle fields and purple-on-dark cards [typography_02][typography_05]. Competent two-column blocks are undercut by collisions — a sticky tab strip rendering twice [layout_07], a logo wall bleeding into a screenshot [layout_08]. Imagery splits between owned brand mockups [color_09] and desaturated generic stock [color_07]. The strongest moments are the most restrained: the clean three-tier compliance and inventory headers [typography_06][typography_11]. Gloss-forward — a coherent palette carrying inconsistent execution.

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: mixed
  page_or_region: Homepage hero headline
  tile_path: store/goinfusive-com/captures/2026-06-09/tiles/homepage/tile-00-y00000.png
  claim: The hero headline manufactures hierarchy by bolding and emphasizing individual words ('Scale', 'ZERO') inside an otherwise light line, then shifts the support line to letter-spaced caps — three treatments stacked in one block rather than a clean size step.
  visible_tells:
  - '''Easily Scale'' mixes a thin weight with a bolded word mid-phrase'
  - '''ZERO'' set in heavier bold among lighter words'
  - '''WE HANDLE EVERYTHING'' jumps to letter-spaced caps directly below'
  confidence: high
- id: typography_02
  family: typography_hierarchy
  polarity: poor
  page_or_region: Homepage hero — supporting line over particle field
  tile_path: store/goinfusive-com/captures/2026-06-09/tiles/homepage/tile-00-y00000.png
  claim: The thin grey support line ('By Installing Our Dedicated Team & Software Solution') sits at low contrast over a mottled purple particle cloud, eroding legibility of the smallest copy tier.
  visible_tells:
  - thin grey weight on a dark purple particle background
  - second line noticeably dimmer than the white line above it
  - background bokeh dots pass directly behind the glyphs
  confidence: high
  contrast_with: store/goinfusive-com/captures/2026-06-09/tiles/homepage/tile-02-y02440.png
- id: typography_03
  family: typography_hierarchy
  polarity: poor
  page_or_region: Platform — persistent feature tab strip
  tile_path: store/goinfusive-com/captures/2026-06-09/tiles/platform/tile-01-y01220.png
  claim: The persistent horizontal tab strip crams seven multi-word all-caps labels into one row, forcing two-line wraps in tiny type with almost no breathing room between cells.
  visible_tells:
  - '''Intelligent Inventory Management'' wraps to two cramped lines in its cell'
  - seven labels packed edge-to-edge across the full width
  - label type is markedly smaller than any body copy on the page
  confidence: high
- id: typography_04
  family: typography_hierarchy
  polarity: mixed
  page_or_region: Platform hero headline
  tile_path: store/goinfusive-com/captures/2026-06-09/tiles/platform/tile-00-y00000.png
  claim: The platform hero shows a competent two-level head/sub relationship — large light headline over a smaller grey paragraph — but resolves emphasis by bolding the trailing clause ('organized, profitable, and scalable') instead of a distinct type style.
  visible_tells:
  - '''The Only Software Built For Wellness Practices'' set large and light'
  - supporting paragraph clearly smaller and dimmer beneath it
  - final clause bolded within the otherwise regular-weight paragraph
  confidence: medium
- id: typography_05
  family: typography_hierarchy
  polarity: mixed
  page_or_region: Platform — feature-card titles in purple on dark cards
  tile_path: store/goinfusive-com/captures/2026-06-09/tiles/platform/tile-00-y00000.png
  claim: The four 'Everything Your Clinic Needs' card titles are set in saturated purple on near-black panels, reading dimmer than the grey body beneath them and pushing the most important label tier toward the contrast floor.
  visible_tells:
  - '''Seamless Ordering & Vendor Control'' in mid-purple on a dark card'
  - card titles dimmer than the grey body text below them
  - purple-on-dark holds across all four card headings in the row
  confidence: medium
  contrast_with: store/goinfusive-com/captures/2026-06-09/tiles/platform/tile-06-y07320.png
- id: typography_06
  family: typography_hierarchy
  polarity: strong
  page_or_region: Platform — 'Built-In 797 Compliance' section
  tile_path: store/goinfusive-com/captures/2026-06-09/tiles/platform/tile-06-y07320.png
  claim: 'This section shows the clearest hierarchy on the site: a large black headline, a medium black sub-line, then evenly-set white card captions on magenta tiles — three legible tiers in descending size with consistent alignment.'
  visible_tells:
  - '''Built-In 797 Compliance'' large and high-contrast on white'
  - '''Stay compliant automatically.'' a clean secondary line below'
  - four card captions uniform in size and weight across the row
  confidence: high
  contrast_with: store/goinfusive-com/captures/2026-06-09/tiles/platform/tile-00-y00000.png
- id: typography_07
  family: typography_hierarchy
  polarity: mixed
  page_or_region: Homepage — 'Stay Ahead of the Chaos' newsletter block
  tile_path: store/goinfusive-com/captures/2026-06-09/tiles/homepage/tile-07-y08063.png
  claim: The newsletter block stacks several near-equal small tiers — a purple sub-head, a grey intro line, bold bullet leads, and grey bullet tails — with too little size or weight separation to guide the eye through them.
  visible_tells:
  - purple 'Join the Infusive Insider Newsletter' barely larger than the grey line under it
  - bullet lead words ('Growth Playbooks') bolded but at body size
  - intro line and bullet bodies share one indistinct grey weight
  confidence: medium
- id: typography_08
  family: typography_hierarchy
  polarity: mixed
  page_or_region: Homepage — 'Uncover the Hidden Profit Leaks' headline
  tile_path: store/goinfusive-com/captures/2026-06-09/tiles/homepage/tile-01-y01220.png
  claim: A two-line gradient-filled headline pairs with a bold white sub-line for a clear primary/secondary read, but the gradient fill lowers the heading's contrast against the dark band at its purple end relative to the plain white text below.
  visible_tells:
  - '''Uncover the Hidden Profit Leaks'' in a purple-to-pink gradient'
  - white sub-line about losing '$5K-$20K+ every month' solid beneath it
  - gradient heading dimmer at its purple end than the white sub-line
  confidence: medium
- id: typography_09
  family: typography_hierarchy
  polarity: strong
  page_or_region: Platform — closing 'Built for Wellness' statement
  tile_path: store/goinfusive-com/captures/2026-06-09/tiles/platform/tile-07-y08540.png
  claim: 'The closing statement is cleanly staged: a large white headline, a regular-weight white paragraph, and a bold white tagline form three legible tiers, and the dark overlay keeps every line readable.'
  visible_tells:
  - '''Built for Wellness. Designed for Scale.'' large and bright'
  - two-line paragraph at clearly smaller regular weight
  - '''Streamline operations. Strengthen margins...'' tagline bolded as a distinct closing tier'
  confidence: high
- id: typography_10
  family: typography_hierarchy
  polarity: mixed
  page_or_region: Platform — lower feature-card body copy
  tile_path: store/goinfusive-com/captures/2026-06-09/tiles/platform/tile-01-y01220.png
  claim: Within the three lower feature cards the title/body relationship is consistent and readable, but the body copy is set quite small with tight leading, compressing the secondary tier into dense label-like blocks.
  visible_tells:
  - '''Real-Time Financial Insights'' title over a tight multi-line grey paragraph'
  - small body type with little line spacing inside each card
  - the three cards repeat the same compressed title-over-paragraph rhythm
  confidence: medium
- id: typography_11
  family: typography_hierarchy
  polarity: strong
  page_or_region: Platform — 'Inventory Management System' header
  tile_path: store/goinfusive-com/captures/2026-06-09/tiles/platform/tile-03-y03660.png
  claim: This centered section header executes a clean three-tier descent — large white title, medium white sub-line, smaller grey paragraph — on a dark ground with even alignment and clear size steps.
  visible_tells:
  - '''Inventory Management System'' large and centered in white'
  - '''Know exactly what you have...'' as a distinct medium sub-line'
  - a narrow grey support paragraph centered beneath at the smallest tier
  confidence: high
- id: layout_01
  family: layout_composition_components
  polarity: mixed
  page_or_region: Homepage — 'Is your clinic ready' pain-point list
  tile_path: store/goinfusive-com/captures/2026-06-09/tiles/homepage/tile-02-y02440.png
  claim: 'The right-hand pain-point list is a tidy stacked component set: four equal-height pill rows, each with a left icon and a single left-aligned label, evenly spaced and roughly aligned to the paired image height beside it.'
  visible_tells:
  - four rounded rows of equal height stack with uniform vertical gaps
  - each row pairs a left-side icon with one left-aligned label line
  - the stack's top and bottom roughly align to the before-image on the left
  confidence: medium
- id: layout_02
  family: layout_composition_components
  polarity: mixed
  page_or_region: Homepage — hero dashboard + overlapping testimonial card
  tile_path: store/goinfusive-com/captures/2026-06-09/tiles/homepage/tile-00-y00000.png
  claim: The hero composes a dashboard mockup with an overlapping translucent testimonial card, but the card collides with the dashboard's right edge and crops it rather than resolving into a clean offset.
  visible_tells:
  - translucent testimonial card ('...grow our business 300%') overlaps and crops the dashboard's right side
  - the card's quote text wraps tightly against its own rounded border
  - the nav pill and APPLY NOW button sit cleanly aligned in the bar above
  confidence: medium
- id: layout_03
  family: layout_composition_components
  polarity: mixed
  page_or_region: Homepage — INFUSIVE intro band over room photo
  tile_path: store/goinfusive-com/captures/2026-06-09/tiles/homepage/tile-01-y01220.png
  claim: The text column and laptop screenshot share a two-column layout, but the laptop image is cropped hard at the right edge and the body copy sits low-contrast over a busy room photo.
  visible_tells:
  - the laptop dashboard mockup is clipped at the right boundary of the frame
  - paragraph text overlays a dim room photo, reducing legibility separation
  - the 'MORE ABOUT INFUSIVE' pill is left-aligned and cleanly formed below the copy
  confidence: medium
- id: layout_04
  family: layout_composition_components
  polarity: mixed
  page_or_region: Homepage — scalloped/notch section dividers
  tile_path: store/goinfusive-com/captures/2026-06-09/tiles/homepage/tile-02-y02440.png
  claim: Sections are separated by a repeated downward-pointing notch/scallop divider that imposes an unusual rhythm and leaves a visible seam where the curve meets the next section's flat top.
  visible_tells:
  - a centered V-notch dips into the top edge of the dark section
  - a matching scalloped curve closes the section at its bottom
  - the notch recurs as the transition device between adjacent bands
  confidence: medium
  contrast_with: store/goinfusive-com/captures/2026-06-09/tiles/homepage/tile-04-y04880.png
- id: layout_05
  family: layout_composition_components
  polarity: mixed
  page_or_region: Homepage — newsletter ebook + form section
  tile_path: store/goinfusive-com/captures/2026-06-09/tiles/homepage/tile-07-y08063.png
  claim: 'The newsletter block resolves into a clean two-column layout: angled ebook mockup left, heading/benefit-bullets/inline-form stacked right on a single left edge with a paired Name/Email field row.'
  visible_tells:
  - heading, sub-line, three bullet rows, and form all share one left edge
  - Name and Email inputs sit as equal-width fields beside the SUBSCRIBE NOW pill
  - the ebook cover is offset at a consistent angle in the left column
  confidence: medium
- id: layout_06
  family: layout_composition_components
  polarity: mixed
  page_or_region: Platform — hero CTA over band transition
  tile_path: store/goinfusive-com/captures/2026-06-09/tiles/platform/tile-00-y00000.png
  claim: The platform hero pairs a left laptop mockup with right-side copy competently, but the section header below is squeezed close to the CTA button with little separating whitespace.
  visible_tells:
  - '''REQUEST A DEMO'' pill sits only a small gap above the next gradient heading'
  - the 'Everything Your Clinic Needs...' heading crowds the hero's lower edge
  - the top nav row and APPLY NOW button are cleanly aligned and evenly spaced
  confidence: medium
- id: layout_07
  family: layout_composition_components
  polarity: poor
  page_or_region: Platform — duplicated sticky feature bar
  tile_path: store/goinfusive-com/captures/2026-06-09/tiles/platform/tile-01-y01220.png
  claim: The seven-segment sticky feature bar renders twice stacked within a single viewport, two near-identical magenta strips sitting directly above one another with the section content crowded beneath.
  visible_tells:
  - two copies of the seven-segment feature bar appear stacked in the same tile
  - both strips carry the identical 'Seamless Ordering...Aligned Patient Care' labels
  - the lower content ('All your vendors. One system.') is pushed tight under the doubled bars
  confidence: high
- id: layout_08
  family: layout_composition_components
  polarity: poor
  page_or_region: Homepage — vendor logo wall over screenshot
  tile_path: store/goinfusive-com/captures/2026-06-09/tiles/homepage/tile-06-y07320.png
  claim: The vendor logo wall collides with a dashboard screenshot bleeding up from behind, so partial logos and a half-visible table overlap in the same band with no clean separating panel.
  visible_tells:
  - the top row of vendor logos is clipped at the upper frame edge
  - a faint list/table screenshot sits directly behind the named-logo row and CTA
  - the 'LEARN MORE ABOUT OUR VENDORS' pill overlaps the screenshot rather than a solid panel
  confidence: high
- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: Site-wide purple-to-magenta palette (homepage + platform heroes)
  tile_path: store/goinfusive-com/captures/2026-06-09/tiles/homepage/tile-00-y00000.png
  claim: A single purple-to-magenta gradient palette governs both pages' heroes, giving a coherent owned color identity across the site.
  visible_tells:
  - deep violet-to-magenta gradient hero background
  - magenta-red gradient APPLY NOW pill at top-right of the nav
  - the same violet field carries the white wordmark and headline
  confidence: high
  contrast_with: store/goinfusive-com/captures/2026-06-09/tiles/platform/tile-00-y00000.png
- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: CTA accent discipline (homepage)
  tile_path: store/goinfusive-com/captures/2026-06-09/tiles/homepage/tile-05-y06100.png
  claim: The magenta-to-red gradient pill is reserved consistently for primary CTAs, so the accent reads as a disciplined action color rather than decoration.
  visible_tells:
  - the 'START YOUR GROWTH JOURNEY' pill uses the same magenta-red gradient seen on other CTAs
  - the pill shape and glow treatment repeat identically across sections
  - no other element on the section borrows that accent color
  confidence: high
  contrast_with: store/goinfusive-com/captures/2026-06-09/tiles/platform/tile-08-y09760.png
- id: color_03
  family: color_brand_imagery
  polarity: mixed
  page_or_region: Platform — feature ribbon color spectrum
  tile_path: store/goinfusive-com/captures/2026-06-09/tiles/platform/tile-06-y07320.png
  claim: The horizontal feature ribbon spreads the brand across a violet-to-red spectrum of tabs, coherent in hue but diluting the accent by making the whole bar compete for attention and letting its red end mimic the CTA color.
  visible_tells:
  - seven contiguous tabs graduate from violet through magenta to red
  - no single tab is emphasized as the active state
  - the red end of the ribbon matches the primary CTA color
  confidence: medium
  contrast_with: store/goinfusive-com/captures/2026-06-09/tiles/platform/tile-07-y08540.png
- id: color_04
  family: color_brand_imagery
  polarity: mixed
  page_or_region: Homepage — recurring particle/wave texture motif
  tile_path: store/goinfusive-com/captures/2026-06-09/tiles/homepage/tile-04-y04880.png
  claim: A flowing purple wave-mesh texture recurs as a section device, giving the dark backgrounds a consistent owned visual language tied to the hero's particle field.
  visible_tells:
  - a glowing violet wave-grid mesh fills the 'Ready To Scale' band
  - the same particle/bokeh texture echoes the hero in tile-00
  - the texture stays within the established violet range
  confidence: medium
  contrast_with: store/goinfusive-com/captures/2026-06-09/tiles/homepage/tile-00-y00000.png
- id: color_05
  family: color_brand_imagery
  polarity: poor
  page_or_region: Homepage — vendor logo wall over photo/screenshot
  tile_path: store/goinfusive-com/captures/2026-06-09/tiles/homepage/tile-06-y07320.png
  claim: The vendor logo wall lays third-party marks over a busy photo-and-screenshot background with no neutral containment plate, so logos sit at uneven contrast and the top row ghosts into the dark image.
  visible_tells:
  - the upper logo row is clipped and ghosted into a dark photo
  - named marks (McKesson, ProRx, Baxter) sit on a greyed semi-transparent panel, not a clean band
  - white/grey marks float at mixed optical weights with no unifying plate
  confidence: high
  contrast_with: store/goinfusive-com/captures/2026-06-09/tiles/homepage/tile-00-y00000.png
- id: color_06
  family: color_brand_imagery
  polarity: mixed
  page_or_region: Homepage — trust-bar logo strip
  tile_path: store/goinfusive-com/captures/2026-06-09/tiles/homepage/tile-00-y00000.png
  claim: The lower trust-bar renders partner logos flat-white on dark, legible but visibly mismatched in weight and style, reading as assembled logos rather than normalized lockups.
  visible_tells:
  - wordmarks range from serif (REMEDY) to bold sans at unequal sizes
  - several marks sit at different optical weights on the same baseline
  - the strip reads as collected logos, not a unified treatment
  confidence: medium
  contrast_with: store/goinfusive-com/captures/2026-06-09/tiles/homepage/tile-06-y07320.png
- id: color_07
  family: color_brand_imagery
  polarity: poor
  page_or_region: Homepage — 'Before' warehouse slider image
  tile_path: store/goinfusive-com/captures/2026-06-09/tiles/homepage/tile-02-y02440.png
  claim: The 'Before' split-slider image of a clinician amid boxes reads as desaturated generic stock dropped against the flat purple panel with no color grading to match the palette.
  visible_tells:
  - a vertical split-slider divides a desaturated stockroom photo
  - the lighting and subject are interchangeable stock, not branded
  - the photo sits abruptly on the flat purple panel with no grading toward the palette
  confidence: medium
  contrast_with: store/goinfusive-com/captures/2026-06-09/tiles/homepage/tile-00-y00000.png
- id: color_08
  family: color_brand_imagery
  polarity: mixed
  page_or_region: Homepage — 'How It Works' photo cards
  tile_path: store/goinfusive-com/captures/2026-06-09/tiles/homepage/tile-05-y06100.png
  claim: The three Apply/Onboard/Grow step cards crop disparate stock people photos into uniform violet frames, achieving layout consistency but not a coherent owned image set.
  visible_tells:
  - each card holds a different stock scene (deskside, video call, group)
  - subjects, settings, and color temperature vary card to card
  - brand cohesion comes only from the violet card frame, not the photos
  confidence: medium
  contrast_with: store/goinfusive-com/captures/2026-06-09/tiles/homepage/tile-03-y03660.png
- id: color_09
  family: color_brand_imagery
  polarity: strong
  page_or_region: Homepage — ebook lead-magnet mockup
  tile_path: store/goinfusive-com/captures/2026-06-09/tiles/homepage/tile-07-y08063.png
  claim: The 'Stay Ahead of the Chaos' booklet mockup is rendered in the brand's own violet-magenta gradient with the same wave texture, making the asset feel native to the palette rather than borrowed.
  visible_tells:
  - the booklet cover uses the same violet-to-magenta gradient as the site
  - the cover's wave texture echoes the section background motif
  - the asset reuses cleanly across homepage and platform pages
  confidence: high
  contrast_with: store/goinfusive-com/captures/2026-06-09/tiles/platform/tile-07-y08540.png
- id: color_10
  family: color_brand_imagery
  polarity: mixed
  page_or_region: Platform — light-section palette shift
  tile_path: store/goinfusive-com/captures/2026-06-09/tiles/platform/tile-04-y04880.png
  claim: The reporting section flips to a near-white background that breaks from the dark violet system, reading clean but tonally disconnected with a sharp light/dark seam against the adjacent bands.
  visible_tells:
  - a white background hosts the dark product laptop and grey UI
  - brand purple survives only in the feature ribbon and CTA pill
  - a sharp light/dark seam separates this from the neighboring violet bands
  confidence: medium
  contrast_with: store/goinfusive-com/captures/2026-06-09/tiles/platform/tile-00-y00000.png
- id: color_11
  family: color_brand_imagery
  polarity: poor
  page_or_region: Homepage — closing two-man portrait
  tile_path: store/goinfusive-com/captures/2026-06-09/tiles/homepage/tile-07-y08063.png
  claim: The two-man portrait closing the page sits on the dark violet field with hard-cut edges and no color grading, reading as a pasted-in stock photo rather than integrated brand imagery.
  visible_tells:
  - the subjects' neutral daylight skin tones clash with the violet backdrop
  - a hard silhouette cutout with no gradient blend into the section
  - the lighting on the figures does not match the section's ambient color
  confidence: medium
  contrast_with: store/goinfusive-com/captures/2026-06-09/tiles/homepage/tile-00-y00000.png
- id: iconography_01
  family: iconography_illustration
  polarity: strong
  page_or_region: Platform — 797 Compliance feature row
  tile_path: store/goinfusive-com/captures/2026-06-09/tiles/platform/tile-06-y07320.png
  claim: The four compliance icons (magnifier-over-document, clipboard-with-cross, figure-with-checklist, checklist-with-shield) share one thin monoline stroke and a matching faceted badge frame, reading as a deliberate icon set rather than mixed clip-art.
  visible_tells:
  - a uniform thin white outline weight across all four glyphs
  - each icon seated in an identical faceted badge
  - consistent glyph size and optical centering within the badges
  confidence: high
  contrast_with: store/goinfusive-com/captures/2026-06-09/tiles/homepage/tile-02-y02440.png
- id: iconography_02
  family: iconography_illustration
  polarity: mixed
  page_or_region: Platform — 'Everything Your Clinic Needs' card icons
  tile_path: store/goinfusive-com/captures/2026-06-09/tiles/platform/tile-00-y00000.png
  claim: The top-of-card icons hold a consistent hairline monoline weight in faint circular medallions matching the rest of the platform icon system, but they sit small and dim atop the dark cards with low visual presence.
  visible_tells:
  - the same hairline stroke weight on each card icon
  - each glyph centered in a faint circular medallion at the card top
  - the glyph-to-card size ratio is small, muting their impact
  confidence: medium
- id: iconography_03
  family: iconography_illustration
  polarity: mixed
  page_or_region: Homepage — 'The result?' benefit row
  tile_path: store/goinfusive-com/captures/2026-06-09/tiles/homepage/tile-04-y04880.png
  claim: The four benefit icons (upward-arrow chart, head-with-shield, handshake, stopwatch) are clean and consistent in weight, but the metaphors are stock-generic with no bespoke detail distinguishing them from a default icon pack.
  visible_tells:
  - a uniform thin-line treatment across all four glyphs
  - the handshake and stopwatch are conventional off-the-shelf metaphors
  - no custom detail differentiates them from a stock set
  confidence: medium
- id: iconography_04
  family: iconography_illustration
  polarity: poor
  page_or_region: Homepage — pain-point list icons
  tile_path: store/goinfusive-com/captures/2026-06-09/tiles/homepage/tile-02-y02440.png
  claim: The four pain-point icons beside 'Juggling 10+ vendor accounts', 'Unstable pricing', etc. are tiny low-contrast magenta line glyphs whose internal detail muddies and barely reads against the near-black rows.
  visible_tells:
  - glyphs are small and sit in dim magenta on near-black pills
  - internal line detail blurs at the rendered size
  - each row's icon is hard to distinguish from the next
  confidence: medium
  contrast_with: store/goinfusive-com/captures/2026-06-09/tiles/platform/tile-06-y07320.png
- id: iconography_05
  family: iconography_illustration
  polarity: mixed
  page_or_region: Platform — financial 'See the true cost' dashboard render
  tile_path: store/goinfusive-com/captures/2026-06-09/tiles/platform/tile-05-y06100.png
  claim: The financial section shows real product-table UI but composites two overlapping screenshot frames with a detached circular magnifier loupe that adds no readable detail, leaving a busy, decorative stack.
  visible_tells:
  - two overlapping screenshot frames sit at different depths
  - a round magnifier loupe floats over a table edge as decoration
  - the right-edge table is partly cropped by the frame
  confidence: medium
- id: iconography_06
  family: iconography_illustration
  polarity: mixed
  page_or_region: Platform — purchase-order product UI in laptop
  tile_path: store/goinfusive-com/captures/2026-06-09/tiles/platform/tile-00-y00000.png
  claim: The 'Create Purchase Order' screenshot on the laptop is a real, internally consistent application UI with aligned form fields and an itemized order-summary panel, not a faked placeholder graphic.
  visible_tells:
  - a structured two-column form with labeled input rows
  - a right-side 'Purchase Order Summary' with itemized totals ($550.00)
  - consistent table typography within the product screen
  confidence: medium
- id: iconography_07
  family: iconography_illustration
  polarity: poor
  page_or_region: Homepage — 'Before' slider-comparison device
  tile_path: store/goinfusive-com/captures/2026-06-09/tiles/homepage/tile-02-y02440.png
  claim: The before/after slider over the storeroom photo shows a circular divider handle, but both halves look nearly identical so the device reads as a half-finished UI element rather than a designed comparison.
  visible_tells:
  - a vertical split line with a round drag-handle at center
  - the left and right halves of the photo appear almost the same
  - a 'Before' label is present with no visible 'after' contrast
  confidence: low
- id: iconography_08
  family: iconography_illustration
  polarity: mixed
  page_or_region: Homepage — 'Stay Ahead of the Chaos' ebook render
  tile_path: store/goinfusive-com/captures/2026-06-09/tiles/homepage/tile-07-y08063.png
  claim: The newsletter lead-magnet is a glossy faux-3D paperback mockup with a curled cover and cast shadow — a competent template-style product render rather than custom illustration.
  visible_tells:
  - a faux-3D book with perspective, page-edge thickness and curl
  - a generic gradient cover with stacked title text
  - a soft drop shadow typical of a stock mockup generator
  confidence: medium
```

## Provenance

Tiles read: homepage (8) + platform (10) from `captures/2026-06-09/tiles/` — all 18 active, no exclusions, no Tier-B re-render (the capture was clean). Mined blind + judged per [`/visual-evidence`](../../skills/visual-evidence/SKILL.md): four family miners saw only the tiles (no dossier, no web), the judge pruned 18 of 56 raw cards (mainly miner tile mis-citations, corrected against a verified tile-content map). Snapshot caveat: reflects the 2026-06-09 capture; the live site changes.
