# Receipt - SERP Datadog-alternatives panel

Supports the claim that ≥5 independent Datadog-alternatives listicles exist and the core
rival set recurs across ≥2 independent ones.

```yaml
receipt_type: source-panel
created: 2026-06-25
evidence_mode: bounded-live
source_grade: direction-finding
source_family: SERP/listicle
spend_note: paid-credit
snippet_only: yes
claim_ids_supported: [C1]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source family / type | Grade | Spend | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|---|
| S1 | firecrawl_search "best Datadog alternatives 2026 observability monitoring tools" (id 019efcf4-2188-7139-b076-6305cd504d92) | 2026-06-25 | search result | direction-finding | paid-credit (2, −1 refund = net 1) | yes | C1 |

## Method

One `firecrawl_search` query, `limit: 6`. Search-result snippets used as leads only; the
one decision-grade source (C2) was scraped in full. Search feedback submitted
(feedbackId 019efcf5-ab84-726f-ac4b-60c410e9bbd0), 1 credit refunded.

## Evidence

Returned listicles (independent publishers): newrelic.com/blog (rival blog), velodb.io
(VeloDB, SigNoz, Dynatrace, Grafana Cloud), solarwinds.com (Top 14 → scraped as C2),
dotcom-monitor.com (Dynatrace + New Relic lead; Prometheus+Grafana), uptrace.dev (Datadog,
Grafana, New Relic, Uptrace), plus a Reddit r/ExperiencedDevs thread (Splunk for logs).
Core rivals Dynatrace / New Relic / Splunk / Grafana recur across ≥2 independent listicles.

## Limits

`snippet_only: yes` — these are leads, not decision-grade. Only C2 was scraped in full and
used for a confident named-set claim. Reddit is review/forum-adjacent, not used as evidence.

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C1 | ≥5 independent Datadog-alternatives listicles exist; core rivals recur across ≥2 | S1 | Snippet-grade; vendor-authored listicles dominate (L004) |
