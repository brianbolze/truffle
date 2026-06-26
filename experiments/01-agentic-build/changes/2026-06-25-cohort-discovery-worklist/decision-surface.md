# Decision Surface: Cohort Discovery Worklist

Strategic frame: [`_design/2026-06-26-coverage-strategy-frame.md`](../../../../_design/2026-06-26-coverage-strategy-frame.md)

**Problem.** Truffle needs a way to propose missing companies worth capturing. This packet tested a store-first cohort worklist against frozen telehealth holdouts and a conversation-intelligence benchmark before granting engine authority.

**Decision needed.** Merge the packet as-is, hold it, or revise/downscope into a follow-on packet.

**Recommendation: hold-after-review.** The validation artifacts are useful, and the rerun is now reproducible, but the broad discovery verb did not earn graduation. Do not create `/cohort-discovery` from this packet. The current forward shape is summarized in [`candidate-filtering/2026-06-26-cohort-discovery-worklist-synthesis.md`](candidate-filtering/2026-06-26-cohort-discovery-worklist-synthesis.md).

**What changed.** Packet-local docs/scripts only: accepted proposal, proposal review, lead decision, frozen inputs, validation plan, implementation notes, receipts, raw iteration-2 source outputs, a packet-local runner/scorer for the rerun, a packet-local search harness over existing raw outputs, and a bounded page/entity extraction probe. No `store/`, `tools/`, `skills/`, schema, Signals, or `/research-company` changes.

**Evidence.** Telehealth failed even after WebSearch: F3/F4 recovery 10/13, F2 recovery 5/15; Niagen Plus, Rex MD, and Lifeforce still missed. The second query-family rerun recovered Rex MD but regressed broad recall to 6/13 F3/F4 and 4/15 F2, so better prompts alone are not the fix. Pollution control worked: Brian-marked `tier_c_only` / `exclude` rows are barred from Tier A/B. Conversation intelligence remains positive but imperfect: store-first union reached 9/10 top-10 overlap, with Loom missed and product/workflow rows needing separate scoring.

**Search addendum.** A packet-local search harness treats discovery as graded entity retrieval over the existing iteration-2 raw outputs. Telehealth raw-unit ranking is poor at top-K (P@10 0.100, R@10 0.030, nDCG@10 0.139) and the top unknowns include source/publisher domains. That finding led to the page/entity extraction probe below and argues against another query-only pass. Conversation intelligence still validates store-first retrieval: 9/10 top-10 targets found, Loom still missed.

**Page extraction result.** A fixed 15-page result/list panel improved telehealth materially after direct HTTP plus Firecrawl fallback for the two blocked GLP-1 pages (estimated 2 Firecrawl base scrape credits): P@10 0.600, R@10 0.182, nDCG@10 0.562; must-hit retrieval 11/13, should-hit 7/15, worth_capture 4/5. It still missed Niagen Plus and Lifeforce, and the top ranks still need candidate-type filtering because source domains can compete with capture targets.

**Risk.** Medium during validation because it shaped future agent authority and used paid/search tools; final artifact risk is low because it is packet-local docs/scripts only.

**Checks.** JSON inputs parse. Iteration-2 raw outputs are scored. Search harness and page-extraction output JSON parse. No trailing whitespace or non-ASCII findings. No independent post-implementation review has run; only proposal review exists.

**Follow-on.** Build the next packet-local version around the synthesis: page/entity extraction, candidate cards, agent-led qualification plus usefulness judgment, and four validation checks: discovery recall, source-pollution precision, filter recall preservation, and usefulness / gap coverage. Treat [`candidate-filtering/candidate-qualification-mini-proposal.md`](candidate-filtering/candidate-qualification-mini-proposal.md) as parked prior art. Keep conversation scoring split into company targets versus product/workflow targets. Treat Exa `/search` as novelty/candidate review, not the recall backbone.
