# Can CoWork consume the store? — desk probe

*2026-06-10. **Desk research only** — docs + issue tracker via a claude-code-guide agent; no live CoWork session was probed. Trigger: Brian ran company-query prompts in CoWork with global instructions pointing at `$WEB_RESEARCH_HOME`; CoWork couldn't find the tools.*

## Question

Can `/query-companies` (and the store generally) be consumed from Claude CoWork, and what would it take?

## Findings (doc-confirmed, not locally reproduced)

1. **No shell env.** CoWork sessions run in an isolated Linux VM and never source the shell profile — `$WEB_RESEARCH_HOME` doesn't exist there. *Fixed engine-side regardless of CoWork:* the skill now falls back to the canonical store path (commit `777e382`). [env-vars doc](https://code.claude.com/docs/en/env-vars)
2. **Skill registry is unreliable.** CoWork keeps an internal skill registry and does not dependably scan `~/.claude/skills/` — personal skills can be silently absent ([#50669](https://github.com/anthropics/claude-code/issues/50669)). This, not the instructions, is why the verb was invisible. The supported packaging is a **plugin** (manifest + `skills/`). [plugins doc](https://code.claude.com/docs/en/plugins)
3. **The blocker: iCloud Drive + the VM.** With Optimize Mac Storage, iCloud replaces files with 0-byte stubs the Linux VM can't hydrate — documented data loss ([#32637](https://github.com/anthropics/claude-code/issues/32637)). The store *lives on iCloud Drive*: a CoWork agent over a stubbed store would emit confident silent false-negatives ("X not in store", empty profiles) — the exact failure class the 2026-06 trust-surface work eliminated. Writes are out of the question.

## Decision

**Hold.** Claude Code is the verified consume surface (implicit routing passed in-repo hit/miss + cross-project, 2026-06-09/10); briefs are self-contained HTML and need no harness. CoWork adds three fragile layers for no current consumer need.

## The live probe to run before reopening this

Grant the Web Research folder to a CoWork session; run `ls -la store/*/profile.md` and read one profile end-to-end. Zero-byte stubs → store location decision comes first. Clean → package read-only `/query-companies` as a minimal plugin (`create-cowork-plugin` skill exists) and re-probe routing. Tracked in BACKLOG → Presentation surface.
