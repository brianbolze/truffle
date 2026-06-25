# Consumer Review

Question: **Where did Truffle create reader value, and where did it fall short?**

## Verdict

- **Valuable? Yes** — for both a strategist mapping connected hardware and a builder.
- **Why:** the schema finding and the market read are the *same* finding — the per-brand
  revenue-structure table doubles as a buyer's-glance comparison and as the evidence that
  the single `business_model` field misfires on hybrids. That dual payoff is the run's
  strength.
- **Where Truffle added value:** (a) the Result(1) two-leg table — Oura/Whoop/Eight
  Sleep/Peloton device price + recurring price + which leg the store named primary, in one
  glance; (b) the device-as-a-service spectrum (Market Pattern) names distinctions with
  direct purchase implications (Whoop: join and the device ships; Eight Sleep: buy the Pod,
  Autopilot required year 1; Oura: ring works, membership unlocks scores); (c) the
  Oura-vs-Apple tag-flip is the sharpest consumer-facing result — it shows concretely that
  filtering `business_model` to find recurring-revenue wearables *or* device-sellers
  silently misses companies.
- **Where Truffle added little or fell short:** the *blend* per brand (which leg is
  required vs optional, who bundles whom) is the single most decision-relevant fact and it
  is **not** in a scannable form — it lives in prose and inline `STRAIN:` comments. A buyer
  comparing Eight Sleep (mandatory) vs Oura (optional) must read paragraphs to extract it.
- **What the consumer can do now:** rank the four wearables by commitment structure and
  total first-year cost shape; know that a naive `business_model` filter is unsafe for this
  cohort.
- **Safer/better than generic Claude + web search:** yes — every structural claim traces
  to a dated store capture with a line cite, and the denominator (only 4 Subscription-tagged
  Hardware profiles) is an exhaustive local grep, not a vibe.
- **Biggest limit:** prices are promo-snapshots with partial uncaptures; not usable for a
  live cost comparison without the freshness caveat (which is real and named, just buried).
- **Human follow-up needed:** none for the structural question; a buyer wanting live total
  cost would need a refresh capture.

## Value diagnostics

| Signal | What to look for | Evidence / gap |
|---|---|---|
| **Useful** | Decision aid, not just a summary. | Strong — Result(1) table + spectrum are directly actionable for comparison. |
| **Judgment-ready** | Cited, rare ingredients. | Strong — two-leg structure per brand, cited to frontmatter + body lines. |
| **Sourced & cited** | Traces to dated captures. | Strong — all store paths + line numbers; C1 is an exhaustive grep. |
| **Deep enough** | Covers the set, not examples. | Strong — full 8-company panel + exhaustive 19-profile denominator. |
| **Fresh enough** | Stale assumptions visible. | Partial — promo-snapshot caveat present but buried in Evidence Used / Missing Coverage. |
| **Kept / reusable** | Warm files for next ask. | Yes — read.md + run-notes leave the cohort draw + denominator reusable. |
| **Shortfall mapped** | Names where it couldn't support. | Strong — Gap Map + Source Gaps name the composite-revenue field gap and the off-site economics ceiling. |

## Job fit

| Job | Did the read help? | Missing / next step |
|---|---|---|
| **Compare a whole field** | Yes — connected-hardware cohort compared on revenue structure, cited. | Blend (required vs optional leg) not in a scannable row. |
| **Build on top without re-capturing** | Yes — names that `business_model` alone can't filter hybrids; downstream systems should not trust it as a hybrid filter. | A composite-revenue field would resolve it (held — no consumer yet). |
| **Five-second brief input** | Partly — the table lands in 5s; the commitment-structure nuance needs a paragraph read. | Surface required-vs-optional as a table column next time. |

## Lens check

- **Strategist:** lands fast and plainly; the spectrum is a non-obvious insight (one
  `offering_category` hides five different revenue blends).
- **The Pantry / downstream system:** usable as ingredients, with the explicit warning
  that `business_model` is not a safe hybrid filter — exactly the labeled caveat a
  downstream judge needs.
- **First Contact:** trustworthy — the run shows its denominator work and refuses to
  over-claim a fix.

## Raw learning to preserve

Consumer-side sightings appended to `learning/observations.md` this pass: the
actionability gap (blend not scannable) is captured as review row **CR1**. The run's own
rows (S1, G1, R1, G2, S2, W1) already cover the structural value finding. The mode-line
"undersells the consumer value present" is a phrasing note, not a system sighting — not
logged.

**Did not propose lessons, graduate anything, or implement system changes.**
