---
date: 2026-06-24
run: changes/2026-06-22-signal-delta-sec-edgar
kind: friction
---

**Saw.** I was asked to run `agent-build-review` in `proposal` mode on `proposal.md`, but the file was `Status: implemented` with a full Implementation Receipt and verification log already in it. The skill and reviewer-context define `proposal` and `change` as distinct modes (review the decision vs. review the build against the accepted proposal), but neither says what a `proposal`-mode review *is* once the packet has already shipped — so I had to decide on my own to keep judging the decision-soundness and explicitly not slide into diff-verification, and to flag the lifecycle position as a finding. The single-file packet (only `proposal.md`, no separate frame/diff/decision-surface) compounded it: the proposal carries its own "Review Notes" and receipt, so "what am I independent of?" was ambiguous.

**Not claiming.** Not claiming the mode model is wrong or that a "post-hoc proposal review" mode is needed — one sighting, on one packet that happens to fold decision + receipt into a single doc. The pressure I felt was to invent a rule for "review requested after implementation"; I'm recording the urge, not the patch.
