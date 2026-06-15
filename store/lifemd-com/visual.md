---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.0"
domain: lifemd.com
captured_at: 2026-06-15
source_capture: 2026-06-15
qa_status: clean
---

## Visual & brand impression

LifeMD presents as a polished, component-disciplined mass-consumer health brand. Type hierarchy is strong on hero and section heads [typography_01][typography_04][typography_06], and layout leans on genuinely repeatable systems — uniform hero cards, a tidy 2×3 insurance-logo grid, a clean FAQ accordion, and reused per-vertical promo blocks [layout_01][layout_02][layout_04][layout_05]. Color is its most distinctive asset: a confident per-category palette delivered in full-bleed teal and lavender bands [color_01][color_02][color_05][color_06]. It slips on imagery and icons — generic golden-hour stock [color_09], blue-cast lifestyle photos [color_07], commodity line-art glyphs [iconography_04], and inert supporting cards [iconography_07] — plus near-illegible footnotes and a sub-headline lost over a photo [typography_03][typography_07]. The in-app product renders are the craft peak [iconography_08].

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: "homepage \u2014 above-the-fold hero"
  tile_path: store/lifemd-com/captures/2026-06-15/tiles/homepage/tile-00-y00000.png
  claim: "The hero establishes a clear three-level hierarchy \u2014 a large bold display headline, a compact nav/label tier, and small supporting body text \u2014 with the headline size/weight gap creating an immediately readable entry point."
  visible_tells:
  - "\"The Doctor Will See You Now\" renders at display scale in heavy weight on white with nothing competing nearby"
  - "Nav items sit noticeably smaller and lighter, separated by the LifeMD logo"
  - "Body copy to the right of the headline drops to a clearly smaller, lighter size"
  confidence: high
- id: typography_02
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "homepage \u2014 product card carousel (Wegovy, Zepbound, Estradiol, Inderal)"
  tile_path: store/lifemd-com/captures/2026-06-15/tiles/homepage/tile-01-y01220.png
  claim: "Card product names are legible but the weight jump from product name to category label is negligible, leaving the two levels nearly indistinguishable at glance speed."
  visible_tells:
  - "\"Wegovy\u00ae\" and \"Zepbound\u00ae\" names share near-identical size and weight with the \"Weight Loss\" category line beneath them"
  - "No color or style differentiation separates name from category \u2014 both read as short dark text lines of similar scale"
  confidence: high
  contrast_with: store/lifemd-com/captures/2026-06-15/tiles/homepage/tile-00-y00000.png
- id: typography_03
  family: typography_hierarchy
  polarity: poor
  page_or_region: "homepage \u2014 legal/footnote dense-text tile"
  tile_path: store/lifemd-com/captures/2026-06-15/tiles/homepage/tile-10-y11962.png
  claim: "The footnote block is a wall of sub-10px text with no internal hierarchy \u2014 no bold callouts, no size differentiation, no scannable entry points \u2014 structurally flat and practically unreadable."
  visible_tells:
  - "Multiple disclaimer paragraphs in near-identical small gray text with no heading or visual break between them"
  - "Entire block is one typographic level set against dark navy"
  confidence: high
- id: typography_04
  family: typography_hierarchy
  polarity: strong
  page_or_region: "homepage \u2014 \"Accepted Insurance Providers\" section"
  tile_path: store/lifemd-com/captures/2026-06-15/tiles/homepage/tile-08-y09760.png
  claim: "A clean three-tier hierarchy: large heavy navy heading, clearly smaller lighter-navy body paragraph, and text-free logo cards that let the heading carry the section."
  visible_tells:
  - "\"Accepted Insurance Providers\" set large, heavy, navy across three lines"
  - "Body paragraph beneath is markedly smaller, regular weight, same hue but lighter"
  - "The six insurance logo cards contain no text"
  confidence: high
- id: typography_05
  family: typography_hierarchy
  polarity: strong
  page_or_region: "lifemd_plus \u2014 FAQ section"
  tile_path: store/lifemd-com/captures/2026-06-15/tiles/lifemd_plus/tile-03-y03660.png
  claim: "The FAQ uses a two-column split \u2014 oversized display-weight left heading, regular-weight question rows on the right \u2014 achieving hierarchy through scale and spatial separation rather than color."
  visible_tells:
  - "\"Frequently Asked Questions\" set very large and heavy across three stacked lines in the left column"
  - "FAQ question rows are small regular weight, separated by thin dividers, consistent across all visible items"
  confidence: high
- id: typography_06
  family: typography_hierarchy
  polarity: strong
  page_or_region: "womens_health \u2014 statistics section (80%, 50%, 77%, 60%)"
  tile_path: store/lifemd-com/captures/2026-06-15/tiles/womens_health/tile-04-y04880.png
  claim: "The stat grid lands a sharp two-level hierarchy \u2014 oversized navy percentage numerals doing the heavy lifting, with a small reduced-contrast caption sentence receding cleanly beneath each."
  visible_tells:
  - "\"80%\", \"50%\", \"77%\", \"60%\" render at large display scale in dark navy"
  - "Explanatory sentences beneath sit in small regular weight at noticeably lower contrast"
  confidence: high
- id: typography_07
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "womens_health \u2014 hero (copy over photograph)"
  tile_path: store/lifemd-com/captures/2026-06-15/tiles/womens_health/tile-00-y00000.png
  claim: "The hero headline reads cleanly against the taupe photo, but the sub-headline paragraph below is small, faint white on the same mid-value background with no scrim, leaving the sub-tier effectively invisible without close inspection."
  visible_tells:
  - "\"Personalized Care, Backed by Leading Women's Health Experts\" reads clearly: white, bold, large"
  - "The sub-headline paragraph below is white, small, and nearly lost against the warm gray-beige field \u2014 no darkening applied"
  confidence: high
  contrast_with: store/lifemd-com/captures/2026-06-15/tiles/womens_health/tile-04-y04880.png
- id: typography_08
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "membership \u2014 hero pricing card ($19/mo) and bullet list below it"
  tile_path: store/lifemd-com/captures/2026-06-15/tiles/membership/tile-00-y00000.png
  claim: "The pricing card differentiates plan name from price well by weight/size, but the Title-Cased benefit bullets below sit at near-identical optical size to the \"LifeMD+\" label, blurring the tier gap."
  visible_tells:
  - "\"LifeMD+\" and \"$19/mo\" are clearly differentiated in one row by weight and size"
  - "Bullets like \"24/7 Urgent & Primary Care With Low, Upfront Costs\" are Title Cased and nearly the same size as the plan-name label, collapsing the step down"
  confidence: medium
- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: "homepage hero \u2014 category card grid"
  tile_path: store/lifemd-com/captures/2026-06-15/tiles/homepage/tile-00-y00000.png
  claim: "The hero deploys a disciplined two-card system over a uniform pill-button row \u2014 consistent border-radius, internal padding, and photo-bleed treatment \u2014 showing repeatable component logic, not ad-hoc layout."
  visible_tells:
  - "Weight Loss and Women's Health cards share an identical rounded-rect shell, left-aligned label, and bottom-right portrait bleed"
  - "Three secondary buttons below (Mental Health, Cardiovascular Health, Urgent & Primary Care) share a uniform pill component with icon prefix and chevron suffix"
  - "Two-column split with a consistent inter-card gap"
  confidence: high
- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: "homepage \u2014 repeating category promo blocks (Weight Loss / Women's Health / Mental Health)"
  tile_path: store/lifemd-com/captures/2026-06-15/tiles/homepage/tile-03-y03660.png
  claim: "Successive full-width promo blocks apply the same left-text / right-visual two-column template with consistent padding, CTA placement, and a bottom-right tagline lockup, demonstrating a controlled section component reused at scale."
  visible_tells:
  - "Each block: colored full-bleed background, left column with headline + bullet list + CTA, right column with product/person graphic"
  - "Tagline lockups (\"Unlock Your Potential\", \"Restore Your Rhythm\") appear in identical bottom-right position across blocks"
  - "Inter-block rhythm is consistent \u2014 no collapsed or expanded gaps"
  confidence: high
- id: layout_03
  family: layout_composition_components
  polarity: strong
  page_or_region: "membership \u2014 hero pricing card + image"
  tile_path: store/lifemd-com/captures/2026-06-15/tiles/membership/tile-00-y00000.png
  claim: "The membership hero splits into a well-proportioned two-column layout \u2014 pricing card left, phone-call image right \u2014 both inside matched rounded containers that hold optical balance across the full-bleed blue section."
  visible_tells:
  - "Left card has clean internal structure: name + price row, description, full-width CTA button, then checklist at a consistent left margin"
  - "Right image container matches the card's corner radius and vertical extent"
  - "White circle-checkmark bullets are uniform in size and alignment"
  confidence: high
- id: layout_04
  family: layout_composition_components
  polarity: strong
  page_or_region: "homepage \u2014 insurance provider grid"
  tile_path: store/lifemd-com/captures/2026-06-15/tiles/homepage/tile-08-y09760.png
  claim: "The insurance section is a tight 2\u00d73 logo grid where every cell is an identically-sized rounded rectangle with uniform padding and centered logo \u2014 a precise component system with no misaligned or variably-sized cells."
  visible_tells:
  - "All six tiles (Aetna, BlueCross BlueShield, Health Net, Cigna, United Healthcare, Medicare) share identical dimensions and corner radius"
  - "Each logo is horizontally and vertically centered"
  - "Gaps between tiles are uniform horizontally and vertically"
  confidence: high
- id: layout_05
  family: layout_composition_components
  polarity: strong
  page_or_region: "lifemd_plus \u2014 FAQ accordion"
  tile_path: store/lifemd-com/captures/2026-06-15/tiles/lifemd_plus/tile-03-y03660.png
  claim: "The FAQ accordion holds a stable two-column layout (large heading left, question list right) with no collision \u2014 each row a consistent height with chevron flush-right, reading as a finished component."
  visible_tells:
  - "Left heading anchored top-left of its column with no reflow artifacts"
  - "Each FAQ row has identical divider weight, left-aligned question text, and a same-size chevron at the right edge"
  - "Row heights appear uniform across all visible entries"
  confidence: high
- id: layout_06
  family: layout_composition_components
  polarity: mixed
  page_or_region: "homepage \u2014 product card carousel"
  tile_path: store/lifemd-com/captures/2026-06-15/tiles/homepage/tile-01-y01220.png
  claim: "Card shells are uniform but the product photos crop at noticeably different focal distances within identically-sized cards, weakening the component finish."
  visible_tells:
  - "Wegovy card is a close hand-injection shot while the Estradiol Patch card is a looser top-down pill-on-skin shot \u2014 the crop approach is not normalized"
  - "Card shells (rounded rect, image top, name + category below) are uniform"
  - "Carousel dots and chevrons are positioned correctly but the dot indicator is small relative to the cards"
  confidence: medium
- id: layout_07
  family: layout_composition_components
  polarity: mixed
  page_or_region: "homepage \u2014 \"Medical care when and where you need it\" three-column section"
  tile_path: store/lifemd-com/captures/2026-06-15/tiles/homepage/tile-05-y06100.png
  claim: "The three-column feature row is unbalanced: the left blue card is dense with large text and a CTA, while the two right white cards carry small text and faint UI mocks, leaving an unresolved density mismatch with no shared baseline."
  visible_tells:
  - "Left blue card fills its column with large text + CTA; right two columns show smaller text and faint condition-picker / video-call mocks"
  - "The right columns' illustrative diagrams are much smaller than the left card's content mass"
  - "No vertical separator or shared baseline aligns the three panels"
  confidence: medium
- id: layout_08
  family: layout_composition_components
  polarity: mixed
  page_or_region: "weight_management \u2014 product selector panel"
  tile_path: store/lifemd-com/captures/2026-06-15/tiles/weight_management/tile-01-y01220.png
  claim: "The two-panel selector (list left, detail card right) is competent but \"NEW\" badges appear on some list rows and not others without a reserved badge column, so labeled rows read wider and entry heights vary."
  visible_tells:
  - "\"Wegovy Pill\", \"Foundayo\", \"Zepbound KwikPen\" carry NEW badges; \"Wegovy\", \"Zepbound Vial\" do not \u2014 badge column not reserved"
  - "Green square thumbnails are uniform, but row heights differ between single-line and badge-carrying entries"
  - "Right detail card is clean and well-contained with tag chips, product image, and CTA"
  confidence: medium
- id: layout_09
  family: layout_composition_components
  polarity: mixed
  page_or_region: "womens_health \u2014 \"How LifeMD works\" 4-step process row"
  tile_path: store/lifemd-com/captures/2026-06-15/tiles/womens_health/tile-04-y04880.png
  claim: "The four-step process bar uses an opacity fade to mark inactive steps, but center-aligned text wraps to different depths so the columns bottom-align unevenly, with only a thin top rule and no connector tying the sequence together."
  visible_tells:
  - "\"Complete the online intake\" (Step 1) is fully opaque; Steps 2\u20134 are reduced opacity"
  - "Step text wraps to differing line counts; bottom edges do not share a baseline"
  - "STEP 1\u20134 labels sit above a thin horizontal rule; no connector line or numbered node ties the columns as a sequence"
  confidence: medium
- id: layout_10
  family: layout_composition_components
  polarity: poor
  page_or_region: "homepage \u2014 patient review mosaic grid"
  tile_path: store/lifemd-com/captures/2026-06-15/tiles/homepage/tile-07-y08540.png
  claim: "The review section mixes portrait-photo cards and text-only cards in adjacent cells without a shared row height, producing mismatched density that reads unfinished rather than editorial."
  visible_tells:
  - "Top row: two text-only review cards flanking a taller portrait card, leaving unequal bottom margins"
  - "Bottom row repeats the mismatch in reverse"
  - "Star ratings and reviewer attribution lines are lightweight and sit at inconsistent vertical positions across cells"
  confidence: medium
  contrast_with: store/lifemd-com/captures/2026-06-15/tiles/homepage/tile-08-y09760.png
- id: layout_11
  family: layout_composition_components
  polarity: strong
  page_or_region: "womens_health \u2014 \"World-renowned experts\" provider card list"
  tile_path: store/lifemd-com/captures/2026-06-15/tiles/womens_health/tile-02-y02440.png
  claim: "Three stacked provider cards each use the same three-zone internal layout (headshot left, name + role center, institution logo right) at identical card dimensions \u2014 a well-constrained repeating component."
  visible_tells:
  - "Each card: square headshot left, name in medium weight + role in small caps center, university logo right \u2014 alignment holds across all three"
  - "Card border, padding, and corner radius are visually identical across the three rows"
  - "Institution logos (UC Irvine, Stanford, SUNY) are scaled to a consistent optical size despite different source proportions"
  confidence: high
- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: "homepage \u2014 hero category cards"
  tile_path: store/lifemd-com/captures/2026-06-15/tiles/homepage/tile-00-y00000.png
  claim: "The hero applies a per-category color system \u2014 teal for weight loss, lavender for women's health, plus coral/red/blue accents on the secondary pills \u2014 used consistently as card fills, not arbitrary hues."
  visible_tells:
  - "Two large hero cards in distinct solid fills (teal left, lavender right)"
  - "Three smaller pill buttons below carry separate accent colors (blue, coral-red, blue) tracking their category"
  confidence: high
  contrast_with: store/lifemd-com/captures/2026-06-15/tiles/homepage/tile-05-y06100.png
- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: "homepage \u2014 Wegovy promotional band"
  tile_path: store/lifemd-com/captures/2026-06-15/tiles/homepage/tile-01-y01220.png
  claim: "The weight-management band commits to a single saturated teal fill top-to-bottom finished with an organic white wave divider \u2014 a confident full-bleed brand-color module rather than a default white band."
  visible_tells:
  - "Uniform deep teal background covering the full-width module"
  - "Organic white wave transition at the bottom edge separating it from the next section"
  confidence: high
- id: color_03
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "homepage \u2014 product card carousel photography"
  tile_path: store/lifemd-com/captures/2026-06-15/tiles/homepage/tile-01-y01220.png
  claim: "Product photo backgrounds vary per card \u2014 peach, lavender, grey, blue-grey \u2014 suggesting per-product tinting rather than an enforced art-direction rule, with no shared crop or prop styling linking them as a family."
  visible_tells:
  - "Four card thumbnails side by side with visibly different background tints"
  - "No shared crop ratio or consistent prop styling across the four"
  confidence: medium
  contrast_with: store/lifemd-com/captures/2026-06-15/tiles/homepage/tile-00-y00000.png
- id: color_04
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "weight_management \u2014 patient testimonial photos"
  tile_path: store/lifemd-com/captures/2026-06-15/tiles/weight_management/tile-02-y02440.png
  claim: "Testimonial photos are candid user-submitted snapshots \u2014 mixed color temperatures, framing, and lighting \u2014 creating a visible seam between the polished hero above and this section."
  visible_tells:
  - "Three testimonial images at different ambient light conditions: bright outdoor, dimmer indoor, overcast outdoor"
  - "No consistent background, crop, or filter treatment unifying the three"
  confidence: high
  contrast_with: store/lifemd-com/captures/2026-06-15/tiles/weight_management/tile-00-y00000.png
- id: color_05
  family: color_brand_imagery
  polarity: strong
  page_or_region: "weight_management \u2014 hero"
  tile_path: store/lifemd-com/captures/2026-06-15/tiles/weight_management/tile-00-y00000.png
  claim: "The weight-management hero repeats the homepage teal palette as a full-bleed teal-to-green field with a produced model shot whose dark top integrates cleanly with the color, reading as intentional art direction."
  visible_tells:
  - "Full-bleed teal-to-green gradient hero background"
  - "Model in a dark top photographed on a studio-lit cutout that blends into the color field"
  confidence: high
- id: color_06
  family: color_brand_imagery
  polarity: strong
  page_or_region: "womens_health \u2014 hero"
  tile_path: store/lifemd-com/captures/2026-06-15/tiles/womens_health/tile-00-y00000.png
  claim: "The women's-health hero shifts to a warm greige/taupe field with a higher-quality editorial natural-light portrait, signaling a deliberate per-vertical palette rather than a site-wide monochrome."
  visible_tells:
  - "Muted warm taupe field behind a woman shot with editorial natural-light quality"
  - "Wardrobe (black jacket, neutral tones) coordinates with the background and departs from the teal/blue of other pages"
  confidence: high
  contrast_with: store/lifemd-com/captures/2026-06-15/tiles/lifemd_plus/tile-00-y00000.png
- id: color_07
  family: color_brand_imagery
  polarity: poor
  page_or_region: "lifemd_plus \u2014 photo carousel (Tap. Talk. Treat.)"
  tile_path: store/lifemd-com/captures/2026-06-15/tiles/lifemd_plus/tile-02-y02440.png
  claim: "The LifeMD+ carousel casts a heavy blue/cyan digital overlay across its lifestyle photos, reading as stock-photo-with-color-grade and washing out subject detail \u2014 a treatment absent from the cleaner heroes elsewhere."
  visible_tells:
  - "All three carousel images carry a strong blue/cyan overlay obscuring face and clothing detail"
  - "The blue cast is absent on the women's-health and weight-management hero photography, marking it inconsistent"
  confidence: high
  contrast_with: store/lifemd-com/captures/2026-06-15/tiles/womens_health/tile-00-y00000.png
- id: color_08
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "membership \u2014 hero full-bleed band"
  tile_path: store/lifemd-com/captures/2026-06-15/tiles/membership/tile-00-y00000.png
  claim: "The membership hero uses a lighter, cooler sky-blue gradient than the deep teal on the homepage/weight-management blocks \u2014 the blue family is reused but drifts in value, and the white pricing card recedes into the pale field rather than popping as on the teal modules."
  visible_tells:
  - "Full-bleed sky-blue gradient distinctly lighter than the teal heroes"
  - "White phone mockup and CTA card sit low-contrast against the light blue"
  confidence: medium
  contrast_with: store/lifemd-com/captures/2026-06-15/tiles/homepage/tile-01-y01220.png
- id: color_09
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "homepage \u2014 \"Feel better\" lifestyle photography band"
  tile_path: store/lifemd-com/captures/2026-06-15/tiles/homepage/tile-05-y06100.png
  claim: "The full-bleed outdoor lifestyle photo (woman in tall grass, golden-hour tone) is generic wellness stock with no brand color, product, or telehealth context, breaking the category-coded color logic established in the sections above."
  visible_tells:
  - "Full-bleed warm golden-hour outdoor photo unrelated to the teal/lavender/blue palette"
  - "No product, device, or telehealth UI element in frame"
  confidence: high
  contrast_with: store/lifemd-com/captures/2026-06-15/tiles/homepage/tile-00-y00000.png
- id: color_10
  family: color_brand_imagery
  polarity: strong
  page_or_region: "homepage \u2014 \"Meet your LifeMD medical care team\" doctor portraits"
  tile_path: store/lifemd-com/captures/2026-06-15/tiles/homepage/tile-06-y07320.png
  claim: "Doctor portraits are produced on consistent neutral grey backgrounds with matching head-and-shoulder crops and medical attire, giving the credibility section a unified look through restraint rather than color."
  visible_tells:
  - "Two doctor portraits (Dr. Doug Lucas, Dr. Anthony Puopolo) share a neutral-grey background and similar crop"
  - "Both in professional medical attire; a LifeMD logo is visible on one scrub"
  confidence: high
- id: color_11
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "womens_health \u2014 \"Healthcare designed with you in mind\" feature cards"
  tile_path: store/lifemd-com/captures/2026-06-15/tiles/womens_health/tile-03-y03660.png
  claim: "The feature-card row defaults to a near-white/light-beige background with small grey icon chips holding generic line-art \u2014 competent and clean but with no owned visual language tying it to the category palette or hero imagery."
  visible_tells:
  - "Three cards on very light warm off-white with small grey rounded icon containers"
  - "Icons are generic line-art (stethoscope, box, heart motif) with no custom illustration character"
  confidence: medium
- id: iconography_01
  family: iconography_illustration
  polarity: strong
  page_or_region: "weight_management \u2014 medication selector list (left rail)"
  tile_path: store/lifemd-com/captures/2026-06-15/tiles/weight_management/tile-01-y01220.png
  claim: "The medication list uses uniform rounded green thumbnail tiles with consistently-scaled product-photo insets, functioning as a coherent mini icon system rather than plain text links, paired with a clean studio render in the detail panel."
  visible_tells:
  - "Eight medication entries each carry an identically-sized green rounded tile with a miniature product photo at the same scale"
  - "The active detail panel shows a clean studio render of the Wegovy pill on a neutral ground with no shadow artifacts"
  confidence: high
- id: iconography_02
  family: iconography_illustration
  polarity: strong
  page_or_region: "homepage \u2014 hero category tiles (Weight Loss / Women's Health)"
  tile_path: store/lifemd-com/captures/2026-06-15/tiles/homepage/tile-00-y00000.png
  claim: "The color-blocked hero cards embed product thumbnails at a uniform small scale and consistent placement, showing a resolved system where color, image crop, and card geometry are coordinated across categories."
  visible_tells:
  - "Weight Loss (teal) and Women's Health (lavender) cards share the same geometry and thumbnail-placement rules"
  - "Product thumbnails inside each card sit at consistent angle and size"
  confidence: high
  contrast_with: store/lifemd-com/captures/2026-06-15/tiles/homepage/tile-04-y04880.png
- id: iconography_03
  family: iconography_illustration
  polarity: strong
  page_or_region: "womens_health \u2014 HRT treatment-option product cards"
  tile_path: store/lifemd-com/captures/2026-06-15/tiles/womens_health/tile-01-y01220.png
  claim: "HRT product photography (cream, patch, vaginal insert, progesterone bottle) is shot on a matched warm-beige ground with unified staging, making the product set read as designed rather than assembled stock."
  visible_tells:
  - "All product cards use the same warm sand background tone"
  - "Patch shown slightly splayed to convey form factor; cream bottle centered upright \u2014 different props, unified staging"
  confidence: high
- id: iconography_04
  family: iconography_illustration
  polarity: mixed
  page_or_region: "weight_management \u2014 feature-benefit cards (Dedicated Medical Experts / Unlock Your Full Potential)"
  tile_path: store/lifemd-com/captures/2026-06-15/tiles/weight_management/tile-04-y04880.png
  claim: "The two supporting feature cards use small grey line-art icons (person-in-circle, upward chart) that are functional but generic \u2014 they read as default UI-pack glyphs, diluting the otherwise polished product photography nearby."
  visible_tells:
  - "\"Dedicated Medical Experts\" uses a standard person-with-circle silhouette with no stylistic personality"
  - "\"Unlock Your Full Potential\" uses a plain upward-trend line, indistinguishable from default system iconography"
  confidence: high
  contrast_with: store/lifemd-com/captures/2026-06-15/tiles/weight_management/tile-01-y01220.png
- id: iconography_05
  family: iconography_illustration
  polarity: mixed
  page_or_region: "membership \u2014 benefit badge chips (FAST / CONVENIENT / AFFORDABLE / IMMEDIATE)"
  tile_path: store/lifemd-com/captures/2026-06-15/tiles/membership/tile-02-y02440.png
  claim: "Benefit badges overlay each portrait card consistently, but the filled-circle checkmark glyph is a commodity UI element \u2014 placement is uniform, yet no custom illustration lifts the cards beyond template quality."
  visible_tells:
  - "The same dark pill badge with check + label appears on all four portrait cards at the same position"
  - "The check glyph is a standard filled circle with a tick"
  confidence: medium
- id: iconography_06
  family: iconography_illustration
  polarity: mixed
  page_or_region: "lifemd_plus \u2014 \"Why Choose LifeMD+?\" three-up cards"
  tile_path: store/lifemd-com/captures/2026-06-15/tiles/lifemd_plus/tile-01-y01220.png
  claim: "The three benefit cards substitute cut-out photos for icons, sidestepping icon design but producing inconsistent visual weight \u2014 the full-torso doctor photo dominates the smaller object-only phone and pill-bottle shots beside it."
  visible_tells:
  - "Card 1 is a full-torso doctor photo; cards 2 and 3 are object-only crops (phone, pill bottle) \u2014 no unified illustration logic"
  - "No icon system present; photographic illustration is the substitute"
  confidence: medium
- id: iconography_07
  family: iconography_illustration
  polarity: poor
  page_or_region: "homepage \u2014 \"Medical care when and where you need it\" supporting cards"
  tile_path: store/lifemd-com/captures/2026-06-15/tiles/homepage/tile-05-y06100.png
  claim: "The two supporting cards in this section carry no icons or illustration \u2014 only faint grey text/UI-mock blocks \u2014 leaving them visually inert with no iconography to carry the pattern used elsewhere."
  visible_tells:
  - "\"24/7 Urgent & Primary Care\" card shows only a faint condition-list mock (flu symptoms, digestive health, pink eye, sinus infections) with no icons"
  - "The \"Convenient Virtual Consultations\" card is similarly empty of graphic treatment"
  confidence: high
  contrast_with: store/lifemd-com/captures/2026-06-15/tiles/weight_management/tile-01-y01220.png
- id: iconography_08
  family: iconography_illustration
  polarity: strong
  page_or_region: "homepage \u2014 app-promo band (\"Your doctor is online and ready to see you\")"
  tile_path: store/lifemd-com/captures/2026-06-15/tiles/homepage/tile-08-y09760.png
  claim: "The blue app-promo band renders a phone device mockup with a legible in-app interface \u2014 weight chart, patient messaging, doctor avatar \u2014 at sufficient resolution to read individual UI elements, the strongest product-render moment captured."
  visible_tells:
  - "Phone screen shows a recognizable weight-management line graph with current vs. goal figures (143 / 120 lbs)"
  - "A LifeMD+ messaging thread with a doctor avatar is visible and legible at display size"
  confidence: high
  contrast_with: store/lifemd-com/captures/2026-06-15/tiles/homepage/tile-09-y10980.png
- id: iconography_09
  family: iconography_illustration
  polarity: poor
  page_or_region: "homepage footer \u2014 app-download panel (\"Healthcare, Made Simple\")"
  tile_path: store/lifemd-com/captures/2026-06-15/tiles/homepage/tile-09-y10980.png
  claim: "The footer app-download phone mockup is rendered small with an illegible app screen and no depth treatment, demonstrating none of the product-render craft shown in the app-promo band above."
  visible_tells:
  - "The footer phone mockup sits on a dark panel with screen content too small to read"
  - "No shadow, lighting, or depth on the device frame \u2014 flat placeholder quality"
  confidence: medium
  contrast_with: store/lifemd-com/captures/2026-06-15/tiles/homepage/tile-08-y09760.png
- id: iconography_10
  family: iconography_illustration
  polarity: mixed
  page_or_region: "lifemd_plus \u2014 pricing-card benefit checkmarks"
  tile_path: store/lifemd-com/captures/2026-06-15/tiles/lifemd_plus/tile-03-y03660.png
  claim: "The benefit bullets use teal-blue filled-circle checkmarks that align with the brand color but are a commodity glyph \u2014 the color match keeps them from feeling foreign without adding distinctive illustration craft."
  visible_tells:
  - "Five checklist bullets (\"24/7 urgent & primary care\u2026\", \"Access to message-\u2026\", etc.) all use the same teal filled-circle checkmark at uniform size"
  - "No custom icon shape \u2014 identical to default checkmark icons in any component library"
  confidence: medium
```

## Provenance

- **Tiles read:** 43 native-resolution tiles across 5 pages (homepage, weight_management, womens_health, membership, lifemd_plus) sliced from the cached 2026-06-15 full-page screenshots (`captures/2026-06-15/tiles/`).
- **QA:** `clean` — all five page overviews inspected; no modals, grey/blank heroes, black media, lazy-load gaps, or mid-animation artifacts. No tiles excluded; no Tier-B browser re-render needed. (Judge note: a faint translucent scrim *is* present on the homepage doctor-team overlay tile, so two over-stated "no scrim" cards were rejected/merged.)
- **Mining:** blind fan-out via `mine.workflow.js` — 4 family miners (Sonnet, tiles-only, no web/dossier access) → judge (Opus). 49 cards mined → **40 accepted / 10 rejected**. The miners never saw `profile.md` or the company's identity; the read is perception, not reputation.
- **Card count:** 40 (above the 8–14 norm) reflects a content-rich 5-page mine spanning all four families; the judge's full tile-verified set is kept as the audit trail (the impression above is the consumable lens).
- **Point-in-time:** the site A/B-tests (PostHog session replay + surveys) and runs promos; these tiles are a 2026-06-15 snapshot, not a fixed truth.
