---
paths:
  - "**/*.py"
---
# Python house style

Applies to the **durable** surface — `scripts/`, `skills/`. Code under `experiments/<date>-*/` is throwaway de-risking probes (see [engine-dev.md](.claude/rules/engine-dev.md)) and is **exempt**: don't retro-type or restyle frozen probes.

Tooling is [`ruff.toml`](ruff.toml): `ruff check` (lint, `--fix` to autofix) + `ruff format`. Ruff replaces flake8.

## Rules

- **Type hints are required** on every function — args and return.
- **Python 3.9 interpreter**, so start each file with `from __future__ import annotations`. That lets you write modern `str | None` / `dict[str, Any]` annotations without a runtime cost — no `typing.Optional`/`Dict` imports.
- **Read files with `with open(...)`** (never a bare `open(p).read()` that leaks the handle to GC), and always pass `encoding="utf-8"` on text reads.
- **No single-letter public parameters.** `resolve(query, profiles)`, not `resolve(query, P)`. Short locals (`p`, `fm`) are fine inside a tight scope.
- **Keep the why-first docstrings.** Every module and non-trivial function says *why* it exists, not just what it does — this is the codebase's signature, preserve it.
- **CLI scripts guard execution**: a `main()` plus `if __name__ == "__main__":`, never logic at import time (so the module stays importable + testable). The `DISPATCH = {cmd: fn}` pattern is the house idiom.
- **Stdlib-first.** PyYAML is the only pip dependency in the core engine; `fc.py` is stdlib-only on purpose. Earn any new dep. **One quarantined exception:** `scripts/shoot.py` (Tier-B visual capture) imports `playwright` and drives system Chrome — opt-in, never imported by a core script. Recipe-time CLI tools (`sips`, `magick`, `rsvg-convert`) aren't pip deps: shell out to them, never add a Python image dep.
