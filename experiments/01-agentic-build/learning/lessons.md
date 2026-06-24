# Lessons

Reviewed, decided patterns — the curated short list. A lesson is the *distilled rule*; the raw sightings stay in `observations/` and are linked, never copied. Brian-taste corrections live in `brian.md`, not here.

## How a lesson works

**One lesson = one `## <id>` block.** Add a lesson by *appending* it — never by shrinking or merging observations (the Anti-Merge Law). Edit a lesson freely; it's the curated view. Retire it by flipping `state`, never by deleting the row.

**States:** `proposed → accepted → graduated` (or `parked` / `dropped`). A row never silently disappears — `dropped` and `parked` rows stay, because they record a decision.

- **proposed** — a review pass surfaced it. Not yet a rule. Awaiting Brian.
- **accepted** — Brian approved it. Ready to sharpen the skill/recipe/convention it improves.
- **graduated** — the lesson now lives in the thing it improves (recipe, skill, doc, or a landed change). Link the diff/packet. Done.
- **parked** — real, but waiting (e.g. for a 2nd sighting, or on a dependency).
- **dropped** — decided not worth it. Keep the row; it stops the same idea recurring.

Source observations are stamped `graduated-into` **only when the lesson graduates** — a `proposed` lesson just lists them on its row, so a parked or dropped lesson leaves its observations unstamped and available for a later pass.

**Graduation heuristics — a lesson earns graduation on one of these:**
- the same thing in ≥2 independent runs, or
- a Brian correction, or
- an independent review catch, or
- one miss severe enough that a single occurrence justifies a guardrail. **Reserve this path** for a `risk-miss` or a silent-wrong data defect — not for general friction, which waits for a 2nd sighting. It bypasses the cross-run check, so it's the easiest to abuse.

**Two self-tests — a lesson must pass both before it graduates:**
1. **State it without naming a specific run or company.** If you can't say it generally, it isn't a rule yet — it's an observation.
2. **What does it replace?** If it adds without replacing anything, default to *not* adding it.

**Subject + routing** (assigned at review): `about-Truffle` → enters Agentic Build's workflow (a change-packet changes Truffle). `about-Agentic-Build` → a light internal edit, second look, no packet.

**Retiring** isn't silent: when a graduated lesson proves wrong, challenge it at the skill (revert the diff), flip this row to `dropped`, and log a *fresh* observation saying so. The trail stays intact.

---

## L001 — Cohort census must count from frontmatter, not a whole-file grep
- **state:** proposed (2026-06-23, review pass)
- **subject:** about-Truffle → Agentic Build workflow
- **observations:** [2026-06-23-cohort-count-grep-inflation-7f3a](observations/2026-06-23-cohort-count-grep-inflation-7f3a.md)
- **gate:** one miss severe enough to justify a guardrail — a silent count-inflation defect (`risk-miss`); the reserved single-sighting path, used here because it qualifies, not a license to graduate singletons generally.
- **note:** seed / bootstrap example — illustrative, not the routine pattern.
- **rule (test 1 — stated generally):** A category-membership count must read the structured frontmatter tag, never grep the whole profile body. A body mention is not membership; counting it silently inflates the cohort and the over-count looks clean.
- **replaces (test 2):** the current whole-file grep in the cohort census recipe — not additive; it corrects an existing recipe.
- **graduation:** pending Brian → then a `/query-companies` recipe fix via agentic-build process (frame → proposal → implement → verify). Link the `changes/` path here when it lands.

---

## L002 — Problem-space artifacts must exclude solutions by structure, not by instruction
- **state:** proposed (2026-06-23, first full review pass)
- **subject:** about-Agentic-Build → light internal edit (frame skill + run/retro-report convention), no change-packet
- **observations:** [2026-06-23-frame-doc-drifted-into-solutions-3777](observations/2026-06-23-frame-doc-drifted-into-solutions-3777.md), [2026-06-20-runs-propose-solution-not-friction-8aa6](observations/2026-06-20-runs-propose-solution-not-friction-8aa6.md)
- **gate:** the same shape in ≥2 independent runs — a frame doc leaked solution opinions, and the Market Read Lab run outputs drifted from reporting friction to proposing solution shapes. Each was caught by an independent review/Brian, not by the author.
- **rule (test 1 — stated generally):** An artifact whose job is to capture problem-space — a frame, a run/retro report — must be kept solution-free by *structure*, not by instruction. A reminder ("leave solutions out") demonstrably doesn't hold: the drift to prescribing fixes recurs even after an explicit instruction. The working countermeasure already exists in this repo — the observation template has *no slot for a fix* — so the move is to generalize that structural guard to the other problem-space artifacts.
- **replaces (test 2):** corrects the frame skill + run-report convention (which today lean on instruction/taste to stay solution-free) by giving them the same no-fix structure observations already use — it sharpens an existing convention rather than adding a free-standing rule.
- **graduation:** pending Brian → then a light edit to the frame skill + the MRL run-report convention. Link the edit here when it lands.
