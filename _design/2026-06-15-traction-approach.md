# APPROACH — External traction Signals (v1)

Date: 2026-06-15 · Status: solution proposal — **v1, hardened by an adversarial pass** (verdict: survives-with-fixes; folded in). Supersedes the 2026-06-14 drafts (archived). Companion to the [traction frame](2026-06-14-traction-frame.md); answers Open Qs #1–#4 + #6.

> **Synthesis note.** This keeps the prior draft's strong *judgments* (the funding boundary, the no-blend-by-construction comparator, the facts-vs-verdicts line, the integrity-veto discipline) and cuts its *build list* to what a probe or a second caller actually earns now. The prior draft built a six-piece card layer before anything needed it; this builds **one comparator + one funding tool**, commits **one findable path convention** (no abstraction), and lets the schema / lint / writer / lens layer graduate when an automated writer **and** a second consumer are real.

## 30-second skim — the calls

- **#3 Comparator (the one real build)** — `tools/signal_delta.py` diffs **raw tool envelopes** (the shared spine the six tools already emit), source-aware branches, level-read-then-delta, deltas + comparability vetoes only — **structurally incapable of a score**. Reading raw keeps the integrity signals (templated reviews, AIO presence, `schema_drift`, `parser_version`) right under the comparator's eye — and drift is already absorbed *at the capture tool*, so a card layer would add normalization, not remove it.
- **#1 Storage** — **a findable path convention now; the machinery deferred.** Persist each capture verbatim to `store/<domain>/signals/<source_type>/<captured_at>.json` (a documented path + a one-line redirect — *no* schema, lint, writer, or SQLite). That's the minimum the comparator's first real run earns: somewhere D0 lives so D7 can find it. The schema-as-contract + lint + sole-writer + lens graduate later, with an automated writer + a second consumer.
- **#2 + #6 Grain & ownership** — grain is a stamped field; **v1 emits only company-grain** (can't mis-sort what's never written). Engine owns the six tools + the comparator + the path convention; the card *schema and its label/polarity enums stay a draft* (project-side) until a second consumer earns a `modules/` graduation. Q#6 closes **only the comparator half**; the label/schema/verdict half stays open. The line: **facts graduate; verdicts stay consumer-side for now.**
- **#4 Funding** — **existence + date + verbatim self-stated terms** from a first-party surface (own newsroom / own SEC filing). Ticker → State; dated round / M&A / Form-D / 8-K → a Signal. No reconciliation, valuation, investor graph, or paid aggregators. Ambiguous Form-D → `name_match_unconfirmed`, never a forced assert.
- **De-risk first** — **two ~$0 probes gate the two tools.** Probe #1 round-trips through the `signals/` path and fires the vetoes on *partial* failures (a 6/7 AIO blanking, not just 100%). Both run before any code.

**The through-line:** build the two tools the probes earn; commit the one path that makes captures accumulate; let the card layer graduate when a second caller knocks. Durable conventions + a deferred throwaway lens; never living infrastructure, never a blended number — **and never machinery a probe hasn't earned.**

---

## #3 — The comparator (build this first)

**Recommendation: `tools/signal_delta.py` — diffs the raw envelopes the six tools emit.** This is [`tools/BACKLOG.md`](../tools/BACKLOG.md)'s top item *as written*: "a generic comparator that understands the shared **envelope** spine… **Act when:** two captures of the same source." Name it `signal_delta.py` (not `compare.py` — `scripts/compare.py` is the specimen-sheet renderer).

**Why raw envelopes, not a normalized "card" layer.** The prior draft diffed persisted cards — a normalized layer that (a) forced a four-piece card stack to exist *before the comparator could run*, and (b) concentrated every integrity check in one un-probed normalization step the comparator never looks behind. **Drift is already absorbed at the capture tool, not downstream:** on a reshape, each tool sets `ok:false`, populates `schema_drift[]`, and blanks the parsed fields *before any consumer reads them* — so a drifted capture reaches the comparator as a ready-made veto, never a poisoned number. A card placed downstream of that boundary absorbs nothing the tool hasn't; it just adds a per-source normalizer that drifts in lockstep. So reading raw **reuses the per-source logic each tool already owns** (the DISPATCH must understand each payload either way) instead of forcing a second normalization copy — and keeps `schema_drift` / `parser_version` / AIO-presence / review-templating directly under the comparator's eye.

**Shape.** `signal_delta.py <a.json> <b.json> [--align-on subject] [--min-gap-days 5]`. A DISPATCH per `source_type`, output reuses the shared spine + a named `comparisons: []` payload (each carries `read_mode: level|delta`, per-metric deltas with units + basis notes, `comparability_flags`/`vetoes`):

| Source | Diffs | Key vetoes / guards |
|---|---|---|
| **trustpilot** | absolute **`review_count`** delta + velocity (per-period) | Diff the monotone cumulative `review_count`, **not** `reviews_last_12m` (a rolling window anchored to capture date — diffing it across uneven gaps double-counts the moved edge; level-read it only). Vetoes: profile removed/merged; templated/duplicate bodies. Carry gap-length + extrapolation factor as a basis note; flag bursty/solicited windows |
| **serp** | organic rank movement **and** AIO presence movement, **diffed independently, never blended** | AIO as soft-cap; **batch-outage veto** — if AIO presence drops across **≥ a high fraction** of a run's rows that previously carried it (not only 100%), flag a probable *surface outage* on all dropped rows, don't report N fake drops |
| **trends** | within-capture trajectory (`delta_7d_vs_prior_7d_pct`), **not** raw point levels | **basis-aware veto:** a point-level delta is comparable only over the captures' date-overlap **and** only if both captures' `peak_date` falls inside that overlap (same normalization anchor); else veto + `renorm_basis_mismatch`. *Needs `peak_date`/`peak_value` added to `trends.py`'s envelope — a one-line capture-tool change probe #1 gates* |
| **wayback** | presence / content-hash | thin normalizer over the existing `wayback.py diff`; never re-fetches |
| **fallback** | reserved-key facts only | "no source-aware delta for `<tool>`" — never guess an unknown payload |

**Safe by construction.** Level-read before delta (one capture → current values + caveats; ≥2 → ordered deltas). A non-comparable pair is a **veto row with empty deltas, never a dropped row**. Every number is bound to one metric within one `source_type`, so **a score is not expressible**. The **grain + source_type + subject-id alignment fence is a hard, unit-tested guard** — a cross-grain pairing is a veto, never a silent skip or an average.

> **Why the two veto fixes matter.** The Trends and AIO vetoes were the adversarial pass's most serious catch: the original "match the window's right edge" rule was *unsatisfiable* (two captures days apart never share an edge; `trends.py` normalizes each to its own peak), and the original "if *every* AIO row blanks" trigger missed the real outages on record (6/7 and 11/12 — partial, not total). Both now match the documented failure signatures.

---

## #1 — Where Signals live (a path convention, machinery deferred)

**Recommendation: commit a written path convention now; defer the machinery.** The comparator needs two captures of the same source separated in time — so *something* must persist the D0 envelope where D7 can find it. Today nothing does: the tools "print, don't write," and no `signals/` home exists, so by default the D0 capture **vanishes** (the archived draft's actual flaw). v1 closes that with a **convention, not an abstraction** — persist each capture verbatim:

```
store/<domain>/signals/<source_type>/<captured_at>.json   # a documented path + a one-line redirect
```

beside `profile.md` (never inside it). That is the *whole* storage commitment — **no schema-as-contract, no lint, no sole-writer, no SQLite.** Those graduate **together, when there's an automated writer and a second consumer** ("extract a shared helper only on the second caller"). Category-grain → the architecture's reserved `cohorts/<category-slug>/`, unbuilt. The SQLite cross-entity lens stays deferred to its one query (the maps frame).

**Why this isn't the archived draft's mistake — and isn't the over-built one either.** The archived draft deferred storage *entirely* (and mis-claimed `captures/` as the home), so nothing accumulated — caller-disciplined, not engine-guaranteed. The over-built draft committed a six-piece card stack. This commits the *one* thing accumulation actually needs — a findable path — and nothing more. The engine is licensed to own it: the rules name "append-only evidence" as in-scope now.

---

## #2 + #6 — Grain & the engine/project line

**Grain (#2): the card carries its own `grain`; v1 emits only `grain=company`.** One shape spans triage and (deferred) maps because `grain ∈ {company|category|sku|molecule|query|page}` is a stamped field with a `subject{}` of only the fitting identifiers. Non-collapse is *mechanical* — v1 doesn't **emit** finer grains, so company review-velocity can never be sorted as SKU demand — backed by the comparator's hard alignment fence. State "schema-reserved-but-unemitted" in the contract so a missing card never reads as "no demand." Disagreement is preserved: each source emits its own row, opposite reads side by side.

**Ownership (#6): facts graduate; verdicts stay consumer-side for now.**

| Engine owns now (facts / machinery) | Project keeps now (verdicts / opinion) |
|---|---|
| The 6 capture tools + the comparator | The formidability / launch-relevance read (viewer-relative) |
| The written `signals/` **path convention** (a findable home) | Cohort/vertical opinion — what's "hot," who "dominates" |
| The deferred regenerable index | Any decision gate built on the signal |
| — | Capture cadence/scope (a spend call) |

The card *schema* — **and the `evidence_label` / `signal_polarity` enums with it** (`signal_polarity` = good-or-bad-*for-whom* is verdict-adjacent) — stays a **draft** (probe folder / project-side), **not** a graduated `modules/SIGNALS.md` contract + `signalscheck.py` lint, until a second engine-side consumer actually appends cards. v1's comparator emits raw per-metric deltas + comparability flags/vetoes with **no generic label/polarity enum**. So Q#6 closes only one half — *the comparator graduates now* — while the label / schema / verdict half stays genuinely open. Graduate the rest on evidence, not a kill clock. *Facts vs. verdicts is today's cleave, not a closed invariant.*

**Judgments — the open edge, door designed, not built.** The formidability verdict stays entirely consumer-side (no `formidable` field anywhere in the store). The sanctioned *future* shape, built **only if a consuming project asks**: a `judgments/<viewer>/<subject>` artifact — viewer-keyed, provenance-bearing (`inputs:` = card hashes), regenerable/disposable, physically segregated from `store/`. Designed so it *can* exist without ever leaking a verdict into the shared facts; built when earned.

---

## #4 — Capital / growth boundary

**Capture the *event*, never the *number-behind-the-number*.** [SCHEMA.md](../SCHEMA.md) L23 already calls funding "a deep-research job, not this one" and keeps a ticker only as a marked identity prior — so funding is natively a Signal.

| IN bounds (first-party, dated, cited) | OUT of bounds (the paid-data swamp) |
|---|---|
| Own-newsroom round / M&A via Firecrawl — verbatim amount + round label + date + named co-leads, *as stated* | Reconciling amounts across sources — record disagreement, never average |
| EDGAR ticker/exchange → `profile.md` **State** | Estimating valuation / post-money / total-raised |
| EDGAR filing stream (dated 8-K/10-K) → **Signal**, `source_type=sec` | Cap tables / ownership %s (PII-adjacent) |
| EDGAR **Form-D existence** — "a Form D matching this name was filed on date Y" (existence + date only) | Investor-graph entity-resolution — co-leads stay verbatim strings |
| Self-reported cumulative ("over $2B raised") — captured **verbatim + flagged** undated/self-reported, never promoted to an event | Paid aggregators (PitchBook / Crunchbase / CB Insights); a blended funding score |

Ticker/is-public = State (rarely changes). Every *dated event* is one Signal card (`grain=company`, observation factual), never edited into the snapshot. The trap the live cohort exposes: a dated round (Sora $14.6M, Apr 2026) is a clean Signal; a cumulative undated total (CFS "$2B") is **not** an event.

**The seam to guard:** asserting a Form-D match for a private startup is a best-effort name-match — the thin end of entity-resolution. Contain it: existence + date only, mandatory name-match caveat, no related-person/cap-table extraction, and a **`name_match_unconfirmed` state** for probable-but-unproven matches (existence-only, never promoted) rather than a binary assert-or-abort. One thin keyless tool (`tools/sec_edgar.py`), gated by the probe below.

---

## Operating discipline (#5, lightly)

Cadence D0 baseline → D7 directional → D14 minimum decision read; velocity period-normalized **with the gap surfaced**. The comparator **triggers no captures** — it runs over already-persisted envelopes, so adding comparison points is a separate re-capture (cost) decision, the caller's. Kill criterion: no synthesis in 2 months → cut the layer.

---

## De-risk first — probes before any code

Both independent, parallel, ~$0 (cached data + keyless GETs); each **gates** its build, and both double as the cheapest shakeout of the draft card schema before any code codifies it.

1. **`experiments/2026-06-15-signal-delta-trustpilot/`** — *gates `tools/signal_delta.py`.* (a) **Round-trip:** persist a capture to the `signals/<source_type>/<captured_at>.json` path, then diff a *later* capture read back from that path — exercising "where did D0 go," not just two files handed over in one session. (b) Diff a clean pair **and degenerate fixtures**: a removed/templated Trustpilot profile **and a *partial* AIO blanking (e.g. 6/7 rows empty, not 100%)** — confirm the vetoes fire on the partial outage, not only a total one. **Pass** = the diff reads cleanly end-to-end *and* the vetoes catch the real failure signatures. A delta that needs a field the envelope lacks (e.g. Trends `peak_date`) is a capture-tool gap to close first, not a comparator gap. *(Sonnet.)*
2. **`experiments/2026-06-15-capital-firstparty-gettability/`** — *gates `tools/sec_edgar.py`.* Hand-write funding cards from cached profiles + free EDGAR for the energy/aero cohort (`sorafuel-com`, `blueenergy-co`, `electra-aero`, `euclidpower-com`, `cfs-energy`, `evoloh-com`, `verdegoaero-com`) + a public control (TSLA) + two VC nulls (`firstround-com`, `sequoiacap-com`); record disagreements unreconciled. **Pass** = ≥4/7 startups yield a dated first-party card, the control yields ticker-State + a filing-Signal, CFS "$2B" stays a flagged baseline, VC nulls yield zero. **Caveat:** if a newsroom page wasn't captured, a null is *missing data*, not *no funding* — note which. *(Sonnet.)*

Only after a probe reads clean does its build land.

---

## What this does *not* build

- **No card-layer machinery in v1** — the schema-as-contract, the lint, the sole-writer, **and the `evidence_label`/`signal_polarity` enums** all defer to the second caller; the schema lives as draft prose the probes shake out. (The one storage thing v1 *does* commit is a findable path convention — see #1.)
- **No living infrastructure** — the comparator is a one-shot script; the SQLite lens is deferred + gitignored-when-built (like `build_db.py`); markdown/JSONL stay truth.
- **No score** (structural), **no judgment in `profile.md`** (ticker only), **no reconciliation / entity-resolution / embeddings / served API / PII.** The SQLite lens and the `judgments/<viewer>/` overlay are designed/reserved, not built.

<sub>**Method** — synthesized from the two archived 2026-06-14 drafts + a four-lens critique, then **hardened by a five-agent adversarial workflow** (4 independent attackers + an independent judge, repo-grounded). Verdict: *survives-with-fixes*; the load-bearing raw-envelope-vs-card cut was independently vindicated (drift is absorbed at the capture tool — `trustpilot.py`/`serpapi.py` set `ok:false`+`schema_drift` and blank parsed fields — so a card absorbs nothing the tool hasn't). Folded-in fixes: the Trends + AIO vetoes re-specified to the documented failure signatures (incl. a one-line `peak_date` addition to `trends.py`), velocity diffed off cumulative `review_count`, the storage *convention* promoted from reserved to written (correcting a false "envelopes already persist" claim), and the unprobed `evidence_label`/`signal_polarity` enums cut from "engine owns now." **Sources** — [traction frame](2026-06-14-traction-frame.md) · [`.claude/rules/engine-dev.md`](../.claude/rules/engine-dev.md) · [frame](2026-05-29-frame.md) + [architecture](2026-05-30-architecture.md) · [`tools/README.md`](../tools/README.md) + [`tools/BACKLOG.md`](../tools/BACKLOG.md) · live Teleprescribe traction v2. Drafted 2026-06-15.</sub>
