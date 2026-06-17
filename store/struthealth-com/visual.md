---
schema_version: "1.0"
domain: struthealth.com
captured_at: 2026-06-17
source_capture: 2026-06-04
qa_status: clean
---

# Strut Health - visual evidence

## Visual & brand impression

Strut Health reads as calm, direct-to-consumer telehealth with a disciplined palette and a reusable conversion kit: pale blue and warm off-white fields, coral CTAs, dark plum utility bands, large round photography, and blue product renders repeat across homepage, category, and PDP pages [color_01][layout_03][layout_04]. The strongest work is systemic rather than expressive: the treatment list, product/pricing rows, icon benefit band, and PDP hero are clear and reusable [layout_02][layout_03][iconography_01]. The site loses distinctiveness where generic circular stock portraits, grey-overlaid blog cards, dense mega-footers, and long unstructured story copy take over [color_04][color_05][layout_06][typography_04].

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: homepage hero
  tile_path: store/struthealth-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png
  claim: The homepage opens with a very clear typographic ladder, separating brand/nav, oversized H1, body copy, primary CTA, category labels, and the next section heading without crowding.
  visible_tells:
    - The H1 occupies two large lines in the upper-left/center area, far larger than the one-line support sentence below it.
    - The filled coral "Start for Free" button is smaller than the H1 but visually heavier than the body copy.
    - Category labels sit below four circular portraits in a separate, smaller type level.
  confidence: high
- id: typography_02
  family: typography_hierarchy
  polarity: strong
  page_or_region: treatment list table
  tile_path: store/struthealth-com/captures/2026-06-04/tiles/homepage/tile-01-y01220.png
  claim: The featured-treatment table uses letterspaced category labels, plain product rows, thin dividers, and coral arrows to make a long roster scannable.
  visible_tells:
    - "MEN'S SEXUAL HEALTH," "HAIR LOSS," and other group labels are uppercase and letterspaced above normal-case product rows.
    - Each row is separated by a thin horizontal rule and ends with a small coral arrow.
    - The pale-blue panel holds many rows without losing alignment.
  confidence: high
- id: typography_03
  family: typography_hierarchy
  polarity: mixed
  page_or_region: how-it-works step blocks
  tile_path: store/struthealth-com/captures/2026-06-04/tiles/how-it-works/tile-00-y00000.png
  claim: The step sections make the process legible, but the oversized light-weight headings create a soft editorial feel that is less crisp than the product and table typography.
  visible_tells:
    - "Step 1" appears as a small coral label above a much larger, light-weight headline.
    - The headline spans multiple lines, while the explanatory paragraph below is comparatively small and grey.
    - The same light display treatment recurs for "Step 2" at the bottom edge of the tile.
  confidence: high
- id: typography_04
  family: typography_hierarchy
  polarity: poor
  page_or_region: our-story body copy
  tile_path: store/struthealth-com/captures/2026-06-04/tiles/our-story/tile-00-y00000.png
  claim: The story page drops from a large mission statement into long, minimally structured paragraphs, making the lower half read more like raw copy than designed editorial content.
  visible_tells:
    - The mission statement is huge and readable, but the following body text becomes a broad multi-line paragraph block.
    - There are no visible subheads, pull quotes, cards, or image breaks in the long body section.
    - The paragraph measure stretches across a wide central column.
  confidence: high
- id: typography_05
  family: typography_hierarchy
  polarity: poor
  page_or_region: footer links and legal text
  tile_path: store/struthealth-com/captures/2026-06-04/tiles/homepage/tile-05-y05426.png
  claim: Footer microtype is organized but too low-emphasis for the volume of links and legal/security details it carries.
  visible_tells:
    - Many product links are set in small grey text against a dark plum background.
    - Category labels are tiny uppercase grey text separated by large vertical gaps.
    - The legal links and address line at the bottom are smaller and dimmer than the already-small footer columns.
  confidence: high
- id: typography_06
  family: typography_hierarchy
  polarity: mixed
  page_or_region: blog card headlines
  tile_path: store/struthealth-com/captures/2026-06-04/tiles/homepage/tile-02-y02440.png
  claim: Blog-card headlines stay readable over dark overlays, but long titles wrap into bulky blocks that flatten the card hierarchy.
  visible_tells:
    - The card titles are large white text over greyed/dimmed image backgrounds.
    - "Where to Buy Testosterone Online..." and "Best Premature Ejaculation Pills..." wrap into four or more lines.
    - The "Read post" label and coral arrow become much smaller secondary elements.
  confidence: high
- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: homepage hero and category entry
  tile_path: store/struthealth-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png
  claim: The homepage hero uses restrained negative space and a simple vertical flow, letting the category portraits bridge the hero to the process section below.
  visible_tells:
    - The H1, support copy, and CTA sit in a left-biased stack with large empty space around them.
    - Four circular category portraits form a centered row under the hero copy.
    - "How Strut Works" starts below the portrait row with enough separation to read as the next module.
  confidence: high
- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: homepage how-it-works cards
  tile_path: store/struthealth-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png
  claim: The three-step process module is a polished repeated card system, with matching coral backgrounds, tilted phone screenshots, and circular number badges.
  visible_tells:
    - Three same-width cards begin in a row beneath the "How Strut Works" heading.
    - Each card uses the same coral field, phone mockup angle, and dark circular number badge.
    - The number badges overlap the card corners consistently.
  confidence: high
  contrast_with: store/struthealth-com/captures/2026-06-04/tiles/how-it-works/tile-01-y01220.png
- id: layout_03
  family: layout_composition_components
  polarity: strong
  page_or_region: weight-loss product rows
  tile_path: store/struthealth-com/captures/2026-06-04/tiles/mens-weight-loss/tile-01-y01220.png
  claim: The category page repeats a clean product-commerce layout, pairing each product image with copy, a small pricing box, a wide CTA, and a secondary learn-more link.
  visible_tells:
    - The vial render sits on the left while the product name, description, pricing box, and buttons align on the right.
    - The pricing card has a consistent outline, radio dot, large price, and coral savings text.
    - The wide coral "Buy now" button and smaller "Learn more" link repeat below the pricing card.
  confidence: high
- id: layout_04
  family: layout_composition_components
  polarity: strong
  page_or_region: PDP hero
  tile_path: store/struthealth-com/captures/2026-06-04/tiles/pdp-injectable-semaglutide/tile-00-y00000.png
  claim: The PDP hero is conversion-complete without feeling crowded, combining product name, support claims, price card, CTA, product render, patient photo, and benefit strip in one coherent first screen.
  visible_tells:
    - The left column stacks H1, support lines, transparent-pricing card, and the primary consultation CTA.
    - The right side layers a blue bottle render with a circular patient image.
    - A dark plum benefit band with four icon-label pairs anchors the section below.
  confidence: high
- id: layout_05
  family: layout_composition_components
  polarity: mixed
  page_or_region: how-it-works page hero
  tile_path: store/struthealth-com/captures/2026-06-04/tiles/how-it-works/tile-00-y00000.png
  claim: The how-it-works hero is structurally simple but less distinctive than the product sections because a full-bleed warehouse photo plus centered text does most of the work.
  visible_tells:
    - The top half is one large darkened warehouse photograph with white title and subtitle centered over it.
    - The navigation and CTA sit on top of the same photo field.
    - The more recognizable phone-card system only begins below the hero.
  confidence: high
- id: layout_06
  family: layout_composition_components
  polarity: poor
  page_or_region: mega-footer
  tile_path: store/struthealth-com/captures/2026-06-04/tiles/homepage/tile-04-y04880.png
  claim: The footer is orderly but overgrown, turning the bottom of the page into a dense product directory that overwhelms its supporting role.
  visible_tells:
    - Product links run in long vertical lists under "For him" and "For her."
    - Multiple categories repeat within the same columns, extending far down the tile.
    - Social links and newsletter labels appear beside the directory but have little visual priority.
  confidence: high
- id: layout_07
  family: layout_composition_components
  polarity: mixed
  page_or_region: PDP process and FAQ sections
  tile_path: store/struthealth-com/captures/2026-06-04/tiles/pdp-injectable-semaglutide/tile-02-y02440.png
  claim: The PDP lower sections are neatly aligned, but the process row and FAQ accordion become sparse linear components compared with the richer hero above.
  visible_tells:
    - The "How it Works" row uses three evenly spaced number circles connected by thin horizontal lines.
    - The FAQ section is a centered list of text rows with coral plus signs on a pale blue background.
    - Both modules use a lot of empty vertical space around relatively plain row content.
  confidence: high
- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: cross-page palette
  tile_path: store/struthealth-com/captures/2026-06-04/tiles/pdp-injectable-semaglutide/tile-00-y00000.png
  claim: The site has a recognizable palette system: pale blue surfaces, warm off-white backgrounds, deep plum bands, and coral action elements recur in one screen.
  visible_tells:
    - The PDP hero uses pale blue as the dominant background.
    - The benefit strip below is deep plum.
    - Coral appears on the CTA, photo-ring accent, and benefit transition accents.
  confidence: high
  contrast_with: store/struthealth-com/captures/2026-06-04/tiles/homepage/tile-01-y01220.png
- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: CTA and accent system
  tile_path: store/struthealth-com/captures/2026-06-04/tiles/how-it-works/tile-01-y01220.png
  claim: Coral is used with discipline as the action/accent color rather than flooding the page.
  visible_tells:
    - The "Start for Free" CTA is coral and centered under the step text.
    - The "Step 2" and "Step 3" labels use the same coral.
    - The dark benefit band keeps the icons white, preserving coral for the CTA and step accents.
  confidence: high
- id: color_03
  family: color_brand_imagery
  polarity: strong
  page_or_region: weight-loss product renders
  tile_path: store/struthealth-com/captures/2026-06-04/tiles/mens-weight-loss/tile-02-y02440.png
  claim: The blue medication containers on pale-blue circular blobs create a more owned and repeatable product-image language than the surrounding lifestyle photography.
  visible_tells:
    - Both Tirzepatide products use blue/white container renders placed over pale blue circles.
    - The product names on the containers match the nearby headings.
    - The rows repeat the same image treatment on a warm off-white page field.
  confidence: high
- id: color_04
  family: color_brand_imagery
  polarity: mixed
  page_or_region: circular lifestyle portraits
  tile_path: store/struthealth-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png
  claim: The circular photo treatment is consistent, but the underlying image language is generic and varied across condition categories.
  visible_tells:
    - The four category portraits share circular crops and thin accent rings.
    - The images mix a bathroom hair-loss portrait, a jogging couple, a skincare close-up, and a smiling couple on a coral background.
    - The photo colors vary more than the surrounding blue/off-white/coral interface.
  confidence: high
  contrast_with: store/struthealth-com/captures/2026-06-04/tiles/mens-weight-loss/tile-02-y02440.png
- id: color_05
  family: color_brand_imagery
  polarity: poor
  page_or_region: blog card imagery
  tile_path: store/struthealth-com/captures/2026-06-04/tiles/homepage/tile-02-y02440.png
  claim: The journal cards weaken the brand system by relying on dim grey image overlays and some nearly image-less tiles that feel generic beside the rest of the site.
  visible_tells:
    - Several article cards are covered by grey/dark overlays with white text.
    - At least two cards read as mostly flat grey fields rather than distinct imagery.
    - The card imagery does not echo the pale-blue, coral, blue-product, or circular-photo system used elsewhere.
  confidence: high
- id: color_06
  family: color_brand_imagery
  polarity: mixed
  page_or_region: press/logo strip above footer
  tile_path: store/struthealth-com/captures/2026-06-04/tiles/pdp-injectable-semaglutide/tile-04-y04880.png
  claim: The monochrome press-logo strip is tidy, but it introduces a grey media-logo band that feels separate from the site's own color and product language.
  visible_tells:
    - "BUSTLE," "MENTAL FLOSS," and "Glam" appear as large grey wordmarks above the footer.
    - The strip sits on the warm off-white field without coral, blue product color, or circular imagery.
    - The typography styles come from the third-party logos rather than the site's house type system.
  confidence: high
- id: iconography_01
  family: iconography_illustration
  polarity: strong
  page_or_region: benefit band
  tile_path: store/struthealth-com/captures/2026-06-04/tiles/homepage/tile-01-y01220.png
  claim: The benefit band uses a consistent white line-icon set that reads quickly against the dark plum field.
  visible_tells:
    - Truck, stethoscope, payment card, and calendar/coin icons share a similar outline stroke.
    - Each icon is paired with a short label in the same horizontal row.
    - The icons maintain consistent scale and spacing across the band.
  confidence: high
- id: iconography_02
  family: iconography_illustration
  polarity: strong
  page_or_region: PDP symptom cards
  tile_path: store/struthealth-com/captures/2026-06-04/tiles/pdp-injectable-semaglutide/tile-01-y01220.png
  claim: The PDP symptom cards use a simple coral line-icon family that matches the site's action color and keeps the medical benefits skimmable.
  visible_tells:
    - Stomach, heart-plus, and waist icons are all drawn as coral outline graphics.
    - Each icon sits inside an equal square tile with a short two-line label.
    - The same coral line style reappears in the "Trust the Medical Experts" module lower on the page.
  confidence: high
  contrast_with: store/struthealth-com/captures/2026-06-04/tiles/pdp-injectable-semaglutide/tile-03-y03660.png
- id: iconography_03
  family: iconography_illustration
  polarity: mixed
  page_or_region: pricing card control
  tile_path: store/struthealth-com/captures/2026-06-04/tiles/pdp-injectable-semaglutide/tile-00-y00000.png
  claim: The pricing card is clear as an interface object, but its radio-dot, outline box, and price stack are generic compared with the more branded product-render treatment beside it.
  visible_tells:
    - The card uses a thin outline rectangle, a small circular radio mark, uppercase "AUTO-REFILL," and a large price.
    - It sits near the blue product render and circular patient photo, which carry more distinctive visual identity.
    - The card's only color accent is the small coral savings line.
  confidence: high
- id: iconography_04
  family: iconography_illustration
  polarity: mixed
  page_or_region: step-number graphics
  tile_path: store/struthealth-com/captures/2026-06-04/tiles/homepage/tile-00-y00000.png
  claim: The numbered process badges are memorable, but the phone screenshots inside the cards are cropped tightly enough that their interface detail is more decorative than informational.
  visible_tells:
    - Dark circular badges with white numbers overlap the top-left of each coral phone card.
    - The phone screenshots are angled and partly cropped at the card edges.
    - Text inside the phone UI is visible but not meant to be read at page scale.
  confidence: high
- id: iconography_05
  family: iconography_illustration
  polarity: poor
  page_or_region: footer trust marks
  tile_path: store/struthealth-com/captures/2026-06-04/tiles/homepage/tile-05-y05426.png
  claim: The third-party trust badges at the bottom break from the otherwise clean line-icon system and create a cluttered patch of mixed styles.
  visible_tells:
    - Multiple vendor/security badges appear as small bitmap logos with different colors, shapes, and text density.
    - The badges sit beside the dark footer's quieter grey legal text.
    - Their detailed seals and rectangular marks contrast with the site's simpler white outline icons and coral line icons.
  confidence: high
- id: iconography_06
  family: iconography_illustration
  polarity: mixed
  page_or_region: footer social icons
  tile_path: store/struthealth-com/captures/2026-06-04/tiles/pdp-injectable-semaglutide/tile-04-y04880.png
  claim: The footer social icons are clean enough, but they feel like default platform marks rather than an extension of the site's custom icon language.
  visible_tells:
    - Instagram, Facebook, and Twitter/X icons appear as simple white outline marks.
    - They are placed under "START A CONVERSATION" in the same footer column as the newsletter label.
    - The platform silhouettes differ from the medical benefit and symptom icon families elsewhere on the site.
  confidence: high
```

## Provenance

Tiles read: homepage (6) + how-it-works (5) + our-story (4) + mens-weight-loss (7) + pdp-injectable-semaglutide (6) = 28 active tiles from `captures/2026-06-04/tiles/`, all cited tiles straight from the cached Firecrawl payloads. QA gate: clean - overview contact sheet plus native tile spot-checks showed no modal, cookie strip, grey/WebGL hero, black media, lazy-load gap, mid-animation state, or content-covering overlay; the small bottom-corner support widget visible on some footer tiles does not cover evidence-bearing content. No exclusions and no Tier-B browser re-render.

Mined as a blind tiles-only pass in Codex on 2026-06-17: no `profile.md`, dossier body, Notion, or live web consulted. The scripted `Workflow(...)` runner referenced by [`/visual-evidence`](../../skills/visual-evidence/SKILL.md) was not exposed in this session, so the cards were authored manually from the active native tiles against [`VISUAL.md`](../../modules/VISUAL.md); the same blinding boundary and lint contract were preserved. Every `poor` structural card was spot-checked against its native tile and reflects visible page state, not capture contamination. Snapshot caveat: reflects the 2026-06-04 cached capture; the live site changes.
