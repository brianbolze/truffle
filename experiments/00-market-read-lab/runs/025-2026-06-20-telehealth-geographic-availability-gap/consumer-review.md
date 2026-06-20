# Consumer Review

Question: **Where did Truffle create reader value, and where did it fall short?**

## Verdict

- **Valuable? Yes.**
- **Why:** On a never-before-read axis (place), the read returns a *protective* insight,
  not just an absence: it shows the store cannot answer "can I get this in my state?" as
  a query, explains exactly why (grain mismatch, not thin coverage), and surfaces the 9
  brands with real partial data at the correct grain. A gap-probe that prevents a harmful
  build decision ("just add an `available_states` field") is rarer and more useful than a
  falsely confident lookup.
- **Where Truffle added value:** the grain-mismatch finding (availability is **product ×
  state**, sometimes **audience × state**, never reliably brand × state); the two-way
  "all 50 states" confound; the honest not-found framing for the 29 silent brands.
- **Where it added little / fell short:** it *cannot* tell a real buyer whether they can
  get a treatment in their state for 45 of 54 brands — by design, store-only maps the gap
  but cannot fill it. The skim layer is weak (see below).
- **What the consumer can do now:** for the 9 disclosing brands, get the verbatim, cited
  state list/exclusion at the right grain; for everyone else, know the store can't say and
  why — and not be misled by "50 states" marketing.
- **Safer than generic Claude + web search?** Yes for *honesty* — it refuses to invent a
  per-state answer and labels claims as claims; a web search would surface brand
  marketing ("all 50 states!") at face value and miss the per-line exclusions.
- **Biggest limit:** the decision-grade answer needs each brand's own eligibility-gate
  page at list grain — a per-brand live surface the store doesn't hold.
- **Human follow-up needed:** none required; a human-gated `/deepen-offerings` sweep of
  the 9 disclosing brands' eligibility pages would convert prose → queryable lists, but
  that is a spend + TAXONOMIES decision.

## Value diagnostics

| Signal | What to look for | Evidence / gap |
|---|---|---|
| **Useful** | Decision aid, not a summary. | Yes — names the 9 disclosing brands + the design guardrail (no brand-level field). |
| **Judgment-ready** | Cited, rare ingredients. | Yes — verbatim state lists (joiandblokes 16, vitalityrx 25, hevahealth 45/30/50, niagenplus 7) with source lines. |
| **Sourced & cited** | Traces to files/dates; uncertainty visible. | Strong — C1–C10 local paths; claims labeled as claims, not truth. |
| **Deep enough** | Covers the set, not examples. | Yes — all 54 cohort brands partitioned exactly (9/2/8/6/29). |
| **Fresh enough** | Capture dates / staleness visible. | Yes — flags intrinsic staleness (struthealth "as of Sept 2024"; controlled-substance state law shifts). |
| **Kept / reusable** | Warm files for the next ask. | Yes — the per-line grain finding is a reusable guardrail. |
| **Shortfall mapped** | Names where Truffle can't support. | Strong — this *is* the result; the gap map is explicit. |

## Job fit

| Job | Did the read help? | Missing / next step |
|---|---|---|
| **Cold-start a company** | Honest orientation: availability not queryable, here are the 9 with real data. | — |
| **Compare a whole field** | Surfaces the only 9 brands with decision-grade disclosure, classified at the right grain. | Can't compare the 45 others on this axis (store-silent). |
| **Build on top without re-capturing** | The product×state grain + "no brand-level field" guardrail is directly actionable for a future builder. | Per-line verbatim depth-backfill if the axis ever earns it. |
| **Trust the cache over time** | Earns trust by labeling absence as not-found and decoding the "50 states" confound. | — |
| **Five-second brief input** | Partial — the verdict is clear but the skim layer is buried. | See lens check. |

## Lens check

- **Strategist:** lands, but slowly — the most protective finding ("a brand-level field
  would be false-precise") sits *third* in Market Pattern and the dense bullet breakdown
  precedes the glanceable gap-map table. A reader skimming could absorb "9 brands have
  data" and miss that those 9 aren't joinable. Surfacing the grain guardrail higher would
  fix it. *(Logged as a synthesis-shape note, not a triage item — one sighting.)*
- **The Pantry / downstream system:** strong — stable cited state lists, visible
  freshness, judgments clearly labeled; a downstream agent could reuse the 9 brands'
  verbatim lists without re-browsing.
- **First Contact:** yes — the henrymeds `unverified_fields` self-flag and the
  not-found discipline make the store's behavior trustworthy.

## Optional triage evidence

No new consumer-side triage item. The hand-off-in-5s / skim-layer weakness is a
**single-sighting synthesis-shape observation** (preserved in `discovery-ledger.md` as a
value-miss), not yet a recurring pattern that warrants a template change. The substantive
backlog evidence (MRL-014, MRL-008 addend) is carried by the developer review.

**Do not graduate or implement system changes.**
