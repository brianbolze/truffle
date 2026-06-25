# Receipt - C1 cold-start sample selection

The reproducible 6-company sample the cold-start calibration reads, and the deterministic rule that produced it.

```yaml
receipt_type: store-query
created: 2026-06-25
evidence_mode: store-only
source_grade: derived
source_family: local-store
spend_note: none
snippet_only: no
claim_ids_supported: [C1]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source family / type | Grade | Spend | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|---|
| S1 | `store/*/profile.md` frontmatter (136 profiles) | store, read 2026-06-25 | local-store | derived | none | no | C1 |

## Method

Goal: a reproducible, non-cherry-picked sample of 5–7 captured companies spanning `entity_type`, `primary_industry`, and capture vintage, including ≥1 non-telehealth and ≥1 less-prominent firm — per the Selected Run Contract `expected_denominator`.

Store shape (grepped 2026-06-25): 136 `profile.md`; `entity_type` = 129 Company / 7 Investor / Holding; `primary_industry` spans 12 values, **Healthcare & Life Sciences 71/136 (52%)** dominant, then Technology 27, Finance 9, Consumer Goods 6, Consulting 6, Energy 5, the rest ≤3. `captured_at` spans 2026-05-30 (oldest) → 2026-06-24 (newest); `schema_version` spans 2.2 → 2.6.

Deterministic slot rule (no quality judgment enters selection):

1. **S-inv / oldest** — alphabetically-first `Investor / Holding` domain → `blueowl-com` (also tied-oldest capture, 2026-05-30). Covers the rare entity_type + the old-vintage extreme in one slot.
2. **S-new** — alphabetically-first domain at the newest `captured_at` (2026-06-24, 6-way tie) → `eightsleep-com`. Covers the new-vintage extreme.
3. **S-tail** — alphabetically-first `Healthcare & Life Sciences` domain → `agelessrx-com`. The realistic long-tail-telehealth cold-start (the 52% bucket).
4. **S-tech** — alphabetically-first `Technology` domain → `airtable-com`.
5. **S-goods** — alphabetically-first `Consumer Goods` domain → `alange-soehne-com`.
6. **S-energy** — alphabetically-first `Energy & Utilities` domain → `blueenergy-co`. A genuinely obscure deep-tech firm.

## Evidence

Final sample (domain | entity_type | primary_industry | captured_at | schema_version):

- `blueowl-com` | Investor / Holding | Finance & Fintech | 2026-05-30 | 2.2
- `blueenergy-co` | Company | Energy & Utilities | 2026-06-14 | 2.6
- `agelessrx-com` | Company | Healthcare & Life Sciences | 2026-05-31 | 2.5
- `airtable-com` | Company | Technology | 2026-06-17 | 2.6
- `alange-soehne-com` | Company | Consumer Goods | 2026-05-31 | 2.2
- `eightsleep-com` | Company | Technology (smart-hardware) | 2026-06-24 | 2.6

Span achieved: 2 entity_types, 5 primary_industries, vintage 2026-05-30→06-24, schema 2.2→2.6, prominence mix (familiar: airtable/alange/eightsleep; obscure: blueowl/blueenergy/agelessrx).

## Limits

n=6 of 136 — a sample, not the store. Telehealth is under-sampled relative to its 52% share (1 of 6) **by design**, to force heterogeneity; a telehealth-weighted sample could read differently. "Alphabetically-first" is unbiased on quality but arbitrary on which specific firm represents each bucket. The reader (an LLM) is not a true blind cold-start reader — it carries broad priors on the famous brands; the prominence confound is analyzed in the read, not eliminated.

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C1 | The 6-company sample is reproducible from frontmatter sorts and spans entity_type / industry / vintage / prominence. | S1 | n=6 sample; telehealth under-sampled by design. |
