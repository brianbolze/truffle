# Market Read

> **Loop 2 correction (2026-06-20):** A 3-pass adversarial review (evidence verifier +
> consumer + developer, Sonnet) re-derived the five load-bearing tallies independently and
> returned **PASS-WITH-FIXES**. Three were overcounted beyond the read's own ±2–3 bar, all from
> the same root cause my run-019-style prose-grep hit again: a **positive/negated polarity
> error** — lines reading "LegitScript … **not shown / not observed**" were counted as
> *positive*. Corrected below: **LegitScript ~33/54 (~61%), not ~42/56 (~75%)**; **named
> clinicians ~38 shown / ~16 not-shown, not ~29/~25**; the C3 accreditation *positive examples*
> wrongly included 4 "not shown" brands (defymedical, brellohealth, maximustribe, ro-co); and
> **"struthealth 180-day money-back" was a ghost citation** (no such language in the pack) —
> removed. The **headline pattern is unchanged and was independently confirmed**: LegitScript is
> the plurality norm, pharmacy accreditation is the rare/unspent differentiator, named clinicians
> track business model. Numbers and exemplars updated; framing softened from "table stakes" to
> "majority norm."

## Question

Across the captured telehealth cohort, what trust/proof devices do brands surface on their
owned pages — clinician credentialing (board-certified, named medical directors), regulatory/
legal framing (LegitScript, FDA, licensed/accredited pharmacy), efficacy/outcome claims, and
commercial-trust devices (money-back guarantee, transparent cancellation) — how do they
cluster by `anchor_category`, and which are capturable owned-page **State** versus marketing
**Judgment** the store should not harden?

## Direct Answer

**The proof-device pattern is already a captured cut.** The `telehealth.md` cohort pack
records a standardized device checklist in its **"Health-merchant credibility"** and
**"Payment & commitment"** lines — per brand, with explicit `y` / `n` / `not shown` flags and
a built-in *"absence noted honestly, not asserted either way"* convention. So the read is an
aggregation, not a new extraction.

**The headline market pattern: brands lean on the cheap merchant seal and under-surface the
deep pharmacy credential.** Across the 56-brand cohort (C1), all counts corrected per the Loop 2
re-derivation:

- **LegitScript certification is the majority norm but not universal** — surfaced on **~33/54
  captured footers (~61%)** (C2). Where it is *absent*, the set splits into genuine N/A
  (supplement sellers truniagen, prohealth; insurance-billed primary-care onemedical;
  non-pharmacy functionhealth) **and brands that simply don't show it on captured pages**
  (defymedical, gethealthspan, hellopepti, ivimhealth, joinfridays, lifemd, nurx, getopt,
  gogeviti, goodlifemeds, joinamble, keeps, kingsbergmedical, niagenplus, struthealth,
  vitalityrx). So it is the floor *most* of the field stands on, not all of it.
- **Pharmacy accreditation (PCAB / ACHC / NABP) is the least-surfaced device** — only **~6
  brands surface it positively** (eden-health, struthealth, hydramed, gethealthspan,
  mylifeforce, innerbalance); **~38/54 are explicitly "not shown"** (C3). This is the cleanest
  differentiator in the cohort: most brands carry the easy LegitScript merchant seal, but few
  surface the deeper compounding-pharmacy accreditation that would substantiate the 503A/503B
  lane the pack records for ~50 of them.
- **Named clinicians are shown by a clear majority** (~38 shown vs ~16 not-shown) **and the
  not-shown set tracks the business model** (C4): provider-fronted optimization brands (TRT,
  longevity/NAD, peptides — defymedical, getpetermd, maximustribe, gethealthspan, marek,
  sermorelin) put a named medical director / advisory board up front; the brands that *skip* a
  named bench are disproportionately commodity GLP-1 compounders (directmeds, henrymeds,
  remedymeds, telolife, ivyrx) leaning on LegitScript + price.
- **Commercial-trust devices are thin and mostly recent**: ~28 brands state **cancel-anytime**;
  only ~5 carry a **money-back / outcome guarantee**, in two flavors — a satisfaction refund
  window (innerbalance 6-month on Oestra, sermorelin 180-day, prohealth 100-day supplement
  refund) and a GLP-1 **"lose X% of bodyweight or your money back"** outcome guarantee (tryshed),
  plus a generic money-back claim (vitalityrx). Most "guarantees" are plan-adjustment, not
  money-back (C5).

**Design answer: query-time-grouping-enough — no new primitive.** The proof-device cut already
exists as semi-structured cohort-pack prose; it rolls up by grep-and-classify. Two wrinkles,
both already-known pressure: (a) it lives in *prose*, not frontmatter, so aggregation is a
classify pass with a real positive-vs-negated parsing risk (`tooling-ergonomics` /
`source-rigor`, cf. run 019's polarity miscount); (b) the entire read sits on a **State /
Judgment boundary** — *device-presence on a captured page is State; whether the underlying
claim is true or differentiating is Judgment the store must not harden.*

## Evidence Used

Local store only; no external fetch, no spend. All counts are **device-presence on captured
pages**, never claim-truth.

- **C1 — denominator:** 54 unique-domain `store/<domain>/telehealth.md` cohort packs (a `find`
  returns 56 because 2 archived copies sit under `captures/`); 54 carry the credibility cut.
  Receipt `proof-device-sweep` S1.
- **C2 — LegitScript ~33/54 shown (~61%)** *(corrected from ~42/56; polarity error)*. Absent/N-A
  set: genuine N/A (truniagen, prohealth supplement; onemedical insurance; functionhealth
  non-pharmacy) **plus** not-shown-on-captured-pages (defymedical, gethealthspan, hellopepti,
  ivimhealth, joinfridays, lifemd, nurx, getopt, gogeviti, goodlifemeds, joinamble, keeps,
  kingsbergmedical, niagenplus, struthealth, vitalityrx). S1.
- **C3 — pharmacy accreditation surfaced positively by only ~6; ~38/54 explicitly "not shown."**
  Positive set *(corrected)*: eden-health, struthealth, hydramed, gethealthspan, mylifeforce,
  innerbalance. (defymedical, brellohealth, maximustribe, ro-co were wrongly listed positive on
  the first pass — their packs say "not shown.") S1.
- **C4 — named clinicians ~38 shown / ~16 not-shown** *(corrected from ~29/~25)*; the not-shown
  set tracks model (commodity GLP-1 compounders). S1.
- **C5 — ~28 cancel-anytime; ~5 money-back/outcome guarantee** (innerbalance, sermorelin,
  prohealth, tryshed, vitalityrx). S1.

## Companies Seen

56-domain telehealth cohort (every `store/<domain>/telehealth.md`). By `anchor_category`
(C1): GLP-1 ×19, TRT ×8, longevity/NAD ×9, multi/none ×11, sexual-health ×3, peptides ×2,
plus single anchors hair (keeps), labs (functionhealth), primary-care (onemedical), womens-HRT
(innerbalance). Per-domain device join in receipt S1.

## Missing / Stale Coverage

- The cut records **what was on captured pages**, not the brand's full site. A brand's
  accreditation or clinician page may exist on a URL the capture did not reach — so every
  "not shown" is **"not found on captured pages," never "brand lacks it."**
- 2 of 56 packs phrase credibility differently and were read by hand, not by the standard line.
- Capture dates vary across the cohort (telehealth.md `captured_at` spans ~2026-05-30 →
  2026-06-20); a footer seal could change between captures. Not a current-claim read, so this
  is a coverage caveat, not a freshness blocker.

## Source Gaps

- **No truth verification.** A LegitScript seal present ≠ the pharmacy is in good standing; a
  "named clinician" ≠ a verified active license; "503A certified" is brand-asserted. Verifying
  any of these would require external sources (LegitScript's verify endpoint, state board
  lookups) — out of scope for a store-only run and explicitly disallowed by the contract.
- Positive-vs-negated counts are grep-classified from prose. The first pass **understated this
  risk** as ±2–3: Loop 2 found a systematic **polarity error** (lines reading "…not shown / not
  observed" counted as positive) that shifted three tallies by up to ~9. Counts above are the
  corrected re-derivation. The *pattern* (LegitScript the majority floor, accreditation rare,
  clinicians model-dependent) was independently confirmed and is robust; the integers are
  decision-grade only after the Loop 2 correction, and even then are best read as "majority /
  minority / rare," not exact.

## External Completeness Check

Not run — the contract is store-only and the read's value is the *internal* device pattern, not
a market census. The one place an outside denominator would matter (is the captured cohort
representative of the GLP-1/TRT market?) is the standing selection-bias caveat (MRL-001), not
specific to this run.

## Market Pattern

**Trust is signalled cheaply and rarely deeply.** The cohort has largely converged on
LegitScript as the merchant-trust seal — the **majority norm (~61%)** rather than universal —
and its *absence* is often diagnostic of business model (supplement / insurance / non-pharmacy)
as much as of any trust gap.
The genuine differentiation lives one layer down and is mostly *unspent*: pharmacy
accreditation (PCAB/ACHC/NABP) is surfaced by a minority even though most brands claim a
compounding lane, and a named clinician bench is a deliberate positioning choice that splits
the field — provider-fronted optimization brands (TRT, longevity, peptides) pay for it;
commodity GLP-1 compounders skip it and compete on price and speed. Commercial-trust devices
(money-back, transparent cancellation) are still emerging as a wedge, concentrated in the
satisfaction-guarantee and GLP-1 outcome-guarantee corners.

For a downstream reader (a strategist or a creative director profiling this field), the
brief-ready line is: **"LegitScript is the floor; a named medical bench and real pharmacy
accreditation are where a brand can still look more legitimate than the pack — and most of the
pack hasn't bothered."**

## What Would Change This Answer

- A re-capture that reached brands' `/about` / `/physicians` / accreditation pages could move
  several "not shown" devices to "shown" — the tallies are capture-depth-bounded.
- Promoting the device checklist from cohort-pack prose to a small structured frontmatter block
  (e.g. `proof_devices: {legitscript: y, pharmacy_accreditation: not-shown, named_clinicians:
  y}`) would make this read a one-line query instead of a classify pass — a `depth-backfill` /
  schema candidate, **not** built here (triage only).
- External verification of any single device (LegitScript status, license lookups) would
  convert device-presence State into a credibility Judgment — a different, approval-gated run.
