---
date: 2026-06-24
run: changes/2026-06-22-signal-delta-sec-edgar
kind: surprise
---

**Saw.** The only independent review in the packet is `proposal-review.md`, run in `proposal` mode and dated 2026-06-24 — but the packet was already `Status: implemented` with a full Implementation Receipt before that review ran. So the "independent review" a medium-risk packet needs before build actually happened after the build, retrospectively, and the reviewer says so explicitly (finding #1). Its load-bearing carry-forward (event-key stability) is a `change`-mode question the `proposal`-mode review couldn't answer — I had to open the code myself to confirm `citation` is in the comparison key and that no fixture pins the re-parse case.

**Not claiming.** Not claiming the build was wrong or that the review was bad — the review flagged its own position in the lifecycle honestly. Just noting the review mode and the packet's stage were mismatched, which left a real correctness question unverified at the point I had to recommend on it.
