# CODEX MASTER RUN PROMPT — Build ASCReview Long-Run Workflow

You are Codex operating in a repository/workspace that contains this ASCReview build pack and the user's generic workflow / Plan Library pack.

## Mission

Build **ASCReview Core + Corpus Library + Distilled Skills + Adversarial QC Harness**.

Do **not** review the user's dissertation yet.

## Must read first

1. `README_START_HERE.md`
2. `DMD_ASCReview_Core_Corpus_Distillation.md`
3. `docs/harness/LONG_RUN_HARNESS.md`
4. `docs/harness/ADVERSARIAL_DISTILLATION_PROTOCOL.md`
5. `docs/harness/CONTEXT_COMPACTION_PROTOCOL.md`
6. `docs/tasks/TASK-ASCREVIEW-0001_BUILD_CORE.md`
7. `docs/tasks/TASK-ASCREVIEW-0002_CORPUS_SKILL_DISTILLATION.md`

## Operating mode

You are allowed to execute this as a **single-window build**. However, you must simulate separated roles:

- WorkflowCreator
- LibraryBuilder-Distiller
- AdversarialAuditor
- Arbiter-Integrator
- RunSupervisor

Never let the same role both propose and approve a rule.

## Timebox

Target build duration: 4–5 hours.

Maximum build duration: 6 hours.

The number of iterations does not matter. Keep iterating until the timebox, unless a hard stop condition appears.

## Primary emphasis

The highest-value work is the corpus and skill-distillation layer.

Do not spend the whole run polishing README files.

Prioritize:

1. source policy and acquisition workflow;
2. corpus index schema and seed index;
3. introduction/methods/results/discussion/figure pattern libraries;
4. reusable review skills;
5. adversarial QC rounds;
6. provenance ledger;
7. task specialization flow.

## Deliverables to create or refine

Create or refine these directories:

```text
ascreview/
  README_ASCReview.md
  ASCReview_CORE_PROMPT.md
  ASCReview_SPECIALIZATION_PROMPT.md
  ASCReview_SECTION_REVIEW_PROMPT.md
  ASCReview_FULL_DRAFT_REVIEW_PROMPT.md
  ASCReview_REVISION_ROUND_PROMPT.md
  USAGE_GUIDE.md

library/
  source_policy.md
  acquisition_plan.md
  source_index.schema.json
  source_index.seed.json
  provenance_ledger.schema.json
  provenance_ledger.seed.json

patterns/
  introduction/
  methodology/
  results/
  discussion/
  figures/

skills/
  review-introduction/
  review-methodology/
  review-results/
  review-discussion/
  review-figures-legends/
  assess-rubric-alignment/
  assess-scientific-claim-strength/
  assess-bioinformatics-methods/
  revision-round-compare/

qc/
  adversarial_distillation_protocol.md
  audit_report.template.md
  distillation_round_ledger.schema.json
  adversarial_qc_report.md

schemas/
  ReviewTaskSpec.schema.json
  MarkingSchemeMap.schema.json
  SectionReviewContract.schema.json
  ReviewReport.schema.json

templates/
  ReviewTaskSpec.template.json
  MarkingSchemeMap.template.json
  SectionReviewReport.template.md
  FullDraftReviewReport.template.md
  RevisionRoundReport.template.md
```

## Required final output

At the end of the run, output:

```text
ASCREVIEW_BUILD_COMPLETE
```

Then provide:

- BuildSummary
- CorpusLibrarySummary
- SkillLibrarySummary
- AdversarialQCReportSummary
- RemainingWeaknesses
- NextRecommendedBuildStep
- FilesCreatedOrModified
- Whether context compaction was used
