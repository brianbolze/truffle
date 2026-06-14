# web-research

A project-agnostic company-research engine: Firecrawl for company-site capture, shared source-signal tools for repeatable external evidence, Claude Max for reasoning, and a file-first store any project can read.

> **Start here:** [`_design/2026-05-29-frame.md`](_design/2026-05-29-frame.md) — the Frame (goal, scope, principles, non-goals). Everything else serves that doc.

## Layout

```
SCHEMA.md TAXONOMIES.md   # the store contract — what a capture writes
QUERYING.md               # how to read the store back — consumer recipes
modules/OFFERINGS.md VISUAL.md  TELEHEALTH.md  # opt-in module contracts in modules/ — offerings.md (per-SKU depth) + visual.md (blind brand-evidence); TELEHEALTH.md cohort pack at root (see SCHEMA → Tier-1 modules)
BACKLOG.md                # system-level weaknesses / ideas (capped, tagged, curated)
_design/      # frame / vision docs (source of truth for intent)
_archive/     # superseded docs
experiments/  # throwaway probes to de-risk decisions before building
scripts/      # engine utilities (querycheck.py — QUERYING.md drift self-test; store.py — resolve()/relations(); offeringscheck.py + cohortcheck.py + visualcheck.py — module-contract linters; tile.py + shoot.py — visual-evidence capture tiers (cached-screenshot crop + Playwright browser re-render); build_db.py — corpus-wide SQLite lens with cohort-gated views, --check-guarded; render.py + compare.py — CLIs over the present/ package, the human-facing lens: briefs, comparison sheets, corpus index)
tools/        # reusable source-signal capture utilities + small consumers (SERP, Wayback, Trustpilot, Trends, Exa; no project judgment)
skills/       # company verbs — query-companies/ (read-only store router), research-company/ (capture + Firecrawl playbook), deepen-offerings/ (offerings-comprehensiveness preset), visual-evidence/ (blind brand-evidence, post-capture); global via ~/.claude/skills and ~/.agents/skills
store/        # the shared company store (store/<domain-slug>/) — created as captures land
```
