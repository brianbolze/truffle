# APPROACH — External traction signals [REJECTED]

NOTE: This proposal was overly conservative, and developed before we updated our engine-dev rules and overall architecture principles modestly.

Date: 2026-06-14 · Status: solution design (Proposal) - REJECTED. Companion to the [traction FRAME](2026-06-14-traction-frame.md); answers its Open Questions #1–#4 + #6. Propose, not build — no SCHEMA edits, no tool code this session.

## 30-second skim

**Build exactly one thing now — the envelope comparator `tools/_delta.py`, stdout-only. Defer everything else.** It's the frame's named first step and the only proposal that cleared an adversarial pass against the anti-Doro line. Storage shape stays deferred (with a safe default), grain/ownership confirm the frame with two anti-smuggling guards, and capital is answered by a probe (too sparse to tool).

| Open Q | The call |
|---|---|
| **#3 Comparator** | **Build `tools/_delta.py`** — importable lib (the `_match.py` shape, *not* a CLI). 2+ same-source envelopes → per-axis deltas + comparability notes. Deltas only; vetoes *suppress-and-note*, never reconcile. **The one build.** |
| **#1 Storage** | **Defer** the durable home (frame left Open Q#1 open on purpose). The comparator decides nothing — it prints. When a run *must* persist, default to a clean sibling `store/<domain>/signals/<date>/` — **never `captures/`** (that's State's raw source). No `log.md`, no cohort ledger, no index.md yet. |
| **#2 Grain** | **Don't pick one.** Keep each tool's native grain; `grain` is a passthrough field (derived from `tool`+`input`); consumers filter by it; the comparator *refuses* cross-grain diffs. |
| **#6 Ownership** | **Confirm v2's line**, one field short of the interpreted card. Engine owns envelopes + comparator + structural grain/axis-name/`metric_direction` + a no-verdict lint. Labels and judgment-polarity stay project-side; whether and how the engine emits them is an open edge, not a closed sequence. |
| **#4 Capital** | Probe says **sparse — 2/15 public, 0/15 first-party rounds. Build no funding tool.** Ticker = State (already captured); EDGAR scale = opportunistic Signal for the rare public anchor; refuse all aggregators. |
| **Deferred** | #7 delivery shape (verb/module/tools-only) and comparative/cohort (market maps) — untouched, per frame. Design keeps maps *non-blocked*, builds nothing for it. |

**The one guardrail over all of it:** don't let the pieces stack into an authoritative signals database (last section).

---

## #3 — The comparability primitive (the one thing to build)

Generate-and-filter over four shapes; the importable lib wins clean.

| Option | Verdict |
|---|---|
| Generic CLI `tools/delta.py` | Heavier than the job; a delta-CLI invites the per-source sprawl `tools/README` warns against. Borrow its delta-envelope *shape*, reject the CLI. |
| **Importable `tools/_delta.py` lib** | **Recommended.** Smallest new surface; mirrors the proven `_match.py`/`_env.py` shape. |
| Per-source comparators (`serp_delta.py`, `trustpilot_velocity.py`…) | Rejected — the exact wrapper sprawl the README forbids ("extract a shared helper only on the second caller"); 80% duplicated plumbing. |
| Convention-only recipe (no code) | Rejected — the *vetoes* are non-obvious and must be code to fire reliably. A human diffing JSON reads a removed profile as −100% velocity: the asymmetric-failure-cost the frame flags. |

- **Shape.** `delta(envelopes: list[dict]) -> dict`. Caller hands it 2+ already-captured envelopes from the *same* tool+source+subject; it never captures, never spends. Output reuses the reserved spine + two payload fields: `deltas[]` (per-axis, grain-tagged, from/to/span — **never summed across axes**) and `comparability_notes[]` (vetoes + caveats). `captured_at` gives the time axis for free.
- **Source-awareness = a small internal DISPATCH on `tool`,** ~15–30 lines/branch:
  - *serpapi* — organic rank + AIO as **separate** rows (the AIO#1-vs-organic#9 gap is the signal; never averaged).
  - *trustpilot* — review-count velocity. **Folds the backlog's "Trustpilot velocity" item in as one branch,** not a separate tool.
  - *trends* — mostly **refuses**: pytrends batch-renormalization puts two captures on different 0–100 scales.
  - *wayback* — presence / content-hash; zero-cost, frozen feed (no validator).
  - *generic fallback* — compare reserved keys only; emit "no source-aware delta for `<tool>`" rather than guess at unknown payload.
- **Comparability vetoes (the load-bearing part):** Trustpilot profile removed/merged → suppress velocity; SERP AIO blanked → don't read AIO movement (organic delta still stands, separately); Trends renormalized → incomparable; `schema_drift[]` non-empty → axis unreadable; grain/identity mismatch → refuse; `ok:false` → no baseline.
- **Does NOT:** blend/score, cohort/market-share read, verdict, capture/spend, write `profile.md`, decide storage.

**The invariant that keeps it honest: vetoes suppress-and-note, never reconcile** — never merge two captures into one value, never pick a winner. It suppresses only on *measurement* grounds (can't subtract: different scale, missing baseline, removed profile), passes integrity flags through verbatim, and never emits the interpretive `vetoed` label. That's the seam between a comparator and a reconciliation engine.

---

## #1 — Storage shape (defer, with a safe default)

The tournament and the adversarial pass disagreed here — and the skeptic won, so the reasoning is worth showing.

| Champion | Pro | Con |
|---|---|---|
| **A. Domain `signals/` + `index.md`** | Rides the domain key; structural `profile.md` isolation. | `index.md` is a hand-kept layer that silently desyncs, partly redundant with `git diff`. |
| **B. Cohort/category ledger** | Matches the maps grain. | Builds the comparative shape the frame spun into *its own sibling frame*; resurrects category-slug governance (the entity-resolution cost domain-as-key erased). Heaviest; serves a walled-off consumer. |
| **C. Project-side only** | Most faithful to "labels stay project-side." | Over-rotates: persists nothing engine-side, so the comparator has nothing to diff cold and the engine never accumulates. |
| **D. Comparator-only / reuse `captures/`** | Lightest; the frame's explicit lean. | Rests on a **false premise**: `captures/` holds State's raw page-scrapes (verified — `mens-trt.md`, `pdp-sermorelin.md`…; the six tools have never written there). Dropping Signal envelopes there co-mingles the two kinds. |

**Recommended: defer the durable home (honor Open Q#1) — the comparator makes no storage decision — and when a run *must* persist envelopes, default them to a clean sibling `store/<domain>/signals/<date>/`, never `captures/`.** No `log.md`, no cohort ledger, no `index.md` yet.

This is **D's discipline** (build the comparator, decide nothing a probe hasn't earned) **corrected by the verifier** and grafted with **A's clean instinct** (a domain-keyed sibling), minus A's risky `index.md`. Concretely:

- The comparator is a pure function — it prints; the caller decides where it lands ("print, don't write"). No storage *decision* is baked.
- The **one** thing decided now: *if* you persist, persist to a sibling `signals/<date>/`, structurally separate from both `profile.md` (the State snapshot) and `captures/` (State's raw source). Verified: no `signals/` exists in the store today — a clean new home, not a contaminated one.
- Everything else stays earned-later: whether `signals/` even becomes standard (vs staying project-side); a cross-run index (v2's deferred `signal-index.jsonl`, only on repeated pain); the SQLite lens (`scripts/build_db.py` precedent — regenerable, never authoritative).

**Why not commit `captures/` (the tournament winner):** it's factually State's raw-source dir, and committing *any* durable signals home now pre-empts a deferral the frame made on purpose — and stacks toward a signals DB (final section). **Why not B/cohort now:** that's the sibling comparative frame's call; building it here imports slug governance and serves a deferred consumer at the live one's expense.

---

## #2 + #6 — Grain & the engine/project line (confirm, with two guards)

These operationalize the frame rather than open a fork.

**#2 Grain — recommended: don't pick a capture grain.** Keep each tool's native grain (serp = query/category, trustpilot = company, wayback = page, trends = brand, exa = company, ads = advertiser). Make `grain` a first-class *field*, deterministically projected from `tool`+`input` (costs ~nothing — already implied by the envelope). Triage filters `grain ∈ {company, brand, page}`; maps filters `grain ∈ {category, query}`. The comparator's one hard job: **refuse to diff across mismatched grain** (a grain-mismatch is itself "not measurable" — surfaced, never bridged).
*Alternative — pick category-keyed (prior art's comparison preference):* rejected — it re-keys domain-native tools onto a grain they can't see, manufacturing the adjacent-grain evidence rule #1 forbids, and starves the live triage consumer.

**#6 Ownership — recommended: confirm v2's line, one field short of the interpreted card.**

- **Engine owns:** the six tools + their envelope · the comparator · `grain` (structural passthrough) · neutral source/axis *names* bound to metric identity (`serp-organic-rank-delta`, not "visibility") · `metric_direction` (did the raw number rise/fall) · integrity flags passed through verbatim · a **no-verdict/no-blend lint** mirroring `visualcheck.py`'s `score:` ban.
- **Project owns:** the interpretive labels (supply only / visibility / trust-flow proxy / plausible movement / vetoed) · judgment-polarity (good/bad-for-thesis) · the full card · calibration anchors/controls · the interpretation memo · the verdict (open edge — under rework).
- The labels *feel* generic but encode a project's theory of what an axis *means* (esp. `vetoed` — deciding an integrity flag disqualifies an axis is a judgment) → they stay project-side until the second consumer (maps, deferred) needs the *same* card.
*Alternative — graduate the generic card skeleton now:* rejected as premature (infra ahead of the second user), and the skeleton drags `evidence_label`/`signal_polarity` (interpretive values) across the State/Signals line. Lifting the card later is cheap (markdown + JSONL); building it early and finding maps wants a different shape is the costly direction.

**Two anti-smuggling guards — the real work here:**
1. **Name the engine field `metric_direction`, not `signal_polarity`.** Same word in v2's card carries the judgment meaning ("threatening to me"); reusing the name inherits the judgment. Bind axis-names to source/metric identity, never a traction-meaning verb.
2. **Integrity flags surface, never act.** The comparator emits "profile merged" *beside* the delta; it never itself emits `vetoed` or suppresses on integrity grounds — that's the project's call. (Distinct from comparability vetoes, which suppress on *measurement* grounds — see #3.)

---

## #4 — Capital/growth boundary (the probe is the answer)

The frame said "prove what's gettable before building." This session's count-probe over the live 15-company telehealth cohort did:

- Public tickers: **2/15** (HIMS; LifeMD incl. its RexMD sub). One Medical is now a private Amazon subsidiary.
- First-party dated funding rounds in any captured page: **0/15**. Press links exist for ~5 but weren't captured; one profile explicitly notes "funding not on-site."

**The line:** first-party = the company's *own* domain (marketing / press / IR) **OR** a public regulator where disclosure is legally mandated (SEC EDGAR: 10-K/10-Q/8-K/Form D). Authorship + mandation, **not** free-vs-paid. Everything else — Crunchbase, Pitchbook, Owler, ZoomInfo, LinkedIn headcount, valuation aggregators, estimated revenue — is the paid-data swamp, refused by non-goal #1.

**Recommended: build no funding tool.** The probe shows the signal is too sparse to pipeline.

- **Ticker = State** (the company *is* public; ticker is stable identity, like parent-company) — already in `profile.md`. Fine there.
- **EDGAR scale (revenue/market cap) = Signal** (dated, time-axis) — fetch *opportunistically* for the rare public anchor and land it in the **signals layer, never** as a `profile.md` frontmatter field (it's the textbook "same fact on a time axis" the State/Signals split excludes). Defer even this until a consumer (maps calibration) needs the anchor.
- **Self-announced rounds / M&A = opportunistic** — capture the press page only when a nav link *already exists*; no dedicated tool, no default credit routing.
- **Refuse:** every aggregator above.

*I dialed this back from the subagent's "build the EDGAR hook" — per least-complexity, the probe already answers #4, and the EDGAR anchor is a calibration need owned by maps, which is deferred. Capture the ticker as State; don't build.*

---

## De-risk first — probes before any SCHEMA/tools change

1. **`experiments/2026-06-14-envelope-delta/` — prove the comparator, especially the vetoes.** Two parts:
   - *Part 1 (free plumbing):* feed `delta()` two **historical** Wayback snapshots of one store homepage → confirm it reads the spine, derives span from `captured_at`, emits a clean changed/unchanged delta. Zero cost, no waiting.
   - *Part 2 (the load-bearing test — a veto MUST fire):* replay a **contaminated** pair — a removed-Trustpilot-profile control (e.g. PeterMD) and/or a SERP AIO-blank case → confirm `delta()` *suppresses* velocity / refuses AIO movement and emits the incomparability note **instead of** a plausible-but-wrong number.
   - **Success = the veto trips on the artifact.** Subtraction is trivial; the vetoes are the only part that can be wrong, and where the asymmetric failure cost lives. If they don't fire reliably on real contaminated captures, the primitive isn't earning its keep and the design reopens.

2. **Bank the capital count-probe** (run this session). Its result — 2/15 public, 0/15 first-party rounds — is what makes "build no tool" *cited*, not asserted. A paragraph here suffices; promote to `experiments/2026-06-14-capital-gettability/` only if you want it reproducible.

3. **No `SCHEMA.md` change and no new tool code until probe #1 passes.** When it does, the first real build is `tools/_delta.py` + a companion `_delta.md` gotchas doc. The no-verdict lint lands with the first engine-side signal output, not before. A thin `tools/SIGNAL-CARD.md` that *publishes* (not writes) the v2 card shape is optional, and only earns its place when the second consumer is real.

---

## The one guardrail — don't let the pieces stack into a signals DB

The sharpest finding from the adversarial pass. Each piece is innocent alone; stacked, they reconstruct what the anti-Doro line refuses:

> committed storage home (#1) + per-tool delta engine (#3) + `grain` stamped on every record (#2) = a dated, grain-keyed *authoritative* signals store with a diff layer = **"change-tracking/diffing as a core concern"** — explicitly on the architecture's refused list.

Five invariants keep it a *convention*, not a database:

- **Storage stays undecided** — don't commit a durable home; the comparator prints, decides nothing.
- **The comparator is a stdout pure-function** — never a standing indexed layer.
- **`grain` is a passthrough fact on a record, never a partition/index key** — the moment you build a directory tree or SQLite *around* grain, it tips.
- **Any SQLite is a regenerable lens only, never authoritative** — built only on repeated cross-run pain (the `build_db.py` precedent).
- **Vetoes suppress-and-note, never reconcile; integrity flags surface, never act** (from #3 and #6).

**Naming:** `tools/_delta.py`, **not** `compare.py` — `scripts/compare.py` already exists (the presentation sheet). Verified.

---

## Out of scope (deferred, per frame)

- **#7 delivery shape** (verb / module / tools-only) — frame says don't answer yet.
- **Comparative/cohort analysis** (market maps) — its own sibling frame. This design keeps it *non-blocked* (a future maps consumer can walk `store/*/signals/` keyed on the shared `input.q`) but builds nothing for it.

<sub>**Method** — a dynamic multi-agent workflow: tournament for storage (#1), generate-and-filter for the comparator (#3), independent reasoning for grain/ownership (#2+#6) and capital (#4), then one adversarial verifier against the non-goals + anti-Doro line. The verifier **overturned the tournament's storage winner** (false "captures/ is already the shape" premise) and surfaced the stack-into-a-DB risk; layout/naming/capture-dir facts verified by hand. **Sources** — [traction FRAME](2026-06-14-traction-frame.md) · [engine Frame](2026-05-29-frame.md) + [Architecture](2026-05-30-architecture.md) (State/Signals/Judgments, anti-Doro line) · [`tools/README`](../tools/README.md) + [`tools/BACKLOG`](../tools/BACKLOG.md) (envelope spine; comparator as first build step) · live Teleprescribe traction v2 (signal-card spine, labels, anchors/controls; territory, not ported). Authored 2026-06-14.</sub>
