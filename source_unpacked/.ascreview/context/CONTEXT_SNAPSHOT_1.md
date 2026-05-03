# ASCReview Context Snapshot 1

## Current Mission

Build ASCReview Core + Corpus Library + Distilled Skills + Adversarial QC Harness + templates/schemas/prompts. Do not review the user's dissertation yet.

## Completed Tasks

- Read `README_START_HERE.md`, `CODEX_MASTER_RUN_PROMPT.md`, `DMD_ASCReview_Core_Corpus_Distillation.md`, `docs/harness/LONG_RUN_HARNESS.md`, `docs/harness/ADVERSARIAL_DISTILLATION_PROTOCOL.md`, `docs/harness/CONTEXT_COMPACTION_PROTOCOL.md`, and both task docs.
- Extracted the build pack into `ascreview_codex_longrun_build_pack_v1/`.
- Built ASCReview Core files under `ascreview/`.
- Built corpus policy, acquisition plan, source index, and provenance ledger under `library/`.
- Expanded pattern libraries under `patterns/`.
- Built installable review skills under `skills/`.
- Built adversarial QC protocol, report, template, and distillation ledger under `qc/`.
- Updated review templates under `templates/`.
- Ran package validation successfully.

## Files Created or Modified

See `ARTIFACT_INDEX_1.json` for machine-readable file groups.

Key groups:

- `ascreview/*`
- `library/*`
- `patterns/introduction/*`
- `patterns/methodology/*`
- `patterns/results/*`
- `patterns/discussion/*`
- `patterns/figures/*`
- `skills/*/SKILL.md`
- `qc/*`
- `templates/*`
- `.ascreview/run_ledger.md`

## Current Unresolved Disputes

- Supervisor tolerance for assertive thesis language is unknown until specialization.
- Institution-specific dissertation structure may override article-style conventions.
- Some optional source metadata should be rechecked before citation export.
- MDAR is currently metadata-only until article-level reuse status is rechecked.
- Actual guideline applicability must be determined by study design during future specialization.

## Current Corpus Status

- Source policy created.
- Acquisition plan created.
- Seed source index created with official guidelines, source-reuse policy sources, and open access writing/methods pattern sources.
- Provenance ledger seeded with accepted rules, evidence tags, confidence, failure modes, limitations, and audit status.
- No copyrighted long full text stored.

## Current Skill Status

Created installable skills:

- `review-introduction`
- `review-methodology`
- `review-results`
- `review-discussion`
- `review-figures-legends`
- `assess-rubric-alignment`
- `assess-scientific-claim-strength`
- `assess-bioinformatics-methods`
- `revision-round-compare`

Each skill includes purpose, when to use, required inputs, priority rules, evidence rules, positive/negative patterns, checklist, output schema, failure modes, and stop conditions.

## Current QC Status

Minimum required adversarial cycles were recorded:

- Introduction: 2
- Methodology: 2
- Results: 2
- Discussion: 2
- Figures/legends: 1
- Rubric alignment: 1
- Revision-round compare: 1

One extra bioinformatics cycle was added because domain relevance is high.

## Next Highest-Value Actions

1. Expand corpus with verified open access biomedical/cancer/genomics source examples.
2. Add automated JSON schema validation for `library/*.json` and `qc/*.json`.
3. Mirror or install `skills/` into `.agents/skills/` if this package needs direct Codex skill installation.
4. Add worked non-dissertation toy examples to test specialization and review contracts.
5. In a future real review session, create a task-specific specialization pack from the actual marking scheme and draft materials.

## Stop Conditions Encountered

None.

## Exact Continuation Instruction

Continue ASCReview long-run build from `CONTEXT_SNAPSHOT_1.md` and `ARTIFACT_INDEX_1.json`.
Do not restart from scratch.
Prioritize unresolved disputes and next actions.
Continue the LibraryBuilder -> AdversarialAuditor -> Arbiter loop.
Do not review the dissertation yet.
