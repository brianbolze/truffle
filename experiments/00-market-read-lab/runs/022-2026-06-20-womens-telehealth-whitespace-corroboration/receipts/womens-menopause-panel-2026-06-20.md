# Receipt - women's-menopause external panel + store reconciliation

Supports the read's claim that a dedicated women's-menopause/HRT segment exists in the
market and is almost entirely uncaptured (run 020's selection-bias confirmed live).

```yaml
receipt_type: source-panel
created: 2026-06-20
evidence_mode: bounded-live
source_grade: secondary   # listicles secondary; SERP direction-finding; store reconciliation derived
source_family: SERP/listicle + owned/official (brand SERP results) + local-store
spend_note: paid-credit   # 14 Firecrawl credits total (2 search @2 + 2 scrape @5)
snippet_only: no          # named sets extracted from full list pages, not snippets
claim_ids_supported: [C1, C2, C3, C4, C5]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source family / type | Grade | Spend | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|---|
| S1 | https://www.everydayhealth.com/services/online-menopause-treatment/ | 2026-06-20 | SERP/listicle (affiliate/SEO) | secondary | paid-credit (5) | no | C1, C3 |
| S2 | https://www.theflowspace.com/reproductive-health/menopause/online-menopause-treatment-2941951/ | 2026-06-20 (page modified 2026-04-27) | SERP/listicle (women's media) | secondary | paid-credit (5) | no | C2, C3 |
| S3 | store/*/telehealth.md (grep `^audience: *women`; market-name token match) | store clocks ~2026-05-30 → 2026-06-20 | local-store | derived | none | no | C4 |
| S4 | firecrawl_search: "best menopause telehealth companies 2026"; "best online menopause and women's hormone (HRT) telehealth platforms 2025" | 2026-06-20 | search results | direction-finding | paid-credit (2+2) | yes (titles/descriptions only) | C5 |

## Method

1. **SERP (S4):** two firecrawl_search queries for best-of menopause/HRT telehealth. Used
   only to (a) discover the two authoritative listicles and (b) confirm head brands surface
   as *direct brand results* (Midi, Evernow, Gennev, Elektra, Winona, Alloy). Titles/
   descriptions are leads, not decision-grade — used as corroboration, never as the named set.
2. **Listicle named-set extraction (S1, S2):** firecrawl_scrape with JSON schema over the
   two full list pages; pulled every named brand verbatim. Two independent authoritative
   sources chosen per the run-012 rule (cross-source recurrence on ≥2 authoritative lists is
   the only trustworthy "default" sub-signal; a single list is affiliate-confounded).
3. **Cross-source recurrence (C3):** set intersection S1 ∩ S2. **Name-variant
   normalization applied before intersection:** a trailing " Health" suffix is treated as
   equivalent (Allara / Allara Health; HerMD / HerMD Health). The exact-string intersection
   is 7 (Evernow, Gennev, Midi Health, PlushCare, Stella, Winona, Wisp); the 2 normalized
   matches bring it to **9**. (Loop-2 verifier flagged that the 9 was otherwise
   non-reproducible from the verbatim sets.)
4. **Store reconciliation (C4):** `grep -rlE "^audience: *women" store/*/telehealth.md`
   for the women-leaning cohort (5); token-match the 9 cross-recurrence names against
   `ls store/*/`.

## Evidence

**S1 (Everyday Health, 17):** Midi Health, Winona, PlushCare, Brightside Health,
WeightWatchers Menopause, Sesame Care, Nurx, Hone Health, Wisp, Stella, Allara, HerMD,
Versalie, Gennev, Respin, Evernow, Elektra Health.

**S2 (Flow Space, 15):** Winona, Midi Health, Wisp, Alloy, PlushCare, Evernow, Allara
Health, Joi + Blokes, Interlude, Stella, Gennev, HerMD Health, Pandia Health, Tia Health,
Intimate Rose.

**S1 ∩ S2 (C3), 9:** Midi Health, Winona, Wisp, PlushCare, Evernow, Allara, Stella,
Gennev, HerMD.

**Store reconciliation (C4):**
- Women-leaning store cohort (5): brellohealth-com, effecty-com, innerbalance-com,
  nurx-com, remedymeds-com.
- Of the 9 cross-recurrence brands, store token-match hits: `hellowisp-com` (Wisp, captured
  `all-genders`). The other 8 (Midi, Winona, PlushCare, Evernow, Allara, Stella, Gennev,
  HerMD) → no store directory.
- Other store hits among listicle names (not in the cross-recurrence head): `honehealth-com`
  (Hone, S1 only, all-genders), `nurx-com` (Nurx, S1 only, women-only), `joiandblokes-com`
  (Joi+Blokes, S2 only, all-genders).

## Limits

- Two listicles = a **coverage radar, not a market census**. Both monetize referrals
  (affiliate/SEO); inclusion and order are commercially influenced. Only the **cross-source
  recurrence head** is treated as a strong signal; single-source names are nominees.
- **Membership only.** No pricing, offer, demand, size, or liveness-beyond-SERP claim. A
  brand surfacing in a listicle + SERP is "named and plausibly live," not "captured."
- **Token-match reconciliation** could miss a store brand under a different domain string
  (e.g. a renamed/parent domain). Manual scan of `ls store/*/` for menopause-name tokens
  found no additional hits, but absence here = "not found by token match," not "proven
  absent."
- Brand audience framing is read from list descriptions + SERP, not a captured `audience`
  field; a capture run is required to confirm each brand's front-door positioning.

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C1 | Everyday Health names 17 menopause platforms (set listed) | S1 | affiliate/SEO listicle; secondary |
| C2 | Flow Space names 15 menopause telehealth companies (set listed) | S2 | women's-media listicle; secondary |
| C3 | 9 brands recur across both authoritative listicles | S1 ∩ S2 | 2 sources only; head robust, margins not |
| C4 | 8 of 9 cross-recurrence brands absent from store; store women-leaning 5 nearly disjoint from market menopause set | S3 | token-match; "not found" ≠ "absent" |
| C5 | Head brands (Midi/Evernow/Gennev/Elektra/Winona/Alloy) surface as direct brand SERP results | S4 | direction-finding; corroboration only |
