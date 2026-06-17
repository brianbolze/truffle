---
schema_version: "1.0"
domain: directmeds.com
captured_at: 2026-06-17
source_capture: 2026-06-04
qa_status: clean
---

## Visual & brand impression

Direct Meds presents as a calm, light-blue medical-commerce template: large navy/cyan display type, rounded pale panels, dark navy pill CTAs, and repeated product-card systems carry most of the polish [typography_01][layout_01][layout_02][color_01]. The strongest pieces are the category grid and product carousel - both are legible, componentized, and easy to scan [layout_01][layout_02]. The brand signal is softer: stock lifestyle photography shifts from wellness smiles to fitness bodies to phone-shot testimonials, while product vials stay consistent but generic on white cards [color_03][color_04][color_05]. Detail finish is uneven: dense PDP/article copy and the large blank PDP rail make long-form pages feel less designed than the homepage modules [typography_05][layout_05]. Overall: coherent and approachable, with template-level discipline more than distinct identity.

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: homepage hero
  tile_path: store/directmeds-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png
  claim: "The homepage hero establishes a clear two-line display hierarchy: the first line is very large cyan, the second line is the same scale in navy, and the small grey support sentence sits far below as a tertiary tier."
  visible_tells:
    - "Look Younger. Feel Energized. uses oversized cyan type; Live Vibrantly. sits directly beneath at matching scale in navy."
    - "The support line is much smaller, grey, and separated by a large vertical gap."
  confidence: high
- id: typography_02
  family: typography_hierarchy
  polarity: strong
  page_or_region: all-solutions hero / category grid
  tile_path: store/directmeds-com/captures/2026-06-04/tiles/all_solutions/tile-00-y00000.png
  claim: "The all-solutions entry uses a tidy three-step hierarchy - small eyebrow, large centered page title, then image-card labels - so the reader can parse page purpose before entering the category grid."
  visible_tells:
    - "How Can We Help? appears as a small centered eyebrow above the much larger Online Prescription Weight Loss Solutions title."
    - "Category labels sit inside dark translucent bands on the image cards and read as a lower tier than the title."
  confidence: high
- id: typography_03
  family: typography_hierarchy
  polarity: strong
  page_or_region: pricing article lead
  tile_path: store/directmeds-com/captures/2026-06-04/tiles/pricing/tile-00-y00000.png
  claim: "The article page creates a readable editorial stack: a very large H1, a compact blue topic pill, date metadata, and numbered H2s that visibly step down from the headline."
  visible_tells:
    - "Understanding The Price Of Personalized Weight Loss Medications spans two large lines."
    - "The blue topic pill and date sit at a much smaller size below the H1."
    - "Numbered section headings like 1. Personalization Requires Precision and 2. Premium Ingredients are smaller than the H1 but heavier than body copy."
  confidence: high
- id: typography_04
  family: typography_hierarchy
  polarity: mixed
  page_or_region: weight-loss product carousel
  tile_path: store/directmeds-com/captures/2026-06-04/tiles/cat_weight_loss/tile-01-y01220.png
  claim: "The product-card typography is legible and repeatable, but name, price, and CTA rely on spacing more than type contrast; the dark CTA button becomes the dominant element on every card."
  visible_tells:
    - "Tirzepatide and Semaglutide names are large navy labels, while prices sit small and pale at the same horizontal level."
    - "Each View Product button is darker, wider, and visually heavier than both the product name and price."
  confidence: high
- id: typography_05
  family: typography_hierarchy
  polarity: mixed
  page_or_region: semaglutide PDP body
  tile_path: store/directmeds-com/captures/2026-06-04/tiles/pdp_semaglutide_inj/tile-00-y00000.png
  claim: "The PDP has clear section headings, but long medical paragraphs and repeated same-weight subheads make the page feel closer to a document than a designed purchase surface."
  visible_tells:
    - "How It Works, How To Take It, What Are The Results?, and Common Side Effects repeat the same heading treatment down the column."
    - "Multiple paragraph blocks run wide and dense between headings with little supporting visual structure."
  confidence: high
- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: all-solutions category grid
  tile_path: store/directmeds-com/captures/2026-06-04/tiles/all_solutions/tile-00-y00000.png
  claim: "The six category cards form the site's strongest component: equal-sized image tiles in a 3x2 grid, each with the same bottom overlay band, label alignment, rounded corners, and circular arrow control."
  visible_tells:
    - "Weight Loss / Body Composition, Anti-Aging / Longevity, and Muscle Recovery / Energy / Performance share equal widths and gutters across the top row."
    - "The second row repeats the same card shape, dark label band, and right-side white circular arrow."
  confidence: high
- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: weight-loss product carousel
  tile_path: store/directmeds-com/captures/2026-06-04/tiles/cat_weight_loss/tile-01-y01220.png
  claim: "The medication carousel is a disciplined commerce module: a fixed left intro panel, uniform rounded product cards, centered vial images, aligned names/prices, and identical full-width CTAs."
  visible_tells:
    - "The left Popular Weight Loss Medications panel stays fixed in width while product cards scroll horizontally."
    - "Tirzepatide and both Semaglutide cards share the same image zone, name/price row, and View Product pill."
  confidence: high
- id: layout_03
  family: layout_composition_components
  polarity: strong
  page_or_region: weight-loss informational split sections
  tile_path: store/directmeds-com/captures/2026-06-04/tiles/cat_weight_loss/tile-02-y02440.png
  claim: "The weight-loss page repeats a clean two-column content pattern: large image block on one side, headline/body/bullets/CTA on the other, then a pale stats band below."
  visible_tells:
    - "About Our Weight Loss Medications pairs a large cropped image and vial on the left with text, bullets, and a CTA cluster on the right."
    - "Typical Outcomes sits in a full-width pale-blue rounded band directly below the split section."
  confidence: high
- id: layout_04
  family: layout_composition_components
  polarity: mixed
  page_or_region: pricing article layout
  tile_path: store/directmeds-com/captures/2026-06-04/tiles/pricing/tile-00-y00000.png
  claim: "The article layout has a useful left table-of-contents rail and a clear reading column, but the page is visually sparse above the fold, with most of the right half left empty."
  visible_tells:
    - "A narrow Table of Content list anchors the left side while the article column begins near the center."
    - "The large H1 and body column occupy the middle; the far-right area is almost entirely white."
  confidence: high
- id: layout_05
  family: layout_composition_components
  polarity: poor
  page_or_region: semaglutide PDP
  tile_path: store/directmeds-com/captures/2026-06-04/tiles/pdp_semaglutide_inj/tile-00-y00000.png
  claim: "The PDP leaves a large empty right rail separated by a vertical rule while the product image, CTA, and dense content are compressed into the left and center columns."
  visible_tells:
    - "A vertical divider appears to the right of the text column, followed by a broad blank white area."
    - "The small product image and Get this medication button sit in a narrow left column while the main copy runs in a constrained middle column."
  confidence: high
- id: layout_06
  family: layout_composition_components
  polarity: mixed
  page_or_region: homepage video testimonial carousel
  tile_path: store/directmeds-com/captures/2026-06-04/tiles/homepage/tile-03-y03660.png
  claim: "The dark testimonial section has an intentional centered-card composition, but the side video tiles are heavily cropped at the edges, making the carousel feel more like a clipped media strip than a polished gallery."
  visible_tells:
    - "The central video-and-quote card is fully visible and aligned in the dark band."
    - "Adjacent video cards at left and right are cropped by the viewport, with faces cut off near the card edges."
  confidence: medium
- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: site-wide palette across hero, cards, and CTAs
  tile_path: store/directmeds-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png
  claim: "The visual system consistently uses a pale blue-white ground, dark navy type and CTA pills, and bright cyan accents, giving the homepage a calm clinical-commerce register."
  visible_tells:
    - "The hero background and category panel are pale blue; main type and buttons are dark navy."
    - "Cyan appears in the hero headline, logo wordmark accent, and small action icons."
  confidence: high
  contrast_with: store/directmeds-com/captures/2026-06-04/tiles/cat_weight_loss/tile-01-y01220.png
- id: color_02
  family: color_brand_imagery
  polarity: mixed
  page_or_region: homepage hero product render
  tile_path: store/directmeds-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png
  claim: "The hero product render is clean and on-brand, but it is small relative to the empty hero field, so the opening depends more on whitespace and type than on a memorable product image."
  visible_tells:
    - "A single NAD+ vial sits on the far right inside a faint circular pale-blue field."
    - "Most of the hero's right and center area remains white or near-white, with no supporting product environment."
  confidence: high
- id: color_03
  family: color_brand_imagery
  polarity: mixed
  page_or_region: all-solutions image cards
  tile_path: store/directmeds-com/captures/2026-06-04/tiles/all_solutions/tile-00-y00000.png
  claim: "The category grid is structurally consistent, but its imagery reads assembled from broad stock-health scenes with different lighting, crops, and subject styles."
  visible_tells:
    - "Cards mix a close-up smiling portrait, a nurse portrait, a group outdoors, a beach/vacation crop, an older couple, and a cropped aesthetic-treatment face."
    - "The dark overlay bands unify labels, but the underlying image color and setting shift sharply from card to card."
  confidence: high
- id: color_04
  family: color_brand_imagery
  polarity: strong
  page_or_region: product cards / medication renders
  tile_path: store/directmeds-com/captures/2026-06-04/tiles/cat_weight_loss/tile-01-y01220.png
  claim: "Medication packshots are the most consistent owned-looking image asset: blue-and-white vial labels, soft shadows, and centered placement repeat across cards."
  visible_tells:
    - "Tirzepatide and Semaglutide vials share blue label bands, centered white-card placement, and soft grey shadows."
    - "The same vial language recurs in the lower About Our Weight Loss Medications image."
  confidence: high
- id: color_05
  family: color_brand_imagery
  polarity: mixed
  page_or_region: testimonial video section
  tile_path: store/directmeds-com/captures/2026-06-04/tiles/homepage/tile-03-y03660.png
  claim: "The dark navy testimonial band creates a strong contrast break from the pale site palette, but the embedded video stills are low-fidelity and visually inconsistent with the cleaner product/card modules."
  visible_tells:
    - "The section background switches to deep navy with cyan heading type and a pale centered quote card."
    - "Video stills show different lighting, framing, and resolution, including close face crops and phone-camera quality."
  confidence: high
- id: color_06
  family: color_brand_imagery
  polarity: poor
  page_or_region: pricing blog hero thumbnail
  tile_path: store/directmeds-com/captures/2026-06-04/tiles/pricing/tile-00-y00000.png
  claim: "The pricing article thumbnail breaks the site's otherwise cool medical palette with a saturated orange field and bright polka-dot graphic language."
  visible_tells:
    - "The blog thumbnail uses a bright orange background with cyan, pink, black, and yellow dot graphics."
    - "That thumbnail sits beside a page otherwise dominated by white, navy, pale blue, and a single blue topic pill."
  confidence: high
  contrast_with: store/directmeds-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png
- id: color_07
  family: color_brand_imagery
  polarity: mixed
  page_or_region: weight-loss lifestyle imagery
  tile_path: store/directmeds-com/captures/2026-06-04/tiles/cat_weight_loss/tile-00-y00000.png
  claim: "The weight-loss page leans on bright outdoor lifestyle photography that feels upbeat and accessible, but the image language is generic and not tightly tied to the product renders."
  visible_tells:
    - "The hero image shows a smiling person outdoors with headphones; the About image shows another smiling person outdoors holding a bottle."
    - "Both photographs are green, sunlit lifestyle scenes, while nearby product renders remain isolated white-card packshots."
  confidence: high
- id: iconography_01
  family: iconography_illustration
  polarity: strong
  page_or_region: category-card action controls
  tile_path: store/directmeds-com/captures/2026-06-04/tiles/all_solutions/tile-00-y00000.png
  claim: "The category cards use a consistent circular arrow affordance that is easy to spot and repeats cleanly across all six cards."
  visible_tells:
    - "Each image card has a white circular button at the right side of the dark label band."
    - "The arrow glyph, circle size, and placement are consistent across both grid rows."
  confidence: high
- id: iconography_02
  family: iconography_illustration
  polarity: mixed
  page_or_region: how-it-works steps
  tile_path: store/directmeds-com/captures/2026-06-04/tiles/homepage/tile-02-y02440.png
  claim: "The step icons create a coherent process rhythm, but the symbols themselves are generic outline metaphors rather than a distinctive illustration system."
  visible_tells:
    - "Chat, pencil/edit, and package icons sit in matching pale-cyan circular badges beside the three steps."
    - "The icons share line weight and color, but read as standard UI symbols."
  confidence: high
- id: iconography_03
  family: iconography_illustration
  polarity: mixed
  page_or_region: product category rail
  tile_path: store/directmeds-com/captures/2026-06-04/tiles/homepage/tile-01-y01220.png
  claim: "The product-category rail provides useful pictorial scanning, but the icon set mixes small medical, fitness, pill, and figure metaphors without much custom character."
  visible_tells:
    - "Anti-Aging, Hair Regrowth, Muscle Recovery, Pain Relief, Skin, and Weight Loss each use a small dark line icon."
    - "The symbols vary from a clock-like mark to dumbbell, pill, bottles, and human figure while staying in a generic outline style."
  confidence: medium
- id: iconography_04
  family: iconography_illustration
  polarity: mixed
  page_or_region: ticker and trust affordances
  tile_path: store/directmeds-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png
  claim: "The top ticker repeats a small medical-symbol icon before every trust phrase, which reinforces the clinical theme but feels more like stock medical decoration than owned brand language."
  visible_tells:
    - "The same small dark medical icon appears before Convenient At-Home Delivery, Personalized Care Plans, and Transparent, All-Inclusive Pricing."
    - "The icon repeats mechanically across the ticker with no variation or additional brand treatment."
  confidence: high
- id: iconography_05
  family: iconography_illustration
  polarity: strong
  page_or_region: weight-loss hero and bullet lists
  tile_path: store/directmeds-com/captures/2026-06-04/tiles/cat_weight_loss/tile-00-y00000.png
  claim: "Cyan checkmarks are used consistently as list markers in the weight-loss hero and later content blocks, giving benefit copy a clear, lightweight visual cue."
  visible_tells:
    - "Three cyan checkmarks mark No Hidden Fees, No Membership Fees, and All-Inclusive Pricing under the hero headline."
    - "The same cyan checkmark language recurs in the About Our Weight Loss Medications bullets on the next tile."
  confidence: high
  contrast_with: store/directmeds-com/captures/2026-06-04/tiles/cat_weight_loss/tile-02-y02440.png
```

## Provenance

Tiles read: homepage (9) + all_solutions (5) + pricing (4) + cat_weight_loss (8) + pdp_semaglutide_inj (3) from `captures/2026-06-04/tiles/` - all 29 active, no exclusions, no Tier-B re-render. QA caveat: the cached full-page stitches repeat the sticky header across lower scroll positions and carry a small chat affordance near page bottoms; cards do not use those artifacts as design evidence. Method caveat: the normal `skills/visual-evidence/mine.workflow.js` runner was not exposed in this Codex session, so this file was authored as a tile-only manual pass with no dossier or live-web read. Snapshot caveat: reflects the 2026-06-04 capture; the live site changes.
