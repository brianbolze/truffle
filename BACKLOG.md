# Backlog

System-level weaknesses, ideas, and TBDs for the engine itself — things that would change the **schema, the verbs, or the workflow**. A living, curated list (capped, not append-only). Per-company capture learnings live in that company's `site_notes` (in `profile.md`), never here.

**Not this file:**
- [`SCHEMA.md`](SCHEMA.md) / [`TAXONOMIES.md`](TAXONOMIES.md) — the store contract. A hard rule that cost a real lesson lands there as a one-liner, not here.
- [`_design/`](_design/) — frame, architecture, references. Durable intent.
- **Notion Roadmap** (the *Truffle — Teamspace Home* teamspace) — big, user-facing initiatives, grouped by [Pillar / Theme](https://app.notion.com/p/getdoro/Product-Pillars-Themes-afdbc4660a084f009ac2df226c3dfd23) + status. This file keeps the *smaller* engine items + **system hardening** (schema / verbs / workflow). When a backlog idea grows into a real user-facing feature, it graduates to the [Roadmap](https://app.notion.com/p/getdoro/2362eca6edf441c18aaa7c0105c4cc23?v=d0d7ab1da3734cf097a2b14408b1c187).

**Item format.** A bold punchline + tags on one scannable line (tags in this order), then 1–3 tight sentences. An optional **Act when** line names the trigger that graduates the item — point at cited experiments rather than restating them.
- **kind** — `[weakness]` gap likely to bite · `[idea]` possible improvement · `[bug]` confirmed defect · `[tbd]` pending decision · `[simplification]` removes surface area / prescriptiveness
- **provenance** — `[@brian]` added / explicitly-approved / co-authored by Brian; untagged = agent-added, subject to review
- `[parked]` = deferred on purpose

If they clearly map to our strategic pillars / themes, tag it with one:

**Bias to remove.** Default is to add — resist it. Before logging, look for a way to *consolidate* or *cut* instead; hunt `[simplification]`s at least as hard as features. If an entry adds surface, note what it replaces.

**Graduate on a trigger, not to clear the list.** Most items sit until a real capture confirms them (≥2 sightings) or their **Act when** fires — then move to a `_design/` doc or just do it.

**Soft cap: ≤15 open items.** Over that, close/cut/promote 2 before adding 1. Stale items (>60 days untouched) default-cut at the next review.

---

- **Automatic retro** `[idea]` `[@brian]`
  Adjust the system / `research-company` verb such that when an agent has a really messy / ineffective capture - they automatically write a retro (or, maybe suggest the user spawn a new session for that retro... idk... I still want the user to get their results quickly - without waiting for the retro to complete...) -- that gets written to _design/retro/ -- following a consistent format / guideline.

- **Skimmable `log.md` format for Signals-layer; OKF visualizer still worth watching** `[idea]` `[md]`
  The architecture's deferred **Signals-layer storage** question (Open Q#1) is now answered: company-grain signals land at `store/<domain>/signals/<source_type>/<captured_at>.json` (per-source verbatim envelopes — committed to the [architecture](_design/2026-05-30-architecture.md), diffed by `signal_delta.py`), **not** a per-concept `log.md`. A human-readable append-only `log.md` of dated events (funding, launches, rebrands) beside `profile.md` remains a *future* option, no longer the open decision. Independent watch: Google [OKF](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/)'s open-source self-contained HTML graph **visualizer** for the long-horizon Visualization phase (its store shape — markdown + frontmatter, file-path = identity — already validates our core bet).
  **Act when:** a consumer needs human-readable dated events, *or* the OKF visualizer matures — don't adopt OKF conformance (no interop consumer earns it; it'd pressure our State/Signals/Judgments + verbatim-provenance opinions OKF omits).
  
- **Run-record coverage is unaudited** `[weakness]` `[@brian]`
  Run records ([`modules/RUNS.md`](modules/RUNS.md)) are written by an agent following a prose skill-step at capture end — no enforcement, no audit. So a missing `store/<slug>/runs/*.json` is ambiguous: pre-`0.1` history, a crashed run, **or the agent simply skipped the step** — that third meaning quietly dents the health/diagnostics signal the layer exists to provide (the Steward's "looks complete but isn't"). The no-Stop-hook call is deliberate (living infra, anti-Doro), so the gap is *coverage*, not the writer.
  **Act when:** the telemetry is actually consumed (an aggregator over `runs/`) **and** coverage looks holey — add a cheap audit (e.g. a `store.py health` flag for a completed capture whose `captures/<date>/` has no paired run-record), never a watcher.

### Capture quality

- **Fix / improve Exa findSimilar tool** `[weakness]` `[sm]` `[brian]`
  After a few experiments, we've found it to be inconsistent for finding similar companies - ie. competitors / same neighborhood. It often just matches on similar naming (e.g. "Honey Health", "Honeybee Health" for "Hone Health"), etc. We want to see if we can salvage it / adjust inputs so we can still use it as a cross-shop signal / neighbor company discovery tool.
  **2026-06-20 research + partial fix (probes + docs):** findSimilar is **anchor-name-bound and not salvageable as a cross-shop signal** — and it *silently ignores* its filter params (`includeText`/`excludeText`/`excludeDomains`) when `category` is set, so there's no API-side topic knob to tune. The salvage that works is a **different endpoint**: Exa `/search` with a function-description query + `category:company` returns real companies (not name-collisions), but recall of a *known/curated* set is low — it's a **net-new discovery** input, not a known-brand cross-shop tool. Full write-up + probe log: [`experiments/2026-06-20-cohort-discovery/references/exa-api-capabilities-and-probes-2026-06-20.md`](experiments/2026-06-20-cohort-discovery/references/exa-api-capabilities-and-probes-2026-06-20.md). **Landed (2026-06-20):** (a) `--exclude-domains` enforced caller-side in [`tools/exa_similar.py`](tools/exa_similar.py) (was void under `category`) + silently-ignored params documented; (b) **new sibling tool [`tools/exa_search.py`](tools/exa_search.py)** (Exa `/search`, `tool: exa_search`) — query→company discovery (`type` pinned `neural`, same excludeDomains caller-side handling), the mode that returns real companies. Kept as a **separate** tool, not merged, because `scripts/signals.py` resolves `tools/{source_type}.py` 1:1. **Remaining:** cross-shop of *known* brands stays on the owned-`/vs` + review-co-shop path (run-030 W1/W2), not Exa; optional later — wire `exa_search` into the `cohort-discovery` bake-off, a `/contents`-summary post-filter, and a shared `_exa.py` only if a 3rd endpoint lands.

- **Adaptive capture-depth — substance floor (probe first)** `[idea]` `[md]` `[@brian]`
  Same observable-substance thread: a generic, cheap, *pre-capture* read of "real company vs. low-signal slop" to gate how much attention a company earns. Engine-owned State; the viewer-relative salience score stays consumer-owned (its eventual consumer is the parked **Monitoring** item). Fail safe toward capturing — skip only on high-confidence slop. Frame: [`experiments/2026-06-13-adaptive-capture-depth-frame/FRAME.md`](experiments/2026-06-13-adaptive-capture-depth-frame/FRAME.md).
  **Act when:** de-risk first — a probe testing whether cheap homepage signal predicts substance-vs-slop on a hand-labeled set, *before* any build.

- **Light, honesty-preserving cleaning pass on payload markdown** `[idea]` `[md]` `[@brian]`
  Captured `.md` is a raw Firecrawl dump (47.5% blank lines; animated stat-counter digit-columns; leaked VWO/JS + consent blobs; hard-break `\\` residue) — the "cleaned" files' *body* is byte-identical to raw (behind a `source_url` header). Researched → [`payload-cleaning.md`](_design/references/payload-cleaning.md): a **subtractive + whitespace-only** ruleset (delete noise lines, never reword) cuts ~19% of bytes while keeping every content byte verbatim; decision lean = strip chrome, don't section-tag.
  **Act when:** de-risk first — `experiments/<date>-payload-clean/` over the 111 existing files, prove zero content-line loss, *then* touch SCHEMA / fc.py.

- **Hero-image module is physical-product-only** `[idea]` `[s]`
  `fc.py hero` + the step-2.5 "offerings.md with flagship product images" option presume a physical render (bottle / vial / pen). On a software/API company there's nothing to capture — the Stripe run (2026-06-04) path-scored 15 candidates that were all lifestyle photography / demo-merchant goods / UI mockups (every score 0.0); the run correctly returned **N/A**, but the guided menu offered it anyway. **Cheap fix:** in the step-2.5 batch, suppress (or label "physical products only") the hero-image option when `offering_category` carries no `Physical Products / Hardware` / CPG — same logic likely applies to `Marketplace / Platform` and `Financial / Fintech`.

- **Re-arming modal isn't *recovered* by single-pass `--dismiss`** `[weakness]`
  2026-06-16 sanity re-run: sequoia + functionhealth cleared cleanly, but gethealthspan's "10% off" modal *re-armed* during the ~10s warm-scroll after the initial dismiss (the probe's <1s dismiss→screenshot window never saw it). It now fails **loud** two ways — `scroll_locked: true` *and* `dismiss_cleared: false` (the no-op guard measures overlay footprint after warm-scroll) — so the operator excludes/caveats correctly. What's still missing is *recovery*: the recoverability the 06-16 `/tmp/reshoot.py` prototype showed is gone.
  **Act when:** a second site re-arms during warm-scroll — try a second `dismiss()` pass right before the scroll-lock/footprint check, or a periodic re-dismiss inside the warm-scroll loop. Don't add a "modal is timed" heuristic — that's denylist drift.

- **Tier-B per-page manifest vs the root tiler manifest can disagree** `[weakness]`
  `tile.py` writes the roll-up `captures/<date>/tiles/manifest.json` (`source: tile`); `shoot.py` writes a per-page `tiles/<page>/manifest.json` (`source: shoot`, now with `dismissed`/`dismiss_cleared`/`scroll_locked`/`overview`). When Tier-B re-renders a page *taller* than the cached shot, its last-tile offset moves — the per-page manifest is correct but the root manifest still points the page's last tile at the old offset (a dangling ref for a glob-based consumer). Seen on ro-co (3 sightings: ro-co/mydrhank/doordash all left a stale or orphan manifest). The orphan-*tile* half is fixed (shoot.py clears its own `tile-*.png`/overview before writing); the manifest-reconciliation half isn't. Real work, not a one-liner.
  **Act when:** a consumer actually reads the root manifest's per-page tile geometry (today the skill assembles the active list from the per-page shoot manifest, so it's latent) — then have the re-tile reconcile the root manifest, or have `shoot.py` update the affected page's entry.

- **`contrast_with` is lint-checked for existence, never that the tile *shows* the contrast** `[weakness]`
  `visualcheck.py` rule 2 confirms a card's `contrast_with` tile exists, is non-self, and is active — but a blind judge can cite a contrast tile that doesn't actually contain the claimed element (parlance `color_04` pointed at a tile showing a different card; caught by the sighted spot-check, passed lint). Orthogonal to Tier-B — a falsifiability hole in the blind→lint chain. Single sighting; agent-flagged for review.
  **Act when:** a second mis-cite shows up — candidate guard is hard (lint can't see pixels); more likely a SKILL spot-check line ("verify each `contrast_with` shows the contrast") than code.

### Parked

- **Visual-quality SCORE — parked (calibration offset)** `[idea]` `[parked]` `[@brian]`
  The *score* (not the evidence — that graduated; see Capture quality) failed calibration through v5: raters agree with each other (≤1-bucket spread) but sit ~1–2 buckets above Brian — "coherent template" reads `strong` where Brian reads `basic`, `weak` never fires, slick dark-gradient reads `excellent` (Infusive, Brian 2.5). Rule-tightening is exhausted; the anchors themselves are off. Evidence: [v1](experiments/2026-06-09-site-presentation-quality/FINDINGS.md) · [v2](experiments/2026-06-09-site-presentation-quality-v2/FINDINGS.md) · [v3](experiments/2026-06-09-site-presentation-quality-v3/FINDINGS.md) · [v5](experiments/2026-06-13-visual-quality-v5-capture-clean-blind-judgment/FINDINGS.md). Frame: [graduation frame](experiments/2026-06-13-visual-quality-graduation-frame/FRAME.md).
  **Act when:** a consumer needs the *score* itself (Notion auto-fill, cohort comparison) — try **anchored comparison** (place against fixed Brian-rated references) or deterministic caps over pruned evidence before any absolute scale; relative ordering is already near-right.

- **Relations graph for Rung-3 SQLite index** `[idea]` `[xl]` `[parked]`
  The derived-index *mechanism* graduated 2026-06-04 for **telehealth cohort aggregation** and broadened 2026-06-10 into the **corpus-wide lens**: [`scripts/build_db.py`](scripts/build_db.py) builds `_out/store.db` (`companies`, corpus `offerings`, folder-level `coverage`, `_meta` freshness/caveats, plus cohort-gated views such as `telehealth_full`), fenced against the price-magnitude / naked-count / cross-type ranking footguns the [sqlite-aggregation probe](experiments/2026-06-04-sqlite-aggregation/) found, `--check`-guarded; [QUERYING Recipe 7](QUERYING.md). The live consumer that earned it was **Brian's Beekeeper browsing + ad-hoc SQL** (latency was never the axis — the lighter `store.py` reader's only edge); the probe's own gating condition (a) thus held. Markdown stays source of truth; the `.db` is gitignored + regenerable.
  **Still parked — the *relations/discovery* graph**, the item's original trigger: [coded-queries](experiments/2026-06-01-coded-queries/) quantified the emptiness (**23/24 relation edges dangle**), so there's no JOIN to serve yet. **When it lands:** index relations on the subsidiary side (`parent`), reverse-scanned. Consumption (P7) found `parent`/`owns` are populated **one-sided** — `delighted.parent: [qualtrics.com]` carries the link, but `qualtrics.owns` doesn't list Delighted. A JOIN that trusts `owns` for symmetry misses real edges: build the graph from `parent` (reverse-scanned across the corpus), treat `owns` as best-effort.

- **"Card" layer + cohort frame for Traction module / verb** `[xl]` `[parked]` `[@brian]`
  v1 of the per-company evidence layer shipped 2026-06-15 (the frame's first graduation: axis-specific evidence, no blend, no verdict): `tools/signal_delta.py` (envelope comparator — trustpilot/serpapi/trends/wayback branches, with `sec_edgar` added 2026-06-22; deltas + comparability vetoes; no score by construction) + `tools/sec_edgar.py` (keyless first-party funding — ticker→State, Form-D/filing→Signal, `name_match_unconfirmed` guard) + `scripts/signals.py` (the store writer: persist/run/import), with the `store/<domain>/signals/<source_type>/<captured_at>.json` path committed to the [architecture](_design/2026-05-30-architecture.md). Front door: [`SIGNALS.md`](SIGNALS.md) · frame: [`_design/2026-06-14-traction-frame.md`](_design/2026-06-14-traction-frame.md) · approach: [`_design/2026-06-15-traction-approach.md`](_design/2026-06-15-traction-approach.md).
  **Still parked:** the card-layer machinery (`modules/SIGNALS.md` schema-as-contract + lint + sole-writer + SQLite lens; the `evidence_label`/`signal_polarity` enums) — graduate only when an automated writer **and** a second consumer exist; the comparative/cohort read (its own sibling frame); the formidability *judgment* (stays consumer-side).

- **Historical diffs & Wayback machine usage** `[idea]` `[xl]` `[parked]` `[@brian]`
  To get a better understanding of each company, use the Wayback Machine to look at the website from 3-months ago, 12 months ago, and 3 years ago to see how it's evolved. The `tools/` primitives now exist — `wayback.py diff` (content fetch + diff) and `signal_delta.py`'s wayback branch (presence/snapshot/content-digest over two tenure captures); the remaining work is a store/module workflow that consumes them across the 3mo/12mo/3yr spread.

- **Monitoring** `[idea]` `[xl]` `[parked]` `[@brian]`
  Add capabilities to monitor changes on key parts of a companies website -- like new product launches, significant rebrands, price changes on certain products, etc. Should do a quick experiment with Firecrawl's new `/monitoring` API.

- **CoWork as a consumer surface** `[tbd]` `[parked]`
  CoWork runs sessions in a Linux VM: no shell env (mitigated — the skill carries a canonical-path fallback), an unreliable personal-skill registry, and a documented iCloud-stub hazard that would surface as silent store false-negatives. Desk findings + the live probe to run first: [`experiments/2026-06-10-cowork-bridge/`](experiments/2026-06-10-cowork-bridge/FINDINGS.md).
  **Act when:** post-06-12 — run the live stub probe; clean → package read-only `/query-companies` as a plugin; stubbed → store-location decision precedes any bridge.
