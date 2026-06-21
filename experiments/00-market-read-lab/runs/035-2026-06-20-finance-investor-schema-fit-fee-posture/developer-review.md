# Developer Review

Question: **What did this run reveal about Truffle's missing or weak ingredients,
capabilities, and guardrails?**

## Capability pressure

| Capability | Observed gap or strength | Evidence from this run | Discovery disposition |
|---|---|---|---|
| **Capture** | *Strength.* The store correctly captures investors as a distinct entity and flags off-site finance facts (AUM/fees) as `unverified_fields` "deep-research, not capture" — it doesn't hallucinate fee data. | 5/7 allocators flag AUM/fees not-on-site (C3); blueowl/spero disclose what *is* on-site (C4/C5). | No-op — capture behaved correctly. |
| **Structure** | **The load-bearing finding.** Two-sided MRL-015: the *subtractive* investor gate (entity_type value + portfolio_shape/business_model empty-by-rule) is **solved and working** (O1); the *additive* capital-allocator field set (stage / AUM band / vintage / thesis / LP type) is the **open gap** — no structured home (O2). | O1/O2; receipt C2/C7; TAXONOMIES:19,72. | **Submit MRL-015 evidence** — first positive confirmation of the gate + first market-read demonstration of the additive gap. |
| **Query / access** | `query-time-grouping-enough` fires **FALSE** on a *content* axis for the first time (O3). The only greppable finance cuts are `entity_type` + `primary_industry`; everything decision-grade (stage, AUM, thesis) is prose. | O3; read.md Gap Map. | **Submit MRL-002 evidence** — sharpens the tag as *corpus-shape-dependent*, not universal. |
| **Freshness / automation** | Not exercised (store-only, no signals read). | — | No-op. |
| **Synthesis** | *Strength.* The read held the State/Judgment boundary cleanly: subtype labels + gate-type framing labeled as Judgment; fee/AUM absence framed as not-found, not not-true; the schema-can't vs firm-didn't distinction (S1) is a genuinely sharp synthesis. | S1; read.md Gap Map "two stacked absences." | No-op — synthesis was a strength. |
| **Guardrails** | *Strength.* Store-only honored (no spend/live browse); denominator treated as partial and reconciled 16→9; the contracted `loop1_failure_mode` (conflating schema-can't with firm-didn't) was avoided **by name**. | Exit check all pass; G2 denominator reconciliation; S1. | No-op. |

## Lenses

**Steward** — The system stayed honest. The investor gate prevents *wrong* structured
data (no fake "Subscription" on a VC), which is the right kind of honesty. The one fix
the Loop-2 verifier caught was cosmetic (G1 "trailing whitespace" → "inline comment
suffix"; the under-count risk is real, the mechanism description was off) — folded into
read.md/receipt/run-notes before finalize. All load-bearing counts (9/7/6/5, the 8
business_model values, both contract line numbers) re-derived with **zero numerical
discrepancy**. State/Judgment boundary held.

**Dev Agent** — The recurring toil is a **field-census** read (which fields populate vs
empty across a cohort) — F1, a distinct grain from the MRL-002 value-extraction recipes.
One sighting; recur-watch. The G1 exact-line-vs-substring grep hazard recurs from run-033
(now 2 sightings on 2 different fields) — a real, cheap-to-state cohort-draw discipline
note. Neither earns a helper yet; both are grep-verifiable contract notes if they recur.

**Founder** — The anti-sprawl call is clear and should hold: MRL-015's additive half
should **not** spawn a capital-allocator structured field family on n=9 evidence — the
facts are off-site for 5/7 (a field would be sparse and rot), and there's no named
downstream finance-cut consumer yet. The lightest path if it ever graduates is a
documented prose convention / query recipe (W1), consistent with "spend on conventions,
not infra." This keeps the gate (which compounds) without buying ontology gravity.

## Recommendation

- **No-op / keep as observation:** the field-census friction (F1), the G2 denominator
  estimate miss, the coverage-caveat (all correctly bounded).
- **Watch for recurrence:** the G1 exact-line grep hazard (2nd sighting, run-033 + 035);
  the W1 additive-field wish (pending a 2nd, less VC-skewed finance cohort + a real
  consumer); the F1 field-census recipe grain.
- **Submit triage evidence:** MRL-015 (two-sided confirmation — the gate works, the
  additive shape is the open gap, first market-read evidence) and MRL-002 (first content-
  axis `query-time-grouping-enough: FALSE`, tag is corpus-shape-dependent). Both as
  Evidence Log entries on existing items, not new items — one sighting each, no new axis.

## Optional triage evidence

See the two Evidence Log entries appended to MRL-015 and MRL-002 in `triage.md`. Both are
additive evidence on existing items; neither moves a graduation clock. Detail lives in
`discovery-ledger.md` run-035 rows O1–O5/S1/G1/W1/F1.
