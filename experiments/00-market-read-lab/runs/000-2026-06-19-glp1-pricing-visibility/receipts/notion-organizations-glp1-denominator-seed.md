# Notion Organizations GLP-1 Denominator Seed

Date: 2026-06-19

## Method

Goal: build a quick Organizations-table denominator for rows where:

- `Categories Served` includes `Weight-GLP1`, or
- `What they lead with` is `GLP-1 / Medical Weight Loss`, or
- `Product Categories` includes `GLP-1 / Medical Weight Loss`.

Structured Notion SQL was unavailable in this session (`notion-query-data-sources` returned
tool-not-found), so this is a **seed list**, not a formal exhaustive export. Inputs used:

- Organizations database fetch for schema.
- Product Categories page `GLP-1 / Medical Weight Loss` for relation target.
- Organizations searches for `Weight-GLP1`, `GLP-1 / Medical Weight Loss`,
  `semaglutide tirzepatide`, and named sanity checks.

Run 0 should improve or verify this denominator before treating it as ground truth.
This list is **not exhaustive**; it reflects what was reachable from the Notion
Organizations table and available connector paths during this setup pass.

## Working Denominator

Count: 34 primary Organizations rows.

| Organization | Notion URL |
|---|---|
| AgelessRx | https://app.notion.com/p/34b84b6d1f4981778801f2a24117dae7 |
| Alt Rx | https://app.notion.com/p/36b84b6d1f4980bab0edef3c37423d6e |
| Blokes | https://app.notion.com/p/34b84b6d1f4981e99f07e4341b8d96aa |
| Citizen Meds | https://app.notion.com/p/35784b6d1f4980c99e3accef0752fe3d |
| Defy Medical | https://app.notion.com/p/34b84b6d1f4981e3acd4e3f74a46a617 |
| Dr Hank | https://app.notion.com/p/35984b6d1f4980a99c91fca646989c2b |
| Effecty | https://app.notion.com/p/35784b6d1f4980ff9d4ffcb1e65479ad |
| Fridays | https://app.notion.com/p/35984b6d1f49802fa2ffc17776c1a31b |
| Gala | https://app.notion.com/p/35784b6d1f4980c09f29eb870f5691d9 |
| GoodRx | https://app.notion.com/p/35984b6d1f4980ab89e1c1d3f9acd159 |
| Henry Meds | https://app.notion.com/p/34b84b6d1f498157b13cfc8c9c4ad4a2 |
| Hims & Hers | https://app.notion.com/p/0cfe47343e4b4aff89a3bb3b4db42fb7 |
| Hone Health | https://app.notion.com/p/95f4651b937c419fbcd5a9683adf0bad |
| HormoneMD | https://app.notion.com/p/35984b6d1f4980f29204f52bb68d42ea |
| Invigor Medical | https://app.notion.com/p/34b84b6d1f4981cda01de76ec19d62e6 |
| Ivy Rx | https://app.notion.com/p/34b84b6d1f4981ba8df8ccc4741ea1bd |
| Kingsberg Medical | https://app.notion.com/p/34b84b6d1f4981b29b66e36e40dea743 |
| Klarity Health | https://app.notion.com/p/35984b6d1f49807784a6e0e998c56bda |
| LifeMD | https://app.notion.com/p/37484b6d1f4980e18db3c057faec7041 |
| Lifeforce | https://app.notion.com/p/34b84b6d1f4981c4b767fe3ee5f7feb1 |
| Max Life | https://app.notion.com/p/35784b6d1f498017a696ce76c426fb74 |
| Maximus Tribe | https://app.notion.com/p/34b84b6d1f4981ffaff0d98634066dbb |
| Medvi | https://app.notion.com/p/35484b6d1f49800c8cd5ce224032cfd4 |
| Mens | https://app.notion.com/p/35984b6d1f4980d9b238df14799596e3 |
| Noom Med | https://app.notion.com/p/35d84b6d1f4980ba9024da6971e707b1 |
| omzo | https://app.notion.com/p/36084b6d1f4980b5989aeb36eec6495c |
| One Medical (Amazon) | https://app.notion.com/p/37484b6d1f4980ba8aa6e989dc6be5ed |
| ProHealth | https://app.notion.com/p/35884b6d1f4980c3baadc6802ffa9c87 |
| Remedy Meds | https://app.notion.com/p/35984b6d1f49809e90dbeb3bb3f7142c |
| Ro | https://app.notion.com/p/34b84b6d1f4980d09a6fd48eb407c38c |
| Shed Rx | https://app.notion.com/p/35784b6d1f4980eb9d49f379a929af77 |
| TMates | https://app.notion.com/p/35d84b6d1f4980859f65f7a909f0534d |
| TRT Nation | https://app.notion.com/p/34b84b6d1f498198a2e3d36acd151639 |
| Trim Rx | https://app.notion.com/p/36b84b6d1f49808498c9fd7065e133a4 |

## Context / Verify Before Counting

These rows surfaced in GLP-1 searches but may be infrastructure, regulatory, owner-adjacent,
or context-only rather than primary GLP-1 market participants:

- Alliance for Pharmacy Compounding
- Eucalyptus
- Infusive
- Keeps
- MD Integrations
- Meta Pharmacy
- OpenLoop
- Ulo
