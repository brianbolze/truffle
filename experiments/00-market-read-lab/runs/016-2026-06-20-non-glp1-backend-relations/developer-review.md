# Developer Review

Question: **What Truffle system behavior does this run pressure?**

> Reviewed via the Loop-2 adversarial workflow (developer pass + evidence verifier, Sonnet).

## Capability pressure

| Capability | What the run exposed | Smallest useful response |
|---|---|---|
| **Structure** | The `pharmacy_partner` relation axis is now a **second sighting** of a join-capable cross-brand backend edge needing frontmatter expression (run 014 = clinical/OpenLoop in GLP-1; run 016 = pharmacy/Strive in non-GLP-1). | A dotted-domain `pharmacy_partner:` field mirroring `parent`/`owns`, **gated on MRL-005/006 human graduation**; not built here. |
| **Query / access** | The ~35-brand named-entity grep→prose-scan→`ls store/*<name>*` resolve loop repeated run 014's manual relation-resolution toil. | A documented QUERYING recipe entry for relation-resolution reads (additive to MRL-002), not a helper. |
| **Capture** | Most named compounders dangle (no store entry); one (`belmarpharmasolutions-com`) is captured-but-no-`profile.md`; one (`hallandalerx-com`) has a profile but is uncited — the join fails from **both** directions. | If MRL-005/006 graduate: capture the supplier `profile.md` first, then add the field. Order of operations matters. |
| **Synthesis** | `pharmacy_model` frontmatter comments carried most named entities this capture and sped the read — positive evidence that richer frontmatter annotation cuts body-scan labor. | Observation; no change. |

## Lenses

**Steward** — System stayed honest. Verifier independently reproduced **all** load-bearing
counts (Strive ×2; Curexa/Tailor Made/Olympia ×2; Beluga singleton; no shared clinical
network outside GLP-1; cohort 35) with one real catch: the read overclaimed
`belmarpharmasolutions-com` as a joinable supplier profile when it has `captures/` only and no
`profile.md` — **corrected in `read.md` + receipt** (now a 3-tier join-readiness distinction).
Receipt denominator *method wording* was also imprecise (a full-line `grep -v GLP-1` yields 33
not 35; the value-parse yields the correct 35) — corrected. State/Judgment separation clean;
J1–J3 labeled and evidence-tied; "concentration" correctly withheld from 2-brand
co-occurrence; absence framed as "not found."

**Dev Agent** — The repeated relation-resolution loop (anchor grep → prose scan → entity
resolve) is now a 2-cohort recurrence and a candidate for a documented recipe — but still
recipe-level; no helper, grep-verifiable contract preferred. The belmar miss argues for a tiny
contract sharpening: "joinable" must mean `profile.md` exists, not "a `store/<domain>/`
directory exists."

**Founder** — The finding compounds the warm asset (one new joinable edge, Strive) while
staying light; no ontology gravity added. The graduation temptation (build the
`pharmacy_partner` edge now) is correctly deferred to the human gate.

## Recommendation

- No-op / keep as observation: the synthesis + query observations (recipe-level).
- **Watch for recurrence:** a third brand naming Strive (or any compounder ≥3 brands).
- **Submit triage candidate:** Evidence-Log appends to **MRL-005**, **MRL-006**, **MRL-001**
  (made in `triage.md`). The MRL-005 recurrence-test bar is **met**; graduation human-gated.

## Triage submissions

See `triage.md` Evidence Log appends (MRL-005/006/001), dated 2026-06-20. The "joinable" =
`profile.md`-exists contract refinement is folded into the MRL-006 append. **No graduation, no
implementation.**
