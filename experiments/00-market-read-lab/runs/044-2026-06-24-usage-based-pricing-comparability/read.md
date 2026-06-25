# Market Read

## Question

For a developer/CTO comparing usage-based dev-infrastructure tools (Datadog, Snowflake, Stripe,
Twilio, PostHog, AWS), can Truffle's captured State let a buyer actually *compare cost*, or do the
incommensurable metered units (per-host vs per-credit vs per-event vs %-of-volume vs per-message)
defeat an apples-to-apples comparison even when verbatim pricing is present — and is the
price-visibility token convention even present across these mostly pre-2.3 captures?

## Result

**Short answer: the store carries the metered prices richly and verbatim, but the cohort is *not*
cost-comparable — each brand bills in its own consumption primitive, so the only thing that compares
across the six is pricing *shape*, never magnitude. This is the third pricing-shape where
unit-incommensurability, not missing data, is the ceiling (after run-023 GLP-1 and run-043 wearable
TCO).**

**(1) Verbatim metered pricing is present and high-quality for 5/6.** Every core member except AWS
carries exact, quoted headline rates pulled from its own `/pricing` page (C1):

| Brand | `business_model` | Billing unit(s), verbatim | Free tier | Captured |
|---|---|---|---|---|
| Datadog | Usage-based / Consumption | `"$15 per host"` (Infra Pro), `"$31"`/host (APM), `"$0.10 per ingested GB"` (Logs), per-million-events | Free tier most products | 2026-05-31 |
| Snowflake | Usage-based / Consumption | `"$2.00 / per credit"` (Std) → `"$4.00 / per credit"` (Biz Critical); `"$23.00 per TB / per month"` storage | Free trial | 2026-05-31 |
| Twilio | Usage-based / Consumption | `$0.0083`/SMS, `$0.0085`/min voice, `$0.05`/verification, `$1`/active-user-hour (Flex/Video), `$0.0013`/email | Free trial | 2026-05-31 |
| PostHog | Usage-based / Consumption | `"$0.00005/event"`, `"$0.005/recording"`, `"$0.0001/request"`, `"$0.10/response"`, `"$0.25/GB"` logs | Generous monthly free tier per product | 2026-06-16 |
| Stripe | Usage-based / Consumption | `"2.9% + 30¢ per successful transaction"`; per-product $/wire, $/payout, $/verification, %-of-volume | No setup/monthly fee (PAYG) | 2026-06-04 |
| AWS | Usage-based / Consumption | *utility metering* — `"You only pay for the services you consume"`; per-service units across 200+ services; **no single rate quoted** (defers to `offerings.md`) | `$100` free-tier credits + 6-mo limits | 2026-05-31 |

**(2) No two brands share a billing unit — the comparison fails on units, not on data (C2).** Host vs
credit vs event vs message vs %-of-transaction-volume vs per-service-utility. The metered unit *is the
product's own consumption primitive*, so "which is cheaper" has no cohort-level answer: a buyer cannot
convert `$15/host` (Datadog) into `$2/credit` (Snowflake) into `2.9%+30¢/transaction` (Stripe) without
modelling their own workload. AWS is the sharpest case — it doesn't even publish a representative rate;
the profile honestly captures the *pricing philosophy* (utility/pay-per-consume) rather than numbers.
What **does** compare cleanly across all six is the **shape**: metered consumption + a free tier as the
top-of-funnel + committed-use/enterprise discount + a self-serve→sales expansion path. Every profile
captures that shape well; none can be ranked on price.

**(3) `business_model: Usage-based / Consumption` is a clean *positive* cohort key — a contrast to
run-039's SaaS collapse (C3).** Grepping the field returns exactly the metered businesses
(datadoghq, snowflake, stripe, twilio, posthog, aws) plus two non-infra entities (blueenergy,
waldo) that are excluded by hand. Unlike run-039, where `[Software / SaaS]` flattened ~19 distinct
sub-markets into one undifferentiated pile, here the field *recovers* the cohort the question is
about. Caveat: it's a coarse primary tag — Stripe and Snowflake carry a 2nd `offering_category`
(Fintech, Marketplace), and the field names only the *primary* leg, so a hybrid like Notion
(`Subscription` primary + a usage-based credits layer riding on top, per its inline comment) sits in
the *foil* set despite having metered revenue. The key recovers pure-play metered businesses, not
every business with metered revenue.

**(4) The price-visibility token convention is near-absent across this cohort — a coverage gap, not a
transparency signal (C4).** The token (`[published | partial | on-request]`, SCHEMA 2.3+) appears on
only **1 of 6** members: Stripe (23 `[published]`, 2 `[on-request]`). The reason is capture-clock, not
opacity:
- Datadog, Snowflake, Twilio, AWS are **schema 2.2 (pre-2.3)** — they predate the token convention
  entirely. SCHEMA is explicit that an absent token = "predates the convention," **not** `[published]`
  (no backfill).
- PostHog's `profile.md` is **schema 2.6 (post-2.3)** yet carries **no tokens** on its `What they offer`
  lines — its fully-public rate cards are captured verbatim but never tokenized. (Its `offerings.md` is
  also untokenized, but that file is on the *module*-schema track at v1.2, which predates the token
  convention independently — a routine module-backfill gap, not part of this tell. The real signal is the
  v2.6 *profile* being untokenized.)
So for a buyer who tried to use the token as a "can I get a price?" filter across this cohort, it would
mislead by *omission*: 5/6 untokenized despite all 6 publishing prices. The token is a real win where
applied (Stripe), but it is not a dependable cross-cohort surface on captures this vintage.

**(5) Stripe is a useful L006 data point — and it's the *non*-trap case (C5).** L006 (proposed) warns
the price-visibility token reports buyer-reachability, not what an intermediary charges its monetized
side. Stripe is an intermediary (payments processor) whose monetization *is* a %-of-volume fee — and
that fee **is** published to its paying customer (the merchant), so its `[published]` tokens read
*correctly*. This matches run-037 DR3's sharpened scope: the L006 trap fires only when the intermediary
leg has **no consumer-facing price** (a marketplace's host/guest take-rate split), not whenever an
entity is an intermediary. Stripe charges its primary customer directly and publishes that charge —
the opposite of the marketplace trap. A second entity-type sighting for L006, landing on the *safe*
side.

## Gap Map

| Buyer need | Store support | Verdict |
|---|---|---|
| See each tool's headline rate verbatim | Strong — exact quoted rates from each `/pricing`, with capture clocks | **Clean** (5/6; AWS by design quotes philosophy not rate) |
| Compare cost across tools | The data is all present but **unit-incommensurable** — no cohort-level "cheaper" exists | **Structural ceiling, not a data gap** |
| Compare pricing *shape* (metered + free tier + enterprise expansion) | Strong — every profile captures the motion | **Clean** |
| Use the price-visibility token to filter "can I get a price?" | Token on 1/6 only (4 predate 2.3; PostHog untokenized) | **Coverage gap — absent ≠ published** |
| Estimate *my* actual bill | Needs the buyer's own workload model (host count, event volume, GMV) | **Off-store by nature — a calculator job, not a capture job** |

The headline result is a **clean gap map of a structural ceiling**: the store did its job (verbatim,
dated, honest pricing) and the un-comparability is a property of the market (every metered SaaS picks
its own consumption unit), not a Truffle shortfall.

## Evidence Used

Store-only; all claims trace to captured `profile.md` files (no external sources).

- **C1** — verbatim metered rates: datadoghq-com profile:54–64 (`$15/host`, `$0.10/GB`),
  snowflake-com profile:66–71 (`$2.00–$4.00/credit`, `$23/TB/mo`), twilio-com profile:59–62
  (`$0.0083/SMS`, `$1/active-user-hour`), posthog-com profile:66–73 (`$0.00005/event` …),
  stripe-com profile:62–66/74–75 (`2.9%+30¢`), aws-amazon-com profile:69–77 (utility, no single rate).
- **C2** — unit incommensurability: the six billing units above share no common denominator;
  AWS profile:69 (`"pay for the services you consume"`), snowflake profile:53 (`no per-seat tiers`).
- **C3** — cohort key: `grep "business_model: Usage-based" store/*/profile.md` → datadoghq, snowflake,
  stripe, twilio, posthog, aws + blueenergy, waldo (non-infra, excluded); contrast run-039 SaaS collapse.
- **C4** — token presence: stripe profile:62–66/74–75 (`[published]`×23, `[on-request]`×2);
  datadoghq/snowflake/twilio/aws `schema_version: "2.2"` (pre-2.3, no tokens); posthog `schema_version:
  "2.6"` with zero tokens on profile.md or offerings.md. SCHEMA.md:99 (absent token = predates-convention).
- **C5** — L006 non-trap: stripe profile:62 (%-of-volume `[published]` to the merchant); run-037 DR3
  scope; lessons.md L006.

## Companies Seen

- **Core usage-based cohort (6):** datadoghq-com, snowflake-com, stripe-com, twilio-com, posthog-com,
  aws-amazon-com.
- **Excluded from the usage-based grep (non-infra, named with reason):** blueenergy-co (energy),
  waldo-fyi (small app).
- **Subscription foils (5):** cloudflare-com, openai-com, notion-com (hybrid: subscription primary +
  usage-credits layer), linear-app, airtable-com.

## Missing / Stale Coverage

- Datadog/Snowflake/Twilio/AWS captured 2026-05-31 (schema 2.2) — pricing pages are volatile; a metered
  rate card can change without notice, so these rates are a dated snapshot, not a durable price (cousin
  of run-043 S3). No staleness defect found; flagged as inherent.
- AWS deliberately captured at philosophy-grain (no per-service rates) — correct for a 200+-service
  catalog, but it means AWS cannot be priced even within its own profile (an `offerings.md` job).

## Source Gaps

- **The buyer's own workload model** is the one ingredient that would make these prices comparable — and
  it is not a capture target at all; it's a per-buyer calculator input (host count, event volume, GMV,
  message count). No source family the store could add closes this; it is off-store by nature.
- No external panel needed or used. The structural answer is fully visible from store State.

## Raw Learning to Preserve

See `run-notes.md` Observations: **S1** (metered units incommensurable — 3rd pricing-shape sighting),
**S2** (`business_model: Usage-based` as a clean positive cohort key — run-039 contrast), **G1** (token
convention near-absent on the cohort — coverage gap, absent ≠ published), **S3** (Stripe = L006 non-trap,
2nd entity-type sighting on the safe side), **G2** (single-valued `business_model` puts the hybrid Notion
in the foil set despite metered revenue), **W1** (anti-sprawl: no normalization field — the ceiling is
market structure, not a missing column).

## External Completeness Check

Not load-bearing — the cohort is defined by an internal field (`business_model: Usage-based`), and the
read's claim is about *comparability*, not *completeness of the cohort roster*. No external denominator
needed. (If a "complete list of usage-based dev-infra vendors" were the question, an external panel would
be required; it is not.)

## Market Pattern

Usage-based dev-infrastructure has converged on a single **commercial shape** — meter the customer's own
consumption primitive, give a generous free tier as acquisition, discount for committed use, expand
self-serve→enterprise — while **deliberately diverging on the metered unit** (host, credit, event,
message, %-of-volume, per-service). That divergence is a feature: each vendor meters the thing that
scales with the customer's value, which makes cross-vendor price comparison structurally impossible and
is exactly why "cost calculators" and FinOps tooling exist as a separate industry. Truffle captures the
shape and the verbatim rates faithfully; it cannot — and arguably should not try to — manufacture a
cross-unit "cheaper than" that the market itself refuses to express.

## What Would Change This Answer

- A **real downstream consumer that needs to *filter/sort* metered tools programmatically** (not just
  read them) would be the trigger to revisit — but per run-037 W1 / run-043 W1, the lightest path is
  still a ranked multi-select `business_model` (so Notion's hybrid is recoverable), **not** a normalized
  price field. Unit-incommensurability means a price-magnitude field would launder false precision —
  exactly what engine-dev's "evidence, not scores" forbids. "No new primitive needed" stays live.
- A **second pre-revenue... no:** a second *post-2.3* usage-based cohort that *is* tokenized would test
  whether G1's token-absence is a vintage artifact (likely) or a convention that doesn't fit metered
  pricing (PostHog's v2.6 *profile* hints at the latter — post-convention yet untokenized; note its
  `offerings.md` absence is a separate module-schema-vintage gap, not evidence for this). That would
  sharpen whether the token convention should ever apply to pure-metered sellers.
