# Receipt - Tech-slice competitor-neighborhood derivation

Supports the read's claim that the SaaS neighborhood is reconstructable from prose but not
from structured fields, that competitor edges are prose-only and mostly off-store, and that
the M&A chain is recorded inconsistently.

```yaml
receipt_type: store-query
created: 2026-06-24
evidence_mode: store-only
source_grade: derived
source_family: local-store
spend_note: none
snippet_only: no
claim_ids_supported: [C1, C2, C3, C4, C5]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source family / type | Grade | Spend | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|---|
| S1 | `store/*/profile.md` frontmatter (`primary_industry`, `offering_category`, `target_market`, `business_model`, `parent`, `owns`, `description`) | captures mostly 2026-06-17 | local-store | derived | none | no | C1, C2, C4, C5 |
| S2 | `store/datadoghq-com/profile.md:73-74` | 2026-06-17 | local-store / owned-site synthesis | secondary (captor-summarized) | none | no | C3 |
| S3 | `store/gong-io/profile.md:59-60` | 2026-06-17 | local-store | secondary | none | no | C3 |
| S4 | `store/dovetail-com/profile.md:85` | 2026-06-17 | local-store | secondary | none | no | C3 |
| S5 | `store/listenlabs-ai/profile.md:121` | 2026-06-17 | local-store | secondary | none | no | C3, C4 |
| S6 | `store/coda-io/profile.md` (`parent`) + `store/superhuman-com/profile.md` (`owns`) | 2026-06-17 | local-store | derived | none | no | C5 |

## Method

1. `grep -rl "^primary_industry: Technology" store/*/profile.md` → 23 profiles.
2. For each, extracted `domain`, `offering_category`, `target_market`, `business_model`,
   `description`, `parent`, `owns` from frontmatter.
3. Clustered into sub-markets by reading the one-line `description` (LLM judgment — flagged
   as such in the read; not a store field).
4. `grep -icE "competitor|compete|alternative to|vs\.|versus|rival"` across the 23 bodies,
   then read the matched lines to separate genuine competitor-naming from generic marketing.
5. Cross-checked each named competitor against `ls store/` to mark in-store vs off-store.
6. Compared the Grammarly/Coda/Superhuman ownership records across the three profiles.

## Evidence

- C1: ~19/23 carry `offering_category: [Software / SaaS]`; the 4 exceptions are apple/casio
  (hardware), eightsleep (hardware), upwork (`Marketplace / Platform`).
- C3: competitor naming present verbatim in ~5/23 bodies at three grains — Datadog (clean
  list: New Relic, Dynatrace, Splunk, Grafana, Elastic), Gong (per-product: Clari;
  Salesloft/Outreach), Dovetail (comparison-page set: Condens, Looppanel, Marvin), Listenlabs
  (Qualtrics, UserTesting + Outset, Remesh, Strella, Conveo), Clari (category posture only).
- C4: of those named, only Clari has a captured profile; New Relic, Dynatrace, Splunk,
  Grafana, Elastic, Salesloft, Outreach, Condens, Looppanel, Marvin, Outset, Remesh, Strella,
  Conveo are absent from `store/`.
- C5: `coda.io` → `parent: [grammarly.com]`; `superhuman.com` → `owns: [coda.io]`, described
  as "Grammarly rebranded." Same acquisition, two different owners recorded.

## Limits

- The 7-cluster sub-market map (C2) is **LLM judgment over prose**, not store State; a
  different reader could draw the boundaries differently. It is a Judgment, labeled as such.
- The competitor-edge census (C3/C4) is bounded by what each captor chose to write into the
  body; absence of a competitor line means "not captured," not "no competitor."
- The captured slice is a partial, capture-biased sample of the SaaS market; counts describe
  the store, not the market.

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C1 | Structured fields collapse ~19 SaaS profiles into one bucket | S1 | — |
| C2 | Slice resolves into ~7 description-legible sub-markets | S1 | LLM judgment, not store State |
| C3 | Explicit competitor edges exist in prose, uneven grain, ~5/23 | S2-S5 | captor-dependent; not exhaustive |
| C4 | Most named competitors are off-store | S1, S5 | "not captured" ≠ "doesn't exist" |
| C5 | M&A chain recorded inconsistently across profiles | S6 | both STRAIN-flagged, not reconciled |
