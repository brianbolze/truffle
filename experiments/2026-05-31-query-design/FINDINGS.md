# Query-design probe — what the CLEAN corpus needs from QUERYING.md

*2026-05-31. Probed the fresh 11-company post-wipe store (commit `3cc2dc2`+) to design
`QUERYING.md` from real data — deliberately **not** reusing the
[consumption experiment](../2026-05-31-consumption/FINDINGS.md)'s scripts/recs, which were
written against the drifted experiment corpus and are now partly obsolete. Probes were inline
`grep`/`rg` + one `yaml.safe_load` pass over all frontmatter; no helper built.*

Corpus: 6 telehealth cohort (hims, honehealth, eden, gethealthspan, getpetermd, maximustribe)
+ 5 diverse outliers (airbnb=marketplace, stripe=fintech, blueowl=investor/holding, notion=SaaS,
nike=apparel).

## TL;DR

- **The clean corpus changes the rung-2 answer.** The consumption test's headline finding
  (contract↔corpus drift) and its #4 (capture-meta grep-noise) are **gone**: `schema_version`
  11/11, every closed-set value on-contract, engine-commentary 0/11 profiles (vs. piles before),
  `site_notes` trimmed (only 1 of 5 `$`-lines in hims is capture-meta now, not the old 36KB blob).
  So `QUERYING.md` does **not** need the drift-fallback `facets`/`term` helper — the corpus now
  means what the contract says.
- **Query *shape* picks the tool — that is the whole design.** `rg`/`grep` = **locate**
  (line-oriented, verbatim, cheap); a **~5-line YAML parse** = **structured query** (group /
  filter / relate). Frontmatter is **valid YAML 11/11**, so a parse is comment-, whitespace-,
  and order-proof where `grep | uniq` is not.
- **`grep | uniq` group-by is unreliable here — proven.** Trailing alignment-padding before the
  inline `# STRAIN` comments (`Multi-product` ≠ `Multi-product␣␣`) and non-canonical multi-select
  order (`[B2C, B2B]` vs `[B2B, B2C]`) both fragment the counts. The YAML parse returns the
  correct distribution (7 Subscription + 1 each); the naïve grep did not.
- **Cross-brand price is intra-cohort-only and manual.** The diverse corpus proves "price" isn't
  one comparable quantity: `$/mo` (telehealth, Notion per-seat), take-rate `%` (Stripe, Airbnb),
  AUM fees (Blue Owl, off-site), per-night/per-guest snapshot (Airbnb listings). Cross-*type* price
  comparison is meaningless; even within telehealth, units fragment (membership-stacked,
  first-month, billing cadence). No numeric/range price query is possible until `offerings.md`
  ships a structured price+unit.

## The two-tier access model (the core recommendation)

| Query shape | Tool | Why — grounded |
|---|---|---|
| Locate / verbatim / "does X appear, where" | `rg` (available) or `grep -r` | line-oriented + cheap (whole corpus is 1,429 ln / 115 KB); `captures/*/*.md` preserve verbatim primary source |
| Filter / group / aggregate / relate | `yaml.safe_load(frontmatter)` (~5 lines, PyYAML 6.0.2 present) | parses 11/11; immune to the comment/trailing-space/ordering that fragment `grep \| uniq`; lists come back as lists (membership tests are trivial) |

## Per-path recipes (grounded)

| Path | Recipe | Ceiling / trap |
|---|---|---|
| **Point read** | `read store/<domain>/profile.md` — one ~10 KB file | none; body sections map 1:1 to the ask, **all entity types** (verified incl. investor/marketplace) |
| **Filter / group** | parse frontmatter → query the dict; **list-membership** for `target_market`/`offering_category` | never `grep\|uniq`; never equality-match a multi-select (order isn't canonical) |
| **Relations** | read `parent`/`owns`: a **domain slug** is joinable, a **quoted name** is not (flagged per Rule B) | no SQLite yet — the corpus has ~no internal edges to JOIN (eden→edenhealthclubs/edenpharmacy is the only one, and those aren't captured) |
| **Cross-brand pricing** | **intra-cohort only**: `rg` price lines across the cohort's profiles → reconcile units **by hand** | cross-*type* is meaningless; no numeric/range ("under $200/mo"); units fragment even within a cohort |
| **Primary source** | `rg '<phrase>' store/<domain>/captures/*/*.md` | check `key_pages` + Provenance + `unverified_fields` to tell "not captured" from "not present" before trusting a negative |

## Coverage is now legible (the consumption test's open problem #5)

`key_pages` (6–13 per profile), `unverified_fields` (1–5), and a Provenance section are present on
**11/11** — so a consumer *can* distinguish a real gap from a capture gap. Worth an explicit recipe
line: before reporting "X doesn't do Y," check these three.

## Don't build yet

- **No `facets`/`term` helper.** The 5-line parse covers group/filter at N=11; a helper earns its
  place only when N strains plain reads or `offerings.md` adds a structured price to aggregate.
- **No SQLite.** Relations are clean domain-slugs now, but there's nothing to JOIN across yet.

## Surfaced for BACKLOG (schema is frozen — not acting now)

- **Single-select judgment fields are the least reproducible.** Nike `primary_industry` went
  Consumer Goods (experiment capture) → **Sports & Recreation** (fresh) across two captures of the
  *same company*; Notion landed `portfolio_shape: Flagship + companions` where the doc's Linear
  example is `Single`. Query these with awareness — and revisit whether `primary_industry` (21
  values, optional, often near-redundant with `offering_category`) earns its Tier-0 slot.
- **The inline `# STRAIN` comment** is great for a human reading one hit but is exactly what breaks
  `grep | uniq` — acceptable once `QUERYING.md` routes grouping through the parser, but note the cost.
- **Faint Rule-A residue:** Stripe's body says "among the most polished sites in the corpus" — a
  cross-capture comparative. Decide whether comparative ranking is allowed under describe-not-engine.
