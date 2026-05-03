# Assess Rubric Alignment

## Purpose

Ensure review comments and revision priorities are anchored to the teacher marking scheme, assignment brief, dissertation handbook, or journal instructions.

## When To Use

Use during specialization, before any section review, and again when composing final reports.

## Required Inputs

- teacher marking scheme or explicit note that no scheme is available
- `SpecializationInputContract.json` or equivalent explicit status for draft, marking scheme, figures/assets, source constraints, and assessment context
- section requirements, weights, word limits, and required headings
- draft section or full draft
- prior review outputs, if any

## Priority Rules

- `teacher_rubric` is the highest-priority evidence type.
- Domain expertise, corpus patterns, and official guidelines cannot override explicit rubric requirements.
- If a criterion is unclear, mark it as unknown rather than guessing.
- A missing input disables only the review mode it blocks: missing rubric blocks scoring, missing figures blocks visual figure review, missing source constraints blocks strong factual adjudication, and missing assessment context blocks final severity/export confidence.

## Evidence Rules

Every high-priority issue must map to a criterion, required element, or documented missing information. If not, classify it as `should_fix`, `optional_polish`, or `provisional`.

## Positive Patterns

- criteria are converted into reviewable questions;
- weights drive priority ordering;
- section comments distinguish required, recommended, and optional improvements;
- unmapped criteria are preserved in the report.
- specialization input status is recorded before scoring or draft review begins;
- severity labels distinguish rubric failure, scientific validity risk, reporting completeness risk, reproducibility risk, policy compliance risk, draft-stage TODO, and polish.

## Negative Patterns

- polished review with no criterion IDs;
- scoring without weights;
- source guideline treated as teacher rubric;
- high-weight criteria buried under stylistic comments.
- reporting guideline converted into a scoring criterion without teacher evidence;
- optional journal-standard comment promoted above an explicit assignment requirement.
- missing marking scheme treated as permission to invent scoring criteria;
- missing figures or source constraints ignored when assigning visual or factual findings.

## Checklist

- Are all rubric criteria extracted into `MarkingSchemeMap.json`?
- Is `SpecializationInputContract.json` present and does it permit the requested review mode?
- Are weights and section mappings recorded?
- Are missing weights listed as unknowns?
- Does each must-fix issue map to a criterion or scientific validity risk?
- Are optional writing preferences separated from scoring risks?
- Are guideline-derived comments labeled as reporting/scientific risk rather than marks unless the rubric says otherwise?
- Are missing rubric elements listed as unknown rather than inferred?
- Are severity categories justified by the specialization contract and evidence tags?
- Are blocked review modes downgraded to missing-information requests instead of hidden assumptions?

## Output Schema

```json
{
  "rubric_source": "",
  "criteria_map": [],
  "unmapped_criteria": [],
  "missing_information": [],
  "priority_order": [],
  "review_constraints": [],
  "specialization_input_status": {},
  "severity_policy": [],
  "allowed_score_estimate": true
}
```

## Known Failure Modes

- Inventing rubric criteria to make review easier.
- Using a journal standard as if it were a school marking scheme.
- Failing to ask for weights before score estimation.
- Hiding uncertainty because a guideline feels authoritative.
- Penalizing a dissertation for not matching article conventions when the local handbook differs.
- Treating a structural specialization contract as a substitute for the actual marking scheme or assessment context.
- Calling an issue a rubric failure when it is only a scientific risk or guideline-supported reporting gap.

## Uncertainty Handling

- If no teacher rubric is present, do not score.
- If a guideline is relevant but not rubric-incorporated, label it as support or risk, not grading authority.
- Preserve unmapped criteria and missing weights in the output.
- If an input is partial, enable only the review permissions that are justified and mark the rest as blocked or provisional.

## Provenance Expectations

- Use rule IDs such as `RUBRIC-R1-RUBRIC-FIRST`, `RUBRIC-R2-GUIDELINE-AS-SUPPORT-NOT-SCORE`, and `RUBRIC-R3-SPECIALIZATION-INPUT-GATE`.
- Every must-fix item should cite a rubric criterion, a scientific validity risk, or a clearly labeled stop condition.
- Do not create teacher-specific rules during generic build mode.

## Stop Conditions

Stop if:

- the user asks for a scored review and no marking scheme is available;
- required section weights are unavailable;
- the review task asks ASCReview to fabricate criteria.
- the specialization input contract is absent or says the requested review permission is false.
