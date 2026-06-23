# GPT-5.5 visual-quality example mining findings

Date: 2026-06-13

## Bottom Line

The example-mining approach worked better than another whole-site rating pass.
GPT-5.5 produced inspectable, contrastive visual evidence across typography,
layout, iconography, and brand/color/imagery. The strongest value was not "better
scores"; it was retrieving specific visual tells that can become a calibration
library.

The run also proved a hard constraint: screenshot QA must happen before fanout.
The first run was aborted for contaminated evidence, and a second audit caught a
Mills newsletter/cookie overlay after agents had started. Once recaptured and
rebuilt, the final outputs were clean.

## Run Shape

- Cohort: 13 sites.
- Final evidence: 50 pages, 310 native-resolution tiles under `tiles-clean/`.
- Agents: 4 GPT-5.5 agents, one per evidence family.
- Output: 48 evidence cards, 12 per family.
- Validation: all cited tile paths exist under `tiles-clean/`; no stale modal/cookie
  claims remain in final agent outputs.

## Screenshot Health

- Function Health homepage was excluded. Multiple Firecrawl attempts rendered the
  real hero media as a flat grey block, including long wait, scroll/wait actions,
  enhanced proxy, and mobile/UA attempts. Function pricing/scans stayed in scope.
  A later follow-up found a patched workaround for the homepage hero by injecting
  Function's own poster asset when Firecrawl hides the WebGL canvas; see
  `FIRECRAWL-WORKAROUND.md`. It was not used in this final evidence set.
- Belmar was recaptured with CookieYes rejected.
- Amble was recaptured with Transcend dismissed.
- Pepti was recaptured with custom cookie UI removed; JS cleanup was more reliable
  than click-only actions.
- Mills was recaptured after the audit found a newsletter modal plus consent box on
  the old homepage.

## Strong Examples The Agents Found

### Function Health

Function remained the clearest high-control reference even without the homepage.

- Typography: pricing/scans use restrained serif/sans contrast, rust italic emphasis,
  and clear size/role steps.
- Iconography/illustration: scans page uses a coherent diagnostic dot-and-line
  vocabulary across map, benefit marks, and body-contour overlays.
- Color/imagery: black, cream, and rust palette feels owned; clinical imagery stays
  warm and restrained.
- Layout: pricing card and comparison table show disciplined container geometry.

Representative cards:

- `functionhealth-com/pricing/tile-00-y00000.png`
- `functionhealth-com/scans/tile-00-y00000.png`
- `functionhealth-com/scans/tile-04-y04880.png`

### Ro

Ro was consistently strong, especially where product photography and interaction
modules carry the page.

- Imagery: real product close-ups and specific editorial crops beat generic condition
  imagery.
- Iconography: simple black line icons stay consistent across benefit lists.
- Layout: the timeline-to-treatment panel is a controlled overlap of full-bleed image,
  central panel, and step accordion.

Representative cards:

- `ro-co/homepage/tile-02-y02440.png`
- `ro-co/weight-loss/tile-02-y02440.png`
- `ro-co/weight-loss/tile-04-y04880.png`

### Nurx

Nurx supplied strong examples of warm consumer-health consistency.

- Color/imagery: yellow/peach surfaces and warm editorial crops cohere across the
  homepage.
- Typography: weight-management page maintains distinct label, headline, body, bullet,
  and CTA roles.
- Layout: service cards repeat image frame, divider, eligibility row, and CTA placement
  despite varying copy lengths.

Representative cards:

- `nurx-com/homepage/tile-00-y00000.png`
- `nurx-com/weight_management/tile-00-y00000.png`
- `nurx-com/our_services/tile-01-y01220.png`

### Hallandale

Hallandale was not as expressive as Function/Ro/Nurx, but it produced strong examples
of plain, controlled execution.

- Color/imagery: hero uses a real pharmacy bottle as the primary brand image.
- Typography: hero hierarchy is simple and legible.
- Layout: product grid and filter rail maintain a predictable scan path.

Representative cards:

- `hallandalerx-com/homepage/tile-00-y00000.png`
- `hallandalerx-com/products/tile-01-y01220.png`

## Mixed Examples

### Pepti

Pepti is memorable but uneven.

- Strong: app-like process graphics share mint surfaces, rounded progress elements,
  order-tracking panels, and status marks.
- Mixed: product/treatment cards get dense and repetitive; tiny vial thumbnails make
  different treatment goals visually interchangeable.
- Mixed: lime/fashion art direction is distinctive, but product thumbnails and process
  graphics can feel like separate systems.

Representative cards:

- `hellopepti-com/homepage/tile-03-y03660.png`
- `hellopepti-com/homepage/tile-11-y13420.png`
- `hellopepti-com/homepage/tile-02-y02440.png`

### Amble

Amble is attractive but not fully stable as a brand system.

- Mixed: saturated color panels are appealing, but the system shifts from white product
  cards to orange/purple/blue campaign panels.
- Mixed: pictograms add atmosphere to results panels but are not precise functional
  iconography.

Representative cards:

- `joinamble-com/homepage/tile-02-y02440.png`
- `joinamble-com/glp1/tile-01-y01220.png`

### Geviti

Geviti shows ambition but weakens at the system layer.

- Strong/mixed: expressive italic display type recurs across hero and explainer
  sections.
- Mixed: data-product mockups are polished, but source icons drift across clip-art
  styles.
- Mixed: grid discipline is real, yet decorative assets do not fully systematize.

Representative cards:

- `gogeviti-com/homepage/tile-00-y00000.png`
- `gogeviti-com/blueprint/tile-01-y01220.png`
- `gogeviti-com/homepage/tile-01-y01220.png`

### Belmar

Belmar is a useful "coherent template" calibration case.

- Mixed/poor: green healthcare palette, angular photo masks, and outline icons are
  competent but generic.
- Mixed: account form has solid field alignment but reads as an undifferentiated
  administrative slab.

Representative cards:

- `belmarpharmasolutions-com/homepage/tile-00-y00000.png`
- `belmarpharmasolutions-com/homepage/tile-01-y01220.png`
- `belmarpharmasolutions-com/account-form/tile-01-y01220.png`

## Poor Examples

### Jinfiniti

Jinfiniti was the clearest poor/mismatched craft source.

- Color/imagery: science chart, hexagon badge, clip-art icons, and promo bars do not
  share a mature system.
- Iconography: test-kit photo, chemical diagram, play button, check icons, and sticky
  commerce/nav treatments compete as unrelated devices.
- Layout: sticky promo/nav interrupts result-card sections mid-scroll.
- Product imagery: catalog cards mix jars, kit boxes, ingredient props, and bundles
  without one product-art direction.

Representative cards:

- `jinfiniti-com/homepage/tile-01-y01220.png`
- `jinfiniti-com/intracellular_nad_test/tile-02-y02440.png`
- `jinfiniti-com/intracellular_nad_test/tile-03-y03660.png`
- `jinfiniti-com/shop/tile-01-y01220.png`

### Kingsberg

Kingsberg repeatedly surfaced dated and uncontrolled execution.

- Imagery: homepage hero reads as a stock composite rather than a controlled scene.
- Typography: all-caps navigation, serif overlay, large green CTA, and centered mission
  text compete.
- Layout: services page relies on old page furniture: main content, sidebar ad, stock
  image, quote box, and headings with different alignment logic.

Representative cards:

- `kingsbergmedical-com/homepage/tile-00-y00000.png`
- `kingsbergmedical-com/services/tile-02-y02440.png`

### Anazao

Anazao was useful for absent-system evidence.

- Typography: oversized cyan headings and centered paragraph blocks feel blunt.
- Iconography: solution areas are identical teal buttons rather than a real pictogram
  system.

Representative cards:

- `anazaohealth-com/homepage/tile-00-y00000.png`
- `anazaohealth-com/homepage/tile-01-y01220.png`

### Infusive

Infusive is a good "designed-looking but generic" trap.

- Color/imagery: glossy purple gradients, magenta pills, abstract wave, laptop mockup,
  and testimonial card read as generic B2B SaaS.
- Typography: many headline/CTA treatments compete in the hero.
- Layout: tabbed feature section layers navigation, photo, text, gradients, and CTA
  into one crowded band.

Representative cards:

- `goinfusive-com/homepage/tile-00-y00000.png`
- `goinfusive-com/platform/tile-02-y02440.png`

### Mills

After recapture, Mills remains a valid low/mid example without needing overlays as
evidence.

- Iconography: service areas rely on darkened stock-photo tiles and decorative marks
  instead of a service icon system.
- Layout: weight-management page stacks text-heavy bands, centered cards, bullets,
  numbered lists, and image blocks without a strong repeated component pattern.
- Typography: clean homepage is readable, but centered copy and decorative all-caps
  headings flatten hierarchy.

Representative cards:

- `millspharmacy-com/homepage/tile-00-y00000.png`
- `millspharmacy-com/homepage/tile-01-y01220.png`
- `millspharmacy-com/weight_management/tile-01-y01220.png`

## Rubric Pieces That Helped Most

- Evidence cards beat whole-site tiers for this phase. They force visible tells and
  produce reusable calibration examples.
- Contrast pairs were high leverage. They made "strong" and "poor" less vibes-based.
- "Generic is common" worked well as a calibration rule. It helped distinguish Belmar
  and Infusive from genuinely strong systems.
- "Distinctiveness is not maximalism" mattered for Pepti/Geviti: both have visual
  ambition, but ambition did not automatically become strong craft.
- The default-down rule belongs in the protocol, but it needs enforcement through
  synthesis; agents still occasionally write generous mixed claims unless contrasted.

## Harness Lessons

1. Add screenshot-health QA as a required first phase.
   Build a full overview contact sheet, inspect it, and record excluded/recaptured pages
   before any agent fanout.

2. Split capture status from design judgment.
   A page with a modal, broken hero, or cookie banner is not a poor design example; it is
   unusable evidence until cleaned or excluded.

3. Keep agents mining evidence, not ranking sites.
   The outputs were most useful when agents produced small, falsifiable cards. Whole-site
   ratings can happen later from the card library.

4. Add a final invalidation scan.
   Search agent outputs for overlay/modal/cookie language and stale paths before synthesis.

5. Consider a second-pass judge only after evidence cards exist.
   A judge should prune/merge cards and label calibration value, not rescore every site
   from scratch.

## Verdict

GPT-5.5 looks promising for visual-quality calibration when the task is framed as
evidence retrieval. The model brought back specific, inspectable examples and generally
respected the "generic is common" spine. The main failure mode was not model judgment; it
was evidence hygiene. The next version should formalize screenshot QA and then reuse this
card-mining structure.
