# Success criteria — visual-evidence module graduation

Date: 2026-06-14 · Status: ratified bar for the build (set with Brian). The gate the
module's first validation run must clear. Companion to [`FRAME.md`](FRAME.md) (why/scope)
and the proven pipeline in [`../2026-06-13-visual-quality-v5-capture-clean-blind-judgment/`](../2026-06-13-visual-quality-v5-capture-clean-blind-judgment/FINDINGS.md).

## Goal

A repeatable, **per-company** module that turns cached (or freshly re-rendered) screenshots
into **cited, blind, falsifiable visual-evidence cards + a ~5-second prose impression** — and
never a score.

## Success criteria — the graduation gate (validation must show all)

1. **Clean tiles in, or excluded.** The QA gate catches a contaminated page (modal /
   grey-hero / black-card / lazy-gap / mid-animation) and either Tier-B re-renders it to the
   approved quality bar, or it's excluded with a noted reason. No contaminated tile reaches a card.
2. **Blind by construction.** Miners + judge see only tiles + protocol — no dossier, profile,
   Notion, or live web; cards reason only from visible tells.
3. **Cards falsifiable + cited.** Each accepted card carries a valid active tile path, ≥1
   concrete visible tell, and one calibrated sentence; generic competence isn't flattered;
   duplicates are pruned. (Lint-checked.)
4. **The line holds.** No score, no frontmatter quality field, no decision gate.
   `visualcheck.py` **fails if a `score:` field appears anywhere** in `visual.md`.
5. **Consumable.** `store/<domain>/visual.md` leads with a cited *Visual & brand impression* a
   creative director reads in ~5s; the cards are the audit trail behind it.
6. **Cheap + repeatable.** Per company; zero Firecrawl on the cached path; own `captured_at`.
   Mirrors the offerings module shape (recipe + schema + destination, opt-in, own lint); the
   default `/research-company` capture is untouched.

## Validation quality bar (graded, not just binary)

- **Capture:** ≥1 contaminated page *proven* caught and remediated (or excluded) — demonstrated,
  not assumed.
- **Cards:** ≥2 strong + ≥2 poor usable cards per family that a reader can verify in the cited
  tile (the v5 pass bar).
- **Calibration:** the known traps handled — coherent-template ≠ strong; dark-gradient gloss ≠
  finish; distinctive ≠ executed.

## Explicitly out of scope (the parked line)

No autonomous quality score, no `1-5`/PQR-lite scale, no frontmatter quality field, no
score-gated downstream decision. The score stays an experiment track against frozen ground
truth (BACKLOG "Visual-quality SCORE — parked").
