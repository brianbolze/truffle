# Market Read

Status: answered 2026-06-19 (Run 002). Stress-test of Run 000 against a tiny live
external panel (Firecrawl, ~8 credits). Panel receipt:
[`receipts/external-event-panel-2026-06-19.md`](receipts/external-event-panel-2026-06-19.md).

> Post-review source-rigor caveat: treat this read as directional, not decision-grade.
> The panel found plausible invalidating events, but leaned too heavily on search/news
> snippets. Re-pull primary FDA/manufacturer sources before quoting law, price, or
> partnership claims.

## Question

Which recent external events or policy changes could invalidate the GLP-1 pricing /
access read (Run 000), and what would a minimal news-monitoring routine need to watch?

## Direct Answer

**Two of Run 000's load-bearing assumptions look vulnerable, and the strategic story may
be moving faster than the store can see.** This run found plausible invalidating events,
but the source grain is too weak for a final market claim.

1. **Compounding legality may have shifted from default floor to exception lane.** Run 000
   treated compounded semaglutide/tirzepatide as "the price floor of the category." The
   panel found FDA/industry signals that shortage-era access has narrowed and enforcement
   risk is live. Primary FDA sources are needed before calling the legal state settled.
2. **Manufacturer-direct branded cash-pay appears materially cheaper than Run 000's branded
   tier.** Run 000 put the branded tier at "$900–$1,900/mo, `on-request`/insurance-set."
   The panel found manufacturer-direct access paths that appear far below that retail/
   insurance-set frame. Primary Novo/Lilly pages are needed before quoting exact numbers.
3. **The premium-up-tier framing may be breaking.** Branded was framed as the gated tier
   above a compounded floor; the panel found signs that manufacturers are selling direct
   and courting telehealth channels. Treat the partnership/pivot specifics as leads until
   primary sources are captured.

**The minimal monitor that would have caught all three:** three narrow, datable,
*category-level* source types —

| Watch | Canonical source | Cadence |
|---|---|---|
| Compounding legality | FDA shortage list / 503A–503B bulks-list actions / warning letters | event-driven, ~monthly check |
| Branded cash-pay floor | NovoCare price guide PDF; LillyDirect/pricinginfo.lilly.com terms | monthly |
| Brand-channel pivots | one news query (GLP-1 telehealth branded partnership / compounding) | monthly |

None of these is a single `store/<domain>/`. The highest-consequence one (FDA status)
has **no company home at all**. That is the system-test finding (below).

## Evidence Used

- **Run 000 `read.md` + `run-notes.md`** — the baseline being stress-tested; it had already
  flagged the branded tier as "the live edge… where a freshness/Signal layer would earn its
  keep." This run supports that prediction directionally, but does not yet quantify it.
- **Live external panel (captured 2026-06-19)** — FDA compounding actions (pharmacytimes,
  medpagetoday, safemedicines, natlawreview); manufacturer direct-pay pages (NovoCare PDF,
  pricinginfo.lilly.com, investor.lilly.com, CNBC, prnewswire); brand-pivot news (Yahoo,
  financialcontent, Reuters). Full cites + dates in the panel receipt.
- **No store re-capture, no `store.py` pass** — this run does not re-derive the cohort; it
  asks what *outside* the store moves the stored answer.

## Companies Seen

This run is event-scoped, not cohort-scoped. The actors that move the read are mostly
**not** the DTC telehealth brands Run 000 enumerated:

- **Regulators / non-company:** FDA (shortage list, 503A/503B bulks list, warning letters).
- **Manufacturers (the cheaper branded channel the cohort capture misses):** Novo Nordisk
  (NovoCare / Wegovy / Ozempic), Eli Lilly (LillyDirect / Zepbound), + Walmart retail pickup.
- **Cohort brands appearing as *event subjects*:** Hims & Hers and Noom showed up in
  brand-pivot news leads. Both are in the Run 000 store list.

## Missing / Stale Coverage

- **The manufacturer-direct channel is structurally invisible to the cohort read.** Novo/Lilly
  direct-pay paths are not "telehealth companies," so a cohort built from DTC-brand pages
  may miss the cheapest real branded access path. The store isn't *wrong* on the brand pages
  — it's blind to a parallel channel.
- **Run 000's branded-price frame may be stale** and its compounded-floor premise may be
  eroding. The *visibility* finding (33/42/25 publish/floor/gate) may still be roughly true;
  the *price-architecture* narrative needs primary-source re-check.
- **Store GLP-1 captures (May 30–Jun 18 2026) are fresh** — but freshness of a capture ≠
  freshness of the *synthesis*: the read decayed faster than the data did, because the
  decaying facts (legality, manufacturer pricing) aren't captured per-company at all.

## Source Gaps

- This run **needed external sources** — the inverse of Run 000, which found the store
  out-completed its external denominator. Here the question is explicitly about exogenous
  events, so an external panel is load-bearing by construction, not by completeness anxiety.
- The panel was deliberately tiny (3 source types). Resisting "broad GLP-1 news digest" was
  the main discipline; the guardrail held.

## External Completeness Check

Not applicable in the denominator sense (no cohort census this run). The relevant
completeness question is **channel** completeness, not company completeness: a cohort read
assembled only from DTC-brand pages is structurally incomplete on manufacturer-direct and
regulatory facts no matter how many brands it captures.

## Market Pattern

- **The price gap that justified compounding may be closing from both sides.** Manufacturer-
  direct branded access appears to be moving down while compounded access is being squeezed.
  That is the strategic lead; exact price and partnership claims need primary-source follow-up.
- **State decays at the rate of its fastest-moving input.** Run 000's slowest-moving finding
(who *publishes vs gates*) is likely more durable; its fastest-moving finding (branded
*price* and compounding *legality*) needs re-check quickly. A market read inherits the
half-life of its most volatile claim — and here that claim is exogenous.
- **The volatile inputs are category-level, not company-level.** One FDA action and two
  manufacturer pages move the whole cohort at once. That is cheaper to monitor than N
  brands — but it has no per-domain home in today's Signals layer.

## What Would Change This Answer

- **FDA reversal or court stay** re-opening 503B compounding would re-floor the category on
  compounded and slow the branded pivot.
- **Manufacturer price moves** (NovoCare/LillyDirect raising or cutting again — both have
  moved twice in <12 months) shift the branded floor monthly.
- **If the engine decides monitoring is a consumer/project job**, not engine Signals, then
  "no new primitive" is the right call and this read just argues for a documented panel
  convention — see the triage submissions in `run-notes.md`.
