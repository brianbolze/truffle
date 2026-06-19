# Run Notes

> **Historical run notice:** This run predates the current autonomous contract. Use it
> for evidence and pressure patterns only; do not copy its header, stage behavior,
> receipt rigor, or artifact shape. Current conventions live in
> `experiments/00-market-read-lab/templates/`.

```yaml
pressure_lenses_fired: [relation-already-a-primitive, query-time-grouping-enough, claim-not-truth, named-is-the-minority, supplier-concentration-radar, coverage-caveat]
```

## 30-second operator read

- **Did it work? Yes — store-only, no scraping, no spend.** Every edge came from three layers
  already in the store: `parent`/`owns` frontmatter, the `telehealth.md` **Fulfillment**/**Provider**
  body lines, and a grep for the named counterparties across the corpus.
- **What was awkward?** The relation data is **half in frontmatter (parent/owns, joinable) and half in
  prose (pharmacy/clinical claims, not)**. There's no single field to filter on for "who does X depend
  on" — you read frontmatter *and* grep bodies, then dedupe by hand.
- **What the next agent should know:** the honest headline is **"relations are load-bearing but mostly
  already captured."** Parent = `parent`/`owns`; integration = `pharmacy_model`. The *only* new pressure
  is a **named supplier/clinical edge**, and it's named in just 5/18 (pharmacy) and ~3/18 (clinical) —
  too sparse to typecast. Resist the urge to build a relations table off this run.

## What happened

Scoped the men/hormone slice of the telehealth packs (18 brands: `audience ∈ {men-only, men-first}`
∪ `anchor_category ∈ {TRT, sexual-health, peptides}`). For each, pulled `parent`/`owns` from
`profile.md` frontmatter and the **Fulfillment** + **Provider** lines from `telehealth.md`. Sorted the
relations into three edge types (parent/front-door · pharmacy · clinical), then grepped the *whole*
corpus for the named counterparties (OpenLoop, Curexa, Strive, Hallandale, affiliated-P.C. language)
to check recurrence and confirm they resolve to existing store profiles. Applied a load-bearing test
(does the edge change the market read?) to each type. Wrote `read.md` + the worksheet receipt.

## Inputs and scope

- Store slices: `store/*/telehealth.md` (54 packs; 18 in the men/hormone working set),
  `store/*/profile.md` frontmatter (`parent`/`owns`), supply-side profiles (openloophealth-com,
  mdintegrations-com, strivepharmacy-com, hallandalerx-com).
- Queries: PyYAML frontmatter parse for the cohort cut + parent/owns; `sed` extraction of the
  Fulfillment block; `grep -ril` across the corpus for named counterparties.
- Working set, **not a denominator** — the question is edge-structure within a known set, so no
  external panel and no census. honehealth / invigor / home-medvi pulled in for relations only.

## Friction log

- **Relations live in two places with two shapes.** `parent`/`owns` are clean joinable frontmatter;
  pharmacy/clinical partners are **prose claims** in the body. Answering "what does brand X depend on"
  means reading structured + unstructured and reconciling by hand. This is the run's main ergonomics note.
- **No in-degree view for backend counterparties.** `store.py relations` joins `parent`/`owns`, but the
  pharmacy/clinical edges aren't in frontmatter, so "which pharmacy is behind the most brands" is a manual
  grep-and-tally. That's *fine* at this sparsity — flagging it, not asking to build it.
- **Ownership claims are a footgun for relation extraction.** "Our pharmacy" / "our own" reads like an
  `integrated`/owned edge but is often marketing over a third party (BlueChew names three). Any future
  typed edge must record the **named entity or the absence**, never the possessive adjective.

## Evidence limits

- **Pharmacy entity named in only 5/18; clinical group in ~3/18.** "Not named" ≠ "no partner" — most
  brands simply don't publish the counterparty. Absence is a capture-grain fact, not a structural one.
- **Page-attested claims, never adjudicated.** The store records "we own our pharmacy"; it cannot tell you
  whether that's true. BlueChew is the live proof the claim and reality diverge.
- **Clinical-provider is the thinnest layer** and arguably the most decision-relevant for regulated care —
  the evidence is weakest exactly where a typed edge would matter most.

## Surprises

- **The parent edge was the strongest *and* the most already-solved.** Going in, "relations" felt like a
  candidate new primitive; the clearest load-bearing case (RexMD→LifeMD) is **already** `parent`/`owns`
  and was **already surfaced in Run 0**. The run mostly *confirms an existing primitive*, not motivates a new one.
- **The shared backends are already in the store.** OpenLoop, MDIntegrations, Curexa, Strive, Hallandale
  are all profiled — and Strive/Hallandale *recruit provider networks*, the B2B mirror of the DTC edge. So
  the typed-edge question is really "do we want joinable supplier edges?", and the *targets already exist*.
- **`pharmacy_model` quietly absorbs most of the pharmacy question.** The integrated-vs-third-party posture
  carries the decision weight; the entity name adds value only under shared-supplier concentration.

## Pressure lenses

"No new *primitive* needed yet" is the honest headline — but unlike Run 0, this run *does* leave a
non-trivial typed-edge candidate on the table (named supplier/clinical edge), held back only by sparsity.

- **`relation-already-a-primitive` (NEW) → NO new primitive for parent/ownership.** The load-bearing edge
  (parent/front-door) is already `parent`/`owns` frontmatter, joinable, and Run-0-confirmed. The run
  *validates* the existing relation fields rather than pressuring for new ones.
- **`query-time-grouping-enough`.** Supplier concentration ("which backend sits behind the most brands")
  is a query-time in-degree count over named edges — the `store.py relations` join already does this for
  `parent`/`owns`. No baked "one of only two who…" comparison belongs in a pack.
- **`claim-not-truth` (NEW).** Relation claims are marketing, not structure (BlueChew). Any relation layer
  must store the named entity/absence and adjudicate nothing — same trust line as the rest of the store.
- **`named-is-the-minority` (NEW).** The decisive caveat: pharmacy named 5/18, clinical ~3/18. A typed field
  this empty would mislead more than it helps — absence reads as "no relationship" when it means "not captured."
- **`supplier-concentration-radar`.** The latent useful finding — a few B2B backends behind many DTC brands —
  is the relation question's real payoff, but it needs more named edges before it's measurable.
- **`coverage-caveat`.** "Not named ≠ no partner" / "not captured ≠ not offered" recurred throughout; the
  standard caveat language is load-bearing here too.

### Note on the pressure-lens framing

This run is the **relation counterpart** to Run 0's pricing-visibility read. Both land on
"query-time-answerable over existing layers, don't build State" — but this one is closer to the line: a
named supplier/clinical edge is a *defensible* future primitive, gated purely on capture sparsity, not on
"it's query-time so never." Worth watching whether a later cohort (where brands name backends more often,
e.g. compounding-heavy GLP-1) flips `named-is-the-minority` and earns the edge.

## Triage submissions

Queue submissions only; none graduated or approved for implementation by this run.

- **[P2 · Submitted] Named-supplier / clinical relation edge — candidate, hold for recurrence.** A typed
  `fulfilled_by` / `clinical_provider` edge from a DTC brand to a **store-resolvable** pharmacy / clinical
  network (Curexa, Strive, Hallandale, OpenLoop, MDIntegrations). *Why submit:* the counterparties are
  already profiled, so the edge joins; supplier-concentration is a genuinely useful market read. *Why not
  graduate:* named in only 5/18 (pharmacy) and ~3/18 (clinical) here — too sparse; the load-bearing parent
  edge is already `parent`/`owns`, and integration posture is already `pharmacy_model`. Re-check on a
  cohort that names backends more often before acting. Links MRL-001 (denominator) loosely; leans on the
  existing QUERYING Recipe 3 relations join, not new infra.
- **[P3 · Submitted] Clinical-provider capture-grain gap.** Most brands name no medical group ("licensed
  providers" only); the few named P.C.s (Wasef, CareGLP) show the grain *can* be captured. If clinical
  relations become load-bearing, this is a **capture-depth** ask (pull the affiliated-P.C. entity during
  capture), not a primitive. One sighting — watch for recurrence.
- **[No-op] No new relation primitive for parent/ownership.** Confirmed already covered by `parent`/`owns`
  + `pharmacy_model`; Run 0 already surfaced the canonical case (RexMD↔LifeMD).

## Next-run advice

- For relation reads, pull **`parent`/`owns` frontmatter AND grep `telehealth.md` Fulfillment/Provider
  lines** — the edge data is split across structured + prose. Don't expect one filter.
- **Trust the named entity or the absence, never the possessive.** "Our pharmacy" is marketing; reconcile
  against the named third parties in the same page.
- To test the supplier-edge candidate properly, run it on a **compounding-heavy GLP-1 cohort** where brands
  name pharmacies more often — that's where `named-is-the-minority` might flip and the typed edge earns its keep.
- The shared backends (OpenLoop, Strive, Hallandale, MDIntegrations) are the **mirror image** of the DTC
  brands — capturing their "provider partner network" pitch is the cheap way to see concentration from the
  supply side without re-capturing every DTC brand.
