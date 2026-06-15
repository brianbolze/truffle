# RETRO — Traction Signals v1 velocity run (~3 credits)

Date: 2026-06-15 · The companion to the [salvage retro](2026-06-15-traction-salvage.md). The salvage landed flat Jun-8 baselines and predicted *"the runner earns its turn later, when a fresh D7 point — trustpilot velocity's missing second capture — is actually worth the spend."* This is that capture. First run that **watches a traction signal move on a live company**, and the first to exercise the **native** capture→persist→diff loop (the salvage only copied already-paid envelopes). Companies: hims-com / honehealth-com / maximustribe-com.

## 30-second skim

- **The headline answered cleanly: velocity moved, and it's sane.** Cumulative Trustpilot `review_count` over ~6.2 days: **Hone +65 (10.4/day) · Hims +54 (8.7/day) · Maximus +7 (1.1/day)** — all monotone-positive, ranking matches maturity, no number needs a second look. The engine answered its own core question — *"is it growing?"* — on real data for the first time.
- **Integrity held without a false positive.** `paid_profile` flagged all three (correct — all paid+solicited); **no hard veto fired**, and the one that *looked* like it should (Hims `merged=True`) correctly **didn't** — the code vetoes merged-*between*-captures, not stable-merged. The rolling-window metric (`reviews_last_12m`) was correctly suppressed to `delta=null`.
- **Cost: exactly 3 Firecrawl credits** (1/profile, as documented). Everything else was free.
- **Free sources round out the store:** 8 wayback re-captures (**7 flat, 1 moved** — a surprise), plus the **first-ever** `sec_edgar` + `trends` D0 envelopes in the store (the salvage found zero of either anywhere). Hims sec_edgar pulled **10 real filings**.
- **Native-capture friction is real and uniform:** every capture needs the same **~6-step stdout→store bridge** the tool provides none of. I'd folded it into a shell function by capture #4. 17 captures this run.
- **Orchestration call — both, and they're one tool:** the runner the salvage deferred is now **earned**, but it and the salvage's importer share a single `persist` primitive. Build that; the runner and importer are thin shells over it.

---

## What I captured (real paths)

| source_type | hims-com | honehealth-com | maximustribe-com | mode | cost |
|---|---|---|---|---|---|
| **trustpilot** | `…/trustpilot/20260615T041642Z.json` | `…/20260615T041714Z.json` | `…/20260615T041747Z.json` | **delta** vs Jun-8 D0 | 3 credits |
| **wayback** (3·3·2 pages) | 3 pages re-captured | 3 pages | 2 pages | **delta** vs Jun-8 D0 | free |
| **sec_edgar** | `…/sec_edgar/20260615T042723Z.json` | `…/20260615T042726Z.json` | `…/20260615T042729Z.json` | D0 (no prior) | free |
| **trends** | `…/trends/20260615T042908Z.json` | `…/20260615T042909Z.json` | `…/20260615T042910Z.json` | D0 (no prior) | free |

17 envelopes persisted to `store/<domain>/signals/<source_type>/…`, every filename `= captured_at` with `-`/`:` stripped (the documented convention). `sec_edgar/` and `trends/` are **new subdirs** — the salvage never created them (those tools postdate its source runs).

## The velocity read (the actual test)

`signal_delta.py D0.json D7.json`, per company — exit 0, `read_mode: delta`:

| Company | `review_count` D0→D7 | Δ | gap_days | **velocity/day** | flags | vetoes |
|---|---|---|---|---|---|---|
| **honehealth-com** | 11579 → 11644 | **+65** | 6.26 | **10.38** | `paid_profile` | — |
| **hims-com** | 8500 → 8554 | **+54** | 6.22 | **8.68** | `paid_profile` | — |
| **maximustribe-com** | 975 → 982 | **+7** | 6.26 | **1.12** | `paid_profile` | — |

**Is the velocity sane? Yes, on every axis.** Monotone-positive (cumulative-lifetime can't go down); plausible weekly cadence; the ranking (Hone > Hims > Maximus) tracks audience size, and Maximus at ~1/day matches its 975-review base. This is the cleanest possible "it works."

Three design behaviors held under live data:

- **`reviews_last_12m` delta suppressed to `null`** (levels still reported: Hims 1991→2052, Hone 5553→5627, Max 487→494). It's a rolling window anchored to each capture date — subtracting it double-counts the moved left edge. The tool refuses the subtraction and says why. The cumulative-vs-rolling distinction is real, not doc theory.
- **`gap_days` = 6.2, not 7.** The salvaged D0 was captured ~22:00–23:00Z Jun-8; my D7 ~04:16Z Jun-15. The brief's "~7-day" was loose; the tool divides Δ by the *actual* gap, so the per-day number is honest regardless.
- **The flag, not a verdict.** All three are `paid_profile` + `asks_for_reviews`, so the count grows partly because they *solicit*. The tool says "solicitation/surfacing caveat" and computes the velocity anyway — the number is real, the interpretation is caveated. That's the capture/judgment line working.

## Integrity discipline meeting real profiles

The interesting result is the veto that **correctly didn't fire.** Hims is `merged + paid + ai_assisted` — the [trustpilot.md](../../tools/trustpilot.md) "not apples-to-apples" profile, and the [signal_delta.md](../../tools/signal_delta.md) branch table reads "removed/merged → veto." I expected a Hims veto. None came — only the paid flag.

**That's right, and the code is more careful than the doc table.** `signal_delta.py:168` fires the merge veto only when `later` is merged AND `earlier` is *not* — i.e. the profile merged *between* captures (a structural break that jumps the count for non-organic reasons). Hims was merged at *both* ends, so the basis is stable and the +54 is a valid same-basis delta. The veto guards a mid-window change, not a standing state. **Doc-precision note (not a bug):** the branch table's "merged → veto" should read "merged-*between-captures* → veto" to match the code.

The other guards, checked against real data:

- **`templated_reviews`: checked, clean.** All three D7 captures carry 20 `recent_reviews`; the dup-body detector (≥2 identical bodies) found none. (The *salvaged* Hims D0 has `recent_reviews: null` — a salvage artifact — but the delta's templated check reads the *later* capture, which is intact, so it still ran.)
- **`bursty_growth`: correctly silent.** Fires at Δ > 50% of base; here Δ is 0.6–0.7% of base. No false alarm on tiny organic weeks.
- **`profile_state`: all `active`** at both ends — no removed/not_found flip to void a pair.

## Free sources

**Wayback (8 pages re-captured, diffed D0→D7) — 7 flat, 1 moved.** As predicted, niche product pages don't get re-crawled weekly: 7/8 showed `snapshot_count` Δ0 with `last_seen` and `content_digest` unchanged (`tenure_days` grows mechanically — it's `now − first_seen`). The surprise: **`honehealth-com/.../mens-sermorelin` flipped `archive_presence` False→True** (`snapshot_count` 0→1, `last_seen` → 2026-05-08, a digest appeared) — between my two captures the Internet Archive's CDX began returning a snapshot it hadn't before. So a week *did* move one thing, and it wasn't one I'd have bet on. The wayback branch applies the same level-vs-delta discipline as Trustpilot: only `snapshot_count` carries a `delta`; presence/timestamp/digest report d0/d7 with `delta=null` (they're flips, not subtractions).

**sec_edgar D0 — the public/private split is exactly the value.** Hims resolved to a real public filer (CIK 0001773751, NYSE, *Hims & Hers Health, Inc.*) with **10 filings** (8-K / 10-Q / 10-K, Nov-2025 → Jun-2026) → 10 factual cards. Hone and Maximus both returned `name_match_unconfirmed`, 0 cards — and for Maximus that's the **identity-seam guard working**: "Maximus" collides with public Maximus Inc (MMS), so the tool refuses to attribute rather than guess. Factual no-match is data.

**trends D0 — levels seeded, disambiguation needed.** Hone mean 56 / Hims 46 / Maximus 3.5 — but these are within-keyword (not cross-comparable for volume), so they're baselines for future weekly trajectory, not a ranking. Disambiguation was load-bearing: `Hims & Hers::Hims` (the bare phrase returns ~0.7 — the ampersand kills it) and `Maximus::Maximus tribe` (bare "Maximus" is Gladiator/Maximus-Inc noise). The Maximus series came back thin (mean 3.5, labeled `fading` — trajectory-on-near-zero is noise, as the tool warns).

## Surprises only live data exposed

1. **The merged veto that shouldn't fire, didn't** — and exposed the doc-table shorthand above. Fixtures with invented flags wouldn't have caught the stable-vs-changed distinction.
2. **One free signal actually moved** (sermorelin archive-presence flip) on a week I'd written off as flat — the honest answer wasn't the predicted one.
3. **pyenv shim non-determinism bit the wayback leg.** `python3 tools/wayback.py` died once with `pyenv: version '3.11' is not installed` while `trustpilot.py`/`signal_delta.py` ran fine seconds earlier — the global pin is `3.11.9`, and the bare `python3` shim intermittently resolved to a non-existent `3.11`. Pinning the interpreter (`~/.pyenv/versions/3.11.9/bin/python3`) made every subsequent call deterministic. **A batch runner must pin the interpreter**, not trust the shim.
4. **The store had no `source_type` slot decision for new tools.** trustpilot/wayback got lucky (tool name == subdir). sec_edgar breaks the tie: tool is `sec_edgar`, but its cards carry `source_type: "sec"`. I chose `sec_edgar/` (tool-name, consistent with the others) — but nothing *defines* that, so two callers could diverge. A persist helper should own this mapping.
5. **`trends.py`'s "owns the loop" design fights the per-domain store.** It takes the whole keyword list and emits one multi-subject envelope; the store wants one envelope per domain. I worked around it by calling it 3× single-keyword. Fine at N=3; a note for whoever batches a cohort.

## Native-capture friction (the step count)

The tool prints JSON to stdout and stops — by design (keeps it composable, judgment-free). So **every** capture needs the caller to hand-write the same stdout→store bridge:

1. resolve domain → store slug (`hims.com` → `hims-com`)
2. resolve source_type subdir (+ derive a `<page-slug>/` for wayback — *two* path parts the tool never emits)
3. `mkdir -p` the subdir (only bit the new types — sec_edgar, trends)
4. run tool → temp file, **check exit / re-run on transient** (Cloudflare wait, pyenv flake)
5. parse `captured_at` out of the JSON
6. compactify → filename, assemble dest path, `mv` into place

**~6 steps per capture, the tool does step 4's output and nothing else.** Unit cost is identical every time, which is the tell: I hand-bridged the 3 Trustpilot captures individually, wrote a shell function by the 4th, and looped the remaining 14 (8 wayback + 3 sec + 3 trends). **17 captures total.** The reflex to abstract the persist away on the very first repeat *is* the orchestration evidence — felt, not theorized.

## The orchestration call — both, unified by one primitive

The salvage retro deferred the runner and pointed at an importer. Having now felt **both halves** — the salvage *placed* already-paid envelopes; this run *ran-then-placed* fresh ones — the answer is:

**Both are earned, and they're the same tool wearing two hats.** They share one missing primitive:

> **`persist(envelope) → store/<domain>/signals/<source_type>/<captured_at>.json`** — computes the path from the envelope's own fields (`captured_at` → filename, `subject` → domain, `tool` → source_type), derives the `<page-slug>/` for page-grain sources, dedups on the *canonicalized* subject (the slash-twin trap the salvage hit), and pins the interpreter. ~30 stateless lines. In-bounds — a CLI wrapper, not the "living infrastructure" the [anti-Doro line](../2026-05-30-architecture.md) refuses.

- **Batch runner** = `persist` + "run tool X over subjects […]" — earned *now*, because this run proved a fresh D7 is worth the spend and the headline signal (Trustpilot velocity) recurs on a weekly clock. It also absorbs the friction above: the 6-step bridge ×17, the interpreter pin, the new-source_type `mkdir`.
- **Importer / consolidation** = `persist` + "place these existing envelopes" — the salvage, exactly. Same path logic, same dedup.

So the recommendation pushes back on building two things: **build the `persist` primitive first.** The runner and importer become ~10-line front-ends, and the conventions I had to decide ad hoc this run (source_type naming, page-slug derivation, captured_at→filename, canonical-subject dedup) get standardized in one place instead of re-litigated per caller.

## Bottom line

*Is it growing?* — **answered cleanly on live data.** Trustpilot review-count velocity moved, monotone and sane, on all three companies, with the right caveat flag and no false veto. Wayback exercised the loop and was ~flat (one honest archive-presence flip). sec_edgar + trends D0 seeded two source_types the store had never held. The build is sound; the gap is purely orchestration — a `persist` primitive that the weekly runner and the salvage importer both stand on.

<sub>**Method** — read [signal_delta.md](../../tools/signal_delta.md) + [trustpilot.md](../../tools/trustpilot.md) + the salvaged Jun-8 D0 envelopes; captured Trustpilot (3 credits) + wayback/sec_edgar/trends (free) via the live tools; diffed with `signal_delta.py`; verified the merged-veto logic against `signal_delta.py:154-192`. No engine code changed — dogfood only. Numbers are this run's actuals; counts current as of capture (review counts move hourly).</sub>
