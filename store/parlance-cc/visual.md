---
schema_version: "1.0"
domain: parlance.cc
captured_at: 2026-06-16
source_capture: 2026-06-10
qa_status: clean
---

## Visual & brand impression

Confident editorial minimalism with real art direction. A flush-left system runs the whole site: oversized display type stepping cleanly down from hero to nav [typography_01], a tight off-white / forest-green / near-black palette that never drifts [color_02], and disciplined repeating components - a three-up offering grid, left-label modules, a split-column article template, a structured footer [layout_02][layout_03][layout_07][layout_08]. The imagery carries it: a tactile textile-macro hero, bespoke 3D product renders, unified dark cinematic thumbnails [color_01][iconography_01][color_03]. It frays at the edges - a centered CTA panel breaks the flush-left rule [layout_12], an untreated TIME cover breaks the curated card set [color_08], and interior pages thin into sparse voids and single-card rows [layout_10][layout_11]. Founder-studio coded: sharp, owned, occasionally overstretched.

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: "homepage hero — above-the-fold headline vs nav"
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-00-y00000.png
  claim: "The hero headline is a large bold sans-serif set roughly 4-5x the nav text size, establishing a clear top-of-scale anchor with strong weight contrast against fine nav labels."
  visible_tells:
  - "Multi-line headline 'It's never been easier to start a company...' in heavy weight at large display scale"
  - "Nav items ('Work', 'Info', 'Contact') rendered tiny — a several-fold scale jump from nav to headline"
  confidence: high
  contrast_with: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-01-y01220.png
- id: typography_02
  family: typography_hierarchy
  polarity: strong
  page_or_region: "homepage — 'Creating breakthroughs is what you do' display block"
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-06-y07320.png
  claim: "The 'Creating breakthroughs is what you do...' block deploys the largest display type on the page — a commanding scale, isolated on white, that makes the two-clause structure unmissable."
  visible_tells:
  - "Four-line block of large display-weight text occupying the full left column"
  - "No competing text adjacent — the typographic mass is isolated for maximum impact"
  confidence: high
- id: typography_03
  family: typography_hierarchy
  polarity: strong
  page_or_region: "homepage — intro paragraph with inline accent terms"
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-01-y01220.png
  claim: "The intro paragraph sits at a clearly intermediate size — larger than the 'Offering' section label below, smaller than headlines — sustaining a legible three-level hierarchy through the scroll."
  visible_tells:
  - "'Parlance is a solo-operator venture creation studio...' set at a comfortable body size, visibly larger than the small 'Offering' label"
  - "Green inline color distinguishes 'Parlance' and 'Creative Capital' as accent terms within otherwise neutral body text"
  confidence: high
- id: typography_04
  family: typography_hierarchy
  polarity: strong
  page_or_region: "homepage — 'Complex challenge. Accepted.' phrase"
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-05-y06100.png
  claim: "A two-line display phrase carries its contrast through color, not weight — 'Complex challenge.' in black, 'Accepted.' in bright green at the same size — splitting one sentence into a visual call-and-response."
  visible_tells:
  - "'Complex challenge.' black bold; 'Accepted.' green bold directly beneath, identical size and weight"
  - "No body copy adjacent; the phrase sits on a generous off-white ground"
  confidence: high
- id: typography_05
  family: typography_hierarchy
  polarity: strong
  page_or_region: "interior pages — breadcrumb / title / author three-level header (scottwitt, sprints, faq, fte, cc)"
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/scottwitt/tile-00-y00000.png
  claim: "Interior pages share a clean three-level type header — tiny breadcrumb label, large display title, intermediate author/date line, divided by a hairline rule — applied consistently across every inner page."
  visible_tells:
  - "scottwitt: small 'Parlance' breadcrumb, large 'About & Contact' title, intermediate 'Scott Witt | Founder' line"
  - "Same ladder (small breadcrumb / large title / author+date / hairline rule) repeats on the Sprints and FAQ headers"
  confidence: high
  contrast_with: store/parlance-cc/captures/2026-06-10/tiles/sprints/tile-00-y00000.png
- id: typography_06
  family: typography_hierarchy
  polarity: strong
  page_or_region: "faq / sprints — bold-label vs regular-body two-level rhythm in prose"
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/faq/tile-00-y00000.png
  claim: "Within dense prose, bold lead-in labels reliably contrast against regular-weight body, plus a third caps-spaced section-header level — a clean rhythm sustained across the FAQ and Sprints bodies."
  visible_tells:
  - "FAQ: bold questions ('Who is Parlance?', 'Are you a consultancy?') over regular answer paragraphs, under caps headers ('ABOUT', 'PRICING & COMPENSATION')"
  - "Sprints body repeats the device: bold 'Naming Sprint' / 'Story Sprint' over lighter descriptor lines"
  confidence: high
  contrast_with: store/parlance-cc/captures/2026-06-10/tiles/sprints/tile-00-y00000.png
- id: typography_07
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "homepage — offering section caps labels vs body copy"
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-02-y02440.png
  claim: "Section labels ('CATEGORY CREATION', 'NARRATIVE CLARITY', 'LEADERSHIP WITHOUT LIMITS') read as a hierarchy level via uppercase casing alone — the body copy below is nearly the same size with no bold weight, compressing the step between label and description."
  visible_tells:
  - "All-caps labels sit just above same-width body paragraphs with minimal size differential"
  - "No bold weight on the labels — casing alone is carrying the hierarchy"
  confidence: high
- id: typography_08
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "scottwitt — Mentorship / Office Hours label vs detail"
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/scottwitt/tile-01-y01029.png
  claim: "Section labels ('Mentorship', 'Office Hours', 'Connect with Scott') sit at the same weight and a similar size to the detail content beside them, leaning on layout position and rule lines rather than typographic contrast to separate label from content."
  visible_tells:
  - "'Mentorship' / 'Office Hours' labels read at roughly the same weight as the listing items ('Navigating Transitions', '$225 / 30 Mins') beside them"
  - "Only white space and dashed rule lines create separation — no clear weight step"
  confidence: high
- id: typography_09
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "homepage — 'Organizations Supported' label vs client list"
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-06-y07320.png
  claim: "The 'Organizations Supported' label is actually smaller than the client-name list it heads, so it doesn't lead visually — the names read as the dominant column with the label as a faint sub-note."
  visible_tells:
  - "Two-line 'Organizations Supported' label is set small; company names ('Constellation', 'Aescape', 'Harlowe'...) are visibly larger"
  - "No weight or color differentiation between label and list entries"
  confidence: high
- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: "homepage hero — vertical zoning of thin nav, headline column, full-bleed image"
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-00-y00000.png
  claim: "The hero stacks three layers in distinct vertical bands — a near-weightless nav strip, a flush-left headline in its own band, then a full-bleed edge-to-edge image — none competing for the same horizontal zone."
  visible_tells:
  - "Nav is a thin strip with logo, two links and one pill CTA, near-zero visual weight"
  - "Headline occupies the top-left at large scale with no element beside it"
  - "Full-bleed textile photo cuts edge-to-edge below with no gutter or padding"
  confidence: high
- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: "homepage — three-up offering card grid"
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-01-y01220.png
  claim: "The three offering cards form a strict equal-width grid with uniform gutters and matched image heights — a disciplined repeating component."
  visible_tells:
  - "Three image cards equal in width with matching top and bottom edges"
  - "Uniform gutter between cards, proportionate to card width"
  - "Card tops share the same baseline"
  confidence: high
- id: layout_03
  family: layout_composition_components
  polarity: strong
  page_or_region: "homepage — recurring left-label / right-content two-column module (Focus, Organizations Supported)"
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-02-y02440.png
  claim: "A left-label / right-content two-column module, opened by a full-width hairline rule, recurs across sections (Focus, Organizations Supported) — confirming it as a site-wide layout system rather than one-off styling."
  visible_tells:
  - "Focus: small 'Focus' label anchored left, topic tags as a right-aligned vertical column with per-row divider rules"
  - "Organizations Supported (tile-06): same left-label / right-list split, opened by the same thin full-width rule"
  confidence: high
  contrast_with: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-06-y07320.png
- id: layout_04
  family: layout_composition_components
  polarity: strong
  page_or_region: "homepage — Notes section: mixed-span card grid"
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-03-y03660.png
  claim: "The Notes section runs a controlled three-column card rhythm with left-aligned captions under each card, a grid variant that reads as deliberate rather than accidental."
  visible_tells:
  - "Cards (.cc, Sprints, FTE, Mentorship, Genagraph, FAQ) align to a consistent three-column grid across two rows"
  - "Caption text below each card aligns to the card's left edge"
  confidence: high
- id: layout_05
  family: layout_composition_components
  polarity: strong
  page_or_region: "homepage — 'Hire Parlance To' numbered accordion"
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-03-y03660.png
  claim: "The 'Hire Parlance To' accordion uses a fixed left numeral column and a far-right expand indicator, with rows divided by evenly spaced hairline rules — a tight repeating component on a visible grid."
  visible_tells:
  - "'01 / 02 / 03' numerals in a fixed left column"
  - "Expand glyph consistently at far right; rows separated by thin rules at identical spacing"
  confidence: medium
- id: layout_06
  family: layout_composition_components
  polarity: strong
  page_or_region: "homepage — Projects grid: 2-up over 3-up asymmetric rows"
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-04-y04880.png
  claim: "The Projects grid mixes a two-column top row (two ~50% cards) with a three-column bottom row (three ~33% cards), varying card size within one column grid while holding the outer margins."
  visible_tells:
  - "Top row: two cards of roughly equal half-width (The Marque, Naming)"
  - "Bottom row: three equal third-width cards (Aescape, WelcomePAC, Fisher Wallace Labs)"
  - "All card edges align to the same outer left/right margins as the rest of the page"
  confidence: high
- id: layout_07
  family: layout_composition_components
  polarity: strong
  page_or_region: "interior pages — split-column article template (faq, sprints, fte, cc)"
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/faq/tile-00-y00000.png
  claim: "Inner article pages share one two-column template — breadcrumb/title/author in the narrow left column, a rounded hero image top-right, body content beneath the right column — repeated without variation across at least four pages."
  visible_tells:
  - "FAQ: left column holds breadcrumb + 'FAQ' title + avatar/author; right column holds the rounded teal/orange hero, body below"
  - "Sprints, FTE and CC pages repeat the identical left-meta / right-hero / right-body arrangement"
  confidence: high
  contrast_with: store/parlance-cc/captures/2026-06-10/tiles/sprints/tile-00-y00000.png
- id: layout_08
  family: layout_composition_components
  polarity: strong
  page_or_region: "footer — multi-column system consistent across pages"
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-07-y08275.png
  claim: "The near-black footer is a disciplined multi-column system — brand/tagline + Email pill at left, two live city-clock columns mid, a nav column at right, social pills top-right — reusing the same pill component seen in nav and CTA."
  visible_tells:
  - "Distinct columns: tagline + teal 'Email' pill, 'Menlo Park 21:13:19' and 'Stockholm 06:13:19' clock stacks, 'Work / Info / Contact' nav"
  - "Instagram / LinkedIn / Dot.share pill buttons top-right reuse the nav/CTA pill shape"
  - "Same footer recurs across homepage, scottwitt and fte tiles"
  confidence: high
- id: layout_09
  family: layout_composition_components
  polarity: mixed
  page_or_region: "homepage — intro body text vs far-right 'Book Time' CTA"
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-01-y01220.png
  claim: "The body description is narrow and left-anchored while the 'Book Time' pill floats to the far right on a lower baseline, leaving a wide empty middle and no visual connector — the two elements feel weakly related."
  visible_tells:
  - "Body copy occupies roughly the left 40% of the width"
  - "Teal 'Book Time' pill is pushed to the far right with a large empty middle zone and no line or proximity tying it to the text"
  confidence: high
- id: layout_10
  family: layout_composition_components
  polarity: mixed
  page_or_region: "scottwitt — Mentorship / Office Hours sparse two-column voids"
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/scottwitt/tile-01-y01029.png
  claim: "The Mentorship / Office Hours sections reuse the left-label / right-content split, but with only a two-word label at left and a short list at right, both columns carry large empty voids and the section rules give little payoff."
  visible_tells:
  - "'Mentorship' / 'Office Hours' sit alone in a half-page left column with no supporting sub-content"
  - "Right column (short list + one pill) is brief, leaving wide blank space across both columns"
  confidence: medium
- id: layout_11
  family: layout_composition_components
  polarity: mixed
  page_or_region: "sprints — 'More Articles' row: one card in a multi-column grid"
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/sprints/tile-01-y01110.png
  claim: "The 'More Articles' row on the Sprints page holds a single card in what reads as a multi-column grid, leaving most of the row empty and the section feeling incomplete."
  visible_tells:
  - "One 'AI You Can Feel' card in the leftmost column"
  - "The rest of the row is empty white space, with 'Read all articles' pill stranded at far right"
  confidence: high
- id: layout_12
  family: layout_composition_components
  polarity: poor
  page_or_region: "homepage — full-bleed CTA panel: centered text breaks the flush-left system"
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-07-y08275.png
  claim: "The dark-green CTA panel centers a three-line headline and a lone pill — the only centered-text module on a site otherwise built flush-left — and the headline breaks unevenly with a short orphan third line."
  visible_tells:
  - "'Proudly supporting the Founders, Investors & Operators of tomorrow's iconic companies' centered across three uneven lines"
  - "Centered teal 'Contact' pill floats below with no secondary anchor; every other section is left-aligned"
  confidence: medium
- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: "homepage hero — full-bleed textile macro with overlaid wordmark"
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-00-y00000.png
  claim: "The hero is a close-cropped, desaturated macro of knotted rope and woven textile with the 'Parlance' wordmark set in white inside it — a tactile, art-directed concept image, not stock corporate photography."
  visible_tells:
  - "Full-bleed near-monochrome warm-grey textile macro filling the lower hero"
  - "Large white 'Parlance' wordmark overlaid into the image rather than placed above it"
  confidence: high
- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: "site-wide palette — off-white ground, forest-green band, near-black footer, restrained green accent"
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-07-y08275.png
  claim: "A tight palette holds without drift across pages: warm off-white body ground, one deep forest-green CTA band, near-black footer, with green reserved for a single inline link and the band — never scattered as decoration."
  visible_tells:
  - "Deep forest-green CTA band over near-black footer base on the homepage tile"
  - "Same off-white ground and green-only accent recur on faq, sprints, fte and cc tiles"
  - "Green confined to one inline link ('Creative Capital') and the band, not used decoratively elsewhere"
  confidence: high
- id: color_03
  family: color_brand_imagery
  polarity: strong
  page_or_region: "homepage — Notes card grid: unified dark cinematic thumbnails with white italic labels"
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-03-y03660.png
  claim: "The Notes/section cards share one editorial register — dark, moody photographic stills with a white italic serif label overlaid on each — giving the grid a consistent cinematic identity with no bright stock card breaking the set."
  visible_tells:
  - "Darkened doorway (.cc), sepia dashboard (Sprints), night street (FTE), fashion still (Genagraph) — all dark-toned with white italic overlay"
  - "Teal/orange chevron (FAQ) is the one graphic card, still dark and same-treatment"
  confidence: high
- id: color_04
  family: color_brand_imagery
  polarity: strong
  page_or_region: "homepage / faq — recurring teal + burnt-orange chevron graphic device"
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/faq/tile-00-y00000.png
  claim: "A teal-field / burnt-orange chevron composition recurs as a controlled brand device — full-size as the FAQ hero and again as a thumbnail in the homepage Notes grid — confirming it's a deliberate motif, not an incidental image."
  visible_tells:
  - "FAQ hero: hard-edged orange chevron over dark teal with a human silhouette integrated and italic 'faq' wordmark"
  - "Same teal/orange chevron recurs as a thumbnail card in the homepage Notes grid and inner-page 'More Articles' carousels"
  confidence: high
  contrast_with: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-03-y03660.png
- id: color_05
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "homepage — Projects grid: mixed image source types under a controlled tonal register"
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-04-y04880.png
  claim: "The Projects grid keeps a controlled tonal register but visibly mixes image source types — high-production editorial portrait, a moody typographic landscape, a flat primary-color vector illustration, and a plain headshot — so the visual language is not uniform."
  visible_tells:
  - "Studio-lit portrait with gold 'M' (The Marque) and dark 'NAMING' landscape read as editorial/cinematic"
  - "WelcomePAC card is a flat orange/blue vector illustration — a different visual language"
  - "Fisher Wallace Labs is a plain neutral-background headshot — more utilitarian"
  confidence: high
- id: color_06
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "homepage / sprints — reel-to-reel and dashboard photos lean on familiar 'analog/speed' tropes"
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-05-y06100.png
  claim: "Two atmospheric photos lean on well-worn creative metaphors — a reel-to-reel tape deck under 'Complex challenge. Accepted.' and a driver's-eye dashboard as the Sprints hero — tonally on-brand but reading as familiar 'analog creativity / speed = urgency' stock tropes rather than owned imagery."
  visible_tells:
  - "Full-width dark reel-to-reel tape-deck photo, with green 'Accepted.' the only color pop"
  - "Sprints hero: sepia driver's-eye dashboard/speedometer, a generic 'speed' metaphor, italic 'Sprints' overlaid to unify it"
  confidence: medium
  contrast_with: store/parlance-cc/captures/2026-06-10/tiles/sprints/tile-00-y00000.png
- id: color_07
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "fte — inner hero card thin when the underlying photo is unremarkable"
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/fte/tile-00-y00000.png
  claim: "The inner hero-card template (dark image + italic serif label) holds structurally, but the FTE card's shallow, low-contrast photo contributes little — revealing the system depends on image quality and feels inert when the photo is unremarkable."
  visible_tells:
  - "FTE hero: very dark, low-contrast image with italic 'fte' label — minimal compositional interest"
  - "Identical card structure to the FAQ chevron and textile hero, but visibly weaker image"
  confidence: medium
  contrast_with: store/parlance-cc/captures/2026-06-10/tiles/faq/tile-00-y00000.png
- id: color_08
  family: color_brand_imagery
  polarity: poor
  page_or_region: "inner pages — 'More Articles' carousel surfaces an external TIME magazine cover"
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/faq/tile-02-y02026.png
  claim: "The 'More Articles' carousel drops a TIME 'Best Inventions of 2024' magazine cover in as an article thumbnail — a third-party masthead with no crop, overlay, or desaturation to unify it — breaking the otherwise tightly curated card language."
  visible_tells:
  - "Full TIME cover (logo, 'BEST INVENTIONS of 2024' headline, white robotic-arm photo) sits as a card beside proprietary editorial cards"
  - "No treatment ties it to the dark italic-label card system; recurs at full size on faq and fte carousels"
  confidence: high
  contrast_with: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-03-y03660.png
- id: iconography_01
  family: iconography_illustration
  polarity: strong
  page_or_region: "homepage — offering grid: bespoke 3D-rendered product objects"
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-01-y01220.png
  claim: "The three offering thumbnails are bespoke 3D renders — a copper tube assembly, scattered teal capsules, and a cream coiled form — sharing one matte palette and consistent shallow-depth-of-field lighting, signalling a production-heavy image direction well above stock."
  visible_tells:
  - "Copper metallic tube/ring render on a pink-grey ground, lower-left card"
  - "Scattered teal cylinders with a pink disc on grey, center card; cream coiled form on warm wood, right card"
  - "All three share the same render quality and lighting direction"
  confidence: high
- id: iconography_02
  family: iconography_illustration
  polarity: strong
  page_or_region: "homepage — section/Notes card thumbnails as per-section scenes"
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-03-y03660.png
  claim: "Each section card carries a distinct photographic or graphic scene chosen to signal that section's tone — a darkened doorway, a dashboard close-up, a fashion still, a bold orange chevron — rather than a single templated thumbnail treatment."
  visible_tells:
  - ".cc: darkened doorway with serif overlay; Sprints: sepia dashboard gauges"
  - "Genagraph: dramatic fashion-shoot still; FAQ: orange chevron graphic with silhouette"
  confidence: high
- id: iconography_03
  family: iconography_illustration
  polarity: mixed
  page_or_region: "homepage — Projects thumbnails: client-sourced mix of treatments"
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-04-y04880.png
  claim: "Project thumbnails mix creative approaches — gold monogram on a photo, a text-only typographic lockup, editorial photography, and a flat illustration — reflecting client-sourced diversity rather than a single unified illustration system."
  visible_tells:
  - "The Marque: gold 'M' monogram on a photographic portrait; Naming: text-only typographic lockup on a dark gradient"
  - "WelcomePAC: flat orange/blue vector illustration; Fisher Wallace Labs: plain product/person photo"
  confidence: high
- id: iconography_04
  family: iconography_illustration
  polarity: mixed
  page_or_region: "site-wide — single circle-glyph logomark and pill-button prefix is the entire UI-icon system"
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-07-y08275.png
  claim: "Iconography is limited to one custom circular emblem — used as the logomark beside the 'Parlance' wordmark and repeated as a small circle prefix on every pill button — consistent and on-brand, but minimal, with no broader icon set anywhere."
  visible_tells:
  - "Circular emblem glyph left of the 'Parlance' wordmark in nav and footer"
  - "Same small circle prefixes 'Contact', 'Email', 'Instagram', 'LinkedIn', 'Dot.share' pills; no other icon types appear"
  confidence: high
- id: iconography_05
  family: iconography_illustration
  polarity: poor
  page_or_region: "all pages — no charts, diagrams, or data graphics anywhere"
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/faq/tile-01-y01220.png
  claim: "No charts, diagrams, process graphics, or infographics appear in any tile — the site communicates purely through photography, type, and editorial composition, leaving diagram/data-visualization craft undemonstrable."
  visible_tells:
  - "FAQ body tile is entirely text-on-white with no graphic element"
  - "Even pricing ('$15k', '$225 / 30 Mins') and engagement detail are plain text lists, never a table or process flow"
  confidence: high
```

## Provenance

Tiles read: homepage (8) + creative_capital (2) + faq (3) + fte (2) + scottwitt (2) + sprints (2) from `captures/2026-06-10/tiles/` — all 19 active, no exclusions. QA gate: **clean** — every page's `overview-480w.png` plus native spot-checks (homepage hero/notes, faq body, sprints More-Articles row, the CTA/footer band) showed no overlay, grey/WebGL hero, black media, lazy-load gap, or mid-animation; **no Tier-B browser re-render was needed** (`shoot.py` / `--dismiss` not invoked on this capture). Run provenance: blind fan-out — 4 Sonnet family miners → Opus judge over the active tiles only via `skills/visual-evidence/mine.workflow.js`, 2026-06-16; no profile, dossier, Notion, or live web consulted (48 raw cards mined → 34 accepted). One sighted post-judge correction: `color_04`'s `contrast_with` was repointed from `sprints/tile-01` (which actually shows the TIME card, not the chevron) to `homepage/tile-03`, where the chevron thumbnail genuinely recurs. Snapshot caveat: reflects the 2026-06-10 capture; the live site changes.
