# web-research — agent orientation

A project-agnostic **company-research engine** — Firecrawl captures, Claude reasons, a file-first store any project can query. Status + layout: [`README.md`](README.md).

## Read first, in order

1. [`README.md`](README.md) — what's here.
2. [`_design/2026-05-29-frame.md`](_design/2026-05-29-frame.md) — **why / scope / non-goals** (the Frame).
3. [`_design/2026-05-30-architecture.md`](_design/2026-05-30-architecture.md) — **how it works** end-to-end (capture lifecycle, consumption, relations).
4. [`SCHEMA.md`](SCHEMA.md) + [`TAXONOMIES.md`](TAXONOMIES.md) — the store contract (what a capture writes); [`QUERYING.md`](QUERYING.md) — how to read it back (what a consumer queries).
5. [`experiments/2026-05-29-query-affordance/FINDINGS.md`](experiments/2026-05-29-query-affordance/FINDINGS.md) — the proof that queryability is the product.

## Proven prior art (read before reinventing)

- **`~/.../agent-workflows/.claude/commands/competitor-watch.md`** — a working Firecrawl capture verb (map+scrape, two-pass homepage, key-page discovery, payload sidecars, Cloudflare/403 handling). The `/research-company` verb is a *generalized, single-company, lighter* version of this. Start here.
- **`agent-workflows/competitive-intel/INVARIANTS.md`** — hard-won Firecrawl quirks. Read before touching capture.
- **`agent-workflows/competitive-intel/scripts/prune-payloads.py`** — progressive payload pruning to adapt.
- **`firecrawl-map`** skill (global) — the map step, already available.
- **Doro `…/web_search/nav_extraction/`** — proven structured-nav extraction (informs the Nav section + `key_pages`).
- **Doro `…/core/schemas/companies.py`** — the full field menu (SCHEMA/TAXONOMIES are already distilled from it).

Full paths (local dev only — a cloud clone won't have these): agent-workflows = `~/Library/Mobile Documents/com~apple~CloudDocs/Text Files/Teleprescribe Venture/Teleprescribe Venture/agent-workflows/`; Doro = `~/Development/software/doro/doro/`.

## How we work here

- **Iterative, not one-shot.** Do a capture by hand on a few real companies first; codify the verb only once the pattern stabilizes. Run experiments in `experiments/<date>-<slug>/` to de-risk before building.
- **Spend on conventions, not infrastructure.** Markdown is the source of truth; any SQLite index is a *derived lens*, never authoritative.
- **Propose, don't write** across a project's boundary. The engine never silently mutates a project's KB.
- **The anti-Doro line:** no graph DB, embeddings, datapoint reconciliation, entity-resolution, or served API. Domain is the key. When a decision smells heavy, that's the flag.
- **Scope guideline:** the engine owns *state* (what a company/offering is). Events (news/funding/M&A) and judgments (relevance/threat) belong to downstream consumers.
- **Commit per logical change**, terse imperative subject (e.g. `schema: portfolio_shape replaces is_multi_product`). `git log` is the changelog — no CHANGELOG file.
