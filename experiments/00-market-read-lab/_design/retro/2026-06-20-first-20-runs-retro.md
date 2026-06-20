---
created: 2026-06-20
last_updated: 2026-06-20
authors: both
status: retro — first ~20 runs (000–023)
---

# Retro: the first ~20 Market Read Lab runs

> **The apparatus runs clean and safely. But it was aimed at the wrong target.** The lab optimized for *"prove the store can answer the question"* when its job was *"stress the store against ambitious questions and harvest what's missing."* Those are opposite jobs. We ran the wrong one — carefully. This retro says what we learned, why the output came out thin, and how we re-point it.

## The one thing to remember

We thought 20 runs had **answered** the big question (does Truffle need a category/cohort system?). They didn't. They showed the store can handle the *easy* questions easily — which is not the same thing. The value of a category capability shows up on the *hard, wide, reach-outside* questions, and those are exactly the ones the lab avoided.

**Absence of category-pressure isn't proof you don't need it. It's proof we never probed where it would appear.**

## What the lab was for

Truffle profiles **one company at a time**. The open question: to really understand a company, don't you need the market around it — its neighbors, substitutes, shared suppliers, what's becoming normal? And if so, does that need a whole new "categories" system, or not?

Rather than build that system on a guess, we ran an experiment: **keep asking real market questions, answer them from what we've captured, and watch where Truffle helps or flails.** Start by persisting the *runs*, not the ontology. ~20 runs in ~2 days.

## What 20 runs actually produced

**The good — discipline held.** This part genuinely worked, and it's worth protecting in the redesign.

- **Clean guardrails.** No run polluted the store, auto-built anything, or wrote back to other systems. The "describe, don't judge" and "propose, don't write" lines held even under the hardest test.
- **Evidence hygiene matured fast.** An early run (002) over-trusted search snippets and got demoted. The fix worked — it never recurred. The three runs that spent real money on outside sources stayed disciplined and on-budget.
- **The double-check earns its keep.** The adversarial review pass caught real errors every time — a whole missed data source, miscounts, an overclaim, even one fabricated example. Zero load-bearing conclusions were ever overturned, but plenty of sloppiness was.

**The disappointing — the output was thin.** After 20 runs, the backlog holds essentially **two ideas and three decisions**. We'd hoped for 15+ clear weaknesses, several new "ingredient" ideas, and sharper thinking about what a category system could even be. We got almost none of that — and **not one** strong idea for a *new kind of ingredient* to capture (beyond a single one: real customer-complaint text from reviews).

## Why it came out thin

*Four root causes. The first is the big one.*

- **We rewarded the wrong thing.** "Answer from the store" was the default, and the store is all telehealth — so nearly every run quietly became *"can I answer this with what I already have?"* That biases toward questions the store *can* handle, so runs rarely hit a wall hard enough to reveal a missing ingredient. **The tell:** the only runs that surfaced a new ingredient were the ~3 that reached *outside* the store. New ingredients live outside. We barely went.

- **The runs answered the wrong job.** A run's job is to *serve a real market need and report where Truffle made it easy or hard, and what it wished it had.* Instead, runs (and the review lenses grading them) leapt to *"here's what to build — a query recipe."* That's solution-shape, and it isn't the run's call. It crowded out plain observation, and it made every run converge on the same hammer — because that's the shape the machinery kept asking for.

- **The tidying hid the richness.** The triage steward dedups aggressively — great for a clean backlog, terrible for idea-generation. Twenty runs of distinct little observations got merged into *"more evidence for the same two items."* The divergence you wanted got tidied away before you could see it. (We don't yet know how much real richness is buried in the raw runs — that's the next step.)

- **Too narrow.** Every run was telehealth, mostly GLP-1 and hormones. Same neighborhood → same observations → repetition. We never felt the friction of a genuinely different market.

<details>
<summary>The original spark, and how far we drifted from it</summary>

The whole thread started (the Waldo "wallow") from envy of a tool that **sells the quality of its inputs** — live social, ads, audience data, trends, events, listicles, forums. The question for Truffle was: *what are the best source ingredients we should capture so future synthesis has better raw material?*

The wallow hypothesized roughly **eight** ingredient families worth exploring: search panels, listicles/directories, ads transparency, news/announcements, Wayback change, reviews/forums, regulatory surfaces, relationship pages.

After 20 runs we meaningfully pursued **one** (review/forum bodies) and brushed two others. That gap — *1 of ~8* — is the cleanest measure of "we didn't go wide enough." The lab drifted from *"what ingredients do we need?"* to *"can we answer questions with what we have?"* and never drifted back.
</details>

## What's genuinely worth keeping

Not everything is a do-over. A few things are real and close to ready:

- **Spotting shared backends.** When two brands quietly use the same behind-the-scenes pharmacy or clinic, that's a useful, captureable fact. Proven across two markets.
- **Real customer complaints, not star ratings.** The one new ingredient the lab actually found — and it carried a whole answer the ratings hid.
- **The "is this even comparable?" instinct.** Prices that look like "$X/month" often aren't the same thing at all. The lab learned to flag that instead of ranking false numbers.

## Where we go next

**Re-point the lab from "prove the store copes" to "stress the store and harvest what's missing."** Concretely:

- **Go wide and go ambitious.** Add markets that feel different. Bias toward questions that *reach past* today's store — including questions we expect to *fail* store-only, precisely to map the gap.
- **Split the job: observe, don't propose.** A run reports friction and wishes. It does *not* propose what to build. Shaping ideas into solutions is a separate, later pass — so runs stop converging on "make a recipe."
- **Keep a divergent idea stream that never gets merged.** Raw, messy, accumulating — separate from the clean backlog. The tidy backlog is downstream of it, not a replacement.

> **Immediate next step:** mine the *raw* runs (not the merged backlog) for every distinct observation, friction point, and "I wish I had ___" hint. If the hunch is right, there are 10–15 ideas buried in there that the tidy-up compressed into two. That harvest becomes the input to redesigning the lab — and tells us whether the thinness was the *lab's* fault or the *triage's*.

### Open questions to settle first

*Frame before mechanism — we deliberately haven't designed the new machinery yet.*

- What does **one great run** produce? (A real answer + N raw observations + ≥1 ingredient wish?) Define the target before the mechanism.
- **How wide:** add a totally different market, or stay in telehealth but only ask questions the store *can't* comfortably answer?
- Should some runs be explicit **"ambition mode"** — pick a question we expect to fail, to map the gap on purpose?
