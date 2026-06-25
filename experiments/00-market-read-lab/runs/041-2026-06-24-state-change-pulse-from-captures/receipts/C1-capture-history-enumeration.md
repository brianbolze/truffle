# Receipt C1 — capture-history enumeration

- **Source:** local store; `store/*/captures/` directory listing.
- **Store clock:** captures dated 2026-05-30 .. 2026-06-17.
- **Source type / grade:** local / primary (filesystem state).
- **Source family:** store-internal.
- **Spend:** none (local).
- **Snippet-only:** no.
- **Claims supported:** C1 (21/145 domains retain 2+ dated captures; capture_at vs newest folder).

## Method
`for d in store/*/captures; do count top-level dirs matching ^YYYY-MM-DD$ (exclude _archive); keep >=2.`

## Result — 21 domains with 2+ top-level dated capture folders
| domain | dated capture folders | profile captured_at | newest folder |
|---|---|---|---|
| agelessrx-com | 05-31, 06-03, 06-04 | 2026-05-31 | 06-04 |
| belmarpharmasolutions-com | 06-02, 06-13 | (none in FM) | 06-13 |
| blueowl-com | 05-30, 05-31 | 2026-05-30 | 05-31 |
| eden-health | 05-30, 05-31, 06-03 | 2026-05-30 | 06-03 |
| functionhealth-com | 06-01, 06-04, 06-13, 06-16 | 2026-06-01 | 06-16 |
| gethealthspan-com | 06-04, 06-16 | 2026-06-04 | 06-16 |
| getopt-com | 06-04, 06-05, 06-16 | 2026-06-04 | 06-16 |
| gogeviti-com | 06-02, 06-03, 06-04 | 2026-06-02 | 06-04 |
| goodlifemeds-com | 06-04, 06-15, 06-16 | 2026-06-04 | 06-16 |
| hellopepti-com | 06-07, 06-09, 06-13 | 2026-06-09 | 06-13 |
| hydramed-com | 06-04, 06-05 | 2026-06-04 | 06-05 |
| joinfridays-com | 06-04, 06-16 | 2026-06-04 | 06-16 |
| keeps-com | 06-04, 06-05 | 2026-06-04 | 06-05 |
| maximustribe-com | 05-31, 06-03, 06-15 | 2026-05-31 | 06-15 |
| millspharmacy-com | 06-09, 06-13 | 2026-06-09 | 06-13 |
| mydrhank-com | 06-03, 06-04 | 2026-06-03 | 06-04 |
| redantler-com | 06-12, 06-14 | 2026-06-12 | 06-14 |
| remedymeds-com | 06-01, 06-03, 06-04 | 2026-06-01 | 06-04 |
| standishspring-com | 06-14, 06-17 | 2026-06-14 | 06-17 |
| vitalityrx-com | 06-04, 06-14 | 2026-06-04 | 06-14 |
| warbyparker-com | 06-04, 06-14 | 2026-06-04 | 06-14 |

Denominator partial: top-level dated folders only; `_archive/` and `signals/` excluded.
Profile captured_at is earlier than the newest folder for nearly all — see C2/C6 for why
that is NOT synthesis lag.
