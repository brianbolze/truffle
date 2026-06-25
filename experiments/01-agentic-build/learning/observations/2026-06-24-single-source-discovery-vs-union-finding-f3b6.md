---
date: 2026-06-24
run: agent-build packet 2026-06-24-neighbor-discovery (/discover-neighbors verb)
kind: friction
---

**Saw.** The verb's design bet on a single discovery feeder (Exa `/search`) — and the weakest one. The prior `2026-06-20-cohort-discovery` bake-off's load-bearing finding was the opposite: "no single technique is complete — **union earns its keep** (websearch + listicle ≈ most of the pool)," with websearch at 0.69 recall, listicle 0.34, and Exa `/findSimilar` failing to even run. A live test then confirmed the single-source weakness independently: exa missed the category-definers in two different cohorts (telehealth: hone/ro/hims; docs/PM: Linear/Asana/Monday/ClickUp…), while one mined listicle recovered nine of them at once. A discovery design anchored on one source is structurally under-powered regardless of which source it picks.

**Not claiming.** Not claiming the union recipe is finalized or that exa has no role (it does surface a real long tail) — only that choosing one feeder, when the available evidence already said "discovery is a union and this feeder is the laggard," was a design error visible before any build.
