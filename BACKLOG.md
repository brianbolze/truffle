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

- **`offerings.md` / `brand.md` schemas deferred** `[tbd]` `[lg]`
  Tier-1 module schemas land when the first project enables them. `offerings.md` seed: [`_design/references/doro-product-analysis-prompt.md`](_design/references/doro-product-analysis-prompt.md). Maybe simplest to just have the agent ask the user when they kick off with the verb -- which could be bypassed / "pre-answered" via some project config file(s). Worth a dedicated design session with a proposal table of options.
  - **Consumption confirms this is the *binding* gap — and names the field.** Two cold-consumer tests ([`2026-05-31-consumption`](experiments/2026-05-31-consumption/), [`2026-05-31-consumption-affordance`](experiments/2026-05-31-consumption-affordance/)) converge here: a cold agent *can* hand-build a cross-brand GLP-1 price table from the body bullets, but the number is non-reusable narrative — not auditable, can't answer "under $200/mo," doesn't scale to N offerings × 50 brands, one model-downgrade from a wrong table. Proposal for the design session: per-offering `price: {value, unit, cadence, included/excluded, molecule, compounded|branded}`. Turns a ~12-call manual pass into a one-parse query; the offering (not company) as the *unit* also dissolves the "frontmatter cohort over-includes" problem the same test surfaced.
- **`querycheck.py` validates structure but not enum *values*** `[bug]` `[sm]`
  It guards QUERYING's structural assumptions (field presence, multiselect convention) but never checks closed-set fields against TAXONOMIES — so `store/mylifeforce-com`'s off-taxonomy `offering_category: Health & Wellness` passed green (caught only by the consumption-affordance test, by hand). Fix: a `--strict` pass that flags any `entity_type`/`target_market`/`offering_category`/`portfolio_shape`/`business_model`/`primary_industry` value not in the TAXONOMIES set (or `Other`). A few lines on the parse it already does; closes the contract↔corpus drift class at the *value* level. (Also: fix mylifeforce.)
- **Underused capture payload — signal audit** `[idea]` `[md]`
  We persist `html`/`rawHtml`/`links`/`images`/`branding`/`metadata` per page, but enrichment basically reads only `markdown` + screenshots (+ `rawHtml` for framework) — likely leaving signal on the table. Run a $0 experiment over existing `.payloads/` to map what each format adds beyond markdown *before* codifying any new enrichment step. (Nav is the one known instance — its own item below.)
- **Nav-structure capture is lossy** `[weakness]` `[md]`
  Markdown flattens mega-nav/flyouts, so the captured `Nav structure` under-represents the real IA. Likely fix: read the `<header>`/`<nav>` region of `rawHtml` (incl. `aria-controls` flyout targets) — borrow Doro's *insight*, not its machinery (Opus reads the HTML directly; no reducer/Haiku/Pydantic). **Validate completeness against the homepage screenshot (ground truth), not substring presence in the md blob** (a label existing somewhere ≠ hierarchy captured). Works *okay* today → not urgent. A specific slice of the payload-signal audit above. Prior art from Doro:
  - services/app/src/app/services/web_search/nav_extraction
  - services/app/src/app/services/web_search/nav_extraction/llm_extraction/implementations/extractor_v1.py
  - services/app/src/app/services/web_search/nav_extraction/schemas.py
- **Multi-ratio logo set via vision** `[idea]` `[md]`
  Replace the single `logo_url` with a small `logos: {}` set — mark/favicon (square), wordmark (rectangle), `og:image`, + the cleanest SVG from `images[]` — chosen by vision at ingestion (AI-at-ingestion fit). Adds frontmatter surface → design in a dedicated session. Would also retire the brittle favicon logo fallback chain. Not v1-critical.
- **Light, safe, honesty-preserving cleaning / normalization pass on the payload markdown** `[idea]` `[md]`
  Captured `.md` is a raw Firecrawl dump — the "cleaned" files are byte-identical to raw (47.5% blank lines; animated stat-counter digit-columns; leaked VWO/JS + consent blobs; hard-break `\\` residue). **Researched → [`_design/references/payload-cleaning.md`](_design/references/payload-cleaning.md):** a *subtractive + whitespace-only* ruleset (delete noise lines, never reword) keeps every content byte verbatim while cutting ~19% of bytes; the section-tagging idea is folded in (decision lean: strip chrome, don't tag — lean on `profile.md`). **Next: de-risk as `experiments/<date>-payload-clean/` — run over the 111 existing files, prove zero content-line loss — before any SCHEMA/fc.py change.** Not started.
- **Add a `specialties` field to the profile frontmatter** `[idea]`
  A multi-select, non-constrained field. A list of things that the company is known for doing / offering. 
- **Junk soft-404 stubs slip past verify** `[weakness]` `[sm]`
  Some sites serve a fake "Page Not Found" stub (HTTP 404, but a real-sized body) for any bad path — Qualtrics did for 4 guessed URLs. It's not thin and each body is unique, so verify's guards don't catch it, and §5.6 ("trust the body, not the status") says keep it. Two fixes: **prevention** — only scrape URLs that appear in the captured map/homepage links, never guess paths from convention (this alone avoids it); **detection** — teach `fc.py verify` to flag a 404-with-not-found-fingerprint. 1 sighting; act on the 2nd.
- **Rung-3 SQLite index — not yet** `[idea]` `[xl]` `[parked for now]`
  Build the derived index only when relations (discovery) or time-series (traction) first demand it. Markdown is the source of truth; the index is a regenerable lens. Don't build ahead of a real query.
