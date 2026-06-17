---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.0"
domain: kingsbergmedical.com
captured_at: 2026-06-17
source_capture: 2026-06-17
qa_status: exclusions-noted
---

## Visual & brand impression

Kingsberg reads like an older medical SEO site: a mountain-plus-doctors hero, heavy serif headers, and strong green CTAs give it immediate clinic intent, but the type hierarchy and nav feel dated [layout_01][typography_01]. The catalog and lab pages are functional but crowded, with sidebar ads, oversized buttons, and table-heavy content competing for attention [layout_02][layout_03]. The palette is consistent green-and-white, yet one-note and occasionally broken by ad-style lime/blue graphics [color_01][color_02]. Imagery leans on stock doctors, lab photos, product cutouts, and numbered badges rather than a distinctive system [iconography_01][iconography_02].

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "homepage hero"
  tile_path: "store/kingsbergmedical-com/captures/2026-06-17/tiles/homepage/tile-00-y00000.png"
  claim: "The first viewport has a clear hierarchy, but it relies on older serif display type, uppercase nav, and a large slogan block rather than a modern clinical typography system."
  visible_tells:
    - "Hero headline sits in a dark translucent box over the mountain image in large white serif type."
    - "Top navigation is bold uppercase sans text while the logo and headline use a different serif/brand treatment."
    - "The pale-green slogan band uses large centered green serif text that repeats the clinical value prop."
  confidence: high
- id: typography_02
  family: typography_hierarchy
  polarity: poor
  page_or_region: "hormone testing article teasers"
  tile_path: "store/kingsbergmedical-com/captures/2026-06-17/tiles/hormone_testing/tile-10-y12200.png"
  claim: "Article teaser headings use oversized underlined green link styling that dominates the page and makes the lower content feel like an SEO archive."
  visible_tells:
    - "Multiple teaser headlines appear in large green underlined serif text."
    - "Each teaser repeats a small thumbnail, green headline, short gray excerpt, and green 'READ MORE' link."
    - "The headings visually outweigh the surrounding body copy and CTA banner."
  confidence: high
- id: layout_01
  family: layout_composition_components
  polarity: mixed
  page_or_region: "homepage first viewport"
  tile_path: "store/kingsbergmedical-com/captures/2026-06-17/tiles/homepage/tile-00-y00000.png"
  claim: "The hero quickly communicates clinic category and primary action, but the header, phone bar, logo strip, doctors, mountains, headline box, and CTA are layered into a busy composition."
  visible_tells:
    - "A full-width mountain hero carries two doctor cutouts, a dark copy box, and a large green button."
    - "A separate dark top bar, translucent logo/nav band, and hero image stack above the first content band."
    - "The first visible content section begins before the hero has visually settled, adding more doctor stock imagery."
  confidence: high
- id: layout_02
  family: layout_composition_components
  polarity: poor
  page_or_region: "product index grid and sidebar"
  tile_path: "store/kingsbergmedical-com/captures/2026-06-17/tiles/product_index/tile-01-y01220.png"
  claim: "The product index mixes catalog cards, a blog sidebar, and a large vertical ad in one scan path, making product comparison visually noisy."
  visible_tells:
    - "The main column shows product cards in two columns while the right rail carries 'Top Stories' and a tall blood-test ad."
    - "Green 'View Product' buttons are wider and heavier than the product names beneath the images."
    - "Product imagery varies between isolated vials, pens, and stock lab photos with large uneven whitespace around the cards."
  confidence: high
- id: layout_03
  family: layout_composition_components
  polarity: poor
  page_or_region: "hormone testing tables"
  tile_path: "store/kingsbergmedical-com/captures/2026-06-17/tiles/hormone_testing/tile-02-y02440.png"
  claim: "The lab-panel content is data-heavy but presented as long centered tables in a narrow column, so scanning requires sustained vertical work."
  visible_tells:
    - "Two-column tables fill the center of the page with alternating gray rows and thick borders."
    - "A separate right-rail ad remains visible while the table content extends vertically."
    - "Large section headings repeat between tables instead of using a compact comparison layout."
  confidence: high
- id: color_01
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "semaglutide PDP"
  tile_path: "store/kingsbergmedical-com/captures/2026-06-17/tiles/semaglutide/tile-00-y00000.png"
  claim: "The site uses a consistent green-and-white brand system across nav, breadcrumbs, tabs, links, and CTAs, but the palette stays mostly in one hue family."
  visible_tells:
    - "Header bar, breadcrumb strip, active tab, text links, and CTA color all use similar greens."
    - "The PDP content area is mostly white, with green as the only strong accent."
    - "The same mountain/doctor hero repeats above the product content."
  confidence: high
- id: color_02
  family: color_brand_imagery
  polarity: poor
  page_or_region: "product index sidebar advertising"
  tile_path: "store/kingsbergmedical-com/captures/2026-06-17/tiles/product_index/tile-01-y01220.png"
  claim: "The sidebar ad breaks the otherwise muted green/white system with a brighter promo palette and billboard-style treatment."
  visible_tells:
    - "The tall 'Schedule Your Blood Test' ad uses bright lime green, yellow, and blue."
    - "The ad has curved graphic shapes and oversized promotional type unlike the product grid."
    - "It sits directly beside the catalog cards and competes with their green CTA buttons."
  confidence: high
- id: iconography_01
  family: iconography_illustration
  polarity: mixed
  page_or_region: "product index CTAs"
  tile_path: "store/kingsbergmedical-com/captures/2026-06-17/tiles/product_index/tile-00-y00000.png"
  claim: "The catalog buttons use a consistent eye icon cue, but the iconography is generic and does not build a differentiated product language."
  visible_tells:
    - "Every visible product card repeats a green 'View Product' button with a small eye icon."
    - "The icon is a simple functional cue rather than a custom medical or brand motif."
    - "Product-card imagery changes style from isolated vial render to stock lab photo."
  confidence: high
- id: iconography_02
  family: iconography_illustration
  polarity: poor
  page_or_region: "homepage process steps"
  tile_path: "store/kingsbergmedical-com/captures/2026-06-17/tiles/homepage/tile-02-y02440.png"
  claim: "The process section uses dated numbered badges with shadows, which reads more like a stock template than a tailored healthcare interface."
  visible_tells:
    - "Three large green circular badges contain the numbers 1, 2, and 3."
    - "Each badge has a bevel/drop-shadow effect and sits above a short process label."
    - "The badges are visually disconnected from the surrounding pale-green benefit content."
  confidence: high
```

## Provenance

- **Tiles read:** Tier-A cached tiles from `store/kingsbergmedical-com/captures/2026-06-17/tiles/` for homepage, product_index, semaglutide, sermorelin, and hormone_testing.
- **Exclusions:** `store/kingsbergmedical-com/captures/2026-06-17/tiles/homepage/tile-03-y03660.png` excluded because the medication carousel region rendered as a large blank dark-green band; treated as capture/lazy-load contamination, not design evidence.
- **Tier-B:** Not used. The remaining cached tiles were clear enough for falsifiable visual evidence.
- **Snapshot caveat:** This is a point-in-time visual read from the captured desktop screenshots; live carousel/media behavior may differ.
