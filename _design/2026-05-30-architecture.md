# Architecture: how web-research works

> **What this is.** The end-to-end picture — layers, the lifecycle of a capture, how the data is consumed, how the system improves itself. Companion to the [Frame](2026-05-29-frame.md): the Frame covers *why* and *scope*; this covers *how*. Still a working draft.

## The loop in one breath

A global verb captures a company **once** — Opus reading many pages, screenshots, and Firecrawl's `branding`/`metadata` — and leaves a structured, cited dossier in a shared store. Every later read (another project, a cross-company query, a deep-research run) **filters that structure instead of re-scraping**. Reasoning is free (absorbed by Claude Max subscription); Firecrawl is the only real cost — so the store is both the moat and the budget.

This is Doro's *"AI at ingestion, structure for retrieval"* on a file-first, single-user substrate — with Doro's heavy infrastructure deliberately refused.

## Three layers

Where things live, and how they connect.

| Layer | What | Lives in |
|---|---|---|
| **Verbs** | Skills / slash commands (`/research-company` …) | Global `~/.claude/skills/` |
| **Engine + Store** | Capture/clean/query scripts, the shared store, default schema + taxonomies | This repo (own remote + iCloud) |
| **Project config** | Which modules, freshness TTLs, destination(s), vertical taxonomy | `.web-research/config.yaml` per project |

A global verb finds the engine via `WEB_RESEARCH_HOME` in `~/.claude/settings.json` — the same file that grants repo access and allowlists `api.firecrawl.dev`. Config resolves as **global defaults ← project overrides**, so a bare session gets sane behavior and a configured project gets its own schema + destination.

> **What the engine owns — and doesn't.** This is the **State / Signals / Judgments** split from the [Frame](2026-05-29-frame.md), made operational. The engine owns **State** — generic, cross-domain **classification** (`entity_type`, `offering_category`, … — see [`TAXONOMIES.md`](../TAXONOMIES.md)) and company-intrinsic facts/observations, captured as a current snapshot. It does *not* own: (a) **market verticals** ("Weight Loss," "Hormone Therapy") — project-owned; (b) **Signals** — the same facts on a time axis (funding, traffic, headcount), which append rather than overwrite and live in the signals layer, not the profile; or (c) **user-relative judgments** — strategic relevance, importance, competitive threat, fit — which depend on *who's asking* and need context the engine doesn't typically have. Rule of thumb: the engine **describes the company**; the project decides **what it means to them**. (The optional `Strategic read` section is company-*intrinsic* observation — "what's notable here" — not relevance-to-you.) Market position rides the same line: record what a site foregrounds as observation, but inferring flagship status / market leadership / adoption from prominence is a judgment about *the market*, not the company — a consumer-layer call, deferred (a future Frame session, not built into capture).

## The lifecycle of a capture

The heart of the system. `/research-company <domain>` runs:

1. **Resolve config** — merge global defaults with the calling project's `.web-research/config.yaml` (modules enabled, TTLs, destination).
2. **Seed from the store** — if `store/<domain>/` exists, read its `site_notes` (capture playbook), `key_pages`, and `captured_at`. The last run teaches this one.
3. **Freshness check** — per-section TTL decides reuse vs. refetch. Fresh ⇒ serve the existing dossier and stop. Stale ⇒ refetch only what's stale.
4. **Map + homepage, in parallel** — Firecrawl `/v2/map` for the URL inventory *and* a `/v2/scrape` of the homepage (the root is almost always the most important page, and its nav/links are themselves a map). Merge both to pick key pages — pricing, products, how-it-works, about.
5. **Scrape the rest** — `/v2/scrape` per remaining key page (markdown + html + links + screenshot + `branding` + `metadata`); raw responses land in `captures/<date>/.payloads/`.
6. **Enrich - AI at ingestion** — Opus reads the *whole* capture (pages + screenshots + branding) and writes `profile.md`: frontmatter (identity, generic classification, visual identity) + body (the synthesized read). Enabled **modules run their own gathering recipe here** — not just fill fields (e.g. `offerings.md`, `brand.md`; see [Modules](#modules-recipes-not-just-schemas)). *This is the expensive step, done once.*
7. **Record** — cleaned observations to `captures/<date>/`, update `site_notes` with anything new, stamp `captured_at`.
8. **Promote (optional)** — propose structured writes to the project's destination (e.g. a Notion DB). Default to "**Propose, don't write**" — the engine never silently mutates a project's source of truth. Those output destinations are typically co-authored with humans, so we need to be careful not to overwrite user-content, and/or add bloat. 

Steps 4–6 are cache-aware: a warm, fresh company skips straight to "serve." v1 runs this interactively in a session; a scheduled cloud routine running the same verb is a later flip, not a rebuild.

**Parallelism via sub-agents.** Where it pays, the verb fans out — a sub-agent per key page to scrape + clean, deeper / specialized analysis (like image analysis), or per opt-in module to enrich — and the lead agent reconciles the results into `profile.md`. (Opus spawns sub-agents sparingly by default, so the verb says explicitly when fan-out helps.)

## Operations vocabulary

| Operation | What | Where it lands |
|---|---|---|
| **Capture** | Pull + persist external signal with provenance | `captures/<date>/` + `.payloads/` |
| **Enrichment** | AI-at-ingestion: structured fields from the capture | `profile.md` frontmatter, `offerings.md` |
| **Synthesis** | Derived understanding across the capture | `profile.md` body, `brand.md` |
| **Promotion** | Propose structured output to a project's KB | project destination (Notion) — propose-only |

## The store

One company = one folder = its whole story. Top docs are the latest view; you rarely open `captures/`.

```
store/<domain-slug>/              # e.g. hone-health
  profile.md                      # State — the current snapshot (frontmatter + body)
  offerings.md                    # a module doc, opt-in, its own freshness
  captures/
    <date>/                       # one self-contained folder per run
      homepage.md  pricing.md     # cleaned observations
      .payloads/                  # raw Firecrawl JSON + screenshots (gitignored, pruned)
    _archive/                     # old runs swept aside to keep the latest obvious
cohorts/<category-slug>/          # (later) cross-company signals that don't key on a domain
```

- **Top = the latest view, `captures/` = the source** you rarely open. A `captured_at` stamp is the freshness pointer — no fragile symlinks (they break across iCloud + git + cloud).
- **Every consumer also gets a primary-source cache.** Beyond the synthesized `profile.md`, the cleaned `captures/` and raw `.payloads/` let an agent quote exact wording or inspect a page *without re-fetching* — pre-fetched primary source, ready to cite.

> **The store holds snapshots today.** The **Signals** layer (funding, traffic-over-time) is a *different record shape* — dated, append-only — and is **not in the store yet**; today it lives in the `competitive-traction` sibling. *Whether web-research grows its own domain-keyed timeline or keeps delegating is an [open question](2026-05-29-frame.md)* — the deliberate "how do these two systems re-relate?" call worth resolving before the aggregation layer hardens.

## Modules: recipes, not just schemas

> **A module is a *recipe + schema + destination* — a mini-verb.** It carries its own way to *gather* (which sources, which pages, what to trust), not just fields to fill — the way `/research-company` carries its capture playbook. The core capture writes `profile.md`; an enabled module runs its recipe to write its own doc. **`offerings.md` is the first exemplar** (`brand.md` next).

**Two module species** (since the `telehealth` pack — see [`SCHEMA.md` → Tier-1 modules](../SCHEMA.md#tier-1-modules-opt-in-separate-docs) + [design](2026-06-04-telehealth-cohort.md)): **depth modules** extend a *universal* dimension at finer grain (`offerings.md`, `brand.md`) with a real gather recipe; **cohort packs** carry *vertical-specific classification* cuts (`telehealth.md`) that go flat in the universal schema, with only a thin recipe (they ride the `profile.md` pages). A cohort pack is per-domain **State** — distinct from the store-level `cohorts/<category-slug>/` *signals* layer below, which the name unfortunately echoes.

**Where a module's output lands is decided by the *kind* of fact** (the Frame's State / Signals / Judgments):

| Kind | Example | Destination |
|---|---|---|
| **State** | what they sell, founders | the `web-research` store (`profile.md` / a module doc) |
| **Signals** | funding, traffic trend | the signals layer (`competitive-traction` today) |
| **Judgments** | formidable? threat? | the project |

A module is opt-in per project (config resolves global defaults ← project overrides) and carries its own freshness TTL. *Detailed module schemas land when the first project enables one — deferred on purpose; see [`SCHEMA.md`](../SCHEMA.md).*

## Three consumption paths

"Queryability is the product" — made concrete. The store is written once and read three ways:

**1. Point read (the dossier).** "Tell me about Hone." A session reads `profile.md`; if stale/absent, the verb captures first. This is the cold-Cowork-session success criterion — one invocation, cited, fresh, no hand-holding.

**2. Cross-company aggregation.** "How does everyone price Sermorelin?" Climbs the query-affordance ladder, cheapest rung that works:

| Rung | What | Status |
|---|---|---|
| 1 | Disciplined frontmatter (grep/ripgrep) | now |
| 2 | A `digest`-style helper wrapped in a skill the agent reaches for | proven in [experiment](../experiments/2026-05-29-query-affordance/FINDINGS.md); the likely real fix |
| 3 | Derived SQLite index, regenerated from the markdown — a cache, never source-of-truth | **landed 2026-06-04** for telehealth cohort aggregation ([`scripts/build_db.py`](../scripts/build_db.py); [QUERYING Recipe 7](../QUERYING.md)); the relations/traction **join graph** stays deferred until a consumer earns it |

**3. Deep-research as a consumer.** An open-ended run (news, funding, M&A, reviews) **reads the store as priors first**, then goes wide, and writes its narrative **project-side, not into the store**. The store stays tight and factual — we never dump news/funding into a profile (that's the Doro "ingest everything into a graph" move we refuse). The store gives the foundation; deep research builds on it.

**Across all three — the store is also a primary-source cache.** Beyond the synthesized `profile.md`, every consumer can pull **verbatim** material: cleaned `captures/` and the raw `.payloads/` (markdown, screenshots) let an agent quote exact wording or inspect a page *without re-fetching*. The value isn't only structured summary — it's pre-fetched primary source, ready to cite.

## Freshness and the cost model

- **TTL-by-section.** Pricing goes stale fast; positioning slower; identity rarely. The capture refetches only what's expired. Tunable per project.
- **Firecrawl is the only real money.** Everything else rides Claude Max. So: cache aggressively, **map before scrape**, scrape only stale pages, and prune payload sidecars on a progressive curve. A company's second look — by any project — is nearly free.
- **The store warms over time and across projects.** This compounding is the whole economic case.

## Self-improvement — two homes

- **Per-company learnings → `site_notes`** in that company's `profile.md`. The next capture reads it first, so the system inherits the playbook ("Cloudflare-fronted; pricing is JS-walled") instead of rediscovering it.
- **System-level learnings → `BACKLOG.md`** — capped (≤15), tagged, bias-checked ("resist additions; hunt simplifications"), with a graduation path. A light retro reviews it.

The unwieldy `proposals/` folder from competitive-intel is deliberately dropped. Captures improve run-to-run via `site_notes`; the system improves via the BACKLOG retro.

## Entities & identity

The store will hold **several** entity types, but primarily "Companies".

- **Companies** — keyed by canonical **domain**. Unique, free, clean. The whole of v1.
- **Offerings** — products/services, keyed *within* a company (`domain` + offering slug). Arrives with `offerings.md`.
- **Cohorts** — category slugs, for cross-company signals that don't attach to one domain (traction, market-map inputs). Later.
- *(more may follow — events, topics, etc.)*

**Identity is easy for companies, hard for everything else.** Domain is a natural global key; offerings and cross-company *concepts* are not. Is "Sermorelin" at brand A the same entity as at brand B? Canonicalizing that *is* the entity-resolution problem we deliberately avoided for companies. The discipline: key offerings **within** a company, and treat cross-company grouping ("Sermorelin across brands") as a **query-time** concern (project vertical + the aggregation layer) — not a stored canonical entity, until it proves it must become one. That's the line that keeps the entity-resolution swamp out.

**Relations follow the same rule — markdown is the ledger, SQLite is the lens.** A company's links to others (competitors, parent/sub, related) live as reference lists in frontmatter — the source of truth, exactly like a Notion relation property (which is itself just an array of references). When joins are needed ("the cluster around X"), the rung-3 **derived SQLite index** projects those references into a queryable graph — regenerated from the markdown, never authoritative. That keeps real relational querying without making a database the system. (For a project that wants rich relational modeling *with a UI*, Notion is already that DB — it's the Promotion destination.)

## What we borrow, what we refuse

<details>
    <summary>The explicit inheritance — and the guardrails</summary>

    **From Doro (ideas):** AI-at-ingestion; "structure for retrieval, not open query-time RAG"; the Capture/Enrichment/Synthesis vocabulary; provenance on every fact — verbatim quotes are our anti-fabrication form of it; freshness/recency weighting; the company field menu.

    **From agent-workflows (substrate):** markdown + YAML + git + Claude Code/Routines; Max-absorbed cost (not LLM API-call pricing); payload sidecars + progressive pruning; the `site_notes` carry-forward; the BACKLOG bias-check.

    **Refused (the anti-Doro line):** Postgres/Neo4j/S3/Temporal; embeddings / vector RAG; a datapoint reconciliation engine; complex entity-resolution machinery (domain *is* the key); multi-tenant schemas; a served API / webhooks; per-market taxonomy + normalization services; and change-tracking/diffing as a core concern. Each was right for a VC-backed PE tool; each is wrong for a single-user file-first engine.

</details>

## What's in scope — a guideline, not a roadmap

A lens for sorting *future* capabilities (a principle, not a commitment), mapping onto the Frame's three kinds of fact:

- **State** — what a company/offering *is* now, capturable from its own primary web sources, cacheable → **the engine owns it.**
- **Signals** — the same facts on a time axis (funding, traffic, headcount; news/M&A as dated events) → **the signals layer**, not the profile.
- **Judgments** — relevance, threat, fit, relative to the asker → **the consumer/project.**

*Discovery* (finding related companies) and *traction* (time-series metrics) sit in the family as distinct capabilities — traction being Signals. When unsure: *is this durable state from the company's own sources, or a stream/opinion that belongs to a consumer?*

## Phasing

| Phase | Delivers | Horizon |
|---|---|---|
| **Foundation** | `/research-company` → single-company dossier; query rungs 1–2 | now |
| **Aggregation** | Cross-company queries; rung 3 index | medium |
| **Visualization** | Market maps, 2×2s, battle maps (crowdedness / dominance / hotness) | long |

Visualizations are pull-consumers, but they reach backward: "hotness" needs traction signals, so **traction is a first-class future signal**, even though the maps are far off.

---

*Companion: [`2026-05-29-frame.md`](2026-05-29-frame.md) (why/scope), [`../SCHEMA.md`](../SCHEMA.md) + [`../TAXONOMIES.md`](../TAXONOMIES.md) (the store contract), [`../experiments/2026-05-29-query-affordance/`](../experiments/2026-05-29-query-affordance/) (the rung-2 proof).*
