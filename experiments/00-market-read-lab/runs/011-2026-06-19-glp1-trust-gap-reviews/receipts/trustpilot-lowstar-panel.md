# Receipt - Trustpilot low-star review panel (3 GLP-1 brands)

Captures the customer-objection bodies (1-2 star reviews) for the three panel brands; primary source for the objection-cluster claims.

```yaml
receipt_type:          source-panel
created:               2026-06-19
evidence_mode:         bounded-live
source_grade:          primary        # first-party customer review bodies, dated; platform-moderated, not representative
source_family:         review/forum
spend_note:            paid-credit    # 3 Firecrawl scrape credits (1 per brand)
snippet_only:          no             # full review bodies captured, not search snippets
claim_ids_supported: [C1, C2, C3, C4, C5, C6]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source family / type | Grade | Spend | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|---|
| S1 | https://www.trustpilot.com/review/remedymeds.com?stars=1&stars=2 | 2026-06-19 | review/forum (Trustpilot 1-2★ bodies) | primary | paid-credit (1) | no | C1, C4, C6 |
| S2 | https://www.trustpilot.com/review/henrymeds.com?stars=1&stars=2 | 2026-06-19 | review/forum (Trustpilot 1-2★ bodies) | primary | paid-credit (1) | no | C1, C3, C6 |
| S3 | https://www.trustpilot.com/review/hims.com?stars=1&stars=2 | 2026-06-19 | review/forum (Trustpilot 1-2★ bodies) | primary | paid-credit (1) | no | C1, C2, C4, C6 |

## Method

`firecrawl_scrape` (markdown, onlyMainContent, waitFor 6000ms) on each brand's Trustpilot
profile filtered to `?stars=1&stars=2` (negative bodies only). Deliberately a low-star cut:
the goal is objection mining, not a balanced rating read. Panel = 3 of 19 store GLP-1 brands,
chosen to span the spectrum: hims (public/scale leader), remedymeds (compounding-heavy
cheap-access), henrymeds (mid-market flat-fee). Each page returned ~12-20 dated review bodies.

## Evidence

**Headline scores (context, confounded — see MRL-008):** hims **3.0** / 8,591 reviews
("Average"); henrymeds **4.4** / 12,503; remedymeds **4.6** / 12,586. remedymeds & henrymeds
both run *paid Trustpilot subscriptions* and *invite* customers to review (upward bias); hims
is a *merged profile*. So the headline score the store already captures (e.g. remedymeds
"Excellent 4.7" badge) is not comparable across the three and travels without objection context.

**Billing / cancellation trap (C1) — dominant cluster, all three brands:**
- remedymeds: "I stopped requesting medication refills… The subscription continued renewing every 28 days… approximately **$2,400 had been charged**. Remedy Meds refunded only the most recent charge." (Jun 18 2026); "They kept charging me after I canceled… stole $600… Only after threatening to contact my bank they returned my money." (Jun 16); "$398.99 each month for December, January, and February… refunded only the February charge and refused… stating a non-refundable policy. However, no services were provided." (Mar 18).
- hims: "I cancelled on same day after I found out the meds are NOT INCLUDED in the fee - but they refuse to refund even though it was same day and no service provided." (Jun 15 2026); "**SCAM ALERT** They charge you for a monthly fee but don't provide service!… said it was non-refundable!" (Jun 19).
- henrymeds: "Subscription charged at **$400/month when I haven't received medication in over a year**… When I tried to cancel… it offered to cut my cost to $178/month." (Jun 7 2026).

**Price bait-and-switch (C2) — venture-scale brands, esp. hims:**
- "The website advertises the Wegovy pill for $149 a month in big black letters… As soon as it's time to get to the actual effective dose, they jack the price up to $299. Classic bait and switch." (hims, Jun 16 2026).
- "the membership shouldn't spike after the first month… membership fee goes up to $149 a month and that's WITHOUT the meds." (hims, multiple).

**Customer-service unreachability / ghosting (C3) — dominant henrymeds cluster, June-2026 degradation signal:**
- "**Defunct as of June 2026** — As of June 15, 2026 they have completely stopped providing customer care. No one answers phones… Chat option has been removed… But they keep charging you." (henrymeds, Jun 16 2026).
- "I used Henry Meds for 2 years… 2 months ago I realized I hadn't received any emails… After 7 weeks, 12 phone calls, 8 emails… I cancelled." (Jun 11); multiple reviewers tie the drop to a **pharmacy switch** ("things changed after they switched pharmacies… semaglutide is diluted").

**Efficacy doubt + lab friction (C4) — secondary:**
- "This is a Med is a scam! …placebo GLP1 that they are selling in a vile." (remedymeds); "Too many requests for lab work" (remedymeds, 2★).

## Limits

A deliberately low-star, single-platform sample. It shows **which objections cluster**, not
their prevalence — the same brands carry thousands of positive invited reviews. "In this
sampled panel" language is required; this cannot support "customers think X" or any
market-representative prevalence claim. Trustpilot bodies are first-party but platform-moderated
and self-selected. Review claims about specific charges/dates are unverified individual accounts.

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C1 | Billing/cancellation traps are the dominant objection cluster across all three brands | S1,S2,S3 | sampled low-star; individual accounts unverified |
| C2 | Price bait-and-switch (dose-step price jump; membership excludes meds) is a distinct hims-side cluster | S3 | concentrated in scale brand |
| C3 | CS unreachability/ghosting dominates henrymeds, with a June-2026 service-degradation signal | S2 | sampled; degradation is a directional signal, not confirmed corporate fact |
| C4 | Efficacy doubt + lab-work friction are secondary clusters | S1,S3 | small N in panel |
| C5 | Owned-page trust devices don't address the actual objection clusters | S1,S2,S3 + store | see store receipt |
| C6 | Panel is 3 of 19, low-star-filtered, directional not representative | S1,S2,S3 | denominator caveat |
