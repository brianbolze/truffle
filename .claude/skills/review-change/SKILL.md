---
name: review-change
description: Use when asked to review a new incoming change or PR in this Web Research / Truffle project.
disable-model-invocation: true
argument-hint: <Any specifics you want reviewed>
---

$ARGUMENTS

- Review [`MAINTAINING.md`](../../../documentation/MAINTAINING.md)
- Review [engine-dev rules](../../rules/engine-dev.md). Are we adhering to them?
- Consider running the `drift-sweep` skill
- Consider looking at this from the perspectives of the different [personas](../../../documentation/personas.md)
- Look at the impact on the directory / file structure. Does this add bloat?
- Does this new change suffer from overfitting? Was it designed based on only a small set of data / specific circumstance?
- Does this new change increase complexity / risk in a way that we haven't anticipated?
- If this new feature / change has an associated "FRAME" doc - read it - and ensure we're meeting it's intended goals.
- If this new feature / change has an associated "PROPOSAL" / "APPROACH" doc - read it - and see if it has drifted.
