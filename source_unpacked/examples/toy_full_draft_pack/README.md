# Toy Full-Draft Pack

This fixture is intentionally unrelated to the user's dissertation.

It exists to test ASCReview's full-draft workflow, rubric mapping, section contracts, draft-stage caveats, and stop conditions without reviewing real user writing.

## Scenario

A fictional short undergraduate lab report examines whether light exposure affects yeast growth in liquid culture. The draft is deliberately simple and not intended as a scientific source.

## Files

- `ReviewTaskSpec.toy_full.json`
- `MarkingSchemeMap.toy_full.json`
- `SectionReviewContract.full_draft.toy.json`
- `toy_full_draft.md`
- `MissingInformationRequest.toy_full.md`
- `ASCReview_DryRunReport.toy_full.md`
- `ASCReview_DryRunFindings.toy_full.json`

## Expected ASCReview Behavior

ASCReview may run a formative workflow test but should:

- avoid treating the toy topic as corpus evidence;
- keep scoring limited to the artificial toy rubric;
- identify missing source evidence for factual biology claims;
- distinguish draft-stage issues from final-submission requirements.
