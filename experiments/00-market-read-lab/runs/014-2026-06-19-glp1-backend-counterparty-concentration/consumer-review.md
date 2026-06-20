# Consumer Review

Loop 2, adversarial three-pass shape. An independent evidence-verifier pass re-ran every grep
against `store/` and confirmed all load-bearing claims (denominator=19; 16/3 pharmacy_model split;
OpenLoop named by exactly home-medvi + joinfridays and resolving to `store/openloophealth-com`;
the 3 named pharmacies all dangling; the 14 unnamed brands genuinely name no entity) with **no
miscounts and no overclaims** — the read's hedging ("lead, not concentration"; "not stated, not
no-relationship") was held throughout.

## Verdict

- **Valuable?** Partly.
- **Why:** Methodologically clean and unusually honest about what it found vs. didn't. It enforces the
  MRL-001/005 contamination guard (possessive "our pharmacy" ≠ named counterparty), surfaces a real
  cross-brand recurrence (OpenLoop), and labels it a *lead* rather than a concentration claim — that
  intellectual honesty is what makes it safer than generic Claude + web search. But the core result is
  genuinely thin: 5/19 name *any* counterparty, 2/19 share one. Two brands is a hypothesis to test, not
  a pattern to act on.
- **What the consumer can do now:** (1) A strategist can assert "clinical backend is more concentrated
  and more *legible* than pharmacy backend in this cohort" — the most actionable sentence in the read.
  (2) A downstream agent gets a concrete, store-joinable proof-of-concept edge (MEDVi → OpenLoop,
  Fridays → OpenLoop) to design a counterparty layer *from* rather than theorize about. (3) A simple
  watch: grep any future GLP-1 capture for "OpenLoop" to see if the recurrence grows.
- **What made it safer / better than generic Claude + web search:** Grounded denominator (19 anchored
  brands, not a guessed list); named-vs-unnamed called out with verbatim quotes as evidence; explicit
  join-resolution check against store profiles, honest about which fail; the contamination guard
  actually enforced. A generic search would likely invent a pharmacy network and call it concentration.
- **Biggest limit:** Two brands is closer to noise than signal — the read says so itself. The pharmacy
  layer is a black box (no store profiles for any named pharmacy), so the pharmacy side is answered
  ("they don't recur; they're almost all unnamed") partly by the brands *choosing opacity*, not by full
  knowledge.
- **Human follow-up needed:** One specific item — capture the joinfridays `/terms-conditions/#pharma`
  partner list before drawing further conclusions about its pharmacy counterparties (a named gap the
  read flags but cannot resolve store-only).

## Value diagnostics

| Signal | What to look for | Evidence / gap |
|---|---|---|
| **Useful** | Clear answer or next step | Clear answer to the named question; the "clinical leaks through; pharmacy is a black box" frame is quotable; the next step (watch for a third OpenLoop brand) is explicit. |
| **Judgment-ready** | Cited ingredients to reason from | Verbatim `telehealth.md` quotes for every named-counterparty claim; join status checked and reported; uncertainty ("floor not ceiling") labeled. |
| **Sourced & cited** | Claims trace to dated captures | All claims trace to `store/`; the anchor-only denominator caveat is carried throughout, not buried. Per-brand capture-staleness not quantified (acceptable for a relation read). |
| **Deep enough** | Covers the intended set | All 19 anchored GLP-1 brands; the one gap (joinfridays pharmacy list) is flagged, not hidden. |
| **Kept / reusable** | Warm state for the next ask | No write-back (per contract). The Companies Seen table + claim IDs C1–C5 let a follow-up agent resume without re-reading the store. |

## Job fit

| Job | Did the read help? | Missing / next step |
|---|---|---|
| **Make AI safe to delegate to** | Yes — verbatim quotes, explicit join checks, contamination guard enforced; a downstream agent can build on these claims without re-browsing. | Pharmacy profiles all missing; any pharmacy-side enrichment finds no join targets today. |
| **Compare a whole field** | Partly — answers the named-counterparty question across the full anchored cohort, but the pharmacy black box means "we can't compare what they don't disclose." | A full-GLP-1 (not anchored-only) denominator would be a second pass. |
| **Build on top without re-capturing** | Yes, narrowly — the OpenLoop edges are store-joinable; the table is reusable state. | The table is a natural seed for a lightweight counterparty frontmatter field — a design decision the read argues for minimally but does not make. |

## Lens check

- **Strategist:** "The clinical layer is where shared infrastructure leaks through" lands fast and is
  novel relative to web search; the labeled "lead, not concentration" call is right. Biggest miss for a
  strategist: it stops at two brands — a strategist wants to know whether OpenLoop is "the Stripe of
  clinical telehealth," and the read honestly can't answer that yet.
- **The Pantry / downstream system:** Companies Seen table is structured, claim IDs anchor to store
  file sections, join status is explicit — consumable without re-browsing. Freshness is implicit
  (2026-06 refresh noted in bodies) rather than per-brand-dated in the output.
- **First Contact:** The contamination guard and the explicit "absence ≠ no relationship" caveat make
  the epistemics visible; a new consumer can see what was checked and what wasn't.

## Triage submissions

One additive candidate (see `triage.md` Evidence Log): the uncaptured joinfridays
`/terms-conditions/#pharma` partner list is an actionable, bounded store gap — if OpenLoop recurrence
is the load-bearing signal, joinfridays' pharmacy counterparties are the next unknown that could move
the pharmacy-side answer. A targeted single-URL bounded-live recapture candidate, not a schema change.
No graduation, no implementation.
