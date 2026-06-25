# Scout

## Prior Context Read

- `learning/lessons.md` / `learning/observations.md` (context, not a question queue):
  Recurring **relay-risk** thread — source-rigor protection (`unverified_fields`,
  "self-reported" prose flags, price-visibility token, point-in-time/sale caveats) is
  **prose-grade and relay-dependent**: it only protects the reader "if the downstream
  agent preserves it" (038-R1, 042-S1/R1/CR2, 046-G2, 048-S3; L002/L004). Never tested
  against the *actual* presentation surface. Also: 13 of the last 14 runs (036–048) are
  store-only schema-fit/cohort reads → schema-fit streak worth breaking.
- `scout-context.md`: select for value + reach + roadmap learning, not store-answerability;
  gap-probes first-class with a bounded plan; name the builder lens.
- Last 3 `run-notes.md` files (046/047/048): 047 bounded-live had a 1-credit spend breach
  (R1/DR1 → variable-cost-format class risk); 048 store-only traction read landed
  "map-not-ingredient." Both reinforce that the relay/synthesis surface, not capture, is
  the live frontier.
- Current run artifacts, if resuming: fresh scaffold.

## Candidate Questions

Scout should select for reader value, reach, source-family diversity, and roadmap
learning. Do not prefer a candidate merely because the store can already answer it.

| Question | Mode | Autonomous eligible? | Evidence mode | Why this is worth a run | Builder lens / design test | What it reaches / probes | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|---|---|
| **(SELECTED)** When the human-facing brief is generated via `scripts/render.py`, does the rendered HTML faithfully carry each profile's source-rigor flags (`unverified_fields`, self-reported/honest-flag prose, the price-visibility token, point-in-time/sale caveats) into the 5-second handoff — or does rendering launder them away? | gap-probe | yes | local-existing | First test of the recurring relay-risk thread (L002/L004; 038/042/046/048 R-rows) against the *actual* relay. The brief is the surface a creative-director/Scott-Witt consumer + a delegated agent actually read. | Presentation layer (`scripts/present/`): does the regenerable lens preserve the flags the markdown source-of-truth carries, or silently drop them? Persistence-boundary + source-rigor on the synthesis surface. | Reaches past "the markdown holds the flag" (true store-wide) to "does the consumed artifact show it." Breaks the schema-fit streak. | Run `render.py` on a flag-heavy panel; diff rendered HTML text vs `profile.md` flag lines. No external. | Treating one company's render as the store-wide behavior; conflating "absent from brief" with "absent from a tab a human could expand." |
| Have the store's most volatile captured prices (GLP-1 monthly, wearable device sale prices) actually drifted since capture — how stale is the cache in practice? | gap-probe | no | bounded-live | Real "trust the cache over time" test with live ground truth; never done. | Persistence boundary for market-sensitive fields; is freshness machinery motivated at this cadence? | Live price re-check vs captured State. | Brand pages re-captured (plain markdown only). | **Spend risk unattended** (047 R1/DR1 breach class); A/B/promo noise. Deferred — not unattended-safe this cycle. |
| For an unfamiliar company, which *ingredient type* is the weak link in a 5-second handoff (what/sells/charges/proof/whitespace)? | calibration | yes | store-only | Reader-value for the brief consumer. | Which ingredient type the synthesis surface under-serves. | Modest — likely re-derives 038's ingredient-type-shaped grounding finding. | Store profiles. | Low marginal learning vs 038. |
| Across the store, can `parent`/`owns` frontmatter draw a self-consistent ownership/consolidation map, or does it disagree with itself (039-G3 Coda chain)? | gap-probe | yes | store-only | Vertical-relation reliability as a market-structure read. | Cross-profile reconciliation of the one structured relation primitive. | Recently adjacent (026 ownership map; 039-G3). | Frontmatter grep. | Repeat of 026/039 shape. |
| Is `denominator-reconciliation` (industry-draw ≠ entity-shape cohort, n=4) now a graduation-ready pattern across a fresh 5th cohort? | calibration | yes | store-only | Calibrates a recurring n=4 sighting. | Cohort-key reliability. | Low reach; risks lesson-closure originating the question. | Store grep. | Lesson-closure driving the question (scout-context "Avoid"). |
| Does `visual.md` add buyer-load-bearing signal over the `Visual & brand impression` already in `profile.md` (045-S4)? | calibration | yes | store-only | Tests module redundancy. | Persistence boundary: does the opt-in module earn its keep. | Modest. | Store profiles w/ + w/o visual.md. | Single-cohort artifact. |

## Selected Question(s)

1. **render-relay flag fidelity** (candidate 1) — the relay-risk thread has recurred
   across ≥5 runs as a *prose-grade, relay-dependent* protection; this is the first run
   to test it on the literal relay (`render.py`). Local-existing, no spend, autonomous-safe,
   and it breaks the store-only schema-fit streak with a presentation-layer probe.

## Selected Run Contract

This is the canonical handoff to Loop 1. If this block and the candidate table disagree,
Loop 1 should trust this block.

```yaml
selected_question: "When the store's human-facing brief is generated via scripts/render.py, do the rendered HTML briefs faithfully carry each profile's source-rigor flags — unverified_fields, self-reported / honest-flag prose, the price-visibility token, and point-in-time / sale price caveats — into the 5-second handoff surface, or does rendering launder them away?"
selected_slug: render-brief-flag-fidelity
run_type: system-test
question_mode: gap-probe
autonomous_eligible: yes
evidence_mode: local-existing
expected_denominator: "A small purposive panel (~5-6) of flag-heavy captured profiles drawn from recent runs: remedymeds + henrymeds (self-reported rating / inconsistent member counts), sorafuel or electra (present-tense description over-claim + milestones), etsy (house-of-brands GMS in unverified_fields), euclidpower (page-conflicting metrics in unverified_fields), therabody or hyperice (sale-snapshot price). Panel is illustrative of flag types, not a census."
likely_source_panel: "Local only: scripts/render.py output (_out/briefs/<slug>.html), store/<slug>/profile.md, scripts/present/ source, SCHEMA.md (price-visibility token), modules/VISUAL.md if relevant."
builder_lens: "The presentation layer (scripts/present/). Tests whether the regenerable HTML lens preserves the source-rigor flags the markdown source-of-truth carries, or silently drops them — a persistence-boundary + source-rigor test on the synthesis/handoff surface, the literal relay the recurring relay-risk rows depend on."
reach_reason: "Tests the recurring relay-risk thread (prose-grade flags travel only if the downstream reader carries them) against the actual artifact a human/agent consumes, instead of re-confirming the markdown holds the flag. New object (render output) never read in a run; breaks the 036-048 store-only schema-fit streak."
allowed_sources:
  - "store/ (profile.md and module files for the panel companies)"
  - "scripts/render.py and scripts/present/ (run + read the renderer)"
  - "_out/briefs/ (generated HTML output, this run)"
  - "SCHEMA.md, TAXONOMIES.md, modules/VISUAL.md (flag contracts)"
  - "experiments/00-market-read-lab/ (lab artifacts)"
disallowed_actions:
  - "No Firecrawl / SERP / external network capture; no paid credits."
  - "No live browsing of company sites."
  - "No store/ mutation; no edits to scripts/ or render output beyond generating briefs into _out/."
  - "No write-back, durable primitive creation, or learning/ lesson edits."
live_evidence_plan: null
approval_needed: no
why_autonomous_safe: "Entirely local: runs a repo script (render.py, with --no-fetch to avoid remote logo/font fetches) over already-captured store files and diffs the output against profile.md. No external network, no spend, no mutation of source-of-truth."
loop1_failure_mode: "Generalizing from one company's render to store-wide behavior; conflating a flag's absence from the brief with its absence from an expandable section; mis-reading a render omission as a profile gap (check profile.md carries the flag first)."
```

## Selection Notes

Question-selection policy lives in `scout-context.md`. Candidate 2 (live price-drift
check) is the strongest *reader-value reach* but is **not unattended-safe this cycle**:
the last two bounded-live runs hit spend friction (040 blocked, 047 1-credit breach over
the variable-cost-format class), so a live panel run unattended carries avoidable spend
risk — deferred to an attended cycle. The selected candidate gets the relay-risk reach
with zero spend by reading the local presentation surface. Candidates 3/5/6 scored lower
on reach (low marginal learning vs 038, or lesson-closure originating the question).
