---
date: 2026-06-26
run: changes/2026-06-26-source-page-tool
kind: brian-correction
---

**Saw.** I built `tools/_firecrawl.py` — a shared Firecrawl `/v2/scrape` caller — and shipped it, ran
the gate, and summarized, all without reading the repo's canonical Firecrawl knowledge:
`skills/research-company/firecrawl-capture.md` (the hazards/params/cost playbook) and `fc.py`'s
existing `post()` caller. Brian had to ask "Did you ever read those? Probably worth it." Only then did
I find the `metadata.creditsUsed` billing guidance, confirm my recipe knobs, and learn `fc.py` is a
deliberately-separate third caller. Afterward Brian said: "I wish you had looked for / read those
automatically." The pointers were already in CLAUDE.md and `.claude/rules/engine-dev.md` under "Prior
art — mine it, don't reinvent it," which names firecrawl-capture.md explicitly.

**Not claiming.** Not claiming the helper came out wrong (the recipe was already compliant) or
prescribing a checklist — the correction is that I reached for code before mining named, in-repo prior
art for a surface that had a canonical doc, and only consulted it when prompted. The urge I'm
resisting: writing a "always grep skills/ before building" rule from one sighting.
