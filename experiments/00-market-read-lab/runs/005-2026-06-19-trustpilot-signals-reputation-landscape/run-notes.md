# Run Notes

```yaml
run_status:            reviewed
evidence_mode:         store-only
autonomous_eligible:   yes
termination_reason:    completed
pressure_lenses_fired: [coverage-caveat, source-rigor, query-time-grouping-enough]
```

## 30-second operator read

- **Did the run work?** Yes. Store-only, no spend, no mutation. **First read to ever touch the
  Signals layer** — prior runs (000–004) were all State reads. The captured Trustpilot signal
  was query-ready straight off disk.
- **What was awkward?** The interesting answer is a *caveat about the signal itself*: among 13
  scorable brands, scores cluster 4.3–4.9 and that mostly tracks `paid_profile` +
  `asks_for_reviews`, not quality. So the read's real value is teaching a downstream consumer
  *not* to sort-by-score-and-stop. hims (3.0, 8,554 reviews, 28% one-star) is the only
  credible low score; the two sub-2.5 brands have ~16–18 reviews (noise).
- **What the next agent should know:** the Signals layer pays off at read time (no re-capture
  needed), but a reputation Signal is a textbook State/Signal/Judgment boundary case — the
  `profile_flags` confounds (paid/solicited) must travel with the score or the read misleads.

## What happened

Gated on the contract (scout-only → store-only → autonomous → approval:no, all pass). Pulled the
latest `signals/trustpilot/*.json` per brand (lexical = chronological on ISO-Z names), extracted
score / volume / distribution / `profile_flags` / `profile_state`, joined `anchor_category` +
`value_chain_role` from each `telehealth.md`. Built one derived receipt
([`receipts/trustpilot-signal-panel.md`](receipts/trustpilot-signal-panel.md)) and wrote the
read keeping Signal (the score) and Judgment ("trusted"/"posture artifact") explicitly separated.
No external fetch, no `store/` write, no `store.py` needed (slug↔signal join was 1:1).

## Inputs and scope

- Working set: **20 brands with a captured `store/<domain>/signals/trustpilot/` dir**; 13 scorable,
  7 `not_found`/`removed`/`empty`. All 20 are `value_chain_role == DTC brand` telehealth.
- Files: `store/*/signals/trustpilot/<latest>.json`, `store/*/telehealth.md` frontmatter.
- Capture clock: 2026-06-15 (19 brands), 2026-06-18 (waldo-fyi). 1–4 days old.
- Exclusions: prior captures per brand (no trend diff — out of scope for the question); the other
  ~34 captured telehealth brands without a Trustpilot signal; all non-Trustpilot signal types.

## Friction log

- **No reusable signal-aggregation surface.** Same shape as the State-read friction in Runs
  000/001/004: to answer one cohort question I hand-wrote a loop over signal JSON, picked the
  latest per dir, and pulled fields. Different store layer (Signals, not State), same in-run
  query-machinery improvisation. (`query-time-grouping-enough` for *this* question, but
  `tooling-ergonomics`-adjacent across runs.)
- **`profile_flags` is the load-bearing part and easy to drop.** The score is trivially
  greppable; the confound flags (`paid_profile`, `asks_for_reviews`) are what make the read
  honest, and nothing in the read path forces them to travel with the score. (`source-rigor`)
- One file had `profile_flags: null` (inactive profile) and crashed a naive `.get()` — minor,
  guarded.

## Evidence limits

- **Trustpilot is a self-selected, *payable* secondary surface** — not independent quality. The
  panel measures solicitation posture × volume more than regard. (`source-rigor`)
- **Coverage floor:** 20/54 captured telehealth brands have any Trustpilot signal; 13 scorable.
  Reputation claims are over this slice, not the market. (`coverage-caveat`)
- **Tiny-N trap:** truniagen (16) / trtnation (18) reviews are near-anecdotal; their low scores
  are not decision-grade.
- **Single snapshot:** no trend; "negative sentiment concentration" is static.
- **Aggregates only:** no review text, so the *why* behind hims' 28% one-star is invisible here.

## Loop 1 exit check

Record `pass` / `fail` for the mandatory exit check before setting final `run_status`.

- Status was `scout-only` before Loop 1: **pass**
- `Selected Run Contract` was present and consistent with header: **pass**
- `autonomous_eligible: yes`: **pass**
- `evidence_mode` was `store-only` or `local-existing`: **pass** (store-only)
- `approval_needed: no`: **pass**
- No disallowed action happened: **pass** (no browse/spend, no re-capture, no `store/` write,
  no primitive creation, no KB write-back; only `read.md` + receipt + run-notes touched)
- Required citations / receipts present and source-graded: **pass** (receipt graded `derived`;
  C1–C5 mapped, with S1 Trustpilot flagged as secondary/self-selected)
- No snippet treated as evidence: **pass** (no external/snippet sources; all from captured JSON)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass** (every score
  carries its capture date + review_count; no pricing/policy/news claims made)
- Absence language says "not found", not "not true": **pass** (7 brands framed as "not captured /
  no Trustpilot presence", never "no reputation"; thin-N framed as noise, not verdict)

All items pass → `run_status: read-done`, `termination_reason: completed`.

## Surprises

- **The signal mostly grades itself, not the brand.** The tight 4.3–4.9 cluster lines up with
  `paid_profile`+`asks_for_reviews` so cleanly that the score reads more as "manages Trustpilot"
  than "is trusted." The confound was sitting in the captured `profile_flags` the whole time.
- **hims inverts the cluster.** The biggest, best-known brand has the lowest *credible* score
  (3.0) precisely because its organic volume (8,554) can't be drowned by solicitation — a neat
  illustration that volume is the real credibility gate.
- **The "distrusted" tail is an artifact.** Sorting by score puts truniagen/trtnation at the
  bottom, but they're 16–18 reviews — the ranking would mislead anyone who didn't open the count.

## Pressure tags

Short `kebab-case` tags for system pressure this run exposed. These are recurrence handles, not a fixed taxonomy and not permission to build.

Use an existing tag when it fits; coin a narrow tag only when the guide misses the thing.

| Tag | Use when |
|---|---|
| `denominator-reconciliation` | The answer depends on defining / cleaning / reconciling the company or source **set**. |
| `source-rigor` | Source grade blocks confidence: snippets, weak secondary sources, missing URLs, or missing capture dates. |
| `source-panel` | A repeated external source **set** seems needed to answer this kind of question. |
| `coverage-caveat` | Store coverage, stale captures, or incomplete modules materially limit the answer. |
| `depth-backfill` | A specific field/module is missing across otherwise relevant companies. |
| `query-time-grouping-enough` | The read was answerable by grouping existing store evidence; no durable category object is needed. |
| `freshness-monitoring` | Current pricing, news, policy, regulation, or launch motion could change or materially improve the answer. |
| `relation-pressure` | Competitors, named parents, suppliers, partners, or other counterparties seem repeatedly useful. |
| `tooling-ergonomics` | Repeated manual steps suggest a helper, query recipe, or template tweak. |

Which tags fired, if any? Did this run need a new or clearer tag?

"No new primitive needed" is a valid outcome.

| Fired tag | What fired in this run | Triage implication |
|---|---|---|
| `coverage-caveat` | 20/54 telehealth brands have any Trustpilot signal; 13 scorable. Reputation panel is a ~37% slice of the captured cohort. | No-op / watch. Standard captured-floor caveat; expected for an opt-in external signal. |
| `source-rigor` | Trustpilot is a payable, solicited surface; the score conflates "well-regarded" with "manages Trustpilot." `profile_flags` confounds must travel with the score or the read misleads. | Watch for recurrence. First sighting at the *Signals consumption* grain (MRL-008 was about external *monitoring* rigor; this is about a captured-signal's interpretive confound). Submit as a watch note, not a new build. |
| `query-time-grouping-enough` | The whole read was answerable by grouping existing captured signals at query time. No durable reputation/category object needed; "who's trusted" stays a labeled query-time Judgment. | No-op / watch. Reinforces the no-new-primitive posture; reputation is a Signal + a downstream Judgment, not new State. |

## Triage submissions

**Do not implement, spike, or recommend immediate graduation from inside the run.**

- **MRL-008 — append evidence (first Signals-consumption sighting).** MRL-008 is about source
  rigor for *external/monitoring* panels (snippets are leads, not evidence). This run surfaces a
  sibling at the *captured-signal interpretation* grain: a captured Trustpilot score carries
  built-in confounds (`paid_profile`, `asks_for_reviews`, review volume) that must travel with it
  or a downstream consumer will sort-by-score and be misled. Candidate (pattern-level, not a
  build): when a read consumes a reputation/sentiment Signal, require the confound flags + volume
  to be reported alongside the score, and keep "trusted/distrusted" as a labeled Judgment. **First
  sighting at this grain — watch for recurrence before any convention.**
- **No new State or Signals primitive.** Reputation is cleanly Signal (the captured score) +
  downstream Judgment ("who's trusted"). The engine already captures the right fields including
  the confounds. Nothing to graduate.
- **Possible no-op note for MRL-007:** this run did *not* surface a homeless category-level
  signal (Trustpilot is per-domain and attached cleanly), so it gives MRL-007 no new evidence —
  worth recording that the per-domain signal path worked fine here.

## Next-run advice

- The Signals layer is query-ready off disk and under-exercised — good territory for the next few
  reads (Wayback tenure, SEC-presence-vs-offer, trends). Each opens a different signal grain.
- For any reputation re-read: **always pull `review_count` + `profile_flags` with the score**, and
  weight confidence by volume. Treat sub-100-review scores as anecdotes.
- A cheap high-value follow-up: **diff the 2–3 existing captures per brand** to convert this static
  snapshot into a score-trajectory read (is anyone moving?) — still store-only, no spend.
- If a second Signals-consumption read also has to hand-roll the "latest-per-dir + extract fields"
  loop, that recurrence (not this one sighting) would be the signal to consider a tiny
  signals-read recipe in QUERYING.
