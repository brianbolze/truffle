"""present — the engine's human-facing lens: store records in, self-contained HTML out.

Why a package: the brief, the comparison sheet, and the index are three views over one
extraction, and each concern needs exactly one home — model.py reads the store, assets.py
fetches and caches, md.py translates dossier markdown, theme.py + css/ own the chrome, and
one module per view does layout. Views never import each other. Frame + approach:
_design/2026-06-12-presentation-layer.md.
"""

from __future__ import annotations

import os
import sys

SCRIPTS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if SCRIPTS not in sys.path:  # sibling engine modules (store.py, offeringscheck.py) resolve from anywhere
    sys.path.insert(0, SCRIPTS)

ROOT = os.environ.get("WEB_RESEARCH_HOME") or os.path.dirname(SCRIPTS)
OUT = os.path.join(ROOT, "_out", "briefs")  # the repo's one derived-artifacts root — never store/
