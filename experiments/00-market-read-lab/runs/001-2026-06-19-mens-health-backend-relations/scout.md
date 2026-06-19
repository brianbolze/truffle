# Scout

## Prior Context Read

- `triage.md`: three submitted items from Run 0; none acknowledged or graduated.
  Most relevant: denominator reconciliation should stay pattern-level, and helper/tooling
  pressure needs recurrence before acting.
- Last 3 `run-notes.md` files: Run 0 only. Main carry-forward: useful market reads
  can be query-time answers; avoid raw keyword membership; record latency and false
  positives without jumping to implementation.
- Current run artifacts, if resuming: new Run 001 scaffold.

## Candidate Questions

| Question | Type | Why this is worth a run | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|
| In men's health / hormone telehealth, which companies reveal shared backend relationships (parent brand, clinical provider network, pharmacy / fulfillment partner), and do those relationships explain offer shape or pricing? | mixed | Directly tests whether "relations" are load-bearing for market reads, not just company notes. Useful to Telehealth because backend structure affects credibility, margin, risk, and vendor strategy. | `profile.md` + `telehealth.md` evidence for a bounded set of men-first / hormone / sexual-health companies; separate named relationships from generic "partner pharmacy" claims; cite capture limits. | Treating absence of a named partner as absence of a relationship; over-building relation types from one read. |
| Do named pharmacy partners recur across compound-heavy telehealth brands, and would that recurrence support a supplier relation primitive? | system-test | Focuses the relation question on one concrete edge type. Could reveal supplier concentration, regulatory exposure, and capture gaps. | Named pharmacy claims in `telehealth.md` / `profile.md`; distinguish pharmacies selling B2B from pharmacies merely named as fulfillment partners. | Many brands do not name pharmacies publicly; the result may mostly be "unknown," which is still useful but thinner. |
| Do parent / front-door relationships matter in DTC telehealth comparisons? | mixed | Run 0 surfaced LifeMD / RexMD as a load-bearing relation; this tests whether ownership/front-door split recurs. | Frontmatter `parent`, profile body, and explicit routing between brands / subdomains / insurance paths. | Too narrow if only one or two examples show up. |
| Are "proprietary" men's sexual-health formulations actually equivalent molecule stacks across brands? | market/system-test | Tests non-company anchors (molecules / formulations) and product-equivalence relations. Commercially useful for offer design. | Offerings rosters for ED / performance brands; compare molecule combinations and delivery forms. | Could become a molecule taxonomy run rather than a relation run; requires careful scope. |
| Which brands outsource the clinical layer to named provider networks or affiliated P.C.s, and does that matter for trust / risk / margin? | mixed | Clinical-provider relationships may be more important than pharmacy relationships for regulated care. | `telehealth.md` clinical flow, named medical groups, provider network claims, and caveats. | Evidence may be sparse or buried in legal pages; live pages may be needed later, but this run should stay store-first. |

## Selected Question(s)

1. In men's health / hormone telehealth, which companies reveal shared backend relationships
   (parent brand, clinical provider network, pharmacy / fulfillment partner), and are those
   relationships load-bearing enough to justify a typed relation candidate?

## Selection Notes

This is intentionally relation-shaped and not another GLP-1 pricing pass. It should test
whether relation pressure shows up in a live market read:

- **Market value:** backend structure changes how a telehealth brand should be read:
  vertically integrated vs. thin marketing layer vs. parent-owned front door vs. pharmacy
  router.
- **System value:** if the same edge types recur and affect the answer, they may belong
  in triage as typed relation candidates. If they do not, keep them as profile notes and
  query-time synthesis.
- **Evidence readiness:** the store already has `parent` frontmatter, `telehealth.md`
  pharmacy / clinical flow fields, and profile notes for several men-first or hormone-
  adjacent brands.
- **Failure mode:** do not infer hidden relationships from silence. "No named partner"
  means not found in the captured material, not no partner.

Treat prior run patterns as hypotheses, not defaults. Prefer testing whether the same
pressure recurs over copying a previous run's exact method.
