---
schema_version: "1.0"
domain: ivyrx.com
captured_at: 2026-06-17
source_capture: 2026-06-04
qa_status: clean
---

## Visual & brand impression

Ivy Rx reads like a polished light-wellness storefront: airy spacing, black display type, and a restrained green/pink/lavender accent system carry the first impression [typography_01][color_01]. The strongest work is the reusable commerce shell - product cards, CTA pills, QA cards, and two-column PDP sections stay aligned and calmly scannable [layout_01][layout_03][layout_05]. The brand relies more on soft gradients and repeated vial renders than deep custom illustration [color_02][iconography_01], and the softer process graphics sometimes fade toward decoration instead of information [iconography_02]. UGC review videos add social energy but visually break from the controlled system [color_04]. Overall: clean DTC-health polish, cohesive, with a few template-thin spots.

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: "homepage hero"
  tile_path: "store/ivyrx-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"
  claim: "The hero establishes a clear type ladder: oversized black display lines, one green accent phrase, a smaller grey support sentence, then a compact dark CTA pill."
  visible_tells:
    - "The headline spans two large centered lines and dominates the viewport"
    - "'Weight Loss' is the only green phrase inside the otherwise black headline"
    - "The support sentence is much smaller and grey, with the CTA separated below it"
  confidence: high
- id: typography_02
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "homepage product cards"
  tile_path: "store/ivyrx-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"
  claim: "The product cards keep labels readable, but the text hierarchy is shallow: category phrase, product name, and button label sit close in scale while the oversized vial render carries most of the emphasis."
  visible_tells:
    - "'Lose weight with' and 'GLP-1 Injections' are separated mainly by color and weight, not a large size step"
    - "The white 'Lose weight' button is visually heavier than the card copy"
    - "The cropped vial dominates the card more than the text block"
  confidence: medium
- id: typography_03
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "treatments product carousel"
  tile_path: "store/ivyrx-com/captures/2026-06-04/tiles/treatments/tile-01-y01220.png"
  claim: "Product names and prices are consistently placed at the card top-left, but the price tier is so small and light that the repeated cards read more as product thumbnails than shopping comparisons."
  visible_tells:
    - "Each card sets the product name large at top-left with the price directly beneath"
    - "Prices such as '$175' and '$155' are much smaller and grey"
    - "The card body is mostly empty gradient space until the vial and buttons"
  confidence: high
- id: typography_04
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "customer review carousel"
  tile_path: "store/ivyrx-com/captures/2026-06-04/tiles/homepage/tile-04-y04880.png"
  claim: "The testimonial cards make quotes highly legible, but author names and the verification pills are pushed into a faint footer tier that weakens card-level hierarchy."
  visible_tells:
    - "Large centered quote text takes most of each white card"
    - "Author names sit near the bottom in small grey type"
    - "'Verified Customers' appears in a small outlined pill below the author"
  confidence: high
- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: "homepage hero product grid"
  tile_path: "store/ivyrx-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"
  claim: "The hero product system is orderly: two wide feature cards sit above four smaller category cards, all sharing rounded corners, centered objects, and aligned pill controls."
  visible_tells:
    - "Two half-width feature cards form a matched row under the trust chips"
    - "Four smaller category cards align in a uniform row beneath"
    - "Rounded cards, centered vials, and pill buttons repeat across the whole grid"
  confidence: high
- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: "treatments category grid"
  tile_path: "store/ivyrx-com/captures/2026-06-04/tiles/treatments/tile-01-y01220.png"
  claim: "The treatment carousel keeps a disciplined card component: product name and price top-left, centered product render, paired CTAs, then a safety-information row at the same baseline."
  visible_tells:
    - "Every visible card uses the same top-left title and price placement"
    - "Dark 'Shop now' and white 'Learn more' buttons repeat at matched heights"
    - "The safety-information row anchors the bottom of each card"
  confidence: high
- id: layout_03
  family: layout_composition_components
  polarity: strong
  page_or_region: "PDP quality-tested section"
  tile_path: "store/ivyrx-com/captures/2026-06-04/tiles/pdp-glp1-personalized/tile-01-y01220.png"
  claim: "The testing module resolves into a clean two-by-two card grid with consistent padding, title/body alignment, and identical green status pills pinned to the upper-right of each card."
  visible_tells:
    - "Four white cards sit in a balanced two-column, two-row grid"
    - "Each card title starts from the same left inset"
    - "Each green 'Passed' pill is placed in the same upper-right position"
  confidence: high
- id: layout_04
  family: layout_composition_components
  polarity: mixed
  page_or_region: "homepage review carousel"
  tile_path: "store/ivyrx-com/captures/2026-06-04/tiles/homepage/tile-03-y03660.png"
  claim: "The video carousel gives the reviews strong vertical-card presence, but the fourth card is clipped at the viewport edge and the navigation arrows float below without tying clearly to the row."
  visible_tells:
    - "Three full portrait video cards are followed by a fourth card cropped at the right edge"
    - "The circular play buttons align over the video centers"
    - "Two small arrow buttons sit in whitespace below the row rather than inside the carousel frame"
  confidence: high
- id: layout_05
  family: layout_composition_components
  polarity: strong
  page_or_region: "PDP explanatory split section"
  tile_path: "store/ivyrx-com/captures/2026-06-04/tiles/pdp-glp1-personalized/tile-03-y03660.png"
  claim: "The GLP-1 explainer section uses a balanced two-column layout: icon-led benefit rows stack on the left while a large rounded lifestyle image anchors the right."
  visible_tells:
    - "Four benefit rows share one left edge and consistent icon boxes"
    - "The image column matches the text block's vertical footprint"
    - "The section leaves generous whitespace between columns without collision"
  confidence: high
- id: layout_06
  family: layout_composition_components
  polarity: mixed
  page_or_region: "PDP why-choose card grid"
  tile_path: "store/ivyrx-com/captures/2026-06-04/tiles/pdp-glp1-personalized/tile-04-y04880.png"
  claim: "The four reason cards are cleanly aligned, but the large white card areas are sparsely populated, leaving each icon and short paragraph floating in a lot of unused space."
  visible_tells:
    - "The grid uses two columns and two rows with matched card sizes"
    - "Small icons occupy only a tiny square near each card's upper-left"
    - "Each paragraph is short, leaving broad empty lower areas inside the cards"
  confidence: high
- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: "site-wide accent system"
  tile_path: "store/ivyrx-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"
  claim: "Green marks the weight-loss/product side while lavender and pink accents carry anti-aging and interface emphasis, creating a consistent soft-health palette."
  visible_tells:
    - "'Weight Loss' appears in green in the hero headline"
    - "The GLP-1 feature card uses a mint-green background and green vial"
    - "The NAD+ card uses a pale lavender background with a purple vial"
  confidence: high
  contrast_with: "store/ivyrx-com/captures/2026-06-04/tiles/anti-aging/tile-00-y00000.png"
- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: "product-card imagery"
  tile_path: "store/ivyrx-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"
  claim: "The cropped vial renders and pastel panels give the product cards an owned, pharmacy-meets-wellness image language rather than plain catalog thumbnails."
  visible_tells:
    - "Large GLP-1 vial is cropped off the bottom of the green feature card"
    - "Large purple vial is cropped similarly in the NAD+ feature card"
    - "Smaller category cards repeat the vial-on-soft-gradient treatment"
  confidence: high
- id: color_03
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "anti-aging category hero"
  tile_path: "store/ivyrx-com/captures/2026-06-04/tiles/anti-aging/tile-00-y00000.png"
  claim: "The anti-aging hero keeps the lavender product panel, but the adjacent dark gym photo introduces a colder, more generic fitness mood than the site's otherwise bright pastel system."
  visible_tells:
    - "A dark blue-black gym photo fills the left feature panel"
    - "The right feature panel returns to pale lavender with a purple vial"
    - "The dark photo sits inside the same rounded card rhythm as the soft product panel"
  confidence: high
- id: color_04
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "UGC video reviews"
  tile_path: "store/ivyrx-com/captures/2026-06-04/tiles/pdp-glp1-personalized/tile-02-y02440.png"
  claim: "The review videos add real human warmth, but their warm kitchens, cars, and selfie lighting visually break from the controlled white/pastel product environment around them."
  visible_tells:
    - "Portrait videos show different real-world backgrounds and lighting temperatures"
    - "Dark gradient overlays and play buttons unify the video cards only at the bottom"
    - "The surrounding section returns to white space and gradient headline text"
  confidence: high
- id: iconography_01
  family: iconography_illustration
  polarity: mixed
  page_or_region: "PDP hero trust badges"
  tile_path: "store/ivyrx-com/captures/2026-06-04/tiles/pdp-glp1-personalized/tile-00-y00000.png"
  claim: "The PDP hero layers three trust badges over the product photo, but the badges use unrelated visual languages, making them feel like imported seals rather than a native icon system."
  visible_tells:
    - "A circular USA seal, a green lab-tested badge, and a blue shield badge sit side by side"
    - "The badges are placed in a translucent brown strip over the vial image"
    - "Their shapes, colors, and line treatments do not match each other or the site's pastel UI icons"
  confidence: high
- id: iconography_02
  family: iconography_illustration
  polarity: mixed
  page_or_region: "process step illustrations"
  tile_path: "store/ivyrx-com/captures/2026-06-04/tiles/treatments/tile-01-y01220.png"
  claim: "The three process illustrations are custom and consistent, but their pale card-on-card treatment is so low-contrast that the icons read more as background texture than functional explanation."
  visible_tells:
    - "Each process card uses a soft pastel illustration above a 'Step' pill"
    - "The left and right illustration panels are faded almost to the white background"
    - "The small medical and shipping icons share pink/lavender accents"
  confidence: high
- id: iconography_03
  family: iconography_illustration
  polarity: mixed
  page_or_region: "PDP benefit list icons"
  tile_path: "store/ivyrx-com/captures/2026-06-04/tiles/pdp-glp1-personalized/tile-03-y03660.png"
  claim: "The benefit-list icons are consistent in size and container, but the line drawings are generic and thin, adding polish without much ownable character."
  visible_tells:
    - "Four identical rounded-square icon containers stack down the left column"
    - "Icons use the same pink/lavender stroke treatment"
    - "The glyphs are simple line symbols beside standard title/body rows"
  confidence: medium
- id: iconography_04
  family: iconography_illustration
  polarity: mixed
  page_or_region: "PDP why-choose cards"
  tile_path: "store/ivyrx-com/captures/2026-06-04/tiles/pdp-glp1-personalized/tile-04-y04880.png"
  claim: "The reason-card icons repeat the pastel line style, but each icon is tiny relative to the card and does little to differentiate the four benefits visually."
  visible_tells:
    - "Each card starts with a small pastel icon inside a faint rounded square"
    - "The icons are visually subordinate to the large blank card backgrounds"
    - "All four cards use the same scale and treatment despite different topics"
  confidence: high
```

## Provenance

Tiles read: homepage (8), treatments (9), weight-loss (7), anti-aging (7), and pdp-glp1-personalized (7) from `store/ivyrx-com/captures/2026-06-04/tiles/` - 38 active tiles total. QA gate found no modal, cookie wall, grey/blank hero, black media card, lazy-load gap, or mid-animation contamination in the cited cached tiles; no exclusions and no Tier-B re-render. Mined from the captured screenshots only; this is a point-in-time visual snapshot of the 2026-06-04 capture, and the live site can change.
