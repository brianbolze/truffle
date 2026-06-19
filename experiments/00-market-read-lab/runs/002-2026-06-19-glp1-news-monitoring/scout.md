# Scout

## Prior Context Read

- `triage.md`: six active queue items, none acknowledged. Most important open
  pressures:
  - `MRL-001`: denominator reconciliation convention, held pattern-level.
  - `MRL-002`: market reads keep hand-building store-query surfaces; prefer QUERYING
    recipes over per-query helpers until the same query recurs.
  - `MRL-005` / `MRL-006`: named supplier / clinical edges are promising but sparse;
    re-test on a backend-naming-dense cohort before graduating anything.
- Last 3 `run-notes.md` files:
  - Run 000: GLP-1 pricing visibility was query-time answerable; store out-completed
    the Notion denominator; latency came from re-deriving denominator / visibility
    mechanics.
  - Run 001: backend relations are load-bearing but mostly already captured; parent
    edges use `parent`/`owns`, integration posture uses `pharmacy_model`, named supplier
    / clinical edges are useful but too sparse in men/hormone.
- Current run artifacts, if resuming: Scout-only scaffold for Run 002. Brian selected
  the News / Monitoring alternate before Loop 1. No read has run.

## Candidate Questions

| Question | Type | Why this is worth a run | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|
| In the compounding-heavy GLP-1 telehealth cohort, do brands name pharmacy or clinical backends often enough for supplier concentration to become measurable? | mixed | Directly tests the recurrence gate for `MRL-005` / `MRL-006` without inventing a new topic. Run 000 already built a GLP-1 working set; Run 001 already defined the relation method. | Start from the Run 000 GLP-1 seller list, then read `telehealth.md` Fulfillment/Provider and profile body claims for named pharmacies / P.C.s / provider networks; report named vs unnamed rate and repeated counterparties. | Over-reading "licensed pharmacy" as a named relation; turning one denser cohort into automatic graduation. |
| Which recent external events or policy changes could invalidate the GLP-1 pricing / access read, and what would a minimal news-monitoring routine need to watch? | mixed | Tests the News / Monitoring pillar directly. Run 000 identified branded-drug access, compounding legality, and price floors as volatile; this asks whether store-only reads need a fresh external layer. | A tiny source panel: FDA/official compounding status, manufacturer cash-pay pages, maybe 1-2 high-signal industry/news sources; compare against Run 000 assumptions. | Becoming broad news research; confusing current policy truth with a reusable monitoring convention. |
| Across men's sexual-performance brands, are "proprietary" formulations actually distinct products or mostly recombinations of the same molecule stack? | mixed | Tests non-company anchors: molecules, formulations, delivery forms, and equivalence. Commercially useful for offer design and positioning. | `offerings.md` rosters for BlueChew, Rugiet, MEDVi QUAD, RexMD, Hims, PeterMD where available; compare active ingredients, delivery form, and claimed differentiators. | Becoming a molecule taxonomy project; treating dosage/formula gaps as proof of uniqueness. |
| Which store fields proved most volatile or quietly stale across the first two reads, and what should a minimal monitoring recipe watch first? | system-test | Moves from "we noticed freshness caveats" to a prioritized monitoring question. Could connect News, Signals, and run notes without building a broad monitor. | Evidence from Run 000 / 001 caveats plus sampled store captures: price floors/promos, branded-drug routing, named backend partners, pharmacy_model, access_model. | Too meta if it never touches company evidence; over-building a monitoring system from two runs. |
| Do supply-side backend profiles (OpenLoop, MDIntegrations, Curexa, Strive, Hallandale) reveal customer/network concentration better than DTC brand pages? | mixed | Tests the mirror-image hypothesis from Run 001: supplier pages may expose relation pressure more cheaply than every DTC capture. Useful for vendor strategy. | Read supply-side profiles and their provider/customer/network claims; compare what they reveal against named DTC edges from Run 001. | Supplier sites may market capabilities without naming customers; absence is not disproof of concentration. |
| What Pantry write-backs have the first two runs produced, and do they imply a reusable write-back artifact or just ad hoc tasks? | system-test | Consumer reviews twice found Pantry outputs hidden inside system notes: Run 000 node diff, Run 001 edge list. This tests whether the lab should produce a standard "write-back candidates" receipt. | Review Run 000 / 001 consumer reviews, receipts, and triage. Identify recurring output types and whether they are useful without direct execution. | Becoming process theater; two sightings may justify a section, not a system. |
| Within GLP-1 / metabolic telehealth, which competitors route patients toward branded drugs, compounded drugs, or parent/partner insurance paths, and what does that imply about offer resilience? | market/system-test | Bridges Run 000 pricing and Run 001 relations. Commercially useful: branded-drug routing may be the strategic response to compounding volatility. | `offerings.md` + `telehealth.md` for GLP-1 brands; parent/partner routing claims; public price/access claims; explicit caveats for stale branded-drug status. | Re-answering Run 000 with slightly different labels; needs a crisp routing/resilience frame. |
| Are missing module gaps (`altrx-com`, `marquelongevitylab-com`) actually blocking market reads, or are they isolated cleanup tasks? | system-test | Pressure-tests `MRL-003` before acting. If these gaps keep blocking runs, backfill priority rises; if not, it stays a bounded cleanup item. | Revisit Run 000 / 001 and any candidate question where these companies would matter; inspect what existing profile data can and cannot answer. | Spending a run on housekeeping rather than market learning; absence in two reads may still be too small a sample. |

## Selected Question(s)

1. **Selected by Brian:** Which recent external events or policy changes could
   invalidate the GLP-1 pricing / access read, and what would a minimal news-monitoring
   routine need to watch?

The prior recommended next question (GLP-1 backend naming / supplier concentration) is
still useful, but deliberately deferred.

## Selection Notes

This run intentionally exercises the **News / Monitoring** pillar rather than another
store-only relation or pricing pass. Run 000's GLP-1 pricing read made several
time-sensitive assumptions: compounding legality, branded-drug availability/cash-pay
pricing, and whether public price floors still reflect a real access path. This run
should ask which external events could invalidate that read, and what a minimal
monitoring routine would need to watch.

Trustworthy evidence should stay deliberately small:

- official FDA / regulatory status for semaglutide and tirzepatide compounding,
- manufacturer or official cash-pay/access pages for branded GLP-1s,
- 1-2 high-signal recent industry/news sources only if they materially change the
  answer,
- Run 000's `read.md` and `run-notes.md` as the baseline being stress-tested.

The output should not become a broad news digest. The market answer is useful, but the
system-learning answer matters too: what source types, cadence, and artifact convention
would be enough for a minimal GLP-1 monitoring routine?

Treat prior run patterns as hypotheses, not defaults. Prefer testing whether the same
pressure recurs over copying a previous run's exact method.

## Scout-only Handoff

Scout-only is complete. Start Loop 1 in a fresh session for this run.
