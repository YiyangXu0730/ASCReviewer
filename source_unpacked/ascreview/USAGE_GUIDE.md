# ASCReview Usage Guide

## Build Mode

This package build mode creates ASCReview itself. It must not review a dissertation.

Outputs from build mode include:

- core prompts;
- source policy and acquisition plan;
- source index and provenance ledger seeds;
- pattern libraries;
- reusable skills;
- adversarial QC report;
- schemas and templates.

## Real Review Mode

Start a new session and provide:

- draft text or the sections to review;
- teacher marking scheme;
- dissertation or manuscript section requirements;
- section weights and word limits;
- source constraints, required citation boundaries, or permission to use verified open sources;
- assessment context, draft stage, target venue, deadline, and desired output;
- domain background sources, if factual review is requested;
- figures and legends;
- supervisor comments, if any;
- desired report format.

ASCReview first runs `ASCReview_SPECIALIZATION_PROMPT.md`. Only after the specialization gate passes should it run section, full-draft, or revision prompts.

## Specialization Input Contract

Every real review session should create `SpecializationInputContract.json` before reviewing text. It records five required input groups:

- draft;
- marking scheme;
- figures/assets;
- source constraints;
- assessment context.

The contract sets review permissions separately:

- draft text review;
- rubric scoring;
- figure review;
- domain factual review;
- final report export.

If an input is missing, disable only the review mode it blocks. For example, a missing marking scheme blocks scoring but may still allow explicitly permitted non-scored formative review. A missing figure asset blocks visual figure review but does not block text-only review.

## Routing And Severity

Specialization must record routing decisions for task type, study design, discipline, modality, reporting guideline, review mode, claim evidence level, and output format.

Use these severity categories:

- `rubric_failure`
- `scientific_validity_risk`
- `reporting_completeness_risk`
- `reproducibility_risk`
- `policy_compliance_risk`
- `draft_stage_todo`
- `style_or_clarity_polish`

Do not label an issue as `rubric_failure` unless supplied rubric, assignment brief, dissertation handbook, or teacher feedback supports it.

## Recommended Review Order

1. Specialization pack.
2. Rubric alignment audit.
3. Section review in this order where possible: Introduction, Methodology, Results, Discussion, Figures/legends.
4. Scientific claim strength check.
5. Full draft coherence review.
6. Revision-round comparison after edits.

## Corpus Expansion

When expanding the corpus:

- verify current source URL, DOI, PMID or PMCID where available;
- verify license and reuse status;
- store metadata and distilled patterns rather than full text;
- mark uncertain sources `metadata_only`;
- record all rules in the provenance ledger.
- update the relevant JSON Schema and validator if new source types, rule families, or round families are introduced.

## Interpreting ASCReview Output

`must_fix` means likely grade, validity, or compliance risk.

`should_fix` means meaningful improvement with lower immediate risk.

`optional_polish` means style or clarity changes that should not displace rubric-critical revisions.

## Hard Stops

ASCReview should stop and request clarification when:

- no marking scheme is available for a scored review;
- `SpecializationInputContract.json` is absent or marks the requested review permission false;
- section weights are unknown and scoring is requested;
- a source cannot be verified;
- copyright status is unclear and full-text storage is requested;
- the user asks to review draft material during build mode.
