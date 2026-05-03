# ASCReview Full Draft Review Prompt

Use this prompt only after task specialization is complete and all draft sections needed for the requested scope are available.

## Mission

Review the whole draft for rubric alignment, cross-section coherence, evidence flow, figure-text consistency, and revision priorities.

## Required Inputs

- full specialized review pack;
- all draft sections in scope;
- figure legends and figure files or descriptions;
- supervisor feedback, if available;
- source evidence index;
- previous section reports, if available.
- draft stage and target assessment/venue.

## Review Sequence

1. Confirm that specialization is complete.
2. Build a section inventory with word counts, headings, and missing components.
3. Map each rubric criterion to the section or sections that satisfy it.
4. Check Introduction -> Methods -> Results -> Discussion logic.
5. Check whether Methods support every Results claim.
6. Check whether Results contain evidence before interpretation.
7. Check whether Discussion returns to aims, limitations, and implications without overclaiming.
8. Check figure-text consistency and legend sufficiency.
9. Check data/code/resource provenance only at the severity appropriate to draft stage and task requirements.
10. Produce a priority-ordered revision plan.

## Cross-Section Failure Modes

- aim introduced but not answered;
- method described but no corresponding result;
- result reported but method omitted;
- discussion claim exceeds the result;
- duplicated background across sections;
- figure panel not cited or cited out of order;
- rubric criterion left unmapped.
- public-data or prediction-model claim exceeds validation evidence;
- final-submission repository/code/resource expectation applied too harshly to an early draft.

## Output

Use `templates/FullDraftReviewReport.template.md`.

Do not include a final submission judgment unless the marking scheme supports it. If scoring is allowed, include confidence and missing-information caveats.
