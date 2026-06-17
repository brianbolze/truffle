---
schema_version: "1.0"
domain: airtable.com
captured_at: 2026-06-17
source_capture: 2026-06-17
qa_status: recapture-used
---

## Visual & brand impression

Airtable now reads from clean pixels as a polished enterprise product system: restrained black-on-white hierarchy surrounds immediately visible product UI, not an empty hero [typography_01][layout_01]. The strongest surfaces use Airtable's color vocabulary to organize work stories: purple and map UI in the homepage hero, red/green/blue workflow panels below, and a pale-blue platform hero with 3D product blocks [color_01][color_02][iconography_01]. Pricing is deliberately conservative — crisp cards, one blue highlighted plan, and long comparison tables that trade clarity for density [layout_03][typography_03][color_03]. Marketplace is the most playful directory surface, with bright geometric framing and custom extension artwork [layout_05][iconography_02].

## Evidence cards

```yaml
- id: typography_01
  family: typography_hierarchy
  polarity: strong
  page_or_region: "homepage hero"
  tile_path: store/airtable-com/captures/2026-06-17/tiles/homepage/tile-00-y00000.png
  claim: "The homepage hero holds a clear three-level type hierarchy: large centered headline, smaller grey explanatory line, and compact CTA pair before the product visual starts."
  visible_tells:
    - "The two-line headline is the largest text in the viewport."
    - "The support copy is smaller, grey, and centered directly under the headline."
    - "Filled dark and outlined CTAs sit as a matched pair below the copy."
  confidence: high
- id: typography_02
  family: typography_hierarchy
  polarity: strong
  page_or_region: "platform hero"
  tile_path: store/airtable-com/captures/2026-06-17/tiles/platform/tile-00-y00000.png
  claim: "The platform hero uses strong left-weighted hierarchy: a stacked oversized headline, a blue supporting statement, then two same-width CTAs on a pale-blue field."
  visible_tells:
    - "Headline breaks into four large lines on the left."
    - "Supporting sentence below is smaller but saturated blue, creating a distinct secondary tier."
    - "Try it now and Book demo buttons align beneath the copy."
  confidence: high
- id: typography_03
  family: typography_hierarchy
  polarity: mixed
  page_or_region: "pricing comparison table"
  tile_path: store/airtable-com/captures/2026-06-17/tiles/pricing/tile-01-y01220.png
  claim: "The comparison table is readable but visually flat: section labels, row labels, checkmarks, and plan columns repeat over a long scan with modest hierarchy changes."
  visible_tells:
    - "Fundamentals, Visualizations, and AI labels step up only slightly from row labels."
    - "Checkmarks repeat across four sparse columns with few visual grouping devices."
    - "Small grey NEW badges sit at the same detail level as row text."
  confidence: medium
- id: layout_01
  family: layout_composition_components
  polarity: strong
  page_or_region: "homepage hero product staging"
  tile_path: store/airtable-com/captures/2026-06-17/tiles/homepage/tile-00-y00000.png
  claim: "The homepage now stages product immediately after the hero copy: a large rounded product canvas sits above the customer proof strip, anchoring the first viewport with concrete UI."
  visible_tells:
    - "A purple-backed product panel begins directly below the CTAs."
    - "The panel includes a prompt field, map UI, left product sidebar, and overlaid feasibility card."
    - "Customer logos sit below the product canvas rather than replacing it as the first concrete visual."
  confidence: high
- id: layout_02
  family: layout_composition_components
  polarity: strong
  page_or_region: "platform page section rhythm"
  tile_path: store/airtable-com/captures/2026-06-17/tiles/platform/tile-01-y01220.png
  claim: "The platform page uses a controlled alternating product-story rhythm: left copy with right UI, then left copy with right colored UI, then integration tiles."
  visible_tells:
    - "Omni section pairs a blue product screenshot on the left with headline and bullets on the right."
    - "Field Agents section reverses emphasis with copy left and orange product panel right."
    - "Integration pills form a compact strip beneath the shared-data section."
  confidence: high
- id: layout_03
  family: layout_composition_components
  polarity: strong
  page_or_region: "pricing plan cards"
  tile_path: store/airtable-com/captures/2026-06-17/tiles/pricing/tile-00-y00000.png
  claim: "The pricing page has a disciplined four-column card system with matching borders, internal spacing, CTA placement, and a single highlighted Team card."
  visible_tells:
    - "Four plan cards share equal width and aligned top edges."
    - "Each card places price, CTA, and feature list in the same vertical order."
    - "The Team card uses a blue top rail, blue border, pale-blue fill, and blue CTA without breaking the grid."
  confidence: high
- id: layout_04
  family: layout_composition_components
  polarity: mixed
  page_or_region: "pricing full comparison"
  tile_path: store/airtable-com/captures/2026-06-17/tiles/pricing/tile-02-y02440.png
  claim: "The full comparison area prioritizes exhaustive tabular coverage over scan comfort, leaving large white vertical spans and many repeated checkmark rows."
  visible_tells:
    - "Rows continue well beyond one viewport with the same four plan columns."
    - "Several columns contain isolated checkmarks surrounded by broad white space."
    - "Category headings break the table, but the row rhythm stays mostly unchanged."
  confidence: high
- id: layout_05
  family: layout_composition_components
  polarity: strong
  page_or_region: "marketplace directory"
  tile_path: store/airtable-com/captures/2026-06-17/tiles/marketplace/tile-00-y00000.png
  claim: "The marketplace root creates a clear directory structure: search hero, tab row, three large feature cards, then paired extension lists with repeated icon/title/description rows."
  visible_tells:
    - "Featured tab is underlined in blue beneath the hero."
    - "Three large cards form the top content row."
    - "Extension lists repeat small icon, bold title, and one-line description in two columns."
  confidence: high
- id: color_01
  family: color_brand_imagery
  polarity: strong
  page_or_region: "homepage product story panels"
  tile_path: store/airtable-com/captures/2026-06-17/tiles/homepage/tile-01-y01220.png
  claim: "The homepage uses color to separate product narratives, shifting from a saturated red app-building panel into green table UI and then blue Omni territory."
  visible_tells:
    - "Production apps panel uses a deep red field with translucent red UI planes."
    - "Competitor table below is framed by a bright green panel."
    - "The next section begins with a pale blue Omni panel and blue spinner mark."
  confidence: high
- id: color_02
  family: color_brand_imagery
  polarity: strong
  page_or_region: "platform hero"
  tile_path: store/airtable-com/captures/2026-06-17/tiles/platform/tile-00-y00000.png
  claim: "The platform hero commits to a pale-blue enterprise stage, using saturated blue only for the primary CTA and selected 3D product elements."
  visible_tells:
    - "Full hero background is a soft blue field."
    - "Primary CTA is the only saturated blue block on the left."
    - "Right-side product render uses blue cubes, glassy blue sphere, and pale blue shadows."
  confidence: high
- id: color_03
  family: color_brand_imagery
  polarity: mixed
  page_or_region: "pricing page"
  tile_path: store/airtable-com/captures/2026-06-17/tiles/pricing/tile-00-y00000.png
  claim: "Pricing is intentionally conservative, relying almost entirely on white cards, grey borders, black type, and one blue emphasis state."
  visible_tells:
    - "Most of the viewport is white, black, and grey."
    - "Blue appears mainly on the Team card top rail, border, fill tint, and CTA."
    - "No product screenshot or colorful brand illustration appears in the first pricing viewport."
  confidence: high
- id: color_04
  family: color_brand_imagery
  polarity: strong
  page_or_region: "marketplace hero and cards"
  tile_path: store/airtable-com/captures/2026-06-17/tiles/marketplace/tile-00-y00000.png
  claim: "The marketplace page uses Airtable's bright accent palette as a visible organizing layer, with yellow, red, teal, blue, and lavender shapes repeated across hero and feature cards."
  visible_tells:
    - "Hero contains cropped yellow, red, teal, blue, and peach geometric blocks."
    - "Featured cards use saturated blue, sky blue, and lavender fills."
    - "Extension icons below echo the same bright accent family."
  confidence: high
- id: iconography_01
  family: iconography_illustration
  polarity: strong
  page_or_region: "platform hero product render"
  tile_path: store/airtable-com/captures/2026-06-17/tiles/platform/tile-00-y00000.png
  claim: "The platform hero uses custom 3D product illustration rather than flat stock art, combining UI cards, cubes, a chart platform, and a glass sphere into one staged system."
  visible_tells:
    - "Central product card floats above layered platform tiles."
    - "Blue cubes and a glassy sphere sit around the UI card."
    - "Faint workflow cards and line connections extend behind the main render."
  confidence: high
- id: iconography_02
  family: iconography_illustration
  polarity: strong
  page_or_region: "marketplace featured cards"
  tile_path: store/airtable-com/captures/2026-06-17/tiles/marketplace/tile-00-y00000.png
  claim: "The marketplace feature cards use custom illustration in a consistent flat style for team, page-design, and scripting concepts."
  visible_tells:
    - "Marketing card shows illustrated people gathered around a screen."
    - "Page designer card uses a stylized pen and document."
    - "Scripting card uses simplified code-window and media-window motifs in the same visual language."
  confidence: high
- id: iconography_03
  family: iconography_illustration
  polarity: mixed
  page_or_region: "pricing icons"
  tile_path: store/airtable-com/captures/2026-06-17/tiles/pricing/tile-00-y00000.png
  claim: "Pricing iconography stays functional but generic compared with the richer product and marketplace visuals."
  visible_tells:
    - "Enterprise Scale uses a simple grey line building icon."
    - "Plan features rely on repeated checkmarks as the main icon system."
    - "The page has no custom product illustration in the card grid."
  confidence: high
  contrast_with: store/airtable-com/captures/2026-06-17/tiles/platform/tile-00-y00000.png
```

## Provenance

- **Tiles read:** `homepage`, `platform`, and `pricing` were Tier-B browser re-renders in `store/airtable-com/captures/2026-06-17/tiles/`; `marketplace` uses the cached Firecrawl root-page tiles because live Chrome redirected `/marketplace` to an individual extension detail page.
- **QA note:** the previous homepage cached screenshot was incomplete in the first viewport. Tier-B homepage loaded 53/54 images over an 8227px page and cleared the cookie banner with an explicit click on the visible close affordance. Platform and pricing were also rerendered cleanly. Marketplace cached root screenshot was retained because it better represents the directory page than the live redirected extension detail.
- **Tier-B:** used for homepage, platform, and pricing; no additional Firecrawl credits were spent.
- **Snapshot caveat:** visual evidence is a point-in-time read of the captured and rerendered screenshots from 2026-06-17; Airtable's rotating hero examples and AI messaging can change independently of the stored dossier.
