# GPT-5.5 run log

Date: 2026-06-13

## Status

GPT-5.5 candidate generation completed for all 10 original V1 packets.

**Superseded for final comparison:** on 2026-06-13 the experiment was tightened to require the `logos:{}` profile module for every sample. The original GPT-5.5 candidates are useful as a first pass, but several profiles left logos empty or partial. They should not be treated as final V1.1 candidates until GPT-5.5 is rerun or patched from the logo evidence packets.

Mechanical check:

```bash
python3 experiments/2026-06-13-research-company-model-bakeoff/scripts/check_candidates.py gpt55
```

Original V1 result: all requested candidate files present; profile frontmatter present; requested module frontmatter values conform to the pre-logo-required experiment checker.

Current V1.1 checker intentionally fails the original GPT-5.5 set where logos are missing or empty.

## Outputs

Candidate artifacts live under `_out/gpt55/` and are intentionally not promoted into `store/`.

| Sample | Requested | Files written |
|---|---|---|
| `telehealth_joinamble` | `profile.md`, `offerings.md`, `telehealth.md` | complete |
| `telehealth_hellopepti` | `profile.md`, `offerings.md`, `telehealth.md` | complete |
| `telehealth_ro` | `profile.md`, `offerings.md`, `telehealth.md` | complete |
| `telehealth_noom` | `profile.md`, `offerings.md`, `telehealth.md` | complete |
| `pharmacy_belmar` | `profile.md` | complete |
| `pharmacy_mills` | `profile.md` | complete |
| `labs_jinfiniti` | `profile.md` | complete |
| `services_redantler` | `profile.md` | complete |
| `fitness_peloton` | `profile.md` | complete |
| `fintech_stripe` | `profile.md` | complete |

## Early Notes

These are not findings yet; they are review prompts.

- GPT-5.5 frequently left logo/font/framework fields empty when the packet did not provide easily verifiable assets. V1.1 fixes this by putting logo evidence directly in each packet and making `logos:{}` required.
- Several runs explicitly downgraded `offerings.md` enumeration to `unknown` or `lines-omitted` when the packet did not prove a full roster.
- Candidate quality still needs blind review against Claude comparator outputs. Do not promote these files into `store/` from this run alone.
