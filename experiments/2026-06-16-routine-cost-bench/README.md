# Routine cost benchmark — 2026-06-16

**Goal.** A measured per-verb baseline (credits · minutes · tokens) to budget the automated
Claude Routines that will capture / refresh / deepen the store. This is the **baseline** step
only — what the routines *should do*, and any plan upgrades, come after.

## What's already known vs what this measures

- **Credits — already authoritative**, not the unknown. `fc.py` records Firecrawl's own
  per-call `creditsUsed` to each capture's `manifest.jsonl`; `scripts/runcost.py` rolls it up.
  Recent baseline (`runcost.py captures --since 2026-06-10`): **median 8, p90 12, max 14**.
  The benchmark just *records* credits per run (and drift-checks them against that baseline).
- **Tokens + wall-clock — the real holes.** Not visible to any script the verb runs; they live
  in the session transcript + the clock. The benchmark captures them via `tally.py`.
- **Signals are NOT benchmarked.** Their cost (SerpApi searches, FC credits) already self-records
  in the signal envelopes and rolls up via `runcost.py signals` — no token-heavy session to measure.

## The variant matrix (one run each, own clean session)

| # | Verb / mode | Brand | Slug | Measures |
|---|---|---|---|---|
| A | `/research-company`, **core only** (no modules) | Alt Rx `altrx.com` | `altrx-com` | capture floor (focused ~6-SKU brand) |
| B | `/research-company`, **full telehealth** (cohort + offerings + logos) | Wisp `hellowisp.com` | `hellowisp-com` | rich path, vast catalog (upper range) |
| C | `/visual-evidence` | `henrymeds-com` | `henrymeds-com` | post-capture mine — **0 credits**, pure token/time |
| D | `/deepen-offerings` | Opt `getopt-com` | `getopt-com` | the deepen routine (roster is `lines-omitted`) |
| E | `/research-company`, **default freshness** (no forced refresh) | `niagenplus-com` | `niagenplus-com` | warm path — what the freshness gate saves |
| F | `/research-company`, **forced full re-scrape** | `niagenplus-com` | `niagenplus-com` | warm upper bound; E↔F = freshness-gate value |

**Run order:** A → B → C → D → E → F. E before F (capture the fresh-serve path before forcing
a re-scrape on the same company). A/B/C/D are independent.

**Setup / prereqs (confirm at run time):**
- Cold brands (A, B) must be **absent** from the store — confirmed 2026-06-16; re-check with
  `python scripts/store.py find altrx.com` (and `hellowisp.com`) → "not in store".
- E/F: `niagenplus-com` was captured 2026-06-15, so default freshness should read it **fresh**.
  Run soon so it stays inside the TTL, else the E↔F contrast blurs.
- D: `getopt-com`'s `offerings.md` is flagged `enumeration: lines-omitted` → real work (won't decline).

## How a run records itself — `tally.py`

Each standalone session does only: print a unique marker → stamp start → run the verb →
`tally.py` → print the row. `tally.py` then, from three honest sources:
- **credits** ← this run's `manifest.jsonl`, windowed by the run's start/end mtime so a same-day
  sibling variant's scrape can't be miscounted (0 for C and a warm-serve E).
- **tokens** ← this session's own transcript, found by the marker (`grep` across `~/.claude/projects`),
  summing `message.usage` (in / out / cache_create / cache_read). Slight undercount: the final
  tally turn isn't flushed yet. If the marker isn't found, the row flags `TOKENS-NOT-FOUND` (read `/cost`).
- **minutes** ← the start/end epochs the prompt stamped around the verb.

Rows append to `results.csv`. Re-running a variant is safe (newest marker-match wins; window keeps credits clean).

## Aggregation (after all 6 rows land)

A final session merges `results.csv` + the `runcost.py` baseline into a dated
**`## Measured baseline`** section appended to [`_design/2026-06-16-routine-budgeting.md`](../../_design/2026-06-16-routine-budgeting.md)
— per-verb credits/minutes/tokens, the B−A module-bundle delta, the E↔F freshness-gate delta,
visual + deepen costs, and a drift-check vs the median-8 baseline. It **stops before** any
upgrade recommendation (that's the next step, once routine demand is defined). Every figure
traces to `results.csv`, `runcost.py`, or a transcript sum — "not measured" beats a guess.
The standalone + aggregation prompts were handed off in chat 2026-06-16.
