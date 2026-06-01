---
paths:
  - "_design/**"
  - "experiments/**"
  - "scripts/**"
  - "skills/**"
  - "BACKLOG.md"
---
# Working on the engine

The contract is [`SCHEMA.md`](SCHEMA.md) + [`TAXONOMIES.md`](TAXONOMIES.md); why/scope is the [frame](_design/2026-05-29-frame.md), how is the [architecture](_design/2026-05-30-architecture.md).

## Principles

- **Spend on conventions, not infrastructure.** Markdown is the source of truth; any SQLite index is a *derived lens*, never authoritative. Improvements to SCHEMAs and TAXONOMIES pays dividends down the line.
- **Iterative, not one-shot.** De-risk designs by running probes in `experiments/<date>-<slug>/` before baking in; Hand-capture a few real companies before codifying a verb/change.
- **The anti-Doro line.** No graph DB, embeddings, datapoint reconciliation, complex entity-resolution, or served API. When a decision smells heavy, that's the flag.
- **Engine owns state — not events or judgments.** What a company/offering *is*: yes. News/funding/M&A and relevance/threat/fit: no — those belong to downstream consumers.
- **Propose, don't write** across a project's boundary. The engine never silently mutates a project's KB.
- **Commit per logical change**, terse imperative subject. `git log` is the changelog — no CHANGELOG file.

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
- **Traction** (the engine's first-class *future* signal for market-maps) → `competitive-traction/` (`SCHEMA.md`, `signals/`, `cohort/`, `rollups/`). Read before building the aggregation / cohort layer.
