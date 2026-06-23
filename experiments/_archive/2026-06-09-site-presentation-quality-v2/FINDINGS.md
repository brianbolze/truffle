# Site presentation quality v2 calibration

Date: 2026-06-09

## Objective

Run a second small calibration pass for `site_presentation_quality`, testing whether richer blind packets and explicit `excellent` cap rules reduce false positives from the first run.

This remains calibration work. No Firecrawl credits were spent. No schema files, frontmatter fields, or company profiles were edited.

## Scope

Same warm sample as v1:

- Function Health - `functionhealth.com` - `store/functionhealth-com`
- Hone Health - `honehealth.com` - `store/honehealth-com`
- Ro - `ro.co` - `store/ro-co`
- Nurx - `nurx.com` - `store/nurx-com`
- Geviti - `gogeviti.com` - `store/gogeviti-com`
- Amble - `joinamble.com` - `store/joinamble-com`
- Hallandale - `hallandalerx.com` - `store/hallandalerx-com`
- Belmar Pharma - `belmarpharmasolutions.com` - `store/belmarpharmasolutions-com`
- Pepti - `hellopepti.com` - `store/hellopepti-com`

## Method

1. Read the engine rules, schema guidance, research-company capture docs, and v1 calibration findings.
2. Built v2 blind packets under `packets/` from cached local artifacts only.
3. Packet contents included screenshots, homepage/key-page metadata, OG/canonical/status/favicon hints, rawHtml framework hints, route/page-structure hints, observed media cues, design-system cues, IA clarity, cross-page consistency, and render/capture caveats.
4. Excluded Brian's Notion ratings and existing `profile.md` visual prose from the blind packets.
5. Ran three blind evaluator agents:
   - Evaluator A: Function Health, Hone Health, Ro.
   - Evaluator B: Nurx, Geviti, Amble.
   - Evaluator C: Hallandale, Belmar Pharma, Pepti.
6. After blind scoring was complete, fetched Brian's Notion `Web design rating` values from `Organizations` / `collection://d0beabe1-d50f-4a15-9349-c6fab743dac8`.

## Blind Ratings

| Company | Blind v2 `site_presentation_quality` | Confidence | Cap-rule read |
|---|---:|---:|---|
| Function Health | excellent | high | Excellent allowed: distinctive and execution-disciplined. |
| Hone Health | strong | high | Capped below excellent for busy ticker/saturated treatment and uneven capture/presentation. |
| Ro | strong | high | Capped below excellent for less distinctive execution plus overlay/minor layout issue. |
| Nurx | strong | high | Capped below excellent: disciplined but more professional than distinctive. |
| Geviti | strong | high | Capped below excellent for "Coming Soon," pale/low-contrast sections, and templated/stock-like imagery. |
| Amble | strong | high | Capped below excellent for repeated privacy overlays and repeated/template-like section patterns. |
| Hallandale | strong | high | Capped below excellent for blank gray media block and clipped marquee. |
| Belmar Pharma | solid | high | Not an excellent candidate: conventional/template-like with generic stock and repeated cookie banner. |
| Pepti | strong | medium | Capped below excellent for placeholder-looking gray blocks, low contrast, sticky elements, and uneven page depth. |

Raw evaluator outputs: `agent-outputs/`.

## Comparison Against Brian's Ratings

Approximate bucket mapping:

- `excellent` ~= 9-10
- `strong` ~= 7-8
- `solid` ~= 5-6
- `basic` ~= 3-4
- `weak` ~= 1-2

| Company | Blind v2 rating | Brian Notion rating | Calibration read |
|---|---:|---:|---|
| Function Health | excellent | 10 | Match. |
| Hone Health | strong | 8 | Match. |
| Ro | strong | 8 | Match. |
| Nurx | strong | 7 | Match. |
| Geviti | strong | 7 | Match; v2 fixed v1's `excellent` false positive. |
| Amble | strong | 6 | Blind high by one bucket; new/remaining false positive. |
| Hallandale | strong | 8 | Match. |
| Belmar Pharma | solid | 4 | Blind high by one bucket; still over-credits coherent B2B structure. |
| Pepti | strong | 6 | Blind high by one bucket; improved from v1's major `excellent` miss. |

Result: 6/9 exact bucket matches.

V2 did not improve the headline match count, but it did reduce severity. There were no `excellent` false positives. Pepti moved from `excellent` to `strong`, and Geviti moved from `excellent` to `strong`.

## Answers To Calibration Questions

1. **Did v2 reduce false positives?** Yes for `excellent` false positives; no for total bucket misses. Geviti is fixed, Pepti is less wrong, Belmar remains high, and Amble became an adjacent high read.
2. **Did cap rules demote Pepti, Geviti, Belmar, or others?** Yes. Pepti and Geviti were demoted from v1 `excellent` to v2 `strong`. Hallandale was also capped below excellent. Belmar stayed `solid`; the checklist prevented `strong` but did not reach Brian's `basic` bucket.
3. **Most reliable evidence families:** render/capture integrity, media asset sophistication, cross-page consistency, design-system consistency, and IA clarity.
4. **Weak proxies:** tech stack, metadata maturity, route maturity by itself, and trust-surface presence without visual polish.
5. **Tech stack:** mostly secondary and sometimes misleading. It should remain a hint, not a scoring input.
6. **Metadata maturity:** weak correlation. Hallandale rated 8 despite weak homepage metadata; Belmar had decent metadata but rated 4.
7. **Professional media assets vs framework:** professional media assets correlated better than framework.
8. **Recommendation:** add an offline `design-scan` packet helper, but keep `site_presentation_quality` as prose convention only. Do not add a schema/frontmatter field yet.

## Recommendation

Add a tiny offline `design-scan` helper that assembles cached packets like this run:

- screenshots and dimensions
- metadata/OG/canonical/status/favicon
- rawHtml framework hints
- route/page-structure hints
- observed render caveat checklist slots
- space for evaluator prose

Do not create a weighted model, derived DB, frontmatter field, or schema convention yet.

The signal is useful enough to standardize packet assembly, but not stable enough to promote. The remaining problem is the `strong`/`solid`/`basic` boundary, especially for coherent but generic B2B surfaces and ambitious pages with unfinished sections.

## Limitations

- Single evaluator per company, not independent multiple ratings.
- Desktop screenshots only; no mobile/responsive or interaction assessment.
- Observed cue blocks were added by the lead agent after screenshot inspection, so they improved packet completeness but may steer evaluator attention.
- Brian's numeric rating is subjective, and the bucket mapping is approximate.
- Notion values were fetched with search + page fetch because only Notion fetch/search tools were exposed in this session.
