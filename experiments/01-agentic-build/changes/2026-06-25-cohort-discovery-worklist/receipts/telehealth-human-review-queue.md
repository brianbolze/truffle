# Telehealth Human Review Queue

Date: 2026-06-25
Stage: post-discovery, pre-scoring checkpoint
Status: Brian review applied; Juniper remains unresolved

## Why This Exists

Notion is too curated to supply a real junk set. The hard pollution gate is:

1. Brian's curated negatives.
2. Brian's review of generated candidates the store does not already know.

No candidate marked `tier_c_only` or `exclude` here may land in Tier A/B.

## Brian's Curated Negatives

These are hard pollution examples for this packet.

| Candidate | Domain | Reason | Expected handling |
| --- | --- | --- | --- |
| HealthEquity | healthequity.com | Benefits infrastructure, not a DTC therapeutics brand | `exclude` or `tier_c_only` |
| Promise Pharmacy | promisepharmacy.com | Pharmacy, not a DTC brand | `exclude` or `tier_c_only` |
| Absolute Rx | absoluterx.com | Pharmacy, not a DTC brand | `exclude` or `tier_c_only` |
| Dr. Telex | drtelex.com | Low-formidability / unclear DTC telehealth operator | `exclude` or `tier_c_only` |
| Jinfiniti | jinfiniti.com | Supplements-adjacent / not core DTC therapeutics | `exclude` or `tier_c_only` |
| MenMD | menmd.com | Low-formidability / narrow men's-health operator | `exclude` or `tier_c_only` |
| MintMD | mintmd.com | Low-formidability / unclear DTC telehealth operator | `exclude` or `tier_c_only` |
| Mint Medicine | mintmedicine.com | Low-formidability / unclear DTC telehealth operator | `exclude` or `tier_c_only` |

## Generated Candidates For Review

Please mark each row as one of: `worth_capture`, `tier_c_only`, `exclude`, or `unsure`.

| Candidate | Likely domain | Store resolution | Source signal | Initial bias | Brian mark |
| --- | --- | --- | --- | --- | --- |
| Ulo | tryulo.com | NOT in store | NY Post 2026 TRT list named Ulo alongside Hims, PeterMD, Ro, Hone, and MangoRX | likely `worth_capture` if verified as a DTC TRT clinic | `worth_capture`; Brian note: hair growth, but notable brand |
| MangoRX | mangorx.com | NOT in store | NY Post 2026 TRT lists named MangoRX as an online men's-health / TRT option | likely `worth_capture`; verify breadth/formidability | `tier_c_only` |
| Alloy Women's Health | myalloy.com | NOT in store | Women's Health menopause-care guide named Alloy with Midi and Evernow | likely `worth_capture` | `worth_capture` |
| Midi Health | joinmidi.com | no exact key; irrelevant fuzzy candidate only | Women's Health menopause-care guide named Midi Health | likely `worth_capture` | `worth_capture`; Brian note: absolutely worth capturing; at least should-have, arguably must-have |
| Evernow | evernow.com | NOT in store | Women's Health menopause-care guide named Evernow | likely `worth_capture` | `tier_c_only` |
| Mochi Health | joinmochi.com | no exact key; irrelevant fuzzy candidate only | NY Post GLP-1 / WeightWatchers alternatives list named Mochi Health | likely `worth_capture`; verify if domain is canonical | `worth_capture` |
| G-Plans Direct | gplansdirect.com | NOT in store | NY Post GLP-1 / WeightWatchers alternatives list named G-Plans Direct | `unsure`; may be plan/program-adjacent rather than strong DTC therapeutics | `tier_c_only` |
| BrightMeds | brightmeds.com | NOT in store | NY Post GLP-1 advertorial/newsroom surfaces named BrightMeds with Hers and Ro | `unsure`; source quality looks promotional, verify before promotion | `tier_c_only` |
| MyStart | mystart.com | NOT in store | NY Post GLP-1 affordability article centered on MyStart | `unsure`; source quality looks promotional, verify before promotion | `tier_c_only` |
| Juniper | myjuniper.com | NOT in store | Search/list signals surfaced Juniper / Eucalyptus as a telehealth operator | `unsure`; likely international boundary question | `unsure`; not marked by Brian in this pass |
| Eucalyptus Health | eucalyptus.health | NOT in store | Search/list signals surfaced Juniper / Eucalyptus as a telehealth operator | `unsure`; likely parent/company boundary question | `worth_capture`; Brian note: acquired by Hims recently |
| Zealthy | getzealthy.com | NOT in store | WIRED 2026 investigation identified Zealthy/FitRx/RoenRx/AMRx as problematic GLP-1 telehealth brands | likely `exclude` or `tier_c_only` | `exclude` |
| FitRx | fitrx.com | NOT in store | WIRED 2026 investigation tied FitRx to Zealthy | likely `exclude` or `tier_c_only` | `exclude` |
| RoenRx | roenrx.com | no exact key; fuzzy candidate `ro-co` only | WIRED 2026 investigation tied RoenRx to Zealthy | likely `exclude` or `tier_c_only` | `tier_c_only` |
| AMRx | amrx.com | NOT in store | WIRED 2026 investigation tied AMRx to Zealthy | likely `exclude` or `tier_c_only` | `exclude` |

## Brian Review Summary

- `worth_capture`: Ulo, Alloy Women's Health, Midi Health, Mochi Health, Eucalyptus Health.
- `tier_c_only`: RoenRx, MyStart, MangoRX, BrightMeds, G-Plans Direct, Evernow.
- `exclude`: Zealthy, FitRx, AMRx.
- unresolved / keep `unsure`: Juniper.

## Source Receipts

- New York Post, "Testosterone delivered to your door? We tapped experts on the best online TRT clinics of 2026": https://nypost.com/health/best-online-trt-clinics/
- New York Post, "Low T? We found the best sites to buy testosterone online in 2026": https://nypost.com/health/best-sites-to-buy-testosterone-online/
- Women's Health, "Where To Actually Find Good Perimenopause Care": https://www.womenshealthmag.com/health/a65268198/how-to-find-a-perimenopause-doctor/
- New York Post, "WeightWatchers files for bankruptcy - where you can still get GLP-1 weight loss drugs": https://nypost.com/2025/05/10/health/weightwatchers-files-for-bankruptcy-we-found-5-alternatives/
- New York Post, "Overpaying for Ozempic? Meet the online program making GLP-1 medication more affordable": https://nypost.com/2025/09/23/health/meet-the-company-making-glp-1-medication-more-affordable/
- WIRED, "I Was Scammed Buying GLP-1s Online. I'm Not Alone": https://www.wired.com/story/i-was-scammed-buying-glp-1s-online-im-not-alone
