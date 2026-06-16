---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.0"
domain: niagenplus.com
captured_at: 2026-06-15
source_capture: 2026-06-15
qa_status: exclusions-noted
---

## Visual & brand impression

A disciplined, system-driven site reading clinical-luxury, not supplement-DTC. A consistent three-level type hierarchy [typography_01] and reusable components — matched product cards [layout_02], alternating benefit blocks [layout_03], a 4-up grid [layout_05], a four-column footer [layout_06] — sit under asymmetric editorial layouts [layout_01] and thin serif display headlines [typography_02]. The palette is tightly held: warm-amber art-directed photography [color_01] on a cream-and-navy ground [color_02], one cobalt accent threading CTAs and the kit box as its lone tension [color_03]. It slips where mood beats clarity: a dark, low-contrast IV section [color_04], an abrupt section join [layout_09], a flat disclaimers block [typography_06]. Iconography is an afterthought: stock social glyphs and bare + marks [iconography_01], photos standing in for icons and diagrams [iconography_02, iconography_04].

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: "homepage hero + two-up product cards + niagen_iv benefit sections"
  tile_path: "store/niagenplus-com/captures/2026-06-15/tiles/homepage/tile-00-y00000.png"
  claim: "A consistent three-level type system — small spaced-caps eyebrow, serif display headline, then a smaller/lighter body block — repeats across the hero, both homepage product cards, and the niagen_iv benefit sections, confirming a deliberate hierarchy rather than per-section invention."
  visible_tells:
    - "Hero: 'TELEHEALTH PROGRAM' caps eyebrow above two-line serif headline 'A new way to access Niagen', body drops smaller/lighter below"
    - "Homepage cards repeat the same eyebrow ('TELEHEALTH PROGRAM' / 'IN-CLINIC NAD+ SUPPORT') + heading + one-line descriptor stack"
    - "niagen_iv tile-02 repeats micro-label ('BETTER TOLERABILITY' / 'FASTER INFUSION TIMES') + serif heading + body twice on one tile"
  confidence: high
  contrast_with: "store/niagenplus-com/captures/2026-06-15/tiles/homepage/tile-02-y02440.png"
- id: typography_02
  family: typography_hierarchy
  polarity: strong
  page_or_region: "homepage — 'science of cellular health' section below hero"
  tile_path: "store/niagenplus-com/captures/2026-06-15/tiles/homepage/tile-00-y00000.png"
  claim: "The off-white section uses a large, thin-weight serif headline ('The science of cellular health, on your terms.') set roughly 3x the size of a normal-weight two-column body block, showing confident weight-and-size contrast between heading and prose."
  visible_tells:
    - "Display heading in a noticeably light/thin serif at display size"
    - "Right-column body text is tightly set at normal weight, clearly subordinate"
  confidence: high
- id: typography_03
  family: typography_hierarchy
  polarity: strong
  page_or_region: "about — hero overlay on dark photo"
  tile_path: "store/niagenplus-com/captures/2026-06-15/tiles/about/tile-00-y00000.png"
  claim: "The about hero stacks eyebrow, headline and body in white over a deep-brown photograph, and all three levels stay legible against the busy image with no contrast failure."
  visible_tells:
    - "'ABOUT NIAGEN PLUS' spaced-caps eyebrow clearly lighter than headline"
    - "Two-line white serif headline 'Clinical Niagen NR access, from the team behind the research' reads cleanly over the dark photo"
    - "No haloing or color bleed where type sits on the image"
  confidence: high
- id: typography_04
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "niagen_iv — product card overlays ('Niagen IV', 'Niagen Shots')"
  tile_path: "store/niagenplus-com/captures/2026-06-15/tiles/niagen_iv/tile-01-y01220.png"
  claim: "On the two image cards the white heading reads well, but the descriptor beneath is small and set over a variable warm-amber photo, dropping the subordinate level to marginal legibility."
  visible_tells:
    - "Headings 'Niagen IV' / 'Niagen Shots' adequately sized in white"
    - "Descriptor copy below is small and rendered over an uneven golden background with low contrast"
  confidence: medium
- id: typography_05
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "homepage — full-bleed midpage statement over portrait"
  tile_path: "store/niagenplus-com/captures/2026-06-15/tiles/homepage/tile-01-y01220.png"
  claim: "The full-bleed centred statement over the face portrait is a single type level — no eyebrow, no body — so the three-level system is deliberately suspended here as a brand moment, breaking system consistency in exchange for impact."
  visible_tells:
    - "Only one text element on the section: the centred white statement 'Pharmaceutical-grade cellular health support, from the global leaders in NAD+ research'"
    - "No subordinate label or paragraph accompanies it"
  confidence: medium
  contrast_with: "store/niagenplus-com/captures/2026-06-15/tiles/homepage/tile-00-y00000.png"
- id: typography_06
  family: typography_hierarchy
  polarity: poor
  page_or_region: "homepage / kit — DISCLAIMERS section"
  tile_path: "store/niagenplus-com/captures/2026-06-15/tiles/homepage/tile-02-y02440.png"
  claim: "The 'DISCLAIMERS' label sits at nearly the same visual weight and size as the numbered fine-print beneath it, so the eye gets little separation between the section label and its body — the one place the otherwise-clear hierarchy goes flat."
  visible_tells:
    - "'DISCLAIMERS' caps label only marginally heavier than the numbered body text"
    - "Three numbered items run at very small size with little breathing room from the label"
  confidence: medium
- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: "homepage hero"
  tile_path: "store/niagenplus-com/captures/2026-06-15/tiles/homepage/tile-00-y00000.png"
  claim: "The hero is a full-bleed editorial photo with text anchored to the lower-left in a narrow column, creating deliberate asymmetry and breathing room instead of a centered layout."
  visible_tells:
    - "Left-aligned headline and pill CTA float over the lower-left quadrant"
    - "Right half of the frame is pure photography (hands opening a box) with no text overlay"
    - "Eyebrow label sits above the headline with clear vertical spacing"
  confidence: high
- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: "homepage — two-up product card row"
  tile_path: "store/niagenplus-com/captures/2026-06-15/tiles/homepage/tile-01-y01220.png"
  claim: "The two product cards share identical internal structure (eyebrow → heading → body → pill CTA) with matched corners, image aspect, and CTA baselines, demonstrating a disciplined reusable card component."
  visible_tells:
    - "Both cards follow the same vertical slot order top to bottom"
    - "'Discover Niagen At-Home' and 'Discover Niagen In-Clinic' CTA pills sit at the same optical baseline"
    - "Card corner radii and image crops are matched left and right"
  confidence: high
- id: layout_03
  family: layout_composition_components
  polarity: strong
  page_or_region: "niagen_iv — alternating text/image benefit sections"
  tile_path: "store/niagenplus-com/captures/2026-06-15/tiles/niagen_iv/tile-02-y02440.png"
  claim: "Benefit sections use a strict alternating layout — image-left/text-right then text-left/image-right — at consistent margins and matched column widths, a systematic template rather than ad-hoc placement."
  visible_tells:
    - "'Your comfort, prioritized': image left, text block right"
    - "'Your time, restored': text block left, image right"
    - "Eyebrow, heading, body, and blue CTA hold consistent proportions in both blocks"
  confidence: high
- id: layout_04
  family: layout_composition_components
  polarity: strong
  page_or_region: "kit — product detail layout"
  tile_path: "store/niagenplus-com/captures/2026-06-15/tiles/kit/tile-00-y00000.png"
  claim: "The product page uses a classic two-column commerce layout — left image stack, right info column with price, CTA and accordion — with tight vertical alignment between price, button, and accordion labels."
  visible_tells:
    - "'$299' and a full-width blue 'Add to cart' button stack in the narrow right column"
    - "Accordion rows ('What to expect', 'Why Niagen over generic NAD+', 'Pharmaceutical-grade standards') align flush left with + toggles"
    - "Left column stacks photos of differing aspect ratios without colliding with the right panel"
  confidence: high
- id: layout_05
  family: layout_composition_components
  polarity: strong
  page_or_region: "kit — 'The Niagen Plus difference' 4-up card row"
  tile_path: "store/niagenplus-com/captures/2026-06-15/tiles/kit/tile-02-y02440.png"
  claim: "Four feature cards sit in a uniform grid with matched height, corner radius, a small circular badge at top-left, and bottom-aligned captions, showing a tightly specified repeating component."
  visible_tells:
    - "All four cards share identical height and corner radius"
    - "Each card carries a small circular badge top-left"
    - "Captions 'Provider-led care', 'Shipped to your door', 'On your time', 'Pharmaceutical-grade' sit at the same baseline across all four"
  confidence: high
- id: layout_06
  family: layout_composition_components
  polarity: strong
  page_or_region: "footer (homepage, about, kit)"
  tile_path: "store/niagenplus-com/captures/2026-06-15/tiles/kit/tile-03-y03660.png"
  claim: "The footer uses a four-column grid (brand/email signup | About Us | Resources | Follow) with consistent gutters and link styling, plus a clean full-width rule separating the legal sub-bar."
  visible_tells:
    - "Four top-aligned columns of equal visual weight"
    - "Link lists share identical line-height and type size within each column"
    - "Sub-bar with copyright left and payment icons right is separated by a full-width rule"
  confidence: high
  contrast_with: "store/niagenplus-com/captures/2026-06-15/tiles/homepage/tile-02-y02440.png"
- id: layout_07
  family: layout_composition_components
  polarity: mixed
  page_or_region: "about — clinical studies section vs niagen_iv alternating blocks"
  tile_path: "store/niagenplus-com/captures/2026-06-15/tiles/about/tile-02-y02440.png"
  claim: "The two about-page study blocks alternate image/text but use different column splits and image sizes between them, breaking the strict symmetry the niagen_iv alternating sections maintain."
  visible_tells:
    - "'Published clinical data' block: image roughly one-third left, text two-thirds right"
    - "'The first controlled clinical study' block: text and image closer to a 50/50 split — proportions differ from the block above"
    - "Vertical gap between the two blocks reads tighter than the niagen_iv section rhythm"
  confidence: medium
  contrast_with: "store/niagenplus-com/captures/2026-06-15/tiles/niagen_iv/tile-02-y02440.png"
- id: layout_08
  family: layout_composition_components
  polarity: mixed
  page_or_region: "kit — photo collage above 'The Niagen Plus difference'"
  tile_path: "store/niagenplus-com/captures/2026-06-15/tiles/kit/tile-01-y01220.png"
  claim: "An editorial collage of two photos at mismatched aspect ratios floats with loose alignment above the section label, reading as an intentional transitional moment but not connecting to the structured grid that follows."
  visible_tells:
    - "Upper portrait photo is narrower and cropped differently from the wide box photo below it"
    - "Neither photo aligns to an apparent column edge"
    - "Large gap below before the 'The Niagen Plus difference' label, disproportionate to the page rhythm"
  confidence: medium
- id: layout_09
  family: layout_composition_components
  polarity: poor
  page_or_region: "niagen_iv — 'Niagen Shots' full-bleed section join"
  tile_path: "store/niagenplus-com/captures/2026-06-15/tiles/niagen_iv/tile-03-y03660.png"
  claim: "The warm full-bleed 'Niagen Shots' section begins right after the 'Our standard, upheld' block with no separator or breathing margin, and its heading drops the eyebrow-label treatment used in sibling product sections, so two distinct zones run together."
  visible_tells:
    - "'Our standard, upheld' text ends close to where the warm full-bleed begins, no rule or spacing gap between"
    - "'Niagen Shots' heading appears inside the image without the micro-label used elsewhere"
    - "Background ramps abruptly from cream to amber with no transition"
  confidence: medium
- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: "site-wide photography (homepage, about, niagen_iv, kit)"
  tile_path: "store/niagenplus-com/captures/2026-06-15/tiles/niagen_iv/tile-00-y00000.png"
  claim: "Every human-subject and product photograph across all four pages shares the same narrow warm amber–brown–terracotta range shot in low, directional light, indicating a single art-directed image language rather than mixed stock — color temperature, depth of field and props all cohere."
  visible_tells:
    - "Hero hands-on-box photo and the woman-with-IV (niagen_iv tile-00) match exactly in warm temperature and saturation"
    - "No tile shows a cool-lit or neutrally-lit subject; ambient light is consistently amber"
    - "No microstock even-illumination or watermarks"
  confidence: high
  contrast_with: "store/niagenplus-com/captures/2026-06-15/tiles/homepage/tile-00-y00000.png"
- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: "site-wide ground + footer"
  tile_path: "store/niagenplus-com/captures/2026-06-15/tiles/kit/tile-03-y03660.png"
  claim: "Content sits on a single warm off-white/cream ground (not pure white) and every footer is the same deep navy, repeated without variation across all pages — disciplined two-anchor background system."
  visible_tells:
    - "FAQ/disclaimers ground in kit tile-03 is clearly cream, not #ffffff; same cream in about tile-01 and niagen_iv tile-02"
    - "Deep navy footer block identical in hue and depth in homepage tile-02 and kit tile-03"
    - "White reversed wordmark and type in the footer with no secondary color breaking the band"
  confidence: high
  contrast_with: "store/niagenplus-com/captures/2026-06-15/tiles/homepage/tile-02-y02440.png"
- id: color_03
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "niagen_iv / about / kit — the lone cool accent (CTA buttons + kit box)"
  tile_path: "store/niagenplus-com/captures/2026-06-15/tiles/niagen_iv/tile-05-y06100.png"
  claim: "A saturated cobalt/navy blue is the only cool hue in the system — it appears on every CTA button and on the navy kit mailer box, threading the footer color through to interactive elements. It both ties elements together and reads as a hard tonal break against the otherwise all-warm photography, leaving the tension only partly resolved."
  visible_tells:
    - "Bright blue 'Find a Clinic' pill against cream in niagen_iv tile-05; same blue on about tile-01 CTAs and the kit 'Add to cart' button"
    - "Navy 'Welcome to Niagen Plus' mailer box (kit tile-01) sits as a cool object inside a warm amber photo — same hue as footer and CTAs"
    - "No echo of the blue anywhere else in the warm/navy compositions — it is isolated to interactive elements and the box"
  confidence: high
  contrast_with: "store/niagenplus-com/captures/2026-06-15/tiles/homepage/tile-00-y00000.png"
- id: color_04
  family: color_brand_imagery
  polarity: poor
  page_or_region: "niagen_iv — dark full-bleed 'Niagen IV' section"
  tile_path: "store/niagenplus-com/captures/2026-06-15/tiles/niagen_iv/tile-01-y01220.png"
  claim: "The lower dark-toned 'Niagen IV' section (man reclining in dim interior) is exposed for mood over clarity — the subject and product elements sink toward shadow, and white body copy sits at low contrast over the murky background, compressing both legibility and the eyebrow/heading size difference."
  visible_tells:
    - "Reclining male subject is dim and low-contrast against the dark interior"
    - "Eyebrow micro-label and section heading sit close in apparent size against the low-contrast amber/black background"
    - "White overlaid body copy reads weakly against the dark image"
  confidence: medium
  contrast_with: "store/niagenplus-com/captures/2026-06-15/tiles/niagen_iv/tile-02-y02440.png"
- id: iconography_01
  family: iconography_illustration
  polarity: poor
  page_or_region: "footer (all pages) + kit FAQ accordion"
  tile_path: "store/niagenplus-com/captures/2026-06-15/tiles/kit/tile-03-y03660.png"
  claim: "The only discrete glyphs site-wide are off-the-shelf: standard social platform logos (Facebook, Instagram, TikTok, X) in the footer and bare plus (+) marks on FAQ/accordion rows — no proprietary or brand-adapted icon system appears anywhere."
  visible_tells:
    - "Four default social platform logos in the navy footer"
    - "Repeated raw '+' toggles down the FAQ list and product accordion, no custom chevron or branded variant"
    - "No decorative or UI iconography elsewhere in nav or footer"
  confidence: high
- id: iconography_02
  family: iconography_illustration
  polarity: mixed
  page_or_region: "kit — 'The Niagen Plus difference' step strip"
  tile_path: "store/niagenplus-com/captures/2026-06-15/tiles/kit/tile-02-y02440.png"
  claim: "The four 'difference' steps use miniature lifestyle photos instead of drawn icons — which dodges generic clip-art but means there is no illustration craft on display; the 'icons' are cropped editorial photography."
  visible_tells:
    - "Cards labeled 'Provider-led care', 'Shipped to your door', 'On your time', 'Pharmaceutical-grade' each show a cropped photo, not a glyph"
    - "No drawn pictogram or custom illustration present in the strip"
  confidence: high
  contrast_with: "store/niagenplus-com/captures/2026-06-15/tiles/kit/tile-03-y03660.png"
- id: iconography_03
  family: iconography_illustration
  polarity: mixed
  page_or_region: "niagen_iv — 'Access Niagen Plus near you' checklist"
  tile_path: "store/niagenplus-com/captures/2026-06-15/tiles/niagen_iv/tile-05-y06100.png"
  claim: "Benefit bullets use plain checkmark glyphs — functional and legible but generic, with no custom stroke weight or brand-specific form that would signal a designed icon."
  visible_tells:
    - "Four checkmark list items below 'Access Niagen Plus near you'"
    - "Checkmarks read as plain Unicode/web-font glyphs, not drawn marks"
  confidence: medium
- id: iconography_04
  family: iconography_illustration
  polarity: poor
  page_or_region: "about — 'Health begins within' macro-cell visual + site-wide product imagery"
  tile_path: "store/niagenplus-com/captures/2026-06-15/tiles/about/tile-01-y01220.png"
  claim: "Where a brand would normally use a scientific diagram or illustration, the site substitutes a soft-focus macro cell photograph ('Health begins within') and otherwise relies entirely on lifestyle/product photography — there are no diagrams, exploded views, ingredient renders or annotations anywhere to judge illustration craft."
  visible_tells:
    - "Large translucent cell-like spheres on a warm amber field stand in as the sole visual explanation of cellular science"
    - "Product shots (vials, IV bags, kit) appear as plain photography with no callouts or annotation layer"
    - "No drawn pictogram or explanatory diagram anywhere across the tiles"
  confidence: high
```

## Provenance

- **Tiles read:** 17 active Tier-A tiles (cached Firecrawl full-page screenshots, `sips`-cropped) across 4 pages — homepage, about, niagen_iv (in-clinic collection), kit (PDP) — from `captures/2026-06-15/tiles/`. Blind 4-family mine + judge (36 raw cards → 24 accepted; 1 dropped at synthesis, below → 23 cards here).
- **Exclusions (5 tiles):** `homepage/tile-03`, `about/tile-04`, `niagen_iv/tile-06`, `niagen_iv/tile-07`, `kit/tile-04` — each dominated by the below-footer **Klaviyo "Unlock more Niagen Plus" newsletter popup on a grey backdrop**, a capture-browser overlay, not site content.
- **Capture caveat (dropped card):** the footer's first clean appearance (`homepage/tile-02`) carries a thin popup sliver at its bottom edge; the judge flagged that modal as a capture artifact (not a design defect). It is **excluded from the cards** and noted here; the disclaimers + four-column footer above it are intact and were judged.
- **No Tier-B re-render** — cached screenshots rendered cleanly above the footer (no WebGL/grey hero, black media, or lazy-load gaps).
- **Snapshot caveat:** a point-in-time read of the 2026-06-15 tiles; the site changes — re-tile + re-mine to refresh.
