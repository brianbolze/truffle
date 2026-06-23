---
date: 2026-06-23
run: changes/2026-06-23-query-companies-cohort-cut (illustrative)
kind: risk-miss
consumed-by: L001
---

**Saw.** While working the cohort-cut packet, `henrymeds` showed up in the GLP-1 cohort census — but its `offerings.md` frontmatter has no GLP-1 tag; it only mentions "GLP-1" once in body prose (a competitor reference). The census count came back looking clean, with no flag that a non-member had been folded in. The headline cohort size is bigger than the set of actual GLP-1 companies, and nobody downstream can see the gap.

**Not claiming.** Not claiming a fix here, and not claiming this is a general problem across all recipes — one sighting, on the cohort census recipe specifically. What's causing the over-count, and whether it generalizes, is the review pass's call.
