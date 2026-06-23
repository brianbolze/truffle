---
date: YYYY-MM-DD
proposed: <M>      # lessons proposed or advanced this pass
left: <K>          # observations deliberately left unconsolidated
---

**Pass summary.** One line: what this pass did, including how many you read (that count is derivable from the folder — keep it in prose, not frontmatter). (e.g. "Read 41 observations, proposed 1 lesson from a 3-sighting cluster, left 38 unconsolidated — singletons or no shared shape.")

**Proposed / advanced.**
- `<lesson-id>` — <one line: the pattern> · from <obs-file>, <obs-file>, … → see lessons.md
  - test 1 (stated generally): <the rule, no run/company named> · test 2 (replaces): <what existing thing it corrects, or "nothing → don't add">
  - gate: <which of the four triggers earned it>

Every proposed lesson MUST carry the two self-tests above — a proposal that can't state itself run-free, or can't name what it replaces, isn't ready. (L001 in lessons.md models the shape.)

**Deliberately left unconsolidated.** The divergent record I chose *not* to act on, and why. This is the honest half — the part the failed system never wrote.
- <obs-file> — <why left: singleton, no shared shape, too thin, watching for a 2nd sighting, …>
- <obs-file> — <why>

**Anti-Merge attestation.** Confirm: no observation was edited, merged, summarized, or deleted this pass. Compression happened only by *adding* lessons that point at observations.

<!--
HOW TO USE THIS FILE — read before running a review pass.

WHAT A REVIEW PASS IS: the out-of-band consolidation step. It reads ALL observations, clusters repeats,
and PROPOSES lessons. It never edits a live skill and never decides a fix at capture time. You run it as
a skill (later, trivially, a scheduled routine). v0 trigger: ≥5 observations since the last review.

FILENAME: reviews/YYYY-MM-DD-pass.md (one note per pass). Copy this file; never write into _TEMPLATE.md.

WHAT THE PASS MAY AND MAY NOT DO:
  MAY  — read across all observations; cluster by shape; draft/advance a lesson in lessons.md (state: proposed);
         stamp `graduated-into: <lesson-id>` only on observations whose lesson actually graduates this pass (e.g. a brian-correction); a lesson left `proposed` lists its observations on its row, unstamped (the ONE permitted touch);
         assign each surfaced cluster its subject (about-Truffle | about-Agentic-Build) and route it.
  MUST NOT — edit, merge, summarize, reorder, or delete any observation (the Anti-Merge Law);
             promote a lesson itself (that's Brian's gate); collapse two distinct shapes into one mushy cluster.

THE "left" COUNT IS NOT OPTIONAL. Most observations should sit unconsolidated most passes — singletons and
divergent one-offs are the asset, not backlog to clear. A pass that consolidates everything is the failure
mode (345→2) in the other direction. Naming what you left, and why, is what makes over-compression auditable.

ROUTING (decided here, not at capture):
  about-Truffle        → the lesson enters Agentic Build's workflow (frame → proposal → review → implement → verify).
                         The learning system feeds the queue; Agentic Build changes Truffle.
  about-Agentic-Build  → a light internal edit to its own skills/docs, second look from a separate sub-agent. No change-packet.
Record the subject + destination in the lesson row, not the observation.
-->
