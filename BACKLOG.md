# Backlog

System-level weaknesses, ideas, and TBDs for the engine itself — things that would change the **schema, the verbs, or the workflow**. A living, curated list (capped, not append-only). Per-company capture learnings live in that company's `site_notes` (in `profile.md`), never here.

**Not this file:**
- [`SCHEMA.md`](SCHEMA.md) / [`TAXONOMIES.md`](TAXONOMIES.md) — the store contract. A hard rule that cost a real lesson lands there as a one-liner, not here.
- [`_design/`](_design/) — frame, architecture, references. Durable intent.

**Item format.** A bold punchline + tags on one scannable line (tags in this order), then 1–3 tight sentences. An optional **Act when** line names the trigger that graduates the item — point at cited experiments rather than restating them.
- **kind** — `[weakness]` gap likely to bite · `[idea]` possible improvement · `[bug]` confirmed defect · `[tbd]` pending decision · `[simplification]` removes surface area / prescriptiveness
- **size** (rough wall time) — `[sm]` ≤½ day · `[md]` ~1 day · `[lg]` 2–3 days · `[xl]` >3 days, break it up
- **provenance** — `[@brian]` added/approved by Brian; untagged = agent-added, subject to review · `[parked]` = deferred on purpose

**Bias to remove.** Default is to add — resist it. Before logging, look for a way to *consolidate* or *cut* instead; hunt `[simplification]`s at least as hard as features. If an entry adds surface, note what it replaces.

**Graduate on a trigger, not to clear the list.** Most items sit until a real capture confirms them (≥2 sightings) or their **Act when** fires — then move to a `_design/` doc or just do it.

**Soft cap: ≤15 open items.** Over that, close/cut/promote 2 before adding 1. Stale items (>60 days untouched) default-cut at the next review.

---

### Discoverability & consumption

- **No store-aware entry point for cross-company / consumption queries** `[weakness]` `[md]`
  Single-company is covered — a fresh agent in another project reliably reaches `research-company`, which transitively reveals the store. But the **consumption / aggregation** shape ("compare these companies", "what do these competitors charge", "is X already in our research") has **no verb**, and `QUERYING.md` is invisible until you're already in the repo — so a fresh agent defaults to bare WebSearch. The [2026-06-01 discoverability test](experiments/2026-06-01-discoverability/) proved it: P4 re-scraped **4 warm brands live** instead of reading the store.
  **Fix — a rung-2 "consume the company store" verb** `[idea]`: the unbuilt half of the Frame's query-affordance ladder ([Frame](_design/2026-05-29-frame.md) rung 2; consumption-affordance **Wall 2**). A skill that triggers on consumption intent, resolves `WEB_RESEARCH_HOME`, reads `QUERYING.md`, and filters the corpus **before any web call**. Sibling to `research-company` (consume vs. capture) — don't fold in. (`WEB_RESEARCH_HOME` is set in `~/.claude/settings.json`; the skills don't *read* it yet — wire that in when this lands.)
  **Act when:** build it next, then re-run the 2026-06-01 probe — pass = a fresh agent compares ≥2 warm companies store-first, at ~$0, with no live re-scrape.

### Schema & taxonomy decisions

- **`offerings.md` / `brand.md` Tier-1 schemas deferred** `[tbd]` `[lg]`
  The Tier-1 module schemas land when the first project enables them; worth a dedicated design session (a proposal table of options — including "agent asks the user at verb kickoff, pre-answerable via a project config file"). Seed: [`doro-product-analysis-prompt.md`](_design/references/doro-product-analysis-prompt.md). Three cold-consumer cohorts (telehealth / SaaS / luxury watches — [consumption](experiments/2026-05-31-consumption/), [consumption-affordance](experiments/2026-05-31-consumption-affordance/)) already settle the hard part of the design:
  - **Price *visibility* is the one universal axis** — `published | gated/on-request | partial`, common to SaaS sales-gating, telehealth quiz-walls, and luxury "price on request" (5/7 watches, 6/9 SaaS). It must be **per-offering in `offerings.md`, not a profile-frontmatter scalar**: Cartier publishes jewelry/fragrance prices but gates its *watches*. The old `pricing_model` (per-seat/usage) framing is **retired** — meaningless for a watch.
  - **Price *value* never generalizes; the heavy normalizer is messy-pricing-specific.** Clean published tiers (SaaS, watch MSRPs) read straight off the body; the `{value, unit, cadence, included/excluded, molecule, compounded|branded}` rig is **earned per messy vertical** (telehealth GLP-1), never universal. `Catalog`-shape sellers cap even published prices at a body **range**, by design.
  - **Cohort grouping stays prose / consumer-side** — no frontmatter home across all three cohorts (agents grouped by brand-name recognition). A value-metric `unit` (per-seat | per-response | flat | per-SKU) is worth having for comparability, but grouping itself is a Tier-2 concern.
  **Act when:** the first project turns on offerings/brand — open the design session; the price-visibility verdict above is the seed.

- **`offering_category` has no Luxury Goods / Jewelry & Watches value** `[weakness]` `[sm]`
  A luxury Maison (jewelry, watches, fragrance, leather goods) has no clean home. Cartier was filed `[Apparel & Footwear, Retail / E-Commerce]` with a STRAIN note — least-bad, but it mis-groups fine jewelry with clothing. Recurs immediately: **rolex-com, patek-com, swatch-com** are already captured and awaiting profiles, same shape.
  **Act when:** the 2nd luxury profile — decide between adding a `Luxury Goods` (or `Jewelry & Watches`) value + migrating, vs. standardizing the cohort on `Apparel & Footwear`. Don't let it fragment across `Apparel` / `Other` / `Retail`.

- **Add a `specialties` field to profile frontmatter** `[idea]` `[sm]` `[@brian]`
  A multi-select, non-constrained list of what the company is known for doing / offering.

### Capture quality

- **Better `/map` guidance so results aren't 90% blog / docs** `[weakness]` `[sm]` `[@brian]`
  The map step over-returns articles and documentation, drowning product/pricing pages — hit on the Cloudflare and Datadog runs (should be noted in their `site_notes`).

- **Junk soft-404 stubs slip past verify** `[weakness]` `[sm]`
  Some sites serve a fake "Page Not Found" stub (HTTP 404, but a real-sized, unique body) for any bad path — Qualtrics did, for 4 guessed URLs. It's not thin, so verify's guards miss it and §5.6 ("trust the body, not the status") says keep it. **Prevention:** only scrape URLs from the captured map/homepage links, never guess paths from convention (this alone avoids it). **Detection:** teach `fc.py verify` a 404-with-not-found fingerprint.
  **Act when:** 2nd sighting (1 so far).

- **Underused capture payload — signal audit** `[idea]` `[md]` `[@brian]`
  We persist `html`/`rawHtml`/`links`/`images`/`branding`/`metadata` per page, but enrichment reads basically only `markdown` + screenshots (+ `rawHtml` for framework) — likely leaving signal on the table. Run a $0 experiment over existing `.payloads/` to map what each format adds beyond markdown *before* codifying any new enrichment step. (Nav, below, is the one known instance.)

- **Nav-structure capture is lossy** `[weakness]` `[md]` `[@brian]` — *a slice of the signal audit ↑*
  Markdown flattens mega-nav/flyouts, so the captured `Nav structure` under-represents the real IA. Likely fix: read the `<header>`/`<nav>` region of `rawHtml` (incl. `aria-controls` flyout targets) — borrow Doro's *insight*, not its machinery (Opus reads the HTML directly; no reducer/Haiku/Pydantic). **Validate completeness against the homepage screenshot (ground truth), not substring presence** (a label existing somewhere ≠ hierarchy captured). Works okay today → not urgent. Doro prior art: `…/web_search/nav_extraction/` (`llm_extraction/implementations/extractor_v1.py`, `schemas.py`).

- **Light, honesty-preserving cleaning pass on payload markdown** `[idea]` `[md]` `[@brian]`
  Captured `.md` is a raw Firecrawl dump (47.5% blank lines; animated stat-counter digit-columns; leaked VWO/JS + consent blobs; hard-break `\\` residue) — the "cleaned" files are byte-identical to raw. Researched → [`payload-cleaning.md`](_design/references/payload-cleaning.md): a **subtractive + whitespace-only** ruleset (delete noise lines, never reword) cuts ~19% of bytes while keeping every content byte verbatim; decision lean = strip chrome, don't section-tag.
  **Act when:** de-risk first — `experiments/<date>-payload-clean/` over the 111 existing files, prove zero content-line loss, *then* touch SCHEMA / fc.py.

- **Multi-ratio logo set via vision** `[idea]` `[md]` `[@brian]`
  Replace the single `logo_url` with a small `logos: {}` set — mark/favicon (square), wordmark (rectangle), `og:image`, + the cleanest SVG from `images[]` — chosen by vision at ingestion. Retires the brittle favicon fallback chain. Adds frontmatter surface → design in a dedicated session. Not v1-critical.

### Parked

- **Rung-3 SQLite index — not yet** `[idea]` `[xl]` `[parked]`
  Build the derived index only when relations (discovery) or time-series (traction) first demand it. Markdown stays the source of truth; the index is a regenerable lens. Don't build ahead of a real query.
  **When it lands:** index relations on the subsidiary side (`parent`), reverse-scanned. Consumption (P7) found `parent`/`owns` are populated **one-sided** — `delighted.parent: [qualtrics.com]` carries the link, but `qualtrics.owns` doesn't list Delighted. A JOIN that trusts `owns` for symmetry misses real edges: build the graph from `parent` (reverse-scanned across the corpus), treat `owns` as best-effort.
