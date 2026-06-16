# web-research

A project-agnostic company-research engine: Firecrawl for company-site capture, shared source-signal tools for repeatable external evidence, Claude Max for reasoning, and a file-first store any project can read.

> **Start here:** [`_design/2026-05-29-frame.md`](_design/2026-05-29-frame.md) — the Frame (goal, scope, principles, non-goals). Everything else serves that doc.

## Layout

```
SCHEMA.md TAXONOMIES.md   # the store contract — what a capture writes
QUERYING.md               # how to read the store back — consumer recipes
SIGNALS.md                # the traction Signals layer — front door (capture → persist → diff, run commands, sources)
modules/OFFERINGS.md modules/VISUAL.md   # opt-in module contracts — offerings.md (per-SKU depth) + visual.md (blind brand-evidence)
TELEHEALTH.md             # the telehealth cohort pack — at root for now (see SCHEMA → Tier-1 modules)
BACKLOG.md                # system-level weaknesses / ideas (capped, tagged, curated)
_design/      # frame / vision docs (source of truth for intent)
_archive/     # superseded docs
experiments/  # throwaway probes to de-risk decisions before building
scripts/      # engine utilities (querycheck.py — QUERYING.md drift self-test; store.py — resolve()/relations(); signals.py — the Signals-store writer (capture = one-company front door, alias-aware; persist an envelope to signals/<source_type>/; run = batch capture, import = consolidate); offeringscheck.py + cohortcheck.py + visualcheck.py — module-contract linters; tile.py + shoot.py — visual-evidence capture tiers (cached-screenshot crop + Playwright browser re-render); build_db.py — corpus-wide SQLite lens with cohort-gated views, --check-guarded; render.py + compare.py — CLIs over the present/ package, the human-facing lens: briefs, comparison sheets, corpus index; runcost.py — read-only corpus cost roll-up: Firecrawl capture credits (from the per-call manifests) + signal-tool spend, cut by verb/slug/date — for routine budgeting)
tools/        # reusable source-signal capture + a comparator (SERP, Wayback, Trustpilot, Trends, Exa, SEC EDGAR); signal_delta.py diffs two captures of the same source into axis-specific deltas; no project judgment
skills/       # company verbs — query-companies/ (read-only store router), research-company/ (capture + Firecrawl playbook), deepen-offerings/ (offerings-comprehensiveness preset), visual-evidence/ (blind brand-evidence, post-capture); global via ~/.claude/skills and ~/.agents/skills
store/        # the shared company store (store/<domain-slug>/) — profile.md + module docs, plus signals/<source_type>/<captured_at>.json (append-only external captures)
```
