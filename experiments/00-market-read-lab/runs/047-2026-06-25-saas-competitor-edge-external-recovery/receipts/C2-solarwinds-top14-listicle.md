# Receipt - SolarWinds Top-14 Datadog-alternatives listicle

Decision-grade source for the named external rival set.

```yaml
receipt_type: external-source
created: 2026-06-25
evidence_mode: bounded-live
source_grade: primary
source_family: SERP/listicle
spend_note: paid-credit
snippet_only: no
claim_ids_supported: [C1, C2]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source family / type | Grade | Spend | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|---|
| S1 | https://www.solarwinds.com/blog/top-14-alternatives-for-datadog-in-2026 | scraped 2026-06-25; page published 2025-12-22, modified 2026-01-28 | vendor blog / listicle | primary (for the named set) | paid-credit (5 — JSON extraction) | no | C1, C2 |

## Method

`firecrawl_scrape`, `formats:["json"]`, `onlyMainContent:true`, schema extracting the
ranked product list. **No PDF / multi-page parse** (per the run-040-hardened plan). The
JSON LLM-extraction format billed 5 credits — see run-notes R1.

## Evidence

Ranked set (14): SolarWinds Observability (self, ranked #1 "Best for hybrid ops"),
Dynatrace, New Relic, Splunk Observability, Grafana, Elastic Observability, Amazon
CloudWatch, Azure Monitor, Google Cloud Operations, IBM Instana, LogicMonitor, Zabbix,
Nagios, Paessler PRTG. All 5 store-named rivals present; set extends with cloud-native +
enterprise + open-source.

## Limits

Vendor-authored (SolarWinds ranks its own product #1) — self-serving rank/inclusion, a
fallback panel not a neutral denominator (L004). The *set* corroborates across independent
listicles (C1); the *ranking* does not.

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C1 | core rivals recur (cross-source) | S1 + C1 panel | — |
| C2 | named 14-set contains all 5 store rivals + extensions | S1 | vendor rank bias |
