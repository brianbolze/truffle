# Receipt - behavioral-health coverage-radar panel

Supports the membership claim that a dedicated behavioral/mental-health telehealth segment
exists and is entirely absent from the captured corpus.

```yaml
receipt_type: source-panel
created: 2026-06-20
evidence_mode: bounded-live
source_grade: secondary   # listicles secondary; store diff derived; SERP direction-finding
source_family: SERP/listicle
spend_note: paid-credit   # 14 credits gross, 2 refunded via search feedback = 12 net
snippet_only: no          # named sets pulled from full list pages via JSON scrape
claim_ids_supported: [C1, C2, C3, C4, C5]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source family / type | Grade | Spend | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|---|
| S1 | https://www.forbes.com/health/mind/best-online-therapy/ | captured 2026-06-20; page modified 2026-05-07 | SERP/listicle (affiliate, "Most Popular = affiliate selections") | secondary | paid-credit (5) | no | C1, C3 |
| S2 | https://www.healthline.com/health/mental-health/online-therapy-that-takes-insurance | captured 2026-06-20; page modified 2026-05-26 | SERP/listicle (affiliate/SEO) | secondary | paid-credit (5) | no | C2, C3 |
| S3 | `ls store/` (135 domains) + `grep store/*/telehealth.md` (54 packs) | store clock 2026-06-20 | local-store | derived | none | no | C4 |
| S4 | firecrawl_search ×2 ("best online therapy and psychiatry telehealth 2026"; "best online mental health services 2026") | 2026-06-20 | search result | direction-finding | paid-credit (2+2, 1+1 refunded) | yes | C5 |

## Method

1. **Store floor:** `grep -rliE "anchor_category: *(mental|behavioral|psych)" store/*/telehealth.md`
   → 0 of 54. `anchor_category` distribution confirms an Rx-commerce/hormone-shaped corpus.
2. **Panel discovery:** 2 firecrawl_search queries surfaced Forbes Health + Healthline as the
   two authoritative listicles (plus brand-owned Grow Therapy blog and direct brand results
   Cerebral/Talkspace/Brave Health). Both searches rated `good`; 1 credit refunded each.
3. **Named-set extraction:** JSON-scraped S1 and S2 with a `named_brands` schema for verbatim
   sets. Hand-excluded 7 insurance *payers* the S2 extractor swept in (Cigna, Anthem, UHC,
   Aetna, Humana, BCBS, Kaiser — not therapy platforms).
4. **Cross-source intersection (C3):** names on *both* S1 and S2 = BetterHelp, Talkspace,
   Brightside Health, Doctor on Demand, MDLive (5). Grow Therapy noted as likely-6th via S2
   og:description, held as direction-finding.
5. **Store diff (C4):** token-matched the 5-head + full union against `ls store/` and against
   `telehealth.md` bodies. 0 directory matches, 0 body mentions. `standishspring-com` was the
   only `ls` token hit (on "spring") and is a false positive — not a behavioral brand.
6. **Stop rule fired:** ">=2 authoritative listicles yield a cross-recurrence set and the
   store diff is computable" — met after S1/S2. No third listicle or owned-page read needed.

## Evidence

- **S1 verbatim (10):** Grow Therapy, BetterHelp, Talkspace, Brightside Health, Amwell,
  Teladoc Health, Sesame Care, LiveHealth Online, Doctor on Demand, MDLive. og note:
  "ranking represents therapy and psychologist visits only — psychiatry and medication
  management … as a separate service"; "Most Popular is calculated from the number of times
  each affiliate product was selected by Forbes Health readers."
- **S2 verbatim platform set (5, post-exclusion):** Brightside Health, Doctor on Demand,
  Talkspace, BetterHelp, MDLIVE. (Extractor also returned 7 insurer names — excluded.)
- **C3 intersection (5):** BetterHelp, Talkspace, Brightside Health, Doctor on Demand, MDLive.
- **C4 store diff:** grow/betterhelp/talkspace/brightside/amwell/teladoc/sesame/livehealth/
  doctorondemand/mdlive/cerebral/talkiatry → all `<none>` in `ls store/`; body grep = 0/54.

## Limits

- **Coverage radar, not census:** 2 affiliate-monetized listicles; only the cross-source head
  is decision-grade (MRL-008 listicle-inclusion confound). Tails are affiliate-confounded.
- **Membership, not size:** "store-absent" = real + uncaptured, NOT large/dominant. No
  demand/share/revenue claim.
- **Therapy-led panel:** both lists center talk-therapy; the psychiatry/medication-management
  sub-lane (Cerebral, Talkiatry) is under-named by the panel, filled only at SERP grade.
- **Token-match absence** = "not found by directory + body grep," not "proven absent" under a
  renamed/parent domain (manual `ls` scan found no extra hits).

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C1 | Forbes names a 10-brand best-online-therapy set (2026) | S1 | affiliate-ordered; therapy-only scope |
| C2 | Healthline names a 5-platform best-online-therapy-with-insurance set (2026) | S2 | 7 insurer names excluded by hand |
| C3 | 5 brands recur across both authoritative listicles (decision-grade head) | S1∩S2 | Grow Therapy a likely 6th, direction-finding |
| C4 | 0 of the head/union are in the store (135 domains, 54 packs) | S3 | token-match floor, not proof-of-absence |
| C5 | A live, dense behavioral-telehealth market exists beyond the listicle heads | S4 | direction-finding (SERP titles) |
