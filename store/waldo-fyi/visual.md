---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.0"
domain: waldo.fyi
captured_at: 2026-06-18
source_capture: 2026-06-18
qa_status: recapture-used
---

## Visual & brand impression

A polished, premium dark-mode product brand. A disciplined near-black ground, white text, and one warm accent per surface [color_01], plus a signature multi-color gradient "orb" that stands in for photography [color_02], set the tone; each product page swaps the hero atmosphere — teal on Monitor [color_06], amber on Strategize [color_07] — echoed in per-page FAQ accent colors [color_04]. Layout is the strongest suit: a centered hero column [layout_01] and repeated equal-height card and two-column components hold a reliable rhythm site-wide [layout_02, layout_06]. Type cascades cleanly at the page and stat level [typography_01, typography_03] but compresses inside product cards and testimonials [typography_05, typography_08]. Custom product-UI renders read as credible [iconography_03, iconography_06]; the weak spots are content-free decorative orbs [iconography_09], bare "+" toggles [iconography_10], an unevenly-weighted logo strip [color_12], and a pacing dead-zone between sections [layout_12].

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: "Homepage hero"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/homepage/tile-00-y00000.png"
  claim: "The hero establishes a clear two-level read: a large medium-weight display headline over a smaller, lighter-weight subhead, separated by adequate leading."
  visible_tells:
    - "Display headline 'Waldo's AI agents are built by marketers...' renders clearly larger than the subhead line beneath it"
    - "Subhead 'Culture moves. Consumers shift...' is a visibly thinner weight, reinforcing level separation without relying on color"
  confidence: high
- id: typography_02
  family: typography_hierarchy
  polarity: strong
  page_or_region: "FAQ section (recurs on every page)"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/homepage/tile-06-y07320.png"
  claim: "The 'FAQs' heading is set in a very large bold weight as an unambiguous section entry, while every accordion question sits at one consistent smaller size and weight — a clean, scannable two-level read."
  visible_tells:
    - "'FAQs' heading is roughly 4x the size of the accordion question text"
    - "All accordion questions render at identical size and weight, producing rhythmic rows with no hierarchy noise"
  confidence: high
  contrast_with: "store/waldo-fyi/captures/2026-06-18/tiles/build/tile-04-y04880.png"
- id: typography_03
  family: typography_hierarchy
  polarity: strong
  page_or_region: "Strategize page — stat block"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/strategize/tile-01-y01220.png"
  claim: "Stat numerals ('150 hrs', '$30K', '85%') are set in a dramatically oversized display weight with a small regular descriptor line below each — a deliberate number / unit / descriptor mini-hierarchy executed cleanly."
  visible_tells:
    - "Numeral glyphs are several times the size of their descriptor lines"
    - "Unit suffixes ('hrs', 'K', '%') are set noticeably smaller than the numerals, adding a sub-level inside the number itself"
  confidence: high
- id: typography_04
  family: typography_hierarchy
  polarity: strong
  page_or_region: "Monitor hero"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/monitor/tile-00-y00000.png"
  claim: "A small all-caps eyebrow ('MONITOR') precedes the large headline and subhead, establishing a legible three-level stack against the dark teal background."
  visible_tells:
    - "Eyebrow 'MONITOR' is set at roughly a fifth of the headline size, letterspaced and differentiated in case"
    - "Headline 'Briefed before you ask.' renders large and white with sufficient contrast over the dark-teal gradient"
  confidence: high
- id: typography_05
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "Homepage — four product feature cards"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/homepage/tile-01-y01220.png"
  claim: "Card titles ('Strategize', 'Pitch', 'Monitor', 'Build') step up only modestly from their body copy, so the within-card hierarchy reads compressed rather than confident."
  visible_tells:
    - "Card titles are only slightly heavier than the body copy beneath them, not a clear bold-vs-regular contrast"
    - "An eyebrow tagline above the card row sits near body size, crowding the small stack"
  confidence: medium
- id: typography_06
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "Build page — 'All the brand, category, and audience data' three columns"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/build/tile-01-y01220.png"
  claim: "A strong top section headline anchors the block, but the three column subheads ('Brand', 'Audience', 'Category') step up only weakly from the body lines below them, softening the internal scan path."
  visible_tells:
    - "Column subheads sit close in size to their body copy at this viewport"
    - "The large section headline provides clear top-level entry, but the column level below does not cascade with proportionate contrast"
  confidence: medium
- id: typography_07
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "Monitor page — chat-partner / receipts section"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/monitor/tile-01-y01220.png"
  claim: "Two major section headings ('Every brief comes with an interactive chat partner.' and 'Annoyingly good data, with receipts.') appear in the same scroll zone at nearly identical size and weight, competing at the same level with no scale step between them."
  visible_tells:
    - "Both headlines render within the same tile at very similar sizes"
    - "No intervening scale step or typographic rest separates them, so the vertical rhythm reads continuous rather than segmented"
  confidence: medium
- id: typography_08
  family: typography_hierarchy
  polarity: poor
  page_or_region: "Testimonial cards (recurs on homepage / build / strategize)"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/build/tile-04-y04880.png"
  claim: "Within each testimonial card the attribution name and title step down only slightly from each other, giving the quote-vs-attribution hierarchy a weak read at a glance."
  visible_tells:
    - "Attribution title ('CEO', 'Executive Director of Strategy', 'Director of Brand Management') is only marginally smaller than the name above it"
    - "Name and title sit tight with no clear weight or size break to separate the two"
  confidence: medium
- id: typography_09
  family: typography_hierarchy
  polarity: poor
  page_or_region: "Build page — 'Built for builders' agent example cards"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/build/tile-02-y02440.png"
  claim: "The agent example cards ('Brief-writing agent', 'Creative-fatigue auditor', 'Side-by-side scouting') pack a title, body paragraph and source tag into a small footprint with little typographic separation, so the cards read as text blocks rather than scannable items."
  visible_tells:
    - "Card title and body paragraph are separated by only a small size step with no boldening on the title"
    - "Source tags sit near body size, not clearly subordinated"
  confidence: medium
- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: "Homepage hero — nav through logo bar"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/homepage/tile-00-y00000.png"
  claim: "The hero is a disciplined centered column: nav, pill CTA, headline, subhead, logo bar and product mosaic all align to the same vertical axis with even spacing and no crowding."
  visible_tells:
    - "'Agentic Brand Intelligence' pill is center-aligned over the headline block"
    - "Logo bar sits equidistant below the headline and above the screenshot mosaic"
    - "Nav items are evenly spaced across one horizontal band"
  confidence: high
- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: "Homepage — four-column product feature cards"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/homepage/tile-01-y01220.png"
  claim: "The four product cards form a tight, evenly-guttered row of identical height, each with the same icon + label + one-line description + two CTA links — a polished repeated component."
  visible_tells:
    - "All four cards share the same bounding height and gutter width"
    - "Each card repeats the same internal layout and no card misaligns on the bottom edge"
  confidence: high
- id: layout_03
  family: layout_composition_components
  polarity: strong
  page_or_region: "Homepage — alternating feature scroll sections"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/homepage/tile-03-y03660.png"
  claim: "Each product section repeats the same two-column split — label + headline + body left, product screenshot right — with uniform vertical spacing, giving a reliable scroll rhythm."
  visible_tells:
    - "Left-column text block aligns to the same left margin across sections"
    - "Right screenshot panel is consistently right-anchored at the same proportional width"
  confidence: high
- id: layout_04
  family: layout_composition_components
  polarity: strong
  page_or_region: "FAQ accordion (recurs site-wide)"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/homepage/tile-06-y07320.png"
  claim: "The FAQ accordion is structurally precise: full-width ruled rows, left-aligned question text, and a '+' toggle right-aligned at a consistent x-position with equal row heights — no drift."
  visible_tells:
    - "Horizontal rules span the full content width with no gap on either side"
    - "'+' icons track to the same far-right x-position across every row"
    - "Collapsed row heights are equal for all items"
  confidence: high
- id: layout_05
  family: layout_composition_components
  polarity: strong
  page_or_region: "Monitor page — four scan-type cards"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/monitor/tile-00-y00000.png"
  claim: "The four scan-type cards (Brand, Trend, Audience, Category) use one compact spec — icon, label, 'Scan' subtext, one-line description — in equal-width columns with no height mismatch."
  visible_tells:
    - "Icon and label are stacked at the same top-padding across all four cards"
    - "All four card footprints are equal width within the row"
  confidence: high
- id: layout_06
  family: layout_composition_components
  polarity: strong
  page_or_region: "Monitor page — scan-detail feature rows"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/monitor/tile-02-y02440.png"
  claim: "Each scan-type section repeats an identical asymmetric two-column template — icon + label + title + description left, inputs/output mockup panel right — held consistently across four consecutive sections."
  visible_tells:
    - "The icon and 'Scan' label sit at the same vertical position at the start of every section"
    - "The right-side mockup panel keeps the same proportional width and top-alignment in each section"
  confidence: high
  contrast_with: "store/waldo-fyi/captures/2026-06-18/tiles/monitor/tile-04-y04880.png"
- id: layout_07
  family: layout_composition_components
  polarity: strong
  page_or_region: "Build page — three-column data breakdown (Brand / Audience / Category)"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/build/tile-01-y01220.png"
  claim: "The three-column data breakdown uses equal-width columns with identical internal structure — icon + label, bold heading, body, then a list of tagged pill items — with no horizontal misalignment."
  visible_tells:
    - "All three column icons sit at the same baseline"
    - "Tagged list items within each column use the same small pill component"
  confidence: high
- id: layout_08
  family: layout_composition_components
  polarity: strong
  page_or_region: "Strategize page — product cross-sell cards (bottom)"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/strategize/tile-06-y07320.png"
  claim: "The three cross-sell cards (Pitch, Monitor, Build) are a clean component instance: equal-width bordered cards with icon + title + one-line description and CTAs aligned to the same vertical positions."
  visible_tells:
    - "All three cards share identical border-radius and stroke weight"
    - "Icon glyphs sit at the same top-left position inside each card"
    - "'Get started'/'Book a demo' and 'Learn more' CTAs share the same width and vertical placement"
  confidence: high
- id: layout_09
  family: layout_composition_components
  polarity: mixed
  page_or_region: "Homepage — testimonial card row"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/homepage/tile-02-y02440.png"
  claim: "Testimonial cards share a component spec but vary enough in quote length that the row reads unbalanced — some cards text-heavy, others sparse — and a 'Case study' badge appears on only one."
  visible_tells:
    - "Quote length differs noticeably between the cards"
    - "The 'Case study' badge appears on only one card, breaking visual parity across the row"
  confidence: medium
  contrast_with: "store/waldo-fyi/captures/2026-06-18/tiles/build/tile-04-y04880.png"
- id: layout_10
  family: layout_composition_components
  polarity: mixed
  page_or_region: "Build page — agent use-case card row"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/build/tile-02-y02440.png"
  claim: "The three agent example cards share a template but differ in body length, and the section sits close under a filter tab bar with tight vertical clearance, so the row reads loose at the seam."
  visible_tells:
    - "Third card body text is markedly shorter than the first two"
    - "The tab bar ('One Marketer', 'Brand Teams', 'Agencies', 'Developers') sits close above the cards with little vertical breathing room"
  confidence: medium
- id: layout_11
  family: layout_composition_components
  polarity: mixed
  page_or_region: "Strategize page — 'Strategize is perfect for' card row"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/strategize/tile-04-y04880.png"
  claim: "The three 'perfect for' cards are bordered and component-consistent, but body-text density varies enough between them that the row reads unevenly, with short-card content floating."
  visible_tells:
    - "First card body is roughly two lines while the middle card runs four or more"
    - "Card heights stretch to the longest body, leaving the shorter card's content top-weighted"
  confidence: medium
- id: layout_12
  family: layout_composition_components
  polarity: poor
  page_or_region: "Homepage — transition between product cards and feature list"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/homepage/tile-01-y01220.png"
  claim: "Between the four product cards and the feature list below sits a large dark gap with no bridging element, a pacing dead zone wider than the rhythm elsewhere on the page."
  visible_tells:
    - "A large empty dark band separates the product-card row from the next content block"
    - "No rule, divider, or decorative anchor bridges the transition; the feature list resumes as sparse left-aligned lines"
  confidence: medium
- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: "Homepage hero"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/homepage/tile-00-y00000.png"
  claim: "A tight two-tone base — near-black ground, white text — is punctuated by a single warm amber/coral accent on one inline phrase, a disciplined palette from the first scroll position."
  visible_tells:
    - "Near-black fills the entire hero field with white body text"
    - "One inline span ('become an expert in minutes') is the only chromatic element in the text block; no competing accent in nav or copy"
  confidence: high
- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: "Homepage hero — ambient glow orb"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/homepage/tile-00-y00000.png"
  claim: "A diffuse multi-color radial bloom (amber through teal) floats above the hero text as the site's primary brand graphic, standing in for photography."
  visible_tells:
    - "Soft radial gradient orb center-top of the hero, transitioning warm amber through green-teal"
    - "Entirely atmospheric with no hard edges; no photography in the hero"
  confidence: high
  contrast_with: "store/waldo-fyi/captures/2026-06-18/tiles/monitor/tile-00-y00000.png"
- id: color_03
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "Footer wordmark (recurs site-wide)"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/homepage/tile-07-y08254.png"
  claim: "The oversized footer wordmark 'WALDO' carries a horizontal teal-to-amber gradient — striking, but the teal half does not appear as a primary color in the body above it, reading as a two-hue compromise rather than one decisive accent."
  visible_tells:
    - "Full-footer-width logotype with a green-teal left side fading to warm amber on the right"
    - "The teal half is absent from body content above; only the amber half echoes the hero inline accent"
  confidence: high
  contrast_with: "store/waldo-fyi/captures/2026-06-18/tiles/homepage/tile-00-y00000.png"
- id: color_04
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "FAQ accent color across pages"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/monitor/tile-06-y07320.png"
  claim: "Each product page carries its own accent hue in the same FAQ UI pattern — the '+' toggle is teal on Monitor, coral on the homepage, yellow-gold on Strategize — a per-page color-coding system that reads as legible but not fully unified."
  visible_tells:
    - "Monitor FAQ '+' icons are teal/cyan"
    - "Homepage FAQ '+' icons are coral and Strategize FAQ '+' icons are yellow-gold — three accent hues in one identical UI pattern across pages"
  confidence: high
  contrast_with: "store/waldo-fyi/captures/2026-06-18/tiles/homepage/tile-06-y07320.png"
- id: color_05
  family: color_brand_imagery
  polarity: strong
  page_or_region: "Build page — hero background"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/build/tile-00-y00000.png"
  claim: "The Build hero keeps the dark ground but adds a subtle dark radial particle/mesh texture behind the headline, adding depth without breaking palette discipline."
  visible_tells:
    - "A faint swirling dot/particle field is visible in the dark hero behind and to the right of the headline"
    - "It stays within the near-black range — not a photo or illustration swap; the 'BUILD' eyebrow uses the teal system accent"
  confidence: medium
  contrast_with: "store/waldo-fyi/captures/2026-06-18/tiles/homepage/tile-00-y00000.png"
- id: color_06
  family: color_brand_imagery
  polarity: strong
  page_or_region: "Monitor page — hero background"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/monitor/tile-00-y00000.png"
  claim: "The Monitor hero runs a teal-green atmospheric gradient behind the headline — a bold per-product color variation that stays within the dark-ground system and keeps the white headline legible."
  visible_tells:
    - "Saturated teal-green glow fills the right and lower hero, with a magenta hint upper-left"
    - "Distinct from the homepage amber bloom — a clear per-product differentiation"
  confidence: high
  contrast_with: "store/waldo-fyi/captures/2026-06-18/tiles/strategize/tile-00-y00000.png"
- id: color_07
  family: color_brand_imagery
  polarity: strong
  page_or_region: "Strategize page — hero background"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/strategize/tile-00-y00000.png"
  claim: "The Strategize hero carries a warm amber-ochre atmospheric glow that ties to the amber accent used for that product's eyebrow and CTA, anchoring it as the 'strategy' tier."
  visible_tells:
    - "Warm amber-ochre glow suffuses the upper hero, fading to near-black at the bottom"
    - "Matches the amber 'STRATEGIZE' eyebrow label color"
  confidence: high
  contrast_with: "store/waldo-fyi/captures/2026-06-18/tiles/monitor/tile-00-y00000.png"
- id: color_08
  family: color_brand_imagery
  polarity: poor
  page_or_region: "Homepage — product UI screenshot mosaic"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/homepage/tile-00-y00000.png"
  claim: "The hero screenshot mosaic mixes heterogeneous internal color treatments with no unifying frame, adding visual noise at the brand surface rather than a coherent image system."
  visible_tells:
    - "One thumbnail is a light/white Patagonia card while others are dark UIs with orange/mixed highlights"
    - "No shared framing treatment (border, shadow, or overlay) ties the thumbnails into a family"
  confidence: medium
  contrast_with: "store/waldo-fyi/captures/2026-06-18/tiles/strategize/tile-01-y01220.png"
- id: color_09
  family: color_brand_imagery
  polarity: strong
  page_or_region: "Strategize — video embed card"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/strategize/tile-01-y01220.png"
  claim: "The embedded video card uses a warm cream/off-white fill with a terracotta starburst mark — a deliberate light-on-dark contrast moment that reads as a considered brand expression, not an accidental light section."
  visible_tells:
    - "Soft cream fill on the video card against the surrounding dark canvas"
    - "Terracotta starburst mark and serif-set 'Evening, Monica' wordmark living within the card's own warm color world"
  confidence: high
  contrast_with: "store/waldo-fyi/captures/2026-06-18/tiles/homepage/tile-00-y00000.png"
- id: color_10
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "Monitor — social / real-time data screenshots"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/monitor/tile-01-y01220.png"
  claim: "Embedded social-content screenshots import external palettes — pink/peach avatars, photo color — with no tint or desaturation, reducing chromatic coherence against the site's dark system."
  visible_tells:
    - "Pink/peach circular avatars visible in the social-post screenshots"
    - "Multiple external UI captures retain their own unrelated color treatments with no harmonizing overlay"
  confidence: medium
  contrast_with: "store/waldo-fyi/captures/2026-06-18/tiles/strategize/tile-01-y01220.png"
- id: color_11
  family: color_brand_imagery
  polarity: strong
  page_or_region: "SOC 2 badge (recurs site-wide)"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/build/tile-03-y03660.png"
  claim: "The SOC 2 Type II badge is rendered as a custom dark-mode circular badge tuned to the dark canvas, rather than a raw white vendor badge — a small deliberate brand-system decision."
  visible_tells:
    - "Dark circular 'AICPA SOC 2' badge in a muted palette consistent with the surrounding dark background"
    - "No light/white vendor badge dropped raw onto the dark surface"
  confidence: medium
- id: color_12
  family: color_brand_imagery
  polarity: poor
  page_or_region: "Homepage — customer logo strip"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/homepage/tile-00-y00000.png"
  claim: "The customer logo strip renders partner marks in monochrome but at visibly uneven weight/opacity, so the trust-bar reads slightly inconsistent rather than normalized."
  visible_tells:
    - "Logos (GUT, CONAIR, ATTIE, dentsu, HAVAS, PETERMAYER, GOLIN, CRASSMEDIA, Kettle & Fire) sit at noticeably varying apparent weights"
    - "No single normalization (uniform monochrome weight/opacity) is applied across the set"
  confidence: medium
- id: iconography_01
  family: iconography_illustration
  polarity: mixed
  page_or_region: "Product / scan card icons (homepage and Monitor)"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/homepage/tile-01-y01220.png"
  claim: "The small product- and scan-card icons read as colored dots rather than legible glyphs at card scale — they function as accent identifiers but carry no discernible symbol."
  visible_tells:
    - "Homepage Strategize/Pitch/Monitor/Build cards each show a small circular accent-color icon with no readable glyph shape"
    - "The Monitor Brand/Trend/Audience/Category cards repeat the same colored-dot treatment with glyphs not discernible at card size"
  confidence: medium
  contrast_with: "store/waldo-fyi/captures/2026-06-18/tiles/monitor/tile-00-y00000.png"
- id: iconography_02
  family: iconography_illustration
  polarity: mixed
  page_or_region: "Strategize — product cross-sell card glyphs"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/strategize/tile-06-y07320.png"
  claim: "At full resolution the cross-sell cards each show a distinct glyph (lines / circular-arrow / grid) consistent in size and stroke weight — a shared icon system, though the glyphs are generic rather than custom."
  visible_tells:
    - "Pitch card uses a horizontal-lines glyph, Monitor a circular-arrow glyph, Build a grid/dot-matrix glyph"
    - "All three share the same apparent stroke weight and bounding box"
  confidence: medium
- id: iconography_03
  family: iconography_illustration
  polarity: strong
  page_or_region: "Build — hero product UI mockup"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/build/tile-00-y00000.png"
  claim: "The hero shows a detailed multi-panel product render — an API query pane and a hierarchical data-tree — at enough resolution and polish to read as a credible product illustration, not a placeholder."
  visible_tells:
    - "Left panel is an API prompt card with color-coded category tags and metadata rows"
    - "Right panel is a labeled tree/list structure with visible depth, composited cleanly onto the dark hero"
  confidence: high
- id: iconography_04
  family: iconography_illustration
  polarity: strong
  page_or_region: "Build — 'Three analysis modes' mesh illustrations"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/build/tile-02-y02440.png"
  claim: "Three wireframe-mesh sphere illustrations differentiate the data tiers and hold up at larger scale — the geometry is distinct across all three, confirming intentional custom assets rather than duplicated shapes with color swaps."
  visible_tells:
    - "Left form is an open ring lattice, center a denser ellipsoid mesh, right two overlapping/interpenetrating loops"
    - "The three forms are visually distinct, not the same asset reused"
  confidence: medium
  contrast_with: "store/waldo-fyi/captures/2026-06-18/tiles/build/tile-01-y01220.png"
- id: iconography_05
  family: iconography_illustration
  polarity: mixed
  page_or_region: "Homepage — 'One agentic platform' isometric grid"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/homepage/tile-01-y01220.png"
  claim: "A large isometric dot-grid / node-network graphic fills the right of the section but sits at very low contrast against the dark ground, rendering it nearly inert rather than expressive."
  visible_tells:
    - "A faint dark-grey dot-matrix / isometric grid is barely readable against the dark background on the right side of the section"
  confidence: medium
- id: iconography_06
  family: iconography_illustration
  polarity: strong
  page_or_region: "Monitor — scan product UI mockups"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/monitor/tile-02-y02440.png"
  claim: "The Monitor scan mockups show styled product screens with input/output columns, labeled rows, and a floating annotation card — clean compositing at a density that reads as faithful product renders, not stock dashboard art."
  visible_tells:
    - "Brand Scan panel shows a two-column Inputs/Output layout with row-level labeled entries"
    - "A floating 'The Brand' annotation card carries readable paragraph text in a right-side callout"
  confidence: high
- id: iconography_07
  family: iconography_illustration
  polarity: strong
  page_or_region: "Strategize — video thumbnail starburst mark"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/strategize/tile-01-y01220.png"
  claim: "The video thumbnail carries a terracotta sun-burst / asterisk mark that recurs as the Waldo product mark, rendered cleanly at card scale alongside the 'W' pairing icon."
  visible_tells:
    - "Orange asterisk/starburst mark beside the 'Evening, Monica' wordmark on the cream card"
    - "The same starburst mark reappears in the 'Claude + Waldo' pairing icon on the same tile"
  confidence: high
- id: iconography_08
  family: iconography_illustration
  polarity: mixed
  page_or_region: "Strategize — 'Connect and go' integration logo grid"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/strategize/tile-02-y02440.png"
  claim: "The integration panel shows a row of third-party platform logos plus a '+N strategy workflows' row at consistent small size — recognizable but entirely third-party marks, not a demonstration of Waldo's own icon design."
  visible_tells:
    - "A row of social/data-platform logos (Instagram, Facebook, TikTok, X, LinkedIn, Google Trends, GWI) sits beneath the Waldo product panel"
    - "A '+N strategy workflows' text row carries no custom iconography for the workflow items"
  confidence: medium
- id: iconography_09
  family: iconography_illustration
  polarity: poor
  page_or_region: "Homepage hero — decorative gradient orb"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/homepage/tile-00-y00000.png"
  claim: "As an illustration the hero's primary element is a content-free soft gradient orb — atmosphere standing in for any iconographic or illustrative substance."
  visible_tells:
    - "A large soft-edged multi-color gradient blob center-top of the hero with no form, structure, or icon content"
  confidence: high
  contrast_with: "store/waldo-fyi/captures/2026-06-18/tiles/build/tile-00-y00000.png"
- id: iconography_10
  family: iconography_illustration
  polarity: poor
  page_or_region: "FAQ accordion toggle icons (site-wide)"
  tile_path: "store/waldo-fyi/captures/2026-06-18/tiles/homepage/tile-06-y07320.png"
  claim: "Every FAQ row uses a bare '+' glyph as its toggle — the simplest possible icon, with no custom treatment, and its color is inherited from the page theme rather than a deliberate icon decision."
  visible_tells:
    - "Each FAQ row ends in a plain '+' at the right margin with no weight tuning to the surrounding type"
    - "The '+' color changes by page (coral on homepage, teal on Monitor), indicating a theme-inherited rather than considered icon color"
  confidence: high
  contrast_with: "store/waldo-fyi/captures/2026-06-18/tiles/monitor/tile-06-y07320.png"
```

## Provenance

- **Tiles read:** 32 native-resolution tiles across 4 pages — homepage (8), strategize (8), monitor (9), build (7) — under `store/waldo-fyi/captures/2026-06-18/tiles/`. Mined blind by a 4-family fan-out (Sonnet miners) + judge (Opus); 47 cards in → **43 accepted, 4 rejected** (2 duplicate merges, 2 unverifiable).
- **QA note (`qa_status: recapture-used`):** ALL tiles are **Tier-B browser re-renders** (`scripts/shoot.py`, real Chromium) — Firecrawl screenshots fail on this SPA (fullPage and any screenshot+content combo 500 with `SCRAPE_ALL_ENGINES_FAILED`; see `profile.md` site_notes), so there were no cached payloads to tile (Tier-A unavailable). Every page manifest reported `dismissed:false`, `scroll_locked:false`, full lazy-media loading — no overlays, grey heroes, or lazy gaps; **no exclusions**, no `--dismiss` needed. The lone `poor` structural card (`layout_12`) was spot-checked against its native tile and confirmed a real design dead-zone, not a capture artifact.
- **Judge corrections (against the tiles):** footer-wordmark gradient direction (teal-left→amber-right) [color_03]; homepage FAQ toggle is coral, not teal [layout_04]; integration-grid count generalized to "+N" [iconography_08].
- **Point-in-time caveat:** a 2026-06-18 snapshot of the captured tiles; the live site changes.
