# Developer Review

Question: **What did this run reveal about Truffle's missing or weak ingredients,
capabilities, and guardrails?**

## Capability pressure

| Capability | Observed gap or strength | Evidence from this run | Discovery disposition |
|---|---|---|---|
| **Capture** | The price-visibility token (SCHEMA-2.3) was not applied at capture for 21/24 Tech profiles, even recent ones (linear 06-17, posthog 06-16 are token-less). Gap is convention-application at write time, not a Firecrawl mechanic or coverage shortfall. | G1, S1; token 3/24 | recur-watch |
| **Structure** | Positive: `business_model` filled 24/24 with zero strain off telehealth; the universal price-visibility 3-value axis correctly described SaaS when read from prose. Schema/taxonomy are not the problem; application discipline is. | C1; SCHEMA 2.3 | observation (positive) |
| **Query / access** | Primary pressure point: the structured path (`rg '\[on-request\]'`) returns near-nothing because the token wasn't applied, so the read dropped to hand-reading 24 prose blocks. Same MRL-002 prose-read friction, now cross-vertical. | F1; read.md Result | recur-watch (one sighting off telehealth) |
| **Freshness / automation** | Not this run's axis. Posture is structurally stable; 05-31 bulk-capture age not load-bearing. Correctly flagged price points stale, posture reliable. | run-notes evidence limits | no-op |
| **Synthesis** | Strong. The dual reader+builder result (three recipe ingredients → three distinct verdicts) is the clearest non-telehealth synthesis the lab has produced. The contracted trap was named and avoided. | read.md Result table | observation (positive) |
| **Guardrails** | Clean. State/Signals/Judgment boundary held; price-visibility labeled as read-time Judgment; absence language ("not captured", not "not gated") held; Loop-1 exit check passed every gate; no disallowed actions. | run-notes exit check; receipt Claim Map | observation (positive) |

## Lenses

**Steward** — System stayed honest. The load-bearing boundary — "price is on-request in
the market" (a market-State observation) vs "the store has no structured price surface" (a
coverage gap) — was handled precisely, and the contracted V1 trap was avoided. The 3/24
token gap is a concrete cross-vertical sighting of depth-backfill pressure, but it is a
*new flavor* distinct from MRL-003 (which is two named telehealth cos lacking their
vertical modules): here a *universal* convention exists, works, and generalizes but wasn't
applied at capture. Distinguishing fact (S1): the gap correlates with depth-of-capture,
not date — so the fix is convention-application, not re-capture.

**Dev Agent** — Lightest fix is W1: backfill the SCHEMA-2.3 token on the 21 token-less
`What they offer` lines — applying an existing convention, no new field/module/scrape.
Consistent with "spend on durable conventions, not living infrastructure." Do not build a
SaaS-specific pricing module; do not persist the prose-derived labels as a field.

**Founder** — Run 028 compounds the warm/cited/cheap asset while staying light. It is the
first cross-vertical *market read* (027 was a classification audit) confirming the engine's
"universal fields + reusable cuts" claim on the read layer. The highest-ROI next move is
not "capture more SaaS" but "backfill the token on the 21 existing profiles" — converts a
prose read into a one-grep structured read at zero Firecrawl cost.

## Boundary assessment

The read stayed on the State side throughout. `business_model` (C1) is greppable State.
The price-visibility classification (C2) is a read-time Judgment from prose, labeled as
such in the Claim Map, with an explicit caveat that no structured field exists to verify
against for 21/24. No classification was hardened into a field or proposed for
persistence. The "market on-request" vs "store has no structured surface" distinction —
the load-bearing boundary — was kept precise. Boundary held.

## Recommendation

- **No-op / keep as observation:** the positive Structure/Synthesis/Guardrails signals.
- **Watch for recurrence:** the 3/24 token-backfill gap (G1/S1/W1) and the cross-vertical
  prose-read friction (F1). One sighting off telehealth each — a second non-telehealth
  slice with the same gap would harden them. Do **not** open a new MRL item yet.
- **Submit triage evidence (mature):** two Evidence Log appends, below.

## Optional triage evidence

- **MRL-002 (append):** First non-telehealth *market read* (not a classification audit,
  per 027) confirms the read-recipe family is not telehealth-overfit — enum-grep
  (`business_model` 24/24) and prose-read ingredients run cleanly on the SaaS substrate;
  only the structured price-visibility grep is blocked, by the token-backfill gap, not a
  recipe defect. `query-time-grouping-enough` fires cross-vertical. Pointer: runs/028
  read.md Result table; run-notes O1; `discovery-ledger.md` 028 O1.
- **MRL-008 (append):** New flavor — *structured-field-absence is not a market fact*.
  Prior MRL-008 entries fix Signal/State headline fields with integrity siblings, or a
  bare relation field's self-description (run 026). This adds: an *absent structured
  convention* (the price-visibility token, 3/24) returns near-nothing on a grep and could
  be read as "SaaS doesn't gate prices" — the inverse of the truth (6 cos fully
  quote-gated, visible only in prose). The guardrail is the "not-captured-in-field ≠
  not-true-in-market" distinction, now cross-vertical. Pointer: runs/028 run-notes V1;
  scout contract `loop1_failure_mode`; read.md Result.
- The token-backfill gap itself: hold at recur-watch in `discovery-ledger.md` (028
  G1/S1/W1); do not open MRL-015 on one sighting.
