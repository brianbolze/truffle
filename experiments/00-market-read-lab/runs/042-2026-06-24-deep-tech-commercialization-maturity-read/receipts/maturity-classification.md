# Receipt - maturity classification (prose vs structured fields)

Supports the maturity ranking and the finding that structured fields are maturity-blind
while prose carries the signal.

```yaml
receipt_type: store-query
created: 2026-06-24
evidence_mode: store-only
source_grade: derived
source_family: local-store
spend_note: none
snippet_only: no
claim_ids_supported: [C2, C3]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source family / type | Grade | Spend | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|---|
| S1 | profile bodies (milestones/traction lines) for the 8 | captured 2026-06-14 | store file (owned/official) | primary (site-attested) | none | no | C2 |
| S2 | profile `description` + `business_model` + `offering_category` frontmatter for the 8 | captured 2026-06-14 | store file | primary | none | no | C3 |
| S3 | profile `unverified_fields` for the 8 | captured 2026-06-14 | store file | primary | none | no | C2, C3 |

## Method

For each profile, extracted (a) the dated maturity anchors from the milestones/traction
prose, (b) the present-tense `description` + `business_model` + `offering_category`, and
(c) the `unverified_fields`. Compared what the prose attests against what the structured
fields encode.

## Evidence

**Prose maturity anchors (S1) — the basis for the ranking (most→least mature):**

- **beta-team:** "2025 IPO… over $1 billion… NYSE… ticker BETA"; "188,000-sq-ft… up to 300 aircraft per year"; "Charge Cubes… UL-listed / UL Certification"; "DO-160G… ARP4754… DO-254"; "FAA test-pilot evaluation."
- **evoloh:** brochure "Pricing below $250/kW for 2026-27 deliveries" `[published]`; "500MW of binding orders to date"; "16 GW of signed intent"; S440 at 3M "operational in 2027."
- **electra-aero:** "EL2 Goldfinch first flew November 11, 2023"; "FAA Part 23 type-certification application… December 2025"; "2,200 pre-orders… valued at nearly $9 billion" (self-reported); "$115 million Series B… April 2025."
- **cfs-energy:** "spun out of MIT in 2018"; "over $2 billion in capital"; SPARC "net-energy demonstration machine being built"; ARC "planned"; Google "200 MW" + Eni ">$1 billion" offtake.
- **verdegoaero:** "founded in 2017"; products "being developed with U.S. Air Force and NASA support"; VH-4T "since 2024 on maturing."
- **blueenergy:** "Founded 2023"; "$380 million in financing" (2026-04); NRC topical report approved; turbines "reserved for site delivery in 2029."
- **sorafuel:** "$14.6 million round" (2026-04); funding supports "construction and operation of a pilot production facility"; demonstration milestone "within 18 to 24 months"; LOI for "first 10 million gallons" of future e-SAF.

**Structured fields are maturity-blind (S2):**

- `description` present-tense for pre-revenue cos: electra "Builds the EL9," evoloh "Manufactures electrolyzer stacks," sorafuel "Produces sustainable aviation fuel" — none has commercial deliveries matching the verb.
- `business_model` **blank** for cfs-energy and sorafuel; intent-only where present (electra/evoloh `Transactional / One-time`, blueenergy `Usage-based / Consumption`).
- `offering_category` shares the value `[Physical Products / Hardware]` for beta-team (shipping/certified components; frontmatter also lists `Services / Consulting`) and electra (only `[Physical Products / Hardware]`, zero deliveries) — the shared value encodes no maturity. Not identical lists.

**`unverified_fields` carries the guard (S3):** sorafuel "current production… describe a planned pilot"; electra "pre-order pipeline value is site-reported, not a price card"; cfs "capital raised is self-reported as 'over $2 billion'"; near-universal "revenue/headcount/cap-table not shown."

## Limits

All anchors are **site-attested and self-reported** (funding, orders, partners) — not
independently confirmed; only beta-team has linked SEC filings (not scraped). The ranking is
relative and defensible from the prose; it is not an audited stage classification. Cannot
prove a company is *not* further along than its site states.

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C2 | The 8 rank cleanly on maturity from milestones prose + `unverified_fields` | S1, S3 | Self-reported; relative not audited |
| C3 | Structured/headline fields (`description`, `business_model`, `offering_category`) are maturity-blind; `description` over-claims on pre-revenue cos | S2, S3 | n=8, single cohort |
