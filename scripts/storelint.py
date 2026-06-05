#!/usr/bin/env python3
"""storelint — checks that hold on *any* authored store file, regardless of which module schema it follows.

The per-module linters (`offeringscheck`, `cohortcheck`) each enforce their own schema. But one failure is
schema-independent: an LLM-authored file can trail a leaked harness control tag (`</content>`, `</invoke>`)
— a generation artifact, not content. That bit four profiles in the first batch and silently shipped to four
more companies before this guard existed (Noom, 2026-06-04). It's a property of *how the file was written*, not
*what schema it follows*, so it lives here once and every per-module linter calls it — rather than re-deriving
(and drifting) the regex per script.

Scoped to **authored** files on purpose: a scraped capture page can legitimately contain a literal `</content>`
(an API doc, an XML tutorial), so this never runs over `captures/` — only the files an agent hand-writes
(`profile.md` / `<cohort>.md` / `offerings.md`). `fc.py` keeps its own mirror of `LEAK_RE` because it ships
self-contained with the `/research-company` skill across the repo boundary; keep the two in sync.

Stdlib-only (matches its callers). Importable lib — no CLI.
"""

from __future__ import annotations

import re

# Leaked harness control tags. Targeted to the tool-call vocabulary so legit URL-template placeholders
# (`<slug>`, `<sku>`, `<drug>`) don't false-positive. MIRROR of fc.py's LEAK_RE — change both together.
LEAK_RE = re.compile(r"</?\s*(?:antml:)?(?:function_calls|invoke|parameter|content)\b[^>]*>", re.I)


def leaked_tags(text: str) -> list[tuple[int, str]]:
    """Every leaked harness tag in `text` as `(line_number, matched_tag)` pairs — `[]` when clean."""
    return [(i, m.group(0)) for i, line in enumerate(text.splitlines(), 1) for m in LEAK_RE.finditer(line)]
