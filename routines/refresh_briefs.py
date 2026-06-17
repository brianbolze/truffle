#!/usr/bin/env python3
"""refresh_briefs — Truffle's first unattended routine (automation-frame L1: derived maintenance).

Regenerates every HTML brief + the corpus index from the markdown store into _out/briefs/. Spends no
Firecrawl credits and never writes store/ — pure derived output, safe to run anytime. The markdown
store stays the source of truth; the briefs are a disposable lens.

Why Python, not a shell wrapper: macOS won't let a launchd agent *execute a script file* that lives in
the iCloud-synced repo (EPERM), but a launchd-run interpreter may *read* an iCloud file as its program
and then freely read/write iCloud data. So the brain stays here, version-controlled; the OS clock (the
plist) only points Python at this file. Verified 2026-06-17 — see routines/README.md.

Run by hand exactly as the timer does:  python3 routines/refresh_briefs.py
Schedule: routines/com.truffle.refresh-briefs.plist  ·  Frame: _design/2026-06-17-automation-frame.md
"""

from __future__ import annotations

import os
import subprocess
import sys
import time
from datetime import datetime, timezone

# Self-locating: routines/ -> repo root, so a repo move can't break the paths (review finding P2).
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(REPO, "_out", "routines")
LOG = os.path.join(LOG_DIR, "refresh-briefs.log")   # the receipt: one line per run — glance here
OUT = os.path.join(LOG_DIR, "refresh-briefs.out")   # full render output, last run only (overwritten)
BRIEFS = os.path.join(REPO, "_out", "briefs")
TIMEOUT_S = 600   # unattended hard stop — satisfies the frame's "Bounded: a stop condition"


def main() -> None:
    os.makedirs(LOG_DIR, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    start = time.monotonic()

    # --no-fetch keeps the unattended run hermetic: local/cached assets + fallbacks, no network to hang
    # on (review finding P1). A human prepping a live demo can render *with* fetch to pre-warm new logos.
    cmd = [sys.executable, os.path.join(REPO, "scripts", "render.py"), "--all", "--index", "--no-fetch"]
    with open(OUT, "w", encoding="utf-8") as out:
        try:
            status = subprocess.run(
                cmd, cwd=REPO, stdout=out, stderr=subprocess.STDOUT, timeout=TIMEOUT_S
            ).returncode
            note = "" if status == 0 else f"exit={status}"
        except subprocess.TimeoutExpired:
            status, note = 124, f"timeout>{TIMEOUT_S}s"

    secs = round(time.monotonic() - start)
    n = len([f for f in os.listdir(BRIEFS) if f.endswith(".html")]) if os.path.isdir(BRIEFS) else 0
    if status == 0:
        line = f"{ts}  ok    {n} files  {secs}s"
    else:
        line = f"{ts}  FAIL  {note}  {secs}s  (see refresh-briefs.out)"
    with open(LOG, "a", encoding="utf-8") as log:
        log.write(line + "\n")
    sys.exit(status)


if __name__ == "__main__":
    main()
