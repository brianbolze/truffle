---
schema_version: "1.0"
domain: kingsbergmedical.com
captured_at: 2026-06-14
source_capture: 2026-06-09
qa_status: clean
---

## Visual & brand impression

A low-craft TRT template leaning on purchased stock to carry the brand. The hero stays legible only via a translucent box over a generic alpine-mountain photo with cut-out stock doctors [color_01][typography_01]; imagery is uniformly bought-in — clipboard medical stock, a clip-art ball-and-stick molecule, a low-res pathway diagram, cut-out 'aging male' composites [color_06][iconography_01][iconography_04]. Type flattens hierarchy by setting body all-bold and muting section titles to grey [typography_02][typography_04]. Layout discipline is the relative bright spot — an even three-column grid and a tidy footer [layout_02][layout_08] — but it's punctured by large empty green voids [layout_05] and a form composited over a hard-cut doctor cutout [layout_12]. Cleanest where plainest: a flat green banner under a serif headline [typography_05].

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: mixed
  page_or_region: homepage hero overlay
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/homepage/tile-00-y00000.png
  claim: The reversed white hero headline 'The Most Effective Hormone Replacement Therapies' sits in a sans-serif over busy mountain imagery, kept legible only by a semi-transparent dark box rather than a strong type-to-image relationship.
  visible_tells:
  - white sans-serif headline confined to a translucent grey rectangle in the upper-right hero
  - headline competes with the textured rock and sky behind the box edges
  confidence: medium
- id: typography_02
  family: typography_hierarchy
  polarity: poor
  page_or_region: homepage 'Experience You Can Trust' section
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/homepage/tile-01-y01220.png
  claim: A serif display headline is paired with a centered all-bold sans-serif body block, removing the regular/bold contrast that normally carries hierarchy.
  visible_tells:
  - serif 'Experience You Can Trust - Compassion You Can Count On' above bold sans-serif centered paragraphs
  - every body line set in bold weight, flattening the type into one emphasis level
  confidence: high
- id: typography_03
  family: typography_hierarchy
  polarity: mixed
  page_or_region: homepage 'Improve Your Health' benefit blocks
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/homepage/tile-01-y01220.png
  claim: The left-aligned 'Benefits of Growth Hormone Therapy' subhead with an underline rule and grey body sets a clear left-rail hierarchy that clashes with the centered serif 'Improve Your Health' title sitting above it, a mixed alignment system.
  visible_tells:
  - bold left-aligned subhead with a thin horizontal rule beneath, body left-aligned below
  - centered serif section title directly above the left-aligned block
  confidence: high
  contrast_with: store/kingsbergmedical-com/captures/2026-06-09/tiles/homepage/tile-00-y00000.png
- id: typography_04
  family: typography_hierarchy
  polarity: poor
  page_or_region: homepage '3 Easy Steps' section title
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/homepage/tile-02-y02440.png
  claim: The serif section title 'Get Started Growth Hormone and Testosterone Therapies' is rendered in muted grey that lowers its contrast on white, so the glossy green 1/2/3 badges below carry more visual weight than the heading.
  visible_tells:
  - two-line serif heading set in grey rather than near-black
  - saturated green numbered badges below outweigh the muted title
  confidence: medium
- id: typography_05
  family: typography_hierarchy
  polarity: strong
  page_or_region: homepage green section banner
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/homepage/tile-03-y03660.png
  claim: The white serif headline 'Growth Hormone and Testosterone Medications' reversed on a solid dark-green band reads cleanly with high contrast and clear dominance, since no imagery sits behind the text.
  visible_tells:
  - white serif headline centered on a flat dark-green block
  - no photo or texture behind the text, so contrast is uncompromised
  confidence: high
  contrast_with: store/kingsbergmedical-com/captures/2026-06-09/tiles/homepage/tile-00-y00000.png
- id: typography_06
  family: typography_hierarchy
  polarity: mixed
  page_or_region: homepage FAQ filter row
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/homepage/tile-03-y03660.png
  claim: Under the large serif 'Frequently Asked Questions' title, the filter labels 'All (63) | Growth Hormone (30) | Testosterone (33)' are tiny pipe-separated items with no intermediate-size element bridging the steep jump from heading to controls.
  visible_tells:
  - large serif FAQ heading directly above very small green pipe-separated filter labels
  - no mid-size element between the heading and the small filter row
  confidence: medium
- id: typography_07
  family: typography_hierarchy
  polarity: poor
  page_or_region: homepage footer columns
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/homepage/tile-05-y04957.png
  claim: The footer packs four small-caps column headers over tightly stacked grey links and a multi-line address with minimal size contrast, reading as a dense uniform block.
  visible_tells:
  - '''GET STARTED / OUR CLINIC / OUR PARTNERS / CONTACTS'' headers barely larger than the link list beneath them'
  - address lines and link items share nearly the same small grey type size
  confidence: medium
- id: typography_08
  family: typography_hierarchy
  polarity: poor
  page_or_region: services page intro and meta line
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/services/tile-00-y00000.png
  claim: The 'Services provided by Kingsberg Medical' heading is crowded by a cramped bulleted list in very small italic green and a tiny right-aligned 'Medically reviewed by' meta block, jamming several type sizes into a small area.
  visible_tells:
  - small italic green bullet items immediately under the heading
  - tiny grey/green 'Medically reviewed by / Written by' meta lines stacked top-right
  confidence: medium
- id: typography_09
  family: typography_hierarchy
  polarity: strong
  page_or_region: services article list headlines
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/services/tile-05-y06100.png
  claim: The article list uses large green serif headlines with a small grey deck and a green caps 'READ MORE' link in thumbnail-left / text-right rows, establishing three clear and repeatable levels.
  visible_tells:
  - large serif green titles 'Does Sermorelin Work?', 'Sermorelin vs Ipamorelin' above grey two-line decks
  - uniform 'READ MORE ->' caps links and rule dividers repeated down every row
  confidence: high
- id: typography_10
  family: typography_hierarchy
  polarity: strong
  page_or_region: testosterone page headline
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/testosterone/tile-00-y00000.png
  claim: The dark serif page headline 'Testosterone Can Be Vital to Peak Performance at Any Age' is the clear dominant level, well-sized and high-contrast on white above a small italic bullet list.
  visible_tells:
  - two-line serif headline in near-black at top of the content column
  - markedly larger than the small italic green bullets beneath it
  confidence: high
- id: typography_11
  family: typography_hierarchy
  polarity: mixed
  page_or_region: testosterone pull-quote block
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/testosterone/tile-03-y03660.png
  claim: The green-tinted italic pull-quote is visually distinct from body, but its small italic size on a faint green-on-green panel gives it weaker emphasis than a callout of that prominence usually carries.
  visible_tells:
  - italic quote 'Testosterone therapy is only available with a doctor's prescription...' on a pale green panel
  - quote type size barely exceeds surrounding body, limiting its callout weight
  confidence: medium
- id: typography_12
  family: typography_hierarchy
  polarity: poor
  page_or_region: testosterone benefits bullet list
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/testosterone/tile-04-y04880.png
  claim: The long benefits list runs as small uniform grey lines with no bolded lead-ins, so a dozen distinct claims flatten into one undifferentiated wall of list items.
  visible_tells:
  - roughly nine near-identical grey bullet lines with no emphasized keywords
  - no sub-grouping or weight variation across the list
  confidence: medium
- id: typography_13
  family: typography_hierarchy
  polarity: mixed
  page_or_region: testosterone 'GET STARTED' form card
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/testosterone/tile-05-y05538.png
  claim: The white reversed 'GET STARTED' headline over a photographic form card stays readable, but the field-placeholder text sits low-contrast against the scenic background.
  visible_tells:
  - large white 'GET STARTED' and bold caps subline reversed over a mountain photo
  - grey placeholder labels inside semi-transparent input fields read faintly against the image
  confidence: medium
- id: layout_01
  family: layout_composition_components
  polarity: mixed
  page_or_region: homepage hero (header + banner)
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/homepage/tile-00-y00000.png
  claim: 'The hero is a competent but dated template: a translucent grey caption box and pill CTA float over a mountain photo, with the two-doctor cutout composited flat against the landscape.'
  visible_tells:
  - semi-transparent grey rounded box holding the headline, no grid relationship to the image edges
  - green rounded GET STARTED pill with circular icon stacked directly under the caption box
  - doctor figures cut out and pasted over the mountain backdrop
  confidence: medium
- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: homepage three-up service cards
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/homepage/tile-01-y01220.png
  claim: The three service cards form a disciplined, evenly-gapped 3-column grid with consistent image height, bold centered titles, and matched body blocks aligned to the same baselines.
  visible_tells:
  - three equal-width columns with uniform gutters
  - each card repeats image-then-bold-title-then-paragraph in the same order
  - titles and paragraph tops align across all three columns
  confidence: high
  contrast_with: store/kingsbergmedical-com/captures/2026-06-09/tiles/homepage/tile-04-y04880.png
- id: layout_03
  family: layout_composition_components
  polarity: poor
  page_or_region: homepage 'Improve Your Health' benefits section
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/homepage/tile-02-y02440.png
  claim: The benefits section leaves the entire right half of the band empty, with three stacked text blocks crammed into the left column and a large void of pale-green space beside them.
  visible_tells:
  - three underlined headings with paragraphs all confined to the left third
  - the right majority of the section is blank pale-green background with no content
  - no image or component fills the intended second column
  confidence: high
- id: layout_04
  family: layout_composition_components
  polarity: mixed
  page_or_region: homepage '3 Easy Steps' numbered process row
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/homepage/tile-02-y02440.png
  claim: The three-step row is cleanly structured with evenly spaced glossy numbered badges, centered titles and matched captions, though the skeuomorphic beveled 1-2-3 buttons read as a dated stock component.
  visible_tells:
  - three green circular badges 1/2/3 at equal column centers
  - each badge above a bold two-line title and a centered caption of similar length
  - badges carry glossy gradient and drop-shadow bevel typical of older UI kits
  confidence: medium
- id: layout_05
  family: layout_composition_components
  polarity: poor
  page_or_region: homepage 'Growth Hormone and Testosterone Medications' green band
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/homepage/tile-04-y04880.png
  claim: A dark-green section header is followed by an enormous empty solid-green block roughly two viewports tall with no content rendered inside it.
  visible_tells:
  - white serif heading on a green bar at top
  - a flat dark-green rectangle spanning full width and several hundred pixels tall below it holding nothing
  - the void ends abruptly at a white section
  confidence: medium
- id: layout_06
  family: layout_composition_components
  polarity: mixed
  page_or_region: homepage FAQ filter tabs + CTA
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/homepage/tile-04-y04880.png
  claim: The FAQ block shows only a thin row of pipe-separated filter labels and a lone green VIEW MORE button, leaving the section sparse with collapsed content and large surrounding whitespace.
  visible_tells:
  - '''All (63) | Growth Hormone (30) | Testosterone (33)'' as a single text line'
  - one centered green VIEW MORE pill with caret below the tabs
  - no question rows visible between the heading and the button
  confidence: medium
- id: layout_07
  family: layout_composition_components
  polarity: poor
  page_or_region: homepage 'Our Mission and Goals' block
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/homepage/tile-05-y04957.png
  claim: The mission block uses a left green accent rule but centers the heading and paragraphs toward the page middle, leaving a wide empty gutter between the rule and the text start, an off-center composition.
  visible_tells:
  - green vertical rule pinned to the far left edge
  - serif heading and two paragraphs centered toward the page middle, not aligned to the rule
  - large blank band between the rule and the text
  confidence: high
  contrast_with: store/kingsbergmedical-com/captures/2026-06-09/tiles/homepage/tile-02-y02440.png
- id: layout_08
  family: layout_composition_components
  polarity: strong
  page_or_region: homepage footer (four-column)
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/homepage/tile-05-y04957.png
  claim: The footer is a tidy four-column layout with uppercase section labels, a CTA button, a vertical link list, partner logos and an address block, each column top-aligned to a shared baseline.
  visible_tells:
  - GET STARTED / OUR CLINIC / OUR PARTNERS / CONTACTS headers aligned in one row
  - evenly spaced vertical link list under OUR CLINIC
  - address and phone block in its own right column with matching top edge
  confidence: high
- id: layout_09
  family: layout_composition_components
  polarity: mixed
  page_or_region: services page intro + sidebar start
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/services/tile-00-y00000.png
  claim: The services page opens a two-column body (main content left, narrow sidebar right) but the reused mountain hero is vertically clipped at the breadcrumb bar and the byline/review meta is rendered tiny against the heading.
  visible_tells:
  - main heading and green bullet list in the left column with a thin right sidebar column
  - '''Medically reviewed by'' meta set in very small text at the top-right'
  - the homepage mountain hero reappears, cropped at the green breadcrumb strip
  confidence: medium
- id: layout_10
  family: layout_composition_components
  polarity: mixed
  page_or_region: services page 'Top Stories' sidebar list
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/services/tile-01-y01220.png
  claim: The right sidebar stacks a repeated thumbnail-plus-label list with a consistent row rhythm, but the items use very small thumbnails and a dense 'Schedule Your Blood Test' promo card is crammed directly beneath with little separation.
  visible_tells:
  - '''Top Stories'' rows each with a small left thumbnail and short title'
  - consistent row rhythm down the rail
  - a dense green/blue promo card butting up immediately under the list
  confidence: medium
- id: layout_11
  family: layout_composition_components
  polarity: poor
  page_or_region: services page main column body copy
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/services/tile-01-y01220.png
  claim: Long undifferentiated paragraphs and a bulleted symptom list run down a narrow left measure while a single inset green callout breaks the otherwise flat text run, producing an unbalanced single-column-in-a-two-column shell.
  visible_tells:
  - dense stacked paragraphs and a vertical bullet list confined to the left measure
  - one inset green-tinted callout box interrupting the flat text run
  confidence: medium
- id: layout_12
  family: layout_composition_components
  polarity: poor
  page_or_region: services page 'Get Started' lead form
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/services/tile-04-y04880.png
  claim: The inline lead-capture form is composited over a photo of a doctor whose hard-cut figure overlaps the form panel, with input fields rendered as faint low-contrast bars that blend into the background image.
  visible_tells:
  - four near-transparent input fields and a green SUBMIT REQUEST button on a photographic background
  - doctor cutout overlapping the right edge of the form panel
  - field labels barely legible against the landscape photo behind them
  confidence: medium
- id: layout_13
  family: layout_composition_components
  polarity: strong
  page_or_region: services page article list (Sermorelin etc.)
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/services/tile-05-y06100.png
  claim: 'The related-articles list is a consistent media-object pattern: left thumbnail, green serif headline, two-line excerpt and a READ MORE link, repeated identically and separated by thin horizontal rules.'
  visible_tells:
  - each row pairs a square thumbnail on the left with title-excerpt-link on the right
  - uniform thin divider lines between every article row
  - READ MORE with arrow at the same offset under each excerpt
  confidence: high
  contrast_with: store/kingsbergmedical-com/captures/2026-06-09/tiles/services/tile-01-y01220.png
- id: layout_14
  family: layout_composition_components
  polarity: poor
  page_or_region: testosterone page 'Declines As You Age' figure row
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/testosterone/tile-02-y02440.png
  claim: A full-width row of age-progression figures is dropped between flat text blocks with generous empty margins above and below, reading as an isolated stock graphic rather than an integrated component.
  visible_tells:
  - six standing male figures spaced left-to-right with cast reflections
  - large empty white margins flanking the figure row
  - the graphic sits between a green pull-quote and a bullet list with no framing container
  confidence: medium
- id: color_01
  family: color_brand_imagery
  polarity: poor
  page_or_region: homepage hero (top)
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/homepage/tile-00-y00000.png
  claim: The hero is a generic stock alpine-mountain landscape behind cut-out stock doctors, with no owned or location-specific imagery tying it to the brand.
  visible_tells:
  - jagged snow-dappled mountain range with green valley behind the doctor pair
  - two white-coat doctors composited as foreground cut-outs over the scenic backdrop
  confidence: high
- id: color_02
  family: color_brand_imagery
  polarity: poor
  page_or_region: homepage 'Get Started' three-up
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/homepage/tile-01-y01220.png
  claim: The three service thumbnails are mismatched stock cut-outs — two white-coat figures on white plus one teal-scrubbed tech on a different crop — so the image language has no shared treatment.
  visible_tells:
  - left two images are isolated-on-white doctor cut-outs, the third is a teal-scrub figure handling a blood vial
  - inconsistent crop, lighting, and background between the three tiles
  confidence: high
- id: color_03
  family: color_brand_imagery
  polarity: poor
  page_or_region: homepage brand palette — two competing greens
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/homepage/tile-04-y04880.png
  claim: Two unrelated greens run on one tile — a saturated lime green for the VIEW MORE button and a muted olive/forest green for the heading band — reading as an undisciplined palette rather than a controlled brand color.
  visible_tells:
  - bright lime-green 'VIEW MORE' button
  - desaturated olive-green section band behind the white 'Growth Hormone and Testosterone Medications' heading
  confidence: high
- id: color_04
  family: color_brand_imagery
  polarity: mixed
  page_or_region: homepage mid-page tinted sections
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/homepage/tile-05-y04957.png
  claim: A pale mint-green section tint is applied consistently as a band background and reused for the footer, giving a recognizable low-saturation brand wash.
  visible_tells:
  - full-width pale mint-green band behind 'Want to improve your health today'
  - same tint reused for the footer block
  confidence: medium
- id: color_05
  family: color_brand_imagery
  polarity: poor
  page_or_region: homepage footer partner logos
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/homepage/tile-05-y04957.png
  claim: The navy-blue A4M/MMI partner logo block is the only saturated cool color on the page and clashes with the green brand system, breaking palette coherence.
  visible_tells:
  - dark navy square logos reading 'A4M' and 'MMI' in the footer
  - navy sits against the green section tint and green 'KINGSBERG MEDICAL' label
  confidence: high
- id: color_06
  family: color_brand_imagery
  polarity: poor
  page_or_region: services — Rx 'Hormone Therapy' stock photo
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/services/tile-00-y00000.png
  claim: The body imagery is generic medical stock — a clipboard with handwritten 'Hormone Therapy', a pen and stethoscope in warm brown tones — that doesn't relate to the green brand palette.
  visible_tells:
  - stock photo of an Rx prescription pad with cursive 'Hormone Therapy' and a pen
  - warm wood/skin tones clash with the page's green accents
  confidence: high
- id: color_07
  family: color_brand_imagery
  polarity: poor
  page_or_region: services sidebar 'Schedule Your Blood Test' panel
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/services/tile-01-y01220.png
  claim: The sidebar promo panel introduces a third blue-and-lime gradient color scheme distinct from both brand greens, fragmenting the palette further.
  visible_tells:
  - blue-tinted lab background with diagonal lime-green band reading 'Schedule Your Blood Test'
  - blue/lime gradient differs from the olive heading green and mint section tint
  confidence: medium
- id: color_08
  family: color_brand_imagery
  polarity: poor
  page_or_region: services 'Get Started' form panel
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/services/tile-05-y06100.png
  claim: The lead-capture panel composites a smiling doctor stock cut-out over a washed mountain scene with translucent form fields and faux-3D beveled 'GET STARTED' type, an assembled look with mismatched lighting between figure and background.
  visible_tells:
  - doctor in red tie cut out over a blurry green hillside
  - '''GET STARTED'' set in faux-3D beveled white type over the photo'
  confidence: high
- id: color_09
  family: color_brand_imagery
  polarity: poor
  page_or_region: testosterone — vial stock photography
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/testosterone/tile-03-y03660.png
  claim: The 'TESTOSTERONE' vials-on-prescription-pad photo is cool blue-toned generic medical stock, pulling the imagery away from the green brand into an unrelated blue color world.
  visible_tells:
  - two blue-capped vials labeled 'TESTOSTERONE' on a blue prescription pad
  - cool blue cast across the whole product shot
  confidence: high
  contrast_with: store/kingsbergmedical-com/captures/2026-06-09/tiles/services/tile-00-y00000.png
- id: iconography_01
  family: iconography_illustration
  polarity: poor
  page_or_region: testosterone page — molecular structure diagram below 'Testosterone' heading
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/testosterone/tile-00-y00000.png
  claim: The testosterone ball-and-stick diagram is unmodified purchased clip-art, with the stock-marketplace watermark text left in place rather than removed.
  visible_tells:
  - literal label 'VECTOR OBJECTS EPS 10' printed under the 'Testosterone / Primary male sex Hormone / Anabolic Steroid' title
  - generic teal ball-and-stick molecule that reads as a stock asset dropped onto a white field
  confidence: high
- id: iconography_02
  family: iconography_illustration
  polarity: poor
  page_or_region: testosterone page — molecule legend and chemical-structure inset
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/testosterone/tile-01-y01220.png
  claim: The Carbon/Oxygen/Hydrogen color key in flat 3D-ball style sits beside a thin line-drawn skeletal steroid formula, so two incompatible stock chemistry illustration languages share one block without unification.
  visible_tells:
  - circular color-key dots labeled Carbon/Oxygen/Hydrogen in flat 3D-ball style
  - adjacent line-drawn skeletal steroid formula in a thin black style — two mismatched graphics side by side
  confidence: high
- id: iconography_03
  family: iconography_illustration
  polarity: mixed
  page_or_region: homepage — '3 Easy Steps' numbered step badges
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/homepage/tile-03-y03660.png
  claim: The 1-2-3 step markers are consistent as a set but rendered in a dated glossy-orb style with heavy bevels and drop shadows rather than a current flat or line treatment.
  visible_tells:
  - three green ring medallions with embossed numerals, gloss highlights and soft drop shadows
  - Web-2.0 'shiny button' aesthetic identical across all three so consistency holds even as the style reads old
  confidence: high
- id: iconography_04
  family: iconography_illustration
  polarity: poor
  page_or_region: services page — Sermorelin pathway diagram thumbnail ('Does Sermorelin Work?')
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/services/tile-05-y06100.png
  claim: The biological pathway diagram beside 'Does Sermorelin Work?' is a low-resolution clip-art schematic with tiny illegible labels, not a crafted custom diagram.
  visible_tells:
  - cramped 'Hypothalamus / Pituitary' boxes and arrows with pixelated, near-unreadable text
  - cartoon brain and liver shapes in clashing flat colors crammed into a small thumbnail
  confidence: high
- id: iconography_05
  family: iconography_illustration
  polarity: poor
  page_or_region: testosterone page — aging-progression figure row
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/testosterone/tile-02-y02440.png
  claim: The 'aging male' progression is a stock photo-composite of cut-out figures standing on a reflective floor, used in place of any custom illustration to carry the decline-with-age idea.
  visible_tells:
  - row of photographic male figures from toddler to elderly with mirror-floor reflections
  - photo cut-outs rather than a drawn or iconographic treatment, reading as a purchased stock montage
  confidence: high
- id: iconography_06
  family: iconography_illustration
  polarity: mixed
  page_or_region: services & testosterone pages — recurring 3D vial product renders on Rx pads
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/services/tile-03-y03660.png
  claim: The HGH and testosterone vial renders are competent glossy 3D stock product images but are generic library assets rather than renders of any actual Kingsberg product.
  visible_tells:
  - photorealistic blue-capped 'HGH' vial with a syringe laid across a generic 'PRESCRIPTION' pad
  - same staged vial-on-Rx-pad composition reused for testosterone, signaling library stock
  confidence: medium
  contrast_with: store/kingsbergmedical-com/captures/2026-06-09/tiles/testosterone/tile-03-y03660.png
- id: iconography_07
  family: iconography_illustration
  polarity: poor
  page_or_region: homepage / global — Kingsberg Medical logo mark in header
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/homepage/tile-00-y00000.png
  claim: The brand mark is a small generic green leaf/sprout glyph that carries no medical or hormone-specific meaning and shows little custom craft.
  visible_tells:
  - tiny green leaf-on-stem icon tucked left of the 'KINGSBERG MEDICAL' wordmark
  - clip-art-grade simplicity with no distinguishing detail at header size
  confidence: medium
- id: iconography_08
  family: iconography_illustration
  polarity: poor
  page_or_region: homepage — 'Get Started' three-up service cards
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/homepage/tile-01-y01220.png
  claim: The three service entries are illustrated only with cut-out stock photos of clinicians, with no icon system to encode the offerings — there is no custom iconography layer at all.
  visible_tells:
  - each card uses a background-removed stock photo (woman in lab coat, man in lab coat, masked tech drawing blood) as its only graphic
  - absence of any unifying line- or glyph-icon set across the trio
  confidence: high
- id: iconography_09
  family: iconography_illustration
  polarity: mixed
  page_or_region: services page — 'READ MORE' arrow glyphs in article list
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/services/tile-05-y06100.png
  claim: The repeated green 'READ MORE ->' arrow glyph is consistent and legible across every list item, a small functional element handled uniformly.
  visible_tells:
  - identical green right-pointing arrow follows each 'READ MORE' label down the article list
  - same color and weight reused on all entries
  confidence: medium
- id: iconography_10
  family: iconography_illustration
  polarity: poor
  page_or_region: services page — 'Sermorelin vs Ipamorelin' / 'Doctors Who Treat...' article thumbnails
  tile_path: store/kingsbergmedical-com/captures/2026-06-09/tiles/services/tile-06-y06384.png
  claim: Article-list thumbnails are generic stock photos (a blue auto-injector pen, a smiling clinician, a seated doctor) with no consistent framing, treatment, or icon overlay tying them to the brand.
  visible_tells:
  - each entry fronted by a different stock photo crop — blue auto-injector pen, white-coat clinician, seated doctor
  - no shared crop ratio or treatment across the thumbnails
  confidence: medium
```

## Provenance

Tiles read: homepage (6) + services (7) + testosterone (6) from `captures/2026-06-09/tiles/` — all 19 active, no exclusions, no Tier-B re-render (the capture was clean). Mined blind + judged per [`/visual-evidence`](../../skills/visual-evidence/SKILL.md): four family miners saw only the tiles (no dossier, no web); the judge pruned 13 of 59 raw cards. Snapshot caveat: reflects the 2026-06-09 capture; the live site changes.
