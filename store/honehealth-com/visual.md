---
schema_version: "1.0"
domain: honehealth.com
captured_at: 2026-06-14
source_capture: 2026-05-31
qa_status: clean
---

## Visual & brand impression

Hone reads as a controlled editorial health brand: acid yellow, black, and white carry the site from ticker to CTA to footer [color_01][color_03]. The type system does real work, pairing oversized serif headlines with small all-caps UI labels and restrained sans body [typography_01][typography_02], though the repeated top ticker/navigation gets busy [typography_03]. Layout is strongest in structured systems: the vertical process spine, pricing split, and dark footer hold together cleanly [layout_01][layout_02][layout_04]. The messier moments are horizontal story rails that visibly clip at the viewport edge [layout_03]. Imagery is most ownable when product/app composites and branded delivery scenes appear [color_02][color_04], while the icon set is consistent but generic [iconography_01].

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: Homepage hero and yellow editorial band
  tile_path: store/honehealth-com/captures/2026-05-31/tiles/homepage/tile-00-y00000.png
  claim: Large high-contrast serif headlines establish a clear editorial voice, while small all-caps controls and sans labels carry the UI layer around them.
  visible_tells:
  - "Longevity engineered around your biology is set as an oversized serif headline over the portrait hero"
  - "The yellow Formulas Built For You band repeats the same large serif treatment in black"
  - "CTA buttons and nav items use compact all-caps sans labels"
  confidence: high
- id: typography_02
  family: typography_hierarchy
  polarity: strong
  page_or_region: Homepage process section
  tile_path: store/honehealth-com/captures/2026-05-31/tiles/homepage/tile-02-y02440.png
  claim: The process section uses a legible hierarchy of tiny step labels, oversized serif action verbs, bold one-line decks, and regular body text.
  visible_tells:
  - "Step 02. sits small above the main phrase"
  - "Consult & Plan is much larger than the surrounding copy, with Plan italicized"
  - "A bold deck line precedes a smaller regular paragraph"
  confidence: high
  contrast_with: store/honehealth-com/captures/2026-05-31/tiles/homepage/tile-01-y01220.png
- id: typography_03
  family: typography_hierarchy
  polarity: mixed
  page_or_region: Site header ticker and navigation
  tile_path: store/honehealth-com/captures/2026-05-31/tiles/homepage/tile-00-y00000.png
  claim: The top ticker and header navigation keep the brand voice consistent, but they pack many small all-caps labels into two shallow bands.
  visible_tells:
  - "The yellow ticker repeats HOT FLASHES, INFLAMMATION, COGNITION, TRT, BRAIN FOG, and LOW ENERGY across the full width"
  - "The header combines MEN, WOMEN, HOW IT WORKS, THE EDGE BLOG, GET STARTED, and SIGN IN in one narrow row"
  - "Both bands rely on small uppercase text and tight horizontal spacing"
  confidence: high
- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: Homepage process spine
  tile_path: store/honehealth-com/captures/2026-05-31/tiles/homepage/tile-03-y03660.png
  claim: The process area is organized by a strict vertical center rule, with copy and product/app composites alternating across a clean two-column rhythm.
  visible_tells:
  - "A thin vertical rule divides the section down the page"
  - "Optimize & Adapt sits on the left while phone and biomarker cards sit on the right"
  - "The next section title aligns back to the center spine below"
  confidence: high
  contrast_with: store/honehealth-com/captures/2026-05-31/tiles/homepage/tile-06-y07320.png
- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: Homepage membership pricing split
  tile_path: store/honehealth-com/captures/2026-05-31/tiles/homepage/tile-05-y06100.png
  claim: The membership comparison resolves into a disciplined 50/50 composition with one white tier and one yellow tier using mirrored internal spacing.
  visible_tells:
  - "Hone Basic and Hone Premium occupy equal-width vertical halves"
  - "Feature lists, plan labels, and price blocks align to matching left edges inside each half"
  - "The yellow right half makes the premium tier visually dominant without changing the component shape"
  confidence: high
- id: layout_03
  family: layout_composition_components
  polarity: poor
  page_or_region: Homepage customer story rail
  tile_path: store/honehealth-com/captures/2026-05-31/tiles/homepage/tile-06-y07320.png
  claim: The customer-story carousel visibly breaks containment, with edge cards and quote text clipped by the viewport rather than resolved into a complete row.
  visible_tells:
  - "The first portrait card is cut off at the left edge"
  - "A partial story card is visible at the far right edge"
  - "Several quote blocks sit below cards in uneven vertical positions"
  confidence: high
  contrast_with: store/honehealth-com/captures/2026-05-31/tiles/homepage/tile-07-y08540.png
- id: layout_04
  family: layout_composition_components
  polarity: strong
  page_or_region: Footer CTA and link columns
  tile_path: store/honehealth-com/captures/2026-05-31/tiles/homepage/tile-09-y10509.png
  claim: The dark footer is cleanly staged with a centered CTA zone above a four-column link grid, then small legal copy and trust badges held in the lower band.
  visible_tells:
  - "The ghosted HONE wordmark spans the black CTA area without obscuring the white headline"
  - "Footer links are grouped into four columns with consistent headers"
  - "LegitScript and Trustpilot badges are isolated at the lower right"
  confidence: high
- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: Site-wide yellow, black, and white system
  tile_path: store/honehealth-com/captures/2026-05-31/tiles/homepage/tile-00-y00000.png
  claim: A high-contrast acid-yellow, black, and white palette governs the visible system, making CTAs, ticker bands, and editorial panels read as one brand language.
  visible_tells:
  - "The symptom ticker and CTA buttons use the same saturated yellow"
  - "The Menopause Time Off band shifts to black while retaining yellow CTA accents"
  - "The large Formulas Built For You panel uses the same yellow as a full-width color field"
  confidence: high
  contrast_with: store/honehealth-com/captures/2026-05-31/tiles/homepage/tile-09-y10509.png
- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: Product and app composite card
  tile_path: store/honehealth-com/captures/2026-05-31/tiles/homepage/tile-04-y04880.png
  claim: Product photography, translucent UI cards, and a yellow tab state are composed into a polished owned treatment rather than a plain stock image block.
  visible_tells:
  - "The testosterone package, pump, vial, and syringe are staged in one rounded image card"
  - "A translucent grey copy panel overlays the product photo"
  - "The active Testosterone tab repeats the brand yellow beneath the card"
  confidence: high
- id: color_03
  family: color_brand_imagery
  polarity: strong
  page_or_region: Dark footer identity treatment
  tile_path: store/honehealth-com/captures/2026-05-31/tiles/homepage/tile-09-y10509.png
  claim: The footer uses a restrained black-on-charcoal wordmark treatment with small yellow accents, giving the closing section a distinct branded signature.
  visible_tells:
  - "Oversized HONE letters appear in dark charcoal behind the CTA"
  - "A small yellow triangular mark sits above the white CTA headline"
  - "The support email and appointment button carry the same yellow accent"
  confidence: high
- id: color_04
  family: color_brand_imagery
  polarity: mixed
  page_or_region: How-it-works hero photography
  tile_path: store/honehealth-com/captures/2026-05-31/tiles/how-it-works/tile-00-y00000.png
  claim: The service photo becomes more ownable because the subjects hold branded Hone boxes, though the underlying lifestyle delivery scene remains conventional.
  visible_tells:
  - "Both people in the hero hold black boxes with yellow HONE marks"
  - "The image uses a familiar doorstep-delivery lifestyle setup"
  - "A translucent white title band overlays the lower half of the photo"
  confidence: high
- id: iconography_01
  family: iconography_illustration
  polarity: mixed
  page_or_region: How-it-works treatment icon grid
  tile_path: store/honehealth-com/captures/2026-05-31/tiles/how-it-works/tile-03-y03660.png
  claim: The treatment grid uses a consistent thin-line icon style, but the symbols are generic category marks rather than a highly distinctive illustration system.
  visible_tells:
  - "Eight cards use black line icons above short labels"
  - "The icon set includes gender symbols, a stethoscope, a heart, chat bubbles, a molecule, and a rocket"
  - "Every card repeats the same light border, centered icon, and centered text rhythm"
  confidence: high
- id: iconography_02
  family: iconography_illustration
  polarity: strong
  page_or_region: Repeated brand mark and CTA arrow motif
  tile_path: store/honehealth-com/captures/2026-05-31/tiles/mens-trt/tile-00-y00000.png
  claim: The small triangular mark and compact play-arrow motif repeat across hero, yellow panel, and CTA controls, giving the interface a recognizable micro-icon language.
  visible_tells:
  - "A triangular line mark sits centered above Formulas Built For You"
  - "The Get Started button includes a small right-pointing triangular arrow"
  - "The same triangle mark appears on the yellow panel directly below the hero"
  confidence: high
  contrast_with: store/honehealth-com/captures/2026-05-31/tiles/homepage/tile-00-y00000.png
```

## Provenance

Tiles read: `store/honehealth-com/captures/2026-05-31/tiles/homepage/`, `store/honehealth-com/captures/2026-05-31/tiles/membership-pricing/`, `store/honehealth-com/captures/2026-05-31/tiles/how-it-works/`, `store/honehealth-com/captures/2026-05-31/tiles/hone-at-home/`, `store/honehealth-com/captures/2026-05-31/tiles/mens-trt/`, and `store/honehealth-com/captures/2026-05-31/tiles/womens-menopause/`, generated from cached `.payloads` screenshots with `scripts/tile.py`.

QA note: Tier-A cached tiles only. Overview and native-tile inspection found no modal, cookie banner, blank hero, black media placeholder, or lazy-load gap requiring exclusion or Tier-B browser re-render. No exclusions.

Run note: generated by Codex + GPT-5.5 on 2026-06-14.

Snapshot caveat: this visual evidence reflects the 2026-05-31 captured tiles; the live site may have changed.
