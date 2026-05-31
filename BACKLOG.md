# Backlog

System-level weaknesses, ideas, and TBDs for the engine itself. Light-touch — 1–3 bullets each, no formatting ceremony. A living, curated list (not an append-only log).

**This is the *system* learning home.** Per-company capture learnings live in that company's `site_notes` (in `profile.md`), not here. This file is for things that would change the engine, schema, or workflow.

**Not this file:**
- [`SCHEMA.md`](SCHEMA.md) / [`TAXONOMIES.md`](TAXONOMIES.md) — the store contract. Hard rules that cost a real lesson go here as one-liners, not as backlog items.
- [`_design/`](_design/) — frame, architecture, references. Durable intent.

**Tags:** `[weakness]` design gap likely to bite · `[idea]` possible improvement · `[bug]` confirmed defect · `[tbd]` pending decision · `[simplification]` a way to *remove* surface area or overly-prescriptive guideline.

**Bias check.** Default is to add; resist it. Before logging an addition, ask: is there a way to *remove* or *consolidate* instead? Hunt `[simplification]`s at least as hard as features. If an entry adds surface, note what existing surface it would replace.

**Graduation.** When an item has a clear next action, move it to a `_design/` doc or just do it. Don't graduate to clear the list — most items should sit until a real capture confirms them (≥2 sightings).

**Soft cap: ≤15 open items.** Over that, close/cut/promote 2 before adding 1. Stale items (>60 days, untouched) default-cut on the next review.

---

- **Rung-3 SQLite index — not yet** `[idea]`
  Build the derived index only when relations (discovery) or time-series (traction) first demand it. Markdown is the source of truth; the index is a regenerable lens. Don't build ahead of a real query.
- **`offerings.md` / `brand.md` schemas deferred** `[tbd]`
  Tier-1 module schemas land when the first project enables them. `offerings.md` seed: [`_design/references/doro-product-analysis-prompt.md`](_design/references/doro-product-analysis-prompt.md). Maybe simplest to just have the agent ask the user when they kick off with the verb -- which could be bypassed / "pre-answered" via some project config file(s). Worth a dedicated design session with a proposal table of options.
- **Credit accounting is unreliable** `[weakness]`
  Observed spend ran 8–58 credits vs. the verb's "~7–10"; agents kept hedging "shared key, can't attribute." Read per-call credits off the Firecrawl response instead of diffing the global balance, and re-baseline the verb's estimate (the all-formats homepage pass looks like the cost driver).
- **Underused capture payload — scoped signal audit** `[idea]`
  We persist `html`/`rawHtml`/`links`/`images`/`branding`/`metadata` per page, but enrichment basically only reads `markdown` + screenshots (+ `rawHtml` for framework). Likely leaving signal on the table. Run a $0 experiment over existing `.payloads/` to map what each format adds beyond markdown before codifying any new step. **Lead example: nav.** Markdown flattens mega-nav/flyouts; Doro recovers these from the `<header>`/`<nav>` region (incl. `aria-controls` flyout targets) — borrow the *insight*, not the machinery (Opus reads the HTML region directly; no reducer/Haiku/Pydantic). **Validate completeness against the homepage screenshot (ground truth), not substring presence in the md blob** (a label existing somewhere ≠ hierarchy captured). Nav works *okay* today, so not urgent.
- **`branding` payload is hint-only — stop trusting it by field** `[weakness]`
  Across the first 15, `branding.colors` needed a `# STRAIN:` correction in 9 and the logo fell back to favicon often; `designSystem` was wrong every time it was mentioned. SCHEMA already says verify-visually / read framework from rawHtml, so captures are fine — but the payload barely earns its keep. Consider dropping `designSystem` from what we store and demoting the whole payload to "hint" in SCHEMA. (≥2 sightings met.)
- **Multi-ratio logo set via vision** `[idea]`
  Replace the single `logo_url` with a small `logos: {}` set — mark/favicon (square), wordmark (rectangle), `og:image`, + the cleanest SVG from `images[]` — chosen by vision at ingestion (AI-at-ingestion fit). Adds frontmatter surface → design in a dedicated session. Overlaps + would partly resolve the "branding payload is hint-only" item's logo fallback chain. Not v1-critical.
- **Lint `profile.md` in the verify step** `[idea]`
  `verify` checks scrape md5-uniqueness but never lints the *written* profile — which is how leaked tool-call tags (`</content>`, `</invoke>`) reached the end of 4 profiles in the first batch. Add a cheap post-write check: no leaked tags, `## Provenance` present, required frontmatter keys present. Replaces hand-inspection.
- **Standardize how A/B-snapshot volatility is recorded** `[idea]`
  6 of 15 sites had live experiments (VWO, Optimizely, rotating hero, listing carousels, quiz-gating) flagged inconsistently — sometimes `site_notes`, sometimes `unverified_fields`. A stock `A/B: <tool>` site_notes line + one standard "prices are a point-in-time snapshot" phrasing keeps it queryable without a new field.
