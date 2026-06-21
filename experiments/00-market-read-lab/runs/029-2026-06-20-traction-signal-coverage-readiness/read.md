# Market Read

## Question

Across the captured store, what traction signal (capital/funding, demand, attention/visibility,
growth/tenure) does any company actually expose today — at what grain, level-vs-delta, and for
how many companies — and is the store **ready to roll a cohort traction-map** per the
traction-frame's 5-step capability ladder (capture / comparability / accumulate / cohort-rollup /
feed-judgment)?

This is a gap-probe on the engine's named *future* axis. The result is the **readiness map**,
not a traction read of any company; per the frame's hard line, this run emits **no** traction or
formidability score/verdict.

## Result

**The store has built the traction *plumbing* but not the traction *substance*. It sits at
roughly rungs 1 + 3 of the frame's 5-rung ladder.** The capture path and the durable
append-only timeline are real and correctly shaped; traction-signal *coverage*, *comparability*,
and *cohort-rollup* are thin-to-absent. **No new primitive is the gap** — the path, comparator,
and six tools already exist (v1 shipped 2026-06-15). The gap is **coverage + comparator-completeness
+ the deferred cohort layer.**

Scored against the frame's own 5-step ladder:

| Rung | Frame capability | Store today | Verdict |
|---|---|---|---|
| **1. Capture** | Capture repeatable external signals cheaply | `signals/` path + 6 tools exist; **49/126 profiled cos** have a `signals/` dir, but only **20/126 (16%)** carry a *genuine* traction signal (C2). The single most-captured signal — Wayback, 47 cos — is **not traction** (tenure/continuity); exa (2) is neighbors (C3). | **Partial** — machinery yes, traction-coverage thin and dominated by a non-traction signal |
| **2. Comparability** | Make repeat captures comparable (deltas/velocity) | Only **11/126 (9%)** are delta-able on a traction type (C4). Even those mostly don't yield clean deltas: `sec_edgar` has **no delta branch** in `signal_delta.py` (4 cos blocked); the 2 "delta-able" SERP cos (waldo, niagenplus) are **same-session multi-query runs, not temporal re-captures — 0 of 2 have a real time-series delta** (subject-identity gap); Trends is single-snapshot for all 5 + 14×-normalization-fragile; only Trustpilot diffs cleanly (~6 per run-018) — and that delta = **solicitation cadence on paid profiles, not demand** (MRL-008/012). | **Weak** — barely standing; the one diffable axis is the most confounded |
| **3. Accumulate** | Accumulate into a durable timeline without polluting State | Append-only `store/<domain>/signals/<source_type>/<captured_at>.json` (C8). State layer carries **0** structured traction fields — correct: the frame says traction never lands in `profile.md` (C6). | **Yes** on shape — but **single-campaign; no refresh cadence yet** (captures cluster 06-08→06-15, MRL-012), so the timeline is a snapshot pile, not an accumulating series |
| **4. Cohort-rollup** | Roll up across a cohort for relative reads | **Not buildable today.** GLP-1 (most-captured cohort, **19** strict-anchored members — method-sensitive: up to 24 if you count any GLP-1 *offerer* mention, the MRL-001 anchored-vs-all-offerers caveat): **5/19** any traction signal, **4/19** delta-able, **all four sharing only Trustpilot** as their cross-company axis (C7). Telehealth-wide (54): 19 any-signal, 10 delta-able, scattered across 3 axes — no axis ranks even half a cohort (C5). | **No** — frame correctly defers this to a sibling frame |
| **5. Feed judgment, never emit** | Feed a consumer-owned judgment; never emit one as truth | The store emits no traction/formidability score; this run emits none. | **Held** — correct by design |

**One-line answer:** *Yes, the store exposes traction signals — but for only 16% of profiled
companies, on a non-traction-dominated capture mix, with 9% delta-able and no cohort that rolls
up. The plumbing is right; the substrate is too thin and too confounded to map a cohort. The
binding constraints are coverage → comparability → rollup, in that order — none of them a missing
primitive.*

## Gap Map

For a gap-probe this is the main result. Where Truffle answered cleanly vs fell short:

- **Answered cleanly (the substrate question):** What traction signal each company exposes, at
  what cadence, is fully readable store-only — one `signals/` walk + axis mapping. The frame's
  rungs 1, 3, 5 are observably built/correct. The store *can* say, per company, "here is the
  cited axis-specific evidence I hold" — exactly the frame's first-graduating capability.
- **Fell short #1 — coverage (rung 1):** 16% traction-signal coverage, and the dominant captured
  signal (Wayback) isn't traction. The 20 traction-signal cos are a near-identical sec_edgar+
  trustpilot **batch campaign on hormone/men's-health brands** → the traction substrate inherits
  the corpus's selection bias (MRL-001). What would change it: a **traction-capture campaign**
  across a real cohort, not a market-representative claim from today's set.
- **Fell short #2 — comparability quality (rung 2):** delta-able ≠ usable velocity. The
  comparator (`signal_delta.py`) exists but is **incomplete** — no sec_edgar branch (MRL-012's
  named ~30-min fix) — and the one clean axis (Trustpilot review-count) is a confounded proxy.
  What would change it: the comparator branch + per-source cadence + a pinned canonical subject
  (MRL-012's three sub-fixes), and capturing a *demand* signal that isn't solicitation-cadence.
- **Fell short #3 — cohort-rollup (rung 4):** no cohort has enough same-axis comparable members.
  This is the frame's explicitly-deferred sibling frame; the run **confirms with numbers** why it
  can't be shortcut from the per-company layer: even the most-captured cohort is ~21% covered
  (4/19 delta-able) on one confounded axis.
- **Correct non-gap:** the empty State traction fields and the absent emitted score are **not**
  defects — they are the frame's boundaries held. A naive read calling "0 traction fields in
  profile.md" a gap would be wrong.

## Evidence Used

All claims are store-derived (no external/current claims; no snippets). Receipt: `receipts/R1-traction-signal-inventory.md`.

- **C1** — traction = Signals on the 5-rung ladder; 5 source-types proxy traction, wayback/exa do not. (R1 S1,S4)
- **C2** — 49/126 profiled have `signals/`; only **20** carry a genuine traction signal. (R1 S1)
- **C3** — most-captured signal (Wayback, 47) is **not** traction. (R1 S1)
- **C4** — **11/126** delta-able on a traction type; most deltas blocked/confounded per run-018/MRL-012. (R1 S1,S5)
- **C5** — among delta-able cos only Trustpilot has enough members to compare (9 vs sec 4, serp 2). (R1 S1)
- **C6** — State layer: **0** structured traction fields (correct by frame); 29 prose mentions. (R1 S2)
- **C7** — GLP-1 (**19** strict-anchored; method-sensitive 19–24 per MRL-001 / run-016 "parse the value, not the comment"): 5/19 any-signal, 4/19 delta-able, all sharing only Trustpilot. (R1 S3,S1)
- **C8** — append-only `signals/<type>/<clock>.json` accumulation path is the right durable shape. (R1 S1)

49 signal-bearing companies inventoried (full list + counts in R1). The traction-signal core (20):
agelessrx, defymedical, directmeds, eden-health, getpetermd, gogeviti, hims, honehealth, hydramed,
joinamble, joinfridays, marekhealth, maximustribe, mylifeforce, niagenplus, sermorelin, struthealth,
trtnation, truniagen, waldo. Delta-able core (11): agelessrx, eden-health, hims, honehealth,
hydramed, joinamble, joinfridays, maximustribe, niagenplus, sermorelin, waldo.

**Axis distribution of the 20 (what the substrate actually looks like):** essentially all 20 carry
the **sec_edgar + trustpilot pair** (the batch campaign — capital footprint + trust-flow proxy); only
**5** add an attention signal (trends), only **2** add SERP (waldo, niagenplus), only **1** adds ads
(waldo). So "multi-axis" is really a **handful of brands** — honehealth (sec+trends+trustpilot, 16
captures), hims (sec+trends+trustpilot), maximustribe, waldo (the only ads+serp+exa+sec carrier),
niagenplus (the only SERP telehealth co). **No company has a clean cross-axis triangulated picture**
(even the richest have single-snapshot trends + un-diffable sec_edgar).

## Missing / Stale Coverage

- **The traction layer is hormone/men's-health-skewed by construction.** The 20 traction-signal
  cos are essentially the sec_edgar+trustpilot batch set; no behavioral-health, women's-health,
  SaaS, or non-telehealth company carries a traction signal except waldo/niagenplus. Any
  "traction map" off today's store would map *the capture campaign*, not a market.
- **No company has a clean cross-axis traction read.** Even honehealth (richest) has trends as a
  single snapshot and sec_edgar with no diff branch — so its "how is it doing?" card is one clean
  Trustpilot velocity + level reads, not a triangulated picture.
- **Stale-risk:** captures cluster 2026-06-08→2026-06-15; nothing is being refreshed on a cadence
  (MRL-012). A traction read is only as live as the last manual capture.

## Source Gaps

- **A demand signal that isn't solicitation-cadence.** Trustpilot review-count velocity is the
  only well-covered delta, and it measures invitation posture on paid profiles, not demand. The
  frame's "demand" axis has no clean store proxy today.
- **Comparator completeness:** the sec_edgar delta branch (MRL-012) is the single highest-leverage
  missing piece for the capital axis — 20 cos have sec_edgar, 0 are tool-diffable.
- **A cohort capture campaign** is the prerequisite for rung 4 — not a new tool, just coverage.

## Raw Learning to Preserve

See `run-notes.md` Discovery ledger: **O1** (16% traction coverage), **O2** (most-captured signal
isn't traction), **O3** (traction substrate inherits selection bias), **G1** (rung-2 comparability
weak: delta-able ≠ usable), **G2** (rung-4 rollup unbuildable, numbers), **S1** (rungs 1/3/5 built,
2/4 not — "plumbing not substance"), **S2** (State carries 0 traction fields = correct, not a gap),
**W1** (no new primitive; coverage+comparator+cohort layer), **F1** (Wayback page-grain walk friction).

## External Completeness Check

Not run — store-only by contract. The completeness question here is internal (which captured cos
expose traction), not market-membership; an external denominator (who *should* have traction) is a
bounded-live follow-up, deliberately deferred this cycle. Flagged in Source Gaps.

## Market Pattern

1. **Capture machinery is ahead of capture coverage.** The engine built the right traction
   plumbing (path, comparator, 6 tools) before populating it — so the store *looks* signal-rich
   (49 dirs) but is traction-poor (20 cos, 11 delta-able). The gap between "we have a signals
   layer" and "we can read traction" is **coverage + comparability**, not architecture.
2. **The dominant captured signal is the least traction-relevant.** Wayback (47 cos) measures
   page tenure; it's cheap and ran widely, but answers "how old is this page?", not "how is this
   company doing?". Capture volume ≠ traction signal — the frame's grain-trap, made concrete.
3. **Traction inherits the corpus's selection bias.** The traction-bearing set is the men's-health/
   hormone batch — the same bias MRL-001 tracks for cohort reads now bounds the traction substrate
   *before any rollup runs*. A cohort traction-map would be doubly coverage-bounded.
4. **The boundaries the frame drew are being held.** No traction State field, no emitted score —
   the State/Signals/Judgment separation survives contact with a real traction read. The open edge
   (formidability) stayed out, cleanly.

## What Would Change This Answer

- **A traction-capture campaign on one real cohort** (e.g. capture sec_edgar+trustpilot+trends+
  serp for all 19 GLP-1-anchored brands, twice, with pinned subjects) would move rung-4 from "not buildable"
  to "testable" — and is the single change that would most change this read. It needs Firecrawl
  spend + human approval (not autonomous-safe), so it's a proposed worklist, not this run's action.
- **The sec_edgar delta branch** (MRL-012, ~30 min) would turn 20 captured capital footprints into
  diffable funding-pulse — the cheapest rung-2 improvement.
- **A bounded-live freshness check** (the deferred candidate) re-capturing a few traction signals
  live would tell us how fast the layer rots — the missing cadence input for rung 2/3.
- If a second traction read on a *different, non-hormone* cohort found the same 1+3-built / 2+4-thin
  shape, it would harden "plumbing-ahead-of-coverage" from a one-run pattern into a roadmap fact.
