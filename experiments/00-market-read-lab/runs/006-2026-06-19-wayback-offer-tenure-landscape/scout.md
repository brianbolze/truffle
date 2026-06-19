# Scout

## Prior Context Read

- `triage.md`: 8 live items. Recurring spine is MRL-002 (reusable store-query helper, P1, 3
  sightings) + MRL-001 (denominator-reconciliation convention). MRL-007/008 are about
  signal/source-rigor; MRL-008 was extended by Run 005 from external-monitoring rigor to
  *captured-signal interpretation* rigor. MRL-009 (write-back-candidates section). No item is
  graduated; all await human decision.
- `scout-context.md`: go wide on plain operator archetypes first; system learning is the second
  layer. Prefer store-only / autonomous-eligible. A reputation/sentiment Signal must carry its
  confounds. Don't manufacture completeness from a partial denominator.
- Last 3 `run-notes.md` (003 abandoned template; 004 category-crowdedness; 005 Trustpilot
  signals/reputation). **005 is the only run to ever consume the Signals layer** and its
  next-run advice names Wayback tenure / SEC / Trends as the under-exercised signal grains to
  hit next, each opening a *different* signal grain.
- Store survey (this scout): 135 profiles · 54 telehealth.md · 66 offerings.md. Signals on disk:
  **wayback 47 domains (46 telehealth) — never consumed by a read**, trustpilot 20, trends 5,
  no serp/sec/exa captured. Wayback is keyed per **offer-page URL** (e.g. `/sermorelin/`), 55
  (domain,keyword) captures; each JSON carries `first_seen`, `tenure_days`, `snapshot_count`,
  `status_trail`, `first_seen_confidence`.

## Candidate Questions

| Question | Type | Autonomous eligible? | Evidence mode | Why this is worth a run | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|
| **Q1 — Wayback offer-page tenure landscape: which captured telehealth offer pages are long-lived vs newly stood up, and what does the captured tenure signal actually measure (and mis-measure)?** | mixed | **yes** | **store-only** | First read to consume the Wayback signal (47 domains on disk, untouched). Tenure = a cheap "how established / how new is this offer" lens for a strategist; and it's the next distinct signal grain after Run 005's reputation grain. | Per-capture `first_seen` + `first_seen_confidence` + `tenure_days`, capture dates, and an honest statement of *what URL* each tenure measures (offer page, not company). | **Conflating offer-page tenure with company age.** Also: treating `snapshot_count` as traffic/quality; overstating from the 47-domain floor; trusting `first_seen` where confidence != `measured`. |
| Q2 — Pricing-transparency map for a non-GLP-1 category (TRT/hormone): who publishes price vs gates behind intake? | market | yes | store-only | Extends Run 000's GLP-1 transparency read to a different category; tests whether the transparency pattern generalizes. | `offerings.md` roster price cells + `telehealth.md` price-visibility frontmatter, scoped to hormone/TRT sellers. | Roster price cells stale or absent → mistaking "not captured" for "gated". Same denominator wall as Runs 000/004. |
| Q3 — Channel / access map: cash-pay vs membership vs insurance vs pharmacy across the captured telehealth cohort. | market | yes | store-only | Plain operator map of how brands let you pay/access care; structural, citable from frontmatter. | `telehealth.md` channel/access + pharmacy_model frontmatter across 54 packs. | Frontmatter field sparsity; channel labels not normalized → forced query-time bucketing (denominator pressure again). |
| Q4 — Offer-format table-stakes: which formats/bundles (subscription, multi-month, bundled labs) recur across rosters and are becoming normal? | market | yes | store-only | "What's becoming table stakes" is a classic read; tests roster-cell parsing at format grain. | Roster cells across 66 `offerings.md`. | Whole-file grep inflation (Run 004's documented trap); format vocab not normalized. |
| Q5 — Trends signal read: branded search interest across the cohort. | market | yes | store-only | Would exercise another signal type. | Captured trends JSON. | **Only 5 domains captured** — denominator far too thin for a cohort read. Low value now. |
| Q6 — Visual/brand-quality landscape from captured `visual.md`. | market | yes | local-existing | 44 visual.md packs; design-impression clustering. | `visual.md` impression text. | `visual.md` carries no score by design (parked); clustering would smuggle in a ranking the layer refuses. |
| Q7 — Current GLP-1 compounding-policy / reference-pricing watch (refresh Run 002's stale claims). | market | **no** | live-external-needs-approval | High decision value, but Run 002's claims are dated. | Primary regulator/manufacturer URLs, capture dates, source grade. | Snippet-grade over-confidence (MRL-008). Needs approval — not unattended-safe. |
| Q8 — Backend pharmacy concentration on a compounding-heavy GLP-1 cohort (MRL-005 recurrence re-test). | market | partial | live-external-needs-approval | Directly re-tests the MRL-005 recurrence gate. | Named counterparties in `telehealth.md` bodies; likely needs fresh capture to be dense enough. | Named-is-the-minority (only 5/18 last time); prerequisite MRL-006 capture not done. |

## Selected Question(s)

1. **Q1 — Wayback offer-page tenure landscape.** Store-only, autonomous-safe, and the highest
   learning-per-token: it consumes a signal layer (Wayback, 47 domains) that no prior run has
   touched, at a grain (tenure) distinct from Run 005's reputation grain, and it sits squarely on
   a known confound (offer-page tenure != company age) that makes it a real State/Signal/Judgment
   boundary test — exactly the MRL-008 "captured-signal interpretation rigor" family.

These are Scout recommendations until Brian or the operator confirms one.

## Selected Run Contract

This is the canonical handoff to Loop 1. If this block and the candidate table disagree,
Loop 1 should trust this block.

```yaml
selected_question: "In the captured telehealth cohort, which offer pages are long-lived vs newly stood up per the Wayback tenure signal, and what does that captured tenure signal actually measure (and where does it mislead, e.g. offer-page tenure vs company age)?"
selected_slug: wayback-offer-tenure-landscape
run_type: mixed
autonomous_eligible: yes
evidence_mode: store-only
expected_denominator: "47 domains with a captured store/<domain>/signals/wayback/ dir (46 telehealth), spanning 55 (domain,keyword) offer-page captures. Partial vs the 54 captured telehealth packs and far smaller than the live market — a captured floor, not a census."
likely_source_panel: "Captured Wayback CDX JSON (store/*/signals/wayback/<keyword>/<latest>.json) + telehealth.md frontmatter (anchor_category, value_chain_role) for joins. No external surface."
allowed_sources:
  - "store/*/signals/wayback/ (captured JSON only)"
  - "store/*/telehealth.md (frontmatter for category/role joins)"
  - "store/*/offerings.md (frontmatter only, if a roster join is needed)"
  - "experiments/00-market-read-lab/triage.md"
disallowed_actions:
  - "live browsing or Wayback/CDX re-fetch"
  - "Firecrawl spend or any new capture"
  - "store/ mutation or write-back to any project KB"
  - "durable primitive / category / signal-type creation"
  - "triage graduation"
approval_needed: no
why_autonomous_safe: "Answerable entirely from captured signal JSON + local frontmatter already on disk; no spend, no live fetch, no mutation. Same posture as Run 005."
loop1_failure_mode: "Conflating offer-page tenure (what these captures measure) with company age; trusting first_seen where first_seen_confidence != measured; reading snapshot_count as traffic/popularity; and overstating cohort completeness from the 47-domain captured floor."
```

## Selection Notes

Q1 wins on the lab's own priorities: it's store-only and evidence-ready (highest autonomy), it
exercises an untouched signal layer (highest system-learning-per-run), and it lands on a live
confound the lab has been circling (MRL-008's signal-interpretation-rigor family) at a *new*
grain. Run 005's explicit next-run advice points here. Q2/Q3/Q4 are solid store-only market reads
held in reserve; Q5/Q6 are too thin or refuse-by-design; Q7/Q8 need approval (live/spend) and are
not unattended-safe.

Treat Q1's method as a hypothesis, not a copy of Run 005: the join is likely 1:1 again, but the
denominator shape is different (per offer-page URL, multiple per domain) and the confound is
tenure-specific, not reputation-specific.
