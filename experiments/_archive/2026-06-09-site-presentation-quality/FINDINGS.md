# Site presentation quality calibration

Date: 2026-06-09

## Objective

Test whether agents can rate observable marketing-site presentation quality from existing Web Research artifacts, then compare blind ratings against Brian's Notion `Web design rating` field.

This is useful because downstream competitive work often asks whether a company looks "legit" or "formidable", but the engine should not score legitimacy or threat. The observable engine-side signal is narrower: whether the marketing site presentation looks polished, competent, basic, weak, broken, or impossible to assess from the capture.

## Scope

Warm, local-only sample:

- Function Health - `functionhealth.com` - `store/functionhealth-com`
- Hone Health - `honehealth.com` - `store/honehealth-com`
- Ro - `ro.co` - `store/ro-co`
- Nurx - `nurx.com` - `store/nurx-com`
- Geviti - `gogeviti.com` - `store/gogeviti-com`
- Amble - `joinamble.com` - `store/joinamble-com`
- Hallandale - `hallandalerx.com` - `store/hallandalerx-com`
- Belmar Pharma - `belmarpharmasolutions.com` - `store/belmarpharmasolutions-com`
- Pepti - `hellopepti.com` - `store/hellopepti-com`

No Firecrawl credits were spent. No schema files, frontmatter fields, or company profiles were changed.

## Non-scope

This does not score company legitimacy, competitive threat, funding, headcount, traffic, SEO, press reputation, truth of claims, clinical/regulatory quality, price transparency, CMS/framework quality, or market strength.

## Method

1. Built blind packets in `packets/` from cached artifacts only: homepage screenshot path, screenshot size, source URL/status/title/description, captured page inventory, and neutral payload hints.
2. Excluded Brian's Notion rating from packets.
3. Avoided existing `profile.md` visual prose because prior model text could bias the read.
4. Spawned three evaluator agents after packet creation:
   - Evaluator A: Function Health, Hone Health, Ro.
   - Evaluator B: Nurx, Geviti, Amble.
   - Evaluator C: Hallandale, Belmar Pharma, Pepti.
5. After all blind ratings were complete, fetched the Notion `Organizations` records and read `Web design rating`.

Notion note: the advertised SQL data-source query tool was unavailable, so ratings were fetched via targeted database search plus page fetch. The fetched source was `collection://d0beabe1-d50f-4a15-9349-c6fab743dac8`.

## Blind Ratings

| Company | Blind `site_presentation_quality` | Confidence | Evidence cues |
|---|---:|---:|---|
| Function Health | excellent | high | Cohesive warm brand system; refined serif/sans hierarchy; polished cards, pricing, comparison, footer; integrated press, stats, videos, clinician grid; clear lab-testing offer. |
| Hone Health | strong | high | Distinct yellow/black identity; clear process narrative; strong app/product mockups; legible membership/FAQ; crowded nav/announcement areas and aggressive yellow blocks reduce refinement. |
| Ro | strong | high | Clear product/category navigation; sharp lifestyle and product photography; consistent treatment cards/carousels; clinician/member/badge trust surfaces; polished but less distinctive. |
| Nurx | strong | high | Cohesive orange/cream/black system; clear service hierarchy; polished photography and clinician/trust sections; consistent cards, CTAs, accordions, footer; dense legal block is visually heavy. |
| Geviti | excellent | high | Distinctive cloud/ocean system; refined type hierarchy; consistent cards, stats, testimonials, pricing, FAQ, footer; art-directed social-proof strips; clear repeated CTAs. |
| Amble | solid | high | Product categories and treatment flow are clear; color-blocked sections and product/person imagery work; cards and CTAs mostly polished; repeated privacy popovers and generic metadata hurt cleanliness. |
| Hallandale | strong | high | Distinct product-in-hand hero; crisp typography; coherent blue/white system; clear category/product presentation; integrated trust cues; gray media block and clipped marquee reduce polish. |
| Belmar Pharma | solid | high | Clear pharmacy positioning and audience CTAs; consistent green system; credentials, cards, tags, testimonial, footer visible; imagery feels generic; cookie banner interrupts upper layout. |
| Pepti | excellent | high | Distinctive long-form visual system; strong typography and custom palette; app/product mockups, calculators, pricing, FAQs, journal, footer; clear peptide therapy offer; some placeholder-looking sections. |

## Comparison Against Brian's Ratings

Approximate bucket mapping used only for this comparison:

- `excellent` ~= 9-10
- `strong` ~= 7-8
- `solid` ~= 5-6
- `basic` ~= 3-4
- `weak` ~= 1-2

| Company | Blind rating | Brian Notion rating | Calibration read |
|---|---:|---:|---|
| Function Health | excellent | 10 | Agree. Blind read and Brian both put it at the top. |
| Hone Health | strong | 8 | Agree. Professional and distinctive, with some conversion-density friction. |
| Ro | strong | 8 | Agree. Polished, clear, and high-production, but not "excellent" distinctive. |
| Nurx | strong | 7 | Close/agrees. Blind evaluator was slightly generous, but still within the strong band. |
| Geviti | excellent | 7 | Blind high. Evaluator over-weighted distinctive art direction and section rhythm. |
| Amble | solid | 6 | Agree. Clean and usable, with capture/presentation friction. |
| Hallandale | strong | 8 | Agree. Modern B2B pharmacy presentation, despite visible media/marquee friction. |
| Belmar Pharma | solid | 4 | Blind high. Evaluator over-credited coherent B2B structure, credentials, and trust badges while under-penalizing generic/dated execution. |
| Pepti | excellent | 6 | Blind high, largest miss. Evaluator over-rewarded ambition, long-form density, and distinctive visual language despite placeholder-like/low-contrast sections. |

Result: 6/9 were bucket matches. Two misses were adjacent-bucket high reads. Pepti was the one large false positive.

## What Worked

- Full-page screenshots are enough to separate obvious top-tier presentation from merely usable pages.
- Concrete evidence cues were easy for agents to produce: typography hierarchy, component polish, trust-surface presentation, card/CTA consistency, image quality, section pacing, and information clarity.
- The scale is useful when anchored to observable presentation, not company strength.
- Capture artifacts were sufficient for all nine warm companies; no `unknown` cases in this sample.

## Failure Modes

- Agents over-rewarded distinctive art direction. Geviti and especially Pepti show that unusual visual language can look "excellent" even when Brian rates the execution lower.
- Agents under-penalized placeholder-like sections, low-contrast pale blocks, and "designed but unfinished" long pages.
- Agents over-credited B2B trust surfaces. Belmar's credentials, testimonials, and footer made the page feel credible, but the presentation still reads closer to basic in Brian's calibration.
- Consent/cookie overlays and empty media blocks need explicit handling: they are not automatically `broken`, but they should lower confidence or cap the rating when they materially obscure the page.

## Scale Adjustment

Keep the labels, but tighten `excellent`:

- `excellent` should require both distinctiveness and execution discipline: clean render, no major placeholder/low-contrast sections, strong asset quality, and polished components across the page.
- `strong` can cover professional, distinctive, or modern sites with minor friction.
- `solid` should be the default for coherent but conventional sites.
- `basic` should explicitly include generic stock-template execution, dated components, or trust badges presented in a cluttered/low-polish way.

Do not add weighting. A short anchor table with examples is enough.

## Recommendation

Keep this as a prose convention for now. Do not add a schema/frontmatter field yet.

The signal is useful, but the false positives show the rubric needs one more calibration pass before becoming a durable workflow. The next smallest useful step is to add a short evaluator prompt/convention to the capture workflow or a tiny offline `design-scan` helper that only assembles a cached-artifact report. It should not write `profile.md` or create a derived database.

If repeated runs keep matching Brian on bucket-level ratings, then consider a later schema convention. Not before.

## Limitations

- Single evaluator per company, not multiple independent ratings per company.
- Mostly homepage full-page screenshots; key-page screenshots were available in packets but not systematically scored.
- Desktop screenshots only; no mobile/responsive or interaction assessment.
- Brian's Notion ratings are subjective numeric values, not a formal rubric, so the bucket mapping is approximate.
