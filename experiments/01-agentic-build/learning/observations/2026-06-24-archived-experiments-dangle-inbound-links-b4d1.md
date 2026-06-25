---
date: 2026-06-24
run: work-menu coverage pass + agent-build-propose neighbor-discovery (2026-06-24)
kind: friction
---

**Saw.** Two experiments were moved to `experiments/_archive/` but their inbound links were left pointing at the old live paths, so a reader grounding a decision follows a dead path: `BACKLOG.md:40` and `tools/exa_search.py:15` both link `experiments/2026-06-20-cohort-discovery/…` (now under `_archive/`), and `BACKLOG.md:43` links `experiments/2026-06-13-adaptive-capture-depth-frame/FRAME.md` (also archived). Verified by `ls` on both the live and `_archive/` paths. n=2 distinct archived dirs, 3 dangling links across BACKLOG + a tool docstring — surfaced incidentally while grounding the neighbor-discovery proposal and re-checking a work-menu gate flag.

**Not claiming.** Not claiming archiving is wrong or that a link-checker should be built — only that archiving an experiment currently has no step that fixes (or redirects) its inbound references, so live-path links rot silently. Whether the fix is a convention, a drift-sweep check, or just spot edits is for the review pass to decide.
