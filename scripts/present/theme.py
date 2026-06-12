"""theme — the one home for the engine's chrome: design tokens + per-view stylesheets.

Why: three views must dress alike without copying each other's CSS. Tokens live here as
Python constants because palette math consumes them; the CSS itself lives in css/*.css as
real files (editor-grade, diffable), inlined at render time so the output stays one
self-contained AirDrop-able file. No build step — open(), f-string, done.
"""

from __future__ import annotations

import os

PAPER = "#F5F1E8"
INK = "#1B1813"

_CSS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "css")


def css(view: str) -> str:
    """The stylesheet for a view, read fresh each render — a CSS edit shows on the next run."""
    with open(os.path.join(_CSS_DIR, f"{view}.css"), encoding="utf-8") as f:
        return f.read()


# The one icon the views need (lucide arrow-up-right) — a full icon module isn't earned.
ARROW_SVG = ('<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
             'stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" '
             'aria-hidden="true"><path d="M7 7h10v10M7 17L17 7"/></svg>')


