# ASCReview Specialization Prompt

Use this prompt at the start of every real review session. Do not review draft prose until specialization is complete.

## Mission

Compile a task-specific ASCReview environment from the user's materials. The output is a specialization pack under `sessions/<task_id>/`.

## Required Inputs

- teacher marking scheme or assignment rubric;
- dissertation or manuscript structure requirements;
- section weights, word limits, and required headings;
- target writing type: dissertation, thesis chapter, article, review, proposal, or revision round;
- draft stage: formative outline, early draft, supervisor review, pre-submission, journal submission, or revision round;
- target venue or assessment context;
- domain background pack or source list;
- draft sections and figure legends, if review will proceed;
- supervisor feedback, if available;
- required output format.

## Build Steps

1. Create `SpecializationInputContract.json` with five explicit input groups: draft, marking scheme, figures/assets, source constraints, and assessment context.
2. Set review permissions in `SpecializationInputContract.json`: draft text review, rubric scoring, figure review, domain factual review, and final report export.
3. Record routing decisions for task type, study design, discipline, modality, reporting guidelines, review mode, claim evidence level, and output format.
4. Create `ReviewTaskSpec.json`.
5. Create `MarkingSchemeMap.json` by extracting only explicit rubric criteria.
6. Create `SectionRubricMap.json` mapping criteria to sections and weights.
7. Create `DomainBackgroundPack.md` using verified sources and uncertainty labels.
8. Create `SourceEvidenceIndex.json` with metadata, source IDs, reuse status, and confidence.
9. Create `SectionReviewContract.json` for each section to be reviewed.
10. Create `ReportTemplate.md` matching the user's requested deliverable format.
11. Create `IterationLedger.json` to track review rounds.
12. Create `MissingInformationRequest.md` for unresolved requirements.

## Specialization Rules

- Do not infer a grading criterion unless the marking scheme explicitly says it or the user labels it as teacher guidance.
- If a domain guideline is relevant, map it as support, not as a replacement rubric.
- If sources are background only, do not treat them as scoring criteria.
- If figures are absent, mark figure review unavailable instead of inventing figure quality findings.
- If the task is biomedical, select relevant reporting guidelines by study design, not by topic alone.
- If the draft is early-stage, label data/code/repository/resource issues as draft-stage caveats unless the rubric requires them immediately.
- If public datasets, portals, or prediction models are used, record database/study IDs, access dates, release versions, query settings, and validation status where available.
- If evidence supports only exploratory, preclinical, biospecimen, public-data, or prediction-model claims, preserve that evidence level in later review contracts.
- Severity must be classified with the specialization severity taxonomy: rubric failure, scientific validity risk, reporting completeness risk, reproducibility risk, policy compliance risk, draft-stage TODO, or style/clarity polish.
- Do not label an issue as rubric failure unless a supplied marking scheme, assignment brief, or teacher feedback supports it.

## Completion Gate

Specialization is complete only when:

- every rubric criterion is mapped or listed as unmapped;
- `SpecializationInputContract.json` lists the status of draft, marking scheme, figures/assets, source constraints, and assessment context;
- review permissions are explicit;
- routing decisions are explicit or listed as unresolved;
- severity taxonomy is available;
- missing weights are documented;
- review scope is explicit;
- draft stage and target venue/assessment context are explicit;
- source evidence has provenance;
- review contracts define allowed outputs and stop conditions.

If the gate fails, output only `MissingInformationRequest.md` and do not review the draft.
