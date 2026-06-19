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

If you really need to put this into planning context - refer to our [Roadmap database](https://app.notion.com/p/getdoro/2362eca6edf441c18aaa7c0105c4cc23?v=38284b6d1f49805a84fd000cd5cb6768) in Notion.

## Principles

- **Spend on durable conventions, not living infrastructure.** Schemas, taxonomies, and file layout earn the real investment. Markdown is the source of truth; any index (SQLite, …) is a *derived, regenerable lens* — never authoritative. Code is welcome — committed tools (`tools/`, `scripts/`) or one-offs alike; what we refuse is *living infrastructure* you must keep alive: a standing server, a hosted API, an authoritative database service. The flag is anything that has to keep running to stay true.
- **Iterative, not one-shot.** De-risk designs by running probes in `experiments/<date>-<slug>/` before baking in; Hand-capture a few real companies before codifying a verb/change.
- **Least-complexity, and push back.** Hunt the simplest 80/20 and cut what isn't essential; changes should try NOT to be *purely additive* — every edit earns a simplification pass (what can go?). Brian over-engineers by his own admission and *wants* the pushback, so challenge scope and say when simpler wins.
- **Frame before solution.** On anything big or fuzzy, don't lead with an implementation proposal — read enough to understand the territory, then ask a few (~4–6) high-leverage clarifying questions where a wrong assumption would waste real work, and wait. Flag any inferred assumption so it's cheap to correct.
- **Engine owns State and Signals; Judgments are the open edge.** *State* — what a company is now: universal fields plus reusable vertical/cohort cuts (a project designs the cut; the engine holds and serves it, no judgments in it). *Signals* — the same facts on a time axis: the reusable capture tools + comparator + the `scripts/signals.py` writer, landing append-only at `store/<domain>/signals/<source_type>/<captured_at>.json`. *Judgments* (relevance/threat/fit, relative to the asker) stay out of the shared store today — but whether and how the engine emits them is actively being reworked, not a closed "no." See the [frame](_design/2026-05-29-frame.md)'s three-kinds split.
- **The anti-Doro line.** No graph DB, embeddings, datapoint reconciliation, complex entity-resolution, or served API. When a decision smells heavy, that's the flag.
- **Propose, don't write** across a project's boundary. The engine never silently mutates a project's KB.
- **Commit per logical change**, with a terse `scope:` subject and detail in the body — see [commit-style](../../documentation/commit-style.md). `git log` is the changelog — no CHANGELOG file.

## Gotchas
- **Overfitting.** When making fixes, especially coming from backlog / feedback items from individual runs or retros - always ask whether the proposed solution is actually generalizable to all types of data / scenarios we may encounter.

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
