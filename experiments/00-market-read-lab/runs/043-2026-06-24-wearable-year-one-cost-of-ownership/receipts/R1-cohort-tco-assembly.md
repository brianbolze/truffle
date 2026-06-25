# Receipt - Cohort year-one TCO assembly (store-only)

Supports the per-brand year-one total-cost-of-ownership table and the "assemblable but
not apples-to-apples" finding, entirely from captured State.

```yaml
receipt_type: store-query
created: 2026-06-24
evidence_mode: store-only
source_grade: derived
source_family: local-store
spend_note: none
snippet_only: no
claim_ids_supported: [C1, C2, C3, C4, C5, C6]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source family / type | Grade | Spend | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|---|
| S1 | store/whoop-com/profile.md:35,40,63,65–67,75 | 2026-06-24 capture | store file / owned-official-derived | primary (captured State) | none | no | C1 |
| S2 | store/ouraring-com/profile.md:41,48,71–74,81 | 2026-06-24 capture | store file | primary | none | no | C2 |
| S3 | store/eightsleep-com/profile.md:37,44,67–68,75,79 | 2026-06-24 capture | store file | primary | none | no | C3 |
| S4 | store/onepeloton-com/profile.md:36,43,64,67–80,87 | 2026-06-24 capture | store file | primary | none | no | C4 |
| S5 | store/apple-com/profile.md:33,40,59 | 2026-05-31→2.2 re-stamp | store file | primary | none | no | C5 |
| S6 | store/therabody-com/profile.md:51,72–79; store/hyperice-com/profile.md:51,84; store/nike-com/profile.md:49,88–94 | 2026-06-24 capture | store file | primary | none | no | C6 |

## Method

Drew the cohort by entity-shape (connected device + recurring layer) rather than
`primary_industry`. For each profile, read frontmatter (`business_model`,
`offering_category`, price-visibility tokens), the body pricing block, and `site_notes` /
`unverified_fields`. Assembled year-one TCO = lowest captured device price + first-year
subscription at the captured cadence. Carried every point-in-time / sale-snapshot flag and
the required-vs-optional status from prose into the table. No external source, no spend.

## Evidence

- Whoop: "membership with the hardware included… you don't buy the device, you join";
  tiers "Starts at $199/239/359/yr" `[partial]`; checkout gated at join.whoop.com.
- Oura: ring "$244–$499"; membership "$5.99 USD/month or $69.99 USD/year, first month
  free"; "the only way to unlock… insights"; same-day Ceramic price disagreement.
- Eight Sleep: "Pod 5… $2,749 (~~$2,999~~), Queen"; "Autopilot… required for the first 12
  months", Standard $199 / Enhanced $299 / Elite $399; "Rent the Pod… from $169/mo".
- Peloton: hardware "$695 (refurb) → $6,695 (Tread+)"; "All-Access Membership $49.99/mo —
  required for Bike/Tread/Row owners".
- Apple: inline prices captured only for Mac ("MacBook Neo… From $599"); Apple Watch
  listed in the catalog with no SKU price; `business_model: Transactional / One-time`.
- Foils: Therabody / Hyperice `business_model: Transactional / One-time`, device-only
  prices, no subscription shown; Nike membership is a free loyalty layer.

## Limits

Cannot prove current prices — all device numbers are 2026-06-24-era sale snapshots the
profiles themselves flag as point-in-time. Cannot deliver an Apple Watch SKU price (below
the captured grain). Cannot prove Whoop's all-in checkout total (gated). Year-one TCO is a
defensible assembled *range*, not a single comparable number, by the four frictions in the
read's Gap Map.

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C1 | Whoop year-one = membership only, device bundled | S1 | Tier floors; all-in gated |
| C2 | Oura = ring once + value-gating membership | S2 | Flash-sale snapshot; price disagreement |
| C3 | Eight Sleep = Pod + mandatory Autopilot (or rent) | S3 | Ultra/non-Queen prices not captured |
| C4 | Peloton = hardware + required All-Access $49.99/mo | S4 | Wide device range; refurb point-in-time |
| C5 | Apple Watch year-one not deliverable from State | S5 | Catalog-grain capture; no Watch SKU price |
| C6 | Foils one-time only, no required sub | S6 | Confirms business_model accurate single-leg |
