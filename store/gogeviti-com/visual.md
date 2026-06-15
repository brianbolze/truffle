---
schema_version: "1.0"
domain: gogeviti.com
captured_at: 2026-06-15
source_capture: 2026-06-03
qa_status: clean
---

## Visual & brand impression

Geviti runs a confident editorial type system — a small upright-sans label over a large italic-serif display head, repeated as a structural motif across pages and inner heroes [typography_01][typography_02][typography_05], with oversized serif numerals as their own display tier [typography_03]. A disciplined navy / warm-cream / sky-blue palette and one reserved CTA pill carry that control [color_02][color_03][color_05], reaching even owned branded packaging [color_06], and the component systems — comparison tables, biomarker rows, plan grids — are tidy [layout_03][layout_04][layout_05]. But the icon layer betrays it: stock Apple emoji and mismatched 3D renders pulled from different sets [iconography_01][iconography_02][iconography_06], alongside off-palette color leaks [color_09][color_10]. The lone craft standout is the in-app data-viz mockup [iconography_04].

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: Homepage hero — dual-font heading system
  tile_path: store/gogeviti-com/captures/2026-06-03/tiles/homepage/tile-00-y00000.png
  claim: 'The hero runs a deliberate two-font hierarchy: a small upright sans label line over a large italic serif display head (''Built For More Healthy Years''), giving a clean two-level signal.'
  visible_tells:
  - Small upright sans label sits directly above the display head at roughly a quarter of its size
  - Display head is a wide italic serif, visually distinct from every other type element on the tile
  - Sub-line and CTA pill drop to a much smaller sans, completing the cascade
  confidence: high
  contrast_with: store/gogeviti-com/captures/2026-06-03/tiles/homepage/tile-01-y01220.png
- id: typography_02
  family: typography_hierarchy
  polarity: strong
  page_or_region: Homepage — repeated section-heading motif
  tile_path: store/gogeviti-com/captures/2026-06-03/tiles/homepage/tile-01-y01220.png
  claim: The sans-label / italic-serif-display pairing ('Three Steps' over 'Zero Waiting Rooms', 'How Geviti works') repeats as a structural motif down the homepage, a reliable hierarchy signal across sections.
  visible_tells:
  - '''Three Steps'' set small and upright in sans'
  - '''Zero Waiting Rooms'' set several times larger in the same italic serif as the hero'
  - Same pattern recurs with 'How Geviti works' label earlier on the tile
  confidence: high
- id: typography_03
  family: typography_hierarchy
  polarity: strong
  page_or_region: Homepage — statistical callout block
  tile_path: store/gogeviti-com/captures/2026-06-03/tiles/homepage/tile-02-y02440.png
  claim: Oversized italic serif numerals ('78%', '93%', '4.9') act as a distinct display level over small light-sans descriptors, producing a clear multi-level hierarchy that holds over the off-white background.
  visible_tells:
  - Stat numerals are very large italic serif in deep navy
  - Descriptor text beneath each figure is small light-weight sans
  - Navy figures vs near-black sans descriptors add a color differentiation axis
  confidence: high
- id: typography_04
  family: typography_hierarchy
  polarity: mixed
  page_or_region: Homepage — three-step process cards body text
  tile_path: store/gogeviti-com/captures/2026-06-03/tiles/homepage/tile-01-y01220.png
  claim: Inside the three-step cards the 'Step 1' label, bold card title, and body copy sit at very close sizes, compressing the within-card hierarchy so title and body are hard to separate at a glance.
  visible_tells:
  - '''Step 1'', bold card title, and body paragraph all live in a narrow size band'
  - Weight (medium vs regular) is the main differentiator with little size gap between title and body
  - Body copy wraps to several lines at a size close to the card title
  confidence: high
  contrast_with: store/gogeviti-com/captures/2026-06-03/tiles/homepage/tile-02-y02440.png
- id: typography_05
  family: typography_hierarchy
  polarity: strong
  page_or_region: Bloodwork page — feature-page hero
  tile_path: store/gogeviti-com/captures/2026-06-03/tiles/bloodwork/tile-00-y00000.png
  claim: The bloodwork hero reuses the two-font template cleanly ('The Blood Test That' in small sans over 'Changes Everything.' in large italic serif), showing the hierarchy system travels to inner pages.
  visible_tells:
  - Small near-black upright sans label above the display head
  - Italic serif display head several times the label size
  - Sub-headline drops to a mid-weight sans at roughly half the display size for a three-level cascade
  confidence: high
- id: typography_06
  family: typography_hierarchy
  polarity: strong
  page_or_region: Supplements page — comparison card micro-typography
  tile_path: store/gogeviti-com/captures/2026-06-03/tiles/supplements/tile-02-y02440.png
  claim: 'The ''Generic Supplements vs Longeviti Blend'' table uses confident restraint: light-weight row labels, medium-weight values at the same size, and color/flag offloading a level — scannable without piling on type sizes.'
  visible_tells:
  - Row labels ('Formulation', 'Ingredients') are visibly lighter than their values
  - Red/green flag marks carry a third level instead of more type variation
  - Card titles ('Generic Supplements', 'Longeviti Blend') are bold and about twice the row-text size, anchoring each card
  confidence: high
- id: typography_07
  family: typography_hierarchy
  polarity: mixed
  page_or_region: Blueprint page — 'THE OLD WAY / THE GEVITI WAY' headings
  tile_path: store/gogeviti-com/captures/2026-06-03/tiles/blueprint/tile-01-y01220.png
  claim: These comparison headings switch from the site's standard italic serif to all-caps upright sans, breaking the established heading language with no clear rationale.
  visible_tells:
  - '''THE OLD WAY'' and ''THE GEVITI WAY'' are all-caps upright sans, unlike every other section head on the site'
  - The departure from the italic serif pattern makes the block read as a different design language
  - Body text beneath stays the standard small sans, so the break is specifically at the heading level
  confidence: medium
  contrast_with: store/gogeviti-com/captures/2026-06-03/tiles/blueprint/tile-02-y02440.png
- id: typography_08
  family: typography_hierarchy
  polarity: strong
  page_or_region: Homepage — dark-background closing CTA
  tile_path: store/gogeviti-com/captures/2026-06-03/tiles/homepage/tile-06-y07320.png
  claim: On the deep-blue gradient, 'Life Is Long.' over 'Make Sure Your Body Keeps Up' holds hierarchy in white at high contrast, with the label dropping to the same white at clearly reduced size.
  visible_tells:
  - White type on dark navy gradient reads at strong contrast for both levels
  - Label-to-display size ratio matches the light-background sections
  - No competing text on the section background keeps the hierarchy uncluttered
  confidence: high
- id: typography_09
  family: typography_hierarchy
  polarity: strong
  page_or_region: Blueprint page — five-step process cards
  tile_path: store/gogeviti-com/captures/2026-06-03/tiles/blueprint/tile-03-y03660.png
  claim: The five-step cards ('Test / Analyze / Build / Deliver / Repeat') run a tight but consistent two-level micro-hierarchy (bold title over light descriptor) that never confuses levels across the row.
  visible_tells:
  - Card title bold weight is clearly heavier than the descriptor line
  - Consistent title-to-descriptor gap across all five cards
  - Section head above ('Your Protocol Never Stops / Working For You.') uses the standard italic serif, correctly anchoring the cards as subordinate
  confidence: high
- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: Homepage — hero composition
  tile_path: store/gogeviti-com/captures/2026-06-03/tiles/homepage/tile-00-y00000.png
  claim: The hero is a clean two-zone composition — a thin promo bar over a full-bleed sky photo with a centered content column — with generous padding and nothing colliding for the axis.
  visible_tells:
  - Centered headline and CTA stack sit well inside the implied column with breathing room both sides
  - Trust icons (physician, tests, clinical-grade) are evenly spaced beneath the button without crowding it
  confidence: high
- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: Homepage — 'How Geviti works' 2x2 feature grid
  tile_path: store/gogeviti-com/captures/2026-06-03/tiles/homepage/tile-01-y01220.png
  claim: The 2x2 feature cards apply a consistent template — icon left, text right, uniform card height, equal gutters — with no visible misalignment.
  visible_tells:
  - All four cards share identical internal padding and a left-aligned text baseline
  - The gutter between left and right cards is visually equal across both rows
  confidence: high
  contrast_with: store/gogeviti-com/captures/2026-06-03/tiles/homepage/tile-00-y00000.png
- id: layout_03
  family: layout_composition_components
  polarity: strong
  page_or_region: Supplements page — Generic vs Longeviti comparison cards
  tile_path: store/gogeviti-com/captures/2026-06-03/tiles/supplements/tile-02-y02440.png
  claim: 'The two-column comparison is the most compositionally controlled component in the set: equal card widths, aligned row labels, and a flag column locked to each card''s right edge.'
  visible_tells:
  - Seven attribute rows align horizontally across both cards with no row-height drift
  - Red/green flag marks are right-flush within each column, not free-floating
  confidence: high
- id: layout_04
  family: layout_composition_components
  polarity: strong
  page_or_region: Bloodwork page — biomarker category cards
  tile_path: store/gogeviti-com/captures/2026-06-03/tiles/bloodwork/tile-03-y03660.png
  claim: 'The biomarker category list uses a strict repeated component: left icon, bold category title, light biomarker subtext, and a right-flush ''Show all N biomarkers'' pill — every row conforms.'
  visible_tells:
  - Icon-to-title baseline is consistent across all visible rows
  - The pill button stays right-flush at the same horizontal position in each row
  - Inter-row spacing is uniform with no orphaned gaps
  confidence: high
- id: layout_05
  family: layout_composition_components
  polarity: strong
  page_or_region: Homepage — inline Plus plan card
  tile_path: store/gogeviti-com/captures/2026-06-03/tiles/homepage/tile-04-y04880.png
  claim: The Plus plan card uses a precise 3x2 icon grid for feature callouts and right-justifies the price to create a clean price-vs-name axis at the card header.
  visible_tells:
  - Six feature icons sit in a 3x2 grid with equal cell widths and vertical spacing
  - '''$127/mo'' is right-flush at the same vertical level as ''Plus / Most Popular'' on the left'
  confidence: high
- id: layout_06
  family: layout_composition_components
  polarity: mixed
  page_or_region: Homepage — testimonial carousel
  tile_path: store/gogeviti-com/captures/2026-06-03/tiles/homepage/tile-02-y02440.png
  claim: The horizontal testimonial carousel clips its first and last cards unevenly — the leftmost is almost fully cut while the rightmost crops mid-quote — so the scroll offset reads as untuned rather than a balanced peek.
  visible_tells:
  - Leftmost 'Lindsay B.' card is truncated to a thin sliver of visible width
  - Rightmost card clips a quote mid-sentence at an awkward break
  confidence: medium
  contrast_with: store/gogeviti-com/captures/2026-06-03/tiles/supplements/tile-03-y03660.png
- id: layout_07
  family: layout_composition_components
  polarity: mixed
  page_or_region: Blueprint page — AI chat mockup with floating bubbles
  tile_path: store/gogeviti-com/captures/2026-06-03/tiles/blueprint/tile-02-y02440.png
  claim: The question-bubble elements flanking the central chat UI sit at differing vertical heights and inconsistent left/right offsets, giving the composition an ad-hoc rather than intentionally layered feel.
  visible_tells:
  - Left-side bubbles ('trending down over the last 3 panels?' and 'Based on my genetics...') are not aligned to a common grid line
  - Right-side bubble ('What should I do about my elevated hsCRP?') floats at a different baseline than the left ones, breaking implied symmetry
  confidence: medium
- id: layout_08
  family: layout_composition_components
  polarity: mixed
  page_or_region: Homepage — closing CTA photo collage
  tile_path: store/gogeviti-com/captures/2026-06-03/tiles/homepage/tile-06-y07320.png
  claim: The closing CTA stacks four rounded photo cards at slight irregular rotations against the dark gradient; the angles don't follow an evident progression, so the collage reads more decorative than art-directed.
  visible_tells:
  - Four photo cards are offset at different small rotation amounts with no clear angular sequence
  - The arrangement is a loose overlapping row rather than a deliberate grid or fan
  confidence: medium
  contrast_with: store/gogeviti-com/captures/2026-06-03/tiles/supplements/tile-02-y02440.png
- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: Homepage — hero palette
  tile_path: store/gogeviti-com/captures/2026-06-03/tiles/homepage/tile-00-y00000.png
  claim: The hero commits to one palette — deep navy type on a photographic blue-sky background — with no competing accent color at the site's most prominent placement.
  visible_tells:
  - Sky photo bleeds full width with no clashing overlay
  - All hero type and CTA label render in one near-black navy
  - The top promo bar uses a dark navy fill echoing the text color rather than an arbitrary accent
  confidence: high
- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: Homepage / pricing / blueprint — recurring warm-cream section background
  tile_path: store/gogeviti-com/captures/2026-06-03/tiles/homepage/tile-04-y04880.png
  claim: A warm cream-to-pale-sand background recurs across content sections on multiple pages, functioning as a deliberate off-white house tone rather than default white.
  visible_tells:
  - Warm beige-cream behind the plan card section here
  - The same warm tone recurs on the blueprint protocol section and supplements stat blocks
  - Tone is consistently warmer than pure white across pages
  confidence: high
  contrast_with: store/gogeviti-com/captures/2026-06-03/tiles/blueprint/tile-03-y03660.png
- id: color_03
  family: color_brand_imagery
  polarity: strong
  page_or_region: All pages — primary CTA button treatment
  tile_path: store/gogeviti-com/captures/2026-06-03/tiles/homepage/tile-04-y04880.png
  claim: Primary CTAs use a single muted sky-blue pill with dark navy label, held to one color and shape across every page with no hue or geometry variation.
  visible_tells:
  - '''Start with Plus'' and ''See All Plans'' on this tile share the same muted blue fill and pill radius'
  - The same pill recurs as 'Start Free', 'Get My Blend', 'See Your Blueprint', 'Meet Makor AI' across other pages with no alternate color
  confidence: high
- id: color_04
  family: color_brand_imagery
  polarity: strong
  page_or_region: Homepage — closing section / footer
  tile_path: store/gogeviti-com/captures/2026-06-03/tiles/homepage/tile-06-y07320.png
  claim: The closing section uses a deep layered blue echoing the hero sky as a full-bleed background, bookending the page with a coherent color story.
  visible_tells:
  - Blue mountain landscape forms the background and transitions into the deep navy footer
  - Rounded lifestyle photo cards sit against the blue, holding contrast without introducing new hues
  confidence: high
  contrast_with: store/gogeviti-com/captures/2026-06-03/tiles/homepage/tile-00-y00000.png
- id: color_05
  family: color_brand_imagery
  polarity: strong
  page_or_region: Multiple pages — typographic color control
  tile_path: store/gogeviti-com/captures/2026-06-03/tiles/homepage/tile-02-y02440.png
  claim: Large display numerals and italic serif headlines consistently render in the same deep navy across pages and section types, showing color used as a typographic control rather than decoration.
  visible_tells:
  - '''78%'', ''93%'', ''4.9'' all render in deep navy on warm cream'
  - The same navy carries the italic display heads ('Real Results.', 'To Invest In Their Future') with no headline in a different color across tiles
  confidence: high
- id: color_06
  family: color_brand_imagery
  polarity: strong
  page_or_region: Supplements page — branded product photography
  tile_path: store/gogeviti-com/captures/2026-06-03/tiles/supplements/tile-02-y02440.png
  claim: The Geviti 'Longeviti blend' box shows a designed geometric tile pattern in navy/blue on cream cardstock — owned branded product imagery that extends the site palette into physical goods.
  visible_tells:
  - The carton carries a custom navy/blue geometric tile pattern on cream paperstock
  - A matching single-pill packet beside it carries the same motif, indicating a real designed packaging system
  confidence: high
- id: color_07
  family: color_brand_imagery
  polarity: mixed
  page_or_region: Bloodwork page — footer CTA landscape
  tile_path: store/gogeviti-com/captures/2026-06-03/tiles/bloodwork/tile-04-y04880.png
  claim: The bloodwork page closes on a golden-hour desert/mountain photo that introduces warm amber and orange tones absent from the rest of the site, an orphaned color moment not echoed elsewhere.
  visible_tells:
  - Full-bleed golden-hour landscape with orange sky and warm rock colors fills the lower half
  - No comparable warm amber/orange appears in any other page's CTA section, which use navy/blue or cream
  confidence: high
  contrast_with: store/gogeviti-com/captures/2026-06-03/tiles/homepage/tile-06-y07320.png
- id: color_08
  family: color_brand_imagery
  polarity: mixed
  page_or_region: Pricing page — Infinite tier card background
  tile_path: store/gogeviti-com/captures/2026-06-03/tiles/pricing/tile-01-y01220.png
  claim: The 'Infinite' card uses a warm peach-to-cream gradient unique to this one card, reading as a one-off decision rather than a system-level differentiation tone.
  visible_tells:
  - The Infinite card sits on a distinct warm salmon/peach-to-cream gradient
  - No analogous warm gradient appears on the other pricing tiers or any other content section
  confidence: high
- id: color_09
  family: color_brand_imagery
  polarity: poor
  page_or_region: Supplements page — AM/PM supplement pack cards
  tile_path: store/gogeviti-com/captures/2026-06-03/tiles/supplements/tile-00-y00000.png
  claim: The AM/PM pack cards pair a warm yellow and a pale lavender background that are not grounded in the site's navy-cream-sky-blue palette, weakening overall palette coherence.
  visible_tells:
  - '''AM Supplement Pack'' card sits on a warm yellow background'
  - '''PM Supplement Pack'' card sits on a pale lavender/lilac background'
  - Neither yellow nor lavender appears as a named accent elsewhere on the page
  confidence: high
  contrast_with: store/gogeviti-com/captures/2026-06-03/tiles/homepage/tile-00-y00000.png
- id: color_10
  family: color_brand_imagery
  polarity: poor
  page_or_region: Bloodwork page — panel comparison photography
  tile_path: store/gogeviti-com/captures/2026-06-03/tiles/bloodwork/tile-01-y01220.png
  claim: The comparison pairs a warm-toned consultation photo with a cold desaturated grey surgeon photo; the temperature mismatch inside one two-up layout reads as stock-photo assembly rather than intentional contrast.
  visible_tells:
  - 'Left ''Longeviti Panel'' card: warm amber-brown skin tones in soft indoor light'
  - 'Right ''Traditional Full Panel'' card: cool grey-white clinical scrubs at high contrast, with no bridging color treatment'
  confidence: high
- id: color_11
  family: color_brand_imagery
  polarity: mixed
  page_or_region: Homepage / supplements — lavender section-transition wash
  tile_path: store/gogeviti-com/captures/2026-06-03/tiles/homepage/tile-05-y06100.png
  claim: A pale lavender-to-white wash appears under the FAQ/mission section, adding a third background tone alongside cream and deep blue that isn't fully systematized.
  visible_tells:
  - Lower half of this tile fades to a subtle blue-violet wash, cooler than the warm cream above it
  - The same lilac wash recurs on the supplements FAQ section, so it repeats but sits between cream and deep-blue without a clear rule
  confidence: medium
  contrast_with: store/gogeviti-com/captures/2026-06-03/tiles/homepage/tile-04-y04880.png
- id: iconography_01
  family: iconography_illustration
  polarity: poor
  page_or_region: Homepage — 'How Geviti works' feature card icons
  tile_path: store/gogeviti-com/captures/2026-06-03/tiles/homepage/tile-01-y01220.png
  claim: The feature-card icons mix mismatched 3D/emoji styles — a glossy molecular cluster, a cartoon AI robot, a green/blue recycling-arrow mark, and a flat blue hex-cluster — reading as lifted from separate icon sets rather than one system.
  visible_tells:
  - The AI robot is a cartoonish 3D toy figure while the recycle mark is a flat 2D arrow glyph
  - The molecular/orbit graphic uses a high-gloss style not shared by the flat blue hex cluster
  - No shared rendering style, shadow direction, or color temperature across the four
  confidence: high
  contrast_with: store/gogeviti-com/captures/2026-06-03/tiles/bloodwork/tile-02-y02440.png
- id: iconography_02
  family: iconography_illustration
  polarity: poor
  page_or_region: Bloodwork page — biomarker category icons
  tile_path: store/gogeviti-com/captures/2026-06-03/tiles/bloodwork/tile-03-y03660.png
  claim: The biomarker category icons are stock Apple emoji used directly (lightning bolt, kidney, anatomical heart, conductor figure, flame) rather than a custom or licensed icon system, reading as placeholder-grade.
  visible_tells:
  - Lightning bolt for Metabolic Health is the standard yellow emoji
  - Kidney for Kidney and Liver Function is the kidney emoji
  - Anatomical heart for Cardiovascular and a conductor/person figure for Hormones are recognizable system emoji
  confidence: high
- id: iconography_03
  family: iconography_illustration
  polarity: poor
  page_or_region: Blueprint page — five-step process icons
  tile_path: store/gogeviti-com/captures/2026-06-03/tiles/blueprint/tile-03-y03660.png
  claim: The five process icons (test-tube rack, robot head, construction helmet+board, cardboard box, recycling arrows) reuse the heterogeneous stock-3D-emoji pool seen site-wide; the flat 2D recycling arrows in particular clash with the 3D objects beside them.
  visible_tells:
  - Test-tube rack is a colorful 3D render, the robot head is a grey flat-ish cartoon, the construction scene is a warm 3D prop
  - The 'Repeat' icon is a flat green/blue circular-arrow mark, visually inconsistent with the 3D renders around it
  confidence: high
  contrast_with: store/gogeviti-com/captures/2026-06-03/tiles/homepage/tile-04-y04880.png
- id: iconography_04
  family: iconography_illustration
  polarity: strong
  page_or_region: Bloodwork page — three-phone app UI mockup
  tile_path: store/gogeviti-com/captures/2026-06-03/tiles/bloodwork/tile-02-y02440.png
  claim: The triple-phone product render shows credibly designed app UI — circular progress arcs, a PhenoAge segmented ring, and color-coded biomarker lists — the most purposeful and internally consistent graphic work on the site.
  visible_tells:
  - All three screens share the same arc/gauge motif at consistent size with a green/yellow/amber status logic
  - The PhenoAge '38' segmented ring with centered number is a deliberate data-viz choice, not emoji or clip art
  confidence: high
  contrast_with: store/gogeviti-com/captures/2026-06-03/tiles/bloodwork/tile-03-y03660.png
- id: iconography_05
  family: iconography_illustration
  polarity: mixed
  page_or_region: Homepage — Plus plan feature icons
  tile_path: store/gogeviti-com/captures/2026-06-03/tiles/homepage/tile-04-y04880.png
  claim: The six plan-feature icons share a warm 3D clay-render style (blood tube, blood-draw arm, stethoscope+Rx, blueprint scroll, discount tag), more cohesive than the 'How Geviti works' row — but the provider figure breaks the object-only pattern and scale/shadow depth still vary.
  visible_tells:
  - Blood tube, orange discount tag, and blueprint scroll share a similar warm clay-render with baked shadows
  - The provider icon shifts to a fully figurative human illustration, breaking the object-only pattern of the other five
  confidence: high
  contrast_with: store/gogeviti-com/captures/2026-06-03/tiles/homepage/tile-01-y01220.png
- id: iconography_06
  family: iconography_illustration
  polarity: poor
  page_or_region: Supplements page — AM/PM pack icons
  tile_path: store/gogeviti-com/captures/2026-06-03/tiles/supplements/tile-00-y00000.png
  claim: The AM and PM pack cards use a sun emoji and a crescent-moon emoji as their only identifiers — stock system emoji standing in for designed product symbols.
  visible_tells:
  - AM card shows the standard yellow sun emoji in the corner
  - PM card shows an unmodified crescent-moon emoji
  confidence: high
- id: iconography_07
  family: iconography_illustration
  polarity: mixed
  page_or_region: Pricing page — Infinite tier feature icons
  tile_path: store/gogeviti-com/captures/2026-06-03/tiles/pricing/tile-01-y01220.png
  claim: The Infinite feature icons mostly share the warm 3D clay-render palette (supplement jar, microscope) but the concierge bell shifts to a metallic copper/gold finish and the doctor figure again breaks the object-only pattern.
  visible_tells:
  - Supplement jar and microscope carry matte warm baked shadows while the concierge bell has a metallic copper/gold finish
  - The dedicated-physician icon is a figurative human illustration, not an object icon like the rest
  confidence: medium
- id: iconography_08
  family: iconography_illustration
  polarity: mixed
  page_or_region: Homepage — problem statement cards (red X badges)
  tile_path: store/gogeviti-com/captures/2026-06-03/tiles/homepage/tile-00-y00000.png
  claim: The five problem cards each use only a red circular 'X' badge as their icon — adequate as a negative signal but a barebones mark with no illustration craft, leaning entirely on color for meaning.
  visible_tells:
  - Each card's only graphic is a solid red circle with a white X
  - No card carries a secondary glyph to reinforce its specific problem statement
  confidence: high
  contrast_with: store/gogeviti-com/captures/2026-06-03/tiles/bloodwork/tile-02-y02440.png
```

## Provenance

- **Tiles read** — 35 native-resolution tiles across 5 pages (homepage, pricing, bloodwork, supplements, blueprint), sliced from the `captures/2026-06-03/` payloads. These are the pages carrying the visual system; the capture also held faq/clinic/testing/genetics, not mined.
- **QA gate** — `clean`. No modals, cookie banners, blank/grey heroes, black media cards, or mid-animation captures in any kept tile; **no exclusions, no Tier-B browser re-render**. (The supplements `tile-04` is cropped at a section seam — the judge rejected two cards that leaned on that seam as unverifiable, but the tile itself is not contaminated.)
- **Mining** — 4 blind family miners (Sonnet) over the active tiles → judge (Opus) pruned 53 raw cards to the 36 accepted here, across all four families with a calibrated strong/mixed/poor spread. The judge also rejected several confidently-wrong tells (e.g. a "Coming Soon overlay renders text illegible" claim where the watermark sits in clear space; a "Free column half the width of Plus" claim where the cards are equal width).
- **Snapshot caveat** — a point-in-time read of the captured 2026-06-03 tiles; the live site changes independently of this file.
