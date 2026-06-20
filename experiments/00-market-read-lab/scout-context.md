# Scout Context

**Status**: lightweight brief for autonomous Market Read Lab scouts.

## What This Is

Market Read Lab runs repeated market-read experiments before Truffle builds durable
category/cohort machinery.

Truffle is mostly company-keyed today: it can describe one company deeply, but real
market work often needs cross-company context, source panels, category boundaries,
relations, change signals, and non-company evidence. The lab answers useful market
questions now, then uses the run history to learn what Truffle should capture, persist,
defer, or explicitly not build.

Persist the **runs**, not the ontology.

## Scout's Job

Pick one plain market-read question that clears two tests:

1. **Value test:** is the answer, using Truffle's captured/cited ingredients,
   materially better than what someone could get from generic Claude + web search?
2. **Design test:** does the run reveal a real pressure point or gap in Truffle, or
   teach us how to approach a bigger design / roadmap item?

The run can pass the design test by showing that no new primitive is needed.
`query-time grouping is enough` is valid learning.

## Selection Process

Start with the market question, not triage closure.

Before selecting, build a quick history map from prior **selected** questions:

```bash
python3 .claude/skills/market-read-lab/scripts/question_history.py
```

Use that map, the value jobs, and the design uncertainties below to generate 5-10
candidates a real downstream reader would recognize. For each leading candidate, name:

- `value_job`: the Truffle job this serves.
- `value_test`: why Truffle should beat generic Claude + web search here.
- `design_test`: what pressure, gap, or roadmap question this run tests.
- `evidence_needed`: source ingredients required for a trustworthy answer.
- `evidence_mode`: `store-only | local-existing | bounded-live | live-external-needs-approval`.
- `false_confidence_trap`: how the read could overclaim.
- `repeat_reason`: `new | recurrence | calibration`, and why that matters.

After candidates exist, check `triage.md` and the last 3 completed `run-notes.md`
only to annotate design pressure, sharpen evidence requirements, catch recent
repeats, or reject candidates that merely execute a parked next step. A triage item
can explain why a candidate teaches something; it should not supply the candidate.

Prefer questions with real reader value and experimental value. Repeat a recent
question shape only when recurrence closes a design decision or tests a materially
different source family, cohort boundary, or roadmap pressure.

## Value Jobs

Use these labels from the Value & Jobs-to-be-Done doc:

- **Make AI safe to delegate to:** grounded, cited ingredients instead of invented
  inputs.
- **Cold-start a company:** instant cited profile for an unfamiliar company.
- **Compare a whole field:** cited cross-brand synthesis without hand-collating tabs.
- **Build on top without re-capturing:** stable State for downstream systems.
- **Trust the cache over time:** detect what changed since last look.
- **Hand off something useful in five seconds:** brief-ready language, pricing, proof,
  or whitespace.

## Design Uncertainties

Use these labels to explain what the run teaches Truffle. They are not a taxonomy of
questions and not a queue.

- **Boundary / membership:** who belongs, who is missing, who is candidate/out, and
  what source surfaces make that knowable.
- **Relations / neighborhood:** competitors, substitutes, parents, partners,
  suppliers, similar companies, and their evidence bars.
- **Source panel:** which repeatable sources define or improve the read: SERPs,
  listicles, ads, reviews/forums, regulatory surfaces, Wayback, relationship pages,
  marketplaces, or other source-of-truth pages.
- **Pattern extraction:** offers, claims, pricing, UX, acquisition surfaces, and what
  is normal vs differentiated.
- **Change pulse / freshness:** launches, pricing shifts, policy changes, partnerships,
  or stale cached fields that could invalidate a read.
- **Persistence boundary:** what can stay query-time, what deserves durable evidence,
  and what might eventually earn relation, membership, source-panel, or category/cohort
  State.
- **Confidence / source grain:** avoid false completeness when sources have different
  grains, freshness, and coverage.

## Evidence & Boundaries

- Use `store-only` only when cached State is genuinely enough.
- Use `bounded-live` when a small public source panel would materially improve the
  read; include a filled `live_evidence_plan` with `budget_class: light`, allowed /
  preferred / disallowed source families, and stop rules.
- Use `live-external-needs-approval` when the needed panel is broad, unclear,
  login-gated, paywalled, private, or likely to sprawl.
- Treat search/news snippets as leads. Current law, policy, pricing, partnership, or
  news claims need primary URLs, capture dates, and source type before confident
  language.
- Do not mutate `store/`, write back to project systems, create durable primitives,
  or graduate triage items.

## Avoid

- Selecting from a fixed question queue or prompt-menu examples.
- Picking a question only because the store can answer it easily.
- Letting triage pressure originate questions instead of annotating reader-valued
  candidates.
- Making completeness claims from partial source panels; say "not found," not "not
  there."
- Turning a query-time grouping into a durable category.
- Treating `triage.md` as a question backlog. Candidate questions live in individual
  run `scout.md` files unless Brian explicitly creates a shared queue.

## Background Pointers

- Lab contract: `experiments/00-market-read-lab/README.md`.
- Design intent: `_design/cohorts-categories/2026-06-19-market-read-lab-proposal.md`.
- Deep background: `_design/cohorts-categories/2026-06-18-wallow.md`.
- Bounded-live convention:
  `experiments/00-market-read-lab/_design/2026-06-19-bounded-live-evidence-proposal.md`.
- Value frame: Notion page `Value & Jobs-to-be-Done`.
- Post-candidate pressure check: `triage.md` and the last 3 completed
  `run-notes.md` files.
