---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.0"
domain: trtnation.com
captured_at: 2026-06-17
source_capture: 2026-06-04
qa_status: exclusions-noted
---

## Visual & brand impression

A competent, template-disciplined DTC build whose structure outclasses its imagery. The system is the strength — a clean, decisive type hierarchy on hero and product cards [typography_01, typography_03], a tightly consistent two-column card grid [layout_01], a repeating category-section rhythm [layout_03], and a controlled navy palette with blue accents and gold reserved for logo, stars, and step numbers [color_01]. Imagery is the soft underbelly: generic mismatched stock thumbnails [color_02], hero photography that shifts genre page to page [color_03, color_05], an unharmonized social-proof row [color_04], and bare pill cutouts beside the one strong branded-vial render [iconography_01, iconography_04] — with no custom illustration anywhere [iconography_05]. Hierarchy frays in long-form copy [typography_06]; the hero headline collides with its subject [layout_05].

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: "homepage hero"
  tile_path: "store/trtnation-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"
  claim: "The hero runs a clean three-level hierarchy: a small all-caps eyebrow, a very large heavy condensed display headline, and a smaller lighter subhead, with decisive size steps between each."
  visible_tells:
    - "'#1 IN THE NATION' small all-caps eyebrow above the headline"
    - "'TESTOSTERONE THERAPY' in heavy condensed type at dominant scale"
    - "Subhead 'Get your spark back. $99/mo / 100% online + Free Shipping' drops to noticeably smaller, lighter weight"
  confidence: high
  contrast_with: "store/trtnation-com/captures/2026-06-04/tiles/about/tile-01-y01220.png"

- id: typography_02
  family: typography_hierarchy
  polarity: strong
  page_or_region: "about page hero title"
  tile_path: "store/trtnation-com/captures/2026-06-04/tiles/about/tile-00-y00000.png"
  claim: "The 'ABOUT US' page title is an oversized white all-caps display set over the darkened photo, legible at a glance and clearly the page-level heading."
  visible_tells:
    - "White all-caps bold letterforms spanning roughly the full content width"
    - "Darkened lower half of the photo gives white text sufficient contrast"
  confidence: high

- id: typography_03
  family: typography_hierarchy
  polarity: strong
  page_or_region: "popular treatments — product cards"
  tile_path: "store/trtnation-com/captures/2026-06-04/tiles/popular_treatments/tile-01-y01220.png"
  claim: "Product cards run a consistent four-level hierarchy — bold product name, paragraph description, colored price, then a light checklist — each level a distinct size/weight so the card scans fast; the price is set in blue to break it out of the black copy."
  visible_tells:
    - "Product name ('Testosterone', 'Enclomiphene') in large bold sans"
    - "Price '$99.99/mo' in blue, distinct from black body copy"
    - "Checkmark feature items drop to small regular weight, clearly subordinate"
  confidence: high

- id: typography_04
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "homepage — 'YOUR HEALTH. YOUR MOVE.' treatment menu"
  tile_path: "store/trtnation-com/captures/2026-06-04/tiles/homepage/tile-01-y01220.png"
  claim: "The section heading 'YOUR HEALTH. YOUR MOVE.' and the menu-tile labels ('Testosterone', 'Sexual Health', 'Weight Loss', 'Anti-Aging') sit at similar bold weight, so the heading does not read as decisively dominant over the tiles beneath it."
  visible_tells:
    - "Section heading bold but not much larger than the tile-name labels"
    - "Tile labels are heavy enough to compete visually with the heading"
  confidence: medium

- id: typography_05
  family: typography_hierarchy
  polarity: poor
  page_or_region: "about page — 'Our Mission' bullet list vs body"
  tile_path: "store/trtnation-com/captures/2026-06-04/tiles/about/tile-02-y02440.png"
  claim: "Under 'Our Mission' the checkmark feature list ('Transparent pricing', 'Unlimited support', etc.) is set at nearly the same size and weight as the paragraph above it, so the shift from prose to list is barely enforced typographically; the same section's 'Our Story'-style heads are only modestly larger than body."
  visible_tells:
    - "Bullet items match the body paragraph weight and size almost exactly"
    - "No type-size change or strong indent signals the switch to a list"
  confidence: medium

- id: typography_06
  family: typography_hierarchy
  polarity: poor
  page_or_region: "testosterone page — long-form body sub-headings"
  tile_path: "store/trtnation-com/captures/2026-06-04/tiles/testosterone/tile-03-y03660.png"
  claim: "In-line sub-headings 'Why Testosterone Matters' and 'How TRT Helps' are set small with only a blue color tint and minimal size/weight lift over the surrounding paragraph text, so they read weakly and are easy to skim past."
  visible_tells:
    - "Both sub-heads are only slightly larger than body and rely on a small blue tint rather than scale"
    - "Little spacing separates the sub-heads from the prose around them"
  confidence: high
  contrast_with: "store/trtnation-com/captures/2026-06-04/tiles/popular_treatments/tile-02-y02440.png"

- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: "popular treatments — product card grid"
  tile_path: "store/trtnation-com/captures/2026-06-04/tiles/popular_treatments/tile-01-y01220.png"
  claim: "The two-column product-card system is tightly consistent: badge, product image, name, body copy, price, four-item checklist, and CTA button occupy the same vertical slots in every card, with uniform borders and corner radii."
  visible_tells:
    - "Testosterone and Enclomiphene cards align blue badge, vial/pill image, name, blue price, four-item checklist, and navy 'Customize Treatment' button at identical vertical positions"
    - "Card outline and corner radius are uniform across both columns"
  confidence: high
  contrast_with: "store/trtnation-com/captures/2026-06-04/tiles/popular_treatments/tile-03-y03660.png"

- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: "labs — three navy feature tiles"
  tile_path: "store/trtnation-com/captures/2026-06-04/tiles/labs/tile-01-y01220.png"
  claim: "The three navy feature tiles (Complete lab checkout / Visit local lab near you / Fast, reliable lab results) form a precise equal-width three-column strip with matching height, icon size, centered text, and even gutters."
  visible_tells:
    - "All three tiles share identical height, navy fill, white icon weight, and centered two-line label"
    - "Gutter spacing between tiles is visually equal"
  confidence: high

- id: layout_03
  family: layout_composition_components
  polarity: strong
  page_or_region: "popular treatments — category section rhythm"
  tile_path: "store/trtnation-com/captures/2026-06-04/tiles/popular_treatments/tile-02-y02440.png"
  claim: "Category breaks follow one repeated two-line pattern down the page — a large heavy black all-caps therapy name over a smaller spaced colored all-caps tagline — giving a reliable section-break rhythm as the user scrolls through Weight Loss, Sexual Health, and Anti-Aging."
  visible_tells:
    - "'SEXUAL HEALTH THERAPY' in large heavy black caps over 'FEEL THE DRIVE AGAIN, INSIDE + OUT.' in smaller blue caps"
    - "Same name-over-tagline pattern recurs for Weight Loss and Anti-Aging on adjacent tiles"
  confidence: high
  contrast_with: "store/trtnation-com/captures/2026-06-04/tiles/popular_treatments/tile-03-y03660.png"

- id: layout_04
  family: layout_composition_components
  polarity: strong
  page_or_region: "popular treatments / testosterone — four-step process strip"
  tile_path: "store/trtnation-com/captures/2026-06-04/tiles/popular_treatments/tile-05-y06100.png"
  claim: "The '100% ONLINE THERAPY' how-it-works strip lays out four equal numbered cards (1 Select Treatment, 2 Review Blood Work, 3 Meet Licensed Provider, 4 Begin Treatment) with matching card shape, numbered amber headers, and a small supporting image in each, then a single centered navy CTA below."
  visible_tells:
    - "Four equal rounded cards in a row, each with an amber step number and short two-line label"
    - "Centered navy 'Customize Your TRT' button sits beneath the strip"
  confidence: high

- id: layout_05
  family: layout_composition_components
  polarity: mixed
  page_or_region: "homepage hero composition"
  tile_path: "store/trtnation-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"
  claim: "The hero composites a branded vial cutout into the lower-right against a lifestyle photo, but the large white headline crashes onto the man's dark torso with no scrim or gap, and the '#1 IN THE NATION' eyebrow floats with weak spatial grouping to the headline — a present hierarchy that is collision-prone."
  visible_tells:
    - "White 'TESTOSTERONE / THERAPY' overlaps directly onto the man's shirt with no gradient or panel behind it"
    - "'#1 IN THE NATION' sits above the headline with a loose gap rather than a tight grouping"
  confidence: high
  contrast_with: "store/trtnation-com/captures/2026-06-04/tiles/testosterone/tile-00-y00000.png"

- id: layout_06
  family: layout_composition_components
  polarity: mixed
  page_or_region: "about page — multi-photo editorial strip"
  tile_path: "store/trtnation-com/captures/2026-06-04/tiles/about/tile-03-y03660.png"
  claim: "The horizontal photo strip above the 'TRT Nation Patients Love Our Commitment to Excellence' banner uses unequal image widths that read as a mosaic, but the proportions follow no apparent grid logic, so the row reads more assembled than composed."
  visible_tells:
    - "Five abutting photos of differing widths with no consistent column or thirds logic"
    - "Subject scale and crop jump from panel to panel"
  confidence: medium

- id: layout_07
  family: layout_composition_components
  polarity: poor
  page_or_region: "about page — clipped treatment carousel rail"
  tile_path: "store/trtnation-com/captures/2026-06-04/tiles/about/tile-05-y05208.png"
  claim: "The footer-area treatment carousel ('Trying to keep it up' / 'Lose weight fast' / 'Energy that lasts' / 'Aging without aches') runs its rail outside the page's content gutter — the left-most card is flush to the viewport edge with no margin while inner cards have gaps, so the rail does not align to the column used by every other section."
  visible_tells:
    - "Left-most card edge is flush against the viewport with no left margin"
    - "A left chevron control sits half off-edge; inner cards carry visible gaps the edge card does not"
  confidence: medium

- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: "site-wide structural palette"
  tile_path: "store/trtnation-com/captures/2026-06-04/tiles/labs/tile-01-y01220.png"
  claim: "A disciplined structural palette holds across pages: navy as the dominant dark surface/CTA color and blue as the secondary accent (prices, badges, taglines), with gold/amber reserved for the logo mark, review stars, and step numbers — the navy filled-card block in particular recurs identically on Labs, Popular Treatments, and the homepage menu."
  visible_tells:
    - "Three navy filled cards with white icon + white label on Labs"
    - "Same navy block reused as menu tiles and 'Customize Treatment' / 'Customize Your TRT' buttons elsewhere"
  confidence: high
  contrast_with: "store/trtnation-com/captures/2026-06-04/tiles/popular_treatments/tile-01-y01220.png"

- id: color_02
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "homepage — lifestyle thumbnail row"
  tile_path: "store/trtnation-com/captures/2026-06-04/tiles/homepage/tile-03-y03660.png"
  claim: "The four lifestyle category thumbnails (older couple at sunset, woman with drink in a cart, man with child, couple in a golf cart) read as generic stock assembled for demographic coverage — no shared lighting, grade, or framing, and a different visual language from the hero athlete photo."
  visible_tells:
    - "Four thumbnails with inconsistent lighting, setting, and subject framing"
    - "Golf-cart and outdoor shots share no visual language with the hero photography"
  confidence: high
  contrast_with: "store/trtnation-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"

- id: color_03
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "page heroes — inconsistent subject genre"
  tile_path: "store/trtnation-com/captures/2026-06-04/tiles/popular_treatments/tile-00-y00000.png"
  claim: "Hero photography genre shifts page to page rather than reading as one shoot: 'MOST POPULAR' uses a navy-graded rooftop couple, About uses a backlit athletic couple at a railing, while Homepage and Testosterone use a solo male athlete — the grade aligns but the subject register does not."
  visible_tells:
    - "Popular hero: romantic couple on a rooftop under a navy grade"
    - "Testosterone/homepage heroes: solo male athlete, different register"
  confidence: medium
  contrast_with: "store/trtnation-com/captures/2026-06-04/tiles/testosterone/tile-00-y00000.png"

- id: color_04
  family: color_brand_imagery
  polarity: poor
  page_or_region: "about page — social-proof image row"
  tile_path: "store/trtnation-com/captures/2026-06-04/tiles/about/tile-03-y03660.png"
  claim: "The social-proof photo row stitches five unrelated stock images (family outdoors, older woman with man, man on phone, older couple, father lifting child) with differing warm/cool/neutral color casts and crop ratios, with no attempt to harmonize them into one grid system."
  visible_tells:
    - "Distinct warm, cool, and neutral color casts across adjacent photos"
    - "Subject matter ranges individual / couple / parent-child with no connecting thread"
  confidence: high

- id: color_05
  family: color_brand_imagery
  polarity: poor
  page_or_region: "labs hero photography"
  tile_path: "store/trtnation-com/captures/2026-06-04/tiles/labs/tile-00-y00000.png"
  claim: "The Labs hero swaps the brand's lifestyle photography for a generic clinical stock shot — a woman in a lab coat against a blurred lab — with no navy grade or overlay, so it reads disconnected from every other page hero."
  visible_tells:
    - "Woman in a white coat in a clinical setting, a different genre from the athlete/couple heroes"
    - "No dark overlay or color treatment ties it to the brand tone used elsewhere"
  confidence: high
  contrast_with: "store/trtnation-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"

- id: color_06
  family: color_brand_imagery
  polarity: poor
  page_or_region: "popular treatments — mixed product-image styles"
  tile_path: "store/trtnation-com/captures/2026-06-04/tiles/popular_treatments/tile-02-y02440.png"
  claim: "Product imagery mixes incompatible styles in the same grid — branded labeled vials, bare white capsule cutouts, and amber tablet photos — with no shared background, shadow handling, or scale, so the card grid feels assembled from different sources."
  visible_tells:
    - "Branded labeled vials on some cards versus plain pill/capsule cutouts on others"
    - "Amber tablet photo carries different lighting and background tone from the vials"
  confidence: high

- id: iconography_01
  family: iconography_illustration
  polarity: strong
  page_or_region: "homepage hero — branded vial render"
  tile_path: "store/trtnation-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"
  claim: "The branded vial composited into the hero is the strongest product graphic on the site — labeled, gold-capped, cleanly placed lower-right, and echoing the brand gold — a deliberate render the bare pill cutouts elsewhere lack."
  visible_tells:
    - "Gold-and-white labeled vial with dark cap composited cleanly into the lower-right of the hero"
    - "Amber label band echoes the gold logo accent"
  confidence: high
  contrast_with: "store/trtnation-com/captures/2026-06-04/tiles/popular_treatments/tile-01-y01220.png"

- id: iconography_02
  family: iconography_illustration
  polarity: mixed
  page_or_region: "anti-aging product cards — vial family"
  tile_path: "store/trtnation-com/captures/2026-06-04/tiles/popular_treatments/tile-03-y03660.png"
  claim: "The NAD+, Glutathione, and Sermorelin vials are shot at a matching angle and scale with distinct label-band colors (blue, white, green) per SKU, forming a coherent product family — a clear step above the flat pill cutouts, though not high-end studio photography."
  visible_tells:
    - "Three vials at matching scale and angle, each with a different colored label band"
    - "Labels read clearly but lack professional lighting depth"
  confidence: high
  contrast_with: "store/trtnation-com/captures/2026-06-04/tiles/popular_treatments/tile-01-y01220.png"

- id: iconography_03
  family: iconography_illustration
  polarity: mixed
  page_or_region: "labs — three feature-tile icons"
  tile_path: "store/trtnation-com/captures/2026-06-04/tiles/labs/tile-01-y01220.png"
  claim: "The labs feature-tile icons are internally consistent — same white outline weight on navy across all three tiles — but the forms (shopping cart, speeding car, checkmark) are generic stock glyphs with no custom craft."
  visible_tells:
    - "Three navy tiles each with one white outline icon at matching size and stroke"
    - "Cart and motion-car icons are recognizable off-the-shelf glyphs"
  confidence: high

- id: iconography_04
  family: iconography_illustration
  polarity: poor
  page_or_region: "popular treatments — bare pill/tablet cutouts"
  tile_path: "store/trtnation-com/captures/2026-06-04/tiles/popular_treatments/tile-01-y01220.png"
  claim: "Pill and capsule products are shown as plain cutout photos on blank white with no shadow, staging, or graphic treatment, giving those cards a bare, undesigned feel next to the branded vial renders."
  visible_tells:
    - "Enclomiphene card shows white capsules floating on blank white with a faint mismatched shadow"
    - "No depth cue, staging, or graphic frame around the cutout"
  confidence: high
  contrast_with: "store/trtnation-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"

- id: iconography_05
  family: iconography_illustration
  polarity: poor
  page_or_region: "about / site-wide — no custom illustration or data viz"
  tile_path: "store/trtnation-com/captures/2026-06-04/tiles/about/tile-02-y02440.png"
  claim: "There is no custom illustration, branded diagram, or data visualization anywhere in the captured pages — the About 'Our Mission' section is a plain checkmark text list with an embedded YouTube thumbnail standing in for original graphic content."
  visible_tells:
    - "'Our Mission' is a plain bulleted text list with no supporting graphic or icon row"
    - "An embedded video thumbnail is the only visual in the section"
  confidence: high
```

## Provenance

- **Tiles read:** native-resolution tiles under `store/trtnation-com/captures/2026-06-04/tiles/` for 5 pages — `homepage`, `testosterone`, `popular_treatments`, `labs`, `about`. 24 active tiles mined blind across four family miners (Sonnet) → judge (Opus): 39 raw cards → 24 accepted (9 strong / 7 mixed / 8 poor), 15 rejected.
- **Exclusions (capture defects, not design):** three tiles dropped before mining because a "Excellent 4.9 / 1943 reviews" review-slider widget failed to load its slides, leaving a large blank navy void, compounded by a sticky-header scroll-stitch band — `homepage/tile-02-y02440.png`, `testosterone/tile-02-y02440.png`, `about/tile-04-y04880.png`. The same unloaded-slider void also recurs lower on `popular_treatments/tile-04-y04880.png` (kept in the active set but no accepted card cites it; the judge rejected the one card derived from it as a JS-load artifact).
- **Sticky-header artifact caveat:** the site's real "America's Clinic" utility bar + white nav is a fixed/sticky header that re-renders mid-tile at nearly every stitch boundary in these full-page screenshots. The judge correctly rejected all three "sticky nav clutters/divides content" cards as capture caveats, not design evidence; the header design itself remains valid evidence elsewhere.
- **Tier-B re-render attempted but blocked:** browser re-render of `https://trtnation.com` via `shoot.py` returned a Cloudflare "Attention Required!" bot-wall (thin/interstitial guard fired), so no clean recapture was possible; the run is confined to cached (Tier-A) tiles. `qa_status: exclusions-noted`.
- **Snapshot caveat:** this is a point-in-time read of the 2026-06-04 captured tiles; the live site may have changed.
