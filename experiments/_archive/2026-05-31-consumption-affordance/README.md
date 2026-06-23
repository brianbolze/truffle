# Consumption-affordance test — does a *cold* agent reach the structure unaided?

*2026-05-31. The [prior consumption test](../2026-05-31-consumption/) was run by the
experimenter **after** reading the contract — it proved the formats are queryable, not that a
consumer discovers them. This one isolates the predecessor's actual failure mode: an arbitrary
agent that lands on the store **cold** ("starts from scratch, never reaches for structure that's
already there"). The control is the point.*

## Hypothesis

If "queryability is the product," a genuinely cold agent — handed only a question and the store's
location — should discover the store + its contract on its own and answer correctly, cited, in one
pass, honest about what it can't answer. Where it can't, the **wall** is the finding (a next decision).

## Method — the cold control

- **Harness:** each probe is a fresh headless `claude -p` process (Opus), cwd = a sandbox copy of
  the store at `/tmp/web-research-consume`. The sandbox **excludes `CLAUDE.md` and `experiments/`**
  so the agent inherits **no** project orientation, no read-order, no memory index, and no answer
  leakage — verified by an introspection control ("no CLAUDE.md / no MEMORY / no read-order: yes to
  none"). This is why the in-repo `Agent` tool was *not* used: its sub-agents inherit this repo's
  `CLAUDE.md` (which says "read README → … → QUERYING.md") and are therefore **not cold**.
- **Prompt = question + store location only.** No mention of QUERYING.md, SCHEMA, grep-vs-YAML, or
  any method hint. Web tools (WebFetch/WebSearch) were left enabled to observe whether a cold agent
  re-scrapes a warm company.
- **Instrument:** `--output-format stream-json` captures the **ground-truth tool trace** (every file
  read, every grep, every network call, in order) — not just the agent's self-reported process log.
- **Primed re-run only on failure:** per the brief, a probe that fails cold would be re-run pointed
  at QUERYING.md; a primed-success localizes the gap to *discoverability*, not data. (Not needed —
  see FINDINGS; every probe found QUERYING.md unaided.)
- **Integrity note:** the first pass ran all 5 agents in parallel; 3 hit a *harness* flake — a
  final-step socket close (P1, P5) or tool-output-batching thrash (P2, the documented IO lag on this
  machine) under contention, not a store problem (their tool traces were valid and on-track). Those
  three were re-run **sequentially** (no parallelism) for clean answers; the traces matched the
  flaked runs. P3/P4 completed clean on the first pass. None of this touched what the agents *did* —
  only whether the final text rendered.
- **Probes (5 + 2), one per consumption path + stated limit:** point-read (Hims) · intra-cohort GLP-1
  price aggregation (flagship) · ill-posed cross-shape "best pricing?" · negative / not-offered-vs-
  not-captured (Function Health) · deep-research-as-consumer (Maximus: state + funding + threat).
  **Addendum 1 (P6–P7), the SaaS cohort as the only new variable:** cross-company price benchmark of the
  research/feedback/intelligence SaaS tools (does aggregation generalize? do *clean* published tiers
  stay queryable or collapse to narrative like telehealth's messy ones? can a cold agent sub-group a
  heterogeneous cohort the frontmatter can't?) · a relation probe (Qualtrics↔Delighted via
  `owns`/`parent`, QUERYING #3).
  **Addendum 2 (P8–P10), the luxury-watch cohort (physical goods, per-SKU/dealer):** point-read (Rolex,
  a no-published-price brand) · cross-cohort price aggregation · the price-*visibility* classification
  question — does *any* pricing field survive a third shape, or is the universal axis price visibility
  (published | on-request | partial), and does even that have to live per-offering not per-company?

Prompts in `_out/` (gitignored bulk); the analysis is in [`FINDINGS.md`](FINDINGS.md).
