# experiments

Throwaway probes to de-risk a decision **before** committing it to the engine. Each subfolder is dated + named. Not production; not load-bearing. The output that matters is a `FINDINGS.md` that feeds the Frame or the eventual design.

- One folder per experiment: `<YYYY-MM-DD>-<slug>/`
- Standard files: `README.md` (hypothesis + method), the probe (script / recipe), `FINDINGS.md` (what we learned).
- Bulk dumps go in `_out/` (gitignored). Keep READMEs, scripts, and FINDINGS in git.

## Log

- [`2026-05-29-query-affordance/`](2026-05-29-query-affordance/) — does a thin query affordance beat grep-from-scratch for cross-brand questions? (rung 2 of the Frame's queryability ladder)
