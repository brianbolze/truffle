# Market Read

## Question

For a 5-brand GLP-1 telehealth panel the store is blind to on state availability
(run-038 G1 — henrymeds, joinfound, remedymeds, ivimhealth, hellowisp), can a *light,
non-gated public source panel* (brand-owned state/legal pages + SERP) recover state-level
availability, or is the buyer's deciding fact only reachable inside the intake funnel?

> **Run did not complete cleanly.** It fails closed to `needs-human-review` on a
> **spend-ceiling breach** (R1): one PDF parse cost 15 credits, taking the run to ~23
> paid credits against the Scout's 10-credit ceiling. Evidence-gathering stopped at that
> point. The findings below are real and source-graded, but the run is blocked, not
> `read-done` — see Gap Map and run-notes exit check.

## Result

**A light public panel partially recovers state availability, and the recovery is
*surface-type-shaped*, not brand-shaped.** The discriminator is *which* non-gated public
surface a brand uses to state availability — its legal/ToS page recovers it, its
marketing funnel does not, and where the only enumerated surface is an interactive
picker, it stays effectively gated. Two grains behave differently:

- **The all-50-vs-not binary is often recoverable** from a non-gated legal/disclaimer
  surface the store didn't capture.
- **The precise per-state list for partial-coverage brands is NOT recoverable** from a
  light public panel — it sits behind the intake funnel or an interactive state-picker.
  This is a true reachability wall at the list grain, not a capture-scope choice.

Per-brand (panel of 5):

| Brand | Store baseline (captured) | Public-panel result | Grade | Recovered? |
|---|---|---|---|---|
| **remedymeds** | "States served — not on captured pages" (captured the `/quiz` funnel + PDPs) | Brand-owned **ToS PDF** (non-gated): "The Services are available in all fifty (50) states plus the District of Columbia." (Last Updated 2025-12-05) | primary, brand-owned | **Yes — binary fully recovered** from a surface the capture skipped |
| **ivimhealth** | No state line captured | Every brand page (home, ToS, first-visit) carries "**Not available in all states**" — a qualifier, never a list | primary, brand-owned | **Partial** — confirms *not* all-50; no enumeration off-funnel |
| **henrymeds** | "one of the states we support" (no list); KYZATREX TRT excl. CA | Brand pages don't enumerate; **Forbes** review: "currently available in 40 states + DC" with named exclusions | secondary (3rd-party) | **No primary** — only a secondary count |
| **joinfound** | State availability behind a ~40-state picker; CA "No plans available" in demo | `/insurance` is again an interactive **state-picker** ("Select state, Alabama, Arizona…"); a **Facebook ad** says "available in all states" | gated / social | **No** — non-gated surface is the picker; no clean list |
| **hellowisp** | Store already strong: "all 50 states"; public `/provider-credentials` per-state license page; 8 states video-required by law | (not re-probed live — already the captured exception) | primary, brand-owned (cached) | n/a — the on-site strong case |

Net: a non-gated public panel moved **remedymeds** from "blind" to "all-50 confirmed
(primary)" and **ivimhealth** from "blind" to "not-all-50 (primary, no list)"; it did
**not** recover a precise state list for any partial-coverage brand. So the answer to the
probe is *both* — the off-surface fact is partly a capture-scope choice (the ToS/legal
source family is under-captured) and partly a true reachability wall (the per-state list
for partial brands is funnel-only).

## Gap Map

- **Truffle answered cleanly:** the *baseline* — that the store is blind on state
  availability for 4/5 of the panel (hellowisp the exception). Run-038 G1 reproduced.
- **The public panel closed (partially):** the **legal/ToS source family** is the
  under-captured non-gated surface. Capturing it would recover the all-50-vs-not binary
  for brands that disclose there (remedymeds). This is a *capture-scope* gap, not a wall.
- **The public panel could NOT close:** the **precise per-state list** for partial
  brands (henrymeds, joinfound, ivimhealth). It lives only inside the intake funnel
  (disallowed to enter) or an interactive picker (joinfound `/insurance`). This is a
  **true reachability wall** at the list grain for a light public panel.
- **What would have changed the answer:** entering the intake funnel / operating the
  state-picker (explicitly disallowed) — i.e. the wall is real, not a search-skill gap.

## Evidence Used

For `bounded-live`, this lines up with `run-notes.md` `live_evidence_used`.

- **C1 — remedymeds all-50 (primary):** `https://remedymeds.com/remedymeds/documents/terms-of-service.pdf`,
  captured 2026-06-24, source type = brand-owned legal page (PDF), **primary**. Quote:
  "The Services are available in all fifty (50) states plus the District of Columbia."
  (doc "Last Updated: 12/5/2025".) Scrape cost 15 credits (15 pp) — see R1.
- **C2 — ivimhealth not-all-50 (primary, no list):** SERP across `ivimhealth.com`
  home / `/terms-and-conditions/` / `/your-first-visit-with-ivim-2/`, captured 2026-06-24,
  brand-owned, **primary** for the qualifier "Not available in all states." (SERP-snippet
  grade; not scraped — snippet is a direct on-page disclaimer repeated site-wide.)
- **C3 — henrymeds 40-states (secondary):** `https://www.forbes.com/health/weight-loss/henry-meds-review/`,
  captured 2026-06-24, third-party review, **secondary** — "available in 40 states + DC."
  Brand-owned pages do not enumerate (direction-finding only).
- **C4 — joinfound picker-gated:** `https://joinfound.com/insurance`, captured 2026-06-24,
  brand-owned but an **interactive state-picker** (not a static list); a Facebook ad
  ("available in all states") is **social/unreliable**, not used for a confident claim.

SERP snippets were treated as leads; the only confident *primary* claim confirmed by
reading a brand page is C1. C2's qualifier is repeated verbatim across several brand-owned
pages in the SERP and is a low-risk negative ("not all states"), not a positive list.

## Companies Seen

Panel of 5, all from run-038's blind set: henrymeds.com, joinfound.com, remedymeds.com,
ivimhealth.com, hellowisp.com. No denominator/census attempted — fixed panel by design.

## Missing / Stale Coverage

Store captures (henry 2026-06-04, found 2026-06-04, remedy 2026-06-01, ivim 2026-06-04,
wisp 2026-06-16) all scoped the **marketing funnel + PDPs**, not the **legal/ToS** pages.
The remedymeds availability statement (in ToS, "Last Updated 2025-12-05") predates the
2026-06-01 capture, so it was reachable at capture time — a scope choice, not staleness.

## Source Gaps

- **Legal/ToS source family** is the load-bearing under-captured surface for the
  availability *binary*. Cheap, public, non-gated, but outside the current capture scope
  (which targets marketing + product pages).
- **Intake funnel / interactive state-picker** is the only surface carrying the precise
  per-state list for partial-coverage brands — disallowed and structurally gated.
- Off-scope but surfaced (not chased): remedymeds ToS names its MSO backend
  (OpenLoop / Rezilient / JMP / J.P. Medical professional entities) — relation-pressure
  relevance; and an **FDA warning letter to Remedy Meds (2025-09-09)** appeared in SERP —
  a regulatory signal. Both flagged, neither pursued (out of this run's scope/ceiling).

## Raw Learning to Preserve

See `run-notes.md` Observations: **G1** (per-state list = true reachability wall),
**S1** (ToS/legal is the recovering surface; capture-scope artifact), **S2** (recovery is
surface-shaped not brand-shaped), **R1** (spend-ceiling breach — PDF parse cost invisible
pre-call), **W1** (lightest path = a capture/recipe note, not a field), **G2** (off-scope
backend-MSO + FDA-letter pointers surfaced by the ToS/SERP panel).

## External Completeness Check

Not applicable — fixed 5-brand panel, no completeness/denominator claim. "Not found" is
used throughout, never "not there."

## Market Pattern

Across DTC telehealth, *where* a brand discloses geographic availability is itself a
pattern: compliance-minded brands state an all-50 (or not-all-50) line in **ToS/legal**;
the precise serviceable-state list is treated as **funnel logic** (eligibility gating),
not marketing content. So the buyer's binary "do they operate in my state at all" is
often public; the precise "is MY state in" resolves only inside intake.

## What Would Change This Answer

- A 2nd brand whose precise per-state list turns out to live on a non-gated page would
  weaken the "list grain = reachability wall" claim (hellowisp's `/provider-credentials`
  is the one near-example — license numbers, not a serviceable-states list).
- Permission to operate the state-picker / enter intake (currently disallowed) would test
  whether the list is *reachable* but just gated, vs genuinely intake-derived.
- A wider panel could show whether ToS-states-disclosure is common or a remedymeds
  idiosyncrasy (n=1 primary positive here).
