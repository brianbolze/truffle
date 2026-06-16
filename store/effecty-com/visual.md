---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.0"
domain: effecty.com
captured_at: 2026-06-16
source_capture: 2026-06-04
qa_status: clean
---

## Visual & brand impression

Effecty reads as a quiet, template-disciplined system: a narrow white/near-black/sage palette held with restraint [color_01], repeating photo-card components from hero to process row [layout_01][layout_02], a consistent two-tone split-word heading pattern [typography_02], and a cleanly resolved dark footer [layout_05][color_08]. Its most owned assets are the purpose-shot branded vials [color_02] and the art-directed GLP-1 banner [iconography_01]. Finish is where it wobbles, mostly in imagery: assembled lifestyle grades [color_03], a recurring stock-doctor archetype [color_07], and grammar-breaking testimonial cards [layout_06][color_06]. A loud amber promo bar sits outside the palette [color_05], icons fall back to generic glyphs and a default chevron accordion [iconography_03][iconography_04], while a hard-clipped carousel [layout_09] and unsubordinated legalese [typography_06] betray template defaults.

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: "Homepage hero"
  tile_path: "store/effecty-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"
  claim: "The hero headline sets a clear top-of-page hierarchy: a large two-line serif-display H1 ('Longevity treatment, / made simple') dwarfs the small medium-weight nav row and the tiny 'Excellent' micro-label, giving an immediate single read order."
  visible_tells:
    - "H1 runs at roughly 3x the size of the nav items (Weight Loss / Longevity / Hormone Therapy / Login)"
    - "Second line 'made simple' is set in a lighter grey, subordinating it within one headline level rather than competing"
    - "Nav and the small green 'Excellent' star label sit far below the headline in scale"
  confidence: high

- id: typography_02
  family: typography_hierarchy
  polarity: strong
  page_or_region: "Section headers — treatments & homepage (two-tone split-word pattern)"
  tile_path: "store/effecty-com/captures/2026-06-04/tiles/treatments/tile-01-y01220.png"
  claim: "Section headers use a consistent two-tone split-word system — first word in solid near-black, trailing word(s) in a muted blue/sage gradient — that reliably flags a new section and recurs across pages."
  visible_tells:
    - "'Longevity' solid black + 'Medication' in muted blue/sage on the treatments section header"
    - "Same pattern on 'How Effecty works', 'Why Effecty?', 'What people say about Effecty', 'Frequently asked questions', and 'What Are We All About'"
    - "Section header sits visibly larger than the product-name text in the cards below it"
  confidence: high
  contrast_with: "store/effecty-com/captures/2026-06-04/tiles/about-us/tile-00-y00000.png"

- id: typography_03
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "Treatments page — product cards"
  tile_path: "store/effecty-com/captures/2026-06-04/tiles/treatments/tile-01-y01220.png"
  claim: "Inside each product card the price line sits at near-body size directly under the larger product name, while a category tag pill ('Longevity') floats top-right at a third size, leaving three small text elements competing at the card's top with weak separation."
  visible_tells:
    - "'NAD+ Injection' name is clearly larger, but '$160/month*' beneath it is small and low-contrast grey"
    - "Category pill 'Longevity' top-right is roughly the same scale as the price, adding a third competing micro-element"
    - "No strong weight or color step between name, price, and tag"
  confidence: medium

- id: typography_04
  family: typography_hierarchy
  polarity: strong
  page_or_region: "Weight-loss GLP-1 detail page — hero"
  tile_path: "store/effecty-com/captures/2026-06-04/tiles/weight-loss-glp1/tile-00-y00000.png"
  claim: "The product-detail hero lands a clean three-level hierarchy: large 'GLP-1 treatment' headline, mid-size 'Starting at $160/month*', then small feature chips housed in light grey capsules that subordinate them clearly."
  visible_tells:
    - "'GLP-1 treatment' is the largest text in the hero"
    - "'Starting at $160/month*' sits a clear step smaller but still prominent"
    - "Feature chips ('Same price at every dose', 'No insurance required', '24/7 support') are smallest and wrapped in pale grey pill containers"
  confidence: high

- id: typography_05
  family: typography_hierarchy
  polarity: strong
  page_or_region: "FAQ section (treatments & homepage)"
  tile_path: "store/effecty-com/captures/2026-06-04/tiles/treatments/tile-05-y06100.png"
  claim: "The FAQ block keeps a clean two-level hierarchy: a large centered 'Frequently asked questions' heading over uniform accordion question rows that are all the same distinctly smaller size and weight."
  visible_tells:
    - "'Frequently asked questions' heading is markedly larger than any accordion row"
    - "All five question rows ('What is Effecty?' … 'What states do you ship to?') are visually identical weight and size"
    - "Each row sits in an evenly spaced pale-grey pill container"
  confidence: high

- id: typography_06
  family: typography_hierarchy
  polarity: poor
  page_or_region: "Treatments page — legal disclaimer under each carousel"
  tile_path: "store/effecty-com/captures/2026-06-04/tiles/treatments/tile-01-y01220.png"
  claim: "The multi-line legal disclaimer after each carousel runs as a full-width grey paragraph at near-body size with no containment or strong size step down, so the fine print reads as a content block rather than subordinated legalese."
  visible_tells:
    - "Disclaimer paragraph spans the full content width directly between carousel groups"
    - "Text is only marginally smaller than product copy and uses a low-contrast grey with no boxing or rule to set it apart"
    - "Same dense disclaimer repeats under both the GLP-1 and Longevity carousels"
  confidence: high
  contrast_with: "store/effecty-com/captures/2026-06-04/tiles/treatments/tile-05-y06100.png"

- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: "Homepage hero — three-card category row"
  tile_path: "store/effecty-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"
  claim: "The hero category row is a disciplined three-column card grid (Weight Loss / Longevity / Hormone Therapy) with identical card height, matching rounded corners, and a CTA pinned to the same bottom-left position in each."
  visible_tells:
    - "Three cards at equal height with uniform corner radius and image treatment"
    - "'Get Started' / 'Learn more' pill CTAs anchor to the same lower-left spot in each card"
    - "Consistent gutters between the three cards"
  confidence: high

- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: "Homepage — 'How Effecty works' three-step row"
  tile_path: "store/effecty-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"
  claim: "The three-step process row (Medical questionnaire / Prescription / Delivery) reuses the same photo-card-over-caption shell as the hero cards, evidencing a repeating component system rather than bespoke sections."
  visible_tells:
    - "Three equal cards share the rounded-corner radius and aspect of the hero category cards above"
    - "Each caption sits bottom-left over a darkened photo in the same position"
    - "Cards are evenly gutter-spaced in a matching three-up grid"
  confidence: high
  contrast_with: "store/effecty-com/captures/2026-06-04/tiles/homepage/tile-01-y01220.png"

- id: layout_03
  family: layout_composition_components
  polarity: strong
  page_or_region: "Homepage / About-us — 'Why Effecty?' trust-pillar grid"
  tile_path: "store/effecty-com/captures/2026-06-04/tiles/about-us/tile-01-y01220.png"
  claim: "The 'Why Effecty?' trust cells form a disciplined grid where each cell pairs a centered headline, short body, an 'Explore' pill, and a cut-out product/photo with a consistently placed lower-right verification badge."
  visible_tells:
    - "Licensed pharmacies / Board Certified cells share identical internal structure and badge placement ('Licensed' and 'Board Certified' chips at lower-right of each image)"
    - "'Explore' dark pill CTA sits in the same relative spot in each cell"
    - "Cell backgrounds and border-radius match the feature cards above"
  confidence: high
  contrast_with: "store/effecty-com/captures/2026-06-04/tiles/homepage/tile-02-y02440.png"

- id: layout_04
  family: layout_composition_components
  polarity: strong
  page_or_region: "Treatments page — category carousel anatomy"
  tile_path: "store/effecty-com/captures/2026-06-04/tiles/treatments/tile-01-y01220.png"
  claim: "Each treatment category renders as a consistent horizontal carousel with identical anatomy: split-word heading left, category pill-toggle right, product cards (photo / name / price / dual-CTA), prev-next arrow controls, then a disclaimer paragraph — repeated unchanged across Longevity and Menopause."
  visible_tells:
    - "'Longevity' heading + 'Longevity' pill toggle, then 'Menopause Products' heading + 'Menopause' pill toggle at the same vertical offset"
    - "Dual CTA ('Get Started' filled, 'Learn more' outline) repeats without variation across every card"
    - "Circular left/right arrow controls sit at the same lower-left position under each carousel"
  confidence: high
  contrast_with: "store/effecty-com/captures/2026-06-04/tiles/treatments/tile-02-y02440.png"

- id: layout_05
  family: layout_composition_components
  polarity: strong
  page_or_region: "Footer — across all pages"
  tile_path: "store/effecty-com/captures/2026-06-04/tiles/treatments/tile-06-y06491.png"
  claim: "The footer is a well-resolved multi-zone layout: brand + email-capture block left, two nav columns right, top-aligned to a shared baseline with even vertical rhythm, closing the dark-field endpoint cleanly."
  visible_tells:
    - "Both nav columns (Weight Loss/Longevity/… and Contact Us/FAQ/…) align to the same top baseline with equal row spacing"
    - "Email input and circular arrow submit button are inline and vertically centered under 'Connect with Effecty'"
    - "'Compounded in the USA' badge and social icons sit at consistent left-column margins"
  confidence: high

- id: layout_06
  family: layout_composition_components
  polarity: mixed
  page_or_region: "Homepage — testimonial carousel"
  tile_path: "store/effecty-com/captures/2026-06-04/tiles/homepage/tile-03-y03660.png"
  claim: "The testimonial row mixes two incompatible card formats — before/after photo-pair-plus-text cards flanking a full-bleed video-still card with an overlaid burned-in caption — without a unifying rule, leaving the row visually unequal."
  visible_tells:
    - "Center card (Amie S.) is a full-height video still with white burned-in 'So I have just been absolutely thrilled' text overlay"
    - "Flanking cards (Amanda R., Jentre R.) show a small before/after portrait pair at top with plain text testimonial below"
    - "Card heights and internal composition visibly differ between center and flanks"
  confidence: high

- id: layout_07
  family: layout_composition_components
  polarity: mixed
  page_or_region: "Hormones page — 'Do you need Progesterone too' section"
  tile_path: "store/effecty-com/captures/2026-06-04/tiles/hormones/tile-01-y01220.png"
  claim: "This section departs from the site's card-and-carousel rhythm with a one-off two-column split — a tall uncontained editorial photo left, a stack of icon-label benefit rows right — that echoes no other module on the reviewed pages."
  visible_tells:
    - "Left column is a full-height portrait of a grey-haired woman with no card container"
    - "Right column is a flat list of benefit rows (Balanced hormone delivery / Supports better sleep / Eases anxiety + mood swings / Whole-hormone harmony) with small right-aligned icons, no card treatment"
    - "No equivalent uncontained two-column split appears on any other reviewed tile"
  confidence: high
  contrast_with: "store/effecty-com/captures/2026-06-04/tiles/hormones/tile-00-y00000.png"

- id: layout_08
  family: layout_composition_components
  polarity: mixed
  page_or_region: "About Us — 'Reach us directly' contact section"
  tile_path: "store/effecty-com/captures/2026-06-04/tiles/about-us/tile-04-y04880.png"
  claim: "The contact section uses an uneven three-panel layout — a 50/50 General Inquiries / Customer Support row above, then a full-width 'For Employers & Partners' card below carrying far more body text — inverting the visual weight toward the least primary contact path."
  visible_tells:
    - "General Inquiries and Customer Support sit in a balanced 50/50 row of equal-height cards"
    - "'For Employers & Partners' spans full width beneath and holds three paragraphs of copy, dwarfing the two cards above"
    - "The employer card is the visually heaviest block despite being a secondary contact route"
  confidence: medium

- id: layout_09
  family: layout_composition_components
  polarity: poor
  page_or_region: "Homepage — treatments carousel clipped fourth card"
  tile_path: "store/effecty-com/captures/2026-06-04/tiles/homepage/tile-01-y01220.png"
  claim: "The homepage treatments carousel clips the fourth card (Sermorelin) hard at the right edge with no fade or peek-styling, so the card reads ambiguously as an overflow artifact rather than a deliberate peek."
  visible_tells:
    - "Sermorelin card is sliced vertically at the right margin, showing only its name and '$200/month*' line"
    - "The clipped card carries no gradient fade or partial-peek treatment; circular prev/next arrows sit below the row but don't visually tie to the cut edge"
  confidence: medium
  contrast_with: "store/effecty-com/captures/2026-06-04/tiles/treatments/tile-00-y00000.png"

- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: "Homepage hero and product cards — palette discipline"
  tile_path: "store/effecty-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"
  claim: "The core palette is narrow and restrained: near-white fields, near-black type, and a single muted sage/blue accent, with no loud competing color across the hero and card rows."
  visible_tells:
    - "White page field dominates the hero"
    - "Sage and muted-blue appear only as card backdrops (Longevity card) and the split-word accent, not scattered"
    - "Product vials carry a unified cool-neutral cast against the white"
  confidence: high
  contrast_with: "store/effecty-com/captures/2026-06-04/tiles/treatments/tile-00-y00000.png"

- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: "Owned product photography — branded vials & packaging"
  tile_path: "store/effecty-com/captures/2026-06-04/tiles/treatments/tile-01-y01220.png"
  claim: "Product photography is purpose-shot and consistent: vials and bottles share studio lighting, a soft grey-to-white ground, and an identically placed 'effecty.' wordmark, making the catalog read as one object family."
  visible_tells:
    - "NAD+, Sermorelin, and Sermorelin ODT renders share the same lighting angle and cast-shadow treatment"
    - "The 'effecty.' wordmark sits centered on each blue-grey label at comparable scale"
    - "No stock pill-jar mismatch among the branded SKUs"
  confidence: high
  contrast_with: "store/effecty-com/captures/2026-06-04/tiles/homepage/tile-03-y03660.png"

- id: color_03
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "Homepage 'How Effecty works' — lifestyle photography"
  tile_path: "store/effecty-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"
  claim: "Lifestyle photography is warm and competent but reads as assembled rather than one coordinated shoot — the woman-on-laptop, the smiling woman, and the delivery-box shot don't share a common color grade or lighting signature."
  visible_tells:
    - "Woman-on-laptop is warm ambient interior; center portrait is brighter/cooler studio light"
    - "Right card is a near product-on-neutral box shot, stylistically detached from the two people photos"
    - "Backgrounds shift from warm interior to soft neutral across the three cards"
  confidence: medium
  contrast_with: "store/effecty-com/captures/2026-06-04/tiles/treatments/tile-01-y01220.png"

- id: color_04
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "Page-to-page hero backgrounds — palette drift"
  tile_path: "store/effecty-com/captures/2026-06-04/tiles/hormones/tile-00-y00000.png"
  claim: "Hero backdrops drift in temperature page to page: the hormones hero uses a warm sandy/tan field behind the model, the weight-loss hero a neutral grey, the homepage white — a mild but visible inconsistency in the otherwise quiet palette."
  visible_tells:
    - "Hormones hero right panel is a warm beige/tan ground"
    - "Weight-loss hero (treatments/tile-00) uses a flat cool-grey ground behind its model"
    - "Homepage hero is white; the tan tone appears nowhere else in the reviewed tiles"
  confidence: medium
  contrast_with: "store/effecty-com/captures/2026-06-04/tiles/treatments/tile-00-y00000.png"

- id: color_05
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "Top promo announcement bar"
  tile_path: "store/effecty-com/captures/2026-06-04/tiles/about-us/tile-00-y00000.png"
  claim: "The full-width top ticker bar uses a saturated amber/gold with star icons — a color that sits outside the sage-and-white system and reads as a loud promotional bolt-on against the otherwise quiet page."
  visible_tells:
    - "Amber/gold ticker repeating 'Up to 50% off most treatments with code EFFECTY100' with star glyphs"
    - "No other surface in the reviewed tiles uses amber/gold"
    - "Bar is markedly higher-contrast than everything beneath it"
  confidence: high
  contrast_with: "store/effecty-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"

- id: color_06
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "Testimonials carousel — user-submitted imagery"
  tile_path: "store/effecty-com/captures/2026-06-04/tiles/treatments/tile-05-y06100.png"
  claim: "The testimonial cards break the controlled imagery grammar: a dim, cool-grey in-car video selfie sits beside warm outdoor before/after portraits, mixing aspect ratios and color environments mid-row."
  visible_tells:
    - "Video card (Amie S.) is a dim car-interior still, cool and grainy"
    - "Adjacent before/after portraits are bright warm outdoor shots"
    - "Card crops and color temperature visibly differ across the row"
  confidence: high
  contrast_with: "store/effecty-com/captures/2026-06-04/tiles/treatments/tile-01-y01220.png"

- id: color_07
  family: color_brand_imagery
  polarity: poor
  page_or_region: "Why Effecty — 'Board Certified' physician stock image"
  tile_path: "store/effecty-com/captures/2026-06-04/tiles/about-us/tile-01-y01220.png"
  claim: "The 'Board Certified' credentialing block uses a recognizable doctor-stock archetype — red-haired woman in a white coat with a stethoscope, arms crossed — and the same image recurs on the homepage Why-Effecty grid, signalling stock rather than owned imagery."
  visible_tells:
    - "White-coat-plus-stethoscope arms-crossed pose against a soft neutral background is the canonical 'doctor stock photo' pattern"
    - "The identical photo appears on both the About-us and Homepage 'Why Effecty?' grids"
    - "A 'Board Certified' verification chip is composited over the lower-right of the figure"
  confidence: high
  contrast_with: "store/effecty-com/captures/2026-06-04/tiles/treatments/tile-01-y01220.png"

- id: color_08
  family: color_brand_imagery
  polarity: strong
  page_or_region: "Footer — across all pages"
  tile_path: "store/effecty-com/captures/2026-06-04/tiles/treatments/tile-06-y06491.png"
  claim: "The footer holds a consistent near-black field with a white 'effecty.' wordmark and white nav, a correctly contrasted brand endpoint that stays disciplined even where page-body imagery varies."
  visible_tells:
    - "Deep near-black footer ground used identically on every reviewed page tile"
    - "White 'effecty.' wordmark + LegitScript badge and white nav text hold clean contrast on the dark ground"
    - "A single sage circular arrow submit button is the only accent in the footer"
  confidence: high
  contrast_with: "store/effecty-com/captures/2026-06-04/tiles/about-us/tile-00-y00000.png"

- id: iconography_01
  family: iconography_illustration
  polarity: strong
  page_or_region: "GLP-1 product page — CTA banner render"
  tile_path: "store/effecty-com/captures/2026-06-04/tiles/weight-loss-glp1/tile-06-y06209.png"
  claim: "The 'Start your GLP-1 journey' banner render is the site's most art-directed graphic: the branded vial on a soft sage ground that matches its own label, a syringe laid at a deliberate diagonal, and a controlled soft cast shadow."
  visible_tells:
    - "Sage banner background echoes the muted-green vial label (deliberate monochromatic pairing)"
    - "Syringe placed on a precise diagonal beside the vial rather than dropped in casually"
    - "Soft grounded shadow anchors the vial without overpowering it"
  confidence: high
  contrast_with: "store/effecty-com/captures/2026-06-04/tiles/homepage/tile-03-y03660.png"

- id: iconography_02
  family: iconography_illustration
  polarity: mixed
  page_or_region: "Homepage / About-us — 'Why Effecty?' feature tiles"
  tile_path: "store/effecty-com/captures/2026-06-04/tiles/homepage/tile-02-y02440.png"
  claim: "The 'Why Effecty?' feature cells lean on product-photo cut-outs as surrogate icons (pill spilling from a jar, credit-card stack, parcel-in-hands) with floating SaaS-style verification chips, a photo-collage technique rather than a crafted icon set."
  visible_tells:
    - "Pill-spilling-from-jar and credit-card-stack cut-outs stand in for icons inside the cells"
    - "White rounded chips ('Pharmacy / Licensed', 'Price / Fixed', 'Delivery / Free', 'Your physician / Board Certified') each carry a small green check badge in a generic component style"
    - "The card-stack and parcel images are lit differently from each other within the same grid"
  confidence: high
  contrast_with: "store/effecty-com/captures/2026-06-04/tiles/weight-loss-glp1/tile-06-y06209.png"

- id: iconography_03
  family: iconography_illustration
  polarity: mixed
  page_or_region: "About Us — 'Effecty Difference' feature-card icons"
  tile_path: "store/effecty-com/captures/2026-06-04/tiles/about-us/tile-01-y01220.png"
  claim: "The four 'Effecty Difference' cards use small outline icons (medical cross, people-group, headset, price-tag) that are recognizable but library-generic, rendered tiny in near-black with no brand-specific treatment or color."
  visible_tells:
    - "Medical-cross icon on 'More Than Just Telemedicine' is a stock uniform-stroke shape"
    - "People-group, headset, and tag icons sit small at top-left of each card with no color or weight differentiation"
    - "Icons read as off-the-shelf outline glyphs rather than drawn for the brand"
  confidence: high
  contrast_with: "store/effecty-com/captures/2026-06-04/tiles/weight-loss-glp1/tile-06-y06209.png"

- id: iconography_04
  family: iconography_illustration
  polarity: poor
  page_or_region: "FAQ accordion — across multiple pages"
  tile_path: "store/effecty-com/captures/2026-06-04/tiles/treatments/tile-05-y06100.png"
  claim: "The FAQ accordion toggle is a bare hairline chevron with no container, brand treatment, or tie to the rounded-pill UI vocabulary used elsewhere — a default-component look."
  visible_tells:
    - "Each row ends in a thin chevron-down glyph inside a faint circle, identical to a default disclosure control"
    - "No visual relationship between the chevron and the pill buttons/badges used across the rest of the UI"
  confidence: medium
```

## Provenance

- **Tiles read (33, all Tier-A cached):** `captures/2026-06-04/tiles/` across five pages — `homepage` (6), `treatments` (7), `hormones` (7), `weight-loss-glp1` (7), `about-us` (6). Source capture 2026-06-04; mined 2026-06-16.
- **QA:** `clean` — all five pages rendered fully (complete layouts, no modals, cookie/consent overlays, grey/WebGL heros, black media, or mid-animation reveals). No tiles excluded; no Tier-B browser re-render needed. The video testimonial cards (homepage/about-us) rendered normally as photo stills with play overlays.
- **One caveat noted, not mined:** the `about-us` hero (`about-us/tile-00`) reads as a near-empty white field carrying only the "What Are We All About" heading — likely an un-rendered hero region. Per the capture-hygiene rule this is a capture caveat, not a design defect, so the four blank-hero observations the miners raised were dropped at the judge stage rather than recorded as `poor` cards. The tile remains valid for its other content (the amber promo bar, `color_05`).
- **One in-flight correction:** `layout_09`'s original "no scroll indicator" tell was contradicted by the tile (circular ←/→ arrows are present below the carousel); the card was retained for its genuine hard-clip/no-fade tell, the tell corrected, and confidence dropped to `medium`.
- **Snapshot caveat:** this is a point-in-time read of the 2026-06-04 captured tiles. The live site (and the promo bar in particular) changes; re-tile and re-mine to refresh.
