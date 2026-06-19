# Receipt - Trustpilot captured-signal panel (20 brands)

The latest captured Trustpilot signal per brand, plus the State join (category/role), that
the reputation read is built on.

```yaml
receipt_type:          store-query
created:               2026-06-19
evidence_mode:         store-only
source_grade:          derived
snippet_only:          no
claim_ids_supported: [C1, C2, C3, C4, C5]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source type | Grade | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|
| S1 | `store/*/signals/trustpilot/<latest>.json` (20 brands) | captured_at 2026-06-15 (19 brands) / 2026-06-18 (waldo-fyi) | store file (Trustpilot capture via tool) | derived (Trustpilot is secondary, self-selected) | no | C1,C2,C3,C4,C5 |
| S2 | `store/*/telehealth.md` frontmatter (`anchor_category`, `value_chain_role`) | store clock May–Jun 2026 | store file | primary (own-site capture) | no | C2,C5 |

## Method

Took the lexically-last `*.json` in each `store/<domain>/signals/trustpilot/` dir (capture
timestamps are ISO-Z, so lexical = chronological). Extracted `trust_score`, `review_count`,
`reviews_last_12m`, `rating_distribution`, `profile_state`, `profile_flags`. Joined
`anchor_category` / `value_chain_role` from each brand's `telehealth.md`. No re-capture, no
external fetch, no `store/` write.

## Evidence

13 of 20 brands have a scorable active profile; 7 have no usable signal
(`not_found` / `removed` / `empty`: eden-health, getpetermd-com, gogeviti-com, hydramed-com,
niagenplus-com, struthealth-com, waldo-fyi).

Scorable brands, by score (capture 2026-06-15):

| Brand | Cat | Score | Reviews | 1★ | 5★ | paid_profile | asks_for_reviews |
|---|---|---:|---:|---:|---:|:--:|:--:|
| marekhealth-com | TRT | 4.9 | 924 | <1% | 97% | yes | yes |
| defymedical-com | TRT | 4.8 | 3,829 | 1% | 95% | yes | no |
| honehealth-com | longevity/NAD | 4.8 | 11,645 | 3% | 93% | yes | yes |
| directmeds-com | GLP-1 | 4.6 | 10,308 | 8% | 84% | yes | yes |
| joinamble-com | GLP-1 | 4.6 | 4,035 | 11% | 81% | yes | no |
| sermorelin-com | peptides | 4.5 | 49 | 4% | 88% | **no** | yes |
| agelessrx-com | longevity/NAD | 4.4 | 2,288 | 7% | 80% | yes | yes |
| joinfridays-com | GLP-1 | 4.4 | 4,475 | 7% | 80% | yes | yes |
| maximustribe-com | TRT | 4.4 | 982 | 9% | 82% | yes | yes |
| mylifeforce-com | longevity/NAD | 4.3 | 184 | 12% | 67% | yes | yes |
| hims-com | GLP-1 | **3.0** | 8,554 | 28% | 39% | yes | yes |
| truniagen-com | longevity/NAD | 2.4 | 16 | 63% | 19% | **no** | **no** |
| trtnation-com | TRT | 2.3 | 18 | 61% | 22% | **no** | **no** |

Score summary (n=13): min 2.3, max 4.9, median 4.40, mean 4.11.

## Limits

- Trustpilot is a self-selected, claimable, **payable** review surface — not an independent
  quality measure. `paid_profile` and `asks_for_reviews` flags are confounds, not metadata.
- Review counts span 16 → 11,645; tiny-N brands (sermorelin 49, mylifeforce 184, truniagen 16,
  trtnation 18) carry near-anecdotal weight.
- 7/20 brands have no usable profile — that is "not captured / no Trustpilot presence", not
  "no reputation."
- Captures are 1–4 days old (fresh) but a single point in time; no trend computed here.

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C1 | 13/20 captured brands have a scorable Trustpilot profile; 7 are not_found/removed/empty | S1 | absence = not captured |
| C2 | Scorable brands cluster tightly at 4.3–4.9 (10 of 13); hims (3.0) and two tiny-N brands (2.3–2.4) are the only sub-4 | S1,S2 | self-selected surface |
| C3 | High scores coincide with paid_profile + asks_for_reviews; the two lowest scorers solicit nothing and have ~16–18 reviews | S1 | posture confound |
| C4 | hims is the only high-volume brand (8,554) with a low score (3.0) and 28% 1★ | S1 | volume overwhelms solicitation |
| C5 | All 20 are DTC telehealth brands (TRT/GLP-1/longevity/peptides); no category shows a distinct reputation tier within this captured set | S2 | small per-category N |
