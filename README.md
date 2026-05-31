# web-research

A project-agnostic company-research engine: Firecrawl for capture, Claude Max for reasoning, a shared file-first store any project can read and any agent can query.

> **Start here:** [`_design/2026-05-29-frame.md`](_design/2026-05-29-frame.md) — the Frame (goal, scope, principles, non-goals). Everything else serves that doc.

## Layout

```
SCHEMA.md TAXONOMIES.md   # the store contract — what a capture writes
QUERYING.md               # how to read the store back — consumer recipes
BACKLOG.md                # system-level weaknesses / ideas (capped, tagged, curated)
_design/      # frame / vision docs (source of truth for intent)
_archive/     # superseded docs
experiments/  # throwaway probes to de-risk decisions before building
scripts/      # engine utilities (querycheck.py — QUERYING.md drift self-test)
skills/       # the capture verb — research-company/ (SKILL.md + fc.py workhorse), global via ~/.claude/skills
store/        # the shared company store (store/<domain-slug>/) — created as captures land
```

*Status: prototyping. Name: `web-research`.*
