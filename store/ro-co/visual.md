---
schema_version: "1.0"
domain: ro.co
captured_at: 2026-06-14
source_capture: 2026-06-04
qa_status: recapture-used
---

## Visual & brand impression

Restrained, editorial DTC-health design that reads premium because it is disciplined, not decorated. A large coral-on-black display headline over a one-accent palette sets a confident tone [typography_01][color_01], and the same rigor recurs as component systems — aligned pricing-card grids [layout_01], a reused left-rail category rhythm [layout_02], and an evenly-built goal selector [layout_06]. The ro.OS pages are the high point: product UIs floated on owned watercolor-gradient blobs [color_04] beside a custom monogram-token set [iconography_01][layout_07], with photography art-directed to brand color [color_03]. It frays at small scale — literal loose-pill ED thumbnails [iconography_06] and a mismatched product-photo category strip [color_06] read inventory-driven, and a competing magenta Most-popular tag [color_02] nicks the otherwise tight accent discipline.

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: pricing page hero
  tile_path: store/ro-co/captures/2026-06-04/tiles/pricing/tile-00-y00000.png
  claim: The hero headline 'Transparent pricing, always' is set at a large display grotesque that dominates the viewport and clearly outranks the smaller gray supporting line beneath it.
  visible_tells:
  - Headline spans roughly half the page width at a single line height
  - Color split (coral 'Transparent pricing' vs black 'always') reinforces emphasis within one type size
  - Supporting paragraph below drops to a markedly smaller gray weight
  confidence: high
- id: typography_02
  family: typography_hierarchy
  polarity: strong
  page_or_region: pricing — left-rail category heading ("Hair loss")
  tile_path: store/ro-co/captures/2026-06-04/tiles/pricing/tile-02-y02440.png
  claim: The left-rail category title 'Hair loss' is set several steps larger than its explanatory body paragraph with generous leading, the same heading tier reused down the whole pricing page for a consistent scan rhythm.
  visible_tells:
  - '''Hair loss'' title is set well above body size in the same grotesque'
  - Body paragraph sits in a narrow left column with even line spacing
  - A wide whitespace gutter separates the heading tier from the product-card grid
  confidence: high
- id: typography_03
  family: typography_hierarchy
  polarity: strong
  page_or_region: weight-loss FAQ block
  tile_path: store/ro-co/captures/2026-06-04/tiles/weight-loss/tile-07-y08540.png
  claim: The 'Weight loss FAQs' and 'Important safety information' headings sit at a clearly larger weight than the uniformly-sized accordion questions, giving a legible two-level hierarchy.
  visible_tells:
  - Section heading is roughly double the question text size
  - Each FAQ row uses identical size/weight with a right-aligned chevron, reading as one consistent tier
  - '''Show more'' link is demoted with smaller underlined text'
  confidence: high
- id: typography_04
  family: typography_hierarchy
  polarity: strong
  page_or_region: homepage category list (above footer)
  tile_path: store/ro-co/captures/2026-06-04/tiles/homepage/tile-07-y07461.png
  claim: The vertical category list (Weight loss / Sexual health / Hair loss / Fertility / Skin) is set in a calm, evenly-leaded medium weight that reads as a single clean navigational tier, distinct from the smaller two-line article-card titles above.
  visible_tells:
  - Five list items share identical size, weight, and vertical spacing
  - Article-card titles above use a smaller two-line size, keeping tiers distinct
  - '''min read'' metadata is demoted to small gray text'
  confidence: high
- id: typography_05
  family: typography_hierarchy
  polarity: strong
  page_or_region: os page 'Pharmacy App' section intro
  tile_path: store/ro-co/captures/2026-06-04/tiles/os/tile-03-y03660.png
  claim: The 'Pharmacy App' block pairs a small green eyebrow, a large bold title, and a measured body paragraph into a clean three-tier hierarchy with comfortable leading in a fixed-width column.
  visible_tells:
  - Green 'Powered by ro.OS' eyebrow sits small above the title
  - Title is set several steps larger and bold
  - Body sits at readable size with consistent line height in a fixed-width left column
  confidence: high
- id: typography_06
  family: typography_hierarchy
  polarity: mixed
  page_or_region: pricing ED product card (Ro Sparks)
  tile_path: store/ro-co/captures/2026-06-04/tiles/pricing/tile-00-y00000.png
  claim: Inside the ED pricing cards the dose-plan rows and prices are legible but flat, with the price and label at near-identical weight so the column lacks a clear emphasis anchor.
  visible_tells:
  - '''4x dose plan'' label and ''$48/mo'' price share similar size and weight'
  - Multiple stacked rows read as undifferentiated until the eye lands on the dollar figure
  - Only the 'Most popular' tag adds a color cue to a row elsewhere on the page
  confidence: medium
- id: typography_07
  family: typography_hierarchy
  polarity: mixed
  page_or_region: pricing 'Ro Body' weight-management card
  tile_path: store/ro-co/captures/2026-06-04/tiles/pricing/tile-07-y08540.png
  claim: The Latisse/Custom-Rx pricing cells crowd plan label and a long parenthetical supply caveat into a tight block where the price competes with wrapped fine print rather than stepping above it.
  visible_tells:
  - '''Monthly plan (3 mL, 1 month supply)'' wraps to two lines beside the ''$110'' price'
  - Caveat text sits at the same size as the plan label with no clear size step to the price
  - Adjacent 'Custom Rx Treatment' rows compress label + 'Most popular' + price into one cramped line
  confidence: medium
- id: typography_08
  family: typography_hierarchy
  polarity: poor
  page_or_region: weight-loss overlaid member video-card captions
  tile_path: store/ro-co/captures/2026-06-04/tiles/weight-loss/tile-07-y08540.png
  claim: Caption text burned onto the member video cards ('lack self-discipline.', 'and a half on Ro.') sits as small white type over busy mid-tone footage where legibility drops and words compete with the image.
  visible_tells:
  - White caption text overlaps detailed clothing/background imagery
  - Caption size is small relative to the card
  - Contrast varies across the frame, some words fade into lighter areas
  confidence: medium
- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: pricing page — ED pricing card grid
  tile_path: store/ro-co/captures/2026-06-04/tiles/pricing/tile-01-y01220.png
  claim: The ED pricing section runs a disciplined two-column card system where each card repeats the same anatomy (product-box mark + title + Rx glyph, a left-label/right-price dose table, a pill 'Get started' CTA, then a tinted disclosure block) so rows align cleanly across cards.
  visible_tells:
  - Generic Viagra and Branded Viagra cards share width, corner radius, and a common baseline grid
  - Dose rows (25/50/100 mg) align horizontally between cards with prices flush-right
  - '''Most popular'' inline tag and the grey safety-info block repeat in the same position per card'
  confidence: high
- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: pricing page — left-rail section rhythm (Hair loss)
  tile_path: store/ro-co/captures/2026-06-04/tiles/pricing/tile-02-y02440.png
  claim: 'The page sustains a left-rail label pattern: each category sets a large left-aligned heading plus body copy in a narrow left column while product cards occupy the right two-thirds, giving every section the same predictable scan rhythm.'
  visible_tells:
  - '''Hair loss'' heading and its paragraph anchor the left column while a 2x2 card grid fills the right'
  - The same left-column width is reused as in the ED section above
  - Generous whitespace gutter separates the text rail from the card cluster
  confidence: high
  contrast_with: store/ro-co/captures/2026-06-04/tiles/pricing/tile-04-y04880.png
- id: layout_03
  family: layout_composition_components
  polarity: strong
  page_or_region: os page — Care Delivery / Pharmacy feature blocks
  tile_path: store/ro-co/captures/2026-06-04/tiles/os/tile-02-y02440.png
  claim: The ro.OS feature sections use a calm editorial layout — left eyebrow/heading/body/CTA stack balanced against a floated product-UI mock on a soft gradient blob — with deliberate large whitespace giving each module breathing room.
  visible_tells:
  - '''Care Delivery App'' eyebrow/heading/body/CTA stack is left-aligned with wide margins'
  - The Patient Overview UI mock floats right over a soft blue gradient shape
  - Very high whitespace-to-content ratio isolates the single module on the tile
  confidence: high
  contrast_with: store/ro-co/captures/2026-06-04/tiles/os/tile-03-y03660.png
- id: layout_04
  family: layout_composition_components
  polarity: strong
  page_or_region: weight-loss / homepage — FAQ accordion + four-column footer
  tile_path: store/ro-co/captures/2026-06-04/tiles/weight-loss/tile-07-y08540.png
  claim: 'The FAQ accordion and four-column footer are cleanly aligned systems: each FAQ row is a full-width rule-divided line with a right-aligned chevron, and the footer columns (Popular / About Ro / Support / Legal) sit on a shared baseline with even gutters.'
  visible_tells:
  - '''Weight loss FAQs'' rows each end with a chevron at a consistent right margin and equal vertical spacing'
  - Footer's four link columns start at the same top baseline with matching label-to-link spacing
  - Background shift (light-grey FAQ vs near-black footer) cleanly demarcates the two modules
  confidence: high
- id: layout_05
  family: layout_composition_components
  polarity: mixed
  page_or_region: pricing page — uneven paired-card heights
  tile_path: store/ro-co/captures/2026-06-04/tiles/pricing/tile-01-y01220.png
  claim: 'Within a single row the paired cards are not height-matched: the Generic Viagra card carries an extra tinted safety block while the Branded Viagra card leaves a tall empty gap before its CTA, so the two cards end at different heights.'
  visible_tells:
  - Generic Viagra card has a grey safety-info panel filling its lower third
  - Branded Viagra card shows a large blank gap between its 100 mg price row and the 'Get started' button
  - The two cards' bottom edges do not terminate level despite being a horizontal pair
  confidence: medium
  contrast_with: store/ro-co/captures/2026-06-04/tiles/pricing/tile-02-y02440.png
- id: layout_06
  family: layout_composition_components
  polarity: strong
  page_or_region: homepage — treatment-goal selector grid
  tile_path: store/ro-co/captures/2026-06-04/tiles/homepage/tile-03-y03660.png
  claim: The 'Prescription treatments for your health goals' block lays a six-cell goal grid (Lose weight, Unlock better sex, Regrow hair, Improve skin, Get fertility insights, New from Ro) as evenly sized tiles each with a leading icon and trailing circular arrow, a consistently built selector component.
  visible_tells:
  - Six goal tiles arranged in a 3x2 grid with equal cell sizing
  - Each tile pairs a small left thumbnail with a circular arrow button at right
  - The grid sits in a band with uniform tile padding
  confidence: high
- id: layout_07
  family: layout_composition_components
  polarity: strong
  page_or_region: os page — 'Explore all ro.OS capabilities' chip grid
  tile_path: store/ro-co/captures/2026-06-04/tiles/os/tile-04-y04880.png
  claim: The capabilities row is a clean repeated badge-tile system — seven equal tiles each with a circular two-letter monogram and a label below — evenly spaced with a pager, reading as a deliberate component set.
  visible_tells:
  - Seven tiles (Patient Intake, Care Comms, Patient Identity, Health Tasks, Insurance, Quality & Safety, Health Data) at equal width
  - Each carries a colored circular monogram (Pi, Cc, Id, Ht, In, Qu, Hd) in matching style
  - Consistent gutters and a centered pager beneath the row
  confidence: high
- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: pricing page hero accent
  tile_path: store/ro-co/captures/2026-06-04/tiles/pricing/tile-00-y00000.png
  claim: A single saturated coral-red accent is used with discipline, coloring only the 'Transparent pricing' phrase against otherwise black/white type, signaling a controlled one-accent system.
  visible_tells:
  - '''Transparent pricing,'' set in vivid coral-red while ''always'' stays black'
  - Same coral reappears only in the product-box marks below, not scattered through the layout
  confidence: high
  contrast_with: store/ro-co/captures/2026-06-04/tiles/pricing/tile-01-y01220.png
- id: color_02
  family: color_brand_imagery
  polarity: mixed
  page_or_region: pricing — 'Most popular' label hue
  tile_path: store/ro-co/captures/2026-06-04/tiles/pricing/tile-01-y01220.png
  claim: A purple/magenta 'Most popular' label introduces a second accent hue that competes with the coral brand red, slightly diluting palette discipline on the pricing tables.
  visible_tells:
  - '''Most popular'' rendered in purple-magenta next to dose rows'
  - This purple does not match the coral red used in the same page's hero and packaging
  confidence: medium
  contrast_with: store/ro-co/captures/2026-06-04/tiles/pricing/tile-00-y00000.png
- id: color_03
  family: color_brand_imagery
  polarity: strong
  page_or_region: weight-loss 'Healthier on Ro' band
  tile_path: store/ro-co/captures/2026-06-04/tiles/weight-loss/tile-03-y03660.png
  claim: A full-bleed lavender-purple band with a color-matched portrait shows owned, art-directed photography keyed to a brand color rather than dropped-in stock.
  visible_tells:
  - Even lavender-purple background filling the band
  - Subject's top tinted the same lavender, white headline and black pill button reading cleanly on top
  confidence: high
- id: color_04
  family: color_brand_imagery
  polarity: strong
  page_or_region: os page — app-UI gradient treatment
  tile_path: store/ro-co/captures/2026-06-04/tiles/os/tile-02-y02440.png
  claim: Product-UI screenshots float on soft blue/green watercolor gradients applied consistently across the Care Delivery, Pharmacy, and Lab app sections, giving the OS imagery a unified owned treatment.
  visible_tells:
  - Patient Overview UI card sits on a pale blue gradient cloud
  - The same gradient-cloud-behind-floating-UI device repeats on the Pharmacy and Lab tiles
  confidence: high
  contrast_with: store/ro-co/captures/2026-06-04/tiles/os/tile-03-y03660.png
- id: color_05
  family: color_brand_imagery
  polarity: strong
  page_or_region: footer (site-wide)
  tile_path: store/ro-co/captures/2026-06-04/tiles/homepage/tile-07-y07461.png
  claim: The near-black footer with white wordmark and a single LegitScript trust badge is applied identically across pages, reinforcing a consistent brand frame and restrained palette.
  visible_tells:
  - Charcoal-black footer, white 'ro' wordmark, hexagonal LegitScript badge
  - Identical layout repeats on the weight-loss and pricing footers
  confidence: high
  contrast_with: store/ro-co/captures/2026-06-04/tiles/pricing/tile-08-y09671.png
- id: color_06
  family: color_brand_imagery
  polarity: poor
  page_or_region: pricing category icon strip
  tile_path: store/ro-co/captures/2026-06-04/tiles/pricing/tile-00-y00000.png
  claim: The horizontal category nav uses tiny mismatched product-photo thumbnails (varied bottle colors, sprays, blister packs) instead of a unified icon set, reading as assembled product shots rather than a designed system.
  visible_tells:
  - Row of inconsistent mini product shots for Hair loss, Cold sores, Men's multivitamin, Testosterone support, etc.
  - Differing product silhouettes, scales, and colors with no shared icon language
  confidence: medium
- id: iconography_01
  family: iconography_illustration
  polarity: strong
  page_or_region: os page — capability monogram chips
  tile_path: store/ro-co/captures/2026-06-04/tiles/os/tile-04-y04880.png
  claim: The 'Explore all ro.OS capabilities' row uses a custom set of circular two-letter monogram tokens (Pi, Cc, Id, Ht, In, Qu, Hd), each in its own pastel hue, giving a consistent and distinctive token set.
  visible_tells:
  - Seven uniform circular badges with bold two-letter abbreviations
  - Each badge a different pastel fill over a light card, at matched size and type treatment
  confidence: high
  contrast_with: store/ro-co/captures/2026-06-04/tiles/pricing/tile-00-y00000.png
- id: iconography_02
  family: iconography_illustration
  polarity: strong
  page_or_region: hair-loss — feature-strip icons under hero
  tile_path: store/ro-co/captures/2026-06-04/tiles/hair-loss/tile-00-y00000.png
  claim: The three-up benefit strip pairs thin-line outline icons (spray/serum mark, shipping box, chat bubble) at a single consistent stroke weight and size.
  visible_tells:
  - Three monoline icons centered above 'Spray, serum...', 'Free shipping...', 'Unlimited messaging' labels
  - Uniform thin stroke and matched optical size across all three
  confidence: medium
- id: iconography_03
  family: iconography_illustration
  polarity: strong
  page_or_region: pricing — branded product-box marks (SIL/CIA)
  tile_path: store/ro-co/captures/2026-06-04/tiles/pricing/tile-01-y01220.png
  claim: The Generic/Branded Viagra and Cialis cards reuse crisp branded box marks ('SIL', 'CIA' in red on black) that are sharp and consistently lit across multiple cards.
  visible_tells:
  - Repeated red-on-black 'SIL' and 'CIA' box thumbnails beside each card title
  - Clean edges and consistent framing at small thumbnail size
  confidence: high
- id: iconography_04
  family: iconography_illustration
  polarity: strong
  page_or_region: weight-loss — Rx product photography
  tile_path: store/ro-co/captures/2026-06-04/tiles/weight-loss/tile-01-y01220.png
  claim: The GLP-1 product cards (Wegovy pill, Zepbound KwikPen, Foundayo pill, Wegovy pen) use studio product photography with even lighting and soft shadows on tinted card backgrounds.
  visible_tells:
  - Four product shots on tinted card backgrounds with consistent soft shadowing
  - Pill and pen renders sharp with realistic material detail
  confidence: medium
- id: iconography_05
  family: iconography_illustration
  polarity: strong
  page_or_region: pricing — Rx (Rx) glyph beside product names
  tile_path: store/ro-co/captures/2026-06-04/tiles/pricing/tile-01-y01220.png
  claim: A consistent Rx glyph sits immediately after every prescription product name (Generic Viagra, Generic of Cialis, Branded Cialis), a coherent typographic mark applied uniformly.
  visible_tells:
  - Identical small Rx symbol trailing each bold product title
  - Mark reused at matched size across all Rx cards on the tile
  confidence: high
- id: iconography_06
  family: iconography_illustration
  polarity: poor
  page_or_region: homepage — ED carousel literal-pill thumbnails
  tile_path: store/ro-co/captures/2026-06-04/tiles/homepage/tile-02-y02440.png
  claim: The ED product carousel relies on literal loose-pill photography in mixed colors (red, yellow, white, blue) each on a differently-toned backdrop, so the thumbnail set feels inventory-driven rather than a controlled icon/imagery system.
  visible_tells:
  - Row of red, yellow, white, and blue loose pills as the product thumbnails
  - Each pill on a different grey/blue/tan backdrop rather than one shared treatment
  confidence: medium
  contrast_with: store/ro-co/captures/2026-06-04/tiles/weight-loss/tile-01-y01220.png
```

## Provenance

Tiles read: homepage (8) + weight-loss (9) + pricing (9) + hair-loss (7) sliced from the cached `captures/2026-06-04/.payloads/` screenshots (Tier-A), plus os (8) browser re-rendered (Tier-B) — 41 tiles, all active, no exclusions. **Tier-B re-render:** the `os` page's cached Firecrawl capture left the Care Delivery / Pharmacy / Lab app-illustration columns empty (scroll-triggered lazy media that never fired); `scripts/shoot.py` drove system Chrome to warm-scroll and settle, recovering the product-UI mockups on their gradient blobs (19/23 images loaded) — hence `qa_status: recapture-used`. The other four pages tiled clean from cached payloads.

Mined blind + judged per [`/visual-evidence`](../../skills/visual-evidence/SKILL.md): four family miners saw only the tile paths (no dossier, no web), returning 56 raw cards; the judge verified each against the cited PNG and kept 28. A synthesis verification pass against a hand-built tile-content map then dropped 1 redundant card (a duplicate read of the pricing category strip) and retargeted 1 mis-cited card (`typography_02`, which cited a 'Cold sores' heading not present in its tile — corrected to the 'Hair loss' heading the tile actually shows) → **27 final cards**. The judge flagged a render-scale split in this capture set (several homepage / weight-loss / os / hair-loss tiles are zoomed-out captures where the page shrinks into the upper frame); 'tiny illegible text' reads on those were treated as capture caveats, not design defects.

Snapshot caveat: reflects the 2026-06-04 capture (os section re-rendered 2026-06-14); the live site changes. Run note: executed from **Claude Code on macOS**, model **Claude Opus 4.8**, **Extra effort** reasoning.
