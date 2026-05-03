# TASK-ASCREVIEW-0001 — Build ASCReview Core

## Goal

Build the reusable workflow skeleton for ASCReview.

## Must build

- `ascreview/README_ASCReview.md`
- `ascreview/ASCReview_CORE_PROMPT.md`
- `ascreview/ASCReview_SPECIALIZATION_PROMPT.md`
- `ascreview/ASCReview_SECTION_REVIEW_PROMPT.md`
- `ascreview/ASCReview_FULL_DRAFT_REVIEW_PROMPT.md`
- `ascreview/ASCReview_REVISION_ROUND_PROMPT.md`
- `ascreview/USAGE_GUIDE.md`

## Core modules

- RequirementClarifier
- MarkingSchemeCompiler
- RubricMapper
- DomainBackgroundCompiler
- SectionReviewer
- CrossSectionCoherenceReviewer
- FigureLegendReviewer
- RevisionRoundReviewer
- ReportComposer
- EvidenceCheck

## Rules

- The core workflow must stay general.
- The current dissertation topic may appear only as an example seed.
- Teacher marking scheme has highest priority.
- If marking scheme is missing, request it.
- If section weights are missing, request them.
- Do not invent rubric criteria.
- Do not review the dissertation during this build.

## Deliverable standard

The Core must make it impossible for a future review session to skip specialization accidentally.
