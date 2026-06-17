---
schema_version: "1.0"
domain: tryshed.com
captured_at: 2026-06-17
source_capture: 2026-06-04
qa_status: clean
---

# Shed Rx - visual evidence

## Visual & brand impression

Shed reads as a polished wellness commerce system: large editorial serif type, green/cream surfaces, black CTAs, and pharmaceutical product renders give the core weight-loss and longevity pages a controlled, premium feel [typography_01][color_01][color_02]. The strongest execution is the reusable grid grammar - product cards, PDP splits, app bands, and calculator/table modules hold together across pages [layout_01][layout_02][layout_03][iconography_01]. The softness comes where performance-marketing material enters: testimonial rails, before/after photos, Trustpilot/play widgets, and the thin press page feel more assembled than art-directed [layout_05][color_04][iconography_05][layout_06]. The footer is also heavy: a giant wordmark and dense link columns overpower tiny legal text [typography_06][layout_07].

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: "homepage hero"
  tile_path: "store/tryshed-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"
  claim: "The homepage opens with a confident serif display headline at true hero scale, using the green second line as emphasis while keeping the member-count proof point and CTA/product grid clearly subordinate."
  visible_tells:
    - "The headline 'Sustainable wellness, made simple' occupies the dominant left column, with 'made simple' in green and the rest in charcoal."
    - "The smaller 'Trusted by over 150,000 members nationwide' line and the product cards below are visibly separate hierarchy levels."
  confidence: high
- id: typography_02
  family: typography_hierarchy
  polarity: strong
  page_or_region: "weight-loss and longevity category heroes"
  tile_path: "store/tryshed-com/captures/2026-06-04/tiles/weight_loss/tile-00-y00000.png"
  claim: "Category pages use a restrained centered hero hierarchy: a large green serif headline, one smaller explanatory line, and two compact CTAs, leaving the product grid to carry the next read."
  visible_tells:
    - "The weight-loss hero headline spans the center in green serif type, with a much smaller paragraph beneath."
    - "Two black rounded CTAs sit below the copy, separated from the product cards by a clear white band."
  confidence: high
  contrast_with: "store/tryshed-com/captures/2026-06-04/tiles/longevity/tile-00-y00000.png"
- id: typography_03
  family: typography_hierarchy
  polarity: strong
  page_or_region: "PDP hero"
  tile_path: "store/tryshed-com/captures/2026-06-04/tiles/semaglutide/tile-00-y00000.png"
  claim: "The PDP hero sets product name, explanatory copy, feature bullets, pricing table, CTA, and FAQ rows into a readable sequence without losing the product title as the primary stop."
  visible_tells:
    - "The 'Compounded Semaglutide Injections' headline is the largest type in the purchase column."
    - "Feature bullets, table cells, CTA, and accordion rows descend in smaller, repeated text sizes."
  confidence: high
- id: typography_04
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "product-card benefit copy"
  tile_path: "store/tryshed-com/captures/2026-06-04/tiles/weight_loss/tile-00-y00000.png"
  claim: "Product cards preserve title and price hierarchy, but dense benefit bullets push several cards toward catalog readability rather than premium editorial spacing."
  visible_tells:
    - "Each card has a bold product name, a smaller subtitle, a bold starting price, and a benefit list stacked closely beneath."
    - "The lower Wegovy and Zepbound cards show multiple bullet lines compressed into the lower card area."
  confidence: medium
- id: typography_05
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "testimonial and proof sections"
  tile_path: "store/tryshed-com/captures/2026-06-04/tiles/mens_hair/tile-01-y01220.png"
  claim: "Social-proof headings combine third-party logo marks, numeric proof, serif headlines, video labels, and quote cards, making the type system busier than the calmer product sections."
  visible_tells:
    - "The section starts with a Trustpilot wordmark, green stars, '4.5', then a large serif headline and a sans-serif subhead."
    - "Below, testimonial cards mix before/after labels, video title text, star icons, and quote text in one viewport."
  confidence: high
- id: typography_06
  family: typography_hierarchy
  polarity: poor
  page_or_region: "footer and legal text"
  tile_path: "store/tryshed-com/captures/2026-06-04/tiles/semaglutide/tile-05-y05387.png"
  claim: "The footer hierarchy is overpowered by a giant SHED wordmark while dense product link columns and pale legal text fight for legibility below the content."
  visible_tells:
    - "The oversized SHED wordmark fills the lower-left footer area and dwarfs the adjacent link columns."
    - "Small grey legal copy above the footer and tiny copyright/legal links sit at much lower contrast than the main footer mark."
  confidence: high

- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: "homepage product grid"
  tile_path: "store/tryshed-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"
  claim: "The homepage product entry point uses a clear modular grid: two large hero cards above three smaller category cards, all with shared radii, image treatment, and CTA placement."
  visible_tells:
    - "The GLP-1 and NAD+ cards form a two-column row with matched height, rounded corners, and black CTAs along the lower edge."
    - "Three smaller category cards below reuse the same rounded image-card language and right-side arrow affordance."
  confidence: high
- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: "category product cards"
  tile_path: "store/tryshed-com/captures/2026-06-04/tiles/longevity/tile-00-y00000.png"
  claim: "The category product grid is a disciplined two-column component system with repeated image/text split cards, consistent gutters, and aligned CTA bars."
  visible_tells:
    - "Longevity cards repeat the same left-image/right-copy structure in two equal columns."
    - "CTA bars line up along the bottom of the visible cards, and card gutters remain even across the grid."
  confidence: high
  contrast_with: "store/tryshed-com/captures/2026-06-04/tiles/weight_loss/tile-00-y00000.png"
- id: layout_03
  family: layout_composition_components
  polarity: strong
  page_or_region: "PDP split layout"
  tile_path: "store/tryshed-com/captures/2026-06-04/tiles/foundayo/tile-00-y00000.png"
  claim: "PDP pages use a stable split-screen commerce layout: oversized product imagery on the left, feature chips and purchase/FAQ controls on the right, then logos and proof beneath."
  visible_tells:
    - "Foundayo's product image occupies the left half while the name, price, chips, explanatory copy, CTA, and FAQ rows sit in a single right column."
    - "A press-logo row starts beneath the hero, preserving the top split before the next proof section."
  confidence: high
  contrast_with: "store/tryshed-com/captures/2026-06-04/tiles/semaglutide/tile-00-y00000.png"
- id: layout_04
  family: layout_composition_components
  polarity: strong
  page_or_region: "app support band"
  tile_path: "store/tryshed-com/captures/2026-06-04/tiles/semaglutide/tile-03-y03660.png"
  claim: "The Pivot app band is cleanly composed, with left-aligned copy and CTA balanced by a large phone mockup on a pale green field."
  visible_tells:
    - "Text, badge, and black CTA form a simple left column with generous whitespace."
    - "The phone mockup is isolated on the right and fades at the bottom without crowding the following team section."
  confidence: high
- id: layout_05
  family: layout_composition_components
  polarity: mixed
  page_or_region: "four-step wellness plan"
  tile_path: "store/tryshed-com/captures/2026-06-04/tiles/homepage/tile-02-y02440.png"
  claim: "The four-step module has solid grid discipline, but the imagery inside the cards jumps across registers, making the row feel assembled from different sources."
  visible_tells:
    - "Four equal cards share a top step pill, centered title, centered body copy, image area, and a shared baseline."
    - "The visuals shift from phone mockup to provider portrait to package handoff to laptop stock image within the same row."
  confidence: high
- id: layout_06
  family: layout_composition_components
  polarity: mixed
  page_or_region: "testimonial rails"
  tile_path: "store/tryshed-com/captures/2026-06-04/tiles/foundayo/tile-02-y02440.png"
  claim: "The testimonial carousel creates quick social-proof density, but edge cards are visibly clipped and the row reads more like a horizontal feed than a composed editorial section."
  visible_tells:
    - "The first testimonial card is cut off at the left edge while five cards continue across the row."
    - "Before/after thumbnail pairs, member pills, names, and quotes repeat in a long rail under the star headline."
  confidence: high
  contrast_with: "store/tryshed-com/captures/2026-06-04/tiles/homepage/tile-01-y01220.png"
- id: layout_07
  family: layout_composition_components
  polarity: poor
  page_or_region: "press page"
  tile_path: "store/tryshed-com/captures/2026-06-04/tiles/press/tile-00-y00000.png"
  claim: "The press page collapses to a single plain article row above the global footer, with little visual structure beyond text width and a divider."
  visible_tells:
    - "One headline, date, paragraph, and blue 'Read more' link occupy the main content area."
    - "The footer begins immediately below a thin divider, with no cards, imagery, or press-list system in between."
  confidence: high

- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: "homepage and core weight-loss palette"
  tile_path: "store/tryshed-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"
  claim: "The core palette is controlled: dark green pharmaceutical imagery, pale cream/green surfaces, black CTAs, and tan accent buttons repeat without turning the first viewport chaotic."
  visible_tells:
    - "The GLP-1 card uses deep green packaging and a black CTA; the NAD+ card uses pale blue-green and the same black CTA."
    - "The header's tan 'Start today' button and pale green feature chips sit within the same restrained neutral system."
  confidence: high
- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: "product renders and packaging"
  tile_path: "store/tryshed-com/captures/2026-06-04/tiles/semaglutide/tile-00-y00000.png"
  claim: "Vials and packaged products are staged as polished, brand-owned commerce assets, using oversized isolated product renders on controlled color fields."
  visible_tells:
    - "The semaglutide vial fills a large dark green product stage with matching thumbnail treatments below."
    - "The same teal/green cap and label language recurs across the homepage GLP-1 card and longevity product grid."
  confidence: high
  contrast_with: "store/tryshed-com/captures/2026-06-04/tiles/longevity/tile-00-y00000.png"
- id: color_03
  family: color_brand_imagery
  polarity: strong
  page_or_region: "longevity editorial imagery"
  tile_path: "store/tryshed-com/captures/2026-06-04/tiles/longevity/tile-02-y02440.png"
  claim: "The longevity page extends the clinical/wellness palette with soft blue-grey science imagery and teal product photography that stays close to the core brand."
  visible_tells:
    - "A pale molecular image sits in a rounded card against warm cream."
    - "The microdose vial photo below uses teal packaging and a cool blue shirt, linking back to the green/blue product language."
  confidence: high
- id: color_04
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "vertical-specific color shifts"
  tile_path: "store/tryshed-com/captures/2026-06-04/tiles/mens_hair/tile-00-y00000.png"
  claim: "The hair and Foundayo pages introduce separate tan/brown and pink product worlds, which helps differentiate verticals but weakens the single green wellness system."
  visible_tells:
    - "The hair hero uses a warm tan/brown background and amber serum bottles instead of the green vial system."
    - "Foundayo's hero swaps to a soft pink tablet stage with matching pink thumbnails."
  confidence: high
  contrast_with: "store/tryshed-com/captures/2026-06-04/tiles/foundayo/tile-00-y00000.png"
- id: color_05
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "before/after testimonial imagery"
  tile_path: "store/tryshed-com/captures/2026-06-04/tiles/homepage/tile-01-y01220.png"
  claim: "User-result photography adds credibility cues, but the mixed crop quality and lighting interrupt the otherwise controlled product-photo system."
  visible_tells:
    - "Before/after thumbnails vary from outdoor snapshots to indoor mirror or portrait photos."
    - "The testimonial cards sit on consistent beige panels, but the images themselves vary sharply in lighting, framing, and background."
  confidence: high
- id: color_06
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "team portraits and blog cards"
  tile_path: "store/tryshed-com/captures/2026-06-04/tiles/homepage/tile-03-y03660.png"
  claim: "The team and blog rows mix crisp studio headshots with darker lifestyle/editorial thumbnails, creating a visible register shift inside one page section."
  visible_tells:
    - "Team headshots sit on bright white backgrounds with clean portrait lighting."
    - "The blog cards below use darker, overlaid lifestyle images with white text and gradient shading."
  confidence: high
- id: color_07
  family: color_brand_imagery
  polarity: poor
  page_or_region: "press page imagery"
  tile_path: "store/tryshed-com/captures/2026-06-04/tiles/press/tile-00-y00000.png"
  claim: "The press page has almost no imagery or branded visual environment, so it drops out of the product-led brand language seen elsewhere."
  visible_tells:
    - "The main press content is text-only: headline, date, paragraph, and blue link."
    - "No product render, portrait, article card image, or branded media asset appears before the footer."
  confidence: high

- id: iconography_01
  family: iconography_illustration
  polarity: strong
  page_or_region: "product graphics"
  tile_path: "store/tryshed-com/captures/2026-06-04/tiles/foundayo/tile-00-y00000.png"
  claim: "Product graphics are the site's strongest illustration layer: oversized vials, tablets, bottles, and thumbnail states carry the visual system more than decorative icons do."
  visible_tells:
    - "The Foundayo tablet is rendered as a large circular pill with embossed script and matching thumbnails."
    - "The same PDP pattern uses large product imagery plus a row of visual thumbnails beneath the main image."
  confidence: high
  contrast_with: "store/tryshed-com/captures/2026-06-04/tiles/semaglutide/tile-00-y00000.png"
- id: iconography_02
  family: iconography_illustration
  polarity: mixed
  page_or_region: "feature chips and benefits"
  tile_path: "store/tryshed-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"
  claim: "Small utility icons in chips and feature rows are serviceable but generic, acting as navigation/benefit markers rather than a distinctive icon system."
  visible_tells:
    - "The hero chips use tiny monochrome icons beside 'Personalized wellness plans', '100% online visit + checkout', and shipping copy."
    - "The icons are simple line/fill symbols with no custom brand styling beyond the pale green pill container."
  confidence: high
- id: iconography_03
  family: iconography_illustration
  polarity: mixed
  page_or_region: "comparison tables"
  tile_path: "store/tryshed-com/captures/2026-06-04/tiles/weight_loss/tile-02-y02440.png"
  claim: "Comparison tables use sparse checkmarks and x marks to simplify scanning, but the marks are small and sit inside a low-contrast table treatment."
  visible_tells:
    - "Rows such as Convenience, No Needles, and Medical Supervision use teal checkmarks and grey x marks."
    - "The table background fades into pale beige/white, and the icons are the only graphic emphasis in several rows."
  confidence: medium
- id: iconography_04
  family: iconography_illustration
  polarity: mixed
  page_or_region: "step and support icons"
  tile_path: "store/tryshed-com/captures/2026-06-04/tiles/homepage/tile-04-y04880.png"
  claim: "Check-circle icons in support lists are consistent and readable, but they remain basic UI glyphs rather than a memorable brand asset."
  visible_tells:
    - "The green app band uses repeated circular check icons for every support bullet."
    - "The icons share size, stroke, and color, but are generic outline checkmarks."
  confidence: high
- id: iconography_05
  family: iconography_illustration
  polarity: poor
  page_or_region: "third-party proof widgets"
  tile_path: "store/tryshed-com/captures/2026-06-04/tiles/mens_hair/tile-01-y01220.png"
  claim: "Third-party proof widgets visually clash with the site's quieter icon language, especially the Trustpilot star lockup and bright video play button."
  visible_tells:
    - "A green Trustpilot star logo and star-rating strip sit directly above the section headline."
    - "A saturated red/pink play button sits over the testimonial video card, unlike the site's black/tan/green controls."
  confidence: high
```

## Provenance

Tiles read: homepage (7) + weight_loss (6) + semaglutide (6) + tirzepatide (6) + longevity (6) + mens_hair (6) + foundayo (8) + press (2) = 47 active tiles from `captures/2026-06-04/tiles/`. QA gate: clean - cached Tier-A tiles carried no modal, cookie banner, grey/blank hero, black media, lazy-load gap, mid-animation artifact, or scroll-lock contamination. No exclusions and no Tier-B browser re-render.

Mined as a Codex tile-only visual pass against the `/visual-evidence` contract: no profile, dossier body, Notion, or live web used for the visual claims; card claims cite only active native tiles. The structured `Workflow(...)` runner was not exposed in this Codex thread, so no separate Sonnet miner fan-out/judge transcript exists for this run. Snapshot caveat: reflects the 2026-06-04 cached capture; the live site changes.
