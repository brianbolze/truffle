---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.0"
domain: eden.health
captured_at: 2026-06-16
source_capture: 2026-05-30
qa_status: clean
---

## Visual & brand impression

Eden reads as a controlled, systematized DTC brand with a genuinely owned core. A per-category color rule carries cleanly from hero to carousel to pricing to CTA [color_01][color_02][color_03], anchored by a confident hero hierarchy [typography_01] and disciplined, reusable components — the product-card grid [layout_01], FAQ accordion [layout_02], pricing carousel [layout_04], and a distraction-free quiz [layout_05]. Product photography is a styled brand system, not stock [iconography_02][iconography_03], and a dark footer closes every page consistently [color_04]. Finish thins toward the page bottoms and the social proof: the About pharmacy block has no hierarchy or containment [typography_06][layout_12], the leadership grid runs asymmetric [layout_07], and imagery breaks art direction wherever it isn't owned — user before/afters [color_06], off-palette data widgets [color_09], decorative charts [iconography_05], default play buttons [iconography_06].

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: "Homepage hero"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/homepage/tile-00-y00000.png"
  claim: "The hero establishes a clear two-level hierarchy: a large bold serif display head ('Muscle growth tailored to you') sits distinctly above a smaller, lighter descriptor line, readable at a glance without relying on color."
  visible_tells:
    - "Display head is notably larger and heavier than the descriptor line beneath it"
    - "Subhead 'Look, feel and perform your best every day' uses a lighter weight and tighter size, creating visible separation"
  confidence: high

- id: typography_02
  family: typography_hierarchy
  polarity: strong
  page_or_region: "GLP-1 page — 3-step section"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/glp1/tile-02-y02440.png"
  claim: "The three-step cards use a consistent three-level type hierarchy — tiny 'STEP' caps label, oversized numeral, bold heading, then regular body — making reading order obvious within each card."
  visible_tells:
    - "Jumbo numerals 1/2/3 set at display scale beside 'STEP' in tiny caps"
    - "Card headings are bold at mid-size; body copy below is clearly smaller and regular-weight"
  confidence: high

- id: typography_03
  family: typography_hierarchy
  polarity: strong
  page_or_region: "How-it-works onboarding quiz"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/how_it_works/tile-00-y00000.png"
  claim: "The quiz screen pairs a prominent heavyweight question head ('What is your primary health goal?') with uniform regular-weight option labels — clean two-level contrast against a near-white field."
  visible_tells:
    - "Question text is substantially larger and darker than every option-row label"
    - "All seven answer options use identical weight and size — no false hierarchy within the list"
  confidence: high

- id: typography_04
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "Homepage — section heads across scroll"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/homepage/tile-04-y04880.png"
  claim: "Section heads are visually consistent (centered, medium-large, same weight) but not differentiated from one another — 'Completely online on your schedule' and 'Trusted by leading medical experts' render near-identically, removing any implied priority between sections."
  visible_tells:
    - "Both section heads use the same centered, medium-bold treatment at similar point size"
    - "No size step-down or weight shift distinguishes a primary from a secondary section head"
  confidence: medium
  contrast_with: "store/eden-health/captures/2026-05-30/tiles/homepage/tile-00-y00000.png"

- id: typography_05
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "Reviews page — stat callout"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/reviews/tile-00-y00000.png"
  claim: "The '98%' stat is rendered at a dramatic display size for impact, but the supporting descriptor beside it is proportionally tiny and light grey, creating an imbalanced pair where the clause nearly disappears."
  visible_tells:
    - "'98%' is set at a dramatically large size relative to surrounding text"
    - "The supporting clause 'of Eden members reported weight loss during treatment' is very small light-grey text that visually recedes beside the statistic"
  confidence: medium

- id: typography_06
  family: typography_hierarchy
  polarity: poor
  page_or_region: "About page — footer legal block"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/about/tile-05-y06100.png"
  claim: "The 'Partner pharmacy information' label and its dense paragraph + bulleted addresses are set at nearly identical weight and size on a light-sage band, with no heading weight contrast — the heading is functionally invisible as a landmark."
  visible_tells:
    - "'Partner pharmacy information' is not meaningfully bolder or larger than the paragraph below it"
    - "Bulleted pharmacy addresses use the same weight as the heading, removing hierarchy across the block"
  confidence: high

- id: typography_07
  family: typography_hierarchy
  polarity: poor
  page_or_region: "Homepage — blog/article card row"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/homepage/tile-07-y08540.png"
  claim: "Article cards in the 'Your guide to health and wellness' row show almost no hierarchy between the small body description and the category tag below it — both render at a similar small, low-contrast size."
  visible_tells:
    - "Description line and category label ('Weight Loss', 'Hair Growth') read at near-identical small size"
    - "No bold or size distinction separates the description from the category tag"
  confidence: medium

- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: "Homepage hero — product card grid"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/homepage/tile-00-y00000.png"
  claim: "The hero uses a tight 3-column card grid for featured treatments with consistent padding, corner radius, and inline 'Learn more' placement, plus a secondary row of four smaller product cards beneath — a well-built repeatable card system."
  visible_tells:
    - "Three equal-width colored product cards (GLP-1, Sermorelin, NAD+) with identical interior padding, rounded corners, and 'Learn more' links at the same vertical position"
    - "A second row of four uniform white mini-cards (MIC+B12, Hormone Therapy, Glutathione, Skin Care) aligned to the same grid"
  confidence: high

- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: "Homepage / GLP-1 — FAQ accordion"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/homepage/tile-06-y07320.png"
  claim: "FAQ accordion rows are a clean, consistent component: full-width rounded cards with left-aligned question text and a right-aligned dark circular '+' toggle, identical across instances and pages."
  visible_tells:
    - "Four accordion rows with rounded-rectangle outlines, uniform height, consistent horizontal padding, and identical dark-circle '+' icons flush right"
  confidence: high
  contrast_with: "store/eden-health/captures/2026-05-30/tiles/glp1/tile-07-y08540.png"

- id: layout_03
  family: layout_composition_components
  polarity: strong
  page_or_region: "Homepage — attribute badge row"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/homepage/tile-06-y07320.png"
  claim: "Six attribute badges (Cruelty Free, Eco Friendly, Paraben Free, Silicone Free, Sulphate Free, Gluten Free) sit in an even 6-column grid, each a rounded-square white card with centered icon and two-line label — executed cleanly with no alignment breaks."
  visible_tells:
    - "Six identical rounded-square tiles at equal width and height, icons vertically centered, labels centered beneath in matching type"
  confidence: high

- id: layout_04
  family: layout_composition_components
  polarity: strong
  page_or_region: "GLP-1 page — medication pricing carousel"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/glp1/tile-01-y01220.png"
  claim: "The medication pricing row uses a consistent card component (product name, price, product image, 'Important safety information' link) replicated cleanly across four items, with the first card filled brand-blue to mark it as the highlighted option."
  visible_tells:
    - "Four side-by-side cards — Personalized GLP-1 (filled blue), Compounded Semaglutide, Compounded Tirzepatide, Ozempic — each with matching internal structure and equal card height"
    - "Price line sits in the same position on every card; 'Important safety information' link repeats at the same bottom anchor"
  confidence: high

- id: layout_05
  family: layout_composition_components
  polarity: strong
  page_or_region: "How it works — onboarding quiz options"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/how_it_works/tile-00-y00000.png"
  claim: "The quiz step uses a disciplined single-column stack of option rows — each a full-width rounded rectangle of consistent height, corner radius, and left-aligned label — a clean, uncluttered form component."
  visible_tells:
    - "Seven full-width rounded-rectangle option rows (Lose weight, Maintain my weight, Better energy & mood, etc.) at equal height and spacing, all left-aligned with no icons or visual noise"
  confidence: high

- id: layout_06
  family: layout_composition_components
  polarity: strong
  page_or_region: "Footer — 4-column nav (site-wide)"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/about/tile-05-y06100.png"
  claim: "The dark footer holds a clean multi-column link layout (Popular, Company, More from Eden, Legal) with consistent gutters, small-cap section headings, and a contained email-signup unit on the left."
  visible_tells:
    - "Four visually separated link columns at even widths with uniform small-cap headings"
    - "Email input + Submit button contained as a self-contained unit in the left column beneath the wordmark"
  confidence: high

- id: layout_07
  family: layout_composition_components
  polarity: mixed
  page_or_region: "About page — leadership team grid"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/about/tile-03-y03660.png"
  claim: "The leadership grid breaks its own rhythm: three circular portraits sit in an even top row, but the remaining two are centered on a second row rather than aligned to the column edges, leaving an unresolved asymmetry."
  visible_tells:
    - "Top row: three circular portraits in even columns; second row: two circular portraits centered, not aligned to the outer columns"
    - "The two rows do not share a common column grid"
  confidence: high

- id: layout_08
  family: layout_composition_components
  polarity: mixed
  page_or_region: "Homepage — BMI calculator / interactive row"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/homepage/tile-01-y01220.png"
  claim: "The interactive row combines three distinct zones (empty BMI form panel, floating-pills product image, results chart) of unbalanced density — the sparse form showing a placeholder '0' leaves a dead zone beside a busier results card."
  visible_tells:
    - "Left form panel shows a large '0' output with sparse height/weight inputs and a 'Calculate BMI' button"
    - "Right card crams a tall green bar chart and a weight slider into the same card height — the row reads unresolved at its rest state"
  confidence: medium

- id: layout_09
  family: layout_composition_components
  polarity: mixed
  page_or_region: "Homepage — two-up promo cards (Age with confidence / Rejuvenate your skin)"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/homepage/tile-03-y03660.png"
  claim: "The two promo cards share corner radius and CTA placement but treat text-over-image contrast differently — the green card sets white 'Rejuvenate your skin' text directly over a light hand-and-product photo with no scrim, risking legibility against the lighter areas."
  visible_tells:
    - "Left tan card: dark 'Age with confidence' text on a solid background, high contrast"
    - "Right green card: white headline over a photographed hand holding a white bottle, no overlay scrim where the photo lightens"
  confidence: medium

- id: layout_10
  family: layout_composition_components
  polarity: mixed
  page_or_region: "About page — accreditation badge cluster"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/about/tile-02-y02440.png"
  claim: "The half-image/half-text 'Safe, reliable' section is structurally standard, but the three accreditation seals (NABP, ACHC Accredited Compounding Pharmacy, and a third circular mark) are dropped inline at differing sizes and styles with no bounding container, reading as a raw logo block rather than a designed element."
  visible_tells:
    - "Three certification marks of differing scale and shape clustered below the checklist"
    - "No consistent container, baseline, or alignment ties the badges to the text column"
  confidence: medium

- id: layout_11
  family: layout_composition_components
  polarity: mixed
  page_or_region: "Reviews page — testimonial card grid"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/reviews/tile-02-y02440.png"
  claim: "The before/after review cards are structurally consistent in width and padding, but card heights vary with quote length and there is no fixed-height or masonry treatment, producing a ragged bottom edge across the row."
  visible_tells:
    - "Row of review cards where the shorter-quote card is visibly shorter than its neighbors, leaving an uneven bottom alignment"
  confidence: high

- id: layout_12
  family: layout_composition_components
  polarity: poor
  page_or_region: "About page — 'Partner pharmacy information' block"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/about/tile-05-y06100.png"
  claim: "The 'Partner pharmacy information' section is laid out as unstyled left-aligned body text and a raw bullet list on a sage band, with no card, divider, or containment separating it from the footer — it reads as an afterthought rather than a designed component."
  visible_tells:
    - "Plain bullet list of pharmacy addresses on a flat mint/sage band with no bounding card"
    - "No divider or container separates the block from the dark footer directly beneath it"
  confidence: high

- id: layout_13
  family: layout_composition_components
  polarity: poor
  page_or_region: "Reviews page — 'Your success story' photo mosaic"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/reviews/tile-04-y04880.png"
  claim: "The right-side photo mosaic (six images in an irregular two-column arrangement) is not grid-aligned: images crop to differing heights and the columns appear unequal, producing a haphazard collage rather than an intentional composition."
  visible_tells:
    - "Six photos in two columns of unequal height and width, not flush to a shared baseline grid"
    - "Visible gaps and offset rows between the stacked images"
  confidence: medium

- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: "Homepage hero — per-category color fields"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/homepage/tile-00-y00000.png"
  claim: "The hero assigns one solid backdrop color per product card — green (GLP-1), terracotta (Sermorelin), blue (NAD+) — a deliberate per-category color rule rather than a random rotation."
  visible_tells:
    - "Three side-by-side cards each carry a distinct solid color field, none repeating"
    - "Color reads as assigned to category, not arbitrary"
  confidence: high

- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: "Homepage carousel — Age with confidence / Rejuvenate your skin"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/homepage/tile-03-y03660.png"
  claim: "The promo carousel repeats the hero's palette discipline at sub-category level: the aging card reuses the same terracotta/sand and the skin card the same kelly green, extending the per-category color system coherently."
  visible_tells:
    - "'Age with confidence' card uses the same terracotta/sand tone as the hero Sermorelin card"
    - "'Rejuvenate your skin' card uses the same kelly green as the hero GLP-1 card"
  confidence: high
  contrast_with: "store/eden-health/captures/2026-05-30/tiles/homepage/tile-00-y00000.png"

- id: color_03
  family: color_brand_imagery
  polarity: strong
  page_or_region: "GLP-1 page — branded-blue product photography"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/glp1/tile-07-y08540.png"
  claim: "Brand blue is used as a full-field studio background for product photography in the CTA card, the same hue carried by the highlighted pricing card and a hero card elsewhere — a recurring brand color, not a one-off."
  visible_tells:
    - "A large solid-blue square holds the arranged injection devices on the right of the CTA card"
    - "The blue matches the filled 'Personalized GLP-1 Injections' pricing card and the homepage NAD+ hero field"
  confidence: high
  contrast_with: "store/eden-health/captures/2026-05-30/tiles/glp1/tile-01-y01220.png"

- id: color_04
  family: color_brand_imagery
  polarity: strong
  page_or_region: "Footer — site-wide chromatic anchor"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/about/tile-05-y06100.png"
  claim: "The dark near-black footer with white type is consistent across every captured page, providing a reliable terminal anchor and holding a tight black/white palette at page end."
  visible_tells:
    - "Dark near-black footer with white type, white wordmark, and white nav links repeats without shade or layout variation"
    - "Same footer appears at the bottom of homepage, GLP-1, and about captures"
  confidence: high

- id: color_05
  family: color_brand_imagery
  polarity: strong
  page_or_region: "About / homepage — medical advisor portraits"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/homepage/tile-05-y06100.png"
  claim: "The medical-advisor portraits share a consistent photographic language — white/teal coats, neutral light-grey backgrounds, bust framing, direct eye contact — giving the credential carousel a purposefully shot, cohesive feel."
  visible_tells:
    - "Four advisor portraits all in white or teal medical coats against controlled neutral backgrounds"
    - "Consistent bust-length framing, lighting, and background tone across the carousel cards"
  confidence: high

- id: color_06
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "Reviews / GLP-1 — user-submitted before/after photos"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/reviews/tile-02-y02440.png"
  claim: "Before/after customer photos are uncontrolled user snapshots — varying lighting, backgrounds, and crops — sitting alongside the controlled studio imagery, with brand-green 'Lost X lbs' chips overlaid on visuals that otherwise carry none of the brand's controlled language."
  visible_tells:
    - "Paired before/after photos with inconsistent indoor/outdoor backgrounds, lighting, and framing across cards"
    - "Green 'Lost 25+ lbs' / 'Lost 65+ lbs' chips are the only branded element overlaid on these snapshots"
  confidence: high
  contrast_with: "store/eden-health/captures/2026-05-30/tiles/glp1/tile-07-y08540.png"

- id: color_07
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "Homepage — editorial lifestyle card row"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/homepage/tile-07-y08540.png"
  claim: "The four lifestyle/editorial cards are competently selected but read as an assembled pool rather than one art direction — color grading, focal length, and background tone differ noticeably from card to card with no unifying cast."
  visible_tells:
    - "Four images (man outdoors, laughing woman, man with hands in hair, woman reclining) differ in grading and background saturation"
    - "No shared color cast or compositional approach links the four as a set"
  confidence: medium

- id: color_08
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "About — leadership headshots"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/about/tile-03-y03660.png"
  claim: "Leadership headshots are unified only by their circular crop — background tone and lighting vary visibly between portraits, signaling assembled rather than purpose-shot photography."
  visible_tells:
    - "Visible headshots show different background tones and lighting qualities within the same circular frame"
    - "The circular crop is the sole unifying device; it does not compensate for the inconsistent source photography"
  confidence: medium

- id: color_09
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "Homepage — in-page data widgets palette"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/homepage/tile-01-y01220.png"
  claim: "The interactive widgets in the weight-loss row introduce off-palette color — a coral-to-lime gradient arc and a forest-green bar chart — that map to neither the brand blue nor the kelly green used in the product cards."
  visible_tells:
    - "The weight-progress arc uses a coral-to-lime gradient unlike any brand accent"
    - "The 'Track Your Progress' bar chart uses forest-green bars distinct from the product-card kelly green"
  confidence: medium

- id: iconography_01
  family: iconography_illustration
  polarity: mixed
  page_or_region: "Homepage / About — attribute icon set"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/homepage/tile-06-y07320.png"
  claim: "The six attribute icons (rabbit, tree, leaf, flask, atom, wheat) are outline-only line glyphs at uniform stroke weight and size — visually consistent as a set — but lean on generic stock science/nature motifs with no distinctive style elaboration; the same set reappears unchanged on the About page, confirming a reusable component."
  visible_tells:
    - "Six cards each with a single outline icon above a two-line label; stroke weight uniform across all six"
    - "Motifs (flask, atom, wheat) are standard stock-icon archetypes with no custom detailing"
    - "Identical icon set and layout recur on the About page"
  confidence: high
  contrast_with: "store/eden-health/captures/2026-05-30/tiles/about/tile-02-y02440.png"

- id: iconography_02
  family: iconography_illustration
  polarity: strong
  page_or_region: "Homepage hero / GLP-1 — product photography system"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/glp1/tile-00-y00000.png"
  claim: "Product imagery functions as a controlled illustration system, not stock: branded vials and injector pens are styled as deliberate flat-lays on solid brand-color backgrounds (lime here), placing product graphics at the top of the visual hierarchy."
  visible_tells:
    - "Multiple pen injectors and a vial arranged at varied angles on a solid lime field, filling most of the frame"
    - "Lime background echoes the brand accent used in buttons and category fields elsewhere"
  confidence: high
  contrast_with: "store/eden-health/captures/2026-05-30/tiles/glp1/tile-01-y01220.png"

- id: iconography_03
  family: iconography_illustration
  polarity: strong
  page_or_region: "GLP-1 page — branded unboxing prop"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/glp1/tile-02-y02440.png"
  claim: "The step-2 card uses a real branded kraft shipping box with the 'eden' wordmark printed in brand green, shot in clean studio light — extending the brand identity into a physical product touchpoint rather than a generic icon."
  visible_tells:
    - "Kraft cardboard box with 'eden' printed on the lid in brand green"
    - "Box shot in even studio light with a soft drop shadow, consistent with the site's product-photo treatment"
  confidence: high

- id: iconography_04
  family: iconography_illustration
  polarity: mixed
  page_or_region: "GLP-1 page — 3-step photography (no icons)"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/glp1/tile-02-y02440.png"
  claim: "The three-step cards substitute real-object photography (phone-in-hand intake form, branded box, candid person with a chat overlay) for any iconographic or illustrative treatment — serviceable and on-brand but skipping custom illustration for the step explainer."
  visible_tells:
    - "Step 1: hands holding a phone showing the Eden intake form"
    - "Step 2: kraft box; Step 3: lifestyle photo of a woman with a 'DR. SMITH' chat overlay — no icons in any step"
  confidence: high

- id: iconography_05
  family: iconography_illustration
  polarity: mixed
  page_or_region: "Homepage — decorative data-viz illustrations"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/homepage/tile-02-y02440.png"
  claim: "The 'Boost Energy Levels' graphic uses gradient-filled capsule bars (Low/Normal/High) as decoration rather than data — a pink-to-green gradient with a floating '45%' label and no axis or source, reading as illustration dressed as a chart."
  visible_tells:
    - "Three capsule bars of differing height labeled Low/Normal/High with a pink-to-green/teal gradient"
    - "'45%' label floats above the bars with no axis, scale, or data source"
  confidence: high
  contrast_with: "store/eden-health/captures/2026-05-30/tiles/homepage/tile-01-y01220.png"

- id: iconography_06
  family: iconography_illustration
  polarity: poor
  page_or_region: "Reviews page — video testimonial play buttons"
  tile_path: "store/eden-health/captures/2026-05-30/tiles/reviews/tile-01-y01220.png"
  claim: "The circular white play-button icons on the three video thumbnails use a default play-triangle convention with no brand styling, sizing variation, or color — invisible as a designed asset."
  visible_tells:
    - "Three thumbnails each with a centered plain white circle and triangle play icon"
    - "Play icons are identical and unstyled across all three — no brand color or custom treatment"
  confidence: high
```

## Provenance

- **Tiles read.** 33 active tiles across five signal pages from `captures/2026-05-30/tiles/` — `homepage` (9), `glp1` (10), `reviews` (7), `about` (7), `how_it_works` (1). The newest capture (`2026-06-03`) is product-detail pages only (a `/deepen-offerings` run) and carries no homepage, so the visual-system pages were re-tiled from the `2026-05-30` dossier capture.
- **QA gate.** `qa_status: clean` — all five `overview-480w.png` previews and spot-checked native tiles rendered fully: no modals/cookie banners, no grey or blank heros, no black media cards, no mid-animation reveals. Reviews video cards rendered as legible freeze-frames (not black). **No exclusions; no Tier-B browser re-render.**
- **Mining.** Blind fan-out via `skills/visual-evidence/mine.workflow.js` (run `wf_b0841412-863`): 4 family miners (Sonnet, tiles-only, no network) → judge (Opus). Miners produced 49 raw cards; the judge accepted **35** after pruning 14 — 11 cross-tile/cross-family merges plus 3 factual corrections (cards whose claimed defect was contradicted by the cited tile: legibly-sized GLP-1 feature icons, the 'Lost X lbs' chips that do carry a glyph, and a price/name-competition claim the carousel disproves).
- **Card set.** All 35 accepted cards retained per the current contract ([VISUAL.md](../../modules/VISUAL.md): one card per distinct visible tell, comprehensive, not capped) — 16 strong / 14 mixed / 5 poor across all four families. Every `poor` structural card was spot-checked against its native tile and reflects genuine visible state, not a capture artifact.
- **Caveat.** Point-in-time snapshot of the captured tiles; the live site changes. Judgments are of *visible visual state* only — no score, no business/clinical/copy read.
