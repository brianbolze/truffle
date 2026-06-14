---
schema_version: "1.0"
domain: parlance.cc
captured_at: 2026-06-14
source_capture: 2026-06-10
qa_status: clean
---

## Visual & brand impression

Restrained editorial minimalism with a real art-direction spine. The site relies on oversized black sans type, pale grey canvas, and disciplined green/teal accents rather than decorative chrome [typography_01][color_01]. The best moments are spacious and confident: the monochrome textile hero, the three-up offering row, and the dark footer/CTA system feel controlled [layout_01][layout_02][color_02][layout_06]. Its weak edge is scanability inside long-form pages, where wide empty rails leave dense article copy doing too much work on the right [layout_05][typography_04]. The image language is deliberately varied - macro texture, rendered objects, cinematic article cards, and project photography - coherent enough to feel curated, not templated [color_03][iconography_02]. Sparse, sharp, and founder-studio coded.

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: Homepage hero headline
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-00-y00000.png
  claim: The homepage opens with a very large black sans-serif headline on an empty pale field, creating a clear dominant type level before any image appears.
  visible_tells:
  - headline spans three long lines in the upper-left quadrant
  - the nav and wordmark stay much smaller, leaving the headline unmistakably primary
  - no image or texture sits behind the headline text
  confidence: high
- id: typography_02
  family: typography_hierarchy
  polarity: strong
  page_or_region: Homepage intro statement below hero image
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-01-y01220.png
  claim: The intro block keeps hierarchy simple with one large sentence tier and selective green emphasis on key words, avoiding extra subheads or decorative type treatments.
  visible_tells:
  - "Parlance" and "Creative Capital" are the only green words in the statement
  - the statement uses one consistent large sans size across four lines
  - the small grey prompt line below is clearly secondary
  confidence: high
- id: typography_03
  family: typography_hierarchy
  polarity: mixed
  page_or_region: Homepage organizations-supported list
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-06-y07320.png
  claim: The organizations-supported section sets up a crisp left label and large right-side list, but the list grows into a tall undifferentiated column with no grouping or weight changes.
  visible_tells:
  - "Organizations Supported" sits as a small two-line label at left
  - company names are stacked in one large uniform sans column
  - every name has the same size and weight from Constellation through Since Tomorrow
  confidence: high
- id: typography_04
  family: typography_hierarchy
  polarity: mixed
  page_or_region: Article template body copy
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/sprints/tile-00-y00000.png
  claim: The article template gives the page title, byline rail, hero image, bold article lead, body paragraphs, and bold subheads distinct roles, but the main column becomes dense once the long text begins.
  visible_tells:
  - "Sprints" is a large left-rail page title separated from the article body
  - bold section leads and paragraph text repeat down the right column
  - several consecutive paragraphs run at similar size and line length below the hero image
  confidence: medium
- id: typography_05
  family: typography_hierarchy
  polarity: strong
  page_or_region: Homepage closing CTA band
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-07-y08275.png
  claim: The closing green band uses centered white type at a single oversized scale, making the CTA statement legible and visually separate from the black footer below.
  visible_tells:
  - white statement sits centered on a flat deep-green band
  - the short teal contact pill sits below as a smaller action tier
  - the black footer begins only after the green band ends
  confidence: high
- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: Homepage hero composition
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-00-y00000.png
  claim: The hero composes a quiet top nav, oversized left-aligned headline, and full-width rounded image panel with generous whitespace and clean edge alignment.
  visible_tells:
  - wordmark/nav occupy a thin top bar while the headline begins far below
  - the image panel starts under the headline and spans nearly the full viewport width
  - rounded image corners align cleanly with the page margins
  confidence: high
- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: Homepage offering card row
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-01-y01220.png
  claim: The offering section is a disciplined three-column system: equal image cards, thin dividers, uppercase titles, and body copy aligned to matching baselines.
  visible_tells:
  - three image cards share the same height, corner radius, and gutters
  - each card repeats image, divider rule, uppercase title, then paragraph
  - title and body baselines align across the row
  confidence: high
- id: layout_03
  family: layout_composition_components
  polarity: mixed
  page_or_region: Homepage focus accordion
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-02-y02440.png
  claim: The focus accordion is clean and airy, but its right-heavy placement leaves the large left half of the section mostly empty after the "Focus" label.
  visible_tells:
  - accordion rows occupy the right column only
  - the left side contains only the small "Focus" heading and a broad blank field
  - each row uses a thin rule and small plus glyph at the far right
  confidence: medium
- id: layout_04
  family: layout_composition_components
  polarity: strong
  page_or_region: Homepage projects grid
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-04-y04880.png
  claim: The projects section shifts from a two-up lead row to a three-up row while preserving even gutters, matching card widths within each row, and consistent label placement below images.
  visible_tells:
  - first row has two wide cards of equal width
  - second row has three equal cards with the same vertical spacing
  - project names and category metadata sit in the same position under each card
  confidence: high
- id: layout_05
  family: layout_composition_components
  polarity: mixed
  page_or_region: Article page template
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/fte/tile-00-y00000.png
  claim: The article template creates an elegant left metadata rail and right content column, but the central page is so sparse that long body copy carries most of the visual load.
  visible_tells:
  - page title, author photo, author name, and date sit isolated in the left rail
  - the right column holds the hero image and all body content
  - large blank space remains between the two columns and below the left rail
  confidence: high
- id: layout_06
  family: layout_composition_components
  polarity: strong
  page_or_region: Global footer and CTA transition
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-07-y08275.png
  claim: The footer resolves into a structured black band with wordmark, social pills, location/time blocks, link columns, and a small email action all placed on stable horizontal rows.
  visible_tells:
  - wordmark and social pills align across the footer top
  - Menlo Park and Stockholm time blocks sit in a centered column
  - Work, Info, and Contact links form a separate right column
  confidence: high
- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: Site-wide neutral palette and green accent
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-01-y01220.png
  claim: The site uses a restrained palette of pale grey, black, white, and deep green, with green reserved for emphasis words and primary action buttons.
  visible_tells:
  - pale grey page background and black headline text dominate the tile
  - green appears only in "Parlance", "Creative Capital", and the Book Time pill
  - offering images carry muted warm/neutral tones rather than competing UI colors
  confidence: high
  contrast_with: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-07-y08275.png
- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: Homepage hero image
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-00-y00000.png
  claim: The monochrome textile macro creates a distinctive brand image, pairing organic tangled texture with a large white wordmark without needing additional color.
  visible_tells:
  - black-and-white yarn/fiber texture fills the hero image panel
  - white "Parlance" wordmark sits large over the texture
  - the monochrome image contrasts with the pale grey page field above it
  confidence: high
- id: color_03
  family: color_brand_imagery
  polarity: mixed
  page_or_region: Homepage notes and project imagery
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-03-y03660.png
  claim: The notes and project cards are clearly art-directed, but the image language swings from black architectural photography to dashboard closeups, fashion editorial scenes, and graphic color blocks in one viewport.
  visible_tells:
  - ".cc", "Sprints", and "fte" cards use dark photographic overlays with italic titles
  - Mentorship uses a pale architectural scene while FAQ uses a saturated green/orange graphic
  - the Genagraph card uses a cinematic street fashion image unlike the other cards
  confidence: high
- id: color_04
  family: color_brand_imagery
  polarity: strong
  page_or_region: Homepage CTA band and footer
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-07-y08275.png
  claim: The dark green CTA band, teal button, and black footer form a controlled dark-mode close that feels intentionally separated from the pale content sections above.
  visible_tells:
  - CTA area is a single uninterrupted deep-green rectangle
  - contact button uses a brighter teal accent on the green field
  - footer below switches to flat black with white text and pale social pills
  confidence: high
- id: iconography_01
  family: iconography_illustration
  polarity: strong
  page_or_region: Header mark and pill-button glyphs
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-00-y00000.png
  claim: The small circular logo mark and hollow-dot button glyphs establish a minimal icon language that stays thin, geometric, and understated.
  visible_tells:
  - wordmark is paired with a small circular line mark at the header left
  - Contact pill uses a tiny hollow circle before the label
  - icon strokes are black, thin, and visually quieter than the wordmark
  confidence: medium
  contrast_with: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-07-y08275.png
- id: iconography_02
  family: iconography_illustration
  polarity: strong
  page_or_region: Homepage offering image set
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-01-y01220.png
  claim: The offering cards use custom-looking dimensional object renders instead of generic glyph icons, giving the service categories a more tactile visual system.
  visible_tells:
  - copper tube and stone ring render for Category Creation
  - floating cylindrical objects and shadows for Narrative Clarity
  - wood-and-cream sculptural form for Leadership Without Limits
  confidence: high
- id: iconography_03
  family: iconography_illustration
  polarity: mixed
  page_or_region: Homepage focus accordion controls
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/homepage/tile-02-y02440.png
  claim: The accordion plus signs are consistent and unobtrusive, but their very pale grey stroke makes the affordance easy to miss inside the large quiet section.
  visible_tells:
  - each focus row ends with the same small plus glyph
  - plus signs are rendered in very light grey
  - row labels are darker and much more prominent than the controls
  confidence: medium
- id: iconography_04
  family: iconography_illustration
  polarity: mixed
  page_or_region: Article-card title overlays
  tile_path: store/parlance-cc/captures/2026-06-10/tiles/faq/tile-02-y02026.png
  claim: The article cards use italic serif title overlays as a graphic identity device, a distinctive alternative to iconography that works visually but varies heavily by card image.
  visible_tells:
  - "The Genagraph", "faq", and "fte" are all set in white italic serif over image cards
  - each title is placed directly on photography or a graphic image instead of in a separate label band
  - the overlay treatment repeats while the underlying imagery changes dramatically
  confidence: high
```

## Provenance

Tiles read: homepage (8) + creative_capital (2) + sprints (2) + fte (2) + faq (3) + scottwitt (2) from `captures/2026-06-10/tiles/` - all 19 active, no exclusions, no Tier-B re-render (the capture was clean). Run provenance: generated by Codex using GPT-5.5 on 2026-06-14 from the active tiles only; no profile, dossier, Notion, or live web was consulted. Snapshot caveat: reflects the 2026-06-10 capture; the live site changes.
