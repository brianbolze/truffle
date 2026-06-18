---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.0"
domain: hims.com
captured_at: 2026-06-18           # own freshness — when these tiles were mined
source_capture: 2026-06-18        # pairs with the 2026-06-18 profile.md capture
qa_status: exclusions-noted
---

## Visual & brand impression

A mature, well-funded DTC brand with strong typographic discipline: large serif display heads resolve cleanly against subordinate copy across heroes and product cards [typography_01][typography_06][typography_07], with color used as a hierarchy level, not decoration [typography_02][typography_05]. A warm brown-sand-terracotta palette and a single amber-gold accent read as a deliberate category system [color_01][color_02][color_03], and components repeat with real rigor — product cards, doctor grid, milestone timeline, comparison table, and footer share one structural template [layout_01][layout_02][layout_04][layout_06][layout_08]. Production is bespoke: custom medication renders, annotation diagrams, process-step UI mocks [iconography_01][iconography_03][iconography_04]. The weakness is consistency — the accent fractures to steel-blue in sexual health and lavender with generic neutral headshots on the about page [color_08][color_09][color_10], plus low-contrast condition labels and generic checkmark icons [typography_09][iconography_09].

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: "homepage — hero"
  tile_path: "store/hims-com/captures/2026-06-18/tiles/homepage/tile-00-y00000.png"
  claim: "The hero establishes a clean two-level hierarchy: a large serif display headline ('The care you've always deserved') contrasts clearly against small nav text and compact product-card labels, with no intermediate levels cluttering the read path."
  visible_tells:
    - "Display headline is the dominant element on white ground, markedly larger than any surrounding text"
    - "Nav items and card sub-labels are visually subordinate without a crowding mid-level"
  confidence: high

- id: typography_02
  family: typography_hierarchy
  polarity: strong
  page_or_region: "homepage — dark GLP-1 promotional section"
  tile_path: "store/hims-com/captures/2026-06-18/tiles/homepage/tile-02-y02440.png"
  claim: "On the dark background section, a large display headline ('Lose up to 25% body weight') remains fully legible in white type, with amber accent text reserved for a single highlighted word, demonstrating color-as-hierarchy rather than decoration."
  visible_tells:
    - "Large white headline sits atop a near-black brown field with no legibility loss"
    - "Amber is used on one keyword only ('SNAC' / qualifier) — functioning as a typographic level, not scattered"
  confidence: high
  contrast_with: "store/hims-com/captures/2026-06-18/tiles/homepage/tile-01-y01220.png"

- id: typography_03
  family: typography_hierarchy
  polarity: strong
  page_or_region: "homepage — doctor team section"
  tile_path: "store/hims-com/captures/2026-06-18/tiles/homepage/tile-05-y06100.png"
  claim: "The 'best care / by the best in medicine' section uses a clearly graded three-level hierarchy: large display heading, a small regular-weight subdeck, and card-level name + specialty labels in distinct smaller sizes — each level visually distinct without overlap."
  visible_tells:
    - "Display heading is roughly 3-4x the size of card name labels"
    - "Specialty labels beneath names are visibly lighter and smaller than the names"
  confidence: high

- id: typography_04
  family: typography_hierarchy
  polarity: strong
  page_or_region: "labs-category — hero"
  tile_path: "store/hims-com/captures/2026-06-18/tiles/labs-category/tile-00-y00000.png"
  claim: "The labs hero resolves to a tight two-level structure: a large serif display line over photography with a single-line sub-claim in a dramatically smaller regular weight below, creating a fast read even over a busy photographic background."
  visible_tells:
    - "Display headline 'Test for signals of 1,000+ health conditions' is the only text competing for attention over the photo"
    - "Sub-claim 'Stay ahead of your health...' is clearly subordinate in size and weight"
  confidence: high

- id: typography_05
  family: typography_hierarchy
  polarity: strong
  page_or_region: "labs-category — price-comparison headline"
  tile_path: "store/hims-com/captures/2026-06-18/tiles/labs-category/tile-04-y04880.png"
  claim: "The 'Learn 5x more about your body for $1,000s less' headline uses size plus selective orange color accent to create hierarchy within a single headline line, so the price differential reads as the dominant message without a separate subheading."
  visible_tells:
    - "Headline is set at display scale; 'for $1,000s less' is rendered in orange against the black remaining text"
    - "No supporting subheadline is present — the accent carries the second emphasis level"
  confidence: high

- id: typography_06
  family: typography_hierarchy
  polarity: strong
  page_or_region: "weight-loss-category — product card grid"
  tile_path: "store/hims-com/captures/2026-06-18/tiles/weight-loss-category/tile-01-y01220.png"
  claim: "Product cards maintain a consistent internal four-level hierarchy — badge label, product name (largest), price line, and fine print — all legible and differentiated at a glance across all five visible cards."
  visible_tells:
    - "Product name ('Wegovy Pill', 'Zepbound Vial', etc.) is consistently the largest text element within each card"
    - "Price and 'Membership required' are visibly smaller and lighter than the name"
    - "Badge chips ('Rx', 'New', 'High dose available') sit at a clearly smaller scale still"
  confidence: high

- id: typography_07
  family: typography_hierarchy
  polarity: strong
  page_or_region: "weight-loss-category — hero headline"
  tile_path: "store/hims-com/captures/2026-06-18/tiles/weight-loss-category/tile-00-y00000.png"
  claim: "The weight-loss hero uses a two-line serif display headline ('Weight loss / that works') with the second line in a warm-brown/orange tone, while body copy sits in a smaller regular weight to the right — creating hierarchy within the headline itself and between headline and supporting copy."
  visible_tells:
    - "Orange-toned second line 'that works' draws the eye as an accent within the heading without a separate sub-level"
    - "Right-column body copy is visibly smaller and lighter, clearly subordinate"
  confidence: high

- id: typography_08
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "sexual-health-category — 'Why men choose Hims' feature cards"
  tile_path: "store/hims-com/captures/2026-06-18/tiles/sexual-health-category/tile-04-y04880.png"
  claim: "Feature card headings use a steel-blue accent on a keyword to add a secondary emphasis level, but the accent is applied inconsistently — some headings highlight a multi-word phrase, others a single word — so the color reads as stylistic rather than rule-driven."
  visible_tells:
    - "First card: blue accent spans 'Trusted sexual health care for men'; second card: blue on 'Unlimited access'; third card: blue on 'Total Control'"
    - "No apparent rule for what portion of a heading receives the accent"
  confidence: medium

- id: typography_09
  family: typography_hierarchy
  polarity: poor
  page_or_region: "labs-category — cancer screening pill labels"
  tile_path: "store/hims-com/captures/2026-06-18/tiles/labs-category/tile-05-y06100.png"
  claim: "The cancer-type pill labels ('Colon cancer', 'Lymphoma', 'Pancreatic cancer', etc.) are set in small, uniform light-weight text over a warm-toned illustration, producing low contrast and no size differentiation — a hierarchy-free list that is hard to scan."
  visible_tells:
    - "All cancer pill chips appear at the same size and weight with no hierarchical emphasis"
    - "Light text on a mid-tone terracotta background reduces legibility; no single label is more prominent"
  confidence: high
  contrast_with: "store/hims-com/captures/2026-06-18/tiles/labs-category/tile-04-y04880.png"

- id: typography_10
  family: typography_hierarchy
  polarity: poor
  page_or_region: "labs-category — legal/disclaimer block"
  tile_path: "store/hims-com/captures/2026-06-18/tiles/labs-category/tile-10-y12200.png"
  claim: "The GRAIL/Galleri disclaimer uses several paragraphs of small regular-weight regulatory copy with only one barely-heavier label ('Laboratory/Test Information'), providing no visual architecture to help a reader locate the relevant clause."
  visible_tells:
    - "Multiple paragraphs of small regular-weight text with a single mid-weight label — no hierarchy progression"
    - "'Laboratory/Test Information' is only slightly heavier than surrounding copy, not a true heading weight"
  confidence: medium

- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: "homepage — hero card grid"
  tile_path: "store/hims-com/captures/2026-06-18/tiles/homepage/tile-00-y00000.png"
  claim: "The hero divides into two side-by-side cards with consistent corner radius, internal padding, and thumbnail positioning, demonstrating a repeatable card grid rather than a one-off layout."
  visible_tells:
    - "Left (weight loss) and right (labs) cards share identical rounded-rectangle frames and matching internal padding"
    - "Product/photo imagery is anchored to the same vertical zone within each card"
  confidence: high

- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: "weight-loss-category — product card row"
  tile_path: "store/hims-com/captures/2026-06-18/tiles/weight-loss-category/tile-01-y01220.png"
  claim: "Five product cards share an identical structure — Rx badge, title, price, membership note, centered product image, FDA stamp, dual CTA buttons, and safety link — with no visible vertical misalignment across the row."
  visible_tells:
    - "All five cards align price text, product image, and dual-button row to the same vertical positions"
    - "FDA-approved circular stamp appears at the same position in every card"
  confidence: high

- id: layout_03
  family: layout_composition_components
  polarity: strong
  page_or_region: "sexual-health-category — review card row"
  tile_path: "store/hims-com/captures/2026-06-18/tiles/sexual-health-category/tile-05-y06100.png"
  claim: "Review cards apply a consistent component — centered 'h' logo mark, name + age, blue highlighted quote, and 'Verified review' badge at the same bottom position — across all four visible cards."
  visible_tells:
    - "Logo mark, name line, and 'Verified review' badge are vertically aligned at identical positions in each card"
    - "The highlighted quote color is uniform across all four cards"
  confidence: high

- id: layout_04
  family: layout_composition_components
  polarity: strong
  page_or_region: "about-the-company — company milestones timeline"
  tile_path: "store/hims-com/captures/2026-06-18/tiles/about-the-company/tile-05-y06100.png"
  claim: "The milestones timeline uses a consistent vertical left-rail with purple year pill, bold event title, body text, and a logo tile — each entry follows the same structural template."
  visible_tells:
    - "Purple year pill, vertical divider line, and logo tile appear at identical horizontal positions for every milestone entry"
    - "Body-text indentation is consistent across entries"
  confidence: high

- id: layout_05
  family: layout_composition_components
  polarity: strong
  page_or_region: "labs-category — three-step process section"
  tile_path: "store/hims-com/captures/2026-06-18/tiles/labs-category/tile-01-y01220.png"
  claim: "Three process steps ('Set a quick appointment', 'Get clear results', 'Unlock your Action Plan') are laid out in equal-width columns with numbered badges, consistent card height, and matching bottom illustration zones."
  visible_tells:
    - "Numbered circle badges sit at identical top positions in each column"
    - "The UI mockup illustration clips to the same bottom area in all three cards"
  confidence: high

- id: layout_06
  family: layout_composition_components
  polarity: strong
  page_or_region: "labs-category — feature comparison table"
  tile_path: "store/hims-com/captures/2026-06-18/tiles/labs-category/tile-04-y04880.png"
  claim: "The comparison table maintains precise row alignment: feature label left, two symbol columns at fixed widths, consistent row heights and hairline dividers throughout."
  visible_tells:
    - "Every row's checked/minus icons center within their columns without drift across 10+ visible rows"
    - "Row dividers are hairline-thin and evenly spaced"
  confidence: high

- id: layout_07
  family: layout_composition_components
  polarity: strong
  page_or_region: "homepage — doctor grid section"
  tile_path: "store/hims-com/captures/2026-06-18/tiles/homepage/tile-05-y06100.png"
  claim: "The doctor-grid section arranges five headshots in a single equal-width row with role badge, name, credentials, and body copy in identical vertical order per card — section-level discipline matching the card-level discipline."
  visible_tells:
    - "All five doctor cards share the same header-badge position, name size, and copy-block alignment"
    - "Card widths appear equal with uniform gaps between cards"
  confidence: high

- id: layout_08
  family: layout_composition_components
  polarity: strong
  page_or_region: "footer — shared across all pages"
  tile_path: "store/hims-com/captures/2026-06-18/tiles/homepage/tile-07-y08487.png"
  claim: "The footer uses a multi-column link grid with consistent column widths, category-label hierarchy, and a distinct app-download / 'hers' cross-link block — the same structure repeats identically across every page captured."
  visible_tells:
    - "Link columns maintain equal visual weight and spacing across the footer width"
    - "App-download block and 'hers — visit forhers.com' card occupy the same positions on homepage and labs footers"
  confidence: high
  contrast_with: "store/hims-com/captures/2026-06-18/tiles/labs-category/tile-10-y12200.png"

- id: layout_09
  family: layout_composition_components
  polarity: mixed
  page_or_region: "about-the-company — long-form article body"
  tile_path: "store/hims-com/captures/2026-06-18/tiles/about-the-company/tile-01-y01220.png"
  claim: "The about-page article uses a narrow centered text column that is functional but generic — no pull quotes, callouts, sidebars, or whitespace variation break up consecutive paragraphs, giving low visual rhythm on a page that hosts richer components elsewhere."
  visible_tells:
    - "Several stacked headed sections with body paragraphs and no graphic punctuation"
    - "No sidebar, icon, image, or rule varies the scroll"
  confidence: high
  contrast_with: "store/hims-com/captures/2026-06-18/tiles/about-the-company/tile-05-y06100.png"

- id: layout_10
  family: layout_composition_components
  polarity: mixed
  page_or_region: "sexual-health-category — '90%' stat section"
  tile_path: "store/hims-com/captures/2026-06-18/tiles/sexual-health-category/tile-03-y03660.png"
  claim: "A large '90% of Hims users are satisfied' stat sits in the left half with the entire right half left empty — an asymmetry that lands as blank rather than spacious because there is no compositional counterweight."
  visible_tells:
    - "Right half of the section is entirely white with no element or intentional negative-space gesture"
    - "'Get started' CTA is left-aligned under the stat with no right-side anchor"
  confidence: medium

- id: layout_12
  family: layout_composition_components
  polarity: mixed
  page_or_region: "weight-loss-category — section transition into dark brand band"
  tile_path: "store/hims-com/captures/2026-06-18/tiles/weight-loss-category/tile-02-y02440.png"
  claim: "A full-bleed dark brand section follows the warm beige product grid with no softened transition, producing an abrupt color break rather than a smooth section rhythm."
  visible_tells:
    - "Warm beige product-grid section above cuts immediately to a near-black background with no transitional element or partial gradient overlap"
  confidence: medium

- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: "homepage / weight-loss — warm brown category palette"
  tile_path: "store/hims-com/captures/2026-06-18/tiles/homepage/tile-00-y00000.png"
  claim: "A warm dark-brown palette is introduced immediately in the hero and held consistently into the weight-loss narrative, functioning as a deliberate category color rather than a generic neutral."
  visible_tells:
    - "Hero banner is a deep warm brown behind product photography"
    - "The same brown recurs in the dark weight-loss promo band directly below as a thematic anchor"
  confidence: high
  contrast_with: "store/hims-com/captures/2026-06-18/tiles/homepage/tile-02-y02440.png"

- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: "homepage / weight-loss — amber accent restraint"
  tile_path: "store/hims-com/captures/2026-06-18/tiles/homepage/tile-02-y02440.png"
  claim: "A single amber-gold accent is used for emphasis text and primary CTAs with no competing accent hues, applied consistently across the weight-loss and labs sections."
  visible_tells:
    - "'SNAC' headline word rendered in solid amber-gold against dark brown"
    - "CTA button on the same tile uses the matching amber-gold fill"
    - "Amber recurs as the 'that works' / accent word elsewhere in the warm sections"
  confidence: high
  contrast_with: "store/hims-com/captures/2026-06-18/tiles/sexual-health-category/tile-05-y06100.png"

- id: color_03
  family: color_brand_imagery
  polarity: strong
  page_or_region: "weight-loss-category — product card backgrounds"
  tile_path: "store/hims-com/captures/2026-06-18/tiles/weight-loss-category/tile-01-y01220.png"
  claim: "Product cards use a unified warm sand/cream background with isolated medication on white cutouts, creating a coherent catalog aesthetic rather than mixed stock-photo staging."
  visible_tells:
    - "All five product cards share the same sand-toned card background"
    - "Medication objects float on a plain ground within each card — no lifestyle props or environmental staging"
  confidence: high

- id: color_04
  family: color_brand_imagery
  polarity: strong
  page_or_region: "weight-loss / labs — brand-matched warm photography"
  tile_path: "store/hims-com/captures/2026-06-18/tiles/weight-loss-category/tile-06-y07320.png"
  claim: "Hero photography of real-looking men is shot against brand-matched warm terracotta/copper backdrops rather than generic white or gray studio setups, tying image language directly to the palette."
  visible_tells:
    - "Man in the 'This time / you have Hims' closing shot is on a solid warm copper-orange backdrop matching the site's terracotta range"
    - "Warm lighting consistent with the brown-amber system, not a neutral studio setup"
  confidence: high
  contrast_with: "store/hims-com/captures/2026-06-18/tiles/about-the-company/tile-03-y03660.png"

- id: color_05
  family: color_brand_imagery
  polarity: strong
  page_or_region: "labs-category — hero palette continuity"
  tile_path: "store/hims-com/captures/2026-06-18/tiles/labs-category/tile-00-y00000.png"
  claim: "The labs hero repeats the warm sand-to-brown gradient used on the weight-loss pages, showing palette discipline across distinct product categories rather than each section choosing its own color."
  visible_tells:
    - "Labs hero background is the same warm sand gradient as the weight-loss hero, not a clinical white or blue"
    - "The man's skin tone is complemented rather than washed out by the background"
  confidence: high

- id: color_06
  family: color_brand_imagery
  polarity: strong
  page_or_region: "labs-category — conditions panel as type-as-image"
  tile_path: "store/hims-com/captures/2026-06-18/tiles/labs-category/tile-02-y02440.png"
  claim: "A full-bleed warm salmon/red panel filled only with large condition-name typography is used as a graphic technique in lieu of photography, showing the brand system extends to type-as-image rather than defaulting to stock photography."
  visible_tells:
    - "Warm red-salmon background filled with condition names in display type — no photography or illustration"
    - "An orange 'Out of range' UI chip overlays the type, linking the panel to the product proposition"
  confidence: high

- id: color_07
  family: color_brand_imagery
  polarity: strong
  page_or_region: "footer — oversized 'hims' wordmark"
  tile_path: "store/hims-com/captures/2026-06-18/tiles/homepage/tile-07-y08487.png"
  claim: "The footer carries a typographic brand expression — 'hims' set at display scale in dark charcoal on near-black — that functions as a brand-owned graphic device, a distinct identity layer separate from the navigational text above and not a hierarchy level competing with content."
  visible_tells:
    - "Oversized 'hims' logotype in dark gray spans the full footer width at display scale"
    - "Dark-gray-on-black treatment makes it clearly identity decoration; the dot of the 'i' is a circle, holding the logo grammar at monumental size"
  confidence: high

- id: color_08
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "sexual-health-category — accent color shift to steel-blue"
  tile_path: "store/hims-com/captures/2026-06-18/tiles/sexual-health-category/tile-05-y06100.png"
  claim: "The sexual-health section uses a steel-blue as its emphasis accent (on headline keywords and testimonial quotes), diverging from the amber-gold used across weight-loss and labs — the multi-category palette is functional but not unified."
  visible_tells:
    - "'loving their results' headline emphasis word is rendered in pale steel-blue, not amber"
    - "Review-card quote text uses the same pale blue accent throughout the section"
  confidence: high
  contrast_with: "store/hims-com/captures/2026-06-18/tiles/weight-loss-category/tile-01-y01220.png"

- id: color_09
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "about-the-company — hero off-brand lavender palette"
  tile_path: "store/hims-com/captures/2026-06-18/tiles/about-the-company/tile-00-y00000.png"
  claim: "The about-page hero uses a flat lavender/lilac background with scattered multicolor confetti dots — a palette absent everywhere else on the site — suggesting the about page was designed under a different brief from the warm brown-amber system."
  visible_tells:
    - "Lavender hero background with multicolor dot scatter is the only lavender usage across the captured pages"
    - "A UI product mockup and a held product float on the lavender field with no warm-tone grounding"
  confidence: high
  contrast_with: "store/hims-com/captures/2026-06-18/tiles/homepage/tile-00-y00000.png"

- id: color_10
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "about-the-company — leadership photography treatment"
  tile_path: "store/hims-com/captures/2026-06-18/tiles/about-the-company/tile-03-y03660.png"
  claim: "Leadership headshots use plain white/off-white backgrounds with no grading to the brand palette — a generic corporate treatment inconsistent with the warm terracotta photography used in product sections."
  visible_tells:
    - "Four headshots all on neutral white or very light gray backgrounds"
    - "No warm tone or color treatment — standard portrait lighting"
  confidence: high
  contrast_with: "store/hims-com/captures/2026-06-18/tiles/weight-loss-category/tile-06-y07320.png"

- id: color_11
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "about-the-company — milestones / awards periwinkle palette"
  tile_path: "store/hims-com/captures/2026-06-18/tiles/about-the-company/tile-07-y08540.png"
  claim: "The about page is almost entirely white with black text, purple milestone accents, and periwinkle-gray award cards — the brand's warm palette is absent, reading as a deliberate content-document treatment but carrying no brand color signal."
  visible_tells:
    - "Purple year pills and award-card backgrounds in flat light periwinkle-gray are the only color elements"
    - "No amber, no warm brown anywhere on the page"
  confidence: high
  contrast_with: "store/hims-com/captures/2026-06-18/tiles/homepage/tile-00-y00000.png"

- id: color_12
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "weight-loss-category — customer transformation photography"
  tile_path: "store/hims-com/captures/2026-06-18/tiles/weight-loss-category/tile-05-y06100.png"
  claim: "Customer transformation photos use real men in candid real-world settings with consistent warm-toned grading and month labels, presenting an owned visual language rather than clinical white-background before/after shots."
  visible_tells:
    - "Multiple customer photo pairs with month labels and name+age captions (Drew 47, Adam 46, Roland 43, Zack 44)"
    - "Photographs show men in casual settings (outdoors, restaurants), not clinical comparison backdrops"
  confidence: medium

- id: iconography_01
  family: iconography_illustration
  polarity: strong
  page_or_region: "homepage — SNAC technology annotation diagram"
  tile_path: "store/hims-com/captures/2026-06-18/tiles/homepage/tile-02-y02440.png"
  claim: "The SNAC technology diagram uses restrained, purpose-built annotation lines with gold dot terminators and inline callout labels, achieving a clinical-infographic look that is clearly custom-crafted rather than stock."
  visible_tells:
    - "Thin gold leader lines with circular terminal dots connect labeled callouts to the pill render"
    - "Callout text is set at reduced weight, subordinate to the product render; line routing is deliberate with no crossings"
  confidence: high
  contrast_with: "store/hims-com/captures/2026-06-18/tiles/labs-category/tile-01-y01220.png"

- id: iconography_02
  family: iconography_illustration
  polarity: strong
  page_or_region: "labs-category — cancer screening body illustration"
  tile_path: "store/hims-com/captures/2026-06-18/tiles/labs-category/tile-05-y06100.png"
  claim: "The translucent male body figure with a green 'No cancer signal detected' badge and a glowing halo ring is a bespoke medical illustration in the brand's warm palette, used purposefully as a reassurance graphic."
  visible_tells:
    - "Translucent warm-toned body figure with internal glow over a terracotta ground"
    - "Green checkmark badge positioned at the torso; a halo ring anchors the figure at the feet"
  confidence: high
  contrast_with: "store/hims-com/captures/2026-06-18/tiles/about-the-company/tile-00-y00000.png"

- id: iconography_03
  family: iconography_illustration
  polarity: strong
  page_or_region: "labs-category — process-step mini UI mocks"
  tile_path: "store/hims-com/captures/2026-06-18/tiles/labs-category/tile-01-y01220.png"
  claim: "The three process cards each contain a small custom UI mock — an appointment-confirmation card, a lab-result chart, and an action-plan breakdown — rendered as inline mini-illustrations rather than generic icons, showing deliberate production investment."
  visible_tells:
    - "Miniature 'Appointment confirmed' card with calendar detail in the first step"
    - "A small results chart in the second; a habit/exercise/nutrition/sleep action-plan breakdown in the third"
  confidence: high

- id: iconography_04
  family: iconography_illustration
  polarity: strong
  page_or_region: "weight-loss-category — product medication renders"
  tile_path: "store/hims-com/captures/2026-06-18/tiles/weight-loss-category/tile-01-y01220.png"
  claim: "Each product card uses a high-detail hero render of the physical medication (embossed pill, autoinjector pen, vial + syringe) on a matching cream background with a consistent FDA-approved stamp — a coherent system across five cards, not stock photography."
  visible_tells:
    - "Wegovy Pill rendered as a 3D pill with 'novo' emboss and soft shadow"
    - "Zepbound KwikPen rendered with fine device detail and a teal branding stripe; FDA stamp at a consistent position on each card"
  confidence: high
  contrast_with: "store/hims-com/captures/2026-06-18/tiles/sexual-health-category/tile-00-y00000.png"

- id: iconography_05
  family: iconography_illustration
  polarity: mixed
  page_or_region: "sexual-health-category — ED product pill renders"
  tile_path: "store/hims-com/captures/2026-06-18/tiles/sexual-health-category/tile-00-y00000.png"
  claim: "The ED product renders (blue oval, pink chew, slate tablet) are clean but simpler than the GLP-1 renders — smooth solid-color objects without embossing or device detail, suggesting different render tiers across product lines."
  visible_tells:
    - "Blue pill is a flat smooth oval with no surface marking"
    - "Pink 'h' chew is a rounded form with a single-letter emboss; the slate tablet shows basic form with no label detail"
  confidence: medium
  contrast_with: "store/hims-com/captures/2026-06-18/tiles/weight-loss-category/tile-01-y01220.png"

- id: iconography_06
  family: iconography_illustration
  polarity: mixed
  page_or_region: "homepage — category shortcut thumbnails"
  tile_path: "store/hims-com/captures/2026-06-18/tiles/homepage/tile-00-y00000.png"
  claim: "The horizontal category shortcut strip uses small photo-style thumbnails (a pill, a hairbrush, a capsule) as category markers rather than a unified line-icon set — functional but inconsistent in visual weight and style."
  visible_tells:
    - "Photo-style thumbnail for 'Have better sex' and a hairbrush photo for 'Regrow hair'"
    - "No consistent stroke weight, outline style, or grid alignment across the row"
  confidence: medium

- id: iconography_07
  family: iconography_illustration
  polarity: mixed
  page_or_region: "labs-category — 'Doctor-trusted treatment plans' badge"
  tile_path: "store/hims-com/captures/2026-06-18/tiles/labs-category/tile-07-y08540.png"
  claim: "The 'Doctor-trusted treatment plans' card uses an abstract two-teardrop illustration (amber + blue overlapping) that is distinctive but semantically ambiguous — the link to 'doctor trust' is not self-evident without the label."
  visible_tells:
    - "Two overlapping teardrop shapes in amber and blue"
    - "No medical iconography (no caduceus, stethoscope, or cross); reads as decorative color accent rather than symbol"
  confidence: medium

- id: iconography_08
  family: iconography_illustration
  polarity: mixed
  page_or_region: "about-the-company — milestone third-party logo anchors"
  tile_path: "store/hims-com/captures/2026-06-18/tiles/about-the-company/tile-06-y07320.png"
  claim: "The milestone timeline and awards row use third-party logos (NYSE, MedMatch, Ad Age, Fortune/Great Place to Work, Inc) as the visual anchors rather than bespoke illustrations — practical, but delegates visual identity to external marks."
  visible_tells:
    - "NYSE wordmark badge for the IPO milestone and a MedMatch logo for the capabilities milestone"
    - "Award cards carry Ad Age, Great Place to Work + Fortune, and Inc Best in Business logos as the dominant graphic"
  confidence: high

- id: iconography_09
  family: iconography_illustration
  polarity: poor
  page_or_region: "sexual-health-category — 'How it works' step checkmarks"
  tile_path: "store/hims-com/captures/2026-06-18/tiles/sexual-health-category/tile-04-y04880.png"
  claim: "The 'How it works' checklist uses plain blue circular checkmark icons as the sole visual punctuation — generic and interchangeable with any SaaS onboarding flow, not differentiated for a health brand."
  visible_tells:
    - "Three identical blue circular checkmark icons at the same size"
    - "No step-specific illustration differentiates each stage"
  confidence: high
  contrast_with: "store/hims-com/captures/2026-06-18/tiles/labs-category/tile-01-y01220.png"
```

## Provenance

- **Tiles read:** 48 active tiles across 5 pages from `captures/2026-06-18/tiles/` — `homepage` (8), `weight-loss-category` (9), `labs-category` (12), `sexual-health-category` (9), `about-the-company` (10). Mined blind by 4 family miners (Sonnet) → judge (Opus); 56 raw cards → 43 kept (26 strong / 13 mixed / 4 poor) → **42 in this file** after the post-judge artifact check below.
- **Excluded (1 tile):** `sexual-health-category/tile-02-y02440.png` — lazy-load gap: the three OTC device-card product images (Standing O Penis Rings, Thrill Ride Prostate Massager, OMG Ring Vibrator) failed to render, leaving empty grey card bodies. A capture artifact, not a design defect → `qa_status: exclusions-noted`.
- **Dropped post-judge (1 card):** `layout_11` (about-the-company "Company milestones" heading rendering twice at identical size). Spot-check against the native tile confirmed a **capture/sticky-scroll compositing artifact** — the right-column timeline renders once and clean; the left-column heading double-stitched in the full-page screenshot. Blind miners/judge can't distinguish this from a real defect; removed per the skill's step-4 structural-card check.
- **Judge QA caveats (verified, did not obscure cited tells):** a privacy/cookie consent banner overlays the bottom of several homepage/labs/weight-loss tiles but sits below the cited evidence; `sexual-health-category/tile-07` is a near-blank lazy-load tile — both cards a miner raised on it were rejected by the judge.
- **Tier-B:** not used — cached Firecrawl screenshots were sufficient after the single exclusion.
- **Judge corrections (blinding held):** the judge falsified three bad tells before acceptance — about-page section headings ARE bold/larger (not flat); the cancer-screening background is warm terracotta (not "teal-green"); the sexual-health hero is steel-blue (not "olive/brown").
- **Snapshot caveat:** a point-in-time read of the 2026-06-18 captured tiles; Hims runs promo/A-B variations, so module layout and accent treatments can shift run-to-run.
