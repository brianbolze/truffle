---
schema_version: "1.0"
domain: alange-soehne.com
captured_at: 2026-06-16
source_capture: 2026-05-31
qa_status: exclusions-noted
---

## Visual & brand impression

A. Lange & Söhne reads as controlled heritage luxury. Its owned signatures: a near-black ground isolating warm gold watch hardware [color_01], catalogue shots floating on seamless white where material alone carries colour [color_02][iconography_04], and a bespoke engraving-illustration language — founder portraits, exploded movements, period etchings — anchoring Heritage [iconography_01][iconography_02][iconography_03]. Structure is disciplined: a strict three-column grid and recurring global modules [layout_01][layout_04][layout_05], with assertive flush-left display heros opening interior pages [typography_01][layout_03]. The weaknesses are finish-level, not foundational — the homepage hero headline shrinks to a caption [typography_02], the footer hierarchy goes flat [typography_05], stock-generic UI/social icons share no DNA with the craft [iconography_05], and repeated cool, ungraded documentation photos break the warm system [color_06][color_07].

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: "Interior page heros (Manufacture, Heritage)"
  tile_path: store/alange-soehne-com/captures/2026-05-31/tiles/manufacture/tile-00-y00000.png
  claim: "Interior pages open with a confident display-scale headline: a small italic eyebrow over an oversized all-caps page word ('MANUFACTURE'), giving a clear three-level entry with unambiguous reading order — the same treatment recurs on the Heritage hero."
  visible_tells:
  - "Small italic eyebrow ('Discover our brand, craftsmanship and heritage') sits visually separate above the oversized all-caps headline"
  - "Headline is roughly 4-5x the eyebrow size; on Heritage a single all-caps 'HERITAGE' dominates the upper third with no competing text"
  confidence: high
  contrast_with: store/alange-soehne-com/captures/2026-05-31/tiles/homepage/tile-00-y00000.png
- id: typography_02
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "Homepage — hero"
  tile_path: store/alange-soehne-com/captures/2026-05-31/tiles/homepage/tile-00-y00000.png
  claim: "The homepage hero headline ('Discover A. Lange & Söhne timepieces') sits in a small centred block below the watch image at a size barely above body text, reading as a caption rather than a commanding statement — the opposite of the assertive display heros used on interior pages."
  visible_tells:
  - "Headline sits below the image at a size only marginally larger than body text"
  - "Subline ('Crafted by Hand in Glashütte, Germany') is nearly the same size as the headline, compressing the hierarchy"
  confidence: high
  contrast_with: store/alange-soehne-com/captures/2026-05-31/tiles/manufacture/tile-00-y00000.png
- id: typography_03
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "Product grids (homepage novelties, all timepieces)"
  tile_path: store/alange-soehne-com/captures/2026-05-31/tiles/all-timepieces/tile-02-y02440.png
  claim: "The product label stack (reference number → all-caps model name → material → price) is consistent and orderly, but the weight/size step between the model name and the material line beneath it is subtle — at thumbnail scale the middle lines read as near-equal rank."
  visible_tells:
  - "Model name ('LITTLE LANGE 1', 'GRAND LANGE 1') is all-caps but only slightly larger than the material descriptor below"
  - "Reference number and price lines sit close in visual weight to the material line, flattening the stack"
  confidence: medium
  contrast_with: store/alange-soehne-com/captures/2026-05-31/tiles/homepage/tile-01-y01220.png
- id: typography_04
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "Manufacture page — editorial body sections"
  tile_path: store/alange-soehne-com/captures/2026-05-31/tiles/manufacture/tile-01-y01220.png
  claim: "Long-form body copy is set as dense centred prose blocks with no drop cap, pull quote, or sub-landmark to break the column — secondary hierarchy within the text is absent, slowing the scan."
  visible_tells:
  - "Multiple consecutive body paragraphs fill the column with no visual interruption"
  - "Section heading 'The art of watchmaking' appears only at the bottom of the tile; the body above carries no sub-heading"
  confidence: medium
- id: typography_05
  family: typography_hierarchy
  polarity: poor
  page_or_region: "Homepage — footer"
  tile_path: store/alange-soehne-com/captures/2026-05-31/tiles/homepage/tile-05-y05714.png
  claim: "The four-column footer renders column headers and link items at near-identical small weight/size, so hierarchy within the footer is essentially flat; the legal/meta row runs as undifferentiated tiny type with no separator from the nav columns above."
  visible_tells:
  - "Column headers ('FAMILIES', 'CONTACT', 'COMPANY', 'SERVICES') are only marginally heavier than the links beneath them"
  - "Imprint/Privacy legal row is a full-width run of tiny type with no visual break from the navigation block"
  confidence: high
- id: typography_06
  family: typography_hierarchy
  polarity: poor
  page_or_region: "All timepieces — page header / filter bar"
  tile_path: store/alange-soehne-com/captures/2026-05-31/tiles/all-timepieces/tile-00-y00000.png
  claim: "The 'All timepieces' page heading is only modestly larger than the filter-bar controls ('Filters', 'BY WATCH FAMILY', 'Available online') and the result count beneath it, collapsing page title, UI chrome, and metadata into three near-equal levels."
  visible_tells:
  - "Page title and filter button labels sit at similar vertical scale"
  - "'96 results found' appears in an even smaller size immediately below, creating three close levels in a tight band"
  confidence: high
- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: "Product grids (all timepieces catalog, homepage novelties)"
  tile_path: store/alange-soehne-com/captures/2026-05-31/tiles/all-timepieces/tile-01-y01220.png
  claim: "The product grid holds a strict 3-column cadence with even gutters and shared label baselines across long scroll lengths, with no column-width drift or vertical jitter — the same disciplined grid governs the centred homepage novelties row."
  visible_tells:
  - "Watch images sit at identical horizontal intervals with equal-width gutters on both sides of the centre column"
  - "Label blocks (reference, name, material, price, CTA) align to a shared baseline beneath each image across columns"
  confidence: high
  contrast_with: store/alange-soehne-com/captures/2026-05-31/tiles/homepage/tile-01-y01220.png
- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: "Homepage — hero"
  tile_path: store/alange-soehne-com/captures/2026-05-31/tiles/homepage/tile-00-y00000.png
  claim: "The homepage hero gives the full viewport to a single macro watch image with no copy or badge overlaid; all text and two CTAs are stacked in a clean centred block below, keeping image and message cleanly separated."
  visible_tells:
  - "Watch macro fills the frame with no overlaid headline or badge"
  - "Centred text block and two button-level CTAs sit below in clear separation from the image"
  confidence: high
- id: layout_03
  family: layout_composition_components
  polarity: strong
  page_or_region: "Manufacture — hero"
  tile_path: store/alange-soehne-com/captures/2026-05-31/tiles/manufacture/tile-00-y00000.png
  claim: "Interior pages open with a full-bleed editorial photograph running edge-to-edge under a floating nav, with the page title set flush-left at display size over the bleed — a deliberate section-entry composition."
  visible_tells:
  - "'MANUFACTURE' sits at display weight flush to the left margin over the full-width hands-and-movement photo"
  - "Nav floats above the photo with no content rail interrupting the bleed"
  confidence: high
- id: layout_04
  family: layout_composition_components
  polarity: strong
  page_or_region: "Shared 3-column editorial card component (homepage, manufacture)"
  tile_path: store/alange-soehne-com/captures/2026-05-31/tiles/manufacture/tile-02-y02440.png
  claim: "A 3-column editorial card component — equal-width image, title, body, 'Read more >' link — recurs with matching image proportions, gutters, and label alignment on both the homepage 'art of watchmaking' row and the Manufacture page, evidencing a genuine shared component system rather than one-off styling."
  visible_tells:
  - "Card image heights, gutter widths, and label top-margins match across the two pages"
  - "Each card's 'Read more >' link sits at the same vertical position below the body copy"
  confidence: high
  contrast_with: store/alange-soehne-com/captures/2026-05-31/tiles/homepage/tile-02-y02440.png
- id: layout_05
  family: layout_composition_components
  polarity: strong
  page_or_region: "Global dark newsletter band (homepage, manufacture, heritage)"
  tile_path: store/alange-soehne-com/captures/2026-05-31/tiles/homepage/tile-04-y04880.png
  claim: "A dark-ground newsletter band with left-aligned white headline and a warm-lit watch shot to the right appears with identical composition across homepage, manufacture, and heritage — a fixed global module."
  visible_tells:
  - "Same near-black band, same headline placement, same watch image right of text across pages"
  - "'SUBSCRIBE >' CTA uses identical small-caps + arrow treatment in each instance"
  confidence: high
  contrast_with: store/alange-soehne-com/captures/2026-05-31/tiles/manufacture/tile-06-y07320.png
- id: layout_06
  family: layout_composition_components
  polarity: strong
  page_or_region: "Global 'How may we further assist you?' module"
  tile_path: store/alange-soehne-com/captures/2026-05-31/tiles/homepage/tile-04-y04880.png
  claim: "A centred 'How may we further assist you?' section — centred headline, single outlined button, bounded boutique-interior photo — recurs at consistent proportions and the same position above the footer across homepage, manufacture, and heritage."
  visible_tells:
  - "Centred headline, centred outlined CTA, and bounded boutique photo use identical proportions across pages"
  - "Section sits at the same distance above the site footer in each instance"
  confidence: high
  contrast_with: store/alange-soehne-com/captures/2026-05-31/tiles/manufacture/tile-07-y08540.png
- id: layout_07
  family: layout_composition_components
  polarity: strong
  page_or_region: "Heritage — hero composition"
  tile_path: store/alange-soehne-com/captures/2026-05-31/tiles/heritage/tile-00-y00000.png
  claim: "The Heritage hero is a multi-layer illustrative composition — an engraved portrait overlaid on schematic exploded-movement drawings — floating on white with no card frame, a distinctly non-photographic art-direction choice for a hero."
  visible_tells:
  - "Line-art watchmaker portrait spans much of the viewport alongside exploded gear-train diagrams"
  - "No bounding box or frame; the illustration floats on a white field, giving depth without photography"
  confidence: high
- id: layout_08
  family: layout_composition_components
  polarity: mixed
  page_or_region: "Heritage — asymmetric image/text split"
  tile_path: store/alange-soehne-com/captures/2026-05-31/tiles/heritage/tile-01-y01220.png
  claim: "Heritage history sections use a large-image-left / narrow-text-right split where the image dominates (~55% width) and the text column is left at a thin measure that feels undersized relative to its narrative weight."
  visible_tells:
  - "Large pocket-watch photograph occupies roughly the left half-plus of the row"
  - "Right-hand body column is narrow enough that the running copy reads visually thin"
  confidence: medium
- id: layout_09
  family: layout_composition_components
  polarity: mixed
  page_or_region: "Heritage — 3-column topic cards (mixed image sources)"
  tile_path: store/alange-soehne-com/captures/2026-05-31/tiles/heritage/tile-04-y04880.png
  claim: "The 3-column card module is structurally consistent but mixes incompatible image sources within a single row — an atmospheric enamel-dial product shot, a bright ambient press-event photo, and a greyscale portrait illustration — sitting raw in the same shell with no framing or tonal treatment to bridge them."
  visible_tells:
  - "Three cards share identical margins yet show a dark constellation dial, a brightly-lit audience photo, and a greyscale illustrated portrait"
  - "No tonal grade or frame reconciles the differing image registers"
  confidence: medium
- id: layout_10
  family: layout_composition_components
  polarity: poor
  page_or_region: "Manufacture — interstitial bounded images (watchmaker, Company)"
  tile_path: store/alange-soehne-com/captures/2026-05-31/tiles/manufacture/tile-04-y04880.png
  claim: "Editorial images on the Manufacture page (watchmaker-at-bench, the 'Company' building shot) are bounded inside the narrower text column rather than given full-bleed or any structural status, repeating the same interstitial pattern between prose blocks with no compositional variation between sections."
  visible_tells:
  - "The 'Company' photo is clearly narrower than a full-bleed treatment, matching the earlier in-column watchmaker image"
  - "Prose above and below shares the image's column width, so the image breaks density but reads as filler, not a designed moment"
  confidence: medium
  contrast_with: store/alange-soehne-com/captures/2026-05-31/tiles/manufacture/tile-01-y01220.png
- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: "Dark hero + dark newsletter band (homepage)"
  tile_path: store/alange-soehne-com/captures/2026-05-31/tiles/homepage/tile-00-y00000.png
  claim: "The brand's dark mode is a disciplined two-tone system: a near-black ground isolating warm yellow/bronze-gold watch hardware as the only saturated colour, repeated identically in the hero and the dark newsletter band — confirming it as a deliberate palette, not a one-off hero choice."
  visible_tells:
  - "Deep charcoal/near-black field fills both the hero and the newsletter band"
  - "Yellow/bronze-gold case metal reads as the sole warm accent; white type is the only other element, no competing UI colour"
  confidence: high
  contrast_with: store/alange-soehne-com/captures/2026-05-31/tiles/homepage/tile-04-y04880.png
- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: "All timepieces — product grid"
  tile_path: store/alange-soehne-com/captures/2026-05-31/tiles/all-timepieces/tile-01-y01220.png
  claim: "Across a large multi-SKU grid, watches are shot on pure white with no props, and metal/dial/strap variety (white gold, platinum, pink gold; slate, blue, black dials) carries all the colour — no UI badges, price chips, or promotional callouts intrude, letting material be the only differentiator."
  visible_tells:
  - "Watches float on identical seamless white grounds with soft, directionally consistent shadows"
  - "Even the boldest accent (blue dial + blue strap) is product-sourced; no coloured badge or callout appears anywhere in the grid"
  confidence: high
  contrast_with: store/alange-soehne-com/captures/2026-05-31/tiles/all-timepieces/tile-00-y00000.png
- id: color_03
  family: color_brand_imagery
  polarity: strong
  page_or_region: "Manufacture — macro movement photography"
  tile_path: store/alange-soehne-com/captures/2026-05-31/tiles/manufacture/tile-02-y02440.png
  claim: "The three-across movement macros share a coherent warm close-up style — rubies, gold chatons, blued screws, and polished plates under consistent warm raking light — forming an owned visual vocabulary for the craft story."
  visible_tells:
  - "Left card: ruby jewels and blued screws over polished gold plates in warm ambient light"
  - "Centre and right cards repeat the gold/warm palette and raking light, including a tweezers-and-hands setting shot"
  confidence: high
- id: color_04
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "Homepage — editorial news cards"
  tile_path: store/alange-soehne-com/captures/2026-05-31/tiles/homepage/tile-03-y03660.png
  claim: "News-card photography is selected to hold a consistently dark, ambient-lit aesthetic — none of the three cards uses bright daylight or colourful event imagery — sustaining the dark/warm palette into editorial content."
  visible_tells:
  - "Left card: macro dial on near-black ground with a green accent light"
  - "Centre card: dark leather car interior with watch at wrist; right card: dark dramatic product composite"
  confidence: medium
- id: color_05
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "Heritage — contemporary portrait photography"
  tile_path: store/alange-soehne-com/captures/2026-05-31/tiles/heritage/tile-02-y02440.png
  claim: "A contemporary colour portrait of a company figure uses a cool, flat available-light style that does not share the warm or engraving aesthetic of the surrounding heritage imagery — workable but not fully unified."
  visible_tells:
  - "Large colour portrait of a grey-haired man in a blue shirt under soft, cool window/studio light"
  - "Sits directly beside warm pink-gold pocket-watch photography, a noticeably cooler and more journalistic register"
  confidence: medium
  contrast_with: store/alange-soehne-com/captures/2026-05-31/tiles/heritage/tile-00-y00000.png
- id: color_06
  family: color_brand_imagery
  polarity: poor
  page_or_region: "Manufacture — outdoor event photograph"
  tile_path: store/alange-soehne-com/captures/2026-05-31/tiles/manufacture/tile-05-y06100.png
  claim: "The wide outdoor event photograph — a garden gathering with tents and cars — is ungraded generic PR imagery: no product, no branded colour, no lighting treatment connecting it to the dark/gold system; it could belong to any event sponsor."
  visible_tells:
  - "Wide shot of a green lawn with white tents, cars, and casual crowds"
  - "Standard daylight exposure with no grade and nothing product- or brand-specific in frame"
  confidence: high
  contrast_with: store/alange-soehne-com/captures/2026-05-31/tiles/homepage/tile-00-y00000.png
- id: color_07
  family: color_brand_imagery
  polarity: poor
  page_or_region: "Repeated boutique-interior / building shots (homepage, manufacture, heritage)"
  tile_path: store/alange-soehne-com/captures/2026-05-31/tiles/homepage/tile-05-y05714.png
  claim: "The same cool, daylit boutique-interior photograph recurs pixel-identically across homepage, manufacture, and heritage as the assist-section image, and the building-exterior shot is similarly ungraded — undistinctive documentation imagery that breaks the warm controlled tonality of the product/craft photography."
  visible_tells:
  - "Glass-partitioned retail space with a small table and flowers, cool daylight, no product spotlighting, repeated identically across pages"
  - "Companion building-exterior shot is overcast standard architecture with no distinctive grade"
  confidence: high
  contrast_with: store/alange-soehne-com/captures/2026-05-31/tiles/manufacture/tile-02-y02440.png
- id: iconography_01
  family: iconography_illustration
  polarity: strong
  page_or_region: "Heritage hero — bespoke line-art illustration"
  tile_path: store/alange-soehne-com/captures/2026-05-31/tiles/heritage/tile-00-y00000.png
  claim: "The Heritage hero is a bespoke engraving-style line illustration — a stipple-and-contour portrait integrated with exploded movement diagrams at matching stroke weight — clearly commissioned for the brand, not a stock asset, establishing an owned image language."
  visible_tells:
  - "Portrait cross-hatching and the gear-train / balance-wheel diagrams are drawn at the same fine stroke weight, indicating a single illustrative hand"
  - "Full white field with grey line engraving and zero photography in the hero"
  confidence: high
- id: iconography_02
  family: iconography_illustration
  polarity: strong
  page_or_region: "Heritage — historical founder portrait illustrations"
  tile_path: store/alange-soehne-com/captures/2026-05-31/tiles/heritage/tile-03-y03660.png
  claim: "Historical founders are rendered as hand-drawn engraving-style portraits rather than period photographs, using consistent cross-hatching and even ink weight across multiple pairs — a cohesive illustration system, not a one-off."
  visible_tells:
  - "Two oval-format engraved portraits (Richard and Emil Lange) with matched cross-hatching and ink weight"
  - "A second portrait pair lower in the tile uses the identical technique"
  confidence: high
- id: iconography_03
  family: iconography_illustration
  polarity: strong
  page_or_region: "Heritage — period archival engravings as editorial imagery"
  tile_path: store/alange-soehne-com/captures/2026-05-31/tiles/heritage/tile-05-y06100.png
  claim: "Period-style archival engravings (a Dresden architectural etching, a woodcut-style allegorical scene) are deployed at the same card scale as photographs, deliberately extending the engraving vocabulary into the editorial layer and reinforcing the historical positioning."
  visible_tells:
  - "One card shows a classical allegorical engraving ('Saxony before watchmaking'), a woodcut-style composition, not a photo"
  - "An adjacent card uses an architectural etching of Dresden buildings at the same scale as the photographic cards"
  confidence: high
  contrast_with: store/alange-soehne-com/captures/2026-05-31/tiles/heritage/tile-04-y04880.png
- id: iconography_04
  family: iconography_illustration
  polarity: strong
  page_or_region: "All timepieces — product photography system"
  tile_path: store/alange-soehne-com/captures/2026-05-31/tiles/all-timepieces/tile-00-y00000.png
  claim: "Catalog renders are shot against a pure white ground at a consistent 3/4 angle with uniform lighting and high fidelity, forming a disciplined product-photography system rather than ad-hoc shots."
  visible_tells:
  - "Top-row watches share identical cropping, angle, and white-ground treatment with no shadow-gradient variation"
  - "Strap texture, case edges, and dial detail resolve cleanly at thumbnail size"
  confidence: high
- id: iconography_05
  family: iconography_illustration
  polarity: mixed
  page_or_region: "Nav and footer UI/social icons (homepage)"
  tile_path: store/alange-soehne-com/captures/2026-05-31/tiles/homepage/tile-05-y05714.png
  claim: "Footer social glyphs and nav utility icons (search, wishlist, bag) are standard platform/thin-line glyphs with no restyling or weight adaptation — functional but generic, sharing no visual DNA with the brand's bespoke engraving language."
  visible_tells:
  - "Row of social icons in the footer uses recognizable platform-standard glyphs at small size"
  - "Nav cluster shows a magnifier, heart, and bag in an interchangeable thin-stroke style"
  confidence: high
  contrast_with: store/alange-soehne-com/captures/2026-05-31/tiles/heritage/tile-00-y00000.png
- id: iconography_06
  family: iconography_illustration
  polarity: poor
  page_or_region: "Manufacture — three editorial cards (purely photographic)"
  tile_path: store/alange-soehne-com/captures/2026-05-31/tiles/manufacture/tile-02-y02440.png
  claim: "The Manufacture three-up editorial strip uses straight macro photography with no diagram, icon, or graphic treatment — none of the gear-diagram or engraving language present elsewhere is carried into this functional section."
  visible_tells:
  - "Three equal-width photographic cards with captions and no illustrative or graphic element"
  - "No attempt to extend the heritage engraving / diagram vocabulary into the section"
  confidence: high
  contrast_with: store/alange-soehne-com/captures/2026-05-31/tiles/heritage/tile-00-y00000.png
```

## Provenance

Tiles read: homepage (6) + all-timepieces (9, tiles 00–08) + manufacture (9) + heritage (8) = 32 active, from `captures/2026-05-31/tiles/`. **Exclusions:** all-timepieces tiles 09–21 (13) — lazy-load gap; the cached Firecrawl payload fired its screenshot before the lower catalogue's product images loaded, leaving text-only cards (unusable as imagery evidence). The loaded top rows (00–08) carry the grid / card / product-photography evidence. **Tier-B:** attempted on the homepage (system Chrome via `shoot.py`, both faithful and `--dismiss`), but the live load throws a scroll-locking overlay that `--dismiss` could not clear — scroll stayed locked, the hero rendered as a black block, tiles came back mislabeled (the `scroll_locked` WARNING fired on both runs). The cached Tier-A homepage was cleaner (hero visible under a thin region-notice strip), so it is what's mined here and **no Tier-B tiles ship**. Mined blind + judged per [`/visual-evidence`](../../skills/visual-evidence/SKILL.md): four family miners saw only the tiles (no dossier, no web), the judge pruned 46 raw cards to 29 (mostly cross-family duplicate tells merged). Every `poor` card was spot-checked against its native tile — all are genuine design tells, no capture artifacts. Snapshot caveat: reflects the 2026-05-31 capture; the live site changes.
