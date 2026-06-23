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
- **gate:** one miss severe enough to justify a guardrail (a clear, silent count-inflation bug — needn't recur).
- **rule (test 1 — stated generally):** A category-membership count must read the structured frontmatter tag, never grep the whole profile body. A body mention is not membership; counting it silently inflates the cohort and the over-count looks clean.
- **replaces (test 2):** the current whole-file grep in the cohort census recipe — not additive; it corrects an existing recipe.
- **graduation:** pending Brian → then a `/query-companies` recipe fix via agentic-build process (frame → proposal → implement → verify). Link the `changes/` path here when it lands.
