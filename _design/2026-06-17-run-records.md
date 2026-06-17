# Run records — capturing what produced each capture

Date: 2026-06-17 · Status: **implemented** ([PR #1](https://github.com/brianbolze/truffle/pull/1)) — contract shipped at [`modules/RUNS.md`](../modules/RUNS.md). Originated as a proposal: a Codex/GPT-5.5 proposal → a 6-lens anti-bloat critique panel → The Founder synthesis → the calls below. Anti-bloat carried decisive weight throughout.

## Short answer

The capture verbs (`/research-company`, `/deepen-offerings`, `/visual-evidence`) don't record **what produced a capture** — which tool (Claude Code / Codex), model (Opus 4.8 / GPT-5.5), and effort. We add a small **per-company JSON telemetry file per run** — `store/<slug>/runs/<run_id>.json`, a sibling of `captures/` and `signals/` — that stores only what code holds and can't recompute. ~9 keys on a typical run. No prose body, no new linter, no living infrastructure. The markdown dossiers stay untouched (zero cruft).

---

## Frame

**Problem.** A captured dossier carries no record of the agent that wrote it. As we run captures across tools (Claude Code, Codex) and models (Opus 4.8, GPT-5.5) at different effort levels, we can't answer "what made this?" — and can't compare capture quality/cost/speed by model, which is the live motive behind the [model bakeoff](../experiments/2026-06-13-research-company-model-bakeoff/FINDINGS.md).

**Why it matters.** This is the queryable key for engine *diagnostics / system-health* (run-time and credit-burn by model × effort × verb; which runs touched which model) — a corpus that pays off only if the provenance is captured consistently at write time, the same discipline as [`source_url`](../skills/research-company/scripts/fc.py) two commits prior.

**Goals.**
- Record tool / model / effort per capture, reliably, at write time.
- Enable cheap cross-run rollups (diagnostics, the bakeoff) without standing infrastructure.
- Stay light and add **zero** clutter to the human-facing dossiers.

**Non-goals.**
- **Not company State.** This is operational trust metadata — it stays *out* of `profile.md` frontmatter ("describe the company, not the engine").
- **No aggregation dashboard up front.** The files are the source of truth; a rollup script is a *later, derived* lens — built when a query exists, not before.
- **No crash-capture hook.** A watcher that must keep running to log failures is living infrastructure (anti-Doro). A crashed run leaves *no record*; absence = died (an orphan `captures/<date>/` with no run-record is the visible signal).
- **No unified cross-tool effort scale.** Premature normalization for a zero-consumer aggregator; store the raw per-tool string.

**Grounding facts (verified this session).**
- **Env exposure (Claude Code):** a skill-spawned shell sees `AI_AGENT` / `CLAUDECODE` (tool), `CLAUDE_EFFORT` (effort, e.g. `xhigh`), `CLAUDE_CODE_SESSION_ID`, `CLAUDE_AGENT_SDK_VERSION` — **deterministic**. `model` is *not* in env, but the agent knows it cold from its system prompt (`claude-opus-4-8`). **Codex also stamps a deterministic *tool* signature** (`CODEX_SHELL` / `CODEX_THREAD_ID` / `__CFBundleIdentifier=com.openai.codex`) — found in the production run, so tool is env-detected for it too; but **neither tool exposes model or effort**, so those stay agent-declared with an `unknown`/omit fallback. *(This corrects the original draft, which assumed Codex exposed nothing — see [the production-run findings](../experiments/2026-06-17-run-record-production/FINDINGS.md).)*
- **Versioning is already per-module.** `profile.md` runs `schema_version` 2.x; `offerings.md`/`visual.md` run their own 1.x; cohort packs their own (telehealth 1.0, with an inline "*independent of profile.md's*" comment). The store has **no global version** — each module owns its own. JSON telemetry (`signals/*.json`) uses `parser_version`, not `schema_version`. The run-record is one more independently-versioned module; it records **only its own** version and never mirrors the others (each artifact already stamps itself; the profile's is already in `store.db`).

---

## Proposal (recommended)

A bare JSON envelope, one file per run, in the signals/telemetry family.

**Path:** `store/<slug>/runs/<run_id>.json` · `run_id` = `<UTC-compact-Z>-<verb>` (e.g. `20260617T153012Z-research-company`), which also names the file.

```json
store/functionhealth-com/runs/20260617T153012Z-research-company.json

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
  "note": "GPT-5.5 claim-audit caught one over-read owns: line; functionhealth /pricing soft-404 dropped."
}
```

Typical run ≈ 9 keys. `effort`, `ended_at`, `components`, `note` are **omit-when-absent** — omission is load-bearing (means "not applicable / absent"; an explicit `"unknown"` means "looked, env was empty").

### Field contract

| field | type / values | filled-by | required? | why it earns its place |
|---|---|---|---|---|
| `record_version` | `"0.1"` (quoted MAJOR.MINOR) | code | yes | the run-record's **own** contract version — *not* `schema_version` (that name is the markdown-module convention; reusing it would falsely imply a shared version line). Anchors the backfill boundary. |
| `verb` | `research-company \| deepen-offerings \| visual-evidence` | code | yes | highest-value field — the tag `runcost.py` waits on today (it falls back to "(untagged)"). `run_id` derives *from* it, not stored twice. |
| `status` | `complete \| partial` | code (control flow) | yes | health signal. `skipped` is **not** a value (we don't write skip records — see decided calls); `failed`/`aborted` are **not** values (a dead agent writes nothing; absence = died). |
| `tool` | `claude-code \| codex \| …` | env (`AI_AGENT`/`CLAUDECODE`) | yes | the cross-tool axis; env-detected, never agent-asserted in Claude Code. |
| `model` | stable ID (`claude-opus-4-8`), **not** the label "Opus 4.8" | agent (self-known) | yes | the rollup axis — one canonical form store-wide or `GROUP BY` shatters into synonyms. **Lead model only**; sub-models live in `components`. |
| `effort` | raw per-tool string \| `"unknown"` | env (`CLAUDE_EFFORT`) | no | the other rollup axis. Raw — **no** unified scale. `"unknown"` = looked-and-empty; omitted = absent. Group by `(tool, effort)`, never `effort` alone. |
| `trust` | `env \| agent` | code | yes | one honesty flag over the spoofable axis (`tool`/`effort`): `env` = env-detected (Claude Code), `agent` = self-reported (Codex/headless). `model` is always agent-self-known and treated reliable, so it's orthogonal — no `mixed` needed. |
| `started_at` | ISO-Z instant | code (t0, stamped at run start) | yes | names the file/`run_id` (the always-UTC date rule resolves cross-midnight runs). |
| `ended_at` | ISO-Z instant | code (clean exit) | no | with `started_at` *derives* wall-time at read; don't store the subtraction. Absent on a crash — honest. |
| `artifacts` | list of `.md` paths | code (stat post-write) | yes (may be `[]`) | coverage ledger. Bare paths — git owns created/updated/unchanged for free; absence of a path = untouched. Assets ride with their `.md`, not listed. |
| `components` | list of `{tool, model, role?}` | agent | no (omit if single-agent) | real fan-out (visual miners, a GPT-5.5 claim-audit). **LLM sub-agents only** — a deterministic shell-out (playwright, fc.py) has no model and is *not* a component. No `count` (list length is the count); the lead is never folded in. |
| `note` | one-line string | agent | no | the "body," as a field not a format — run-color only (a soft-404 dropped, an audit catch). Never the sole home of a State fact. |

### Where it lives, who writes it

- **Contract doc:** a thin per-file contract. **Shipped at [`modules/RUNS.md`](../modules/RUNS.md)** — placed beside `OFFERINGS`/`VISUAL` to keep root uncluttered, and flagged there as the lone telemetry (non-State) member; in *form* a sibling to [`SIGNALS.md`](../SIGNALS.md)'s envelope (the `parser_version` family), not a State depth-module. Keep it to the table above + the omit-when-absent rules.
- **Writer:** a ~30-line helper the skill calls **at the end** of a run, from values it already holds — read env (`AI_AGENT`/`CLAUDE_EFFORT`/`CLAUDE_CODE_SESSION_ID`), take agent-supplied `model`/`verb`/`status`/`artifacts`/`components`/`note`, stamp `ended_at`. **No start/finish/record lifecycle object, no hook.** The one moving part: stamp `started_at` at run start (skill step after slug resolution) and carry it. Mirrors [`fc.py source_stamp`](../skills/research-company/scripts/fc.py) — code stamps the facts it can read; the agent supplies only what it knows.
- **Independent quick win — ship regardless:** add a `--verb` tag to `fc.py`'s per-call manifest write so [`runcost.py`](../scripts/runcost.py) gets cost-by-verb immediately, without waiting on any aggregator walking `runs/`. The record's `verb` and the manifest's `verb` tag are independent wins.
- **Wire three skills:** [`research-company`](../skills/research-company/SKILL.md), `deepen-offerings`, `visual-evidence` — each stamps `started_at` at start and calls the writer at end.

### Decided calls (Brian, this session)

- **Bare JSON, not markdown+frontmatter.** Signals already proved this record type needs no prose body; a second markdown substrate buys nothing and adds a YAML-parse + engine-narration-leak hazard. The "body" survives as the optional one-line `note`.
- **`record_version`, not `schema_version`** — see the field note; avoids the per-module overload.
- **Don't write warm-skip records.** A skip spent nothing and produced nothing; the existing capture clock already shows "how warm." Reserve `runs/` for runs that did work. *(Cheap reversal: if refresh-churn ever needs measuring, add a ~6-key skip skeleton with `status: skipped` and filter on it.)*
- **No `wall_seconds`, `cost`, `capture_dir`, `session_id`, `tool_version`, `run_id`-as-field, `metadata_source`-map, `artifacts[].action`, `run_profile`** — every one restates a fact that lives elsewhere (timestamps, the manifest, the date convention, git, the artifact itself). See Alternatives.

### Left to the implementer (low-stakes, panel-recommended defaults)

- **Heterogeneous-model timing (lead-attributed).** One run = one wall clock; attribute it to the lead `model`. `components` answer "which runs touched GPT-5.5" via a scan, but carry **no** independent timing. State this in the contract so rollups are honestly lead-attributed, not silently wrong.
- **Exact home of the writer helper** (`scripts/` vs alongside `fc.py`) and whether to add a `tests/test_runrecord.py` (like `test_signals.py`) — yes to a small test, **no** to a querycheck-style linter for v1.

### Must survive (scenario battery)

The design was stress-tested against these; the implementer should keep them as the test set:
1. Vanilla CC, one artifact. 2. Cross-tool Codex/GPT-5.5 (`trust: agent`, effort absent). 3. Fan-out (visual: lead + 4× sonnet → `components`). 4. Heterogeneous models in one run (Claude lead + GPT-5.5 audit). 5. Warm-skip (→ **no record written**). 6. Forced refresh over warm. 7. Crash mid-run (→ **no record**; absence = died). 8. `deepen-offerings` (offerings.md only). 9. Multi-artifact. 10. Unknown effort (`"unknown"` vs omitted). 11. Same session, many companies (`run_id` unique). 12. Aggregation read (one pass over `runs/*.json`). 13. Backfill boundary (old captures have no record → "not recorded", never an error). 14. Cross-midnight run (`started_at` UTC names the file). 15. Tier-B playwright shell-out (not a component; → `note` if anywhere).

---

## Alternatives considered

- **A — A prose `Run context:` line in each dossier's Provenance** *(first instinct).* Rejected: adds cruft to every human-facing file and is weak to aggregate (prose parsing). Diagnostics want structure out-of-band.
- **B — A frontmatter field next to `capture_method`.** Rejected: it isn't company State; it's per-artifact (a profile and its visual.md can be captured by different models), so a single profile scalar can't hold it; and it costs a real MINOR schema bump for profile-only coverage.
- **C — Codex's per-run JSON ledger + `runmeta.py` (start/finish/record) + `runstats.py` + timing + a `components` array.** Right placement instinct (out of frontmatter, honesty flag, no backfill), over-built mechanism: a lifecycle object threaded through three skills, a speculative aggregator with no consumer, and noisy wall-time fields. We kept the per-company per-run-file *shape* and cut the machinery.
- **D — Markdown + frontmatter run-record** *(an interim v0).* Rejected by the panel: forks a second substrate, risks engine-narration leaking into a parse-required record, and the signals precedent already settled this as JSON. The one thing markdown bought — a body — became the `note` field.
- **E — `run_profile` absorbs the SCHEMA 2.4 Provenance "Run profile" line.** Rejected with evidence: the real line is a *fat multi-fact narration* (module deltas, version bumps, $0-vs-rescrape), not the one-liner the v0 example faked; absorbing only the toy version leaves the duplication intact **and** hides the note from its human reader in `profile.md`. Nets zero simplification — dropped; **do not touch SCHEMA 2.4.**
- **Structural choices Brian set:** per-company (not a global log) — agents working one company stay in its folder; one file per run (not a rolling append-log) — both assembled on demand by a trivial later script.

---

## Hand-off

**Build:** (1) the writer helper + `started_at` stamp wired into the three skills; (2) the `fc.py --verb` manifest tag for `runcost.py` (independent, ship first); (3) the contract doc, shipped at [`modules/RUNS.md`](../modules/RUNS.md); (4) a small `tests/` file over the scenario battery. **Defer:** the `runs/*.json` aggregator (trivial later), any linter, any skip/crash records. **Gate:** the [`MAINTAINING.md`](../MAINTAINING.md) change-map needs a row for the run-record envelope; run the standard gate (`ruff`, `pytest`) after.
