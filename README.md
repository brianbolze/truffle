# web-research

A project-agnostic company-research engine: Firecrawl for capture, Claude Max for reasoning, a shared file-first store any project can read and any agent can query.

> **Start here:** [`_design/2026-05-29-frame.md`](_design/2026-05-29-frame.md) — the Frame (goal, scope, principles, non-goals). Everything else serves that doc.

## Layout

```
_design/      # frame / vision docs (source of truth for intent)
_archive/     # superseded docs
experiments/  # throwaway probes to de-risk decisions before building
store/        # the shared company store (store/<domain-slug>/) — created as captures land
```

*Status: prototyping. Not yet a git repo / no remote (pending). Working name: `web-research`.*
