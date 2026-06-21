---
paths:
  - "_design/**"
  - "experiments/**"
  - "scripts/**"
  - "skills/**"
  - "tools/**"
  - "BACKLOG.md"
---
# Working on the engine

The contract is [`SCHEMA.md`](SCHEMA.md) + [`TAXONOMIES.md`](TAXONOMIES.md); why/scope is the [frame](_design/2026-05-29-frame.md), how is the [architecture](_design/2026-05-30-architecture.md). **Changing a contract? [`MAINTAINING.md`](../../documentation/MAINTAINING.md) is the blast-radius map — what moves downstream, and the gate to run after.**

Working on a large initiative / feature? Think about *what value* it creates by reading our [strategic-pillars](../../documentation/strategic-pillars.md), and consider *whose shoes* you stand in to feel it by reading our [personas](../../documentation/personas.md).

If you really need to put this into planning context, refer to the [Roadmap database](https://app.notion.com/p/getdoro/2362eca6edf441c18aaa7c0105c4cc23?v=38284b6d1f49805a84fd000cd5cb6768) in Notion. Long-form rationale lives in [Operating Principles](https://app.notion.com/p/38684b6d1f49806a8922e20061e644fa); this file is the short agent-facing rulebook.

## Operating principles

- **Amortize reasoning; meter capture.** Use Claude Code / Codex subscription reasoning for AI work; avoid paid API modes that wrap their own LLM reasoning when a skill can do it. Firecrawl, SerpApi, and repeat capture are scarce: cache aggressively, capture once, and refetch only stale or earned work.
- **Markdown / JSON are truth; derived lenses are disposable.** Markdown is authoritative for agent-readable synthesis; JSON is right for envelopes and telemetry with no prose body. SQLite, rendered HTML, dashboards, and indexes regenerate from files; never make them authoritative.
- **Conventions are infrastructure; queryability is the product.** Frontmatter, bold-led lines, clocks, `captured_at`, `unverified_fields`, paths, closed sets, and lint gates are the system. Every field is a cut: add it only when it divides a real question and can be filled reliably; derive anything free.
- **Capture once; structure at ingestion; query before re-fetching.** The expensive AI step turns raw evidence into reusable structure. Later reads filter the store first, then use focused source tools when fresh external evidence is needed.
- **Engine owns State and Signals; Judgments stay segregated.** State snapshots overwrite; Signals append; viewer-relative verdicts stay project-side or in a physically separate overlay when earned. Preserve grain so page/SKU/query/company facts cannot masquerade as each other.
- **Evidence, not scores.** Store verbatim anchors, axis-specific deltas, caveats, and disagreement. No blended numbers, no generic market scores, no price magnitude fields that launder messy strings into false precision.
- **Fail loud before silently wrong.** A veto row, `unverified_fields`, lint failure, warning, or explicit absence beats a clean-looking artifact with hidden bad data. Before claiming a negative, check what was captured and what was missed.
- **Verbs and skills over services.** Package repeatable work as slash commands, agent skills, scripts, or routines that start, write evidence, and stop. Code is welcome; living infrastructure is not. The flag is anything that must keep running to stay true.
- **Frame first; experiment before build.** On big or fuzzy work, separate problem-space from solution-space before proposing an implementation. Probe in `experiments/<date>-<slug>/`, hand-capture real cases, and persist runs before minting durable ontology or schema.
- **Least complexity; push back on additive fixes.** Hunt the simplest 80/20, ask what a new rule/helper/field replaces, and cut dead weight when improving docs, prompts, or code. Watch for overfitting a one-run retro into a general rule.
- **Propose, don't write** across a project's boundary. The engine may produce structured proposals for a project KB; it never silently mutates another source of truth.
- **Commit per logical change**, with a terse `scope:` subject and detail in the body — see [commit-style](../../documentation/commit-style.md). `git log` is the changelog — no CHANGELOG file.

## Prior art — mine it, don't reinvent it

Capture mechanics + Firecrawl quirks are already distilled in-repo at [`firecrawl-capture.md`](skills/research-company/firecrawl-capture.md) — the capture playbook that ships with the `/research-company` skill (it reconciles agent-workflows' `competitor-watch` + `INVARIANTS`). Beyond capture, two prior systems solved pieces of this — read the relevant one before designing, then keep ours lighter.

**Doro** — the VC-era PE tool whose weight we refused; mine its schemas, refuse its machinery. Base: `/Users/brianbolze/Development/software/doro/doro` (*local dev only — a cloud clone won't have it*). Paths below are relative to that base:

- **Design insights**: `docs/tech-blog-post.md`; "AI at ingestion" principle.
- **Field menu** (adding or changing a field) → `core/src/core/schemas/companies.py`; **closed sets** → the `core/src/core/schemas/categorical_fields/` package (`industries.py`, `offering_categories.py`, `lifecycle_categories.py`, `feature_taxonomy.py`). SCHEMA/TAXONOMIES were distilled from these.
- **Offerings design** → `core/src/core/schemas/products.py` + `core/src/core/schemas/research/product_datapoints.py`.
- **key_pages / nav extraction** → `services/app/src/app/services/web_search/nav_extraction/` (html_reduction → llm_extraction → nav_formatter).
- **The swamp we refuse** → `RECONCILIATION_EXAMPLE.py` + `services/algos/src/algos/services/reconciliation/` (configs, consistency, time_weighting): the datapoint-reconciliation + entity-resolution weight the anti-Doro line rejects. Read it to remember *why* domain-as-key deletes the problem — not to port it.

**agent-workflows** — the Teleprescribe substrate this engine generalizes from; mine its working patterns. Base: `~/Library/Mobile Documents/com~apple~CloudDocs/Text Files/Teleprescribe Venture/Teleprescribe Venture/agent-workflows` (*local dev only — a cloud clone won't have it*). Paths below are relative to that base:

- **Operations vocabulary** (Capture / Enrichment / Synthesis / Promotion) → `ARCHITECTURE.md` — the origin of the [architecture](_design/2026-05-30-architecture.md) doc's ops model.
- **Promotion / propose-don't-write** → `competitive-intel/PROMOTION.md` + `promotion-ledger.md`: the graduation-threshold loop (N consecutive `accepted-as-is` → auto-fill; opinionated fields stay propose-only forever). The prior art for the engine's step-8 Promote.
- **Traction** (the engine's first-class *future* signal for market-maps) → start with the in-repo [traction frame](_design/2026-06-14-traction-frame.md), which supersedes this pointer. It names the current primary prior art — the **live** Teleprescribe `traction v2` layer (`research/competitive/mine/traction/v2/`, off the Teleprescribe root, *not* this `agent-workflows` base) — and treats the older `competitive-traction/` as deprecated: mine it, don't port it. Read it before building the aggregation / cohort layer.
