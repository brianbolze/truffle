# Receipt - unverified_fields + STRAIN self-uncertainty taxonomy

Supports the read's census and six-kind taxonomy of the store's self-uncertainty layer.

```yaml
receipt_type: store-query
created: 2026-06-20
evidence_mode: store-only
source_grade: derived
source_family: local-store
spend_note: none
snippet_only: no
claim_ids_supported: [C1, C2, C3, C4, C5, C6, C7]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source family / type | Grade | Spend | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|---|
| S1 | `store/*/profile.md` frontmatter `unverified_fields:` block (130 files) | captured_at 2026-05-30 → 2026-06-20 | store file | derived | none | no | C1, C2, C3, C4, C5 |
| S2 | `store/*/profile.md` inline `# STRAIN` lines | same | store file | derived | none | no | C7 |
| S3 | `SCHEMA.md` ln 22/23/58/110/112/152 | repo HEAD 2026-06-20 | local-store contract | primary | none | no | C3, C5, C6 |

## Method

1. **Census + count (C1):** Python parse of each `store/*/profile.md`: extract the YAML
   list under `unverified_fields:` from the frontmatter (`---`…`---`), count bullets.
   Result: 130 profiles, 0 empty, 424 items, mean 3.26, per-profile distribution
   {1:1, 2:26, 3:56, 4:34, 5:11, 6:2}.
2. **Taxonomy (C2):** priority-ordered keyword classifier over the 424 item strings into
   seven buckets, then manual sample-validation of the residual "other" (folded mostly into
   not-public/not-captured and internal-inconsistency). Final approximate shares:
   not-public ~48% (190 + most residual), inconsistency ~12%, inferred ~11%, point-in-time
   ~11%, scope-omission ~7%, branding ~6%, tooling ~4%. **The classifier is a hand-rolled
   heuristic; shares are derived Judgment, not a captured field — report as approximate.**
3. **Greppability (C3):** only the point-in-time kind matches a SCHEMA-contracted literal
   string ("point-in-time snapshot, not fixed", SCHEMA.md:112); the inferred/conflict kinds
   have no token and live in free prose.
4. **STRAIN (C7):** grep `STRAIN` across `store/*/profile.md` → 80 lines / 58 profiles;
   keyword-bucket each line → ~56 branding/visual (~70%), 14 classification-field (~18%),
   ~10 other (~12%: inferred/owns/target-market notes). (First pass said 58 branding/73%;
   corrected to 56/~70% per Loop-2 verifier — directional majority-branding claim unchanged.)

## Evidence

Verbatim high-value exemplars (C4), quoted from each profile's `unverified_fields`:

- **Inferred / claim-not-verified:** `alange-soehne-com` "parent: richemont.com is inferred
  from footer corporate-governance links, not an explicit ownership statement"; `blueowl-com`
  "Headcount/AUM figures are the firm's own marketing stats (as of 2026-03-31), not
  independently verified"; `hormonemd-com` "Founding year (2023) + founder … from homepage
  JSON-LD only; no on-page about/history corroboration."
- **Internal-inconsistency:** `gogeviti-com` "Free-tier pay-per-test panel is listed as both
  '$399 full panel' and 'full panel from $349' on the same card"; `beta-team` "production-
  facility size - homepage says 188,000 square feet; timeline says 188,500 square feet";
  `hellopepti-com` "Treatment count — site states three different figures ('40 products',
  '90+ peptide therapies', '50+ treatments')."
- **Absence-discipline (C5):** `henrymeds-com` "State availability — site … does not
  enumerate a list"; `sequoiacap-com` "site states the company list is illustrative."
- **Scope-omission drift:** "Per-SKU roster intentionally not written this run — user
  requested profile + cohort pack + logos, not offerings.md."
- **Branding capture-fail:** `ideo-com` font name "could not confirm from screenshots";
  `waldo-fyi` "og:image is misconfigured to http://localhost:3000/og.png (production bug)."

Five confidence/provenance destinations (C6, SCHEMA.md): `unverified_fields` (ln 58 / rule
ln 23) · `Enriched (model knowledge)` Provenance line (ln 152) · inline `# STRAIN` (ln 22) ·
discrepancy-reporting in prose (ln 23 "report the discrepancy") · point-in-time literal
(ln 112).

## Limits

- The bucket shares (C2) are a **derived heuristic Judgment**, not exact; a different rater
  would move bucket edges by a few points. The load-bearing finding (the layer is a
  heterogeneous prose catch-all with no greppable token for inferred/conflict) does not
  depend on the exact percentages.
- "No caveat recorded" for a field ≠ "field verified" — the census only sees what each
  capturer chose to flag (C5).
- STRAIN bucketing (C7) is also keyword-derived.

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C1 | `unverified_fields` non-empty in 130/130; 424 items, mean 3.26 | S1 | parse-based, reproducible |
| C2 | Six-kind taxonomy + approximate shares | S1 | heuristic; shares ±a few pts |
| C3 | Point-in-time is the only greppable kind (SCHEMA literal) | S1, S3 | — |
| C4 | Verbatim high-value exemplars | S1 | direct quotes |
| C5 | Absence-discipline holds ("not found", not "not there") | S1, S3 | sampled, not exhaustive |
| C6 | Five scattered confidence/provenance destinations | S3 | from contract text |
| C7 | STRAIN 80/58, ~70% branding/visual | S2 | keyword-bucketed; corrected from 73% (verifier) |
