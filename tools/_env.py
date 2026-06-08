#!/usr/bin/env python3
"""Shared key loader for the tools/ library — the one thing all the capture tools share.

Every tool resolves its API key the same way: environment first, then a `KEY=value` line in the
repo-root `.env` (gitignored). Centralised here so the strategy can't drift per-tool — the failure
mode this replaces is one tool quietly learning a second key source (a settings.json fallback, say)
while the others don't, until auth is per-tool folklore. Stdlib-only — no python-dotenv.

A local import: tools do `from _env import load_key`. Python puts a script's own directory on
sys.path[0], so `python3 tools/<name>.py` resolves this from any cwd — the bare-shell-run property
holds, no package install needed.
"""

from __future__ import annotations

import os
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]  # tools/_env.py -> repo root


def load_key(var_name: str) -> str:
    """The API key `var_name`: environment first, else its `KEY=value` line in the repo-root `.env`.

    Fails loud if absent anywhere — a missing key is a setup error, not a capture that should limp on.
    """
    key = os.environ.get(var_name)
    if key:
        return key
    env = _REPO_ROOT / ".env"
    if env.exists():
        with open(env, encoding="utf-8") as f:
            for raw in f:
                line = raw.strip()
                if line.startswith(f"{var_name}="):
                    return line.split("=", 1)[1].strip().strip('"').strip("'")
    raise RuntimeError(f"Missing {var_name} — set it in the environment or in {env}")
