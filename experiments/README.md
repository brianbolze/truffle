# experiments

Throwaway probes to de-risk a decision **before** committing it to the engine. Each subfolder is dated + named. Not production; not load-bearing. The output that matters is a `FINDINGS.md` that feeds the Frame or the eventual design.

- One folder per experiment: `<YYYY-MM-DD>-<slug>/`
- Standard files: `README.md` (hypothesis + method), the probe (script / recipe), `FINDINGS.md` (what we learned).
- Bulk dumps go in `_out/` (gitignored). Keep READMEs, scripts, and FINDINGS in git.

## Log

- [`2026-05-29-query-affordance/`](2026-05-29-query-affordance/) — does a thin query affordance beat grep-from-scratch for cross-brand questions? (rung 2 of the Frame's queryability ladder)
- [`2026-05-30-first-capture/`](2026-05-30-first-capture/) — first end-to-end capture (linear.app): does the lifecycle hold and the SCHEMA fit a clean B2B SaaS?
- [`2026-05-30-breadth/`](2026-05-30-breadth/) — a DTC consumer-health brand (AG1): does the fed-in playbook cut waste, and does the SCHEMA hold for a multi-SKU catalog?
- [`2026-05-30-shapes/`](2026-05-30-shapes/) — Nike / AWS / Benadryl: three awkward shapes that surfaced the `parent`/`owns` relation gap + classification gaps.
- [`2026-05-30-telehealth-cohort/`](2026-05-30-telehealth-cohort/) — six telehealth brands: does an apples-to-apples cohort classify identically? (the cross-company query proof)
- [`2026-05-31-consumption/`](2026-05-31-consumption/) — cold-consumer query battery against the store: do the formats actually answer, and what's the rung-2 recommendation?
- [`2026-05-31-query-design/`](2026-05-31-query-design/) — probe the clean corpus to design `QUERYING.md` from real data.
