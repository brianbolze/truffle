# Receipt - Wayback tenure panel (captured signal)

Derived panel of every captured Wayback signal in the store, with a snapshot-density
diagnostic, supporting the offer-tenure read and its domain-reuse caveat.

```yaml
receipt_type:          store-query
created:               2026-06-19
evidence_mode:         store-only
source_grade:          derived
snippet_only:          no
claim_ids_supported: [C1, C2, C3, C4, C5, C6]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source type | Grade | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|
| S1 | `store/*/signals/wayback/<keyword>/<latest>.json` (47 domains, 55 distinct (domain,keyword) captures) | captured 2026-06-15 / -16 | store file (Wayback CDX capture) | derived | no | C1–C6 |
| S2 | `store/*/telehealth.md` frontmatter (`anchor_category`, `value_chain_role`) | store clock (captures ~May–Jun 2026) | store file | derived | no | C3 |

## Method

- Globbed `*/signals/wayback/*/*.json`; kept the latest capture per (domain,keyword) by
  `captured_at`. 74 raw files → 55 distinct captures across 47 domains.
- Read per-capture `first_seen`, `first_seen_confidence`, `tenure_days`, `snapshot_count`,
  `status_trail`, `input.url`. Split captures into **root** (homepage `input.url`) vs
  **offer/blog** (a specific product or article path).
- Joined `anchor_category` + `value_chain_role` from each domain's `telehealth.md`.
- **Reuse diagnostic:** for each root capture with `first_seen < 2020`, counted snapshots
  taken pre-2020 vs 2024+. A domain with very sparse pre-2020 archival but dense recent
  archival is a *candidate revived/reused domain* (old `first_seen` ≠ current brand age).

## Evidence

- Population: 55 captures / 47 domains. **49 scorable** (`tenure_days` present); 48 `measured`,
  1 `provisional` (honehealth mens-sermorelin, 38d), 6 `insufficient` (no `first_seen`).
- URL type: **39 root, 16 offer/blog** (10 of the offer/blog are scorable; 6 insufficient).
- Root tenure spread: **0.3y (home-medvi-org) → 27.4y (noom-com)**; **27 root domains** have
  `first_seen < 2020` (after de-duping the two domains with two root captures each, onemedical
  and eden-health — the raw glob counts them twice; deduped = 27).
- Offer-page tenure (scorable): 38d (honehealth mens-sermorelin) → 992d (hims hard-mint ED).
- **Reuse diagnostic, root domains first_seen < 2020 (n=27), pre-2020 vs 2024+ snapshots:**
  - Sparse-then-dense (revival candidates): telolife (9/27), remedymeds (7/81), ivyrx (7/482),
    goodlifemeds (13/60), effecty (20/42), directmeds (23/35), getopt (21/73), mylifeforce
    (22/73), vitalityrx (22/41), malemd (22/66), rugiet (2/46), tryshed (4/56), trtnation
    (2/107), functionhealth (1/250), mydrhank (1/76), invigormedical (4/78), eden-health (1/3),
    rexmd (16/312, snapshots truncated — recent bulk dominates).
  - Dense pre-2020 (continuous, age more credible): noom (463 pre-2020), nurx (349), onemedical
    (500), bluechew (184), defymedical (179), ro.co (102), lifemd (76), innerbalance (50),
    hormonemd (37).
- **Structural anachronism:** GLP-1-anchored roots with pre-2021 `first_seen` — telolife (2004),
  ivyrx (2004), remedymeds (2004), goodlifemeds (2006), effecty (2006), directmeds (2008),
  ro.co (2013), tryshed (2014), eden-health (2018) — and online-ED-anchored roots dated 2001
  (rexmd, bluechew). GLP-1 weight-loss telehealth (~2021+) and online-ED telehealth (~2017+)
  post-date those domain origins, so the `first_seen` cannot be the *current brand's* operating
  age. (noom is GLP-1-anchored and pre-2021 but excluded — it predates GLP-1 as a continuously-run
  weight company; mydrhank 2019 is borderline.)

## Limits

- Captured floor: 47 of 135 store profiles (46 of 54 telehealth) have a Wayback signal. Not a
  census; "newest/oldest" is within the captured slice only.
- Wayback CDX coverage is itself uneven (crawler reach, robots.txt, truncation: `ivyrx`,
  `noom`, `onemedical` are `snapshots_truncated: true`, so their snapshot counts are floors).
- The reuse diagnostic ("REVIVED?") is a *derived heuristic* from snapshot density, not proof of
  ownership change. It flags where root `first_seen` is unreliable as brand age; it does not
  establish the true brand founding date (that would need external/registration evidence — out
  of scope, store-only).
- `tenure_days` = `first_seen → last_seen` on one URL; it says nothing about traffic, revenue, or
  quality. `snapshot_count` reflects archival frequency, not popularity.

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C1 | 47 domains / 55 captures have a Wayback signal; 49 scorable; this is the first read to consume it | S1 | captured floor, not census |
| C2 | Captures are mostly homepages (39 root) + a minority of offer/blog pages (16) | S1 | URL type read from `input.url` |
| C3 | Root tenure spans 0.3y–27.4y; oldest-dated roots skew to GLP-1/ED/hormone DTC brands | S1+S2 | join 1:1, no resolver needed |
| C4 | Root `first_seen` overstates brand age for revived/reused domains (sparse-then-dense pattern) | S1 | heuristic, not proof of reuse |
| C5 | GLP-1/online-ED roots dated pre-category (2001–2013) cannot reflect current-brand age | S1+S2 | structural/internal-consistency argument |
| C6 | Offer/blog-page tenure is the truer brand-era marker but is captured for only ~10 brands | S1 | thin coverage |
