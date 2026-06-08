# web-research

A project-agnostic company-research engine: Firecrawl for company-site capture, shared source-signal tools for repeatable external evidence, Claude Max for reasoning, and a file-first store any project can read.

> **Start here:** [`_design/2026-05-29-frame.md`](_design/2026-05-29-frame.md) — the Frame (goal, scope, principles, non-goals). Everything else serves that doc.

## Layout

```
SCHEMA.md TAXONOMIES.md   # the store contract — what a capture writes
QUERYING.md               # how to read the store back — consumer recipes
OFFERINGS.md TELEHEALTH.md  # opt-in module contracts — per-SKU offerings.md (depth module) + the telehealth.md cohort pack; top-level for now (see SCHEMA → Tier-1 modules)
BACKLOG.md                # system-level weaknesses / ideas (capped, tagged, curated)
_design/      # frame / vision docs (source of truth for intent)
_archive/     # superseded docs
experiments/  # throwaway probes to de-risk decisions before building
scripts/      # engine utilities (querycheck.py — QUERYING.md drift self-test; store.py — resolve()/relations(); offeringscheck.py + cohortcheck.py — module-contract linters; build_db.py — derived SQLite lens for telehealth cohort aggregation, --check-guarded)
tools/        # reusable source-signal capture utilities + small consumers (SERP, Wayback, Trustpilot, Trends, Exa; no project judgment)
skills/       # capture verbs — research-company/ (SKILL.md + firecrawl-capture playbook + scripts/fc.py workhorse) + deepen-offerings/ (thin offerings-comprehensiveness preset of it); global via ~/.claude/skills
store/        # the shared company store (store/<domain-slug>/) — created as captures land
```
