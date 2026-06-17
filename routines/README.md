# routines/ — unattended chores

Small scheduled chores that tend the store without anyone asking. Frame (what's allowed, the risk
gradient): [`_design/2026-06-17-automation-frame.md`](../_design/2026-06-17-automation-frame.md).

**The shape (deliberately tiny):** a dumb OS timer (`launchd`) starts an in-repo routine; the routine
runs an existing verb and appends a one-line **receipt**. No framework, no registry, no config — that
gets extracted only once 2–3 routines exist and show what actually repeats.

**The iCloud gotcha (load-bearing).** This repo lives in iCloud Drive. macOS blocks a launchd agent
from *executing a script file* inside iCloud (EPERM, exit 126) — but lets a launchd-run **interpreter**
read an iCloud file as its program and then read/write iCloud data freely (verified 2026-06-17). So
routines are **in-repo Python** (the brain stays version-controlled), and the plist points the
non-iCloud `python` at them. A shell wrapper in the repo would *not* run under launchd.

## Routines

| Routine | Risk | Spends? | Mutates store? | Schedule |
|---|---|---|---|---|
| `refresh_briefs.py` | L1 derived | no | no | daily 06:00 |

### refresh-briefs

Regenerates every HTML brief + the corpus index (`render.py --all --index --no-fetch`) into
`_out/briefs/`. Runs hermetic (`--no-fetch`: local/cached assets, no network to hang on) under a 600s
hard stop. The markdown store stays the source of truth; the briefs are a disposable lens.

- **Receipt:** `_out/routines/refresh-briefs.log` — one line per run (`ok` / `FAIL`). Glance here.
- **Last run's full output:** `_out/routines/refresh-briefs.out`.

**Run by hand** (identical to what the timer does):
```bash
python3 routines/refresh_briefs.py
```

**Install / start the timer:**
```bash
cp routines/com.truffle.refresh-briefs.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.truffle.refresh-briefs.plist
```

**Trigger once now (test):**
```bash
launchctl start com.truffle.refresh-briefs
```

**Retime:** edit `Hour`/`Minute` in the plist, re-`cp` it, then `launchctl unload` + `load`.

**Uninstall (fully reversible):**
```bash
launchctl unload ~/Library/LaunchAgents/com.truffle.refresh-briefs.plist
rm ~/Library/LaunchAgents/com.truffle.refresh-briefs.plist
```
