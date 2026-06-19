# Run Notes

```yaml
run_status:            reviewed
evidence_mode:         store-only
autonomous_eligible:   yes
termination_reason:    completed
pressure_lenses_fired: [query-time-grouping-enough, coverage-caveat, source-panel]
```

> **Loop 2 outcome (2026-06-19):** Reviewed via a 3-pass adversarial workflow (evidence verifier +
> consumer + developer). The verifier confirmed **8 of 9** load-bearing claims verbatim and caught **two
> field-read errors**, both corrected in `read.md` + receipt: (1) the narrative said **"three of four"**
> diagnostic-first brands carry Schedule-III testosterone — the correct count is **four of four** (gogeviti
> was already in the evidence table); the fix *strengthens* the longevity-coat finding. (2) **gethealthspan's**
> access/labs were overstated as "required/membership" — store frontmatter is `access_model: à-la-carte/both`
> + `Labs: optional` (only HRT/GLP-1/TRT are membership-gated); the Diagnostic-first label holds by
> *positioning*, not access. The headline axis finding (supply↔diagnostic) and the cross-cohort "longevity
> coat over hormone optimization" tell **survived scrutiny**. Triage: Evidence Logs appended to **MRL-002**
> (positioning recurrence + a verbatim-field-extract guard) and **MRL-001** (clean-frontmatter contrast);
> one **new P3/Submitted candidate MRL-010** (reviews/forums body content as a source ingredient — second
> sighting). No graduation.

## 30-second operator read

- **Did the run work?** Yes. Store-only, no spend, no mutation. A **fresh read axis** (positioning /
  proof / whitespace) on the longevity/NAD cohort 008 flagged — deliberately *not* a third
  price-visibility grouping.
- **What was awkward?** Naming the "wedge." The four-wedge framing in the question collapsed under the
  data into **one axis** (supply-access ↔ diagnostic-first). The hard line was keeping the wedge/whitespace
  labels as labeled Judgments rather than letting them read as captured fields.
- **What the next agent should know:** the captured-State layer (`telehealth.md` Credibility/Notes +
  `profile.md`) carried a **positioning read** off disk with zero re-capture — a different demonstration
  than the price-column reads. The standout finding: **"longevity clinic" frequently = "hormone-optimization
  clinic in a longevity coat"** — 3–4 of the diagnostic-first brands sell Schedule-III testosterone behind
  the longevity banner. That ties cleanly to 008's "posture tracks business model."

## What happened

Gated on the contract (scout-only → store-only → autonomous → approval:no, all pass). Derived the cohort
by grepping `telehealth.md` frontmatter for `anchor_category: longevity/NAD` → 8 brands. For each, read the
`## Credibility & access` + `## Notes` positioning blocks and pulled the verbatim hero + lead proof device,
cross-checked against `profile.md`/`offerings.md`. Placed each brand on a supply↔diagnostic axis from two
captured signals (required-labs, access model), and flagged which "longevity" brands carry page-attested
Schedule-III Rx. Built one derived receipt
([`receipts/longevity-positioning-panel.md`](receipts/longevity-positioning-panel.md)). Wrote the read
keeping the axis, whitespace, and longevity-coat claims explicitly labeled `[J]` and tied to per-brand
State. No external fetch, no `store/` write.

## Inputs and scope

- `store/*/telehealth.md` frontmatter (cohort derivation) + `## Credibility & access` / `## Notes`
  (positioning + proof + controlled-substance lines) for the 8 core brands (captures 2026-05-31…06-18).
- `store/*/profile.md` + `offerings.md` for verbatim hero/proof cross-checks (agelessrx XPRIZE/"70,000+
  users"; gethealthspan "12K patients"/MD-PhD board; mylifeforce $599 50+ biomarker diagnostic; honehealth
  Trustpilot 4.8/11,677).
- **Straddlers inspected, scored separately:** getopt (TRT-anchored, longevity front door — the clearest
  longevity-coat case), joinfridays (GLP-1-anchored). Neither counted in the core 8.

## Friction log

- **Same latest-capture / field-extract loop** as 008, but reading a *positioning/credibility* surface
  (`Credibility & access` + `Notes`) rather than the `Visibility` column — reinforces MRL-002's "State
  reads beyond pricing" scope. Extraction was trivial (one grep + section read per brand); the only real
  labor was the Judgment of where each brand sits on the axis.
- The cohort grep was clean (`anchor_category` frontmatter did the denominator work in one pass) — no
  manual list-building, unlike 008's hand-drawn TRT boundary.

## Evidence limits

- **Partial cohort** — 8 store-resident brands, not a census; named external longevity brands (Novos, Tally
  Health, Modern Age, Blueprint) are out of frame. Said plainly; the axis/sameness findings are structural,
  not artifacts of the sample.
- **Point-in-time heroes** — agelessrx (coupon instrumentation) and honehealth (Optimizely A/B live) are
  captured-floor snapshots; niagenplus/truniagen heroes observed stable.
- **gogeviti Rx grain is app-walled** — Schedule-III read is from page-attested catalog references, not a PDP.
- **Axis/whitespace are derived Judgments**, not store fields — labeled `[J]` throughout.

## Loop 1 exit check

- Status was `scout-only` before Loop 1: **pass**
- `Selected Run Contract` was present and consistent with header: **pass**
- `autonomous_eligible: yes`: **pass**
- `evidence_mode` was `store-only` or `local-existing`: **pass** (store-only)
- `approval_needed: no`: **pass**
- No disallowed action happened: **pass** (no live fetch, no mutation; point-in-time heroes dated;
  partial cohort flagged)
- Required citations / receipts present and source-graded: **pass** (one derived receipt, 8 brands graded
  primary)
- No snippet treated as evidence: **pass** (no snippets used; pure State)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass** (no current/news claims;
  every positioning/proof claim ties to a dated capture)
- Absence language says "not found", not "not true": **pass** ("no TRT SKU captured", "no named clinician
  roster", "none leads with outcome proof" — never "no such thing exists")

## Surprises

- **The four-wedge premise collapsed.** The question proposed four parallel wedges (NAD vs rapamycin vs
  diagnostic vs hormone); the data sorted them onto **one supply↔diagnostic axis** instead — a cleaner and
  more useful organizing finding than the question assumed.
- **The diagnostic-first pole is a hormone business in disguise.** 3 of 4 (plus straddler getopt) sell
  Schedule-III testosterone; the longevity banner is a category-acceptable wrapper. The supply pole carries
  **zero** scheduled Rx — a clean split.
- **Nobody sells the actual promise.** Every brand leads with mechanism, measurement, or access — none with
  outcome proof of life/healthspan extension. That whitespace is category-structural.

## Pressure tags

| Fired tag | What fired in this run | Triage implication |
|---|---|---|
| `query-time-grouping-enough` | The whole read was a grouping of existing `telehealth.md` positioning/credibility State; no durable "positioning-wedge" or "longevity-cohort" category object is needed or wanted. | no-op — reinforces MRL-002 recipe scope (now State *positioning* reads, not just pricing) |
| `coverage-caveat` | Partial cohort (8 store brands, named external longevity brands absent); point-in-time heroes; app-walled gogeviti Rx grain — all bound the completeness claim. | watch / strengthens MRL-001 |
| `source-panel` | The load-bearing whitespace ("do buyers trust this / what do they regret") and the trust-gap read need a **reviews/forums source set** the store doesn't hold as State. Recurs from 008-family customer-pain pressure. | watch — second sighting of the reviews-as-source-ingredient gap |

No new tag needed. "No new primitive needed" is the honest outcome — this is a recurrence read on a new axis.

## Triage submissions

No new items. This run **adds recurrence evidence** to existing queue items; Loop 2 may append Evidence Log
entries to:

- **MRL-002** (query recipes) — a *State positioning* read (cohort grep on `anchor_category` →
  `Credibility & access`/`Notes` section read → axis labeling) recurred cleanly. Extends the recipe family
  beyond the `Visibility`-column pricing read (008) to a positioning/proof read — same latest-capture +
  field-extract idiom, different captured surface.
- **MRL-001** (denominator reconciliation) — *lighter* this time: the `anchor_category` frontmatter did the
  cohort boundary in one grep, with only the straddlers (getopt, joinfridays) needing a hand call. A useful
  *contrast* data point — when a clean frontmatter cut exists, denominator labor nearly vanishes.

The `source-panel` tag (reviews/forums as a missing source ingredient) is a **watch**, not a submission —
it's the second sighting (008-family customer-pain pressure) but still below a graduation bar; Loop 2 should
decide whether it deserves its own queue item or rolls under existing source-rigor pressure.

No graduation, no implementation, no spike proposed.

## Next-run advice

- The **"longevity coat over hormone optimization"** tell is now a concrete, store-evidenced pattern. A
  tight store-only follow-up could quantify it: across *all* longevity/NAD + TRT brands, what share of
  "longevity"-anchored brands sell Schedule-III testosterone? That sharpens the positioning-vs-substance
  read into a number.
- The **reviews/forums source gap** has now fired twice (trust/whitespace reads keep needing it). If a third
  read needs it, it likely earns an explicit triage item rather than a watch.
- Consider running the **same positioning-axis read on a different cohort** (sexual-health/ED, or GLP-1) to
  test whether "everyone sells mechanism/measurement/access, nobody sells outcome" is a longevity quirk or a
  telehealth-DTC pattern — the positioning analogue of 008's price-posture generalization.
- Tell the operator to start **Loop 2** in a fresh session.

---

**Loop 1 complete — `run_status: read-done`.** Start Loop 2 for review.
