# RUNS — capture run records

> **What this is.** The contract for per-company run telemetry: which agent/tool, model, and effort produced a capture, plus the run's start/end instants and markdown artifacts touched. It is operational metadata, not company State, so it lives out of `profile.md` frontmatter and out of human-facing dossier prose.

Run records are bare JSON files:

```text
store/<slug>/runs/<UTC-compact-Z>-<verb>.json
```

Example:

```json
{
  "record_version": "0.1",
  "verb": "research-company",
  "status": "complete",
  "tool": "claude-code",
  "model": "claude-opus-4-8",
  "effort": "xhigh",
  "trust": "env",
  "started_at": "2026-06-17T15:30:12Z",
  "ended_at": "2026-06-17T16:12:48Z",
  "artifacts": ["profile.md", "offerings.md"],
  "components": [{ "tool": "codex", "model": "gpt-5.5", "role": "claim-audit" }],
  "note": "GPT-5.5 claim-audit caught one unsupported ownership read."
}
```

## Field Contract

| Field | Contract |
|---|---|
| `record_version` | Required quoted MAJOR.MINOR for this JSON envelope. Current: `"0.1"`. Not a markdown `schema_version` — see **Versioning** below. |
| `verb` | Required: `research-company` · `deepen-offerings` · `visual-evidence`. The filename derives from this value. |
| `status` | Required: `complete` · `partial`. Skips, crashes, and aborts write no record. |
| `tool` | Required stable slug for the lead tool. **Both Claude Code and Codex are env-detected** (`CLAUDECODE` / `CODEX_SHELL`·`CODEX_THREAD_ID`·`__CFBundleIdentifier`), so neither needs `--tool`; other tools pass `--tool`. An undetected, unnamed tool is recorded `unknown` (the record still lands) rather than failing the write. |
| `model` | Stable lead-model id, e.g. `claude-opus-4-8`, `gpt-5.5`. The env doesn't carry it (neither tool exposes it), so it's the one field nobody can env-stamp. Source order: **`RUNREC_MODEL`** (your session declaration — authoritative) → `--model` (agent best-known) → `"unknown"`. Use canonical ids, not friendly labels; normalize synonyms at read time. |
| `effort` | Optional raw per-tool effort string. Source order: **`RUNREC_EFFORT`** (your declaration) → `--effort` → Claude Code's `CLAUDE_EFFORT` (auto). Omitted when none of those exist (Codex exposes no effort env). |
| `trust` | Required: `env` when the tool was env-detected **or** an explicit `--tool` the environment corroborates; `agent` when self-reported (or an explicit tool the env can't confirm). `model` is agent-known and not separately trust-tagged. |
| `started_at` | Required ISO-Z instant. It names the file as `<YYYYMMDDTHHMMSSZ>-<verb>.json`; UTC avoids cross-midnight ambiguity. |
| `ended_at` | Optional ISO-Z instant, stamped only on clean write. Wall time is derived from `ended_at - started_at`; do not store `wall_seconds`. |
| `artifacts` | Required list of **bare, company-dir-relative** markdown filenames, e.g. `["profile.md"]` — **not** `store/<slug>/profile.md` (the writer strips a stray prefix). Empty list is allowed for a partial run that produced no markdown. Assets ride with their markdown artifact. |
| `components` | Optional list of LLM helpers only, each `{ "tool": "...", "model": "...", "role": "..." }`; omit for single-agent runs. Deterministic shell tools (`fc.py`, Playwright, ImageMagick) are not components. |
| `note` | Optional one-line run color. Never make it the sole home of a company fact. |

**Versioning.** `record_version` versions *this envelope only*. Every artifact keeps its own `schema_version` **inside itself** — a run that writes `profile.md` (2.6) + `offerings.md` (1.2) + `telehealth.md` (1.0) still stamps `record_version` `"0.1"` here. `artifacts` lists **paths, never versions**; to read an artifact's contract version, open the artifact (it's also in `store.db`).

## Write Rule

The capture skill stamps `RUN_STARTED_AT` immediately after slug resolution:

```sh
RUN_STARTED_AT="$(python3 "$WEB_RESEARCH_HOME/scripts/runrecord.py" now)"
```

At the end of a run that did work, it writes the record:

```sh
python3 "$WEB_RESEARCH_HOME/scripts/runrecord.py" write \
  --slug <slug> \
  --verb research-company \
  --started-at "$RUN_STARTED_AT" \
  --model claude-opus-4-8 \
  --artifact profile.md
```

Both Claude Code and Codex are env-detected, so `--tool`/`--trust` are rarely needed — pass `--tool <slug>` only for a tool the env can't identify. Add `--artifact offerings.md`, `--artifact visual.md`, `--components-json '[...]'`, or `--note "..."` only when they apply.

**Declaring model/effort.** Neither is in the env, so the per-run source is the agent's `--model`/`--effort` (relay what you were told at session start); absent that, `model` is `"unknown"` and `effort` is omitted — the record still lands.

**Batch pin (power option).** `RUNREC_MODEL`/`RUNREC_EFFORT` override authoritatively — but they must live in the **launch environment**, not an in-session `export`. Each agent shell is fresh (shell state doesn't persist between tool calls), so an in-chat `export` is gone before the writer runs. Set it where you start the tool:

```sh
RUNREC_MODEL=gpt-5.5 RUNREC_EFFORT=high codex      # or put it in your shell profile
```

A profile-level pin is **sticky** — it labels *every* session until you unset it. Use it for a deliberate same-model batch and clear it when you switch models.

Do not write warm-skip records. Do not write crash/abort records. Absence of a run record means "not recorded" for pre-0.1 history, or "no completed write reached the recorder" for a new run.

## Timing Read

One run has one wall clock, attributed to the lead `model`. If a run used helper models, scan `components` to find them, but do not infer separate timing for those helpers from this record.
