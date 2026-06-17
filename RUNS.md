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
| `record_version` | Required quoted MAJOR.MINOR for this JSON envelope. Current: `"0.1"`. This is not a markdown `schema_version`. |
| `verb` | Required: `research-company` · `deepen-offerings` · `visual-evidence`. The filename derives from this value. |
| `status` | Required: `complete` · `partial`. Skips, crashes, and aborts write no record. |
| `tool` | Required stable slug for the lead tool, e.g. `claude-code`, `codex`. Claude Code is env-detected; otherwise agent-supplied. |
| `model` | Required stable id for the lead model, e.g. `claude-opus-4-8`, `gpt-5.5`. Use canonical ids, not friendly labels. |
| `effort` | Optional raw per-tool effort string. Claude Code uses `CLAUDE_EFFORT`; if Claude Code is detected and effort is empty, write `"unknown"`. For tools without a reliable effort source, omit it unless the agent knows it. |
| `trust` | Required: `env` when tool/effort came from deterministic environment, `agent` when self-reported. `model` is agent-known and not separately trust-tagged. |
| `started_at` | Required ISO-Z instant. It names the file as `<YYYYMMDDTHHMMSSZ>-<verb>.json`; UTC avoids cross-midnight ambiguity. |
| `ended_at` | Optional ISO-Z instant, stamped only on clean write. Wall time is derived from `ended_at - started_at`; do not store `wall_seconds`. |
| `artifacts` | Required list of repo-relative markdown artifacts touched, e.g. `["profile.md"]`. Empty list is allowed for a partial run that produced no markdown. Assets ride with their markdown artifact. |
| `components` | Optional list of LLM helpers only, each `{ "tool": "...", "model": "...", "role": "..." }`; omit for single-agent runs. Deterministic shell tools (`fc.py`, Playwright, ImageMagick) are not components. |
| `note` | Optional one-line run color. Never make it the sole home of a company fact. |

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

Use `--tool codex --trust agent` when the tool cannot be env-detected. Add `--artifact offerings.md`, `--artifact visual.md`, `--components-json '[...]'`, or `--note "..."` only when they apply.

Do not write warm-skip records. Do not write crash/abort records. Absence of a run record means "not recorded" for pre-0.1 history, or "no completed write reached the recorder" for a new run.

## Timing Read

One run has one wall clock, attributed to the lead `model`. If a run used helper models, scan `components` to find them, but do not infer separate timing for those helpers from this record.
