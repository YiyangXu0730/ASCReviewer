# ASCReview Revision Round Prompt

Use this prompt to compare a revised draft against prior feedback.

## Mission

Classify each previous issue as resolved, partially resolved, unresolved, or newly complicated. Then identify new issues introduced by the revision.

## Required Inputs

- specialized review pack;
- previous draft or previous reviewed section;
- revised draft;
- prior ASCReview report or supervisor feedback;
- marking scheme map;
- source evidence index;
- user's revision goals.
- draft stage and revision scope.

## Review Sequence

1. Confirm specialization artifacts exist.
2. Convert prior feedback into a numbered issue list.
3. Locate evidence of revision in the new draft.
4. Classify each issue:
   - `resolved`
   - `partially_resolved`
   - `unresolved`
   - `new_issue_introduced`
5. Check whether the revision weakened rubric alignment, scientific accuracy, or flow.
6. Check whether newly added text, methods, data, figures, or claims introduced new provenance or traceability gaps.
7. Update must-fix and should-fix priorities.
8. State whether another revision round is necessary.

## Rules

- Do not penalize the revised draft for ignoring feedback that conflicts with the teacher rubric.
- Do not treat wording changes as resolution unless the underlying issue is fixed.
- Do not reopen every possible writing issue; focus on previous feedback plus high-impact new risks.
- Preserve the distinction between rubric risk and optional polish.
- Do not mark a previous issue resolved if the revision fixes wording but introduces a new unsupported claim or missing provenance.

## Output

Use `templates/RevisionRoundReport.template.md`.
