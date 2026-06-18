---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.0"
domain: bullish.co
captured_at: 2026-06-18
source_capture: 2026-06-18
qa_status: exclusions-noted
---

## Visual & brand impression

Bullish commits hard to one idea: a single high-chroma electric blue as the whole canvas — hero, nav, and About page all sit on uninterrupted blue [color_01][color_04], with editorial cards held to a tight blue / black / off-white set [color_02] and a navy-on-blue services grid that extends the family rather than breaking it [color_03]. The hero is one reductive gesture: an oversized geometric-sans wordmark alone on the field [typography_01][layout_01]. Type pairs a display serif against small sans labels with confidence [typography_03], carried into a disciplined masonry card grid [layout_02] and equal-width approach panels [layout_03]. Where it slips is density — the 24-cell services grid and ~40-name client list are flat, hierarchy-free text fields [typography_05][layout_08], the footer reads unbalanced [layout_09], and there is essentially no icon or illustration system [iconography_01].

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: "homepage hero"
  tile_path: "store/bullish-co/captures/2026-06-18/tiles/homepage/tile-00-y00000.png"
  claim: "The hero is a single geometric sans-serif wordmark set at extreme display scale, filling nearly the full viewport width on a flat blue field — hierarchy enforced by total emptiness around it."
  visible_tells:
    - "One word 'Bullish' in a bold geometric sans fills almost the entire tile width"
    - "No competing text, nav, or tagline anywhere in the tile"
  confidence: high
  contrast_with: "store/bullish-co/captures/2026-06-18/tiles/homepage/tile-01-y01220.png"

- id: typography_02
  family: typography_hierarchy
  polarity: strong
  page_or_region: "homepage — hero tagline below wordmark"
  tile_path: "store/bullish-co/captures/2026-06-18/tiles/homepage/tile-01-y01220.png"
  claim: "The tagline mixes two type styles inline — a serif roman for most of the sentence with the words 'capital, consulting' and 'creation' swapped to a heavier sans — creating emphasis through typeface/weight contrast rather than size."
  visible_tells:
    - "'capital, consulting' and 'creation' render in a visibly heavier, different (sans) face than the surrounding serif words"
    - "Emphasis lands without any size change, all on a centered block over blue"
  confidence: high

- id: typography_03
  family: typography_hierarchy
  polarity: strong
  page_or_region: "about page — page hero / H1"
  tile_path: "store/bullish-co/captures/2026-06-18/tiles/about/tile-00-y00000.png"
  claim: "A high-contrast serif carries the page-level H1 at large display scale, set clearly apart from the small sans-serif 'Approach' label and sans card titles below it — a deliberate serif-display vs sans-label split."
  visible_tells:
    - "Large serif 'We partner with companies that embrace creativity…' headline dominates the top of the page"
    - "'Approach' label and 'Capital/Consulting/Creative' card titles are small sans, roughly a quarter of the H1 size"
  confidence: high
  contrast_with: "store/bullish-co/captures/2026-06-18/tiles/homepage/tile-00-y00000.png"

- id: typography_04
  family: typography_hierarchy
  polarity: strong
  page_or_region: "homepage — content card grid"
  tile_path: "store/bullish-co/captures/2026-06-18/tiles/homepage/tile-02-y02440.png"
  claim: "Editorial cards run a consistent three-level type order — a small sans category label ('Insights'/'News') at top, a larger serif title below, and a tiny sans metadata tag pinned at the bottom — legible and repeated across every card."
  visible_tells:
    - "Blue cards show small sans 'Insights' above a larger serif title ('Cultural Theme: Ubiquitous Wellness'), with 'Capital, Creative, Consulting' in tiny type at the lower edge"
    - "The label-to-title size step repeats identically across multiple cards in the tile"
  confidence: high

- id: typography_05
  family: typography_hierarchy
  polarity: poor
  page_or_region: "about page — services grid"
  tile_path: "store/bullish-co/captures/2026-06-18/tiles/about/tile-01-y01220.png"
  claim: "The 24-item services grid sets every label in one identical sans size, weight, and color on identical navy cards — a flat typographic field with zero hierarchy or grouping to guide the eye."
  visible_tells:
    - "'Advertising', 'Brand Architecture', 'Consumer Decision Journeys', 'Visual Identity' etc. all share the same size/weight/color"
    - "No grouping header, accent, or size variation differentiates any of the 24 cells"
  confidence: high

- id: typography_06
  family: typography_hierarchy
  polarity: poor
  page_or_region: "about page — engagements list"
  tile_path: "store/bullish-co/captures/2026-06-18/tiles/about/tile-02-y02440.png"
  claim: "The engagements client list renders ~40 names in a single uniform sans size and weight, with only the small 'Engagements' label barely set apart — no typographic differentiation among any client names."
  visible_tells:
    - "'Anheuser-Busch', 'August', 'Bandit', 'Horizon Hobby' etc. all share one identical type treatment"
    - "The 'Engagements' section label is the same small sans, distinguished only by position not by weight or size"
  confidence: high

- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: "homepage hero"
  tile_path: "store/bullish-co/captures/2026-06-18/tiles/homepage/tile-00-y00000.png"
  claim: "The hero is a full-bleed single-color field holding only an oversized wordmark — a reductive layout that trades all information density for one bold gesture."
  visible_tells:
    - "Electric blue fills 100% of the viewport with no nav, tagline, or CTA visible"
    - "The single word 'Bullish' is the only element on screen"
  confidence: high

- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: "homepage feed — content card grid"
  tile_path: "store/bullish-co/captures/2026-06-18/tiles/homepage/tile-02-y02440.png"
  claim: "A masonry four-column grid applies one disciplined card component — consistent rounded corners, a colored fill, category tag pinned bottom-left, title anchored top-left — repeated cleanly across dozens of items down the full scroll."
  visible_tells:
    - "Uniform corner radius across blue, black, and off-white fill variants"
    - "Category tag sits in the identical bottom-left position on every card"
    - "Four-column cadence holds across many tiles of scroll"
  confidence: high
  contrast_with: "store/bullish-co/captures/2026-06-18/tiles/homepage/tile-04-y04880.png"

- id: layout_03
  family: layout_composition_components
  polarity: strong
  page_or_region: "about page — approach section"
  tile_path: "store/bullish-co/captures/2026-06-18/tiles/about/tile-00-y00000.png"
  claim: "The three approach cards (Capital / Consulting / Creative) are equal-width white panels with equal gutters and identical internal padding on a blue field — crisp structural parallelism."
  visible_tells:
    - "Three cards of exactly equal width with equal gaps between them"
    - "Title and body anchored identically at top-left inside each card"
    - "'Approach' label sits flush-left at the same distance above all three"
  confidence: high

- id: layout_04
  family: layout_composition_components
  polarity: strong
  page_or_region: "about page — services grid"
  tile_path: "store/bullish-co/captures/2026-06-18/tiles/about/tile-01-y01220.png"
  claim: "The services grid is a strict six-column system of deep-navy rounded cards with center-aligned labels — every cell holds equal proportions and uniform row heights across four rows, even with multi-line labels."
  visible_tells:
    - "Six equal-width columns with equal gaps"
    - "Labels center-aligned both horizontally and vertically in every cell"
    - "Row heights stay uniform whether the label is one or two lines"
  confidence: high

- id: layout_05
  family: layout_composition_components
  polarity: strong
  page_or_region: "homepage feed — nav bar"
  tile_path: "store/bullish-co/captures/2026-06-18/tiles/homepage/tile-01-y01220.png"
  claim: "The nav resolves to a spare two-item text menu ('Explore / About') centered, with only a small square icon at far left and a full-width rule beneath — minimal and controlled."
  visible_tells:
    - "Exactly two text links plus one small square glyph; no dropdowns, search, or secondary links"
    - "A full-width horizontal rule separates the nav from the content below"
  confidence: high

- id: layout_06
  family: layout_composition_components
  polarity: mixed
  page_or_region: "about page — team member photos"
  tile_path: "store/bullish-co/captures/2026-06-18/tiles/about/tile-03-y03513.png"
  claim: "The team-photo row breaks the grid discipline of the rest of the About page: only three headshots sit left-aligned with the right half of the row left empty, leaving an unresolved partial row."
  visible_tells:
    - "Three headshots occupy the leftmost columns; the right portion of the row is empty blue"
    - "The three frames share a rounded-square crop but each photo has different lighting and background"
  confidence: medium

- id: layout_07
  family: layout_composition_components
  polarity: mixed
  page_or_region: "homepage — filter slider control"
  tile_path: "store/bullish-co/captures/2026-06-18/tiles/homepage/tile-17-y20740.png"
  claim: "The Capital-to-Creative slider that filters the feed is visually so minimal it reads as low-affordance — a hairline track with a tiny square handle and end labels, with no obvious cue that it is interactive."
  visible_tells:
    - "Slider is a thin full-width line with a small blue square handle and 'Capital'/'Creative' text labels at the ends"
    - "No button styling, tooltip, or fill state signals interactivity at a glance"
  confidence: medium

- id: layout_08
  family: layout_composition_components
  polarity: poor
  page_or_region: "about page — engagements client list"
  tile_path: "store/bullish-co/captures/2026-06-18/tiles/about/tile-02-y02440.png"
  claim: "The client list is plain text in two columns on a blue field with no dividers, headers, or spacing system — structure is alphabetical order alone, with a wide empty left margin that leaves the section visually unanchored."
  visible_tells:
    - "Two columns of names ('Anheuser-Busch'… / 'Horizon Hobby'…) with no rules, micro-labels, or grouping"
    - "The whole left third of the band is empty, the list pushed to the center-right"
  confidence: high

- id: layout_09
  family: layout_composition_components
  polarity: poor
  page_or_region: "homepage footer"
  tile_path: "store/bullish-co/captures/2026-06-18/tiles/homepage/tile-18-y21081.png"
  claim: "The footer leaves the entire center two-thirds empty between the left contact blocks and the right-aligned social links, and the email signup floats far below the contact row with a large gap, so the footer reads as unbalanced and ungrouped."
  visible_tells:
    - "Contact blocks sit far left, social links far right, with a large empty void between them"
    - "The email signup field is separated from the contact row above by a wide vertical gap"
  confidence: high

- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: "homepage hero"
  tile_path: "store/bullish-co/captures/2026-06-18/tiles/homepage/tile-00-y00000.png"
  claim: "The brand commits fully to one high-chroma electric blue as the hero surface — no gradient, texture, or secondary hue — a confident palette reduction with white type the only other element."
  visible_tells:
    - "Full-bleed saturated blue behind the wordmark"
    - "Zero secondary colors in the tile; only white type"
  confidence: high

- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: "homepage card grid"
  tile_path: "store/bullish-co/captures/2026-06-18/tiles/homepage/tile-02-y02440.png"
  claim: "The editorial cards run a tight three-value system — brand blue, near-black, and off-white — applied with discipline across dozens of cards, with text consistently white-on-dark or dark-on-light and no rogue accent colors."
  visible_tells:
    - "Blue, black, and off-white cards interleave across all four columns with no color outliers"
    - "Text contrast is consistently handled by the card fill, no intermediate accent hues"
  confidence: high
  contrast_with: "store/bullish-co/captures/2026-06-18/tiles/homepage/tile-07-y08540.png"

- id: color_03
  family: color_brand_imagery
  polarity: strong
  page_or_region: "about page — services grid (blue-on-blue)"
  tile_path: "store/bullish-co/captures/2026-06-18/tiles/about/tile-01-y01220.png"
  claim: "The services grid extends the palette into a deep near-navy card fill set against the electric-blue page — a layered blue-on-blue treatment that reads as an intentional tonal extension, not drift."
  visible_tells:
    - "All 24 service cards use one deep navy fill, distinct from yet in the same family as the electric-blue background"
    - "The navy-on-blue contrast is consistent and clearly deliberate across the whole grid"
  confidence: high

- id: color_04
  family: color_brand_imagery
  polarity: strong
  page_or_region: "about page — full-page canvas"
  tile_path: "store/bullish-co/captures/2026-06-18/tiles/about/tile-00-y00000.png"
  claim: "Blue is the full-page canvas on the About page, not just a hero band — nav, H1, white approach cards, and navy service tiles all sit on uninterrupted blue, confirming blue as an environment-level brand decision."
  visible_tells:
    - "Nav, display H1, three white cards, and the service row all sit on one continuous blue field"
    - "No switch to a white body background anywhere in the tile"
  confidence: high
  contrast_with: "store/bullish-co/captures/2026-06-18/tiles/homepage/tile-00-y00000.png"

- id: color_05
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "homepage card grid — warm portfolio cards"
  tile_path: "store/bullish-co/captures/2026-06-18/tiles/homepage/tile-02-y02440.png"
  claim: "A couple of portfolio cards introduce warm tones that sit slightly apart from the otherwise cool blue/black/white system — a tan/beige Sourdough Sidekick card and a creamy off-white Daisy card."
  visible_tells:
    - "Sourdough Sidekick card has a warm tan/taupe background, warmer than the cool system around it"
    - "Daisy card uses a creamy off-white rather than a neutral white"
  confidence: medium

- id: color_06
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "about page — team photos"
  tile_path: "store/bullish-co/captures/2026-06-18/tiles/about/tile-03-y03513.png"
  claim: "Team headshots commit to a black-and-white treatment in matching rounded-square frames, but the greyscale photos show inconsistent lighting and backgrounds across the three, undercutting the unified look."
  visible_tells:
    - "All three headshots are desaturated to greyscale — a consistent decision"
    - "Left photo has bright window blinds behind it, center is flat and dark, right has a white brick wall — no shared set or lighting"
  confidence: medium

- id: iconography_01
  family: iconography_illustration
  polarity: poor
  page_or_region: "homepage — global chrome / nav & footer"
  tile_path: "store/bullish-co/captures/2026-06-18/tiles/homepage/tile-01-y01220.png"
  claim: "The site carries essentially no icon system — the only mark is a tiny square glyph in the nav that reads as a functional menu affordance, and the footer lists social platforms as plain text rather than icons."
  visible_tells:
    - "Top-left nav holds a small rectangular outline glyph with no stroke refinement or identity investment"
    - "No icons accompany any nav item, card, or CTA; footer LinkedIn/Instagram/Twitter are plain text links"
  confidence: high
  contrast_with: "store/bullish-co/captures/2026-06-18/tiles/about/tile-01-y01220.png"

- id: iconography_02
  family: iconography_illustration
  polarity: poor
  page_or_region: "about page — services grid"
  tile_path: "store/bullish-co/captures/2026-06-18/tiles/about/tile-01-y01220.png"
  claim: "The 24-cell services grid carries no icons, glyphs, or illustration — every tile is text-on-navy and nothing else, with the rounded-card shape as the only graphic decision."
  visible_tells:
    - "All 24 service tiles contain a label only, no supporting icon or mark"
    - "The rounded-corner card is the sole non-text graphic element"
  confidence: high

- id: iconography_03
  family: iconography_illustration
  polarity: poor
  page_or_region: "homepage — content card grid"
  tile_path: "store/bullish-co/captures/2026-06-18/tiles/homepage/tile-02-y02440.png"
  claim: "Editorial cards rely entirely on solid color fills as their visual language — no illustration, chart, or decorative mark appears in any card; the blue/black/off-white blocks plus type carry the whole grid."
  visible_tells:
    - "Blue and black cards hold only a category label and a headline, no graphic"
    - "Off-white cards hold only a brand name and tagline, with no illustration or ornament"
  confidence: high
```

## Provenance

- **Tiles read:** `store/bullish-co/captures/2026-06-18/tiles/` — `homepage/` (19 tiles) and `about/` (4 tiles), 23 active tiles mined by four blind family miners (Sonnet) → judge prune. 34 raw cards mined → 24 accepted (13 strong / 4 mixed / 7 poor) / 10 rejected.
- **Curation:** The `/capital` and `/creative` feed pages were tiled but **dropped from the active set** — both are near-identical masonry feeds to the homepage (same hero wordmark, same card system), so they carry no distinct visual evidence. Coverage = homepage (the signature wordmark + masonry system + nav + footer) and about (serif H1, white approach cards, navy services grid, B&W team photos).
- **QA — `exclusions-noted`:** The homepage portfolio cards render with **empty grey image regions** across the scroll (lazy-loaded brand imagery that did not fire — tiles 02/03/04/08/16). Per the blind-read brief this is a **capture caveat, not design evidence**; the judge correctly rejected all six artifact-dependent cards (heterogeneous-imagery, uneven-density, hollow-grid claims). Accepted cards cite only cleanly-rendered regions (text cards, type, grid structure, palette). No Tier-B re-render was needed — the brand's real visual system reads intact from the cached tiles.
- **Spot-check:** Every `poor` structural card was verified against its native tile (footer `tile-18`, services grid `about/tile-01`, engagements `about/tile-02`, nav `tile-01`) — all reflect real rendered content, none a compositing/animation artifact.
- **Caveat:** Point-in-time snapshot of the 2026-06-18 captured tiles; the live site changes.
