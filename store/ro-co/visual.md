---
schema_version: "1.0"
domain: ro.co
captured_at: 2026-06-16
source_capture: 2026-06-04
qa_status: recapture-used
---

## Visual & brand impression

Restrained DTC-health design that reads premium through discipline, not decoration: a near-white/near-black system with a single warm terracotta accent [color_01], used even as the hierarchy device in the two-tone pricing headline [typography_02]. The strength is systematized structure — tightly repeating pricing cards [layout_02], a uniform GLP-1 carousel [layout_03], and a controlled hero grid [layout_01]. The ro.OS page is the high point: one reused left-text/right-mockup template [layout_04] over a custom gradient-blob illustration system [iconography_01] with a high-fidelity dashboard render [iconography_02]. It frays at the seams — flat secondary-text hierarchy [typography_07][typography_08], photo- and numeral-as-icon stand-ins [iconography_05][iconography_07], and palette breaks: a dark-red sexual-health mood [color_07], a one-off lavender band [color_05], and a cool ro.OS split from the warm consumer pages [color_06].

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: homepage hero — 'Healthier on Ro' page heading
  tile_path: store/ro-co/captures/2026-06-04/tiles/homepage/tile-00-y00000.png
  claim: The hero heading 'Healthier on Ro' is set at a large size in a light-to-medium-weight sans, left-aligned with generous white-space above and below, establishing a clean top of the type scale that reads instantly.
  visible_tells:
  - Heading runs roughly 3-4x the nav link size
  - Ample whitespace separates it from the nav row and the card modules below
  confidence: high
- id: typography_02
  family: typography_hierarchy
  polarity: strong
  page_or_region: pricing page — hero heading 'Transparent pricing, always' (two-tone)
  tile_path: store/ro-co/captures/2026-06-04/tiles/pricing/tile-00-y00000.png
  claim: The display headline splits one phrase into two colors — 'Transparent pricing,' in warm terracotta-orange and 'always' in black at the same face and size — using color rather than weight as the hierarchy device, and it is the only colored text on the page.
  visible_tells:
  - First clause rendered in terracotta-orange, second clause in black, identical size and weight
  - No other heading or body text on the tile uses color, so the accent reads as deliberate
  confidence: high
  contrast_with: store/ro-co/captures/2026-06-04/tiles/pricing/tile-01-y01220.png
- id: typography_03
  family: typography_hierarchy
  polarity: strong
  page_or_region: pricing page — left-column category headings
  tile_path: store/ro-co/captures/2026-06-04/tiles/pricing/tile-05-y06100.png
  claim: Category headings ('Genital herpes', 'Men's Multivitamin') are set at a consistent large size that is clearly 2-3x the body copy beneath them, giving every product section a legible H2 that anchors the left navigation column.
  visible_tells:
  - "'Genital herpes' heading is visibly several times larger than the prose paragraph below it"
  - Same treatment recurs at every category section down the page
  confidence: high
- id: typography_04
  family: typography_hierarchy
  polarity: strong
  page_or_region: homepage — '3,000,000+ members' stat callout
  tile_path: store/ro-co/captures/2026-06-04/tiles/homepage/tile-04-y04880.png
  claim: The '3,000,000+' figure is rendered at display scale as the largest numeral on the tile, with a small eyebrow label above and a caption beneath, producing a clean two-level stat hierarchy.
  visible_tells:
  - Numeral towers over the surrounding text at several lines of body-height
  - Small label sits directly above it and a caption/pull-quote sits below at much smaller size
  confidence: high
- id: typography_05
  family: typography_hierarchy
  polarity: strong
  page_or_region: weight-loss page — hero heading over white panel
  tile_path: store/ro-co/captures/2026-06-04/tiles/weight-loss/tile-00-y00000.png
  claim: The hero heading 'Get access to prescription weight loss medication online' is large, left-aligned black type set on the white page panel above the photo strip, keeping it fully legible without resorting to a text-shadow or photo overlay.
  visible_tells:
  - Heading sits on clean white above the three-panel photo row, not over imagery
  - It is the largest text unit on the tile, spanning two lines at display size
  confidence: high
- id: typography_06
  family: typography_hierarchy
  polarity: mixed
  page_or_region: ro.OS page — feature-section text levels (Care Delivery / Pharmacy App)
  tile_path: store/ro-co/captures/2026-06-04/tiles/os/tile-02-y02440.png
  claim: Each ro.OS feature block opens well with a tiny green 'Powered by ro.OS' eyebrow and an H2-scale product name, but the supporting body paragraph drops to a small size very close to the eyebrow's register, so below the heading the levels compress.
  visible_tells:
  - "Eyebrow 'Powered by ro.OS' is the smallest level; 'Care Delivery App' is the clear H2"
  - Body paragraph beneath the heading sits at a small size with little weight separation from the eyebrow
  confidence: medium
  contrast_with: store/ro-co/captures/2026-06-04/tiles/os/tile-03-y03660.png
- id: typography_07
  family: typography_hierarchy
  polarity: poor
  page_or_region: homepage — 'Backed by the country's leading health experts' block
  tile_path: store/ro-co/captures/2026-06-04/tiles/homepage/tile-05-y06100.png
  claim: The advisory section's body paragraph, credential bullets, and doctor name/title labels are all set at small, near-identical sizes with no weight contrast, flattening the block so no element reads as more important than another.
  visible_tells:
  - Body copy, the three credential bullets, and the doctor captions all render at similar compact size
  - Doctor name labels ('Dr. Malyeda Barnes, MD') carry the same weight as the institution line below them
  confidence: medium
  contrast_with: store/ro-co/captures/2026-06-04/tiles/homepage/tile-00-y00000.png
- id: typography_08
  family: typography_hierarchy
  polarity: poor
  page_or_region: pricing page — expanded product-card safety text
  tile_path: store/ro-co/captures/2026-06-04/tiles/pricing/tile-05-y06100.png
  claim: Inside the product cards the expanded Valacyclovir safety paragraph sits at the same small size as the 'Important safety information' disclosure label above it, with no size or weight step between the heading and the multi-sentence body — a flat disclosure zone.
  visible_tells:
  - Multi-line safety warning runs at near-footnote size, indistinguishable from the disclosure link label
  - No graduated hierarchy separates the disclosure headline from its paragraph
  confidence: high
- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: homepage hero — dual card + shortcut grid
  tile_path: store/ro-co/captures/2026-06-04/tiles/homepage/tile-00-y00000.png
  claim: The above-fold uses a controlled two-column card grid sharing a precise baseline and corner radius, with a row of three shortcut tiles below repeating the same gutter — a coherent grid rather than ad-hoc placement.
  visible_tells:
  - "Two equal-width image cards ('New GLP-1 options', 'Lose weight on GLP-1s') align on a shared horizontal baseline with matching radius"
  - Three shortcut tiles below carry the same gutter and alignment as the cards above
  confidence: high
- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: pricing page — product-card component system
  tile_path: store/ro-co/captures/2026-06-04/tiles/pricing/tile-01-y01220.png
  claim: Pricing cards are a tightly controlled component — thumbnail, name, dose/price rows, 'Get started' button, collapsible safety footer — repeating identically across every card with no padding or height drift.
  visible_tells:
  - Four cards (Generic/Branded Viagra, Generic/Daily Generic Cialis) share identical internal padding, label positions, and button width
  - "The 'Most popular' tag sits at the same inline position within each card that carries it"
  confidence: high
  contrast_with: store/ro-co/captures/2026-06-04/tiles/pricing/tile-03-y03660.png
- id: layout_03
  family: layout_composition_components
  polarity: strong
  page_or_region: homepage — GLP-1 product carousel
  tile_path: store/ro-co/captures/2026-06-04/tiles/homepage/tile-01-y01220.png
  claim: The medication carousel holds each card to a fixed width with image, name, availability badge, two-button CTA and safety link in a uniform vertical stack, with availability badges pinned at the same top offset on every card.
  visible_tells:
  - Five visible cards (Wegovy pill, Zepbound KwikPen, Foundayo, Wegovy pen, Zepbound) share identical height and slot order
  - "Status badges ('In stock', 'New', 'New and in stock') sit at the same top-left offset on each card"
  confidence: high
- id: layout_04
  family: layout_composition_components
  polarity: strong
  page_or_region: ro.OS page — left-text / right-mockup section template
  tile_path: store/ro-co/captures/2026-06-04/tiles/os/tile-02-y02440.png
  claim: The ro.OS feature sections reuse one left-text / right-UI-mockup split — eyebrow, heading, body, pill CTA in the same slot order on the left, the app render floated right inside a soft gradient blob — applied without drift across Patient, Care Delivery and Pharmacy App.
  visible_tells:
  - Left column slot order (eyebrow + heading + body + pill button) is identical between Care Delivery and Pharmacy sections
  - UI mockup is right-aligned within a soft gradient blob at the same relative scale each time
  confidence: high
  contrast_with: store/ro-co/captures/2026-06-04/tiles/os/tile-03-y03660.png
- id: layout_05
  family: layout_composition_components
  polarity: mixed
  page_or_region: weight-loss page — stacked sections run together
  tile_path: store/ro-co/captures/2026-06-04/tiles/weight-loss/tile-04-y04880.png
  claim: Two distinct sections — 'What's included in the Ro Body membership?' and 'Explore your GLP-1 options' — stack on the same white ground at the same body size with no divider, color shift, or generous gap, so they visually run together as one unit.
  visible_tells:
  - The membership bullet list ends and the next headline begins with little vertical breathing room
  - No rule, background change, or spacing signals the section break
  confidence: medium
- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: homepage — overall palette discipline
  tile_path: store/ro-co/captures/2026-06-04/tiles/homepage/tile-00-y00000.png
  claim: The site runs a disciplined near-white / near-black palette with a single warm terracotta-blush accent reserved for a marketing moment, not scattered through the UI chrome.
  visible_tells:
  - Nav and body are black-on-white with no secondary UI colors
  - The blush/terracotta tone appears only in a hero band, not in nav, cards, or utility copy
  confidence: high
- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: homepage — GLP-1 product photography language
  tile_path: store/ro-co/captures/2026-06-04/tiles/homepage/tile-01-y01220.png
  claim: Product photography across the medication rail shares one close-crop studio treatment — clean neutral/pastel gradient grounds, no clutter — and the availability badge chips are a single uniform muted teal/sage, giving the row a coherent image language.
  visible_tells:
  - Each drug card (Wegovy pill, Zepbound, Foundayo, Wegovy pen) uses the same neutral-gradient studio ground at matching scale
  - "'New' / 'New and in stock' badge chips are the same muted green on every card"
  confidence: high
- id: color_03
  family: color_brand_imagery
  polarity: strong
  page_or_region: hair-loss page — Ro private-label product photography
  tile_path: store/ro-co/captures/2026-06-04/tiles/hair-loss/tile-04-y04880.png
  claim: Ro's own products (Revive Shampoo, Restore Conditioner) are shot as identical matte-black bottles against the same neutral off-white ground, signalling a coherent private-label identity that matches the site's restraint.
  visible_tells:
  - Two matte-black cylindrical bottles with minimal label and 'ro' mark at the same angle and scale
  - No props or colored backdrops — pure white-ground studio photography
  confidence: high
- id: color_04
  family: color_brand_imagery
  polarity: mixed
  page_or_region: homepage — UGC testimonial video grid
  tile_path: store/ro-co/captures/2026-06-04/tiles/homepage/tile-04-y04880.png
  claim: The testimonial section breaks the controlled photographic palette with a grid of vertical smartphone-shot member videos whose mixed lighting, settings, and color casts contrast visibly with the produced imagery elsewhere.
  visible_tells:
  - Video stills show mixed domestic settings with uncontrolled warm/cool casts
  - Adjacent produced sections (doctor portraits) use even neutral studio light, making the contrast plain
  confidence: high
  contrast_with: store/ro-co/captures/2026-06-04/tiles/homepage/tile-05-y06100.png
- id: color_05
  family: color_brand_imagery
  polarity: mixed
  page_or_region: weight-loss page — lavender one-off section
  tile_path: store/ro-co/captures/2026-06-04/tiles/weight-loss/tile-03-y03660.png
  claim: A full-width solid lavender/purple band appears behind a posed member photo as a one-off color that is not drawn from the rest of the palette, loosening the otherwise tight color discipline.
  visible_tells:
  - "Full-bleed lavender background behind the 'Healthier on Ro' member section"
  - This lavender does not recur on any other tile in the set
  confidence: high
  contrast_with: store/ro-co/captures/2026-06-04/tiles/homepage/tile-00-y00000.png
- id: color_06
  family: color_brand_imagery
  polarity: mixed
  page_or_region: ro.OS page — cool teal/blue palette vs warm consumer pages
  tile_path: store/ro-co/captures/2026-06-04/tiles/os/tile-06-y07320.png
  claim: The ro.OS page closes on a wide cool teal-to-white gradient behind the 'ro.OS' logotype — a blue palette disconnected from the warm terracotta accent used on the consumer pages, creating a cross-page palette split.
  visible_tells:
  - "Blue-teal gradient fills the band full-width behind the large 'ro.OS' type"
  - The warm terracotta accent from the consumer pages appears nowhere on this page
  confidence: high
  contrast_with: store/ro-co/captures/2026-06-04/tiles/pricing/tile-00-y00000.png
- id: color_07
  family: color_brand_imagery
  polarity: poor
  page_or_region: homepage — sexual-health block dark/red mood break
  tile_path: store/ro-co/captures/2026-06-04/tiles/homepage/tile-02-y02440.png
  claim: The sexual-health block uses a dark full-bleed close-up of bodies with a glowing red product callout, a mood and color temperature jarringly different from the white/pastel system that returns immediately in the product cards below it.
  visible_tells:
  - "Dark/black-dominant full-bleed image behind 'Better sex with fast-acting, long-lasting Ro Sparks'"
  - "Red 'Starts working in 15 mins' product callout with a glowing red ring, clashing with the muted system"
  - Product cards directly beneath snap back to the white-ground pastel look in the same scroll
  confidence: high
  contrast_with: store/ro-co/captures/2026-06-04/tiles/homepage/tile-01-y01220.png
- id: color_08
  family: color_brand_imagery
  polarity: poor
  page_or_region: hair-loss page — before/after scalp photo strip
  tile_path: store/ro-co/captures/2026-06-04/tiles/hair-loss/tile-01-y01220.png
  claim: The before/after results strip uses raw clinical top-of-head scalp photos with uneven, ungraded lighting that reads as unbranded reference imagery rather than the produced photography used elsewhere on the same page.
  visible_tells:
  - Row of cropped overhead scalp photos with visible cool/warm light shifts frame to frame
  - No consistent background or post-production grade matching the white-ground product shots on the page
  confidence: high
  contrast_with: store/ro-co/captures/2026-06-04/tiles/hair-loss/tile-04-y04880.png
- id: iconography_01
  family: iconography_illustration
  polarity: strong
  page_or_region: ro.OS page — gradient-blob backdrops behind app renders
  tile_path: store/ro-co/captures/2026-06-04/tiles/os/tile-01-y01220.png
  claim: The ro.OS sections float polished app/dashboard renders over soft custom multi-color gradient blobs (orange-teal, blue, yellow-green, red-purple variants) — a repeated, clearly-designed illustrative system that is the most considered visual treatment on the site.
  visible_tells:
  - Patient App phone mockup sits over a soft orange-teal gradient blob with deliberate depth and shadow
  - The same blob device recurs in matching softness/opacity behind the Care Delivery, Pharmacy and Lab renders
  confidence: high
  contrast_with: store/ro-co/captures/2026-06-04/tiles/homepage/tile-03-y03660.png
- id: iconography_02
  family: iconography_illustration
  polarity: strong
  page_or_region: ro.OS page — Care Delivery App dashboard render fidelity
  tile_path: store/ro-co/captures/2026-06-04/tiles/os/tile-02-y02440.png
  claim: The Care Delivery dashboard mockup is rendered with convincing UI fidelity — a 'Patient Overview' header, a real weight-trend line chart with axis structure, and small legible sidebar glyphs — showing more craft than the decorative chart elements on the consumer pages.
  visible_tells:
  - "Dashboard shows a labelled weight-trend line chart ('20 lbs (8.8%)') with genuine data structure"
  - Sidebar icons (bell, chart, message) are small but consistent and legible at thumbnail scale
  confidence: high
- id: iconography_03
  family: iconography_illustration
  polarity: mixed
  page_or_region: ro.OS page — capabilities row colored letter-avatars
  tile_path: store/ro-co/captures/2026-06-04/tiles/os/tile-04-y04880.png
  claim: The 'Explore all ro.OS capabilities' row replaces icons with saturated colored circles holding two-letter abbreviations (Pi, Cc, Id, Ht, In, Qu, Hd) — identity by initial rather than symbol; uniform sizing and type give the row coherence, but the multi-color circles are the busiest color moment on the site versus its two-color restraint elsewhere.
  visible_tells:
  - Eight circles in distinct saturated colors (blue, teal, lime, orange, burgundy, red, green) each carry a two-letter label, no symbol inside
  - No other surface in the tile set uses this many colors at once
  confidence: high
- id: iconography_04
  family: iconography_illustration
  polarity: poor
  page_or_region: homepage — hero trust-signal checkmark bullets
  tile_path: store/ro-co/captures/2026-06-04/tiles/homepage/tile-00-y00000.png
  claim: The upper-right trust-signal list uses tiny circle-check glyphs with no stroke variation or brand character — interchangeable with any default SaaS checklist.
  visible_tells:
  - Four bullets with identical small circle-check marks at roughly caption scale, no color or weight differentiation
  confidence: high
- id: iconography_05
  family: iconography_illustration
  polarity: poor
  page_or_region: homepage — '100% convenient' feature row uses photos as icons
  tile_path: store/ro-co/captures/2026-06-04/tiles/homepage/tile-03-y03660.png
  claim: The four '100% online, 100% convenient' callouts each carry a small square photo or product render in place of a designed icon — one a phone-UI screenshot, another an assorted-product shot — giving the row a patchwork rather than systematized look.
  visible_tells:
  - Four distinct photographic thumbnails of inconsistent visual register sit where icons would go
  - One card shows a phone screen, another a product cluster — different visual languages within one component
  confidence: high
  contrast_with: store/ro-co/captures/2026-06-04/tiles/os/tile-04-y04880.png
- id: iconography_06
  family: iconography_illustration
  polarity: mixed
  page_or_region: weight-loss page — hero sub-value line icons
  tile_path: store/ro-co/captures/2026-06-04/tiles/weight-loss/tile-00-y00000.png
  claim: Three thin line icons under the hero (provider coaching, GLP-1 options, hunger help) are internally consistent in stroke but generic stock healthcare forms, matching the undistinguished checkmark register seen on the homepage.
  visible_tells:
  - Three monoline glyphs of even stroke weight below the headline
  - Forms read as standard stock icons (person/chat, plus, clock) with no brand-specific character
  confidence: medium
- id: iconography_07
  family: iconography_illustration
  polarity: poor
  page_or_region: hair-loss page — process steps as numbered photo cards
  tile_path: store/ro-co/captures/2026-06-04/tiles/hair-loss/tile-04-y04880.png
  claim: The 'How treating hair loss with Ro works' step strip uses photo cards with superimposed numerals instead of any iconographic language — the 'icon' is just a number over photography, with no illustrative craft.
  visible_tells:
  - Three-step row is photo cards (person, branded box, spray bottle) with plain numerals overlaid
  - No icon or illustration system carries the steps beyond the superimposed numbers
  confidence: medium
- id: iconography_08
  family: iconography_illustration
  polarity: mixed
  page_or_region: pricing page — product photos as category tab icons
  tile_path: store/ro-co/captures/2026-06-04/tiles/pricing/tile-00-y00000.png
  claim: The pricing category tab strip uses small product-photo thumbnails as navigation icons rather than a drawn icon system; the renders are clean, evenly sized and neutral-ground, so the row stays orderly even though identity is carried by the product object itself.
  visible_tells:
  - Roughly a dozen tabs each pair a small product photo (pill bottle, syringe, tube) with a label at consistent scale
  - No custom icon appears — the product photography is the icon
  confidence: high
```

## Provenance

Tiles read: homepage (8) + weight-loss (9) + pricing (9) + hair-loss (7) sliced from the cached `captures/2026-06-04/.payloads/` screenshots (Tier-A), plus os (8) browser re-rendered (Tier-B) — 41 tiles, all active, no exclusions. **Tier-B re-render:** the `os` page's cached Firecrawl capture left the Care Delivery / Pharmacy / Lab app-illustration columns empty (scroll-triggered lazy media that never fired); `scripts/shoot.py` drove system Chrome (faithful default — **no `--dismiss`**, since no overlay covered the page) to warm-scroll and settle, recovering the product-UI mockups on their gradient blobs (19/23 images loaded). The shoot manifest recorded `dismissed: false`, `scroll_locked: false`, and emitted `overview-480w.png` with no stderr WARNING — hence `qa_status: recapture-used`. The other four pages tiled clean from cached payloads.

Mined blind + judged per [`/visual-evidence`](../../skills/visual-evidence/SKILL.md): four family miners (Sonnet) saw only the tile paths (no dossier, no web), returning 49 raw cards; the judge (Opus) verified each against the cited PNG and kept 32, merging cross-family duplicates (the ro.OS gradient-blob system → one card; the capabilities letter-avatar circles → one card) and rejecting one capture artifact (a homepage card with a blank/grey image area). A final sighted spot-check of the `poor` *structural* cards against their native tiles then dropped 3 over-calls — a pricing "dead column" whose tell mis-placed the product card, a hair-loss carousel peek read as a mis-sized frame, and the homepage goal-selector grid (a uniform 2×3 grid) read as a ragged content-sized row — → **29 final cards** (14 strong / 8 mixed / 7 poor).

Snapshot caveat: reflects the 2026-06-04 capture (os section re-rendered 2026-06-16); the live site changes. Run note: executed from **Claude Code on macOS**, model **Claude Opus 4.8**.
