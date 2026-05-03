# Toy Specialization Pack

This example is intentionally not based on the user's dissertation.

It exists only to test whether ASCReview can create a task-specific review environment before draft review.

## Scenario

A student asks for formative review of an Introduction for a short biomedical research proposal about yeast oxidative stress response. The marking scheme is simplified and artificial.

## Files

- `ReviewTaskSpec.toy.json`
- `MarkingSchemeMap.toy.json`
- `SectionReviewContract.introduction.toy.json`
- `MissingInformationRequest.toy.md`

## Use

Run `ascreview/ASCReview_SPECIALIZATION_PROMPT.md` against these inputs. ASCReview should identify that the toy pack is sufficient only for formative Introduction review, not full draft scoring.
