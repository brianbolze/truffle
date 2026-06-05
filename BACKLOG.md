# Backlog

System-level weaknesses, ideas, and TBDs for the engine itself — things that would change the **schema, the verbs, or the workflow**. A living, curated list (capped, not append-only). Per-company capture learnings live in that company's `site_notes` (in `profile.md`), never here.

**Not this file:**
- [`SCHEMA.md`](SCHEMA.md) / [`TAXONOMIES.md`](TAXONOMIES.md) — the store contract. A hard rule that cost a real lesson lands there as a one-liner, not here.
- [`_design/`](_design/) — frame, architecture, references. Durable intent.

**Item format.** A bold punchline + tags on one scannable line (tags in this order), then 1–3 tight sentences. An optional **Act when** line names the trigger that graduates the item — point at cited experiments rather than restating them.
- **kind** — `[weakness]` gap likely to bite · `[idea]` possible improvement · `[bug]` confirmed defect · `[tbd]` pending decision · `[simplification]` removes surface area / prescriptiveness
- **provenance** — `[@brian]` added / explicitly-approved / co-authored by Brian; untagged = agent-added, subject to review
- `[parked]` = deferred on purpose

**Bias to remove.** Default is to add — resist it. Before logging, look for a way to *consolidate* or *cut* instead; hunt `[simplification]`s at least as hard as features. If an entry adds surface, note what it replaces.

**Graduate on a trigger, not to clear the list.** Most items sit until a real capture confirms them (≥2 sightings) or their **Act when** fires — then move to a `_design/` doc or just do it.

**Soft cap: ≤15 open items.** Over that, close/cut/promote 2 before adding 1. Stale items (>60 days untouched) default-cut at the next review.

---

- **Automatic retro** `[idea]` `[@brian]`
  Adjust the system / `research-company` verb such that when an agent has a really messy / ineffective capture - they automatically write a retro (or, maybe suggest the user spawn a new session for that retro... idk... I still want the user to get their results quickly - without waiting for the retro to complete...) -- that gets written to _design/retro/ -- following a consistent format / guideline.

### Discoverability & consumption

- **No store-aware entry point for cross-company / consumption queries** `[weakness]` `[md]`
  Single-company is covered — a fresh agent reliably reaches `research-company`, which transitively reveals the store. The **consumption / aggregation** shape ("compare these companies", "what do these competitors charge", "is X already in our research") has **no verb**. The [2026-06-01 discoverability test](experiments/2026-06-01-discoverability/) caught P4 re-scraping **4 warm brands live**. (The rival skill that owned that intent, `competitive-research-audit`, is now **uninstalled** — so the miss-mode is now "defaults to WebSearch," not "routed to a rival.")
  **Fix — a rung-2 "consume the company store" verb** `[idea]`: a sibling to `research-company` (consume vs. capture — don't fold in) that triggers on consumption intent, reads `WEB_RESEARCH_HOME` + `QUERYING.md`, and filters the corpus **before any web call** (Frame rung 2; consumption-affordance **Wall 2**). `WEB_RESEARCH_HOME` is now set in `~/.claude/settings.json` but **no skill reads it yet** — wire that in here.
  **Act when:** a live consumer appears (none today → unhurried). Then re-run the probe — pass = a fresh agent compares ≥2 warm companies store-first, ~$0, no live re-scrape.

### Schema & taxonomy decisions

- **Revisit 2.2's "no `founders`/`legal_entity` field" call — a cohort consumer has now appeared** `[tbd]` `[sm]`
  2.2 deliberately kept both out (`legalName` folds into `aliases`; founders "stay at the deep-research edge," prose-only) "until a cohort consumer defines the right shape." The 2026-06-01 Teleprescribe telehealth deep-research cohort is that consumer — all 6 reports leaned on founders + legal entity, several KB-load-bearing (PeterMD "no real Peter"; Remedy → founder Haris Memon). **But the evidence cuts both ways:** most founders were dug *externally* (Sunbiz/news), not from JSON-LD — which is exactly *why* 2.2 edged them; only site-derivable ones are true store-state.
  **Decide:** promote a queryable `legal_entity` out of `aliases` (cheap, low-risk), and/or a `founders` field filled *only when site-derivable* — never one that needs external research to fill, which would break the site-derived-state line.

### Capture quality

- **Junk soft-404 stubs slip past verify** `[weakness]` `[sm]`
  Some sites serve a fake "Page Not Found" stub (HTTP 404, but a real-sized, unique body) for any bad path — Qualtrics did, for 4 guessed URLs. It's not thin, so verify's guards miss it and §5.6 ("trust the body, not the status") says keep it. **Prevention:** only scrape URLs from the captured map/homepage links, never guess paths from convention (this alone avoids it). **Detection:** teach `fc.py verify` a 404-with-not-found fingerprint.
  **Act when:** 2nd sighting (1 so far).

- **Leaked-tag guard only runs on `profile.md`** `[bug]` `[s]`
  The `</invoke>`/`</content>` leaked-tag check lives in `fc.py verify` (profile.md only); `cohortcheck.py` and `offeringscheck.py` don't check for it, so a `telehealth.md` / `offerings.md` can ship leaked tags silently. Hit on the Noom run (2026-06-04) — both module files trailed a `</content>` that only a manual `tail` caught. **Fix:** lift the leaked-tag scan into a shared helper all three linters call (or have cohortcheck/offeringscheck run it).

- **Light, honesty-preserving cleaning pass on payload markdown** `[idea]` `[md]` `[@brian]`
  Captured `.md` is a raw Firecrawl dump (47.5% blank lines; animated stat-counter digit-columns; leaked VWO/JS + consent blobs; hard-break `\\` residue) — the "cleaned" files are byte-identical to raw. Researched → [`payload-cleaning.md`](_design/references/payload-cleaning.md): a **subtractive + whitespace-only** ruleset (delete noise lines, never reword) cuts ~19% of bytes while keeping every content byte verbatim; decision lean = strip chrome, don't section-tag.
  **Act when:** de-risk first — `experiments/<date>-payload-clean/` over the 111 existing files, prove zero content-line loss, *then* touch SCHEMA / fc.py.

- **Hero-image module is physical-product-only** `[idea]` `[s]`
  `fc.py hero` + the step-2.5 "offerings.md with flagship product images" option presume a physical render (bottle / vial / pen). On a software/API company there's nothing to capture — the Stripe run (2026-06-04) path-scored 15 candidates that were all lifestyle photography / demo-merchant goods / UI mockups (every score 0.0); the run correctly returned **N/A**, but the guided menu offered it anyway. **Cheap fix:** in the step-2.5 batch, suppress (or label "physical products only") the hero-image option when `offering_category` carries no `Physical Products / Hardware` / CPG — same logic likely applies to `Marketplace / Platform` and `Financial / Fintech`.

### Parked

- **Rung-3 SQLite index — not yet** `[idea]` `[xl]` `[parked]`
  Build the derived index only when relations (discovery) or time-series (traction) first demand it. Markdown stays the source of truth; the index is a regenerable lens. Don't build ahead of a real query. [coded-queries](experiments/2026-06-01-coded-queries/) quantified the emptiness: **23/24 relation edges dangle** today.
  **When it lands:** index relations on the subsidiary side (`parent`), reverse-scanned. Consumption (P7) found `parent`/`owns` are populated **one-sided** — `delighted.parent: [qualtrics.com]` carries the link, but `qualtrics.owns` doesn't list Delighted. A JOIN that trusts `owns` for symmetry misses real edges: build the graph from `parent` (reverse-scanned across the corpus), treat `owns` as best-effort.

- **Traction module / verb** `[idea]` `[xl]` `[parked]` `[@brian]`
  Still desparately need more signals on growth / traction - ways of answering questions like "is this a formidable competitor?" or "do they have any real leadership in the markets they operate in?". Been thinking that this is _not_ a responsibility of this Web Research system, but I still haven't found a good home for it. There are some tools for this in the Teleprescribe Venture project's `agent-workflows` (`competitive-traction`), but those were designed in the past - and are not able to be used for other projects. Much of the output of a "Traction" style tool wouldn't live directly in the `store` because it's not all `State`, but rather `Signals`, and some `Judgements` - but identifying traction signals for a company is definitely something most projects researching projects in any market would want to do, so it would be nice to provide something for them. Still needs further design thinking to get right. 
  This would be primarily designed to get an idea of a company's "market share" (which is _rarely_ directly observable) - but we could get an idea of this through signals like:
  - Funding / growth trajectory / M&A
  - SEO/AIO rankings
  - Published / public revenue figures
  - People / leadership ("is the leadership team legit?")
  - Predictions about their roadmap (can often get an idea of this by looking at job descriptions on career pages)
  - Notable differentiation from their competitors

- **Historical diffs & Wayback machine usage** `[idea]` `[xl]` `[parked]` `[@brian]`
  To get a better understanding of each company, use the Wayback Machine to look at the website from 3-months ago, 12 months ago, and 3 years ago to see how it's evolved.

- **Monitoring** `[idea]` `[xl]` `[parked]` `[@brian]`
  Add capabilities to monitor changes on key parts of a companies website -- like new product launches, significant rebrands, price changes on certain products, etc. 
