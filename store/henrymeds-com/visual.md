---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.0"
domain: henrymeds.com
captured_at: 2026-06-16
source_capture: 2026-06-04
qa_status: clean
---

## Visual & brand impression

Henry presents as a controlled, single-anchor brand: one deep forest green plus warm cream carried across every band, footer, and product panel [color_01], extended into sage product surfaces [color_05] and on-label green packaging that gives the medications real branded identity [iconography_04][iconography_05]. The component system is disciplined — the three-step process [layout_01], category pills [layout_02], FAQ accordion [layout_03], and footer [layout_04] repeat without drift, and the type hierarchy reads cleanly from hero to dark bands [typography_01][typography_03]. Where it slips is the supporting layer: generic off-the-shelf outline icons [iconography_02], mixed-register step graphics [iconography_01], uneven stock photography [color_03][color_06], a compressed product-page type scale [typography_07], and small unresolved details — a stray gold footer accent [color_02] and an unbalanced 3+2 grid [layout_07].

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: "homepage hero"
  tile_path: "store/henrymeds-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"
  claim: "The hero runs a clean three-level hierarchy — small eyebrow label, large serif display headline, smaller sans body line — with enough size/weight contrast between each level to read instantly."
  visible_tells:
    - "Tiny eyebrow 'No Insurance. No Waiting Rooms.' sits above the headline at a much smaller scale"
    - "Serif display headline 'Your Health, Simplified.' is substantially larger and heavier than the line below"
    - "Sans body 'Affordable, personalized care from the comfort of your home.' drops to a noticeably smaller, lighter weight"
  confidence: high

- id: typography_02
  family: typography_hierarchy
  polarity: strong
  page_or_region: "how_it_works / homepage — step cards"
  tile_path: "store/henrymeds-com/captures/2026-06-04/tiles/how_it_works/tile-00-y00000.png"
  claim: "Within each step card the bold title ('Medical Forms', 'Meet with a Healthcare Provider', 'Receive Medication') sits visibly larger and heavier than the descriptor line beneath, giving a tight two-level within-card read repeated identically across all three cards."
  visible_tells:
    - "Card titles in medium-bold weight"
    - "Descriptor lines beneath each title clearly smaller and lighter grey"
    - "Same treatment on all three cards"
  confidence: high
  contrast_with: "store/henrymeds-com/captures/2026-06-04/tiles/trt/tile-02-y02440.png"

- id: typography_03
  family: typography_hierarchy
  polarity: strong
  page_or_region: "homepage — dark testimonial band"
  tile_path: "store/henrymeds-com/captures/2026-06-04/tiles/homepage/tile-01-y01220.png"
  claim: "The bold serif heading 'Patients Love Our Personalized Care' in cream-white on the deep green band reads cleanly with no contrast failure — color and weight flip together to hold legibility."
  visible_tells:
    - "Large serif heading in cream against deep forest green, no halation"
    - "Small gold 'View Trustpilot Reviews' link below confirms a clear two-level read on the dark surface"
  confidence: high

- id: typography_04
  family: typography_hierarchy
  polarity: strong
  page_or_region: "values page — icon-led sub-section heads"
  tile_path: "store/henrymeds-com/captures/2026-06-04/tiles/values/tile-00-y00000.png"
  claim: "The values page shows a working three-tier scale: large serif 'Our Values' heading, mid-tier sub-heads ('Transparent', 'Proven', 'Affordable'), and small body copy under each — each level visibly distinct in size, the three sub-heads matched to one another."
  visible_tells:
    - "'Our Values' is the largest text on the right column"
    - "The three sub-heads are clearly smaller than the heading but larger/bolder than the body paragraphs"
    - "Sub-heads typeset at equal size across the three columns"
  confidence: high

- id: typography_05
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "wm_semaglutide — 'What is Compounded Semaglutide?' section"
  tile_path: "store/henrymeds-com/captures/2026-06-04/tiles/wm_semaglutide/tile-04-y04880.png"
  claim: "Below the serif heading the body paragraphs are set quite small and dense, and one mid-paragraph bolded sentence ('Henry Meds exclusively works with licensed compounding pharmacies in the United States.') introduces a rogue emphasis level that reads as a pseudo-subhead not used elsewhere in the system."
  visible_tells:
    - "Multiple lines of small body text under the heading"
    - "One bolded sentence stands out mid-block as a faux sub-head"
  confidence: medium
  contrast_with: "store/henrymeds-com/captures/2026-06-04/tiles/how_it_works/tile-00-y00000.png"

- id: typography_06
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "trt page — 'What Henry Offers' section"
  tile_path: "store/henrymeds-com/captures/2026-06-04/tiles/trt/tile-02-y02440.png"
  claim: "The 'What Henry Offers' block leans on inline bold weight rather than a size tier — the product name and price ('Starting at $129 per Month...') are bolded within body text with no distinct sub-heading level between the section title and the prose, making it harder to scan than the card-based sections elsewhere."
  visible_tells:
    - "Section title 'What Henry Offers' at standard section-head size"
    - "Product name + price carried by bold weight inside a body block at nearly body size"
    - "No intermediate sub-head level"
  confidence: medium
  contrast_with: "store/henrymeds-com/captures/2026-06-04/tiles/how_it_works/tile-00-y00000.png"

- id: typography_07
  family: typography_hierarchy
  polarity: poor
  page_or_region: "trt — feature sub-heads + body under 'Transformation with TRT'"
  tile_path: "store/henrymeds-com/captures/2026-06-04/tiles/trt/tile-01-y01220.png"
  claim: "Under each feature bullet ('Medically Supervised Testosterone Therapy', 'Online Access to Healthcare Providers', 'Professional, Affordable Care') the descriptive sentence is set so small relative to the heading that it reads as fine print rather than supporting copy — a compressed jump in the scale."
  visible_tells:
    - "Bold-but-modest sub-head labels"
    - "Descriptive lines beneath sit at a markedly smaller size, hard to read at page scale"
  confidence: medium
  contrast_with: "store/henrymeds-com/captures/2026-06-04/tiles/values/tile-00-y00000.png"

- id: typography_08
  family: typography_hierarchy
  polarity: strong
  page_or_region: "footer — disclaimer de-emphasis (all pages)"
  tile_path: "store/henrymeds-com/captures/2026-06-04/tiles/homepage/tile-02-y02440.png"
  claim: "The legal disclaimer block is set visibly smaller than the nav-link text above it, functioning as an intentional bottom tier that flags boilerplate without disturbing the rest of the scale, and it holds at the same treatment on every footer captured."
  visible_tells:
    - "Disclaimer paragraph measurably smaller than the footer nav link text"
    - "Consistent across homepage, how_it_works, values, trt, and wm_semaglutide footers"
  confidence: high

- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: "homepage + how_it_works — 3-step 'How Henry Works' component"
  tile_path: "store/henrymeds-com/captures/2026-06-04/tiles/how_it_works/tile-00-y00000.png"
  claim: "The three-step process is a genuine reusable component — equal-width rounded cards, numbered badge on top, illustration zone, bold label, body line in fixed vertical order — and it reappears with the same structure on both the homepage and the standalone How It Works page."
  visible_tells:
    - "Three equal cards, numbered badges 1/2/3 centered above each"
    - "Each card: illustration zone, bold label, short body, same order"
    - "Same component recurs on the homepage hero region with identical proportions"
  confidence: high
  contrast_with: "store/henrymeds-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"

- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: "site-wide — treatment category pill/link component"
  tile_path: "store/henrymeds-com/captures/2026-06-04/tiles/how_it_works/tile-00-y00000.png"
  claim: "The 'We Can Help You With' pill-links (circular cropped photo + label + green arrow-circle) are a consistent navigational component reused on the how-it-works page and the homepage with the same shape, sizing, and affordance."
  visible_tells:
    - "Each pill: circular cropped portrait at left, label text, green filled arrow-circle at right"
    - "Layout wraps to a 3+2 pattern with consistent left-edge alignment"
  confidence: high
  contrast_with: "store/henrymeds-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"

- id: layout_03
  family: layout_composition_components
  polarity: strong
  page_or_region: "site-wide — FAQ accordion"
  tile_path: "store/henrymeds-com/captures/2026-06-04/tiles/how_it_works/tile-01-y01220.png"
  claim: "The FAQ accordion is a fully consistent component — hairline separator per row, left-aligned question, plus-icon flush right — repeated without drift across the homepage, how-it-works, TRT, and semaglutide pages."
  visible_tells:
    - "Hairline rule between rows, plus-icon flush right on every item"
    - "Same component appears on multiple pages with matched leading and spacing"
  confidence: high
  contrast_with: "store/henrymeds-com/captures/2026-06-04/tiles/wm_semaglutide/tile-04-y04880.png"

- id: layout_04
  family: layout_composition_components
  polarity: strong
  page_or_region: "site-wide — footer"
  tile_path: "store/henrymeds-com/captures/2026-06-04/tiles/homepage/tile-02-y02440.png"
  claim: "The dark-green footer is a disciplined repeated component: cream contact card at left, divider-separated nav column at right, trust badges in a centered row, legal block, and an oversized faint wordmark as a background graphic — identical structure on every page captured."
  visible_tells:
    - "Cream contact card (logo, email, phone, Get Started button) at a fixed left position"
    - "Single nav column with divider rules at right, trust-badge row centered below, giant 'Henry' wordmark watermark behind"
  confidence: high

- id: layout_05
  family: layout_composition_components
  polarity: strong
  page_or_region: "trt + wm_semaglutide — subscription benefit icon bar"
  tile_path: "store/henrymeds-com/captures/2026-06-04/tiles/trt/tile-00-y00000.png"
  claim: "The four-item 'subscription includes' bar (icon + short label, evenly spaced across the full container on a pale lilac strip) is reused identically on both the TRT and semaglutide product pages, a shared benefit-bar component."
  visible_tells:
    - "Four icon+label cells at equal spacing across the full width"
    - "Identical lilac strip and layout on the semaglutide hero"
  confidence: high
  contrast_with: "store/henrymeds-com/captures/2026-06-04/tiles/wm_semaglutide/tile-00-y00000.png"

- id: layout_06
  family: layout_composition_components
  polarity: mixed
  page_or_region: "homepage + values — hero photo edge-bleed asymmetry"
  tile_path: "store/henrymeds-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"
  claim: "The split-column heroes let the photo bleed to the viewport edge while the text column keeps conservative inset padding, creating an asymmetric weight where the text sits low against a large image — a recurring pattern (homepage and values) that reads as a system choice but sits in tension with the fully-contained sections below."
  visible_tells:
    - "Homepage photo occupies the right ~55% and bleeds to the edge; left text column has generous whitespace above it"
    - "Values hero repeats the same edge-bleed photo + inset text, while the contained value-icon columns below have gutters"
  confidence: medium
  contrast_with: "store/henrymeds-com/captures/2026-06-04/tiles/values/tile-00-y00000.png"

- id: layout_07
  family: layout_composition_components
  polarity: mixed
  page_or_region: "homepage + how_it_works — treatment pills 3+2 grid"
  tile_path: "store/henrymeds-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"
  claim: "The five treatment pills wrap into a 3+2 pattern where the bottom row is left-aligned and does not center under the top row, leaving a noticeable empty gap at right that reads as an unfinished grid decision."
  visible_tells:
    - "Bottom row of two pills left-aligned, unbalanced empty space at right"
    - "Same misalignment recurs on the how-it-works page with the same 3+2 treatment"
  confidence: medium
  contrast_with: "store/henrymeds-com/captures/2026-06-04/tiles/how_it_works/tile-00-y00000.png"

- id: layout_08
  family: layout_composition_components
  polarity: mixed
  page_or_region: "trt — 'Transformation with TRT' section seam"
  tile_path: "store/henrymeds-com/captures/2026-06-04/tiles/trt/tile-01-y01220.png"
  claim: "The left-bleed transformation photo abuts the bottom of the step-cards section above it with no separating whitespace or rule, so the two content blocks visually merge at the seam, and the right text+bullet column floats without a baseline shared with the image."
  visible_tells:
    - "Man's portrait top edge crops into the step-card row above with no gap"
    - "Three checkmark bullets float at right with no visible shared column baseline"
  confidence: medium

- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: "site-wide — green + cream two-tone system"
  tile_path: "store/henrymeds-com/captures/2026-06-04/tiles/homepage/tile-01-y01220.png"
  claim: "A single deep forest green plus a warm cream form a tightly disciplined two-tone system — green is the sole chromatic anchor for every major band and footer, cream is the held page/card canvas, and no competing accent hue (blue, purple, red) appears anywhere in the set."
  visible_tells:
    - "Full-bleed forest-green testimonial band and footer repeat the exact same green across all pages"
    - "Cream canvas and cream cards (not pure white) recur on homepage, how_it_works, and values"
    - "Green-on-cream contrast is the primary compositional move on every page; no secondary brand color present"
  confidence: high
  contrast_with: "store/henrymeds-com/captures/2026-06-04/tiles/how_it_works/tile-00-y00000.png"

- id: color_02
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "footer nav dividers — all pages"
  tile_path: "store/henrymeds-com/captures/2026-06-04/tiles/homepage/tile-02-y02440.png"
  claim: "A muted gold/yellow appears only on some footer nav divider rules and nowhere else — and it is applied inconsistently (gold under some links, pale grey under others within the same column), so it reads as an unresolved leftover rather than a deliberate third brand accent."
  visible_tells:
    - "Thin gold-yellow rules under several footer nav links, pale/grey rules under others in the same list"
    - "Same uneven gold recurs across multiple footers; no CTA, heading, or icon ever uses the gold"
  confidence: medium
  contrast_with: "store/henrymeds-com/captures/2026-06-04/tiles/how_it_works/tile-01-y01220.png"

- id: color_03
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "homepage / trt / wm_semaglutide — testimonial portrait mosaic"
  tile_path: "store/henrymeds-com/captures/2026-06-04/tiles/homepage/tile-01-y01220.png"
  claim: "The six-portrait mosaic strip on the green band mixes white-balance and lighting conditions that do not cohere — some warm, some cool, some indoor, some outdoor — and the identical strip is reused across pages without re-curation, suggesting assembled rather than directed photography."
  visible_tells:
    - "Six cropped portraits with visibly different exposure/white-balance side by side; far-right portrait reads markedly more orange"
    - "Same mosaic repeats unchanged on trt and wm_semaglutide testimonial bands"
  confidence: high
  contrast_with: "store/henrymeds-com/captures/2026-06-04/tiles/trt/tile-02-y02440.png"

- id: color_04
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "values page — provider portrait"
  tile_path: "store/henrymeds-com/captures/2026-06-04/tiles/values/tile-00-y00000.png"
  claim: "The values hero portrait of a smiling provider is competent but generic and slightly off-palette — the light teal/blue scrubs are the only cool tone in the whole set, pulling away from the warm green-and-cream system, and the framing matches standard healthcare-stock conventions."
  visible_tells:
    - "Provider fills the left half against a plain light background"
    - "Light teal/blue scrubs are the lone cool hue in the set"
    - "Three-quarter crop and lighting read as conventional healthcare stock"
  confidence: medium
  contrast_with: "store/henrymeds-com/captures/2026-06-04/tiles/trt/tile-01-y01220.png"

- id: color_05
  family: color_brand_imagery
  polarity: strong
  page_or_region: "wm_semaglutide — sage product spotlight panel"
  tile_path: "store/henrymeds-com/captures/2026-06-04/tiles/wm_semaglutide/tile-03-y03660.png"
  claim: "The oral-semaglutide spotlight sits on a soft sage panel that is a lighter tint of the brand's forest green — a deliberate on-palette surface that ties the product visual into the color system rather than cutting to plain white, while the surrounding canvas stays cream so the panel reads as a contained brand accent."
  visible_tells:
    - "Pale sage-green background swatch behind the Henry-branded oral tablet bottle"
    - "Sage is a clear lighter tint of the primary green; surrounding page remains cream"
  confidence: high

- id: color_06
  family: color_brand_imagery
  polarity: poor
  page_or_region: "trt — 'Transformation with TRT' lifestyle photo"
  tile_path: "store/henrymeds-com/captures/2026-06-04/tiles/trt/tile-01-y01220.png"
  claim: "The transformation photo (man in a grey t-shirt against a blurred green-grey outdoor background) carries no relationship to the brand palette — its green is ambient, not curated — and the standard mid-shot crop is indistinguishable from generic wellness stock."
  visible_tells:
    - "Grey shirt against an unfocused neutral background; no brand color in the frame"
    - "Conventional mid-shot portrait with no compositional or color-treatment distinction"
  confidence: medium

- id: iconography_01
  family: iconography_illustration
  polarity: mixed
  page_or_region: "homepage — 'How Henry Works' step graphics"
  tile_path: "store/henrymeds-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"
  claim: "The three step graphics mix registers — a flat UI form mock-up for step 1, a photographic provider framed in a phone for step 2, a branded kraft prop bag for step 3 — three different graphic vocabularies side by side with no unifying illustration treatment, reading as assembled rather than a designed system."
  visible_tells:
    - "Step 1 flat form screenshot, step 2 photo-in-device frame, step 3 physical prop bag — three registers in one row"
  confidence: high
  contrast_with: "store/henrymeds-com/captures/2026-06-04/tiles/how_it_works/tile-00-y00000.png"

- id: iconography_02
  family: iconography_illustration
  polarity: poor
  page_or_region: "values + trt — outline glyph icon rows"
  tile_path: "store/henrymeds-com/captures/2026-06-04/tiles/values/tile-00-y00000.png"
  claim: "The decorative outline glyphs are generic and off-the-shelf — the values row (magnifying glass, heart-with-checkmark, coin) and the TRT 'subscription includes' strip (plan, medication, truck, purchase) are the same small teal outline style with no custom detailing or brand inflection, indistinguishable from a default icon library."
  visible_tells:
    - "Three teal outline value icons are plain standard symbols at small scale"
    - "TRT benefit strip uses identically-weighted teal outline icons; the shipping glyph is a generic truck silhouette"
  confidence: high
  contrast_with: "store/henrymeds-com/captures/2026-06-04/tiles/trt/tile-00-y00000.png"

- id: iconography_03
  family: iconography_illustration
  polarity: mixed
  page_or_region: "site-wide — category pill arrow glyph"
  tile_path: "store/henrymeds-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png"
  claim: "The category pills pair a circular model photo with a green filled circle-arrow on every instance — functional and consistent, but the arrow glyph is a bare generic directional reused everywhere, so the pattern does the navigation work with no distinctive icon character; the same configuration repeats on the how-it-works page (template reuse, not tailored illustration)."
  visible_tells:
    - "Each pill: circular cropped portrait + small green filled circle-arrow at the right edge"
    - "The same arrow glyph and pill configuration recur on the how-it-works category cards"
  confidence: high
  contrast_with: "store/henrymeds-com/captures/2026-06-04/tiles/how_it_works/tile-00-y00000.png"

- id: iconography_04
  family: iconography_illustration
  polarity: strong
  page_or_region: "wm_semaglutide + how_it_works — branded product/packaging imagery"
  tile_path: "store/henrymeds-com/captures/2026-06-04/tiles/wm_semaglutide/tile-04-y04880.png"
  claim: "Product and packaging carry consistent on-label branding rather than generic stock — the Semaglutide injection vial, oral-tablet bottle, and kraft delivery bag all apply the brand's dark-green cap/panel and 'Henry' wordmark, extending the brand color into tangible product identity across SKUs."
  visible_tells:
    - "Semaglutide vial has a dark-green cap, green base panel, 'Henry' wordmark, and 'RX ONLY' label"
    - "Oral-tablet bottle shares the same dark-green lid and white label system; how-it-works delivery bag is a kraft bag with the green 'Henry' wordmark"
  confidence: high
  contrast_with: "store/henrymeds-com/captures/2026-06-04/tiles/values/tile-00-y00000.png"

- id: iconography_05
  family: iconography_illustration
  polarity: strong
  page_or_region: "wm_semaglutide — oral-tablet floating-pill product shot"
  tile_path: "store/henrymeds-com/captures/2026-06-04/tiles/wm_semaglutide/tile-03-y03660.png"
  claim: "The oral-tablet bottle is styled with white pills suspended in mid-air above the bottle on the sage card — a composed, art-directed product image rather than a plain white-background pharmaceutical shot."
  visible_tells:
    - "Multiple white pills visually floating above the open bottle against the soft green card, an intentionally composed shot"
  confidence: high

- id: iconography_06
  family: iconography_illustration
  polarity: mixed
  page_or_region: "footer — third-party trust badge cluster (all pages)"
  tile_path: "store/henrymeds-com/captures/2026-06-04/tiles/homepage/tile-02-y02440.png"
  claim: "The three footer trust badges come from divergent design vocabularies — an illustrated US-map seal, a dark LegitScript hexagon with metallic type, and a thin-line HIPAA caduceus — so the cluster reads as a mixed-polish band of borrowed third-party marks rather than a unified set."
  visible_tells:
    - "US-map 'Compounded by Licensed Pharmacies' badge is illustrated; LegitScript is a dark polygon; HIPAA uses a traditional caduceus line mark — three different styles in one row"
  confidence: high
```

## Provenance

- **Tiles read.** 23 native-resolution tiles across five pages from `captures/2026-06-04/tiles/`: `homepage/` (4), `how_it_works/` (3), `values/` (4), `trt/` (5), `wm_semaglutide/` (7), plus each page's `overview-480w.png`. Tier-A only — sliced from the cached Firecrawl payloads; **no Firecrawl spend, no Tier-B browser re-render**.
- **QA note.** `clean` — every page rendered without modal/cookie/grey-hero/lazy-load contamination, so no tiles were excluded. One synthesis-time **attribution** correction (not a capture issue): three mined cards mis-cited `wm_semaglutide/tile-05` (the footer) for the "Compounded Oral Semaglutide" sage promo. The sage panel + floating-pill bottle actually render on `tile-03`; `color_05` and `iconography_05` were re-pointed there, and a "poor overflow" layout card was dropped — `tile-03` shows the floating pills are intentional art-direction (the same element `iconography_05` reads as deliberate), not a layout defect.
- **Snapshot caveat.** A point-in-time read of the 2026-06-04 capture; henrymeds.com changes, so these tells describe the captured tiles, not necessarily the live site.
