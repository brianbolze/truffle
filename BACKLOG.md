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
  
### Presentation surface

- **Corpus index brief — `render.py --index`** `[idea]` `[s]`
  One self-contained HTML page: every profiled company (logo, name, one-liner, per-layer clocks) linking to its brief — the render-twin of `store.py health`, and the store's only human front door beyond the file tree. Everything computed at render time; nothing baked.
  **Act when:** a human asks "what's in the store?" and the CLI answer feels thin — or before the 2026-06-12 Scott demo if Brian wants the 5-second "this is real" artifact.

- **Tune the brief for a brand-strategy reader** `[idea]` `[sm]`
  The brief's first external human (Scott Witt / Parlance) values language extraction, competitor patterns, and visual signals; check whether briefs lead with voice + positioning or with classification fields, and reorder only if the fix is small. Yardstick: lands with a creative director in 5 seconds.
  **Act when:** after the 06-12 meeting — let Scott's actual reactions pick the changes; don't pre-polish.

- **Cross-company comparison view** `[idea]` `[parked]`
  "Compare X and Y" today = two brief links + chat synthesis, and that's right: a side-by-side artifact drags in exactly the cross-company price/unit normalization judgments the store refuses to hold; cohort SQL covers the structured case.
  **Act when:** a human consumer asks for the side-by-side twice (rule of two) — and then intra-cohort only.

- **CoWork as a consumer surface** `[tbd]` `[parked]`
  CoWork runs sessions in a Linux VM: no shell env (mitigated — the skill carries a canonical-path fallback), an unreliable personal-skill registry, and a documented iCloud-stub hazard that would surface as silent store false-negatives. Desk findings + the live probe to run first: [`experiments/2026-06-10-cowork-bridge/`](experiments/2026-06-10-cowork-bridge/FINDINGS.md).
  **Act when:** post-06-12 — run the live stub probe; clean → package read-only `/query-companies` as a plugin; stubbed → store-location decision precedes any bridge.

### Schema & taxonomy decisions

- **Revisit 2.2's "no `founders`/`legal_entity` field" call — a cohort consumer has now appeared** `[tbd]` `[sm]`
  2.2 deliberately kept both out (`legalName` folds into `aliases`; founders "stay at the deep-research edge," prose-only) "until a cohort consumer defines the right shape." The 2026-06-01 Teleprescribe telehealth deep-research cohort is that consumer — all 6 reports leaned on founders + legal entity, several KB-load-bearing (PeterMD "no real Peter"; Remedy → founder Haris Memon). **But the evidence cuts both ways:** most founders were dug *externally* (Sunbiz/news), not from JSON-LD — which is exactly *why* 2.2 edged them; only site-derivable ones are true store-state.
  **Decide:** promote a queryable `legal_entity` out of `aliases` (cheap, low-risk), and/or a `founders` field filled *only when site-derivable* — never one that needs external research to fill, which would break the site-derived-state line.

### Capture quality

- **Light, honesty-preserving cleaning pass on payload markdown** `[idea]` `[md]` `[@brian]`
  Captured `.md` is a raw Firecrawl dump (47.5% blank lines; animated stat-counter digit-columns; leaked VWO/JS + consent blobs; hard-break `\\` residue) — the "cleaned" files are byte-identical to raw. Researched → [`payload-cleaning.md`](_design/references/payload-cleaning.md): a **subtractive + whitespace-only** ruleset (delete noise lines, never reword) cuts ~19% of bytes while keeping every content byte verbatim; decision lean = strip chrome, don't section-tag.
  **Act when:** de-risk first — `experiments/<date>-payload-clean/` over the 111 existing files, prove zero content-line loss, *then* touch SCHEMA / fc.py.

- **Hero-image module is physical-product-only** `[idea]` `[s]`
  `fc.py hero` + the step-2.5 "offerings.md with flagship product images" option presume a physical render (bottle / vial / pen). On a software/API company there's nothing to capture — the Stripe run (2026-06-04) path-scored 15 candidates that were all lifestyle photography / demo-merchant goods / UI mockups (every score 0.0); the run correctly returned **N/A**, but the guided menu offered it anyway. **Cheap fix:** in the step-2.5 batch, suppress (or label "physical products only") the hero-image option when `offering_category` carries no `Physical Products / Hardware` / CPG — same logic likely applies to `Marketplace / Platform` and `Financial / Fintech`.

### Parked

- **Web design quality / site-presentation rating** `[idea]` `[parked]` `[@brian]`
  Rating observable site-presentation quality from capture screenshots failed calibration three times (2026-06-09): raters agree with each other (≤1-bucket spread) but sit ~1–2 buckets above Brian — "coherent template" reads `strong` where Brian reads `basic`, `weak` never fires, and slick dark-gradient template aesthetics read `excellent` (Infusive, Brian 2.5). Rule-tightening is exhausted; the anchors themselves are off. Evidence: [v1](experiments/2026-06-09-site-presentation-quality/FINDINGS.md) · [v2](experiments/2026-06-09-site-presentation-quality-v2/FINDINGS.md) · [v3 bottom-heavy fail](experiments/2026-06-09-site-presentation-quality-v3/FINDINGS.md). What survives: the evidence *cues* (template/stock/render-defect reads) were accurate — they stay welcome as `Visual & brand impression` prose; the bucket is what's parked. The depth-gate use case never needed it (gate on observable site substance instead).
  **Act when:** a consumer needs the rating itself (Notion auto-fill, cohort comparison) — then try **anchored comparison** (place against fixed Brian-rated reference screenshots) before any absolute scale; v3 showed relative ordering is nearly right even when absolute labels aren't.

- **Rung-3 SQLite index — corpus lens landed; relations graph still parked** `[idea]` `[xl]` `[parked]`
  The derived-index *mechanism* graduated 2026-06-04 for **telehealth cohort aggregation** and broadened 2026-06-10 into the **corpus-wide lens**: [`scripts/build_db.py`](scripts/build_db.py) builds `_out/store.db` (`companies`, corpus `offerings`, folder-level `coverage`, `_meta` freshness/caveats, plus cohort-gated views such as `telehealth_full`), fenced against the price-magnitude / naked-count / cross-type ranking footguns the [sqlite-aggregation probe](experiments/2026-06-04-sqlite-aggregation/) found, `--check`-guarded; [QUERYING Recipe 7](QUERYING.md). The live consumer that earned it was **Brian's Beekeeper browsing + ad-hoc SQL** (latency was never the axis — the lighter `store.py` reader's only edge); the probe's own gating condition (a) thus held. Markdown stays source of truth; the `.db` is gitignored + regenerable.
  **Still parked — the *relations/discovery* graph**, the item's original trigger: [coded-queries](experiments/2026-06-01-coded-queries/) quantified the emptiness (**23/24 relation edges dangle**), so there's no JOIN to serve yet. **When it lands:** index relations on the subsidiary side (`parent`), reverse-scanned. Consumption (P7) found `parent`/`owns` are populated **one-sided** — `delighted.parent: [qualtrics.com]` carries the link, but `qualtrics.owns` doesn't list Delighted. A JOIN that trusts `owns` for symmetry misses real edges: build the graph from `parent` (reverse-scanned across the corpus), treat `owns` as best-effort.

- **Traction module / verb** `[idea]` `[xl]` `[parked]` `[@brian]`
  Still need ways of answering questions like "is this a formidable competitor?" or "do they have real leadership in the markets they operate in?" The direction is now clearer: `tools/` owns reusable source-capture primitives (SERP, Wayback, Trustpilot, Trends, Exa) and source-aware consumers; project-specific traction reads stay above them. Do **not** promote a general traction score/verb until repeat captures and comparator layers prove which axes are actually comparable.
  This would be primarily designed to get an idea of a company's "market share" (which is _rarely_ directly observable) - but we could get an idea of this through signals like:
  - Funding / growth trajectory / M&A
  - SEO/AIO rankings
  - Published / public revenue figures
  - People / leadership ("is the leadership team legit?")
  - Predictions about their roadmap (can often get an idea of this by looking at job descriptions on career pages)
  - Notable differentiation from their competitors

- **Historical diffs & Wayback machine usage** `[idea]` `[xl]` `[parked]` `[@brian]`
  To get a better understanding of each company, use the Wayback Machine to look at the website from 3-months ago, 12 months ago, and 3 years ago to see how it's evolved. The source-capture home for this is now [`tools/BACKLOG.md`](tools/BACKLOG.md): Wayback content fetch + diff should land there as a reusable primitive before this becomes a store/module workflow.

- **Monitoring** `[idea]` `[xl]` `[parked]` `[@brian]`
  Add capabilities to monitor changes on key parts of a companies website -- like new product launches, significant rebrands, price changes on certain products, etc. 
