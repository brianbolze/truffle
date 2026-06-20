# Receipt - Hone neighbor-set derivation

How the candidate neighbor field and per-brand classification inputs were produced from the store.

```yaml
receipt_type:          store-query
created:               2026-06-20
evidence_mode:         store-only
source_grade:          derived
source_family:         local-store
spend_note:            none
snippet_only:          no
claim_ids_supported: [C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14, C15, C16, C17]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source family / type | Grade | Spend | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|---|
| S1 | `grep -lE "^anchor_category: (TRT\|longevity/NAD\|labs)" store/*/telehealth.md` | store clock 2026-05-31→2026-06-18 | store file (derived) | derived | none | no | C1 |
| S2 | `store/honehealth-com/profile.md` | 2026-06-18 | store file (firecrawl) | State | none | no | C0 |
| S3 | per-brand `store/<domain>/telehealth.md` frontmatter + positioning comments (anchor_category, audience, modality, pay_model, hero/wedge prose) | 2026-05-31→2026-06-18 | store file (firecrawl) | State | none | no | C2–C17 |

## Method

1. **Anchor job**: read `honehealth-com/profile.md` → Overview/Positioning/What-they-offer for the
   core job-to-be-done and load-bearing mechanics (panel wedge, membership, breadth, both sexes,
   longevity framing).
2. **Candidate field**: `grep -lE "^anchor_category: (TRT|longevity/NAD|labs)" store/*/telehealth.md`
   → 16 non-Hone brands (TRT 8, longevity/NAD 7, labs 1). One pass, no manual list.
3. **Classification inputs**: for each candidate, pulled `anchor_category`, `audience`, `modality`,
   `pay_model` frontmatter + the inline positioning comments (captured State) that describe the wedge
   and front door. Tiered by the substitute test (does a Hone shopper cross-shop for the *same
   lab/physician-led optimization job*) vs adjacency (overlaps a component, different core job).

## Evidence

- Candidate field counts: **TRT (8)** defymedical, getopt, getpetermd, hormonemd, marekhealth,
  maximustribe, trtnation, vitalityrx; **longevity/NAD (7, ex-Hone)** agelessrx, gethealthspan,
  gogeviti, mylifeforce, niagenplus, prohealth, truniagen; **labs (1)** functionhealth. (Hone itself
  is longevity/NAD.)
- Discriminating State examples: functionhealth `modality: async` + "no gating consult, does not
  prescribe" → adjacent despite sharing the diagnostic wedge; vitalityrx `audience: men-only` +
  "enclomiphene, NOT exogenous T" → adjacent single-mechanism; mylifeforce "50+ biomarker diagnostic
  wedge" + both-sex tracks → Tier-1 substitute.

## Limits

- **Anchored-only floor (MRL-001):** un-anchored generalists selling hormone/longevity lines are
  excluded; the set is a floor, not Hone's full competitive universe.
- Classification is a **positioning judgment**, not an enum lookup — `anchor_category` is necessary
  but not sufficient to separate substitute from adjacent (see read §Design finding).
- No demand-side corroboration (no SERP/Exa/owned-vs panel; store-only contract). Supply-side
  positioning inference only.

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C1 | Candidate neighbor field = anchored TRT/longevity/labs set (16 brands) | S1 | anchored-only floor |
| C0 | Hone anchor job + mechanics | S2 | self-reported owned-site State |
| C2–C17 | Per-brand positioning inputs for tiering | S3 | positioning judgment, not enum-derivable |
