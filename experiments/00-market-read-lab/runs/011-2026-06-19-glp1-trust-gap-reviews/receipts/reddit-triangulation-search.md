# Receipt - Reddit triangulation search (billing/cancellation cluster)

A second source family (Reddit) to test whether the dominant billing/cancellation objection appears off Trustpilot. Direction-finding only — snippets, not opened pages.

```yaml
receipt_type:          source-panel
created:               2026-06-19
evidence_mode:         bounded-live
source_grade:          direction-finding   # search-result snippets, not full bodies
source_family:         review/forum
spend_note:            paid-credit         # 2 Firecrawl search credits
snippet_only:          yes
claim_ids_supported: [C1, C3]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source family / type | Grade | Spend | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|---|
| S4 | firecrawl_search `site:reddit.com` — "kept charging after cancel no refund" across panel brands | 2026-06-19 | review/forum (Reddit search results) | direction-finding | paid-credit (2) | yes | C1, C3 |

## Method

One `firecrawl_search` restricted to `reddit.com` for the billing/cancellation objection.
Used only to corroborate that the dominant Trustpilot cluster is not a single-platform artifact.
Results were **not** opened/scraped — treated as leads per source-rigor rules.

## Evidence

Snippet leads (r/henrymeds), all pointing at the same cluster as the Trustpilot bodies:
- "Henrymeds no longer has medication, refusing to cancel subscription… tried to charge me AGAIN."
- "they don't contact you just charge your card."
- "contact them right away to cancel or they'll just keep charging you monthly even if you don't get any more meds. They use the 'access to' [subscription framing]."
- "Henry Meds has been charging me $297/mo for absolutely nothing. No medication, and no medical consultations."

## Limits

Snippets are leads, not decision-grade evidence. They corroborate the *direction* of the
Trustpilot cluster (billing-after-cancel; June-2026 medication-availability problems at
henrymeds) but were not read in full and carry no verified prevalence. A dedicated
r/henrymeds subreddit existing and trending on this topic is itself a directional signal.

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C1 | Billing/cancellation cluster appears on a second source family (Reddit), not just Trustpilot | S4 | snippet-only; directional |
| C3 | henrymeds medication-availability / cancellation problems corroborated off-platform | S4 | snippet-only; directional |
