# Scout

## Prior Context Read

- `learning/lessons.md` / `learning/observations.md` (context, not a question queue):
  L001–L006 read. L005 (`query-time-grouping-enough`) and L006 (price-visibility token
  grain, `proposed`, awaiting 2nd entity-type beyond marketplaces — run-037 S2/DR3
  arguably supplies it) are the live decision surfaces. Observation stream is heavily
  `schema-edge-entity-type` + `denominator-reconciliation` + `relation-pressure` from
  runs 036–039. `denominator-reconciliation` (industry ≠ entity-shape cohort key) is now
  n=3 (036 G3, 037 G2, 039 DR1/S2).
- `scout-context.md`: two-test selection (value/reach + design); select for reader value,
  reach, source-family diversity, calibration — **not** store-answerability. Gap-probes
  first-class with a bounded plan.
- Last 3 `run-notes.md` files (037, 038, 039): all store-only; 036–039 are a tight
  **schema-fit / entity-shape cohort** streak (marketplace, wearable, SaaS neighborhood).
  Run 040 (bounded-live GLP-1 state availability) stalled at `needs-human-review`.
- Current run artifacts, if resuming: fresh scaffold (run 041).

**Landscape read:** the recent batch over-samples one shape — "does the universal schema
fit non-telehealth entity type X" — store-only, n=4 consecutive. Under-served value jobs:
**trust the cache over time** (freshness/change-pulse, last touched store-only at 018/032)
and **hand off in 5 seconds**. Under-sampled substrate: the retained dated raw captures
(`store/<domain>/captures/<date>/`), which ~22 domains carry 2–4 of and which no recent
run has used as a diff source. Selecting to break the streak toward a fresh builder lens
(persistence boundary) with real reader value, store-only safe.

## Candidate Questions

Scout should select for reader value, reach, source-family diversity, and roadmap
learning. Do not prefer a candidate merely because the store can already answer it.

| Question | Mode | Autonomous eligible? | Evidence mode | Why this is worth a run | Builder lens / design test | What it reaches / probes | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|---|---|
| **C1.** For brands with 2+ dated captures retained under `store/<domain>/captures/`, can a reader reconstruct what market-relevant State (pricing, offers, positioning) *changed* between two captures — and does the synthesized `profile.md` preserve any of that change, or does snapshot-overwrite erase it? | gap-probe | yes | store-only | Directly serves "trust the cache over time" — the literal "what's new since last look" question a returning reader asks. Breaks the schema-fit streak. | **Persistence boundary**: State overwrites (per architecture); the only change-pulse substrate is raw captures, which are unsynthesized. Tests whether the store can answer change-pulse *without* a Signals/diff primitive. | Whether retained raw captures are a usable diff source, or whether overwrite has already erased the comparison; whether `profile.md` prose ("resolves prior capture's…") is a reliable change channel. | Per-brand grep across two dated capture dirs (homepage/membership/pricing pages); `profile.md` `unverified_fields` + `site_notes` for in-prose change notes. | Claiming "nothing changed" when the prior capture simply wasn't retained at the needed page grain → "not found," not "not there." Conflating capture-method noise (proxy/markup drift) with real market change. |
| **C2.** Across all captured DTC consumer brands regardless of vertical, which monetize via a membership/subscription wedge, and can one query draw that cohort or does it need per-vertical judgment? | value-read | yes | store-only | A strategist's real cross-vertical pattern question; tests the n=3 industry-key blindness on a positive-draw cohort. | denominator-reconciliation — is `business_model: Subscription` a robust cross-vertical key or a coverage artifact? | 4th sighting of industry/model ≠ entity-shape key, this time cross-vertical not within one. | `business_model` + `offering_category` grep store-wide; spot-check prose. | Recurrence of an already-n=3 thread with little new — risks executing a parked observation rather than reaching. |
| **C3.** Take 3–4 captured brands across verticals; do their `render.py` briefs "land with a creative director in 5 seconds" — what survives the 5-second skim and what's noise? | calibration | yes | store-only | Tests the live "hand off in 5 seconds" job against the named consumer (Scott Witt). | Presentation layer — is the brief the right 5s artifact, or is State-rich ≠ skim-ready? | Consumer value frontier directly, not a schema question. | Render briefs; judge against the 5s bar. | Thin engine/design payload — more a presentation critique than a market-read; risks no durable learning. |
| **C4.** For the captured watch cohort (Rolex, Patek, AP, Lange, Cartier, Swatch, Casio), which brands do third-party "best luxury watch brands 2026" listicles/SERPs name as default, and how does that named set compare to the store's watch slice? | gap-probe | yes | bounded-live | Source-family diversity — every bounded-live run so far is GLP-1/telehealth; this tests the coverage-radar recipe (L001) on a non-telehealth vertical. | source-panel — does the SERP→listicle→store-diff recipe generalize off telehealth? | Whether L001's coverage radar is telehealth-overfit. | SERP + ≥2 authoritative listicles, store token-match diff; tight light ceiling. | Unattended bounded-live risk — 040 just stalled at needs-human-review; listicle quality for luxury watches may be ad-laden. |
| **C5.** Across the store, what do `unverified_fields` systematically flag (price ambiguity, conflicting counts, scope caveats), and can a reader filter high-confidence vs hedged State at query time? | calibration | yes | store-only | Trust-surface read; would tell a downstream agent which fields to relay confidently. | confidence-grain — is `unverified_fields` a queryable trust cut? | Whether the store's own hedge channel is machine-filterable. | Grep `unverified_fields` store-wide; categorize. | Overlaps run 031 (confidence-grain) — recurrence weak unless materially sharper. |
| **C6.** Of the ~22 domains with 2+ captures, which were actually *re-synthesized* (profile `captured_at` advanced) vs left on an old profile despite a newer raw capture — is there a synthesis-lag gap? | gap-probe | yes | store-only | Surfaces a freshness-integrity risk: a stale `profile.md` sitting on top of a newer raw capture. | freshness-monitoring — capture clock vs synthesis clock divergence. | Whether `captured_at` can be trusted as the freshness signal. | Compare profile `captured_at` to newest `captures/<date>/` dir per domain. | Narrow/meta — interesting to the builder, thin reader value alone; better folded into C1. |

## Selected Question(s)

1. **C1 — State change-pulse from retained captures** (primary). Strong reader value
   ("what changed since last look"), fresh builder lens (persistence boundary), store-only
   safe, breaks the schema-fit streak, and uses an under-sampled substrate (dated raw
   captures). C6 is folded in as a sub-check (synthesis-lag) since both read the
   capture-clock vs synthesis-clock relationship.

These are Scout recommendations until Brian or the operator confirms one.

## Selected Run Contract

This is the canonical handoff to Loop 1. If this block and the candidate table disagree,
Loop 1 should trust this block.

```yaml
selected_question: "For captured brands that retain 2+ dated raw captures under store/<domain>/captures/, can a reader reconstruct what market-relevant State (pricing, offers, positioning) changed between two captures, and does the synthesized profile.md preserve that change or does snapshot-overwrite erase it? Sub-check: do any domains carry a newer raw capture than their profile.md captured_at (synthesis lag)?"
selected_slug: state-change-pulse-from-captures
run_type: mixed
question_mode: gap-probe
autonomous_eligible: yes
evidence_mode: store-only
expected_denominator: "Store domains with 2+ dated capture folders under captures/ (top-level dated dirs, excluding _archive); ~22 by a first pass. Treat as partial until enumerated in Loop 1."
likely_source_panel: "Local only: store/<domain>/captures/<date>/*.md across two dates per brand; store/<domain>/profile.md (captured_at, unverified_fields, site_notes); architecture.md for the State-overwrite contract."
builder_lens: "Persistence boundary — State snapshots overwrite while the change-pulse a returning reader wants lives only in unsynthesized raw captures. Tests whether change-pulse is answerable from retained substrate without a Signals/diff primitive, and whether the capture clock and synthesis clock can diverge."
reach_reason: "Reaches past the comfortable single-snapshot read into whether the store can answer 'what's new since last look' at all — a value job (trust the cache over time) the recent schema-fit streak did not touch, using a substrate (dated raw captures) no recent run mined."
allowed_sources:
  - "store/ (profile.md, captures/<date>/, signals/ if present)"
  - "_design/2026-05-30-architecture.md and SCHEMA.md for the State/Signals contract"
  - "experiments/00-market-read-lab/learning/ (context only)"
disallowed_actions:
  - "No Firecrawl, scrape, crawl, or live browsing — store-only."
  - "No store/ mutation, write-back, or new capture."
  - "No durable primitive creation, no lesson proposal/graduation."
live_evidence_plan: null
approval_needed: no
why_autonomous_safe: "Answerable entirely from local store files (raw captures + profiles) and the architecture contract; no spend, no external sources, no mutation."
loop1_failure_mode: "Reading capture-method/markup noise (proxy or template drift between captures) as real market change; or claiming 'no change' when the prior capture simply lacked the page at the needed grain. Must say 'not found,' not 'not there,' and separate synthesis-lag (C6) from genuine State change."
```

## Selection Notes

Question-selection policy lives in `scout-context.md`. C2 was deprioritized as a 4th
sighting of an already-n=3 thread (low reach). C4 (bounded-live watch coverage radar) is
the strongest *reach-past-cache* alternative and the one to run next if a source-family-
diversity probe is wanted, but unattended bounded-live carries the 040 stall risk, so it
is not selected for this autonomous cycle. C1 wins on fresh builder lens + clean store-only
safety + streak-breaking value.
