# Run Notes

> **Historical run notice:** This run predates the current autonomous contract. Use it
> for evidence and pressure patterns only; do not copy its header, stage behavior,
> receipt rigor, or artifact shape. Current conventions live in
> `experiments/00-market-read-lab/templates/`.

```yaml
pressure_lenses_fired: [source-panel, source-rigor, coverage-caveat, category-scoped-signal-gap, synthesis-staleness]
```

> First News/Monitoring run. `category-scoped-signal-gap` and `synthesis-staleness`
> are one-sighting system lenses — submitted to watch for recurrence, not to act on.
> `source-rigor` is a process learning from operator review.

## 30-second operator read

- **Did it work? Yes, but with a source-rigor miss.** A tiny live panel (~8 Firecrawl
  credits) found a real direction of travel: Run 000's compounding-law and branded-cash-pay
  assumptions look vulnerable. But the run was too confident from lazy news/search evidence.
  Search snippets can find where to look; they are not enough to make regulatory or pricing
  claims decision-grade.
- **What was awkward?** The honest deliverable is a *non-finding for the store*: the events
  that move the read (FDA status, NovoCare/LillyDirect pricing) **don't live in any company
  in the cohort** — and the biggest one has no company home at all. That's the interesting
  part, but it doesn't map onto today's per-domain Signals path.
- **What the next agent should know:** this is the mirror image of Run 000. Run 000 inverted
  the "need a source panel" expectation (store out-completed the external list). Here the
  source panel is genuinely load-bearing — because the question is about *exogenous* events
  the store can't see by construction. The two runs together calibrate *when* the source-panel
  lens fires: external panel for event/freshness questions, internal reconcile for membership.

## What happened

Read Run 000's `read.md` + `run-notes.md` as the baseline, plus the scout selection and the
seed panel. Ran 4 Firecrawl searches (FDA compounding status; NovoCare Wegovy pricing;
LillyDirect Zepbound pricing; telehealth branded-pivot news) → one tight panel receipt
([`receipts/external-event-panel-2026-06-19.md`](receipts/external-event-panel-2026-06-19.md)).
Built a staleness-delta table against Run 000's three time-sensitive assumptions, then wrote
the read plus a minimal-monitor source spec. Checked `SIGNALS.md` to confirm the signal path
is strictly `store/<domain>/...` before submitting the category-grain triage item. No store
re-capture, no `store.py` pass — this run asks what *outside* the store moves the answer.
Post-review, the biggest learning is that external/current-event reads need a higher
receipt bar than store-only reads.

## Inputs and scope

- Baseline: Run 000 `read.md`, `run-notes.md`.
- External panel (captured 2026-06-19): FDA actions (pharmacytimes, medpagetoday,
  safemedicines, natlawreview); manufacturer direct-pay (NovoCare PDF, pricinginfo.lilly.com,
  investor.lilly.com, CNBC, prnewswire); brand pivots (Yahoo, financialcontent, Reuters).
- Spend: ~8 Firecrawl credits (4 searches). The mistake: treating search snippets as
  citation-grade because the panel was intentionally tiny. For monitoring/news runs,
  snippets are direction-finding only. Receipts need exact URLs, captured dates, source
  type, and primary/secondary status before the read can use confident language.
- Exclusions: deliberately no broad GLP-1 news digest; no re-derivation of the Run 000 cohort.

## Friction log

- **No place to file an exogenous, category-level signal.** The whole result is three facts
  that govern the GLP-1 cohort — and there is no obvious store location for "FDA compounding
  status" or "manufacturer reference price." `SIGNALS.md` already half-acknowledges this:
  Trends/SERP are keyword/category-grain and "stay on the pipe," attached to a domain via
  `--domain`. A regulator has no domain to attach to.
- **The read had to be hand-assembled as a staleness diff.** There's no convention for "stress
  a prior read against fresh external events" — I invented the delta table. Light, but it's the
  second lab artifact (after Run 000's denominator recipe) that a market read had to improvise.
- **Lazy news fetching manufactured confidence.** The agent found the right source classes
  quickly, then over-treated snippet summaries as evidence. That's a lab/process learning,
  not just a caveat on this answer.

## Evidence limits

- The panel is intentionally shallow (search snippets + dates, not fetched source bodies).
  It is good enough to establish *where to investigate*, not to quote exact numbers or make
  strong regulatory claims. Before reuse, pull primary FDA/manufacturer pages directly and
  record exact URLs plus capture dates in the receipt.
- "Two of three assumptions stale" is a judgment over Run 000's prose, not a recomputed cohort.
  The *visibility* split (33/42/25) was not re-tested and is probably still ~true; only the
  *price/legality* claims were stressed.
- Manufacturer cash-pay offers are themselves promotional and dated. The branded floor is
  volatile, which is the point; exact numbers need primary-source re-check before reuse.

## Surprises

- **The synthesis decayed faster than the data.** Store captures (May 30–Jun 18 2026) are
  fresh, yet Run 000's *read* is stale — because the decaying facts (legality, manufacturer
  price) aren't captured per-company at all. Freshness of a capture ≠ freshness of a read.
- **The cohort capture is channel-blind, not just stale.** Manufacturer-direct branded
  paths appear to be materially cheaper than the DTC-brand pages imply, but they are
  invisible to a read built from DTC-telehealth pages because the manufacturers aren't
  "telehealth companies." More brand captures wouldn't fix it.
- **The market may be converging the way Run 000 said it might** ("compounding-law movement
  → brands shift to the branded tier") — but the partnership/pivot evidence needs primary
  follow-up before it carries more than directional weight.

## Pressure lenses

- **`source-panel` (FIRED — inverts the Run 000 inversion).** Run 000 found the external panel
  *unnecessary* (store out-completed it). Here it's load-bearing, because the question is about
  exogenous events. Net lesson across both runs: reach for an external panel for
  **event/freshness** questions, not for **membership/denominator** questions. Sharpens the
  conditional Run 000 added to the pressure table.
- **`source-rigor` (NEW — process learning).** A source panel is not the same thing as a
  citation-grade receipt. News/search panels may identify candidate events, but any claim
  about current law, policy, prices, or partnerships needs primary-source URLs and dates
  before the read uses confident language.
- **`coverage-caveat` (channel variant).** The standard "not-captured ≠ not-offered" caveat has
  a sibling here: **not-captured-because-out-of-cohort** (manufacturer-direct channel). Worth
  naming as channel-completeness vs company-completeness.
- **`category-scoped-signal-gap` (NEW — one sighting).** The signals that move a cohort read are
  category-level exogenous events (regulatory status, manufacturer reference pricing) with no
  per-domain home; the highest-consequence one (FDA) has no company home at all. `SIGNALS.md` is
  `store/<domain>/signals/...`. Submitted below; watch for recurrence before acting.
- **`synthesis-staleness` (NEW — one sighting).** A read inherits the half-life of its most
  volatile claim, and that claim can decay while the underlying captures stay fresh. Argues for
  marking a read's volatile claims / governing external clocks, not for new State.

"No new *State* primitive needed" holds. Whether a new *Signals* primitive is needed is a
genuine fork (see triage) — and may resolve to "monitoring is a consumer/project job."

## Triage submissions

Queue candidates only — none graduated or approved for implementation by this run.

- **[P3 · Submitted] Category-scoped / non-company exogenous-signal anchor.** Regulatory status
  and manufacturer reference pricing govern a whole cohort but have no per-domain home; FDA has
  no company home at all. Evidence: this run's panel + `SIGNALS.md`'s own keyword-grain caveat +
  the deferred "cohort maps." *Proposed next step (if it recurs):* decide **where** category-grain
  exogenous signals live — a market/topic-scoped path (e.g. `store/_market/<topic>/…`) vs a
  project-side monitor — explicitly **not** building one now, and explicitly anti-Doro (no graph,
  no entity-resolution). One sighting.
- **[Low · Submitted] Minimal-monitor source-panel convention.** The 3-source shape (FDA
  compounding; NovoCare + LillyDirect price pages; one branded-pivot news query, ~monthly) is a
  reusable template for "what external events could invalidate a stored market read." But the
  convention must include source rigor: exact URL, captured date, source type, primary vs
  secondary, and whether the claim is snippet-only / direction-finding. Candidate: a
  *documented panel convention*, not a built monitor. Sighting #1 of a monitoring panel.
- **[Evidence, not new item] Directionally supports Run 000's own prediction** that "the
  branded-drug tier is the live edge… where a freshness/Signal layer would earn its keep."
  Attach to whichever of the two items above Loop 2 keeps after primary-source confirmation.
- **[No-op] No new State primitive.** The pricing/access answer was never a State object; it's a
  freshness/Signal question. And possibly no new *Signals* primitive either, if the engine rules
  monitoring a consumer/project cadence — that fork is for human review, not this run.

## Next-run advice

- **Treat the source-panel lens as conditional, now calibrated by two runs:** external panel for
  event/freshness/legality questions; internal reconcile for membership/denominator. Don't default
  either way.
- **Before quoting a price, policy, or partnership live,** pull the primary page directly
  and record it in the receipt. Search snippets establish where to look, not a number or
  legal status to commit to.
- **If a third run also surfaces a homeless category-level signal,** that's recurrence — and the
  point to actually design where exogenous/cohort signals live. One more sighting, not yet.
- **Consider a run that re-tests Run 000's visibility split** (33/42/25) directly against current
  captures — this run only stressed the price/legality claims, not the publish-vs-gate finding.
