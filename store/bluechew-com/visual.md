---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.0"
domain: bluechew.com
captured_at: 2026-06-15
source_capture: 2026-06-04
qa_status: exclusions-noted
---

## Visual & brand impression

BlueChew runs two visual modes. The dark homepage and product pages are controlled and confident — a single-accent black/gold/blue palette held across sections [color_01][color_02][color_03], a high-craft render of foil sachets and blue tablets [iconography_01], clean display-weight hierarchies [typography_01][typography_03], and an oversized bordered BLUECHEW wordmark anchoring every footer [color_10][layout_08]. Then it drops to template grade: the reviews page is an achromatic plain-text wall — no cards, stars, or avatars [layout_07][color_08][iconography_09] — and the about page swaps in an off-system blue hero and generic blue-circle SaaS icons [color_07][color_09][iconography_07]. Stock attribute icons [iconography_06], ungraded endorser and lifestyle photography [color_05][color_06], and an off-palette stock blood-flow infographic [color_04] keep the polish from ever being uniform.

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: "homepage hero"
  tile_path: "store/bluechew-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"
  claim: "The hero achieves a clean three-level hierarchy — massive condensed all-caps headline, a single smaller body sentence, and small grey icon-lock trust bullets — each level visually unambiguous from the others."
  visible_tells:
    - "All-caps 'HAVE BETTER SEX!' headline at heavy display weight dominates the left column"
    - "'Get hard faster and stay hard longer.' sits at a clearly smaller regular weight below it"
    - "Three icon+body trust lines render at a third, noticeably smaller grey-tint level"
  confidence: high
  contrast_with: "store/bluechew-com/captures/2026-06-04/tiles/reviews/tile-00-y00000.png"

- id: typography_02
  family: typography_hierarchy
  polarity: strong
  page_or_region: "homepage — 'Gold Standard' section"
  tile_path: "store/bluechew-com/captures/2026-06-04/tiles/homepage/tile-01-y01220.png"
  claim: "Four distinct weight-and-size levels stack legibly in one section: gold display headline, white all-caps sub-headline, grey descriptor sentence, and small ingredient callout labels — intentional scale stepping."
  visible_tells:
    - "Gold 'THE GOLD STANDARD' occupies a display tier clearly above everything else"
    - "'BOOST AROUSAL + BLOOD FLOW' uses a white all-caps mid-weight second tier"
    - "'4-in-1 Sublingual / Dissolves quickly under your tongue' drops to small grey body"
    - "Ingredient labels (Sildenafil, Tadalafil, Apomorphine, Oxytocin) with parenthetical sub-labels form a fourth, smallest tier"
  confidence: high

- id: typography_03
  family: typography_hierarchy
  polarity: strong
  page_or_region: "sildenafil product page — PDP header"
  tile_path: "store/bluechew-com/captures/2026-06-04/tiles/sildenafil/tile-00-y00000.png"
  claim: "The product name 'SIL' renders at an outsized display weight that creates immediate visual entry, with subtitle, body paragraph, and feature-tile labels each dropping to clearly differentiated smaller sizes."
  visible_tells:
    - "'SIL' appears at large display weight, white-on-black, functioning as pure display type"
    - "'Chewable with Sildenafil' sits noticeably smaller beneath it as a subtitle"
    - "Feature tiles ('As Needed Readiness', 'Up to 45MG', etc.) use mid-weight label text clearly subordinate to the headline"
  confidence: high
  contrast_with: "store/bluechew-com/captures/2026-06-04/tiles/reviews/tile-00-y00000.png"

- id: typography_04
  family: typography_hierarchy
  polarity: strong
  page_or_region: "homepage process cards"
  tile_path: "store/bluechew-com/captures/2026-06-04/tiles/homepage/tile-05-y06100.png"
  claim: "Within the four step-cards ('Choose Your Plan', 'Complete Your Medical Profile', etc.) a consistent three-part micro-hierarchy — step number, card title, descriptor — reads cleanly at small size."
  visible_tells:
    - "Step numbers ('01'-'04') appear in a very small light-weight cap at the card top-left, clearly subordinate"
    - "Card titles sit in a noticeably larger medium-weight"
    - "Descriptor lines ('Pick the chew that's right for you') render at the smallest size with reduced brightness"
  confidence: high

- id: typography_05
  family: typography_hierarchy
  polarity: strong
  page_or_region: "about page — feature list and CTA block"
  tile_path: "store/bluechew-com/captures/2026-06-04/tiles/about/tile-01-y01220.png"
  claim: "On the white about-page section, a bold feature-term / lighter-descriptor pairing ('Effective / Stronger & long-lasting erections') delivers a clean weight-only two-level micro-hierarchy, with a larger all-caps section heading marking a clear third tier."
  visible_tells:
    - "Bold labels 'Effective', 'Convenient', 'Dedicated' sit at body size but heavier than their descriptors, creating weight-only hierarchy"
    - "'ENHANCED PERFORMANCE STARTS HERE' uses all-caps bold at a larger size as a clear third tier above those labels"
  confidence: high

- id: typography_06
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "homepage — stats bar and testimonial section"
  tile_path: "store/bluechew-com/captures/2026-06-04/tiles/homepage/tile-02-y02440.png"
  claim: "The stat numerals (3X, 5X, 8X) create a strong primary level, but the section heading 'Hear It From / The Best' below uses a modest weight that reads close to body copy, blurring the heading-to-body distinction."
  visible_tells:
    - "Large white numerals '3X 5X 8X USA' dominate the upper half with clear visual primacy"
    - "'Hear It From / The Best' in the lower-left uses a weight close to surrounding copy, making its role as a section header ambiguous"
  confidence: medium
  contrast_with: "store/bluechew-com/captures/2026-06-04/tiles/homepage/tile-01-y01220.png"

- id: typography_07
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "sildenafil page — stat callout with pill image"
  tile_path: "store/bluechew-com/captures/2026-06-04/tiles/sildenafil/tile-02-y02440.png"
  claim: "The radial pill callout uses two weight levels well ('4 - 6 HOURS' vs the small 'Lasts up to'), but 'NEED IT' reads at nearly the same scale as '4 - 6 HOURS', producing two competing primary statements."
  visible_tells:
    - "'4 - 6 HOURS' and 'NEED IT' both appear in large all-caps white type at comparable sizes"
    - "The connector labels 'Lasts up to' and 'Ready when you' are the only clearly subordinate tier and are very small"
  confidence: medium

- id: typography_08
  family: typography_hierarchy
  polarity: poor
  page_or_region: "reviews page — testimonial list"
  tile_path: "store/bluechew-com/captures/2026-06-04/tiles/reviews/tile-00-y00000.png"
  claim: "Below a large 'TESTIMONIALS' headline the page collapses to a flat two-level system — bold reviewer name, uniform grey body — with no per-review weight, size, or grouping variation across long and short entries."
  visible_tells:
    - "'TESTIMONIALS' display headline at top, then each reviewer name (e.g. 'Johnny D.') in plain bold with no supporting tier"
    - "All review bodies share one size, weight, and grey tone regardless of length"
    - "No rating, date, or label tier appears between name and body text"
  confidence: high
  contrast_with: "store/bluechew-com/captures/2026-06-04/tiles/homepage/tile-01-y01220.png"

- id: typography_09
  family: typography_hierarchy
  polarity: poor
  page_or_region: "sildenafil page — 'SIL Impact' eyebrow section"
  tile_path: "store/bluechew-com/captures/2026-06-04/tiles/sildenafil/tile-04-y04880.png"
  claim: "The 'THE SIL IMPACT' eyebrow sits at nearly the same rendered height as the three claim lines it should organize, so it reads as a peer item rather than a heading above the list."
  visible_tells:
    - "'THE SIL IMPACT' spaced-cap label is only marginally smaller than '#1 Chewable in the USA' directly beneath it"
    - "No size gap, rule, or added spacing distinguishes the section label from its content lines"
  confidence: medium

- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: "homepage / hero"
  tile_path: "store/bluechew-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"
  claim: "The hero splits a left-anchored text block from a full-bleed diagonal product scatter — clean left-rail alignment while the imagery bleeds right with no hard container, a deliberate asymmetric composition over a stock split-hero."
  visible_tells:
    - "Headline, subhead, CTA, and trust icons stack flush to a consistent left edge"
    - "Gold sachets arranged diagonally across the right two-thirds with no container boundary"
    - "'5 Million+ Men Served' social-proof bar floats as a centered pill above the composition"
  confidence: high

- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: "sildenafil PDP / hero split"
  tile_path: "store/bluechew-com/captures/2026-06-04/tiles/sildenafil/tile-00-y00000.png"
  claim: "The PDP uses a clean left-image / right-content split with a tightly spaced, internally consistent 2x2 attribute grid (icon + label pairs) in the right column."
  visible_tells:
    - "Product image on a light panel left, dark spec column right, with a hard boundary between them"
    - "Four attribute tiles form an exact 2x2 grid with equal gutters and card height"
    - "Each tile's icon sits centered at the same vertical position"
  confidence: high

- id: layout_03
  family: layout_composition_components
  polarity: mixed
  page_or_region: "homepage / stat bar"
  tile_path: "store/bluechew-com/captures/2026-06-04/tiles/homepage/tile-02-y02440.png"
  claim: "The four-column stat bar (3X / 5X / 8X / USA) shares a consistent typographic system, but the fourth column substitutes a flag emoji for a numeral, breaking the rhythm set by the first three."
  visible_tells:
    - "First three columns follow large-numeral + 'X' + subline"
    - "Fourth column shows a US flag emoji in place of a numeral, with a subline that doesn't parallel the superlative structure"
  confidence: high

- id: layout_04
  family: layout_composition_components
  polarity: mixed
  page_or_region: "homepage / review card row"
  tile_path: "store/bluechew-com/captures/2026-06-04/tiles/homepage/tile-03-y03660.png"
  claim: "The review-card row is a consistent component at the atomic level (star rating, quote, avatar, label) but a partially cropped rightmost card with no visible scroll affordance leaves it ambiguous whether it is a carousel or a hard-edged grid."
  visible_tells:
    - "Four full cards plus one partial card at the right edge"
    - "No visible scroll indicator or next-arrow in the tile (a pager-dot row is small and far above)"
    - "Card widths and internal anatomy are consistent across visible instances"
  confidence: medium
  contrast_with: "store/bluechew-com/captures/2026-06-04/tiles/sildenafil/tile-03-y03660.png"

- id: layout_05
  family: layout_composition_components
  polarity: mixed
  page_or_region: "sildenafil PDP / before-after section"
  tile_path: "store/bluechew-com/captures/2026-06-04/tiles/sildenafil/tile-01-y01220.png"
  claim: "The Before/After split flanks two illustration halves with text columns of unequal weight — 'Before' carries two short lines, 'After' three — leaving the composition slightly lopsided until the centered tagline below resolves it."
  visible_tells:
    - "'Before (Without SIL)' text column carries fewer lines than the 'After' column"
    - "Centered two-line tagline ('One formula — / Better blood flow. Better performance') is the only element re-centering the symmetry"
  confidence: medium

- id: layout_06
  family: layout_composition_components
  polarity: poor
  page_or_region: "homepage / FAQ + footer region"
  tile_path: "store/bluechew-com/captures/2026-06-04/tiles/homepage/tile-05-y06100.png"
  claim: "The FAQ accordion and Important Safety block are left-aligned to roughly half the viewport with no right-side counterpart, leaving a large empty dark zone — the section does not use the full grid."
  visible_tells:
    - "FAQ accordion items span only ~45% of the page width"
    - "The entire right half of the page from the FAQ section down is empty dark space"
    - "The same truncated left-column FAQ treatment recurs in the footer tile, confirming a systemic choice"
  confidence: high
  contrast_with: "store/bluechew-com/captures/2026-06-04/tiles/homepage/tile-04-y04880.png"

- id: layout_07
  family: layout_composition_components
  polarity: poor
  page_or_region: "reviews page / testimonial list"
  tile_path: "store/bluechew-com/captures/2026-06-04/tiles/reviews/tile-00-y00000.png"
  claim: "The reviews page renders testimonials as an unstyled plain-text list — bold name over a paragraph, no cards, separators, or rating components — producing a wall of uniform body copy with no scan affordance."
  visible_tells:
    - "No card containers, bounding boxes, fills, or horizontal rules between entries"
    - "Body text at the same size and weight as surrounding paragraphs, with only the bold name differentiating"
    - "No star, date, or verified-buyer component on any entry"
  confidence: high
  contrast_with: "store/bluechew-com/captures/2026-06-04/tiles/homepage/tile-03-y03660.png"

- id: layout_08
  family: layout_composition_components
  polarity: strong
  page_or_region: "footer / wordmark tombstone"
  tile_path: "store/bluechew-com/captures/2026-06-04/tiles/homepage/tile-06-y06549.png"
  claim: "The footer closes with a full-width thin-bordered wordmark at display scale — a deliberate compositional period that gives the page a strong terminal anchor rather than a utility footer."
  visible_tells:
    - "'BLUECHEW' rendered at display size in wide-tracked caps filling nearly the full viewport width"
    - "Thin rectangular border frames the wordmark with even inset on all sides"
    - "Same element recurs on the about-page footer tile, confirming a global component"
  confidence: high

- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: "homepage hero"
  tile_path: "store/bluechew-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"
  claim: "The hero commits to a disciplined single-accent palette — near-black ground, gold foil packaging, and the blue pill — with no competing hues, an unusually controlled first impression."
  visible_tells:
    - "Dark charcoal background fills the canvas"
    - "Gold/bronze sachets are the only warm tone"
    - "Two blue tablets provide the sole cool accent, echoing the brand name"
  confidence: high

- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: "homepage — gold/black section transition"
  tile_path: "store/bluechew-com/captures/2026-06-04/tiles/homepage/tile-02-y02440.png"
  claim: "A gradient from near-black into deep amber-gold bridges the dark hero into the 'Gold Standard' band, using the packaging color as a structural background rather than just a product detail."
  visible_tells:
    - "Full-bleed amber-gold gradient fills the stat-bar band"
    - "Gradient gold matches the sachet gold from the hero tile, reinforcing coherence"
  confidence: high
  contrast_with: "store/bluechew-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"

- id: color_03
  family: color_brand_imagery
  polarity: strong
  page_or_region: "sildenafil product page — hero"
  tile_path: "store/bluechew-com/captures/2026-06-04/tiles/sildenafil/tile-00-y00000.png"
  claim: "The PDP uses a clean white-panel-left / black-panel-right split that keeps the blue tablet and black sachet legible on a neutral field while extending the dark brand voice."
  visible_tells:
    - "Left panel solid off-white, right panel solid black"
    - "Blue BC tablet on the white panel with a visible shadow, center-stage"
    - "No decorative textures or gradients in either panel"
  confidence: high

- id: color_04
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "sildenafil — before/after blood-flow illustration"
  tile_path: "store/bluechew-com/captures/2026-06-04/tiles/sildenafil/tile-01-y01220.png"
  claim: "The before/after blood-flow panel introduces orange and bright-blue CGI tonally disconnected from the gold-and-dark palette, reading as a licensed/stock infographic rather than brand-commissioned imagery."
  visible_tells:
    - "Orange/red vascular render left, vivid blue right — neither hue appears elsewhere in the system"
    - "Generic 3D cell/fluid aesthetic consistent with stock medical illustration"
    - "'Before' and 'After' labels set in warm orange and bright blue that don't match the CTA blue or gold accent"
  confidence: high
  contrast_with: "store/bluechew-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"

- id: color_05
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "homepage — celebrity endorser grid"
  tile_path: "store/bluechew-com/captures/2026-06-04/tiles/homepage/tile-02-y02440.png"
  claim: "The celebrity portrait row mixes editorial and promotional treatments whose lighting and grades are not unified, so the strip reads as assembled from different shoots rather than a directed campaign."
  visible_tells:
    - "Portraits show mixed backgrounds: dark stage, outdoor green, a graphic title card"
    - "Color temperatures vary across the visible frames"
    - "No consistent framing or color overlay to unify the strip"
  confidence: medium

- id: color_06
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "homepage — user photo grid"
  tile_path: "store/bluechew-com/captures/2026-06-04/tiles/homepage/tile-04-y04880.png"
  claim: "The 'who made the switch' lifestyle photo row varies in exposure and source quality with no unifying color treatment, so it doesn't bind to the brand palette."
  visible_tells:
    - "Five-panel strip with noticeably different exposure levels per image"
    - "Backgrounds range from outdoor daylight to indoor white to street"
    - "No duotone, tint, or overlay binding the row to the dark/gold palette"
  confidence: medium

- id: color_07
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "about page — hero"
  tile_path: "store/bluechew-com/captures/2026-06-04/tiles/about/tile-00-y00000.png"
  claim: "The about hero uses a heavily blue-shifted full-bleed photo that introduces a third color register anchored to neither the dark nor gold systems used elsewhere, then reverts to black packaging just below."
  visible_tells:
    - "Full-bleed image carries a cool teal-blue cast over the whole frame"
    - "No black ground or gold accent from the homepage system in the hero"
    - "Product sachet in the lower white section reverts to black packaging, an abrupt tonal shift within one page"
  confidence: high
  contrast_with: "store/bluechew-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"

- id: color_08
  family: color_brand_imagery
  polarity: poor
  page_or_region: "reviews page"
  tile_path: "store/bluechew-com/captures/2026-06-04/tiles/reviews/tile-00-y00000.png"
  claim: "The reviews page is entirely achromatic — white ground, black text, one blue CTA — with no brand imagery or color expression beyond the utility layer, making it visually anonymous against the dark brand pages."
  visible_tells:
    - "Pure white page background throughout"
    - "All review text in default black with only bold-name differentiation"
    - "No images, icons, or color accents except a single blue 'GET STARTED' button"
  confidence: high
  contrast_with: "store/bluechew-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"

- id: color_09
  family: color_brand_imagery
  polarity: poor
  page_or_region: "about page — feature icons"
  tile_path: "store/bluechew-com/captures/2026-06-04/tiles/about/tile-01-y01220.png"
  claim: "The 'Effective / Convenient / Dedicated' row uses pale blue-circle line-art icons on white that read as a generic SaaS template with no relationship to the brand's dark packaging aesthetic."
  visible_tells:
    - "Three light-blue circles with thin outline icons (rocket, box, 24h) at equal size"
    - "Icon style matches off-the-shelf UI icon libraries, not bespoke brand illustration"
    - "Placed on stark white with no link to the black or gold palette used elsewhere"
  confidence: high
  contrast_with: "store/bluechew-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"

- id: color_10
  family: color_brand_imagery
  polarity: strong
  page_or_region: "site-wide footer wordmark"
  tile_path: "store/bluechew-com/captures/2026-06-04/tiles/homepage/tile-06-y06549.png"
  claim: "The oversized BLUECHEW wordmark — white spaced capitals inside a thin border on black — is a distinctive, reproduction-stable brand lock-up that recurs across page templates."
  visible_tells:
    - "Full-width bordered wordmark in wide-set uppercase"
    - "Purely typographic — no logo bug or image — making it high-contrast and stable"
    - "Recurs on the about footer tile, confirming a global lock-up"
  confidence: high

- id: iconography_01
  family: iconography_illustration
  polarity: strong
  page_or_region: "homepage — hero product render"
  tile_path: "store/bluechew-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"
  claim: "The hero uses a high-production product render — gold foil sachets and blue tablets at precise angles with realistic reflections and soft shadows on a near-black gradient — genuine craft rather than a stock workaround."
  visible_tells:
    - "Multiple sachets at varying tilt angles with a consistent light source on the metallic foil"
    - "Loose tablets with cast shadows and surface specular, not flat cutouts"
    - "Tight depth-of-field feel even at this zoom"
  confidence: high

- id: iconography_02
  family: iconography_illustration
  polarity: strong
  page_or_region: "homepage — 'How to get BlueChew' step cards"
  tile_path: "store/bluechew-com/captures/2026-06-04/tiles/homepage/tile-05-y06100.png"
  claim: "The four step cards use bespoke dark-tone imagery — close-up tablet, phone-in-hand UI, glowing 24h clock-shield, kraft shipping bag — making each step visually distinct while holding a consistent dark palette and numbered system."
  visible_tells:
    - "Each card is a distinct photographic/rendered subject, not a repeated icon template"
    - "Consistent dark teal/navy cast across all four panels"
    - "Step numbers (01-04) in small text at each card's top-left"
  confidence: high
  contrast_with: "store/bluechew-com/captures/2026-06-04/tiles/about/tile-01-y01220.png"

- id: iconography_03
  family: iconography_illustration
  polarity: strong
  page_or_region: "homepage — ingredient particle diagram"
  tile_path: "store/bluechew-com/captures/2026-06-04/tiles/homepage/tile-01-y01220.png"
  claim: "The four-ingredient callout uses a single blue particle-burst graphic with leader lines to symmetric left/right ingredient labels, a custom infographic that feels designed rather than templated."
  visible_tells:
    - "Blue particle burst centered as a single composed element"
    - "Ingredient labels split two to a left rail (Sildenafil, Tadalafil) and two to a right rail (Apomorphine, Oxytocin)"
    - "Particle color matches the product blue, reinforcing the brand link"
  confidence: high

- id: iconography_04
  family: iconography_illustration
  polarity: strong
  page_or_region: "sildenafil PDP — pill-with-callout diagram"
  tile_path: "store/bluechew-com/captures/2026-06-04/tiles/sildenafil/tile-02-y02440.png"
  claim: "A centered blue tablet with two asymmetric leader lines ('Lasts up to 4-6 HOURS' / 'Ready when you NEED IT') makes the pill itself the graphic anchor, showing confident use of negative space."
  visible_tells:
    - "Single tablet floats centered on black with no container or background fill"
    - "Two label lines emerge at different angles, not a symmetric template"
    - "Mixed type sizes within each label create internal hierarchy"
  confidence: high

- id: iconography_05
  family: iconography_illustration
  polarity: mixed
  page_or_region: "sildenafil PDP — before/after mechanism illustration"
  tile_path: "store/bluechew-com/captures/2026-06-04/tiles/sildenafil/tile-01-y01220.png"
  claim: "The 'How Bluechew SIL works' panel splits a red/orange restricted-flow motif from a blue increased-flow motif — a custom visual metaphor that conveys mechanism without a clinical diagram, though its stock-render aesthetic sits off the brand palette."
  visible_tells:
    - "Hard vertical center split with a warm-to-cool color shift"
    - "Left: organic red cell shapes in amber fluid; right: blue translucent bubbles in luminous waves"
    - "Directional flow arrows reinforce the before/after read"
  confidence: high

- id: iconography_06
  family: iconography_illustration
  polarity: mixed
  page_or_region: "sildenafil PDP — feature attribute icons"
  tile_path: "store/bluechew-com/captures/2026-06-04/tiles/sildenafil/tile-00-y00000.png"
  claim: "The four product-attribute tiles use thin-line circular icons (lightning, wifi-arc, hourglass, pill) that are functionally distinct but feel pulled from a generic outline library rather than drawn for the brand."
  visible_tells:
    - "Lightning-in-circle, wifi-arc, hourglass, and circular pill — common stock icon forms"
    - "Uniform stroke weight and radius suggesting a library set"
    - "Monochrome white-on-dark with no brand-color differentiation"
  confidence: high
  contrast_with: "store/bluechew-com/captures/2026-06-04/tiles/sildenafil/tile-01-y01220.png"

- id: iconography_07
  family: iconography_illustration
  polarity: mixed
  page_or_region: "about page — value-prop icon row"
  tile_path: "store/bluechew-com/captures/2026-06-04/tiles/about/tile-01-y01220.png"
  claim: "The three feature icons (rocket / box / 24h shield) in light-blue circles use distinct metaphors but the rocket-for-effectiveness mapping is a generic SaaS convention and none share anything proprietary with the product."
  visible_tells:
    - "Rocket-in-blue-circle for 'Effective' — a common growth/performance stock metaphor"
    - "Box-delivery icon for 'Convenient' — standard e-commerce form"
    - "24h shield icon for 'Dedicated' — same motif reused from the homepage step card"
  confidence: high
  contrast_with: "store/bluechew-com/captures/2026-06-04/tiles/homepage/tile-05-y06100.png"

- id: iconography_08
  family: iconography_illustration
  polarity: poor
  page_or_region: "homepage — reviewer avatar icons"
  tile_path: "store/bluechew-com/captures/2026-06-04/tiles/homepage/tile-03-y03660.png"
  claim: "Review-card avatars use a generic grey circular person-silhouette placeholder repeated identically across cards — the default avatar seen in countless review widgets, with no brand-differentiated treatment."
  visible_tells:
    - "Small grey circle with a white person silhouette beside each reviewer name"
    - "Identical across all visible review cards, no personalization"
    - "Plain yellow star row with no styled rating graphic"
  confidence: high
  contrast_with: "store/bluechew-com/captures/2026-06-04/tiles/sildenafil/tile-01-y01220.png"

- id: iconography_09
  family: iconography_illustration
  polarity: poor
  page_or_region: "reviews page — testimonials layout"
  tile_path: "store/bluechew-com/captures/2026-06-04/tiles/reviews/tile-00-y00000.png"
  claim: "The testimonials page carries zero iconographic or illustrative elements — no avatars, no star icons, no dividers — only a typographic header over plain text, offering no visual-craft signals."
  visible_tells:
    - "Name + paragraph only; no stars, avatars, or divider illustration"
    - "White ground, left-aligned body with no differentiation between entries"
    - "'TESTIMONIALS' header is typographic only"
  confidence: high
```

## Provenance

- **Tiles read (active, 20):** `captures/2026-06-04/tiles/` — homepage (tile-00…06, 7), sildenafil (tile-00…06, 7), reviews (tile-00…02, 3), about (tile-00…02, 3). Pages chosen to carry the visual system: dark homepage + product PDP, plus the reviews and about pages where execution diverges.
- **Exclusion (1):** `gold-plan/tile-00-y00000.png` — a plan-selector modal composited over a dimmed/greyed page plus a cookie banner; no readable page layout sits behind the scrim, so it is unusable as visual-system evidence (not a poor-design example). The page was dropped from mining; `qa_status: exclusions-noted`.
- **Cookie-banner caveat (kept tiles):** a site-wide "BlueChew uses cookies… Dismiss" consent banner overlays the lower portion of four hero tiles (homepage/tile-00, sildenafil/tile-00, about/tile-00, reviews/tile-00). The load-bearing evidence (hero headlines, PDP spec block, testimonial wall) sits in the clean upper region of each, so the tiles stayed active; the blind miner/judge protocol treats consent banners as a capture artifact, and the judge rejected the two cards whose specific tell sat inside the banner zone (an about-hero layout section-break card and an about-hero orbiting-dots iconography card). No tile was re-rendered — this is `exclusions-noted`, not `recapture-used`.
- **Mining:** blind fan-out via `/visual-evidence` — 4 family miners (Sonnet) over the active tiles only → judge (Opus) pruned 51 raw cards to 36 accepted (9 typography, 8 layout, 10 color, 9 iconography), preserving a strong/mixed/poor spread per family.
- **Snapshot caveat:** point-in-time read of the 2026-06-04 capture. The live site changes; re-tile and re-mine to refresh.
