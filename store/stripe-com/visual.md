---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.0"
domain: stripe.com
captured_at: 2026-06-16
source_capture: 2026-06-04
qa_status: recapture-used
---

# Visual evidence — stripe.com

## Visual & brand impression

Stripe presents a tightly systematized design language: one warm-to-cool gradient is the sole chromatic event on a near-white page [color_01], extended into a per-product hue system that holds identical color grammar across heros [color_02]. Custom, high-craft illustration is the signature — layered abstract ribbons, a pointillist particle globe, bespoke integration diagrams [iconography_01, iconography_04, iconography_03] — riding on reusable layout components [layout_04, layout_08] and a clean, size-driven type hierarchy [typography_01, typography_03]. It thins where the system stops: photography is untreated stock/documentary sitting apart from the gradient world [color_07, color_08], small feature icons read as high-grade stock rather than bespoke [iconography_06], and the footer abandons the page's whitespace discipline for extreme density and flattened hierarchy [layout_14, typography_07].

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: "homepage hero"
  tile_path: "store/stripe-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"
  claim: "The hero runs a clean three-tier type hierarchy with strong size contrast between each level, and a single accent-colored word in the headline adds a fourth signal without adding a size level."
  visible_tells:
    - "Display headline 'Financial infrastructure to grow your revenue.' renders at roughly 3-4x the size of the sub-sentence below"
    - "The word 'grow' is set in a lighter purple while the rest stays near-black, a color cue inside one size level"
    - "Top nav items sit at a clearly smaller, lighter weight than all body copy"
  confidence: high
- id: typography_02
  family: typography_hierarchy
  polarity: strong
  page_or_region: "payments page interior section headers"
  tile_path: "store/stripe-com/captures/2026-06-04/tiles/payments/tile-02-y02440.png"
  claim: "A repeatable three-tier section pattern (small purple eyebrow, large bold heading, lighter paragraph) recurs cleanly across interior sections, giving reliable hierarchy signposting."
  visible_tells:
    - "Purple 'Online payments' eyebrow sits well below the large bold heading 'Optimize your checkout experience'"
    - "Body paragraph drops to regular weight and visibly smaller size than the heading"
    - "Eyebrow color alone separates it from heading and body without a size jump"
  confidence: high
  contrast_with: "store/stripe-com/captures/2026-06-04/tiles/connect/tile-03-y03660.png"
- id: typography_03
  family: typography_hierarchy
  polarity: strong
  page_or_region: "pricing hero plan cards"
  tile_path: "store/stripe-com/captures/2026-06-04/tiles/pricing/tile-00-y00000.png"
  claim: "The pricing cards run a self-contained four-level hierarchy (plan name, price figure, descriptor, feature list) where weight and size step down predictably at each level, keeping dense info scannable."
  visible_tells:
    - "'Standard' and 'Custom' plan names are medium-weight, clearly subordinate to the much larger price figure"
    - "The price figure '2.9% + 30¢' is set larger and bolder, anchoring each card"
    - "Descriptor 'per successful transaction for domestic cards' drops to small regular weight beneath the price"
  confidence: high
- id: typography_04
  family: typography_hierarchy
  polarity: strong
  page_or_region: "homepage stat callouts"
  tile_path: "store/stripe-com/captures/2026-06-04/tiles/homepage/tile-03-y03660.png"
  claim: "Stat figures are rendered dramatically larger and heavier than their captions, creating maximum size contrast across the four-stat row."
  visible_tells:
    - "Stat numerals (135+, $1.9T, 99.999%, 200M+) are roughly 4-5x the cap-height of the caption text below each"
    - "Numerals are the only heavy-weight element; captions are small regular grey"
  confidence: high
- id: typography_05
  family: typography_hierarchy
  polarity: strong
  page_or_region: "enterprise hero"
  tile_path: "store/stripe-com/captures/2026-06-04/tiles/enterprise/tile-00-y00000.png"
  claim: "On the dark hero, a single word 'enterprise' is set in an orange accent at the same display size as the surrounding white headline, functioning as a typographic color highlight rather than a new hierarchy level."
  visible_tells:
    - "The word 'enterprise' matches 'Build the next era of your' in size and weight but is rendered in orange"
    - "Body copy beneath drops to clearly smaller regular weight"
  confidence: high
- id: typography_06
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "connect page interior section headings"
  tile_path: "store/stripe-com/captures/2026-06-04/tiles/connect/tile-03-y03660.png"
  claim: "Interior H2s sit clearly larger than body but at a medium (not bold) weight, yielding a structurally correct hierarchy with low heading-to-paragraph weight contrast."
  visible_tells:
    - "'Build your payment business with speed and flexibility' and 'Embed streamlined onboarding...' read as semibold rather than heavy"
    - "The 'How it works' eyebrow is small blue, so the section anchor relies on size alone, not weight"
  confidence: medium
- id: typography_07
  family: typography_hierarchy
  polarity: poor
  page_or_region: "homepage site footer"
  tile_path: "store/stripe-com/captures/2026-06-04/tiles/homepage/tile-11-y13415.png"
  claim: "The footer collapses to a single small type size for both column category labels and individual links, leaving almost no visual hierarchy between group headers and their children."
  visible_tells:
    - "Column headers ('Products and pricing', 'Solutions') and their link items share the same cap-height"
    - "Only a faint weight step, no size or color step, separates a header from the links it groups"
  confidence: high
  contrast_with: "store/stripe-com/captures/2026-06-04/tiles/pricing/tile-00-y00000.png"
- id: typography_08
  family: typography_hierarchy
  polarity: poor
  page_or_region: "enterprise small report-card grid"
  tile_path: "store/stripe-com/captures/2026-06-04/tiles/enterprise/tile-10-y12200.png"
  claim: "The small report-card grid uses very small text with minimal differentiation between the 'Report' label, card title, and summary body, making the three levels hard to separate."
  visible_tells:
    - "The 'Report' badge, the linked title, and the summary body all render at a similar cap-height"
    - "No clear weight step is visible between title and summary at this render size"
  confidence: medium
- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: "homepage hero"
  tile_path: "store/stripe-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"
  claim: "The hero uses a confident asymmetric split: left-anchored headline and CTAs against a large abstract gradient ribbon filling the right, with an even single-baseline logo strip beneath."
  visible_tells:
    - "Headline and button pair flush-left with clear left margin"
    - "Gradient ribbon occupies the right portion without colliding with text"
    - "Logo strip (OpenAI, Amazon, NVIDIA, Ford, Coinbase, Google, Shopify) evenly spaced on one baseline"
  confidence: high
- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: "homepage feature card grid"
  tile_path: "store/stripe-com/captures/2026-06-04/tiles/homepage/tile-01-y01220.png"
  claim: "The feature card grid holds tight internal alignment: each card carries a header zone, a bounded visual panel with product UI or illustration, and a consistent label, signaling a real component system rather than one-offs."
  visible_tells:
    - "Cards share the same corner radius and panel treatment across the grid"
    - "Each card's internal visual (phone mockup, bar chart, card, particle globe) is contained within its own bounded panel"
    - "Header labels sit at a consistent vertical position across the row"
  confidence: high
- id: layout_03
  family: layout_composition_components
  polarity: strong
  page_or_region: "homepage backbone stats section"
  tile_path: "store/stripe-com/captures/2026-06-04/tiles/homepage/tile-03-y03660.png"
  claim: "The four-stat bar uses a strict equal-width column grid with shared baselines for numerals and captions, with generous padding giving the sparse content room."
  visible_tells:
    - "Four stat units are equidistant and top-aligned on the same baseline"
    - "Caption text under each number starts at an identical vertical offset"
    - "Section is padded generously above and below the row"
  confidence: high
- id: layout_04
  family: layout_composition_components
  polarity: strong
  page_or_region: "payments hero"
  tile_path: "store/stripe-com/captures/2026-06-04/tiles/payments/tile-00-y00000.png"
  claim: "The payments hero reuses the same asymmetric two-zone template as the homepage hero with page-specific content (yen checkout card, diagonal gradient band), evidence of a reusable layout component rather than bespoke per-page design."
  visible_tells:
    - "Left zone headline matches the homepage hero weight and line-length range"
    - "Right zone floats a checkout form card with matching corner radius and shadow"
    - "A four-column benefit strip beneath the fold mirrors the homepage four-stat pattern"
  confidence: high
  contrast_with: "store/stripe-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"
- id: layout_05
  family: layout_composition_components
  polarity: strong
  page_or_region: "payments customer logo band"
  tile_path: "store/stripe-com/captures/2026-06-04/tiles/payments/tile-01-y01220.png"
  claim: "The 4x2 logo grid normalizes each logo to the same optical height with consistent gutters, reading as an intentional display band rather than a flat list."
  visible_tells:
    - "Amazon, Shopify, airbnb, URBN in row one; Figma, H&M, Uber, Zoom in row two, all vertically centered"
    - "Logo bounding boxes are visually equal in height despite varied logotype widths"
    - "Uniform padding within each cell; no logo touches its cell edge"
  confidence: high
- id: layout_06
  family: layout_composition_components
  polarity: strong
  page_or_region: "payments multiple-ways-to-accept card row"
  tile_path: "store/stripe-com/captures/2026-06-04/tiles/payments/tile-02-y02440.png"
  claim: "The three-column feature card row shares a rigorous internal anatomy (heading, subhead, checkmark benefit list, UI thumbnail, explore link) with each element aligned across columns."
  visible_tells:
    - "Card headings (Prebuilt payment page, Shareable payment links, Flexible embedded form) start at the same vertical position"
    - "Checkmark bullet lists share the same indentation and line-height"
    - "UI thumbnail insets sit at the same height within each card"
  confidence: high
- id: layout_07
  family: layout_composition_components
  polarity: strong
  page_or_region: "pricing product pricing table"
  tile_path: "store/stripe-com/captures/2026-06-04/tiles/pricing/tile-01-y01220.png"
  claim: "The left-rail category nav plus right-panel pricing table forms a disciplined two-column layout on a shared vertical grid, with product cards rendering at consistent widths and right-aligned price figures."
  visible_tells:
    - "Left rail groups products under bold category labels (Money management, Revenue and finance automation) with regular-weight sub-items"
    - "Right panel product name and 'Start now' button occupy a full-width top bar before bullets begin"
    - "Sub-row price text (Cards and wallets, Link) aligns to the right edge consistently"
  confidence: high
- id: layout_08
  family: layout_composition_components
  polarity: strong
  page_or_region: "connect use-case card carousel"
  tile_path: "store/stripe-com/captures/2026-06-04/tiles/connect/tile-02-y02440.png"
  claim: "The three-card carousel (platforms, marketplaces, enterprise) keeps uniform card dimensions, a blue top-border accent, and a fixed logo cluster at each card base, indicating a reusable card component with slot-swapped content."
  visible_tells:
    - "All three cards are identical height with flush blue top borders"
    - "Logo rows at each card base (Shopify/Mindbody/Housecall Pro; StyleSeat/Lyft/Kickstarter; Ford/PGA) share the same baseline and spacing"
    - "Headings and explore links occupy the same internal positions across cards"
  confidence: high
- id: layout_09
  family: layout_composition_components
  polarity: strong
  page_or_region: "homepage dark infrastructure section"
  tile_path: "store/stripe-com/captures/2026-06-04/tiles/homepage/tile-07-y08540.png"
  claim: "A full-bleed navy band abruptly switches the page from light to dark, with constrained left-aligned prose and pill buttons adapted to the dark ground, creating strong alternating-band vertical rhythm."
  visible_tells:
    - "Full-width navy band ends the preceding light section with a hard edge, no fade"
    - "Heading and body are left-aligned within a constrained text column, not full-width"
    - "Two pill CTAs ('View developer docs', 'View Stripe's GitHub') reuse the light-section button shape on dark"
  confidence: high
- id: layout_10
  family: layout_composition_components
  polarity: strong
  page_or_region: "payments developer code-snippet section"
  tile_path: "store/stripe-com/captures/2026-06-04/tiles/payments/tile-11-y13420.png"
  claim: "The developer section is a clean two-zone layout (prose left, language-tabbed code block right) where the tab bar and numbered code stay contained within their column without overflow."
  visible_tells:
    - "Language tabs (Node.js, Ruby, Python, Go, PHP, Java, .NET) with an active Node.js state"
    - "Code lines are numbered with syntax highlighting inside a contained dark panel"
    - "Left prose column ends cleanly before the code block; no text wraps around the code"
  confidence: high
- id: layout_11
  family: layout_composition_components
  polarity: mixed
  page_or_region: "homepage startup + Atlas promo two-column blocks"
  tile_path: "store/stripe-com/captures/2026-06-04/tiles/homepage/tile-06-y07320.png"
  claim: "The Stripe Startups and Atlas promo pair are flat gradient tiles that read as lower-finish than the main feature cards, which carry product UI or illustration depth."
  visible_tells:
    - "Left tile is a flat purple-magenta gradient block, right tile a flat orange-yellow gradient, neither with a UI mockup or illustration"
    - "Body copy sits below each tile, while the SaaS section just above uses a much richer illustrated UI block"
  confidence: medium
  contrast_with: "store/stripe-com/captures/2026-06-04/tiles/homepage/tile-01-y01220.png"
- id: layout_12
  family: layout_composition_components
  polarity: mixed
  page_or_region: "homepage What's happening news card row"
  tile_path: "store/stripe-com/captures/2026-06-04/tiles/homepage/tile-09-y10980.png"
  claim: "The news card row presents cards at unequal visual weight: a large chromatic 'Annual letter 2025' card beside smaller cropped photo cards, creating density imbalance within a peer row."
  visible_tells:
    - "Annual letter card occupies noticeably more horizontal space than its neighbors"
    - "Right-side cards are cropped editorial photo thumbnails with no heading visible at tile scale"
    - "Only the row header with nav arrows unifies the unequal items"
  confidence: medium
- id: layout_13
  family: layout_composition_components
  polarity: mixed
  page_or_region: "pricing features-out-of-the-box grid"
  tile_path: "store/stripe-com/captures/2026-06-04/tiles/pricing/tile-00-y00000.png"
  claim: "The 4x2 feature grid is competent but its icon+label+checklist cells run to unequal heights with tight top padding, feeling cramped next to the more generous whitespace elsewhere on the page."
  visible_tells:
    - "Checklist items per cell run from one to four lines, producing unequal row heights"
    - "Whitespace between the 'Features available out of the box' header and the icon row is tighter than the padding in the pricing hero above"
  confidence: medium
- id: layout_14
  family: layout_composition_components
  polarity: poor
  page_or_region: "homepage footer mega-menu"
  tile_path: "store/stripe-com/captures/2026-06-04/tiles/homepage/tile-11-y13415.png"
  claim: "The footer link grid runs to extreme density with dozens of product names in tight vertical lists, abandoning the section-level whitespace discipline used everywhere above it."
  visible_tells:
    - "Six columns of vertically-listed links with near-zero row gutter"
    - "The 'Ready to get started?' pre-footer uses generous whitespace; the link grid immediately below collapses to dense type with no breathing room"
  confidence: high
  contrast_with: "store/stripe-com/captures/2026-06-04/tiles/homepage/tile-03-y03660.png"
- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: "homepage hero"
  tile_path: "store/stripe-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"
  claim: "The hero stakes one large warm-to-cool gradient ribbon as the sole chromatic event against a near-white page, with all type kept near-black so nothing competes, evidence of palette restraint."
  visible_tells:
    - "Orange-to-violet-to-pink ribbon occupies the right portion, blending into white with no hard edge"
    - "Body copy and nav stay near-black/grey; the ribbon carries all the warmth"
  confidence: high
- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: "per-product hero hue system (payments / connect / enterprise)"
  tile_path: "store/stripe-com/captures/2026-06-04/tiles/payments/tile-00-y00000.png"
  claim: "Each product hero gets its own gradient hue while keeping identical color grammar (soft diagonal blend, white nav, dark body): payments runs blue-teal-to-violet, connect runs electric cobalt-to-cyan, enterprise runs amber-gold-to-violet on dark, confirming a systematic per-product hue strategy."
  visible_tells:
    - "Payments hero band is distinctly cooler (blue-teal to lavender) than the homepage orange"
    - "Connect hero is a saturated cobalt-to-cyan diagonal sweep"
    - "Enterprise hero shifts to a dark ground with amber-gold cresting to deep violet"
  confidence: high
  contrast_with: "store/stripe-com/captures/2026-06-04/tiles/connect/tile-00-y00000.png"
- id: color_03
  family: color_brand_imagery
  polarity: strong
  page_or_region: "homepage feature card gradient fills"
  tile_path: "store/stripe-com/captures/2026-06-04/tiles/homepage/tile-01-y01220.png"
  claim: "Feature cards use individually tinted gradient fills (pink-to-lavender, blue-to-teal, pink-to-coral) that all belong to one family of soft sweeps, showing controlled variety inside a single system."
  visible_tells:
    - "Top-left card shows a pink-to-lavender gradient behind the phone mockup"
    - "Billing card shows a blue-to-teal chart background"
    - "Card-issuing tile uses a full-bleed pink-to-coral gradient"
  confidence: high
- id: color_04
  family: color_brand_imagery
  polarity: strong
  page_or_region: "enterprise uptime highlight section"
  tile_path: "store/stripe-com/captures/2026-06-04/tiles/enterprise/tile-08-y09760.png"
  claim: "A standalone dark section uses a large flowing amber-to-violet wave as the sole decoration behind the 99.999% uptime stat, with the stat tinted to match the gradient crest, treating the brand gradient as a rhetorical device."
  visible_tells:
    - "Full-bleed dark panel with a luminous amber-to-violet wave across the lower half"
    - "The '99.999%' stat is rendered in a warm gold tonally matched to the wave crest"
  confidence: high
- id: color_05
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "payments section-divider bands"
  tile_path: "store/stripe-com/captures/2026-06-04/tiles/payments/tile-06-y07320.png"
  claim: "Flat solid-color diagonal bands recur as page-transition devices (purple here, teal further down) with hard geometric edges, a cruder gesture than the soft gradient blends used in the heros, making the band a consistent inconsistency."
  visible_tells:
    - "A flat violet-purple diagonal strip crosses the page between sections with no edge feathering"
    - "A teal diagonal strip later on the same page repeats the same sharp-edge treatment"
  confidence: medium
  contrast_with: "store/stripe-com/captures/2026-06-04/tiles/payments/tile-00-y00000.png"
- id: color_06
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "payments customer testimonial panel"
  tile_path: "store/stripe-com/captures/2026-06-04/tiles/payments/tile-08-y09760.png"
  claim: "The Slack quote panel uses a flat brand-purple fill with a heavily purple-tinted office photo bleeding the right half, a stock-photo treatment where the tint does the brand work rather than any distinctive photography."
  visible_tells:
    - "Left half is solid purple; right half is a dark office photo carrying a purple cast overlay"
    - "The photo subject and composition are unremarkable; only the tint ties it to the palette"
  confidence: medium
- id: color_07
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "homepage customer hero image"
  tile_path: "store/stripe-com/captures/2026-06-04/tiles/homepage/tile-04-y04880.png"
  claim: "The Hertz customer image is a generic aerial road-intersection stock shot, well-chosen for scale and neutrality but carrying no brand color grade or owned image language."
  visible_tells:
    - "Full-bleed aerial of a road intersection with a single yellow taxi, no brand overlay"
    - "No color grade distinguishes it from a licensable stock image"
  confidence: medium
- id: color_08
  family: color_brand_imagery
  polarity: poor
  page_or_region: "payments in-person customer photo (Squire)"
  tile_path: "store/stripe-com/captures/2026-06-04/tiles/payments/tile-05-y06100.png"
  claim: "The Squire barbershop customer photo is straightforward documentary photography with no brand color treatment or distinctive crop, sitting with no visual relationship to the gradient-driven system around it."
  visible_tells:
    - "Warm-toned barbershop scene with natural ambient lighting, no grade or overlay linking it to the purple/gradient system"
    - "The image could be swapped for any lifestyle brand's shop photo without changing the impression"
  confidence: high
  contrast_with: "store/stripe-com/captures/2026-06-04/tiles/payments/tile-08-y09760.png"
- id: iconography_01
  family: iconography_illustration
  polarity: strong
  page_or_region: "homepage hero abstract ribbon"
  tile_path: "store/stripe-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"
  claim: "The hero deploys a custom high-craft abstract ribbon illustration with precise layered color banding (peach, orange, violet, pink) reading as a distinct branded signature, not a stock gradient."
  visible_tells:
    - "Multi-layer ribbon form with tight controlled color transitions filling the right of the hero"
    - "Smooth organic curves with no visible seam or banding artifact"
  confidence: high
- id: iconography_02
  family: iconography_illustration
  polarity: strong
  page_or_region: "homepage backbone radial illustration"
  tile_path: "store/stripe-com/captures/2026-06-04/tiles/homepage/tile-03-y03660.png"
  claim: "A bespoke particle-burst / fiber-optic radial illustration anchors the 'backbone of global commerce' stat block, achieving complexity and metaphorical coherence beyond off-the-shelf assets."
  visible_tells:
    - "Thousands of fine pale-blue radiating lines from a central point at high resolution"
    - "The radial sits directly beneath and compositionally integrated with the stat row"
  confidence: high
- id: iconography_03
  family: iconography_illustration
  polarity: strong
  page_or_region: "homepage dark section: integration diagram and waveform mesh"
  tile_path: "store/stripe-com/captures/2026-06-04/tiles/homepage/tile-08-y09760.png"
  claim: "The dark section carries two purpose-built illustrations: a node-and-edge integration diagram with branded icon nodes around a central Stripe wordmark, and a layered purple-to-pink sine-wave mesh, both clearly custom rather than library assets."
  visible_tells:
    - "Branded square icon nodes in a radial spoke layout connect to a central 'stripe' wordmark node with hairline edges"
    - "Below it, a stacked gradient wave mesh of fine lines creates a 3D ribbon illusion shifting navy-to-violet-to-pink"
  confidence: high
  contrast_with: "store/stripe-com/captures/2026-06-04/tiles/homepage/tile-03-y03660.png"
- id: iconography_04
  family: iconography_illustration
  polarity: strong
  page_or_region: "homepage borderless-money particle globe"
  tile_path: "store/stripe-com/captures/2026-06-04/tiles/homepage/tile-01-y01220.png"
  claim: "The 'Access borderless money movement' panel uses a pointillist particle globe (a dense scatter of colored dots forming a world-map sphere), plainly custom-rendered rather than photographic or clip-art."
  visible_tells:
    - "Particle density shifts from warm pink/orange to cool lavender across the sphere with no hard edge"
    - "A geographic silhouette is visible within the dot field"
  confidence: high
- id: iconography_05
  family: iconography_illustration
  polarity: strong
  page_or_region: "payments analytics dashboard mockups"
  tile_path: "store/stripe-com/captures/2026-06-04/tiles/payments/tile-07-y08540.png"
  claim: "The Payments Intelligence cards carry small product-faithful chart illustrations (gradient bar chart, authorization line comparison, Radar detection chart) that read as real dashboard UI, not generic stock screenshots."
  visible_tells:
    - "The 'Boost revenue' card uses blue-to-teal graduated bar fills matching the palette"
    - "Adjacent cards show a purchase-authentication keypad and a multi-series hairline line chart consistent with real dashboard rendering"
  confidence: high
- id: iconography_06
  family: iconography_illustration
  polarity: mixed
  page_or_region: "feature icon set (pricing grid / connect 4-up)"
  tile_path: "store/stripe-com/captures/2026-06-04/tiles/pricing/tile-00-y00000.png"
  claim: "The small feature icons share a consistent blue/teal/purple gradient, rounded-square, isometric-ish treatment but at display size are indistinct from high-quality stock sets, with no unifying geometric vocabulary marking them as bespoke; the same archetype-reuse pattern shows on the connect benefit row."
  visible_tells:
    - "Pricing grid icons (global access, fraud, checkout, payouts) are small gradient-filled isometric tiles similar in weight and color"
    - "Connect's globe-with-arrow and globe-with-magnifier reuse one base glyph with different suffixes, a library-reuse pattern"
  confidence: medium
  contrast_with: "store/stripe-com/captures/2026-06-04/tiles/homepage/tile-08-y09760.png"
- id: iconography_07
  family: iconography_illustration
  polarity: mixed
  page_or_region: "payments compliance badge row"
  tile_path: "store/stripe-com/captures/2026-06-04/tiles/payments/tile-10-y12200.png"
  claim: "The compliance section mixes official third-party certification marks (AICPA SOC, PCI, PSD2/SCA) with a generic stroke globe glyph for E-Money Licenses, and the generic mark weakens the otherwise consistent custom-illustration tone."
  visible_tells:
    - "AICPA SOC, PCI DSS, and PSD2/SCA marks are lifted directly from certifying bodies"
    - "The E-Money Licenses tile uses a plain white-on-teal globe glyph inconsistent with the custom work elsewhere"
  confidence: medium
```

## Provenance

- **Tiles read:** 71 native-resolution tiles across 5 pages — `homepage`, `payments`, `pricing`, `connect`, `enterprise` — under `store/stripe-com/captures/2026-06-04/tiles/`. Pages curated to the ones carrying Stripe's visual system (flagship + payments / pricing / connect / enterprise signal pages).
- **QA note — Tier-B re-render (`scripts/shoot.py --dismiss`) on `homepage` + `enterprise`.** Every page's hero tile carried a site-wide Intercom sales-chat overlay (expanded "N sales reps available… Chat now" proactive message on homepage/connect/enterprise/pricing; collapsed launcher on payments). On `homepage` and `enterprise` the proactive bubble covered real evidence (the "Flexible solutions" intro + a product card; the customer-logos band), so both were re-rendered with `--dismiss` — the affordance path cleared the proactive message via its own close control, collapsing it to the persistent "Chat with Stripe sales" launcher (a faithful site element, kept in-frame). Both manifests: `dismissed: true`, `scroll_locked: false`, `overview-480w.png` emitted; no `WARNING`s fired. The `enterprise` cached payload had also rendered its animated amber-gold→violet hero gradient flat-dark (WebGL-incomplete); the Tier-B render restored it, and cards `color_02 / color_04 / typography_05` rest on that recovered gradient.
- **Tier-A kept (chat launcher noted, not excluded):** `connect`, `pricing`, `payments` heros carry the same persistent corner chat launcher — a low-harm faithful capture-fact over gradient/empty space that leaves hero evidence intact, so they were not re-rendered. No tiles were excluded for contamination.
- **Snapshot caveat:** point-in-time read of captured tiles. `homepage` + `enterprise` tiles were re-rendered live on 2026-06-16, 12 days after the 2026-06-04 dossier capture — minor live drift (e.g., the homepage customer-logo carousel showed a different set — OpenAI / Amazon / NVIDIA / Ford / Coinbase / Google / Shopify — at render time). The site changes; this captures these tiles.
