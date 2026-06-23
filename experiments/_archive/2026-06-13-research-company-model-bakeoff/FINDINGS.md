# `/research-company` model bakeoff findings

Date: 2026-06-13

## Bottom line

Claude is the better default writer for `/research-company` today.

On the V1.1 frozen-packet bakeoff, both final candidate sets passed the mechanical file/logo gates, but the blind GPT judge picked Claude on 9 of 10 samples: 8 clear Claude wins, 1 narrow Claude win, and 1 GPT safer-default split. The deciding metric was edit burden, not prose taste:

- **Claude:** 1 severe + 7 moderate edits across 10 samples; average blind score **461.4 / 500**.
- **GPT-5.5:** 0 severe + 33 moderate edits across 10 samples; average blind score **405.1 / 500**.

GPT-5.5's main failure mode was not hallucination. It was **under-extraction**: leaving packet-backed prices, offerings, proof points, nav structure, and cohort nuance out of the candidate artifact. For this store, omission is not harmless; `profile.md` / `offerings.md` / `telehealth.md` are query substrate. A pretty, restrained profile that misses captured facts still creates downstream blind spots.

The one GPT win matters: on Red Antler, GPT correctly refused to convert "family of partners" into ownership, while Claude wrote unsupported `owns:` values. That is exactly the kind of claim GPT-5.5 should be used to audit.

## Scope

Compared final V1.1 candidate outputs:

- GPT-5.5: `_out/gpt55_v11/<sample_id>/`
- Claude: `_out/claude/<sample_id>/`

Excluded:

- `_out/gpt55/` — superseded V1.0, pre-required-logo run.

Inputs:

- Frozen evidence packets under `_out/packets/`
- Required `logos:{}` evidence in each packet
- `profile.md` for all samples
- `offerings.md` + `telehealth.md` for the four telehealth samples

Mechanical checks:

```bash
python3 experiments/2026-06-13-research-company-model-bakeoff/scripts/check_candidates.py gpt55_v11
python3 experiments/2026-06-13-research-company-model-bakeoff/scripts/check_candidates.py claude
```

Both passed.

Judging evidence present in repo:

- Blind packets: `_out/blind/<sample_id>/A|B/`
- Private map: `_out/blind/model_map.json`
- GPT blind judgments: `_out/judging/gpt/*.md`

No Claude judge-pass files were present under `_out/judging/` when this findings doc was written. That weakens the "two-judge" design, but not in the obvious direction: the available GPT judge favored Claude decisively, so the result is not GPT self-preference.

## Aggregate Results

| Sample | Winner | Label | Claude severe/mod | GPT severe/mod | Claude score | GPT score |
|---|---|---|---:|---:|---:|---:|
| `fintech_stripe` | Claude | clear win | 0/1 | 0/3 | 471.5 | 429.5 |
| `fitness_peloton` | Claude | clear win | 0/1 | 0/3 | 460.0 | 415.0 |
| `labs_jinfiniti` | Claude | clear win | 0/0 | 0/4 | 475.5 | 398.5 |
| `pharmacy_belmar` | Claude | clear win | 0/1 | 0/4 | 469.5 | 407.0 |
| `pharmacy_mills` | Claude | clear win | 0/0 | 0/4 | 469.5 | 409.5 |
| `services_redantler` | GPT-5.5 | split / safer default | 1/1 | 0/1 | 398.0 | 425.5 |
| `telehealth_hellopepti` | Claude | clear win | 0/0 | 0/5 | 476.5 | 382.5 |
| `telehealth_joinamble` | Claude | clear win | 0/0 | 0/2 | 472.5 | 404.0 |
| `telehealth_noom` | Claude | narrow win | 0/2 | 0/3 | 445.5 | 405.0 |
| `telehealth_ro` | Claude | clear win | 0/1 | 0/4 | 475.0 | 374.5 |

## What Claude Did Better

Claude extracted more of the packet.

That showed up everywhere the site had a dense fact surface:

- **Stripe:** Claude carried the larger pricing/product index: Terminal, Managed Payments, Radar, Connect, Stablecoins, Disputes, Sigma, Data Pipeline, Revenue Recognition, Issuing, and more. GPT stayed accurate but too thin.
- **Peloton:** Claude captured hardware pricing breadth, refurbished tiers, trial/payment/HSA nuance, and product surfaces. It did miss the All-Access price once, but still needed fewer edits than GPT.
- **Jinfiniti:** Claude preserved the actual catalog shape — NAD tests, supplements, panels, bundles, provider paths, prices, CLIA proof, and claimed customer/doctor counts. GPT over-collapsed the company into diagnostics.
- **Belmar and Mills:** Claude captured operational proof: 503A/503B lane, states, facilities, accreditations, PCAB/PCCA/NCPA/USP quality signals, and workflow details. GPT profiles were materially under-covered.
- **Telehealth samples:** Claude was substantially stronger on per-offering pricing and cohort nuance, especially HelloPepti, JoinAmble, and Ro.

The practical read: Claude is more willing to fill the contract to the altitude the store needs.

## What GPT-5.5 Did Better

GPT-5.5 was more conservative around uncertain relationships.

The Red Antler sample is the proof. The packet described Fat Earth and Wild Fruit as a "family of partners." Claude turned that into:

- `owns: ["wildfruit.co", "fat-earth.com"]`
- "owned partners" in prose

That is not packet-attested. GPT kept `owns: []` and explicitly wrote that the relationship was not treated as proven.

This is the main place GPT-5.5 belongs in the workflow: **claim audit**, especially around `parent`, `owns`, pharmacy ownership, integrated fulfillment, and any site wording that sounds corporate but is not legally explicit.

## Failure Modes

### Claude

Claude's failure mode is **over-assertion from suggestive language**.

Observed severe case:

- Red Antler: "family of partners" became `owns:` and "owned partners."

Moderate cases:

- Peloton: said All-Access price was not captured even though packet contained `$49.99/mo`.
- Noom: said the menopause page was not captured/read even though `sources/menopause.md` existed.
- Ro: needed softer wording around Ro.OS "integrated pharmacy/lab" claims versus retail/manufacturer exceptions.

Pattern: Claude can be too confident when a site implies structure. It needs an ownership/pharmacy-model guardrail.

### GPT-5.5

GPT-5.5's failure mode is **under-coverage**.

Repeated moderate edits:

- missed captured price rows
- missed product/line breadth
- missed proof points and certifications
- missed nav/catalog taxonomy
- collapsed broad product surfaces into a smaller story
- chose safer but less useful `profile.md` altitude

Pattern: GPT writes a cleaner short brief, not a complete store artifact. That is not enough for `/research-company`.

## Logos And Modules

Both V1.1 sets passed the required-logo checker and wrote local `assets/wordmark.svg` where the packet supplied decoded SVGs.

However, the checker is still too loose: several profiles on both sides included URL wordmarks without `w` / `h` measurements, even though `SCHEMA.md` says the logo slots should carry measurements as facts. Tighten `scripts/check_candidates.py` before the next bakeoff or promotion pass:

- require `wordmark` entries to include `w` and `h`
- require `logomark` entries to include `px` and `transparent`
- require `og` entries, when present, to include `w` and `h`
- allow missing `og` only when `LOGO_EVIDENCE.md` says no OG image was declared

Offerings stayed correctly scoped to the four telehealth samples. Do not blanket-force `offerings.md` onto services or giant platforms; create a separate product-roster stress test for Peloton, Jinfiniti, Mills, and possibly Stripe if needed.

## Recommendation

Use Claude as the default `/research-company` writer.

Use GPT-5.5 as a second-pass reviewer, not the primary capture writer:

1. Run Claude to produce the candidate artifacts.
2. Run GPT-5.5 as a claim auditor against the packet.
3. Ask GPT to focus narrowly on unsupported claims, relation fields, pharmacy/integration posture, missing uncertainty, and volatile prices.
4. Promote only after the severe/moderate edit list is cleared.

If GPT-5.5 is used as a writer, change the prompt shape. It needs an explicit "extract before synthesize" step:

- enumerate every captured price row
- enumerate every offering/category/nav line
- enumerate proof/certification/count/date claims
- only then write `profile.md`

Without that extraction spine, GPT tends to produce a polished but underpowered dossier.

## Promotion Notes

For quick promotion from this bakeoff:

- Start from Claude outputs for all samples except `services_redantler`.
- For `services_redantler`, either use the GPT output or patch Claude by removing unsupported `owns:` and "owned partners" language.
- Patch Claude's known moderate misses before promotion:
  - Peloton: add/repair All-Access `$49.99/mo`.
  - Noom: fix the menopause-page-not-captured statement and reconcile page-specific price floors.
  - Ro: soften integrated pharmacy/lab wording to "Ro.OS page claims..." and preserve retail/manufacturer exceptions.
  - Stripe: soften "dual hubs" unless keeping it strictly as an inference from office entries.
- Run a stricter logo-dimension checker before promoting any logo blocks into `store/`.

## Design Takeaway

The experiment worked because it measured the right thing: edit burden against frozen evidence, not which model writes prettier prose.

The answer is not "GPT-5.5 is bad at research." The answer is narrower and more useful:

**GPT-5.5 is currently better as a skeptical reviewer than as the canonical `/research-company` dossier author. Claude still writes the more complete store artifact.**
