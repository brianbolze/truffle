# Receipt - Store ownership-edge map (parent / owns)

Supports the consolidation map: every non-empty `parent`/`owns` edge in the store, which
edges join to a captured profile, and the absence-discipline distribution.

```yaml
receipt_type: store-query
created: 2026-06-20
evidence_mode: store-only
source_grade: derived
source_family: local-store
spend_note: none
snippet_only: no
claim_ids_supported: [C1, C2, C3, C4, C5, C6, C7, C8]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source family / type | Grade | Spend | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|---|
| S1 | `store/*/profile.md` frontmatter `parent:` / `owns:` (135 dirs, 126 with the fields) | store clock per file (capture dates vary) | local-store / owned-official frontmatter | derived | none | no | C1–C8 |

## Method

- `grep "^parent: \[[^]]"` and `grep "^owns: \[[^]]"` over `store/*/profile.md` to pull all
  non-empty edges, preserving the inline provenance `#` comments.
- For each referenced target domain, tested existence of `store/<slug>/` (domain→slug = `.`→`-`).
- Counted `parent: []` total / with-comment / bare to gauge absence discipline.
- Checked bidirectional reconciliation: does a child's `parent` target list the child in its own `owns`, and vice-versa, when both are captured.

## Evidence

**Non-empty `parent:` edges (child → parent), 13 brands:**

| Child (captured) | Parent value | Parent captured? | Grade of disclosure |
|---|---|---|---|
| aws-amazon-com | amazon.com | no | explicit (subsidiary) |
| onemedical-com | amazon.com | no | explicit attestation ("/about-us") |
| keeps-com | thirtymadison.com | no | explicit (footer/legal route) |
| nurx-com | thirtymadison.com | no | explicit |
| niagenplus-com | niagenbioscience.com | no | explicit (rebrand) |
| truniagen-com | niagenbioscience.com | no | explicit (nav "Our Parent Company") |
| cartier-com | richemont.com | no | **inferred / STRAIN** |
| alange-soehne-com | richemont.com | no | **inferred / STRAIN** |
| rexmd-com | lifemd.com | **YES** | explicit (FAQ) |
| delighted-com | qualtrics.com | **YES** | explicit |
| hims-com | "Hims & Hers Health, Inc." | n/a (name, no domain) | explicit |
| openai-com | openaifoundation.org | no | explicit |
| redantler-com | "Red Antler Group" | n/a (name) | explicit |

**Non-empty `owns:` edges (parent → children), 15 brands:** alpha-sense (Tegus/Sentieo/BamSEC/Canalyst, names), casio (gshock.casio.com, edifice-watches.com), eden-health (edenhealthclubs.com, edenpharmacy.com), etsy (reverb.com, depop.com), euclidpower (Thresh Power), ford (fordpro.com), functionhealth (ezra.com), lifemd (rexmd.com, shapiromd.com, navamd.com), marekhealth (marekdiagnostics.com), nike (converse.com, Jordan Brand, NikeSKIMS), qualtrics (Press Ganey Forsta), tryshed (shednutrition.com, shedsupplements.com), twilio (sendgrid.com, segment.com), uber (ubereats.com, uberfreight.com, uberhealth.com), upwork (go-lifted.com).

**Joinability test — referenced targets present in store:** `qualtrics.com`, `lifemd.com`, and `rexmd.com` of ~21 distinct referenced domains. All others absent.

**Reconciliation:**
- `lifemd ↔ rexmd`: rexmd `parent:[lifemd.com]` AND lifemd `owns:[rexmd.com,...]` → **only fully captured, bidirectionally reconciled edge.**
- `delighted → qualtrics`: child points up, but qualtrics `owns:["Press Ganey Forsta"]` only — **does not list delighted** (one-directional / unreciprocated, even though both captured).

**Concentration — parents linked to ≥2 captured children:** amazon (aws, onemedical), thirtymadison (keeps, nurx), niagenbioscience (niagenplus, truniagen), richemont (cartier, alange-soehne — both inferred). All four multi-child parents are **uncaptured**.

**Absence discipline:** `parent: []` = 109 total; **6** carry a distinguishing comment (IDEO "independent"; Rugiet "operates independently"; Swatch "not stated, see unverified_fields"; Notion "operating co not parent"; alliahealth "not stated"; +1), **103 are bare** (no comment).

## Limits

- Frontmatter records only what each captured site discloses → the map is a **floor**, not a census of true ownership.
- Corpus is selection-biased (telehealth-heavy + an ad-hoc set of general brands), so concentration counts are not a market structure.
- "Inferred/STRAIN" parents (richemont ×2) are not primary attestations.
- Cannot prove a `parent: []` brand is independent vs merely undisclosed/uncaptured (103/109 are silent).

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C1 | 13 captured brands disclose a non-empty `parent`; 15 disclose non-empty `owns` | S1 | floor; disclosed-only |
| C2 | Only 3 of ~21 referenced targets (qualtrics, lifemd, rexmd) are captured | S1 | |
| C3 | `lifemd ↔ rexmd` is the only fully-captured bidirectionally-reconciled edge | S1 | |
| C4 | `delighted → qualtrics` is captured-but-unreciprocated | S1 | |
| C5 | 4 parents link ≥2 captured children; all 4 are uncaptured | S1 | richemont pair is inferred |
| C6 | 103 of 109 `parent: []` are bare (no independent-vs-unknown comment) | S1 | |
| C7 | Cleanest ownership facts come from general public companies (Amazon/Etsy/Nike/Uber/Twilio/Ford/Casio) | S1 | still dangling — siblings uncaptured |
| C8 | The convention CAN distinguish independent vs not-stated (6 commented empties) but rarely does | S1 | |
