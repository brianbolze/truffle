# Backlog

System-level weaknesses, ideas, and TBDs for the engine itself. Light-touch — 1–3 bullets each, no formatting ceremony. A living, curated list (not an append-only log).

**This is the *system* learning home.** Per-company capture learnings live in that company's `site_notes` (in `profile.md`), not here. This file is for things that would change the engine, schema, or workflow.

**Not this file:**
- [`SCHEMA.md`](SCHEMA.md) / [`TAXONOMIES.md`](TAXONOMIES.md) — the store contract. Hard rules that cost a real lesson go here as one-liners, not as backlog items.
- [`_design/`](_design/) — frame, architecture, references. Durable intent.

**Tags:** `[weakness]` design gap likely to bite · `[idea]` possible improvement · `[bug]` confirmed defect · `[tbd]` pending decision · `[simplification]` a way to *remove* surface area.

**Bias check.** Default is to add; resist it. Before logging an addition, ask: is there a way to *remove* or *consolidate* instead? Hunt `[simplification]`s at least as hard as features. If an entry adds surface, note what existing surface it would replace.

**Graduation.** When an item has a clear next action, move it to a `_design/` doc or just do it. Don't graduate to clear the list — most items should sit until a real capture confirms them (≥2 sightings).

**Soft cap: ≤15 open items.** Over that, close/cut/promote 2 before adding 1. Stale items (>60 days, untouched) default-cut on the next review.

---

- **Working name "web-research" not final** `[tbd]`
  Decide before it's load-bearing in skills/paths/remote. "Market Intelligence" is the aspirational name; keep the humble one until the map layer ships.

- **Rung-3 SQLite index — not yet** `[idea]`
  Build the derived index only when relations (discovery) or time-series (traction) first demand it. Markdown is the source of truth; the index is a regenerable lens. Don't build ahead of a real query.

- **`offerings.md` / `brand.md` schemas deferred** `[tbd]`
  Tier-1 module schemas land when the first project enables them. `offerings.md` seed: [`_design/references/doro-product-analysis-prompt.md`](_design/references/doro-product-analysis-prompt.md).
