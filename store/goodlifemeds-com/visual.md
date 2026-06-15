---
schema_version: "1.0"
domain: goodlifemeds.com
captured_at: 2026-06-15
source_capture: 2026-06-04
qa_status: recapture-used
---

# Good Life Meds — visual evidence

## Visual & brand impression

Good Life leads with brand and color. Owned matte-black packaging and per-SKU color art direction [color_02, color_03] carry a category-level theming system — green for weight-loss and wellness, warm amber-terracotta for sexual health [color_04] — and the studio packaging render is the single strongest asset [iconography_04]. Typography is confident up top: a cinematic hero with clear display hierarchy [typography_01] and a systematic four-level footer [typography_06], over generous negative space and a disciplined, repeating product-card system [layout_01, layout_02]. Finish slips below the fold — an undifferentiated all-caps ticker [typography_09], a lopsided Health-Guide jump [typography_10], low-contrast process steps [layout_07], unnormalized testimonial cards [layout_11], generic trust glyphs and thin iconography [iconography_01, iconography_07], and stock-photo palette breaks in portraits and blog thumbnails [color_06, color_09].

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: "homepage hero"
  tile_path: "store/goodlifemeds-com/captures/2026-06-15/tiles/homepage/tile-00-y00000.png"
  claim: "The hero headline sits at a confident display size — roughly 4-5x the nav label size — establishing a clear top-level entry point with no competing element at the same weight."
  visible_tells:
    - "White serif/grotesk display headline 'We're simplifying the path to the Good Life' set large and centered over the dark image"
    - "Nav items and the 'Find your treatment' CTA are visibly smaller by a factor of ~4-5x, leaving the headline uncontested at the top of the hierarchy"
  confidence: high
- id: typography_06
  family: typography_hierarchy
  polarity: strong
  page_or_region: "footer — dark section (all pages)"
  tile_path: "store/goodlifemeds-com/captures/2026-06-15/tiles/homepage/tile-11-y12429.png"
  claim: "The dark footer runs a four-level type stack — large white display tagline, all-caps column labels, regular-case link items, and the smallest legal line — consistent and correctly scaled."
  visible_tells:
    - "Display headline 'Transform your health, transform your life' set large in white, the dominant element"
    - "Column labels ('CATEGORIES', 'POPULAR', 'RESOURCES') in all-caps small text forming a labeled-list tier"
    - "Link items below each header are the same small size but regular case — a clear third tier"
    - "'© 2026 Good Life Meds LLC' legal line is the smallest text, correctly at the bottom"
  confidence: high
- id: typography_09
  family: typography_hierarchy
  polarity: poor
  page_or_region: "homepage — top announcement bar"
  tile_path: "store/goodlifemeds-com/captures/2026-06-15/tiles/homepage/tile-00-y00000.png"
  claim: "The top announcement bar runs five short all-caps items at near-identical size and weight, collapsing any hierarchical signal into an undifferentiated ticker."
  visible_tells:
    - "Five short labels (e.g. 'FDA-REGULATED PHARMACIES', '100% ONLINE PROCESS', 'NO MEMBERSHIP REQUIREMENTS') render in the same small all-caps style across the full bar width"
    - "No visual emphasis distinguishes a primary message from the supporting items"
  confidence: high
- id: typography_10
  family: typography_hierarchy
  polarity: poor
  page_or_region: "homepage — 'Health Guide' editorial section"
  tile_path: "store/goodlifemeds-com/captures/2026-06-15/tiles/homepage/tile-08-y09760.png"
  claim: "The 'Health Guide' section heading is set at an oversized display scale that dwarfs the article captions, while the left-column explainer copy is so small it registers as a footnote rather than a supporting sub-head — a lopsided jump with no intermediate tier."
  visible_tells:
    - "'Health Guide' renders in very large display type, roughly 4-5x the article-title size"
    - "Left-column supporting copy ('Expert insights on health, wellness, and modern care') is set in fine text that reads no larger than the article captions"
  confidence: high
  contrast_with: "store/goodlifemeds-com/captures/2026-06-15/tiles/homepage/tile-01-y01220.png"
- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: "homepage — hero section"
  tile_path: "store/goodlifemeds-com/captures/2026-06-15/tiles/homepage/tile-00-y00000.png"
  claim: "The hero deploys a full-bleed cinematic image with a centered headline and a single pill CTA over a minimal nav, producing a confident, uncluttered negative-space composition."
  visible_tells:
    - "Headline floats center with ample dark space around it; single arrow CTA ('Find your treatment') sits beneath with generous breathing room"
    - "Nav bar is minimal: centered wordmark, four category links, one Login — no clutter or competing elements"
  confidence: high
- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: "homepage — product category carousels (Weight Loss / Daily Wellness)"
  tile_path: "store/goodlifemeds-com/captures/2026-06-15/tiles/homepage/tile-03-y03660.png"
  claim: "Product card carousels are a repeating component system applied identically across categories: equal-width cards, consistent padding, identical 'Get started' + 'Learn more' button pair, aligned product-name typography."
  visible_tells:
    - "Four cards per row at identical height and internal padding in the Weight Loss carousel"
    - "Each card carries the same 'Get started' + 'Learn more' button pair at the same vertical position"
    - "The Daily Wellness carousel mirrors the exact same grid and card anatomy"
  confidence: high
  contrast_with: "store/goodlifemeds-com/captures/2026-06-15/tiles/homepage/tile-04-y04880.png"
- id: layout_07
  family: layout_composition_components
  polarity: mixed
  page_or_region: "homepage — 'How it works' section"
  tile_path: "store/goodlifemeds-com/captures/2026-06-15/tiles/homepage/tile-07-y08540.png"
  claim: "The 'How it works' step list is layered as low-contrast semi-transparent cards over busy packaging photography, making the steps hard to parse and the scan order ambiguous."
  visible_tells:
    - "Step labels render as low-contrast grey-on-dark text overlapping the box photography behind them"
    - "Left-column intro text and step-detail text share similar weight, blurring scan order"
    - "Step numbering is small and does not anchor the eye"
  confidence: medium
- id: layout_11
  family: layout_composition_components
  polarity: poor
  page_or_region: "sexual health — 'Real Stories, Real Results' testimonial row"
  tile_path: "store/goodlifemeds-com/captures/2026-06-15/tiles/sexual_health/tile-04-y04880.png"
  claim: "The three testimonial cards have no height normalization — quote length varies, so card bodies and attribution lines land at different vertical positions, making the row read as unfinished."
  visible_tells:
    - "Center card quote is noticeably longer than the left and right, giving the cards visibly different body heights"
    - "Attribution names ('Sean', 'Nick', 'James') sit at different vertical positions across the three cards"
  confidence: high
- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: "homepage — product packaging section"
  tile_path: "store/goodlifemeds-com/captures/2026-06-15/tiles/homepage/tile-01-y01220.png"
  claim: "Branded packaging (matte black 'Good Life' box, dark-glass vials, consistent labeling, warm cream ground) shows an owned product visual identity rather than assembled stock photography."
  visible_tells:
    - "Matte black 'Good Life' debossed box as the hero object, not a generic medicine image"
    - "Glass vials with matching minimalist labels share the dark-earth palette of the hero"
    - "Warm cream background ties the packaging to the site's neutral ground"
  confidence: high
  contrast_with: "store/goodlifemeds-com/captures/2026-06-15/tiles/semaglutide/tile-02-y02440.png"
- id: color_03
  family: color_brand_imagery
  polarity: strong
  page_or_region: "semaglutide PDP — product hero"
  tile_path: "store/goodlifemeds-com/captures/2026-06-15/tiles/semaglutide/tile-00-y00000.png"
  claim: "The PDP uses a saturated forest-green background matched precisely to the green product vial, demonstrating per-SKU color art direction rather than a generic white-background product shot."
  visible_tells:
    - "Rich hunter-green backdrop fills the entire left half of the split layout"
    - "Vial and background are the same green family, creating figure-ground integration"
    - "White 'Semaglutide' label on the vial maintains the site's black-and-white type system"
  confidence: high
- id: color_04
  family: color_brand_imagery
  polarity: strong
  page_or_region: "sexual health — product feature (Ignite Strips)"
  tile_path: "store/goodlifemeds-com/captures/2026-06-15/tiles/sexual_health/tile-05-y06100.png"
  claim: "The Ignite Strips feature uses a warm brown-red gradient background that echoes the sexual-health hero's amber palette, showing intentional category-level color theming distinct from the weight-loss green."
  visible_tells:
    - "Reddish-brown gradient background, warm and clearly distinct from the cooler greens of the weight-loss SKUs"
    - "Black sachet with large white 'G' monogram floats cleanly against it — a planned, staged-studio contrast with foreground surface reflections"
  confidence: high
- id: color_06
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "homepage — social proof / testimonials ('Trusted by thousands')"
  tile_path: "store/goodlifemeds-com/captures/2026-06-15/tiles/homepage/tile-05-y06100.png"
  claim: "The testimonial portraits vary significantly in lighting, background and framing — four different ambient palettes in one section — undermining the tight palette discipline shown elsewhere on the site."
  visible_tells:
    - "Five portrait crops with distinct ambient palettes: one bright indoor, one neutral studio, one dark blue-grey, one warm-beige"
    - "No unifying overlay, vignette or background treatment is applied to bring the set together"
  confidence: high
  contrast_with: "store/goodlifemeds-com/captures/2026-06-15/tiles/homepage/tile-00-y00000.png"
- id: color_09
  family: color_brand_imagery
  polarity: poor
  page_or_region: "sexual health — Health Guide article thumbnails"
  tile_path: "store/goodlifemeds-com/captures/2026-06-15/tiles/sexual_health/tile-01-y01220.png"
  claim: "Blog article thumbnails are unfiltered stock photography with mismatched warm and cool tones, breaking the palette continuity established by the hero and product sections above."
  visible_tells:
    - "Three article cards with incompatible ambient palettes side by side: a cool-green outdoor scene, a warm indoor scene, and a cool blue-sky beach scene"
    - "No color overlay or consistent crop treatment normalizes the set; the cool beach sky conflicts with the page's amber hero"
  confidence: high
  contrast_with: "store/goodlifemeds-com/captures/2026-06-15/tiles/sexual_health/tile-00-y00000.png"
- id: iconography_01
  family: iconography_illustration
  polarity: poor
  page_or_region: "homepage — trust pillars row"
  tile_path: "store/goodlifemeds-com/captures/2026-06-15/tiles/homepage/tile-02-y02440.png"
  claim: "The four trust-pillar icons are tiny, flat, monochrome glyphs with no custom stroke personality or enclosure — indistinguishable from generic system-UI icons."
  visible_tells:
    - "All four icons render at the same small size with no discernible stroke personality"
    - "Icons sit above plain label text with no color accent, enclosure or sizing hierarchy signaling intentional craft"
  confidence: high
- id: iconography_04
  family: iconography_illustration
  polarity: strong
  page_or_region: "homepage — product packaging / unboxing photo"
  tile_path: "store/goodlifemeds-com/captures/2026-06-15/tiles/homepage/tile-01-y01220.png"
  claim: "The matte-black 'Good Life' debossed box with a curated product arrangement is shot at a near-isometric angle with studio lighting, functioning as a premium product render and the strongest single visual asset on the homepage."
  visible_tells:
    - "Box lid and contents are in sharp focus with consistent warm-key lighting and no visible clipping or color fringing"
    - "Multiple objects (vials, insert card, box lid) are composed inside the frame in a styled, non-documentary way"
  confidence: high
  contrast_with: "store/goodlifemeds-com/captures/2026-06-15/tiles/homepage/tile-02-y02440.png"
- id: iconography_07
  family: iconography_illustration
  polarity: mixed
  page_or_region: "homepage — floating UI chips on lifestyle photo ('Medical support, on your terms')"
  tile_path: "store/goodlifemeds-com/captures/2026-06-15/tiles/homepage/tile-06-y07320.png"
  claim: "The floating UI chips (weight readout, doctor-message chip, product card) overlaid on the lifestyle photo are a competent illustrative device, but the chip-level iconography is generic and small enough to read as template-sourced."
  visible_tells:
    - "Doctor chip uses a small circular avatar with no custom border or badge treatment"
    - "Weight chip shows a plain bold '165lbs' numeral with no icon tying it to the brand"
  confidence: medium
```

## Provenance

- **Tiles read.** 40 native-resolution viewport tiles across four pages carrying the visual system: homepage (12), weight-loss category (9), sexual-health category (8), and the semaglutide PDP (11). Overview strips were built per page for the QA scan.
- **QA — `recapture-used`.** The cached 2026-06-04 Firecrawl screenshots were contaminated site-wide by a **Transcend consent overlay** ("Your Privacy Choices" / Allow / Don't Allow), stamped into the bottom-right of every page and repeated down each one — covering content (e.g. a homepage testimonial card). Click-dismissal missed it (duplicate widget + closed shadow root), so all four pages were **re-rendered Tier-B** in system Chrome (`scripts/shoot.py`, no Firecrawl spend) with the consent mount hidden. Re-rendered tiles are clean of the overlay; animations settled (the weight-loss count-up resolves to a real value; the semaglutide teal "0" is a genuine empty-input BMI calculator, not a stuck count-up). No tiles were excluded; no card depends on a modal/blank/black/artifact region.
- **Mining + judge.** Blind fan-out (4 family miners, Sonnet, tiles-only) → judge (Opus) verified every cited PNG. Miners produced 47 raw cards; the judge accepted 38 (17 strong / 14 mixed / 7 poor) and rejected 6 as evidence-contradicted or overstated taste reads. Judge cross-tile flag: the footer CTA accent is **category-themed, not a single site accent** (green on the homepage, terracotta on sexual-health) — captured positively in [color_04].
- **Curation.** This file carries a curated **16 of the 38** accepted cards (8 strong / 3 mixed / 5 poor, all four families), keeping the judge's verbatim cards and ids while dropping near-duplicate repeats of the same tell (e.g. six "clean hierarchy" strong-typography cards collapse to two; three "consistent product-card system" cards to one). The full 38-card judge set lives in the run transcript.
- **Snapshot caveat.** A point-in-time read of tiles re-rendered 2026-06-15 from a 2026-06-04 capture; the live site may have changed since.
