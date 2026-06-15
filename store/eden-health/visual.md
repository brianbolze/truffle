---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.0"
domain: eden.health
captured_at: 2026-06-15
source_capture: 2026-05-30
qa_status: clean
---

## Visual & brand impression

Eden reads as a controlled, systematized DTC brand. Its core is genuinely owned: a categorical per-product color palette [color_01], commissioned doctor portraits in branded scrubs [color_04], repeated card systems with shared anatomy [layout_02], a distraction-free quiz screen [layout_05], and bespoke brand-gradient data-vis widgets [iconography_01] — all anchored by a confident hero hierarchy [typography_01]. Finish thins in the secondary zones. Long-form text collapses to one weight in the footer and pharmacy disclosure [typography_10], blog cards ship without titles [typography_09], a borderless calculator floats on the hero [layout_07], and the four-up feature row runs ragged [layout_11]. Imagery breaks art direction wherever it isn't owned — user-submitted before/afters [color_08] and unprocessed video freeze-frames [color_11] sit beside generic stock icons [iconography_05] and dropped-in accreditation badges [iconography_07].

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: "homepage hero"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/homepage/tile-00-y00000.png"
  claim: "The hero establishes a clean three-level hierarchy — large display headline, small subtitle line, and tight nav/utility text — with enough weight and size contrast between levels to read instantly."
  visible_tells:
    - "\"Muscle growth tailored to you\" renders at a notably larger weight than the subtitle \"Look, feel and perform your best every day.\" below it"
    - "Nav links are visibly lighter and smaller than both body and headline, creating a third distinct level"
  confidence: high

- id: typography_09
  family: typography_hierarchy
  polarity: poor
  page_or_region: "homepage — guide/blog card row"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/homepage/tile-07-y08540.png"
  claim: "Blog card captions sit beneath lifestyle photos with no enlarged article title — the descriptive blurb and the small category pill are the only text levels, so the cards offer no display-level title to anchor scanning."
  visible_tells:
    - "Cards for \"Weight Loss\", \"Healthy Aging\", \"Hair Growth\", \"Women's Hormones\" show a small blurb line above a button-styled category pill, with no large headline above either"
    - "No bold or enlarged article title is visible; the strongest text element is the small pill label"
  confidence: high
  contrast_with: "store/eden-health/captures/2026-05-30/tiles/glp1/tile-02-y02440.png"

- id: typography_10
  family: typography_hierarchy
  polarity: poor
  page_or_region: "about — partner pharmacy disclosure block"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/about/tile-05-y06100.png"
  claim: "The partner pharmacy disclosure section uses a single undifferentiated text weight for heading, body, and bulleted address lines, collapsing three logical levels into one."
  visible_tells:
    - "\"Partner pharmacy information\" heading is barely heavier than the paragraph body that follows it"
    - "Bulleted pharmacy names (GoGoMeds, Precision, Enovex, AbsolutePharmacy) are set in the same size as surrounding sentence text, with only light bolding on the name portion to distinguish label from value"
  confidence: high
  contrast_with: "store/eden-health/captures/2026-05-30/tiles/homepage/tile-06-y07320.png"

- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: "homepage — product category cards (hero row)"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/homepage/tile-00-y00000.png"
  claim: "The three hero product cards (GLP-1, Sermorelin, NAD+) are a consistent card system: equal width, equal height, per-card colored background, product photography at the same scale and position, label and CTA in the same slot."
  visible_tells:
    - "All three cards share rounded corners, identical internal padding, and a \"LEARN MORE\" link in the same bottom-left position"
    - "Background colors (green, terracotta, blue) change per card while all structural slots hold position"
  confidence: high

- id: layout_05
  family: layout_composition_components
  polarity: strong
  page_or_region: "how_it_works — quiz/onboarding flow"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/how_it_works/tile-00-y00000.png"
  claim: "The quiz flow screen is extremely clean: centered logo, a single centered headline, and a stacked column of equal-width option tiles with consistent internal padding and uniform border treatment — the composition is entirely devoted to the selection task."
  visible_tells:
    - "Seven option tiles are visually identical: same width, same rounded-corner radius, same left-text alignment, same vertical padding"
    - "No decorative elements, images, or competing copy anywhere on the screen"
  confidence: high

- id: layout_07
  family: layout_composition_components
  polarity: mixed
  page_or_region: "homepage — BMI calculator / hero split"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/homepage/tile-01-y01220.png"
  claim: "The GLP-1 hero section breaks into three co-equal horizontal zones (photo + text, BMI tool, weight-prediction chart) but the BMI calculator card sits on a white surface against a white background with no visible boundary, making it float ambiguously and weakening section cohesion."
  visible_tells:
    - "The BMI card uses a white surface on a near-white background with no card edge"
    - "The weight-prediction green bar chart uses a different visual language from the BMI card beside it"
    - "The full-bleed woman photo bleeding up from above sets a composition the two calculator elements do not match"
  confidence: high
  contrast_with: "store/eden-health/captures/2026-05-30/tiles/glp1/tile-02-y02440.png"

- id: layout_11
  family: layout_composition_components
  polarity: poor
  page_or_region: "homepage — 'Completely online' 4-up feature section"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/homepage/tile-04-y04880.png"
  claim: "The four-column feature section mixes column content types — a doctor portrait, a phone UI mockup, an angled product photo, and a hand holding a green box — at inconsistent crop heights, so the row lacks structural parity and the bottom edge runs ragged."
  visible_tells:
    - "Column 2's phone UI mockup is taller than the provider portrait in column 1 and the injection product shot in column 3"
    - "Column 4's wide box-in-hand shot sits lower than the other three, creating a ragged bottom edge across the row"
  confidence: high

- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: "homepage hero — product card trio"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/homepage/tile-00-y00000.png"
  claim: "The hero uses three tightly controlled background colors — one per product card — creating a deliberate categorical palette that reads as a system rather than an accident."
  visible_tells:
    - "GLP-1 card sits on green"
    - "Sermorelin card on warm terracotta"
    - "NAD+ card on sky blue — three distinct hues, no card shares a color"
  confidence: high

- id: color_04
  family: color_brand_imagery
  polarity: strong
  page_or_region: "homepage — medical team portrait cards"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/homepage/tile-05-y06100.png"
  claim: "Doctor portraits are shot on consistent warm-white backgrounds, in teal-green scrubs or white coats with the 'eden' embroidered logo — a clearly commissioned, on-brand shoot tied to the brand green."
  visible_tells:
    - "Teal/green scrubs on multiple doctors, matching brand green"
    - "'eden' embroidered text visible on at least one coat"
    - "Consistent background tone and lighting across the visible cards in the carousel"
  confidence: high

- id: color_08
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "reviews — before/after customer grid"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/reviews/tile-02-y02440.png"
  claim: "Before/after transformation photos are user-submitted (varying lighting, phone snapshots) sitting alongside the polished brand palette — a common category pattern but a visible break from art direction."
  visible_tells:
    - "Varied indoor lighting and casual phone-photo framing across multiple cards"
    - "'Before/After' labels overlaid on informal photos"
    - "Green 'Lost X lbs' pill badge is brand-colored but sits on inconsistent photo backgrounds"
  confidence: high

- id: color_11
  family: color_brand_imagery
  polarity: poor
  page_or_region: "reviews — video testimonial thumbnails"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/reviews/tile-01-y01220.png"
  claim: "Video testimonial thumbnails are unprocessed freeze-frames — dark, low-contrast shots with a white play icon overlaid, no brand color framing, no consistent cropping, no graphic treatment marking them as owned content."
  visible_tells:
    - "Three dark video thumbnails side by side, each with a centered white play-circle icon"
    - "Backgrounds range from autumn foliage to a grey indoor setting"
    - "No color grade, border, or brand overlay unifies the frames"
  confidence: high
  contrast_with: "store/eden-health/captures/2026-05-30/tiles/glp1/tile-07-y08540.png"

- id: iconography_01
  family: iconography_illustration
  polarity: strong
  page_or_region: "homepage — BMI / progress UI widgets"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/homepage/tile-01-y01220.png"
  claim: "The inline data-vis widgets (weight-prediction bar chart and progress controls) are crafted with brand-gradient fills and a custom slider token — reading as bespoke product UI illustration, not stock chart components."
  visible_tells:
    - "The prediction bar chart uses a pink-to-green gradient fill matching the brand palette"
    - "A custom orange slider/needle token sits on the 'weight you could lose' control rather than a default UI element"
  confidence: high

- id: iconography_05
  family: iconography_illustration
  polarity: mixed
  page_or_region: "homepage — 'Cruelty Free / Eco Friendly' badge row"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/homepage/tile-06-y07320.png"
  claim: "The six ingredient-claim icons (rabbit, tree, leaf, beaker, atom, wheat) are serviceable outline icons but rely on recognizable stock archetypes with no visible Eden-specific customization — function without distinction."
  visible_tells:
    - "The rabbit and atom glyphs match widely-used generic outline icon sets"
    - "No brand-specific detailing or stroke-weight modification is visible on any of the six"
  confidence: high
  contrast_with: "store/eden-health/captures/2026-05-30/tiles/homepage/tile-02-y02440.png"

- id: iconography_07
  family: iconography_illustration
  polarity: mixed
  page_or_region: "about — accreditation badge cluster"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/about/tile-02-y02440.png"
  claim: "The NABP and 'ACCREDITED Compounding Pharmacy' badges appear as third-party raster lockups dropped in-line without visual unification, breaking the otherwise clean icon system."
  visible_tells:
    - "NABP seal and the 'ACCREDITED' rectangular lockup sit side-by-side at different sizes and background treatments"
    - "The badges' raster styling clashes with the clean monoline icons in the ingredient row directly below"
  confidence: medium
```

## Provenance

- **Tiles read.** Five signal pages from `captures/2026-05-30/tiles/` — `homepage` (9 tiles), `about` (7), `glp1` (10), `reviews` (7), `how_it_works` (1) — 34 native-resolution tiles total. The newest capture (`2026-06-03`) is product-detail pages only and carries no homepage, so the visual-system pages were tiled from `2026-05-30`.
- **QA gate.** `qa_status: clean` — all five `overview-480w.png` previews and spot-checked native tiles rendered fully: no modals/cookie banners, no grey or blank heros, no black media cards, no mid-animation reveals. Reviews video cards rendered as legible freeze-frames (not black). **No exclusions; no Tier-B browser re-render needed.**
- **Mining.** Blind fan-out via `skills/visual-evidence/mine.workflow.js` (run `wf_ffda3c85-b2b`): 4 family miners (Sonnet, tiles-only, no network) → judge (Opus). Miners produced 52 raw cards; the judge accepted 44 after pruning 8 (2 hard tile-contradictions, 6 cross-family duplicates).
- **Curation.** The 44 accepted cards were curated here to a representative **14** (the contract's "8–14 typical") balanced across the four families and strong/mixed/poor — ids and card text preserved verbatim from the judge. The fuller accepted set is recoverable from the run output if a deeper audit trail is wanted.
- **Caveat.** Point-in-time snapshot of the captured tiles; the live site changes. Judgments are of *visible visual state* only — no score, no business/clinical/copy read.
