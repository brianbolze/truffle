---
schema_version: "1.0"
domain: goodlifemeds.com
captured_at: 2026-06-16
source_capture: 2026-06-04
qa_status: recapture-used
---

# Good Life Meds — visual evidence

## Visual & brand impression

A controlled, photography-led brand. A confident full-bleed editorial hero carries legible display type with no text shield [typography_01][layout_01], set against a disciplined charcoal-and-cream palette [color_01]. The strongest work is the imagery: own-brand vials staged in a green gradient tuned across products [color_02], a branded packaging system [color_03], a cutout figure composited to the page palette [color_04]. Component systems hold — product cards, the four-up trust grid, the PDP split, the calculator dashboard [layout_02][layout_03][layout_04][layout_05]. Typography is the soft spot: hierarchy flattens across accordion, pillar, and FAQ labels [typography_05][typography_06][typography_08], a two-tone headline reads decorative [typography_04], and inline avatars fracture one headline [typography_07]. Register slips where third-party content enters — stock benefit macros [color_05], Wegovy manufacturer shots beside brand cards [color_06] — and trust icons read generic against the photography [iconography_02].

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: homepage hero
  tile_path: store/goodlifemeds-com/captures/2026-06-16/tiles/homepage/tile-00-y00000.png
  claim: The hero headline holds confident display scale and stays fully legible in white over a dark mid-band of the full-bleed cycling photo, with no text shield — a single small pill CTA below forms a clean two-level stop.
  visible_tells:
  - Large white headline ('We're simplifying the path to the Good Life') sits cleanly on the dark center of the image without ghosting or a backing panel
  - One small outlined pill CTA ('Find your treatment') below is the only subordinate element
  confidence: high
- id: typography_02
  family: typography_hierarchy
  polarity: strong
  page_or_region: homepage — full-bleed category section headers (Weight Loss, Daily Wellness)
  tile_path: store/goodlifemeds-com/captures/2026-06-16/tiles/homepage/tile-02-y02440.png
  claim: The full-bleed category headers set 'Weight Loss' at display scale (~80px equivalent) in white over a desaturated lifestyle photo, with a clear size step down to the supporting blurb beneath — a strong section anchor.
  visible_tells:
  - Very large white 'Weight Loss' label over a muted photo of a person's back
  - Supporting body copy visibly smaller and lower-contrast directly below the label
  confidence: high
  contrast_with: store/goodlifemeds-com/captures/2026-06-16/tiles/homepage/tile-03-y03660.png
- id: typography_03
  family: typography_hierarchy
  polarity: strong
  page_or_region: semaglutide page — 'Benefits' section header
  tile_path: store/goodlifemeds-com/captures/2026-06-16/tiles/semaglutide/tile-02-y02440.png
  claim: The 'Benefits' heading is set at extreme display scale filling roughly 40% of the viewport width and anchors a clean two-level structure — benefit sub-labels and one-line descriptions sit far smaller and clearly subordinate.
  visible_tells:
  - Very large left-aligned 'Benefits' headline dominates the upper-left of the section
  - Benefit names ('Supports healthy weight loss', 'Boosts energy naturally') and their descriptions are at a modest readable size, clearly below the heading in the hierarchy
  confidence: high
- id: typography_04
  family: typography_hierarchy
  polarity: mixed
  page_or_region: homepage — 'Improve your / daily wellness' callout
  tile_path: store/goodlifemeds-com/captures/2026-06-16/tiles/homepage/tile-04-y04880.png
  claim: The lower-page callout splits emphasis mid-phrase — 'Improve your' in a darker standard weight, 'daily wellness' in a lighter olive-green tint — a recurring two-tone headline device that reads stylistic rather than as a hierarchy cue.
  visible_tells:
  - '''Improve your'' rendered darker; ''daily wellness'' rendered in a lighter green on the next line'
  - Same dark/green two-tone split also appears on 'Achieve your / weight loss goals' (tile-03), confirming it is a deliberate motif
  confidence: medium
  contrast_with: store/goodlifemeds-com/captures/2026-06-16/tiles/homepage/tile-03-y03660.png
- id: typography_05
  family: typography_hierarchy
  polarity: mixed
  page_or_region: semaglutide page — purchase panel accordion labels
  tile_path: store/goodlifemeds-com/captures/2026-06-16/tiles/semaglutide/tile-00-y00000.png
  claim: The PDP top pair is well-ranked (large product name over a smaller price), but the stacked accordion labels ('What's Included', 'What is Compounded Semaglutide?', 'Transferring from another provider?') all sit at the same small weight, flattening the section list into an undifferentiated stack.
  visible_tells:
  - '''Compounded Semaglutide'' in clear display size with ''$99'' smaller beneath — good top pair'
  - Five accordion row labels all rendered at the same small size and weight with no emphasis step between them
  confidence: medium
- id: typography_06
  family: typography_hierarchy
  polarity: mixed
  page_or_region: homepage — 4-up trust pillars
  tile_path: store/goodlifemeds-com/captures/2026-06-16/tiles/homepage/tile-02-y02440.png
  claim: Within each trust pillar the bold label ('Trusted by doctors', 'Clinical experts', etc.) and its two-line description are typeset at nearly the same small size, leaving only a faint weight difference to carry the label-vs-body hierarchy.
  visible_tells:
  - Pillar labels sit just slightly heavier than the descriptions beneath them — no size step or color change
  - All four columns repeat the same minimal label/body contrast
  confidence: medium
- id: typography_07
  family: typography_hierarchy
  polarity: poor
  page_or_region: homepage — 'Trusted by thousands' social-proof headline
  tile_path: store/goodlifemeds-com/captures/2026-06-16/tiles/homepage/tile-05-y06100.png
  claim: The headline 'Trusted by [avatars] thousands of customers nationwide' embeds circular avatar thumbnails inline within the running display type, breaking the line and making the heading read as assembled rather than set.
  visible_tells:
  - A small clustered avatar thumbnail is inlined between 'Trusted by' and 'thousands' inside the headline text
  - A green Trustpilot rating cluster sits immediately under the broken headline, further fragmenting the type block
  confidence: high
- id: typography_08
  family: typography_hierarchy
  polarity: poor
  page_or_region: semaglutide page — FAQ section
  tile_path: store/goodlifemeds-com/captures/2026-06-16/tiles/semaglutide/tile-09-y10980.png
  claim: The FAQ question rows and the introductory paragraph beside the heading sit at the same size and weight, so there is no typographic step between section intro and the tappable question list — the questions don't read as the primary interactive layer.
  visible_tells:
  - Each FAQ row ('What happens if I'm not approved...', 'How does semaglutide work?') is the same small weight as the 'Find answers to common questions...' intro paragraph
  - Only a thin right-aligned chevron, not type weight, signals the rows are expandable
  confidence: medium
- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: homepage — hero section
  tile_path: store/goodlifemeds-com/captures/2026-06-16/tiles/homepage/tile-00-y00000.png
  claim: The hero is a full-bleed editorial photograph carrying one centered headline and a single CTA pill, with no card container or competing element in the primary viewport — a confident, uncluttered opening.
  visible_tells:
  - Cycling photograph bleeds to all four edges with no border or frame
  - Single centered headline and one pill CTA; only a small sticky product mini-card intrudes at the lower-left
  confidence: high
- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: homepage / weight loss — product category card rows
  tile_path: store/goodlifemeds-com/captures/2026-06-16/tiles/homepage/tile-03-y03660.png
  claim: Product cards share a tight component template — equal card height, centered product image, product name, and a paired 'Get started / Learn more' button row with an identical small grey disclaimer footer — reading as a system, not ad-hoc repetition.
  visible_tells:
  - Four cards in view with matching image-zone height, name, and a green 'Get started' + 'Learn more' button pair
  - Each card carries the same small grey disclaimer line ('IMPORTANT SAFETY INFORMATION') along its bottom edge
  confidence: high
  contrast_with: store/goodlifemeds-com/captures/2026-06-16/tiles/weight_loss/tile-03-y03660.png
- id: layout_03
  family: layout_composition_components
  polarity: strong
  page_or_region: homepage — 4-up trust pillars
  tile_path: store/goodlifemeds-com/captures/2026-06-16/tiles/homepage/tile-02-y02440.png
  claim: A four-column trust row uses consistent icon-over-label-over-body stacks at equal widths with even gutters and a shared top edge, showing reliable grid adherence on a secondary section.
  visible_tells:
  - Four equal columns ('Trusted by doctors', 'Clinical experts', 'Fast & discrete delivery', 'Safe, quality medications') with a small icon above each
  - All four text blocks align to the same top edge
  confidence: high
- id: layout_04
  family: layout_composition_components
  polarity: strong
  page_or_region: semaglutide PDP — product detail layout
  tile_path: store/goodlifemeds-com/captures/2026-06-16/tiles/semaglutide/tile-00-y00000.png
  claim: The PDP hero is a clean two-column split — large vial photograph on a green gradient at left, a left-aligned purchase column at right (name, $99, Buy now, benefit bullets, a promo-code box, and stacked accordion rows) — composited without clutter.
  visible_tells:
  - 'Left: full-height green vial photograph on a green-to-black gradient'
  - 'Right: product name, price, ''Buy now'', two check-bullets, a boxed ''$100 Off First Order / NEWME100'' promo callout, and a stack of accordion rows, all sharing one left indent'
  confidence: high
- id: layout_05
  family: layout_composition_components
  polarity: strong
  page_or_region: weight loss — calculator dashboard section
  tile_path: store/goodlifemeds-com/captures/2026-06-16/tiles/weight_loss/tile-04-y04880.png
  claim: The 'Weight Loss Calculators' block arranges five interactive calculator widgets (BMI, Protein, Water Intake, Calorie Deficit, Total Daily Energy) in a uniform card grid with matching borders, a 'View X' link in the same position on each — component reuse beyond basic marketing modules.
  visible_tells:
  - Calculator cards at uniform size with a bold readout (e.g. BMI '23', Calorie Deficit '1,835 kcal') and a 'View ...' link in the same lower-left slot
  - Card borders and internal padding appear consistent across the grid
  confidence: high
- id: layout_06
  family: layout_composition_components
  polarity: mixed
  page_or_region: homepage — testimonial / social-proof mosaic
  tile_path: store/goodlifemeds-com/captures/2026-06-16/tiles/homepage/tile-05-y06100.png
  claim: The social-proof portraits sit in an irregular asymmetric mosaic at different sizes and vertical offsets rather than a structured grid — intended as editorial looseness, but it leaves uneven gutters and a ragged top edge that read as unresolved more than art-directed.
  visible_tells:
  - Five portrait stills at clearly different sizes and baselines — a small one far left, a tall one, then a cluster at right
  - Gaps between portraits are visibly unequal; tops do not align
  confidence: medium
- id: layout_07
  family: layout_composition_components
  polarity: mixed
  page_or_region: semaglutide — 'Always quality tested' section
  tile_path: store/goodlifemeds-com/captures/2026-06-16/tiles/semaglutide/tile-05-y06100.png
  claim: The quality section pairs a left-side stack of test names ('Potency', 'Sterility', 'pH') against a right-side body-copy column, but the test-label rows and their paragraphs do not share a common baseline and the inter-row gaps differ, leaving the two columns slightly out of register.
  visible_tells:
  - 'Left: ''Potency'', ''Sterility'', ''pH'' stacked with small green ''PASSED'' pills; gaps between rows differ visibly'
  - Right-column paragraphs do not align to the top of their corresponding left-side label
  confidence: medium
- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: homepage — overall palette (hero + footer)
  tile_path: store/goodlifemeds-com/captures/2026-06-16/tiles/homepage/tile-00-y00000.png
  claim: The brand runs a disciplined neutral base — dark charcoal nav and type against warm off-white/cream backgrounds — sustained across hero and content sections without deviation.
  visible_tells:
  - Dark charcoal pill nav bar over the warm backlit photo; off-white cream in the sticky product mini-card
  - Same cream background carries into the sections below the fold
  confidence: high
- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: homepage / weight loss — product photography environment
  tile_path: store/goodlifemeds-com/captures/2026-06-16/tiles/weight_loss/tile-05-y06100.png
  claim: Own-brand product shots use a deep green gradient field tuned to the packaging color, so vial and background read as one deliberate environment rather than a generic studio sweep — and the same treatment recurs on the semaglutide vial, confirming a consistent cross-product photography language.
  visible_tells:
  - Deep-to-mid green gradient behind the green 'Tirzepatide+' vial; bottle and ground tonally unified
  - Semaglutide vial (semaglutide tile-00) is lit and staged in the same green gradient with matching lighting direction
  confidence: high
  contrast_with: store/goodlifemeds-com/captures/2026-06-16/tiles/semaglutide/tile-00-y00000.png
- id: color_03
  family: color_brand_imagery
  polarity: strong
  page_or_region: homepage — 'How it works' packaging photography
  tile_path: store/goodlifemeds-com/captures/2026-06-16/tiles/homepage/tile-07-y08540.png
  claim: Packaging is shown as a proprietary branded box system in muted khaki/olive tones, staged as a styled editorial shot — multiple printed units at staggered angles with the 'Good Life' tagline visible — not a vendor stock render.
  visible_tells:
  - Several matte Good Life-branded boxes arranged at overlapping angles against a warm taupe ground, one box opened to show contents
  - Printed 'We're simplifying the path to the Good Life' tagline legible on the box faces
  confidence: high
- id: color_04
  family: color_brand_imagery
  polarity: strong
  page_or_region: homepage — 'Medical support, on your terms' cutout figure
  tile_path: store/goodlifemeds-com/captures/2026-06-16/tiles/homepage/tile-06-y07320.png
  claim: The section uses a cutout-style photograph of a person against the site's cream background with a controlled cast shadow and floating UI chips (a weight stat card, a chat bubble, a product card) — a deliberate composite tuned to the page palette rather than a foreign floating element.
  visible_tells:
  - Figure isolated on warm cream with a soft cast shadow, background matching the page cream
  - Tonally matched floating chips ('165 lbs' weight card, a green Tirzepatide+ card, a provider chat bubble) integrated around the figure
  confidence: high
  contrast_with: store/goodlifemeds-com/captures/2026-06-16/tiles/homepage/tile-05-y06100.png
- id: color_05
  family: color_brand_imagery
  polarity: mixed
  page_or_region: semaglutide — benefits thumbnail imagery
  tile_path: store/goodlifemeds-com/captures/2026-06-16/tiles/semaglutide/tile-02-y02440.png
  claim: The benefit-row thumbnails break from the brand's own photography register — generic stock macros (measuring tape on skin, green leaf texture, blue lab equipment, red pomegranate seeds) that are tonally unrelated to each other and to the warm/green palette used elsewhere.
  visible_tells:
  - Measuring-tape-on-skin crop, a green leaf macro, and a cool-blue equipment macro stacked as benefit thumbnails
  - Their color temperatures clash with each other and with the site's controlled green/cream system
  confidence: high
  contrast_with: store/goodlifemeds-com/captures/2026-06-16/tiles/semaglutide/tile-00-y00000.png
- id: color_06
  family: color_brand_imagery
  polarity: mixed
  page_or_region: weight loss — brand-name product cards on white
  tile_path: store/goodlifemeds-com/captures/2026-06-16/tiles/weight_loss/tile-03-y03660.png
  claim: On a single product row the Wegovy items (blue/white pen injector, plain white pill) sit in manufacturer-style photography on white cards, directly beside the brand's own green-gradient Tirzepatide/Semaglutide cards — a visible register clash within one row.
  visible_tells:
  - Wegovy pen and white pill shown flat on white card backgrounds with no branded environment
  - Same-row Compounded Tirzepatide and Semaglutide cards use the green-gradient brand treatment
  confidence: high
  contrast_with: store/goodlifemeds-com/captures/2026-06-16/tiles/weight_loss/tile-05-y06100.png
- id: color_07
  family: color_brand_imagery
  polarity: mixed
  page_or_region: sexual health — per-category warm palette shift (hero + footer CTA)
  tile_path: store/goodlifemeds-com/captures/2026-06-16/tiles/sexual_health/tile-07-y08230.png
  claim: The sexual-health page swaps the brand's green accent for a warm terracotta/rust register — the footer 'Find your treatment' CTA panel is rust-orange here where every other page's is olive green, and the section's hero and product cards run amber/orange — a per-category mood that breaks the single-accent system.
  visible_tells:
  - Footer CTA panel is rust-orange, versus the olive-green panel on the homepage and weight-loss footers
  - Same page's 'Popular Treatments' hero glows amber with orange Sildenafil/Tadalafil canisters
  confidence: high
  contrast_with: store/goodlifemeds-com/captures/2026-06-16/tiles/homepage/tile-10-y12200.png
- id: iconography_01
  family: iconography_illustration
  polarity: strong
  page_or_region: sexual health — Ignite Strips product graphic
  tile_path: store/goodlifemeds-com/captures/2026-06-16/tiles/sexual_health/tile-05-y06100.png
  claim: The Ignite Strips matte-black foil packet with an embossed white 'G' monogram is a premium, deliberately designed product graphic staged in studio lighting on an amber-brown gradient — packaging-design investment, not stock imagery.
  visible_tells:
  - Matte-black single-dose sachet with a large white geometric 'G' and a small 'SINGLE DOSE' tab, lit cleanly on a warm gradient
  - '''Ignite Strips / Prescription Only'' typeset as part of the staged graphic'
  confidence: high
- id: iconography_02
  family: iconography_illustration
  polarity: poor
  page_or_region: homepage — trust/feature icon row
  tile_path: store/goodlifemeds-com/captures/2026-06-16/tiles/homepage/tile-02-y02440.png
  claim: The four trust-row icons are generic thin monochrome line glyphs with no custom character — indistinguishable from an off-the-shelf utility icon set and visibly weaker than the site's strong product photography.
  visible_tells:
  - Four small low-weight line icons above 'Trusted by doctors / Clinical experts / Fast & discrete delivery / Safe, quality medications'
  - No stylistic differentiation, custom stroke, or brand detailing on any of the four
  confidence: high
  contrast_with: store/goodlifemeds-com/captures/2026-06-16/tiles/weight_loss/tile-05-y06100.png
- id: iconography_03
  family: iconography_illustration
  polarity: mixed
  page_or_region: weight loss — calculator widget graphics
  tile_path: store/goodlifemeds-com/captures/2026-06-16/tiles/weight_loss/tile-04-y04880.png
  claim: The BMI card adds a thin green arc-ring gauge around its '23' readout — the one data-viz gesture in the grid — while the Protein, Calorie Deficit, and Total Daily Energy cards reduce to bare numerals, so the diagram craft is inconsistent across the set.
  visible_tells:
  - BMI card shows a partial green arc ring around a large '23' numeral
  - Sibling calculator cards display plain numbers ('1,835 kcal', etc.) with no supporting graphic
  confidence: medium
- id: iconography_04
  family: iconography_illustration
  polarity: mixed
  page_or_region: FAQ sections (homepage, weight loss) — decorative pill prop
  tile_path: store/goodlifemeds-com/captures/2026-06-16/tiles/weight_loss/tile-07-y08540.png
  claim: An oversized green capsule/tablet render floats beside the FAQ accordion as ambient brand decoration — a deliberate illustrative touch, but it is a plain 3D pill reused verbatim across pages with no contextual variation.
  visible_tells:
  - A large stacked green pill/tablet render sits left of the FAQ accordion at roughly 4x text size
  - The same pill prop reappears identically on the homepage FAQ (homepage tile-09)
  confidence: high
  contrast_with: store/goodlifemeds-com/captures/2026-06-16/tiles/homepage/tile-09-y10980.png
```

## Provenance

Tiles read: homepage (12), semaglutide (11), sexual_health (8), weight_loss (9) from `captures/2026-06-16/tiles/` — all four pages **Tier-B browser re-renders** (`scripts/shoot.py`, system Chrome). The cached 2026-06-04 Firecrawl payloads carried a "Your Privacy Choices" consent overlay pinned over content on every page, so each page was re-rendered with `--dismiss`.

**Capture caveat (loud).** `--dismiss` did **not** clear the "Your Privacy Choices" CMP — its controls ("Allow" / "Don't Allow" / "More choices") are off `shoot.py`'s affordance label set and it ignores Escape, so the consent card stays pinned lower-right in every tile. It does not lock scroll, so no `scroll_locked` flag fired (each manifest reads `dismissed: true`, `scroll_locked: false`). Handled per the blind protocol: miners were told to discount it, the judge surfaced it as a card, and it was dropped in synthesis (a capture artifact is never a design card). **Readers should discount the lower-right corner of every tile.** The homepage hero also carries a secondary "Compounded Tirzepatide+" promo card (lower-left) that `--dismiss` likewise left in place.

Mined blind + judged per [`/visual-evidence`](../../skills/visual-evidence/SKILL.md): four family miners (Sonnet) saw only the tiles (no dossier, no web); the judge (Opus) kept 29 of 45 raw cards. The synthesis spot-check dropped 3 of those — the CMP caveat card, plus two layout `poor` reads whose tells did not survive native-tile review: a footer-CTA "defect" contradicted by its own clean contrast anchor (`weight_loss/tile-08`), and a carousel/FAQ "collision" with visible separating whitespace. **26 cards ship** (8 typography, 7 layout, 7 color, 4 iconography).

Drift caveat: the live homepage re-rendered 2026-06-16 differs from the 2026-06-04 dossier (new hero photograph, reordered sections); `source_capture` stays the dossier date. Snapshot caveat: this reflects the 2026-06-16 re-render of a site that changes.
