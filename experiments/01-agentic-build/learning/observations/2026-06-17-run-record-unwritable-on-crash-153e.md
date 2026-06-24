---
date: 2026-06-17
run: session/de724c08-734a-4f9e-a5b2-d92a39bfce56 (mined 2026-06-23)
kind: risk-miss
---

**Saw.** An adversarial panel reviewing the proposed run-record contract found that two of its richest fields — a failed/aborted status and a crash-written record — are things the writing agent provably can't emit when it dies. The contract was shaped around the success path, so the fields that matter most in a failure would always be absent. The Codex v0 and my own read had both missed it.

**Not claiming.** Not claiming a watchdog or exit-hook — one sighting of a success-only contract design.
