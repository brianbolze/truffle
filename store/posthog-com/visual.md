---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.0"
domain: posthog.com
captured_at: 2026-06-16
source_capture: 2026-06-16
qa_status: clean
---

## Visual & brand impression

PostHog presents as a confident, engineering-led indie brand. A warm linen canvas [color_02] carries a custom isometric mascot world [color_01][iconography_01] and a recurring hedgehog persona system [iconography_02], with consistent orange CTAs [color_03] and crisp type hierarchy in its heroes and pricing cards [typography_01][typography_05][typography_10], punched by orange keyword accents [typography_07][typography_08]. Deliberately anti-slick retro devices — a CRT-TV demo container [iconography_04], a software-box parody [iconography_09], an MS-Paint road-sign embed [layout_14] — choose personality over polish. Control slips in the long tail: flat equal-weight section headings down-page [typography_04], duplicated dense body copy [typography_02], inconsistent bold emphasis [typography_11], and informal, unsystematic team-avatar photography [color_08]. High craft where it counts; intentional roughness elsewhere.

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: "Homepage hero"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/homepage/tile-00-y00000.png"
  claim: "The hero establishes a clear three-level hierarchy — large display headline ('Just ask @PostHog.'), a compact subhead paragraph, and small supporting link text — with visibly stepped size and weight at each level."
  visible_tells:
    - "Display headline is notably larger and heavier than the paragraph beneath it"
    - "Supporting links ('MCP', 'Watch a demo', 'Talk to a human') are the smallest text unit, set lighter, forming a third legible tier"
  confidence: high
- id: typography_02
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "Homepage mid-page body copy"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/homepage/tile-01-y01220.png"
  claim: "Body copy in the data-stack section is dense with tight leading, and inline italic emphasis ('the full set of data', 'outside your product') interrupts reading rhythm without adding a hierarchy level, weakening paragraph-level separation."
  visible_tells:
    - "The 'When you're analyzing how customers...' block and the bullet list sit at near-identical size with minimal leading between them"
    - "A full duplicated sentence ('Having all the data in one place...') renders twice in sequence, with italic inline emphasis breaking the scan"
  confidence: medium
- id: typography_03
  family: typography_hierarchy
  polarity: strong
  page_or_region: "Homepage CTA footer ('PostHog Cloud' product card)"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/homepage/tile-03-y02625.png"
  claim: "The 'PostHog Cloud' card layers type deliberately — product name in large bold, a small italic subtitle, a label line, and a price string that splits a struck-through '$0' against 'FREE' in orange — each token legibly distinct on one line."
  visible_tells:
    - "'PostHog Cloud' heading is bold and much larger than 'Digital download*' beneath it"
    - "The strikethrough '$0' and colored 'FREE' share a line but are differentiated by weight, color, and decoration"
  confidence: high
- id: typography_04
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "Homepage late sections ('Why PostHog?', 'Bedtime reading', 'Shameless CTA')"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/homepage/tile-02-y02440.png"
  claim: "Late-scroll section headings ('Why PostHog?', 'Bedtime reading', 'Shameless CTA') are correctly bolded but all render at the same size with no color, rule, or scale step, so the lower page reads as a flat run of equal-weight sections with no macro-hierarchy."
  visible_tells:
    - "'Why PostHog?', 'Bedtime reading', and 'Shameless CTA' all appear at the same approximate size and weight"
    - "No size increase, color, or divider distinguishes a top-level section break from a sub-section"
  confidence: medium
- id: typography_05
  family: typography_hierarchy
  polarity: strong
  page_or_region: "Pricing page — plan comparison cards"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/pricing/tile-01-y01220.png"
  claim: "The plan cards ('Free', 'Pay-as-you-go') use a clear three-level type stack: plan name in bold italic, a descriptor line in regular weight, and feature sub-items in a smaller, lighter face, all legible at a glance."
  visible_tells:
    - "'Free' is bold italic, clearly differentiated from 'No credit card required' in light roman below"
    - "Feature sub-lines ('Usage capped at free tier limits') render smaller and lighter than the bold feature name above"
  confidence: high
- id: typography_06
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "Pricing page — 'Compare plans' section label"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/pricing/tile-01-y01220.png"
  claim: "The 'Compare plans' section label is small and regular-weight with no size step over adjacent body copy, reading as a caption rather than a primary section break before the visually larger plan cards it introduces."
  visible_tells:
    - "'Compare plans' sits flush-left in small regular weight, the same scale as surrounding text"
    - "The plan cards immediately below are visually much larger, making the heading feel subordinate to its own content"
  confidence: medium
- id: typography_07
  family: typography_hierarchy
  polarity: strong
  page_or_region: "Pricing page — 'This is the call to action' footer heading"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/pricing/tile-05-y06100.png"
  claim: "The page finale uses a large centered bold heading with an orange-accented keyword ('call to action') — the largest text in the tile — delivering crisp hierarchy against the small FAQ body copy above it."
  visible_tells:
    - "'This is the call to action.' is the largest, heaviest text unit in this tile"
    - "The phrase 'call to action' renders in orange, a second emphasis level within the heading"
  confidence: high
- id: typography_08
  family: typography_hierarchy
  polarity: strong
  page_or_region: "AI page — 'What PostHog AI can do for [you]' section heading"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/ai/tile-05-y06100.png"
  claim: "The section heading uses a bracketed orange keyword ('[you]') as a controlled typographic interrupt — same scale and weight as the surrounding heading but color-differentiated and underlined — drawing the eye without breaking the line."
  visible_tells:
    - "'[you]' renders in orange (and underlined) against dark heading text at the same size"
    - "Surrounding heading copy is the largest text on this tile, anchoring the section"
  confidence: high
- id: typography_09
  family: typography_hierarchy
  polarity: poor
  page_or_region: "AI page — 'How PostHog uses PostHog AI' video card overlays"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/ai/tile-04-y04880.png"
  claim: "The video-card overlay text ('HOW EDWIN USES POSTHOG AI TO INVESTIGATE TRAFFIC') stacks all-caps display words at near-equal weight with no clear entry point — the subject name, verb, and 'POSTHOG AI' all compete, yielding label noise rather than a read order."
  visible_tells:
    - "All-caps 'POSTHOG AI' and the surrounding line are nearly the same visual weight"
    - "Multiple weight/color treatments crowd the small card-label area with no dominant first word"
  confidence: medium
- id: typography_10
  family: typography_hierarchy
  polarity: strong
  page_or_region: "About page hero"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/about/tile-00-y00000.png"
  claim: "The about hero ('We're here to help product engineers build successful products') shows a clean two-level hierarchy: a large heavy heading directly over a smaller regular-weight paragraph, with no extraneous levels."
  visible_tells:
    - "Heading runs at roughly twice the cap-height of the body copy below it"
    - "Weight contrast between the bold heading and regular subparagraph is immediately legible"
  confidence: high
- id: typography_11
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "Pricing page — 'A note from our co-founder' card"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/pricing/tile-02-y02440.png"
  claim: "The founder-note bullets apply bold emphasis inconsistently — the first two open with full bold lead sentences, while later bullets bury bold phrases mid-sentence — so the leading phrase of each point can't be scanned reliably."
  visible_tells:
    - "First two bullets open with full bold sentences ('We make a profit with every product.')"
    - "Later bullets place bold phrases ('default alive', 'we don't rely on investors to grow') mid-line rather than at the opening"
  confidence: medium
- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: "Homepage — left icon-rail + simulated browser-chrome content frame"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/homepage/tile-00-y00000.png"
  claim: "The site wraps content in a distinctive shell — a narrow fixed left icon-rail plus a simulated browser-window chrome (tab strip + address bar) on a sandy outer background — a deliberate compositional container rather than a plain centered column."
  visible_tells:
    - "Vertical left strip of small icon+label nav items (Product OS, Pricing, Docs) at fixed width"
    - "Content rendered inside a browser-chrome element with visible address bar and tab"
    - "Warm cream outer frame separates the chrome from the page edge (figure-ground)"
  confidence: high
- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: "Homepage — hero (demo panel left, isometric illustration right)"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/homepage/tile-00-y00000.png"
  claim: "The hero splits a live chat/thread UI demo panel on the left against a large isometric illustration on the right, anchored by an orange interactive tab strip — a composed hero with weight beyond a generic headline-plus-screenshot."
  visible_tells:
    - "Isometric building/landscape illustration occupies roughly the right third at significant scale"
    - "Thread/chat demo panel sits left, vertically centered against the illustration mass"
    - "Orange tab strip (Create pull requests in Slack / Fix bugs automatically / Ask PostHog anything) anchors the demo's base"
  confidence: high
- id: layout_03
  family: layout_composition_components
  polarity: mixed
  page_or_region: "Homepage — scrolled body sections (customers, data stack, pricing intro)"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/homepage/tile-01-y01220.png"
  claim: "Below the hero the page drops the browser-chrome framing and reverts to a plain single-column document flow — a bare bordered logo table, then left-text/right-illustration floats with no shared grid — undercutting the hero's structural distinctiveness."
  visible_tells:
    - "Two-column customer logo table (VCs / Product engineers) rendered as a plain bordered table, no card shell"
    - "Pricing-intro section is a left-text / right-illustration float not aligned to a defined column grid"
    - "Section headers sit flush-left with no separation system"
  confidence: high
- id: layout_04
  family: layout_composition_components
  polarity: strong
  page_or_region: "Pricing — hero product tile grid"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/pricing/tile-00-y00000.png"
  claim: "The pricing hero packs a dense icon-labeled product tile grid (Analytics, Session Replay, Feature Flags, Experiments, Surveys, Data Warehouse, Workflows, Logs, etc.) at uniform tile size with even gutters across multiple rows and columns — a disciplined repeating component."
  visible_tells:
    - "12+ product tiles at identical dimensions with consistent icon-left / label-right internal layout"
    - "Even gutters held across rows with no overflow or misalignment"
    - "Uniform pill/chip shape and border weight across all tiles"
  confidence: high
- id: layout_05
  family: layout_composition_components
  polarity: strong
  page_or_region: "Pricing — plan comparison cards"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/pricing/tile-01-y01220.png"
  claim: "The Free / Pay-as-you-go comparison uses a well-finished card component — matching internal padding, checklist rows with identical icon+text structure, and an orange CTA at the same width in both cards — reading as a system component, with a precisely-placed 'Just pick this one!' callout tab on the Free card."
  visible_tells:
    - "Both cards share identical structure: plan name, subhead, checkmark feature rows, retention line, CTA"
    - "'Get started - free' CTA appears in both at the same width/height and border-radius"
    - "'Just pick this one!' callout sits precisely above the Free card's top border"
  confidence: high
- id: layout_07
  family: layout_composition_components
  polarity: mixed
  page_or_region: "Pricing — pricing calculator interactive section"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/pricing/tile-02-y02440.png"
  claim: "The pricing calculator's three columns (product list left, event sliders center, 'How our pricing works' prose right) are structurally clear but don't share a top baseline, and the slider track is bare (a single orange dot on a grey line, no scale markers), so the right prose column reads as unaligned rather than a designed panel."
  visible_tells:
    - "Left product list, center slider stack, and right prose column do not share a common top edge"
    - "Slider track is minimal — single orange dot on a grey line with axis labels (0/1M/10M/50M/250M) but no styled scale"
    - "Orange highlight ('Generous free tier for each product') applied mid-paragraph in the right column"
  confidence: medium
- id: layout_08
  family: layout_composition_components
  polarity: strong
  page_or_region: "Pricing — FAQ with avatar-keyed answers"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/pricing/tile-04-y04880.png"
  claim: "The FAQ repeats a disciplined component — circular avatar left, question right, then an indented answer row with a smaller avatar and the responder's name in orange — applied identically across every entry with consistent vertical rhythm."
  visible_tells:
    - "Each row: avatar left + question; indented answer beneath with smaller avatar and orange name link"
    - "Avatar crop, size, and left-alignment identical across all entries (Tim Glaser, Simon Fisher, Tiina Turban, Rick Marron…)"
    - "Consistent spacing between question-answer pairs through the section"
  confidence: high
- id: layout_09
  family: layout_composition_components
  polarity: strong
  page_or_region: "AI page — categorized side-nav + tab-switched feature panel"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/ai/tile-00-y00000.png"
  claim: "The AI page pairs a grouped side-navigation (Analytics / Product engineering / Communication / PostHog data stack, each with icon-label items and dividers) against a tab-switched feature panel with a distinct active state — a mature two-pane component."
  visible_tells:
    - "Left nav: bold group labels over flush icon-text item lists with dividers between groups"
    - "Active item (Product Analytics) visually highlighted vs inactive items"
    - "Right panel renders selected feature content in a consistent frame"
  confidence: high
- id: layout_10
  family: layout_composition_components
  polarity: strong
  page_or_region: "AI page — 'Skills' 2x2 capability grid"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/ai/tile-01-y01220.png"
  claim: "The four-cell Skills grid (Build insights from plain English / Write and explain HogQL / Deep dive into your product data / Navigate the UI) uses an even component — bold heading, a blue filled progress-bar graphic, two-line body — at identical dimensions and shared left-edge alignment across both columns."
  visible_tells:
    - "2x2 grid of equal-width, equal-height cells, no overflow"
    - "Each cell: bold heading, blue progress-bar fill, two-line body"
    - "Consistent left-edge alignment across both columns"
  confidence: high
- id: layout_11
  family: layout_composition_components
  polarity: mixed
  page_or_region: "AI page — 'AI everywhere' integration cards (coding agent / Slack)"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/ai/tile-01-y01220.png"
  claim: "The two 'wherever you work' cards (In your coding agent / In Slack) are equal-width with a matching icon+title / link header, but the interiors are dense bold-lead bullet paragraphs running close to the card edges — they read as inline text blocks rather than a paced component."
  visible_tells:
    - "Both cards: icon + bold title top-left, doc link top-right, then stacked bold-lead bullet paragraphs"
    - "Body text runs near the card edges with little visible internal padding"
    - "Heavy, evenly-dense text fill with little whitespace between points"
  confidence: medium
- id: layout_12
  family: layout_composition_components
  polarity: strong
  page_or_region: "AI page — persona selector tab row"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/ai/tile-05-y06100.png"
  claim: "The five-tab persona selector (Founders / Product Engineers / Product Managers / Growth & Marketers / Data Analysts) pairs each tab with a distinct character illustration at consistent scale and position, with a selected-state box on the active tab — a polished tabbed component."
  visible_tells:
    - "Five equally-spaced tabs, each with a unique illustrated character above the label"
    - "Active tab (Founders) has a visible selected-state highlight box"
    - "All five illustrations sit at the same dimensions and vertical position"
  confidence: high
- id: layout_13
  family: layout_composition_components
  polarity: strong
  page_or_region: "AI page — Roadmap three-column kanban"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/ai/tile-06-y07320.png"
  claim: "The roadmap uses a three-column kanban (Under consideration / In progress / Shipped) with solid colored header bars (grey / orange / green) over uniformly padded card entries, making the status taxonomy immediate and the columns evenly structured."
  visible_tells:
    - "Three equal-width columns with solid colored header bars"
    - "Card entries share consistent padding and text structure within each column"
    - "Shipped entries use left checkmarks; Under consideration uses numbered badges"
  confidence: high
- id: layout_14
  family: layout_composition_components
  polarity: poor
  page_or_region: "AI page — bottom CTA (MS-Paint / road-scene parody embed)"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/ai/tile-07-y08540.png"
  claim: "The AI page closes on a raw screenshot of an image-editing app — its menu bar, toolbox and color palette visible — holding garish rainbow WordArt over a desert-road photo with a STOP sign, dropped into the page flow with no card, border, or padding to relate it to the structured sections around it."
  visible_tells:
    - "Image-editor chrome (menu bar, left toolbox, swatch palette) is visible inside the embedded graphic"
    - "Multi-color WordArt ('Get started today!!', 'If you're looking for a sign…') over a road photo with a STOP sign"
    - "No container wraps the image; it floats at browser-screenshot fidelity between structured UI sections"
    - "Palette of neon yellow / cyan / red has no relationship to any color used elsewhere on the site"
  confidence: high
- id: layout_15
  family: layout_composition_components
  polarity: strong
  page_or_region: "Products page — feature roster three-column grouped list"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/products/tile-01-y01060.png"
  claim: "The product feature roster uses a three-column grid of icon-label items grouped under bold all-caps headers (UNDERSTAND PRODUCT USAGE / DEBUG & FIX ISSUES / SHIP FEATURES & GET FEEDBACK), with uniform column widths, consistent icon sizing, and no baseline drift across 20+ items."
  visible_tells:
    - "Three equal-width columns, each with multiple icon-text rows at consistent line height"
    - "Bold all-caps group labels left-aligned above each column group"
    - "Icon sizes consistent across all items with no visible baseline drift"
  confidence: high
- id: layout_16
  family: layout_composition_components
  polarity: mixed
  page_or_region: "About page — hero in browser-chrome frame"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/about/tile-00-y00000.png"
  claim: "The about hero reuses the browser-chrome frame but sits sparse — headline left, a small gradient pie-chart illustration upper-right leaving heavy whitespace — then drops to a plain single-column document flow with a founders' signature JPEG floated right at an awkward width relative to the text column."
  visible_tells:
    - "Pie-chart illustration upper-right is small versus the hero text mass, leaving the right half of the frame mostly empty"
    - "Founders' signature image floated right of 'So how did we get here?' creates an unbalanced left-heavy text block"
    - "No grid module in the body — text and image in an ad hoc float"
  confidence: medium
- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: "Homepage hero — custom isometric world illustration"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/homepage/tile-00-y00000.png"
  claim: "The hero deploys a fully custom isometric world — tiled green terrain, hedgehog character figures, and branded structures — clearly owned art rather than stock, with an internally coherent warm-green/terracotta palette that matches the beige page ground."
  visible_tells:
    - "Isometric green-tile landscape with hedgehog figures and a castle/building complex fills the hero's right column"
    - "Illustration palette (warm greens, terracotta, sandy neutrals) coheres and ties to the beige background"
  confidence: high
- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: "Across pages — warm linen page background"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/homepage/tile-00-y00000.png"
  claim: "A warm off-white/linen background replaces SaaS-default pure white, giving a consistent tonal ground that unifies text, product screenshots, and illustration across homepage, about, products, and pricing."
  visible_tells:
    - "Page background is visibly warm-tinted beige, not #FFFFFF"
    - "The same linen tone carries from nav through footer across multiple pages"
  confidence: high
- id: color_03
  family: color_brand_imagery
  polarity: strong
  page_or_region: "Homepage / Pricing / Products — CTA buttons"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/homepage/tile-03-y02625.png"
  claim: "A single saturated amber-orange serves as the sole primary CTA color across every page, with no competing accent — the discipline holds from homepage hero through pricing cards to footer."
  visible_tells:
    - "'Get started' buttons on homepage, pricing, and products all use the same amber-orange fill"
    - "No blue, green, or alternate-colored primary buttons appear anywhere in the tile set"
  confidence: high
- id: color_04
  family: color_brand_imagery
  polarity: strong
  page_or_region: "AI page — video thumbnail system"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/ai/tile-04-y04880.png"
  claim: "The 'How PostHog uses PostHog AI' video thumbnails share a designed two-color treatment — color-blocked backgrounds (orange, teal, purple) with consistent display title styling and a PostHog wordmark in a fixed lockup position — a purposeful thumbnail system, not ad-hoc crops."
  visible_tells:
    - "All four cards share the same title styling and color-blocked background convention"
    - "PostHog wordmark sits in a consistent lower lockup position on each card"
  confidence: high
- id: color_05
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "AI page — roadmap status column colors"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/ai/tile-06-y07320.png"
  claim: "The roadmap's saturated amber 'In progress' and bright green 'Shipped' header bars are a secondary status palette that carries the hierarchy almost entirely on color, and these greens don't reappear elsewhere — a functional but slightly disconnected extension of the otherwise muted linen-and-orange system."
  visible_tells:
    - "Amber and bright-green column headers contrast strongly with the muted linen palette"
    - "All three column labels are the same size/weight, so removing color would leave them undifferentiated"
    - "The green does not recur in any other UI section in the tile set"
  confidence: medium
- id: color_06
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "AI page — 'Chat with your data' feature cards"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/ai/tile-03-y03660.png"
  claim: "The 'Chat with your data' cards use flat pastel fills (orange, green, blue, pink) that read as independent per-card accents — pleasant but not drawn from the amber CTA or warm-linen base, so they float rather than tie into the core palette."
  visible_tells:
    - "Four feature cards each on a different pastel background (orange, green, blue, pink) hosting a hedgehog vignette"
    - "The pastel hues do not echo the amber CTA or the linen ground"
  confidence: medium
- id: color_07
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "Pricing page — Y Combinator testimonial block"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/pricing/tile-01-y01220.png"
  claim: "The testimonial block sets a real circular headshot (Cat Li) against a solid near-black panel with an orange keyword highlight — the only photographic portraiture and the only black panel in the tile set, a one-off convention rather than a defined photo style."
  visible_tells:
    - "Circular-cropped color portrait on a solid near-black panel"
    - "Orange highlighted phrase within white testimonial text on the dark panel"
    - "No other portrait photography or black panel appears elsewhere in the set"
  confidence: medium
- id: color_08
  family: color_brand_imagery
  polarity: poor
  page_or_region: "Pricing FAQ — team avatar photos"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/pricing/tile-04-y04880.png"
  claim: "The FAQ team headshots are small, variably lit, and informally shot — different backgrounds, crops, and warm/cool casts across avatars — showing no photography art direction binding the human imagery together."
  visible_tells:
    - "Six avatar thumbnails each in a different environment with different lighting and crop distance"
    - "Some warm-toned, some cool; face crops and sizes inconsistent"
  confidence: high
- id: iconography_01
  family: iconography_illustration
  polarity: strong
  page_or_region: "Homepage hero — isometric mascot world"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/homepage/tile-00-y00000.png"
  claim: "The hero's isometric scene shows genuine illustration investment — multiple hedgehog characters at consistent proportions across poses, a perspective-consistent tile platform with varied foliage and architecture — well above clip-art or stock quality."
  visible_tells:
    - "Multiple characters share consistent hedgehog proportions and shading across poses"
    - "Perspective-consistent tile platform with varied foliage and structural detail"
    - "Warm earth-tone palette applied coherently across foreground and background"
  confidence: high
- id: iconography_02
  family: iconography_illustration
  polarity: strong
  page_or_region: "AI page — persona selector hedgehog variants"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/ai/tile-05-y06100.png"
  claim: "Each persona tab features a unique costumed variant of the same hedgehog character (lab coat, engineer at machinery, magnifying-glass detective, marketer at a flowchart, analyst at a desk) at consistent line weight and proportion — a disciplined custom character system, not generic icon swaps. Its recurrence across hero, homepage, and feature cards makes it a coherent owned mascot."
  visible_tells:
    - "Five distinct hedgehog illustrations with unique props/costume signalling occupation"
    - "Consistent body proportions, line weight, and shading across all five variants"
    - "Same character recurs on the homepage isometric hero and feature-card vignettes"
  confidence: high
- id: iconography_03
  family: iconography_illustration
  polarity: strong
  page_or_region: "Homepage — 'no sales call' prohibition badge"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/homepage/tile-01-y01220.png"
  claim: "A custom 'no sales call' badge — the hedgehog mascot on fire inside a red prohibition circle — is a self-contained brand glyph that doubles as messaging, executed in the site's illustration style and primary orange-red."
  visible_tells:
    - "Hedgehog rendered inside a standard prohibition circle in the site's illustration style"
    - "Orange-red stroke/fill matching the primary palette"
  confidence: high
- id: iconography_04
  family: iconography_illustration
  polarity: strong
  page_or_region: "Products page — retro CRT-TV demo container"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/products/tile-01-y01060.png"
  claim: "A hand-drawn retro CRT-television frame (rounded housing, knobs, VHS-style control bar) is used as a bespoke container for the live AI demo chart — brand illustration integrated directly into a functional product mockup rather than decorating beside it."
  visible_tells:
    - "Hand-drawn CRT housing with rounded corners, knobs, and a control bar"
    - "A live line-chart renders inside the screen area, merging illustration with product UI"
    - "Warm line-art style consistent with the mascot work elsewhere"
  confidence: high
- id: iconography_05
  family: iconography_illustration
  polarity: strong
  page_or_region: "Homepage — 'Bedtime reading' spot illustration"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/homepage/tile-02-y02440.png"
  claim: "A night-scene spot illustration — a hedgehog at a desk under a wall clock in a blue-lit room — brings editorial-quality narrative art to a low-stakes link section, signalling illustration is a systematic investment, not reserved for hero moments only."
  visible_tells:
    - "Dark blue atmospheric background establishing a night setting"
    - "Hedgehog at a desk with monitor glow and a distinct posture"
    - "Clock and ambient lighting add narrative beyond simple decoration"
  confidence: high
- id: iconography_06
  family: iconography_illustration
  polarity: strong
  page_or_region: "AI page — 'Chat with your data' card vignettes"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/ai/tile-03-y03660.png"
  claim: "Small inline card vignettes show the hedgehog in distinct action poses with clear silhouette differentiation, holding the illustration system together at reduced size across the pastel cards."
  visible_tells:
    - "Card-sized hedgehog vignettes with visually distinct props per card"
    - "Illustrations stay legible and characterful at small size"
    - "Pastel card backgrounds differentiate per use-case"
  confidence: high
- id: iconography_07
  family: iconography_illustration
  polarity: mixed
  page_or_region: "Products / AI — functional product icon set"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/products/tile-01-y01060.png"
  claim: "The functional product icons (Web Analytics, Funnels, Traces, Feature Flags, Error Tracking, etc.) are consistently sized but heterogeneous in style — varying stroke weight, fill approach, and glyph complexity, with per-icon colors rather than a tight shared palette — reading closer to emoji-adjacent glyphs than one unified custom set."
  visible_tells:
    - "Product icons vary in stroke weight and fill approach"
    - "Per-icon colors are distinct rather than from a shared palette"
    - "Glyph complexity is inconsistent — some simple shapes, others detailed"
  confidence: medium
- id: iconography_08
  family: iconography_illustration
  polarity: mixed
  page_or_region: "AI page — hero illustration panel"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/ai/tile-00-y00000.png"
  claim: "The AI hero scene — hedgehog characters with filing boxes and a computer on a teal panel — matches the brand illustration language but is compositionally busier and less resolved than the isometric homepage hero, with characters and props at similar visual weight and no clear focal point."
  visible_tells:
    - "Multiple overlapping character poses with no clear focal hierarchy"
    - "Filing boxes and laptop props read at a similar weight to the characters"
    - "Teal-green panel contrasts the characters but the scene reads crowded"
  confidence: medium
- id: iconography_09
  family: iconography_illustration
  polarity: mixed
  page_or_region: "Pricing / Homepage — retro software-box CTA parody"
  tile_path: "store/posthog-com/captures/2026-06-16/tiles/pricing/tile-05-y06100.png"
  claim: "The retro 90s software-box CTA (3D product-box render, real G2 Leader badge, CD-ROM, hand-lettered 'NOT ENDORSED BY KIM K' starburst) is a deliberate parody artifact mixing photoreal product renders with flat brand elements — readable as a joke but intentionally rough, tonally apart from the otherwise clean system."
  visible_tells:
    - "3D product-box and CD-ROM renders with a real G2 Leader badge pasted on"
    - "Hand-lettered orange starburst overlay in a mismatched style"
    - "Photoreal hardware renders sit beside flat brand typography on a bare linen ground"
  confidence: medium
```

## Provenance

- **Tiles read (Tier-A cached, native-resolution):** 22 tiles across 5 pages — `homepage` (4), `pricing` (7), `ai` (9), `about` (1), `products` (2) — from `store/posthog-com/captures/2026-06-16/tiles/`. Pages chosen to span the visual system; `/handbook/brand/assets` (a handbook page) was not mined.
- **QA gate:** `clean` — all five page overviews rendered fully (no overlays, grey/WebGL heroes, black media, or lazy-load gaps); no tiles excluded, no Tier-B browser re-render needed.
- **Blind mining:** 4 family miners (Sonnet, tiles-only, no dossier/web) → judge prune/merge (54 mined → 44 accepted). One accepted card (`layout_06`, a partner-card row read as "clipped") was dropped at the post-mining structural spot-check: it is a horizontal-scroll carousel cut by the screenshot's right edge — a capture/scroll artifact, not a layout defect. Final: **43 cards** (26 strong · 14 mixed · 3 poor).
- **Spot-check note:** the three `poor` cards were verified against their native tiles as genuine, fully-rendered design elements — not capture artifacts. `[layout_14]`'s MS-Paint embed and `[iconography_09]`'s software-box are *intentional* anti-slick parody (corroborated by the CRT-TV container `[iconography_04]`); the polarity reflects unrefined finish read blind, the brand intent is deliberate.
- **Snapshot caveat:** a point-in-time read of the 2026-06-16 captured tiles; PostHog ships frequently and rotates illustrations — re-tile to refresh.
