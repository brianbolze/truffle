---
date: 2026-06-17
run: session/6b01df38-5cbf-437f-8d92-cc6cc38bd09b (mined 2026-06-23)
kind: risk-miss
---

**Saw.** I built and hand-verified a refresh-briefs routine, and it passed. A /review-change sweep afterward flagged that the wrapper has no timeout while render.py fetches logos/fonts for ~130 companies — a slow or hung host could stall the unattended run indefinitely. The successful hand-run had hidden a failure mode that only bites when nobody's watching.

**Not claiming.** Not claiming a timeout is the fix or that review must precede hand-runs — one sighting of a hand-run masking an unattended hang.
