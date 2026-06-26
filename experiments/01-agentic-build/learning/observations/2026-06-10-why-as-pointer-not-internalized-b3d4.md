---
date: 2026-06-10
run: session:6d795869 (mined 2026-06-25)
kind: brian-correction
---

**Saw.** Drafting a sub-agent prompt, the agent supplied a goal + `<data>` + `<approach>` but no "why" — it had offloaded the motivation to a referenced doc instead of stating it. Brian caught it: "Ok. Is there a reason you didn't have any why / context in this prompt?" Seen again in c8076a6d the same day. The agent treated *a pointer to* context ("read X for the why") as equivalent to the context being held in the brief.

**Not claiming.** Not claiming every prompt needs a long why section — only that a link to the motivation is not the same as the motivation being internalized where the work happens.
