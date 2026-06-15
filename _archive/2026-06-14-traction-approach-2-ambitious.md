# APPROACH — External traction Signals

Date: 2026-06-14 · Status: solution proposal (Prototyping → Proposal). Companion to the [traction frame](2026-06-14-traction-frame.md); answers its Open Questions #1–#4 + #6. Reasoned **fresh** under the posture revised today — the engine now owns the generic Signals machinery, a Signals-storage home is in scope, and a regenerable/deletable index is an *allowed lens*. Propose, not build: no SCHEMA edits, no tool code here.

## 30-second skim — the calls

- **#1 Storage** — **domain-keyed `store/<domain>/signals/cards.jsonl`** (append-only cards beside `profile.md`, never inside it), with `raw/` kept verbatim and a **gitignored SQLite lens deferred** until the maps consumer earns it. Category-grain → architecture's reserved `cohorts/<category-slug>/`, **unbuilt in v1**.
- **#3 Comparator** — **one committed `tools/signal_delta.py`** (renamed off the existing `compare.py`) that **diffs cards, not raw envelopes**, source-aware branches, *level-read then delta*, emits deltas + comparability vetoes **only — structurally incapable of a score.**
- **#2 + #6 Grain & ownership** — **the card carries its own `grain`; v1 emits only `grain=company`.** Engine graduates the *generic convention* (card schema + enums + comparator + the domain-keyed home); the project keeps every *verdict*. The durable line: **facts graduate, verdicts never.**
- **#4 Funding** — **existence + date + verbatim self-stated terms from a first-party surface** (own newsroom, or own SEC filing). Ticker → `profile.md` State; dated round/M&A/Form-D/8-K → a Signal card. **No reconciliation, no valuation, no investor graph, no paid aggregators.**
- **De-risk first** — **two `experiments/` probes before any code**: a Trustpilot hand-diff (gates the comparator) and a funding-gettability pass on the live energy/aero cohort (gates an EDGAR tool). Both spend ~$0.

> **The through-line.** *One* grain-stamped card, written by *one* validating shim, into a *per-company* file that is a strict extension of the engine's existing file-first bet — plus a *disposable* lens held back until the one query files genuinely can't do (cross-entity time-series). Durable conventions + a throwaway lens; never living infrastructure, never a blended number.

This is the simplest shape that still honors *capture once, read back*. The method behind it: 5 independent champions for storage → pairwise tournament; generate-and-filter for the comparator; an adversarial pass that read the actual repo and returned **PASS-with-mitigations** on all four — no refused tripwire fires. The mitigations (path reconciliation, the rename, enforce-in-code) are folded in below.

---

## #1 — Where time-series Signals live

**Recommendation: A, domain-keyed — refined to one v1 home.** Cards live append-only at `store/<domain>/signals/cards.jsonl`, a physically separate file beside `profile.md`. The company is the unit of organisation because the company is the unit of the live consumer (per-company triage).

| Candidate | Shape | Verdict |
|---|---|---|
| **A · Domain-keyed** | `store/<domain>/signals/…` beside State | **recommended** — least-complexity for the first graduation; the per-company read is one `git log -p` / `jq` |
| B · Cohort-keyed | `cohorts/<slug>/signals.jsonl` primary | front-loads the *deferred* maps consumer; adds a `meta.json` membership surface = a second entity-resolution problem |
| C · Run-keyed folders | `signals/runs/<date>/{raw,cards,INTERP}` | **runner-up** — *proven in prod* (Teleprescribe v2) and keeps raw beside cards; but optimises "capture a batch" over "read one company over time," which is the triage read |
| D · Grain-routed hybrid | two homes, routed by grain | nearly identical to A; the routing + a "ghost" `cohorts/` dir is machinery v1 doesn't need yet |
| E · Comparator-only | no engine home; run-local files | overruled by a *premise*: the home is now in-scope and triage is already live. Its own fatal con — "accumulation is caller-disciplined, not engine-guaranteed" — is the betrayal of *capture once, read back* |

**The recommended shape** (company-grain only in v1):

```
store/<domain>/
  profile.md                     # State — the snapshot, unchanged, never holds time-axis facts
  signals/
    cards.jsonl                  # Signals — append-only, one card per claim, git diff = change report
    raw/<date>-<source>.json     # verbatim tool stdout, kept so a normalizer bug ≠ re-spend
    NOTES.md                     # optional synthesis (integrity vetoes, what the method can't see)
cohorts/<category-slug>/         # category-grain home — RESERVED by the architecture, UNBUILT in v1
scripts/
  build_db.py                    # extend the existing rung-3 lens to read cards.jsonl — DEFERRED
  append_signal.py               # NEW: the sole validating writer (validate · dedupe · tee raw)
```

**Why A, and why the refinement.** Folder = company = its whole story; `signals/cards.jsonl` is a strict extension of the bet the engine already made, not a detour. The five grafts the tournament pulled from the losers are what make it ship-ready:

- **Preserve the raw envelope** (from C) — `append_signal.py` tees verbatim tool stdout to `signals/raw/` *before* normalizing. Closes A's biggest hole: a tool schema-drift or a cardify bug no longer costs a Firecrawl re-spend. **Mandatory, not optional** (the "cost compounds on the time axis" lesson).
- **A synthesis home** (from C) — optional `NOTES.md` so the *no-synthesis-in-2-months* kill criterion is greppable. Synthesis only — no `formidable:` field.
- **Grain-routing as committed code** (from D/B) — the domain-vs-category rule lives in the validator, not in lore.
- **Write-time validation + `card_id` dedupe** (from E/D) — `append_signal.py` is the *only* sanctioned writer; rejects `schema_drift ≠ []`, dedupes on `card_id`, with a pre-commit JSONL check as backstop.
- **Lens strictly deferred + stamped** (from E) — design `card_id/grain/subject` as indexable columns now, but don't materialise `signals.db` until the cross-entity maps consumer is live. Per the research brief, that lens earns its place at *exactly one* query — cross-entity time-series — which is the deferred sibling frame.

**My refinement over the raw winner** (the least-complexity push): the champion proposed a second namespace (`store/_signals/<slug>/`) for category-grain cards *now*. But the grain answer (#2) lands **only company-grain in v1** — so there are no homeless category cards to house yet. Collapsing to a single v1 home both resolves the path inconsistency the adversarial flagged **and** defers the non-canonical-slug entity-resolution seam entirely. When the maps frame ships, category cards land in the architecture's already-reserved `cohorts/<category-slug>/` ([SCHEMA.md](../SCHEMA.md) L211 confirms that name is taken for exactly this).

**Residual risks (carried, mitigated).** Append-only JSONL has no native write guarantees → the whole integrity story leans on `append_signal.py` being the *only* writer (backstop: CI/pre-commit schema check). Cross-entity reads are slow until the deferred lens exists → acceptable *only* while the maps consumer stays deferred; if it arrives early, A pays a small append-only lens build, **not** a schema migration.

---

## #3 — The comparability primitive

**Recommendation: Design A — one committed `tools/signal_delta.py` that diffs persisted cards.** This is [`tools/BACKLOG.md`](../tools/BACKLOG.md)'s top item and the frame's first real build step (Open Q#3). Rename is non-negotiable: `scripts/compare.py` already exists (the presentation specimen-sheet renderer) — two `compare.py` doing unrelated things is a live confusion hazard.

| Design | Idea | Verdict |
|---|---|---|
| **A · one CLI, card-diff** | DISPATCH branches over the card spine | **recommended** — the hard source-specific normalization is already done at capture; comparison collapses to align-subtract-flag |
| B · per-source scripts | `trustpilot_velocity.py`, … | wrapper sprawl the repo's own conventions warn against; 4 copies of alignment + veto logic that drift |
| C · diff raw envelopes | no card layer | re-implements every tool's payload semantics; couples the comparator to every upstream's drift. Kept only as an `--envelopes` convenience |
| D · pure code-execution | Claude writes the diff each run | non-reproducible — the veto list + velocity formula get re-derived (and re-bugged) each session; that's how the grain trap slips back in |

**Shape.** `signal_delta.py --cards run-*.jsonl [--align-on subject] [--min-gap-days 5]`. Internally a `DISPATCH` per `source_type` (the repo's existing multi-verb idiom): **trustpilot** (count delta + monthly velocity + profile-state/template vetoes), **serp** (organic rank movement *and* AIO presence movement, **diffed independently, never blended** — the "AIO #1 vs organic #9" disagreement is the tell), **trends** (within-keyword window change; refuses cross-keyword level deltas), **wayback** (a thin *normalizer* over the already-built `wayback.py diff` — never re-fetches). Output reuses the shared envelope spine + a named `comparisons: []` payload; each comparison carries `read_mode: level|delta`, per-metric deltas with units + basis notes, and `comparability_flags` / `vetoes`.

**Why it's safe by construction.**
- **Level-read before delta-read** — one card → current values + caveats only (useful on day 0, before any baseline); ≥2 cards → ordered deltas. Honors "level-reads beat delta-reads before a baseline exists."
- **Fails safe** — a non-comparable pair is emitted as a **veto row with empty deltas**, never a dropped row, so a removed profile or a drifted surface can't silently vanish from the change report.
- **No-blend guard is structural** — every number is bound to one metric within one `source_type`; there is no field that combines across metrics or sources, so a score is *not expressible*. This is the strongest part of the pack and the frame's hardest refusal.
- **Comparability vetoes** generalise v2's hard-veto list: profile removed/merged, templated/duplicate review bodies, `schema_drift`/`parser_version` change between captures, gap below `--min-gap-days`, input mismatch (different slug/query/geo/timeframe = not the same surface), AIO treated as soft-cap, off-vertical Exa neighbour drift.

**Mitigation (from the adversarial):** the grain/source-type alignment fence must be a **hard, unit-tested guard** in the DISPATCH — two cards pair only if `grain` *and* `source_type` *and* the grain-appropriate subject-id all match; a cross-grain pairing attempt is a veto, never a silent skip or an averaged number. Grain collapse is the frame's rule-#1 trap; it can't live in prose.

---

## #2 + #6 — Capture grain & the engine/project line

**Grain (#2): the card carries its own `grain`; v1 emits only `grain=company`.** This *dissolves* the question rather than compromising it. One JSONL schema spans per-company triage and category-keyed maps because `grain ∈ {company|category|sku|molecule|query|page}` is a stamped field with a `subject{}` object holding only the identifiers that fit. The triage consumer reads the `grain=company` slice; the maps consumer (deferred) reads `grain∈{category,query}` from `cohorts/<cat>/`. **Same row shape, different grain key, different home — zero schema fork.**

The non-collapse guarantee is *mechanical*: v1 simply doesn't **emit** finer-grain cards, so there's nothing to mis-read upward (company review velocity can never be sorted as SKU demand). Finer grains are **schema-reserved-but-unemitted** — state this in the contract so a reader never assumes a missing category card means "no demand." Disagreement is preserved, never averaged: each source emits its own card, so opposite-polarity reads sit side by side as signal.

**Ownership (#6): the line moved today — once — and here is where it rests.**

| Engine owns **now** (facts / machinery) | Project keeps **now** (verdicts / opinion) |
|---|---|
| The 6 capture tools (ratified) | The **formidability / launch-relevance** read — viewer-relative |
| The **generalized card schema** as a contract: `modules/SIGNALS.md` (peer to OFFERINGS/VISUAL) + a `signalscheck.py` lint (mirrors `offeringscheck.py`) | The optional `teleprescribe_read` reducer (stays in the project repo) |
| The generic `evidence_label` + `signal_polarity` **enums** (domain-agnostic) | **Cohort/vertical opinion** — which space is "hot," who "dominates" |
| The **domain-keyed Signals home** (a file convention, not a service) | Any **decision gate** built on the signal (depth-gating, go/no-go) |
| The **comparator** + the deferred regenerable index | Which companies/cohorts to capture, at what **cadence** (a spend call) |

**The durable line (won't move again): facts graduate, verdicts never.** Anything factual and source-attestable about what a company *is* or *has-done-over-time* is engine machinery (State/Signals). Anything that means something *relative to who asks* (formidable? a threat? worth capturing deeper?) is a Judgment and stays consumer-side. This is the same cleave [SCHEMA.md](../SCHEMA.md) L209 already draws for cohort packs and the visual-quality frame draws for perception-vs-pricing — load-bearing across three independent surfaces, so it's the real invariant.

> **The load-bearing premise — flagged, dated.** Graduating the *generic convention* (not migrating Teleprescribe's project-flavoured cards) rests on a second consumer — per-company triage beyond Teleprescribe — being real. The frame leaves Open Q#6 open and v2's verdict was "stay project-flavoured." The revised posture puts the home in scope, so the call is defensible — but it's a **design bet, not a fact (2026-06-14)**. Backstop: if no consumer synthesizes engine-side cards within **2 months (by 2026-08-14)**, the kill criterion fires and the layer retreats project-side. Make this assumption explicit so the clock can actually ring.

**Judgments — the open edge, door designed, not built.** The formidability verdict lives entirely consumer-side today (there is deliberately no `formidable` field anywhere in the store). The *sanctioned future shape*, built **only if a consuming project asks**: a `judgments/<viewer>/<subject>` artifact that is **viewer-keyed** (the path carries who asks — two viewers can hold opposite reads and both be right), **provenance-bearing** (`inputs:` = hashes of the exact cards it derived from, so a verdict is traceable and detectably stale), **regenerable + disposable** (tier-3; nothing authoritative), and **physically segregated** (never inside `store/` or `cohorts/`, so a judgment can never leak into the shared facts). Even the future maps consumer routes its *facts* to Signals and its *opinion* to this space.

---

## #4 — Capital / growth boundary

**Recommendation: capture the *event*, never the *number-behind-the-number*.** Existing doctrine already backs this — [SCHEMA.md](../SCHEMA.md) L23 says funding "is a deep-research job, not this one" and keeps a ticker only as a marked *identity prior*. So funding is natively a Signal, not a State field.

| IN bounds (first-party, dated, cited) | OUT of bounds (the paid-data swamp) |
|---|---|
| **Own-newsroom round / M&A** via Firecrawl — verbatim amount + round label + date + named co-leads, *as the company stated it* | **Reconciling** amounts across sources — record disagreement, never average or pick a "true" value |
| **EDGAR ticker/exchange** → `profile.md` **State** (CIK-resolved, durable identity) | **Estimating** valuation / post-money / total-raised — no derived money figures |
| **EDGAR filing stream** (dated 8-K / 10-K) → **Signal** card, `source_type=sec` | **Cap tables / ownership %s** — never reconstructed (PII-adjacent) |
| **EDGAR Form-D existence** — even for private startups: "a Form D matching this name was filed on date Y" (existence + date only) | **Investor-graph entity-resolution** — co-leads stay verbatim strings; no canonical fund linking, no SPV disambiguation |
| **Self-reported cumulative claim** ("over $2B raised") — captured *verbatim + flagged* undated/self-reported, never promoted to an event | **Paid aggregators** (PitchBook / Crunchbase / CB Insights / AlphaSense); a **blended funding score** |

**Free, first-party sources** (all keyless): `data.sec.gov/submissions/CIK….json` (ticker + 1000 recent filings, incl. 8-K), `efts.sec.gov` full-text (Form-D for private cos), `company_tickers.json` (CIK lookup), the company's own newsroom (already in Firecrawl's wheelhouse).

**State-vs-Signal split.** Ticker/is-public = State (rarely changes). Every *dated event* — round, M&A, Form-D, material 8-K — is one Signal card (`grain=company`, observation factual: "announced $X on date Y" / "Form D filed date Y"), **never edited into the snapshot**. The trap the live cohort exposes: a dated round (Sora $14.6M, Apr 2026) is a clean Signal; a cumulative undated total (CFS "$2B") is **not** an event and must not be promoted to one.

**The one seam to guard** (adversarial): asserting "a Form D matching this name exists" for a private startup is a best-effort *name-match* — the thin end of the entity-resolution wedge. Contain it: existence + date **only**, mandatory name-match caveat, **no** related-person/cap-table extraction, and **abort to "no asserted SEC trace"** if namesake/SPV collisions make the match ambiguous. Never let name-match quietly become entity-resolution.

Scope note: most of "funding" is **card-emission over captures the engine already does** (the newsroom page) + one thin new keyless tool (`tools/sec_edgar.py`). Prove it's worth even that before building (below).

---

## Operating discipline (#5, lightly)

Not a design fork — a few conventions the above implies: **cadence** is D0 baseline → D7 directional → D14 minimum decision read; velocity is period-normalized so D0→D7 and D7→D14 compare. The **comparator triggers no captures** — it runs over already-persisted cards, so adding comparison points is a separate *re-capture* decision (cost compounds on the time axis; cadence/scope discipline is the caller's, per the frame). **Kill criterion:** no synthesis in 2 months → cut the layer (greppable via empty `NOTES.md`).

---

## De-risk first — probes before any SCHEMA or `tools/` change

Both are independent, run in parallel, spend ~$0 (cached data + keyless GETs), and each **gates** its build. They also double as the shakeout for the card schema itself — hand-writing real cards is the cheapest test of `modules/SIGNALS.md` before `append_signal.py` codifies it.

1. **`experiments/2026-06-14-signal-delta-trustpilot/`** — *gates `tools/signal_delta.py`.* Take two real, differently-dated Trustpilot captures of the same slug, hand-cardify both, hand-compute the expected output (review-count delta, `reviews_per_30d` velocity), and confirm ≥2 vetoes fire (input-mismatch, gap-too-short, profile-state). **Pass** = the card-diff contract reads cleanly end-to-end on real data. If a delta needs a field the card doesn't carry, fix the *cardify* step, not the comparator. *(Sonnet — structured diff, not heavy reasoning.)*
2. **`experiments/2026-06-14-capital-signal-firstparty-gettability/`** — *gates `tools/sec_edgar.py` + the funding-card convention.* For the live store cohort (`sorafuel-com`, `blueenergy-co`, `electra-aero`, `euclidpower-com`, `cfs-energy`, `evoloh-com`, `verdegoaero-com`) + a **public control** (Tesla / TSLA) + **two VC nulls** (`firstround-com`, `sequoiacap-com`): hand-write funding Signal cards from the *cached* profiles, resolve CIK + pull the free EDGAR submissions/Form-D, and write a one-page boundary ledger recording every place two sources disagree — **left unreconciled by design**. **Pass** = ≥4 of 7 startups yield a dated first-party card, the public control yields ticker-State + a filing-Signal, the CFS undated "$2B" stays a flagged baseline (not an event), and the VC nulls produce **zero** own-raise cards. **Kill** if a usable round *requires* reconciling numbers, or Form-D name-matching needs the entity-resolution we refuse. *(Sonnet.)*

Only after a probe reads clean does its build land. The shared substrate both exercise — `modules/SIGNALS.md` (the generalized card contract) + `signalscheck.py` (mirroring the existing validators) — can be drafted in parallel; `append_signal.py` and the deferred `build_db.py` lens extension follow the comparator probe.

---

## What this does *not* build — the guardrails held

The adversarial pass (which read the running code, not just the prose) returned **PASS-with-mitigations** on all four decisions: **no Still-Refused tripwire fires**, and several refusals are honoured more rigorously than the frame required. Confirmed intact end-to-end:

- **No living infrastructure** — every writer/reader is a one-shot script; the SQLite lens is gitignored + stamped non-authoritative (exactly like the live `build_db.py`) and deferred; markdown/JSONL stay the source of truth. Nothing must keep running to stay true.
- **No de-facto score** — the comparator can't blend, funding refuses derived figures, the index refuses cross-grain ranking, the verdict is fenced consumer-side. No surface fuses metrics into one number.
- **No judgment leak** — only `is-public/ticker` (a sanctioned identity prior) touches `profile.md`; every dated event is a Signal card; the formidability read stays consumer-side; the `judgments/<viewer>/` overlay is designed-not-built.
- **No reconciliation, no entity-resolution, no embeddings, no served API, no PII** — funding records existence + verbatim terms only; the two non-canonical-key seams (cohort slug; Form-D name-match) are deferred or kill-gated.

The required mitigations are about **internal consistency and enforcement, not pulling back scope** — all folded in above: one v1 home (`store/<domain>/signals/cards.jsonl` + `raw/`) and the architecture's reserved `cohorts/<category-slug>/` for the deferred category grain; the comparator renamed to `tools/signal_delta.py`; the grain fence, sole-writer validation, and raw-tee turned into enforced code; the "second consumer" graduation premise dated against the kill clock.

<sub>**Method** — dynamic multi-agent design workflow (10 agents): 5 independent storage champions → pairwise tournament (winner A, runner-up C); generate-and-filter for the comparator (winner: single card-diff CLI); parallel forks for grain/ownership + funding; a separate adversarial verifier stress-testing every decision against the *actual* refused list (repo-grounded — verified `compare.py`, `build_db.py`, `.gitignore`, `modules/`, SCHEMA L23/L209/L211). **Sources** — [traction frame](2026-06-14-traction-frame.md) (Open Qs) · [`.claude/rules/engine-dev.md`](../.claude/rules/engine-dev.md) (durable-conventions-not-living-infra; engine owns State+Signals) · [frame](2026-05-29-frame.md) + [architecture](2026-05-30-architecture.md) (State/Signals/Judgments; reserved `cohorts/<category-slug>/`) · stress-testing brief (`_temp/`) (relax markdown-as-truth precisely for cross-entity Signals; judgments as viewer-keyed overlays) · [`tools/README.md`](../tools/README.md) + [`tools/BACKLOG.md`](../tools/BACKLOG.md) (six tools; comparator backlog item) · live Teleprescribe traction v2 (`research/competitive/mine/traction/v2/`: card schema, raw→card→interpretation spine, D0/D7/D14 cadence, integrity vetoes). Authored 2026-06-14.</sub>
