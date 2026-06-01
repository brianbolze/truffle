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
  Single-company is covered — a fresh agent reliably reaches `research-company`, which transitively reveals the store. The **consumption / aggregation** shape ("compare these companies", "what do these competitors charge", "is X already in our research") has **no verb**. The [2026-06-01 discoverability test](experiments/2026-06-01-discoverability/) caught P4 re-scraping **4 warm brands live**. (The rival skill that owned that intent, `competitive-research-audit`, is now **uninstalled** — so the miss-mode is now "defaults to WebSearch," not "routed to a rival.")
  **Fix — a rung-2 "consume the company store" verb** `[idea]`: a sibling to `research-company` (consume vs. capture — don't fold in) that triggers on consumption intent, reads `WEB_RESEARCH_HOME` + `QUERYING.md`, and filters the corpus **before any web call** (Frame rung 2; consumption-affordance **Wall 2**). `WEB_RESEARCH_HOME` is now set in `~/.claude/settings.json` but **no skill reads it yet** — wire that in here.
  **Act when:** a live consumer appears (none today → unhurried). Then re-run the probe — pass = a fresh agent compares ≥2 warm companies store-first, ~$0, no live re-scrape.

### Schema & taxonomy decisions

- **`offerings.md` design drafted (not activated); `brand.md` still deferred** `[tbd]` `[md]`
  The initial `offerings.md` design session is **done** → [`_design/2026-06-01-offerings.md`](_design/2026-06-01-offerings.md) (9-field record; per-offering `price_visibility` the one universal axis; heavy price-normalization left per messy vertical; `pricing_model` retired). What's open is a second design review, and **activation** — whether/when to write the file, gated on a project enabling the module (single-offering companies fold a `price_visibility` token into `profile.md` instead). `brand.md` schema is still unstarted; seed [`doro-product-analysis-prompt.md`](_design/references/doro-product-analysis-prompt.md).
  **Act when:** Brian decides, or a project turns on offerings (wire SCHEMA's Tier-1 stub → the design doc; add `offerings.md` lint to `fc.py`/`querycheck.py`) or brand.

- **Add a `specialties` field to profile frontmatter** `[idea]` `[sm]` `[@brian]`
  A multi-select, non-constrained list of what the company is known for doing / offering.

- **Add a `socials` frontmatter field (LinkedIn, X, Instagram, …)** `[idea]` `[sm]` `[@brian]`
  A small map filled when present — `linkedin` / `x` / `instagram` / `youtube` / `facebook` / `tiktok`. Multi-source, **not** JSON-LD-only: `sameAs` (rawHtml) is the cleanest, but near-universal footer/header anchors to the social domains are a free fallback (markdown links + `rawHtml`). Additive → MINOR bump. Overlaps the discoverability item's `linkedin`/`x`/`wikipedia` external-links hook; capture rides the `rawHtml` read ↑ (the [signal audit](experiments/2026-06-01-signal-audit/FINDINGS.md) found 0/profiles carry socials today, all 6 sampled JSON-LDs do).

### Capture quality

- **Junk soft-404 stubs slip past verify** `[weakness]` `[sm]`
  Some sites serve a fake "Page Not Found" stub (HTTP 404, but a real-sized, unique body) for any bad path — Qualtrics did, for 4 guessed URLs. It's not thin, so verify's guards miss it and §5.6 ("trust the body, not the status") says keep it. **Prevention:** only scrape URLs from the captured map/homepage links, never guess paths from convention (this alone avoids it). **Detection:** teach `fc.py verify` a 404-with-not-found fingerprint.
  **Act when:** 2nd sighting (1 so far).

- **Read `rawHtml`'s structured layer (JSON-LD + `<header>`) at enrichment** `[idea]` `[md]` `[@brian]` — *graduated from the signal audit → [FINDINGS](experiments/2026-06-01-signal-audit/FINDINGS.md)*
  Audit verdict: `rawHtml` is the one badly-underused payload (`html`/`links` proved dead weight — the "html recovers garbled prices" rationale was 0/43, all artifacts; `branding`/`metadata`/`images` ~scoped right). Read its **JSON-LD** (32/43 homepages: `legalName`, `alternateName`→`aliases`, founders, self-reported `AggregateRating`, `medicalSpecialty`) + the `<header>` flyout region — Opus reads both slices of the already-persisted payload directly; **no reducer/Haiku/Pydantic** (anti-Doro), hint-to-verify like `branding`. **Consolidates nav (below) + the logo set into one change**; live decision is the scope boundary (which JSON-LD fields enter the profile vs brush the Frame's deep-research exclusion — founders/founding-date are the edge).
  **Act when:** next. [Probe 4](experiments/2026-06-01-signal-audit/FINDINGS.md) already ran the delta: enrichment *already* gets the identity basics (founders/HQ/desc) from the about page — the clean net-new wins are **socials (`sameAs`)** (0/profiles have them), self-reported **ratings**, and verbatim **`legalName`/`foundingDate`/specialties**. Remaining work: light SCHEMA guidance + playbook edit (Opus reads the slice, hint-to-verify). Field boundary already decided — lean to adding (company-published).

- **Nav-structure capture is lossy** `[weakness]` `[md]` `[@brian]` — *direction confirmed by the [signal audit](experiments/2026-06-01-signal-audit/FINDINGS.md); fold into the `rawHtml` read ↑*
  Markdown flattens mega-nav/flyouts, so the captured `Nav structure` under-represents the real IA. Audit confirmed the fix is the `<header>`/`<nav>` region of `rawHtml` (incl. `aria-controls` flyout targets — twilio 51, apple 23) and **ruled out `links`** (flat + redundant + noisy). Borrow Doro's *insight*, not its machinery (Opus reads the HTML directly; no reducer/Haiku/Pydantic). **Validate completeness against the homepage screenshot (ground truth), not substring presence** (a label existing somewhere ≠ hierarchy captured). Works okay today → not urgent. Doro prior art: `…/web_search/nav_extraction/` (`llm_extraction/implementations/extractor_v1.py`, `schemas.py`).

- **Light, honesty-preserving cleaning pass on payload markdown** `[idea]` `[md]` `[@brian]`
  Captured `.md` is a raw Firecrawl dump (47.5% blank lines; animated stat-counter digit-columns; leaked VWO/JS + consent blobs; hard-break `\\` residue) — the "cleaned" files are byte-identical to raw. Researched → [`payload-cleaning.md`](_design/references/payload-cleaning.md): a **subtractive + whitespace-only** ruleset (delete noise lines, never reword) cuts ~19% of bytes while keeping every content byte verbatim; decision lean = strip chrome, don't section-tag.
  **Act when:** de-risk first — `experiments/<date>-payload-clean/` over the 111 existing files, prove zero content-line loss, *then* touch SCHEMA / fc.py.

- **Multi-ratio logo set via vision** `[idea]` `[md]` `[@brian]`
  Replace the single `logo_url` with a small `logos: {}` set — mark/favicon (square), wordmark (rectangle), `og:image`, + the cleanest SVG from `images[]` — chosen by vision at ingestion. Retires the brittle favicon fallback chain. Adds frontmatter surface → design in a dedicated session. Not v1-critical.

### Parked

- **Rung-3 SQLite index — not yet** `[idea]` `[xl]` `[parked]`
  Build the derived index only when relations (discovery) or time-series (traction) first demand it. Markdown stays the source of truth; the index is a regenerable lens. Don't build ahead of a real query. [coded-queries](experiments/2026-06-01-coded-queries/) quantified the emptiness: **23/24 relation edges dangle** today.
  **When it lands:** index relations on the subsidiary side (`parent`), reverse-scanned. Consumption (P7) found `parent`/`owns` are populated **one-sided** — `delighted.parent: [qualtrics.com]` carries the link, but `qualtrics.owns` doesn't list Delighted. A JOIN that trusts `owns` for symmetry misses real edges: build the graph from `parent` (reverse-scanned across the corpus), treat `owns` as best-effort.
