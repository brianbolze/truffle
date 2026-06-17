# FINDINGS — run-record layer, first production run

Date: 2026-06-17 · The de-risking that should have *preceded* codifying the run-record contract ([design](../../_design/2026-06-17-run-records.md)), recorded after the fact. Pairs with the fixes in commit `fcd11f6`.

## What ran

The first real multi-tool exercise of the run-record layer ([`modules/RUNS.md`](../../modules/RUNS.md)): **~14 records across 13 companies** — **2 in Claude Code (Opus 4.8)**, **~12 in Codex (GPT-5)** — mostly `visual-evidence`, a couple `research-company`. Brian drove it; the records landed in `store/<slug>/runs/`.

## Why it matters

The design was de-risked by a 6-lens panel + a 15-scenario battery — but **all on imagined scenarios, not observed behavior.** Scenario #2 ("cross-tool Codex") was reasoned about, never run. So the battery gave false confidence: it "covered" Codex on paper and missed every real Codex behavior below. This is the engine-dev *"hand-capture a few real companies before codifying"* rule, violated — the panel de-risked the *design*, nothing de-risked the *behavior*. This note closes that loop.

## What broke (and the fix shipped in `fcd11f6`)

- **Records dropped entirely.** `posthog`, `linear` were captured but wrote **no** run-record — the write was the *last* skill step, after the user-facing report, so agents stopped at the deliverable. `nurx`'s own note: *"Backfilled after omission."* → **Fix:** write the record *before* the report, marked required, in all three skills.
- **Codex footgun.** With no `--tool`, the writer hard-errored `tool could not be detected` and agents abandoned the bookkeeping. → **Fix:** detect Codex from its env signature (`CODEX_SHELL` / `CODEX_THREAD_ID` / `__CFBundleIdentifier=com.openai.codex`); an undetected tool now writes `"unknown"` instead of erroring.
- **Codex can't run the visual workflow.** `mine.workflow.js` is a Claude Code *Workflow*; Codex has no runner (`directmeds`: *"workflow runner not exposed in this Codex session"*). It improvised a degraded manual pass — and one record (`getpetermd`) **fabricated 4 miners** by copying the skill's boilerplate JSON. → **Fix:** "components must be the miners that actually ran"; degraded passes record `status: partial`.
- **Model-id chaos.** `gpt-5` vs `gpt-5-codex` across runs; Brian expected `gpt-5.5`. Self-report is unreliable. → **Fix:** declare-or-fallback (`RUNREC_MODEL` / `--model` / `"unknown"`); normalize synonyms at read time.
- **Effort absent for all Codex.** Not in Codex's env, never instructed. → **Fix:** `RUNREC_EFFORT` / `--effort` / omit.
- **`trust` inconsistent.** `marek`=`agent` vs `trt`=`env` — *both* Claude Opus — because one agent passed `--tool` and one didn't. → **Fix:** `trust` is `env` only when the env *corroborates* the named tool.
- **Artifact path ambiguity.** `directmeds` wrote `store/directmeds-com/visual.md`; everyone else `visual.md`. → **Fix:** the writer strips a stray `store/<slug>/` prefix.

## Codex environment (discovered)

```
CODEX_SHELL=1   CODEX_THREAD_ID=019ed727-…   __CFBundleIdentifier=com.openai.codex
CODEX_SANDBOX=seatbelt   CODEX_SANDBOX_NETWORK_DISABLED=1   CODEX_CI=1
```
Tool is deterministic. **Model and effort are not present** (neither is Claude's model) — they remain agent-declared. Observed on **Codex Desktop**; a CLI variant may differ (the `"unknown"` fallback catches a missed signature).

## Open / residual

- **The 14 records are pre-fix test residue.** Their Codex fields (`model` id, missing `effort`, fabricated `components`) and `directmeds`'s path are **not** retro-corrected — rewriting telemetry after the fact fabricates provenance. They predate every fix here; a clean slate is **delete + re-capture** (regenerates correct records under the fixed writer), which is Brian's call. Until then, filter `runs/` by date / `record_version` before aggregating.
- **Lesson for the engine:** a single real probe capture, per tool, *before* codifying would have surfaced all of the above for free. The panel + battery are good for design shape; they are not a substitute for one real run.
