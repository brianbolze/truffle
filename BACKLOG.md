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

- **`log.md` as the Signals-layer shape — probe** `[idea]` `[md]`
  Google's [Open Knowledge Format](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/) (v0.1, 6/12) is near-identical to our store — markdown + frontmatter, file-path = identity, AI-at-ingestion — independent validation of the core bet. Its one shape we lack: an optional per-concept **append-only `log.md`** beside the snapshot. That's a candidate answer to the architecture's deferred **Signals-layer** open question (the "domain-keyed files" option): dated events (funding, launches, rebrands) append to `store/<domain>/log.md` while `profile.md` stays a clean snapshot — keeping Signals *out* of State. Also worth watching: OKF's open-source self-contained HTML graph **visualizer** for the long-horizon Visualization phase.
  **Act when:** the Signals-layer decision comes up (or a consumer needs dated events) — `experiments/<date>-signals-logmd/` testing the shape on 2–3 companies with real events *before* touching SCHEMA. Don't adopt the OKF spec wholesale: no interop consumer earns it, and conforming would pressure the State/Signals/Judgments + verbatim-provenance opinions OKF deliberately omits. The [traction frame](_design/2026-06-14-traction-frame.md) (Open Q#1) now engages this storage decision directly.
  
### Presentation surface

*Substantially reworked for the 6/12 Scott demo (now mostly shipped): lens-package split, quieted chrome (Source Serif 4 + DM Mono, near-white paper, "chrome serves content"), promoted brief renderer, `--index` corpus front door, `--all` pre-warm, classification datasheet demoted to a chip strip, `compare.py`. Durable record: [`_design/2026-06-12-presentation-layer.md`](_design/2026-06-12-presentation-layer.md). Items below are what's still open.*

- **Tune the brief for a brand-strategy reader** `[idea]` `[md]`
  The brief's first external human (Scott Witt / Parlance) values language extraction, competitor patterns, and visual signals; check whether briefs lead with voice + positioning or with classification fields, and reorder only if the fix is small. Yardstick: lands with a creative director in 5 seconds. 6/12 call **confirmed the reader profile** — "guitar hero, not fender" (non-technical, connector-oriented) — but the tool demo was **deferred to a part-2 session (week of 6/16)**, so Scott still hasn't seen a brief.
  **Act when:** the part-2 demo — let Scott's live reactions pick the changes; don't pre-polish. What to *lead* that session with: [`_temp/2026-06-12-scott-demo-beyond-town.md`](_temp/2026-06-12-scott-demo-beyond-town.md) — Scott uses Town (an AI chief-of-staff) and has seen Brian's Town-generated deck ([`_temp/competitor_deck.html`](_temp/competitor_deck.html)), which Town built *entirely from Brian's substrate* (its words: "I did not do any live web research"). So the demo frames Town as witness, not rival: these tools are the capture layer Town stood on and can't reach — provenance pull + `compare`, not "more AI output."

### Capture quality

*The capture-trust pass (SCHEMA 2.6) shipped from the [model bakeoff](experiments/2026-06-13-research-company-model-bakeoff/FINDINGS.md): `legal_entity` promoted out of `aliases` (founders stay prose-only); the `parent`/`owns` evidence bar sharpened (affiliation ≠ ownership); the `logos:{}` slot-measurement lint enforced (`fc.py`/`check_candidates.py`); the completeness self-check landed scratch-only in [skill step 7](skills/research-company/SKILL.md); offerings activation needed no change (the consumer-pull rule was already right). The thread below is the remaining **observable-substance read** (evidence/floor, not score): is a company worth depth at all.*

*Visual-quality evidence **graduated 2026-06-14** → the [`visual.md` module](modules/VISUAL.md): the `/visual-evidence` skill mines cached or browser-re-rendered screenshots into blind, cited cards + a `Visual & brand impression` (capture tiers `scripts/tile.py` + `scripts/shoot.py`; lint `scripts/visualcheck.py`, which **fails on any `score:` field** — the parked line below is mechanical now, not a promise). Validated on goinfusive (38 cited cards, correctly un-seduced by the dark-gradient gloss; QA→Tier-B proven on functionhealth's grey WebGL hero). Frame + acceptance bar: [`FRAME.md`](experiments/2026-06-13-visual-quality-graduation-frame/FRAME.md) · [`SUCCESS_CRITERIA.md`](experiments/2026-06-13-visual-quality-graduation-frame/SUCCESS_CRITERIA.md).*

- **Adaptive capture-depth — substance floor (probe first)** `[idea]` `[md]` `[@brian]`
  Same observable-substance thread: a generic, cheap, *pre-capture* read of "real company vs. low-signal slop" to gate how much attention a company earns. Engine-owned State; the viewer-relative salience score stays consumer-owned (its eventual consumer is the parked **Monitoring** item). Fail safe toward capturing — skip only on high-confidence slop. Frame: [`experiments/2026-06-13-adaptive-capture-depth-frame/FRAME.md`](experiments/2026-06-13-adaptive-capture-depth-frame/FRAME.md).
  **Act when:** de-risk first — a probe testing whether cheap homepage signal predicts substance-vs-slop on a hand-labeled set, *before* any build.

- **Light, honesty-preserving cleaning pass on payload markdown** `[idea]` `[md]` `[@brian]`
  Captured `.md` is a raw Firecrawl dump (47.5% blank lines; animated stat-counter digit-columns; leaked VWO/JS + consent blobs; hard-break `\\` residue) — the "cleaned" files are byte-identical to raw. Researched → [`payload-cleaning.md`](_design/references/payload-cleaning.md): a **subtractive + whitespace-only** ruleset (delete noise lines, never reword) cuts ~19% of bytes while keeping every content byte verbatim; decision lean = strip chrome, don't section-tag.
  **Act when:** de-risk first — `experiments/<date>-payload-clean/` over the 111 existing files, prove zero content-line loss, *then* touch SCHEMA / fc.py.

- **Hero-image module is physical-product-only** `[idea]` `[s]`
  `fc.py hero` + the step-2.5 "offerings.md with flagship product images" option presume a physical render (bottle / vial / pen). On a software/API company there's nothing to capture — the Stripe run (2026-06-04) path-scored 15 candidates that were all lifestyle photography / demo-merchant goods / UI mockups (every score 0.0); the run correctly returned **N/A**, but the guided menu offered it anyway. **Cheap fix:** in the step-2.5 batch, suppress (or label "physical products only") the hero-image option when `offering_category` carries no `Physical Products / Hardware` / CPG — same logic likely applies to `Marketplace / Platform` and `Financial / Fintech`.

### Parked

- **Visual-quality SCORE — parked (calibration offset)** `[idea]` `[parked]` `[@brian]`
  The *score* (not the evidence — that graduated; see Capture quality) failed calibration through v5: raters agree with each other (≤1-bucket spread) but sit ~1–2 buckets above Brian — "coherent template" reads `strong` where Brian reads `basic`, `weak` never fires, slick dark-gradient reads `excellent` (Infusive, Brian 2.5). Rule-tightening is exhausted; the anchors themselves are off. Evidence: [v1](experiments/2026-06-09-site-presentation-quality/FINDINGS.md) · [v2](experiments/2026-06-09-site-presentation-quality-v2/FINDINGS.md) · [v3](experiments/2026-06-09-site-presentation-quality-v3/FINDINGS.md) · [v5](experiments/2026-06-13-visual-quality-v5-capture-clean-blind-judgment/FINDINGS.md). Frame: [graduation frame](experiments/2026-06-13-visual-quality-graduation-frame/FRAME.md).
  **Act when:** a consumer needs the *score* itself (Notion auto-fill, cohort comparison) — try **anchored comparison** (place against fixed Brian-rated references) or deterministic caps over pruned evidence before any absolute scale; relative ordering is already near-right.

- **Rung-3 SQLite index — corpus lens landed; relations graph still parked** `[idea]` `[xl]` `[parked]`
  The derived-index *mechanism* graduated 2026-06-04 for **telehealth cohort aggregation** and broadened 2026-06-10 into the **corpus-wide lens**: [`scripts/build_db.py`](scripts/build_db.py) builds `_out/store.db` (`companies`, corpus `offerings`, folder-level `coverage`, `_meta` freshness/caveats, plus cohort-gated views such as `telehealth_full`), fenced against the price-magnitude / naked-count / cross-type ranking footguns the [sqlite-aggregation probe](experiments/2026-06-04-sqlite-aggregation/) found, `--check`-guarded; [QUERYING Recipe 7](QUERYING.md). The live consumer that earned it was **Brian's Beekeeper browsing + ad-hoc SQL** (latency was never the axis — the lighter `store.py` reader's only edge); the probe's own gating condition (a) thus held. Markdown stays source of truth; the `.db` is gitignored + regenerable.
  **Still parked — the *relations/discovery* graph**, the item's original trigger: [coded-queries](experiments/2026-06-01-coded-queries/) quantified the emptiness (**23/24 relation edges dangle**), so there's no JOIN to serve yet. **When it lands:** index relations on the subsidiary side (`parent`), reverse-scanned. Consumption (P7) found `parent`/`owns` are populated **one-sided** — `delighted.parent: [qualtrics.com]` carries the link, but `qualtrics.owns` doesn't list Delighted. A JOIN that trusts `owns` for symmetry misses real edges: build the graph from `parent` (reverse-scanned across the corpus), treat `owns` as best-effort.

- **Traction module / verb — now framed** `[idea]` `[xl]` `[parked]` `[@brian]`
  The problem is defined: [`_design/2026-06-14-traction-frame.md`](_design/2026-06-14-traction-frame.md). It scopes the first graduation (per-company, axis-specific *evidence* — no blend, no verdict), keeps the formidability *judgment* consumer-owned, defers comparative/cohort to a sibling frame, and leaves the storage shape (incl. OKF `log.md`) open. Primary prior art is the live Teleprescribe `traction v2` layer; the older `agent-workflows/competitive-traction` is superseded. The original signal wishlist (funding/M&A, SEO/AIO, revenue, leadership, roadmap-via-jobs, differentiation) now lives in the frame.
  **Act when:** the design brainstorm picks up the frame's Open Questions — start with the comparability primitive ([`tools/BACKLOG.md`](tools/BACKLOG.md)) and the storage shape.

- **Historical diffs & Wayback machine usage** `[idea]` `[xl]` `[parked]` `[@brian]`
  To get a better understanding of each company, use the Wayback Machine to look at the website from 3-months ago, 12 months ago, and 3 years ago to see how it's evolved. The source-capture home for this is now [`tools/BACKLOG.md`](tools/BACKLOG.md): Wayback content fetch + diff should land there as a reusable primitive before this becomes a store/module workflow.

- **Monitoring** `[idea]` `[xl]` `[parked]` `[@brian]`
  Add capabilities to monitor changes on key parts of a companies website -- like new product launches, significant rebrands, price changes on certain products, etc. 

- **CoWork as a consumer surface** `[tbd]` `[parked]`
  CoWork runs sessions in a Linux VM: no shell env (mitigated — the skill carries a canonical-path fallback), an unreliable personal-skill registry, and a documented iCloud-stub hazard that would surface as silent store false-negatives. Desk findings + the live probe to run first: [`experiments/2026-06-10-cowork-bridge/`](experiments/2026-06-10-cowork-bridge/FINDINGS.md).
  **Act when:** post-06-12 — run the live stub probe; clean → package read-only `/query-companies` as a plugin; stubbed → store-location decision precedes any bridge.
