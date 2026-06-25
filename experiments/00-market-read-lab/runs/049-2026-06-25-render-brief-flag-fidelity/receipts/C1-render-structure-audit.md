# Receipt - render-structure audit

Supports the read's claim that `scripts/render.py` preserves flag *content* but renders it
at lower salience than the hero `description` (C1–C4).

```yaml
receipt_type: local-file
created: 2026-06-25
evidence_mode: local-existing
source_grade: derived
source_family: local-store
spend_note: none
snippet_only: no
claim_ids_supported: [C1, C2, C3, C4]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source family / type | Grade | Spend | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|---|
| S1 | `scripts/present/brief.py`, `scripts/present/model.py` | repo @ 2026-06-25 | local-store / renderer source | primary (the code itself) | none | no | C1,C2,C3,C4 |
| S2 | `_out/briefs/{remedymeds,henrymeds,sorafuel,euclidpower,therabody,etsy}-com.html` | generated 2026-06-25 (`render.py … --no-fetch`) | local-store / generated artifact | derived | none | no | C1,C2,C4 |
| S3 | `store/{…}-com/profile.md` (panel) | 2026-05-31 … 2026-06-24 | local-store / dossier | primary | none | no | C1,C2 |

## Method

Ran `python scripts/render.py remedymeds henrymeds sorafuel etsy euclidpower therabody --no-fetch`
(`--no-fetch` = no remote logo/font fetch → zero network). Read `brief.py` + `model.py` in full
to map every flag → its render location. For each brief, grepped the generated HTML for the flag
content and counted `unverified_fields` `<li>` against the source `profile.md` list length.

## Evidence

- `unverified_fields` → "What we couldn't verify" `<li>` counts match source exactly:
  remedymeds 3/3, henrymeds 3/3, sorafuel 2/2, euclidpower 2/2, therabody 4/4, etsy 4/4.
- Tab state: `id="t-profile" checked` (default); trust tab is index 3 (`data-t="trust"`).
  `_provenance_html` (`brief.py:190-222`) renders `unverified_fields` + `site_notes` only inside
  that 4th tab.
- `_profile_panel` (`brief.py:259-263`): `overview` + `strategic read` `open_=True`;
  `credibility & proof` (the "self-reported" prose) `open_=False` (collapsed).
- Hero: `brief.py:381` renders `description` as `hero-desc` at 21–29px display, no adjacent flag.
  sorafuel hero-desc = "Produces sustainable aviation fuel by converting ambient air, water, and
  renewable electricity…"; the pilot/maturity guard is `store/sorafuel-com/profile.md:96-98`.
- Price-vis chips (`brief.py:93-96`): therabody 57 `vis-published`; remedymeds 3 `vis-published`
  + 3 `vis-on-request` — in the tab-2 roster only.

## Limits

Audits the single-company HTML brief relay only (`brief.py`). Does not cover the comparison sheet
(`compare.py`), the corpus index (`index.py`), or a delegated agent reading `profile.md` directly —
those relays could carry different salience. Does not measure real reader behavior; "5-second path"
is the default-open DOM path (hero + auto-open Overview/Strategic read), an analytic proxy for a
fast read, not an observed one.

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C1 | Hero renders `description` at top salience, unguarded | S1,S2,S3 | salience is a layout fact; "unguarded" = no flag in the same view, not that no flag exists in the file |
| C2 | `unverified_fields` + `site_notes` render only in tab 4 | S1,S2 | reachable in 1 click; off the *default* path, not absent |
| C3 | Default Profile tab collapses the proof ("self-reported") section | S1 | expandable; collapsed ≠ dropped |
| C4 | Price-vis token survives as a roster chip (tab 2) | S1,S2 | only where `offerings.md` exists |
