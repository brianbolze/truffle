# Consumer Review

Question: **Where did Truffle create reader value, and where did it fall short?**

## Verdict

- **Valuable? Yes.** Run 028 delivered a real, actionable SaaS pricing-landscape read
  *and* settled the design question run 027 left open (do the read recipes generalize off
  telehealth, not just the taxonomy?).
- **Why:** the reader answer — price visibility tracks GTM motion, ~14 self-serve/PLG
  publish rate cards, ~6 enterprise sales-led are quote-gated — is a concrete finding with
  named company-level evidence, not a hedged non-answer. The builder answer is equally
  clean: enum-grep and prose-read ingredients generalize; only the structured-token path
  fails, and for a known backfill reason.
- **Where Truffle added value:** the GTM-motion framing (publish = PLG, gate = sales-led)
  explains *why* each cluster behaves as it does, not just *that* it does. The named
  on-request cluster (clari, alpha-sense, gong, qualtrics, usertesting, listenlabs) and
  the usage-based = cloud/AI-infra sub-cluster (aws, snowflake, twilio, datadog, posthog,
  waldo) are clean, reusable cohort cuts derived with zero new capture. `business_model`
  is filled 24/24 — a greppable, durable primary-filter asset.
- **Where Truffle added little / fell short:** the price-visibility answer required
  hand-reading prose across 24 profiles because the universal SCHEMA-2.3 token is
  populated 3/24 (offerings.md 4/24). A consumer who wants "give me all the on-request
  companies" as a grep **cannot** — they must commission a fresh prose read. The ~14/~6
  split is a read-time Judgment, not a verifiable field, so it carries less precision than
  the telehealth equivalent. Entry-offer structure (free-tier vs trial vs demo-gated) was
  only partially separable from prose — that sub-part of the question was answered weakly.
- **What the consumer can do now:** use `business_model` (24/24) as a primary store
  filter; use the GTM-motion heuristic to place any of the 24 named companies; run the
  usage-based sub-cluster as a follow-on read with no new capture. Cannot: run a one-grep
  structured price-visibility query off telehealth until the token is backfilled.
- **Safer/better than generic Claude + web search:** yes, on the structured side. The
  business_model fill and the specific named buckets are primary-source facts from
  own-site captures, not training-data recall. Generic Claude would produce a plausible
  taxonomy but couldn't name *which* companies are quote-gated today, nor surface the
  backfill gap as a quantified obstacle.
- **Biggest limit:** the structured price-visibility surface is nearly empty off
  telehealth (3/24), so the split is a prose Judgment and no cheap cross-vertical
  price-visibility comparison is possible until backfill. A capture-era gap, not a schema
  defect.
- **Human follow-up needed:** none required for the read to stand. Optional: a steward
  decision on whether to backfill the SCHEMA-2.3 token on the 21 token-less profiles.

## Value diagnostics

| Signal | What to look for | Evidence / gap |
|---|---|---|
| **Useful** | Clear answer / decision aid. | Yes — GTM-motion split + named clusters; a strategist can act on it. |
| **Judgment-ready** | Fresh, rare, cited ingredients. | Partly — business_model is greppable State; price-visibility is a prose Judgment (labeled). |
| **Sourced & cited** | Claims trace to dated captures. | Yes — receipt with store clocks; primary own-site grade; uncertainty flagged. |
| **Deep enough** | Covers the intended set. | Yes for the 24 profiled Tech cos; denominator is a floor (tech-adjacent cos under other industries missed). |
| **Fresh enough** | Capture dates visible. | Yes — 19/24 at 2026-05-31 noted; posture treated as stable, price points as possibly stale. |
| **Kept / reusable** | Warm files for the next ask. | Yes — read.md + receipt; the usage-based cohort + business_model cut are reusable. |
| **Shortfall mapped** | Names where Truffle couldn't support. | Yes — the 3/24 token gap and weak entry-offer capture are named precisely (G1/W1, Gap Map). |

## Job fit

| Job | Did the read help? | Missing / next step |
|---|---|---|
| **Compare a whole field** | Yes — published/on-request split across 24 cos by GTM motion. | A structured price-visibility query needs the token backfill. |
| **Five-second brief input** | Yes — "SaaS pricing splits on GTM motion: self-serve publishes, enterprise sales-led gates." | — |
| **Build on top without re-capturing** | Partly — business_model 24/24 is queryable; price-visibility is not (prose only). | Backfill the token to make it greppable. |
| **Cold-start a company** | Partly — any of the 24 can be placed in the GTM map with primary-source backing. | — |

## Lens check

- **Strategist:** the GTM-motion framing is the right altitude — it explains buyer
  sophistication / deal complexity (the on-request cluster is exactly the
  revenue/experience/research-intelligence set). Cannot do a structured cross-portfolio
  comparison today without the backfill.
- **The Pantry / downstream system:** `business_model` is a reliable 24/24 primary
  filter; the price-visibility token is **not** (21/24 empty) and offerings.md is thinner
  still (4/24) — a Pantry consumer expecting to query this field will be disappointed off
  telehealth.
- **First Contact:** the named buckets are immediately trustworthy for a first brief; the
  6 quote-gated cos form a coherent, nameable cluster. Lands in one sentence (Scott-Witt
  brief-grade).

## Optional triage evidence

- **MRL-002 (append):** first non-telehealth *market read* confirms the read-recipe family
  generalizes — see developer-review and `discovery-ledger.md` 028 O1.
- **MRL-008 (append):** structured-field-absence-is-not-a-market-fact guardrail (V1), now
  cross-vertical. See developer-review.
- The 3/24 token-backfill gap (G1/W1) is real but one-sighting off telehealth — preserve
  in `discovery-ledger.md`, hold at recur-watch; do not graduate.
