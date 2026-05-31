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

- **Lint `profile.md` in the verify step** `[idea]`
  `verify` checks scrape md5-uniqueness but never lints the *written* profile — which is how leaked tool-call tags (`</content>`, `</invoke>`) reached the end of 4 profiles in the first batch. Add a cheap post-write check: no leaked tags, `## Provenance` present, required frontmatter keys present. Replaces hand-inspection.

- **`branding` payload is hint-only — stop trusting it by field** `[weakness]`
  Across the first 15, `branding.colors` needed a `# STRAIN:` correction in 9 and the logo fell back to favicon often; `designSystem` was wrong every time it was mentioned. SCHEMA already says verify-visually / read framework from rawHtml, so captures are fine — but the payload barely earns its keep. Consider dropping `designSystem` from what we store and demoting the whole payload to "hint" in SCHEMA. (≥2 sightings met.)

- **Specify the Provenance section before a consumer parses it** `[weakness]`
  Heading is consistent (15/15) but contents drift: ~5 bullet-list / ~10 prose, and credits-spent appears in only 3 of 15. Codify a minimal template in SCHEMA (pages · method · verify result · credits · couldn't-get) so it stays greppable. Tighten, don't add a field.

- **Credit accounting is unreliable** `[weakness]`
  Observed spend ran 8–58 credits vs. the verb's "~7–10"; agents kept hedging "shared key, can't attribute." Read per-call credits off the Firecrawl response instead of diffing the global balance, and re-baseline the verb's estimate (the all-formats homepage pass looks like the cost driver).

- **Standardize how A/B-snapshot volatility is recorded** `[idea]`
  6 of 15 sites had live experiments (VWO, Optimizely, rotating hero, listing carousels, quiz-gating) flagged inconsistently — sometimes `site_notes`, sometimes `unverified_fields`. A stock `A/B: <tool>` site_notes line + one standard "prices are a point-in-time snapshot" phrasing keeps it queryable without a new field.
