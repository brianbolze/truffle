# Developer Review

Question: **What system change does this suggest?**
Verdict: **No new State primitive. Hold the typed-edge candidate behind recurrence and a
capture-grain prerequisite; land the run's two submissions as MRL-005 (edge, held) + MRL-006
(named-counterparty capture grain). Parent/ownership confirmed already covered.**

## Steward

**Caveat and provenance discipline is strong; the real corpus pressure is a capture-grain gap, and
it's broader than the run scoped it.**

- Well-handled: governing clocks named (~20d oldest), working set declared as **not a denominator**,
  `claim-not-truth` flagged with the BlueChew proof, `named-is-the-minority` (5/18 pharmacy, ~3/18
  clinical) stated, and the freshness footgun called out — backends churn quietly and **won't show as
  a price move**, so a swap is a Signal-layer catch, not State. Reusable as-is.
- **Grain finding (new evidence):** the relation data is **split by shape** — `parent`/`owns` are
  clean joinable frontmatter; pharmacy/clinical partners are **prose claims** in the body. There is no
  single field for "what does brand X depend on." The run logs this as ergonomics, but it's the
  **load-bearing system fact**: the only reason supplier-concentration isn't a one-command answer today
  is that the named counterparty lives in prose, not frontmatter.
- **Generalize the run's clinical P3.** The run submitted a *clinical-only* capture-grain gap. The
  Steward lens shows it's the **same gap for pharmacy** — both are prose-only, both block the join.
  Frame one item: capture the **named counterparty (pharmacy *and* medical group)** into joinable
  frontmatter when the page names it. → MRL-006, generalized.

## Founder

**Anti-Doro check on the edge candidate (run's P2): the value is reachable without a relations
subsystem — hold it, and if it ever graduates, mirror `parent`/`owns`, don't build a graph.**

- The run's "no new *primitive* for parent/ownership" holds — `parent`/`owns` + `pharmacy_model`
  already carry the load-bearing edges, and **`store.py relations` already ranks join targets by
  in-degree** (QUERYING Recipe 3). That *is* the supplier-concentration query the run wants. So for
  the **joinable** edges, supplier concentration is answerable **today**; nothing to build.
- The gap is purely that named pharmacy/clinical counterparties aren't *in* joinable frontmatter.
  That reframes the candidate: it is **not** a new typed-edge ontology — it's (a) **capture the named
  entity into frontmatter** (MRL-006, grain) so it joins, then (b) the **existing** `relations`
  in-degree count does the rest. Building a separate `fulfilled_by`/`clinical_provider` *subsystem*
  off a 5/18-populated, claim-contaminated relation is exactly the premature-machinery move the
  anti-Doro line warns against.
- **Guardrail to attach to the candidate:** if it graduates, do it as **joinable dotted-domain
  frontmatter mirroring `parent`/`owns`** (cheap, precedented, already indexed by `relations`) — not a
  new edge table or relation type registry. And gate graduation on **recurrence**: the run names the
  falsification — re-run on a **compounding-heavy GLP-1 cohort** where brands name pharmacies more
  often, and see whether `named-is-the-minority` flips. One sighting → submit, not graduate. Holds the
  lab's "repeated pressure earns conventions" line.

## Dev Agent

**Cheapest asset is a recipe note, not a tool — and the helper pressure is a recurrence of MRL-002,
not a new item.**

- The run hand-built a second in-run query surface (relations: pull `parent`/`owns` frontmatter **AND**
  grep `telehealth.md` Fulfillment/Provider, then dedupe by hand). Run 0 hand-built the denominator
  union; this is a **different query shape, same pattern** — market reads keep inventing store queries
  in-run. That's recurrence of the *pattern* behind MRL-002, not of the same query, so it **strengthens
  the case for a QUERYING recipe layer over per-query helpers** — without graduating a helper. → light
  evidence note on MRL-002, no new item.
- At current sparsity, **no new tool is justified**: `store.py relations` + a one-line grep tally
  already answer backend in-degree for the joinable edges; the prose edges are too few to automate. The
  80/20 is the run's own next-run advice promoted to a QUERYING note ("for relation reads, read
  frontmatter *and* grep Fulfillment/Provider; trust the named entity or the absence"). Recipe, not
  script — same posture as Run 0's Dev Agent.

## Triage Submissions

- **New — MRL-005:** named-counterparty **relation edge** (pharmacy + clinical) — candidate State edge,
  **hold for recurrence**. Counterparties already resolve to store profiles, so the edge joins; supplier
  concentration is a genuine market read. Do **not** graduate: 5/18 pharmacy, ~3/18 clinical, claim-
  contaminated; parent edge already `parent`/`owns`, posture already `pharmacy_model`. If graduated,
  implement as joinable frontmatter mirroring `parent`/`owns` (indexed by `store.py relations`), not a
  new subsystem. Recurrence gate: re-test on a backend-naming-dense cohort (compounding-heavy GLP-1).
- **New — MRL-006:** named-counterparty **capture-grain gap** (pharmacy *and* clinical) — generalizes
  the run's clinical-only P3. Most brands stop at *"licensed US compounding pharmacy"* / *"licensed
  providers"*; the few named (Curexa, Strive, OpenLoop, Wasef PC, CareGLP) prove the grain is
  capturable. This is the **prerequisite** for MRL-005 — capture-depth, not a primitive. P3.
- **Adjustment — MRL-002:** add Run 001 as a second sighting of in-run query-building (relations
  surface) and link it; reinforces "prefer a QUERYING recipe layer; hold committed helpers until the
  *same* query recurs."
- **No-op / confirmed:** no new relation primitive for parent/ownership — `parent`/`owns` +
  `pharmacy_model` cover it, `store.py relations` already counts in-degree, Run 0 surfaced the canonical
  RexMD↔LifeMD case.
