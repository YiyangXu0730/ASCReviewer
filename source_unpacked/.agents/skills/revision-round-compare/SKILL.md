# Revision Round Compare

## Purpose

Compare a revised draft with prior feedback and classify issue resolution.

## When To Use

Use after at least one previous review, supervisor feedback round, or ASCReview report exists.

## Required Inputs

- specialized review pack
- previous draft or reviewed section, if available
- revised draft
- prior feedback or report
- prior score basis or previous ASCReview report, if score movement is requested
- response-to-feedback notes, if available
- figures/assets and source constraints if revised figures or factual claims are in scope
- marking scheme
- user's revision goals

## Priority Rules

- Teacher/supervisor feedback and rubric criteria dominate.
- Prior ASCReview comments are secondary to teacher instructions.
- New issues should be raised only when they affect rubric, scientific validity, coherence, or high-value revision quality.
- If prior feedback or revised material is missing, resolution classification is blocked or provisional.

## Evidence Rules

Resolution status must cite visible evidence in the revised draft. Do not mark an issue resolved because wording changed unless the underlying problem is fixed.

## Positive Patterns

- previous issues are converted into trackable items;
- each item has a status and evidence location;
- new issues are separated from unresolved old issues;
- the updated must-fix list is shorter and priority ordered.
- missing revision inputs are handled through a revision input gate before comparison begins.

## Negative Patterns

- vague "improved" judgments;
- missing evidence for resolution;
- reopening unrelated polish issues;
- ignoring new contradictions introduced by revision.
- new figure/data/method/source traceability gaps introduced during revision;
- revised claim strength exceeds newly added evidence;
- reanalysis changes are not propagated to figures, legends, methods, and claims.
- revision comparison attempted without prior feedback, revised draft, or previous review basis.

## Checklist

- Is every previous issue represented?
- Are prior feedback, revised draft, and previous review basis available enough to compare?
- Does the revised draft contain evidence of change?
- Did the change fix the underlying problem?
- Did the change create new rubric, coherence, or scientific risks?
- Should the score estimate or priority list change?
- Did the revision add new data, methods, figures, sources, or claims that now require provenance checks?
- Did the revision introduce new availability, access, or traceability statements that need verification?
- If data, preprocessing, model design, contrasts, thresholds, or figure-generation code changed, did downstream text and legends change consistently?

## Output Schema

```json
{
  "revision_round": {
    "revision_input_status": {},
    "resolved": [],
    "partially_resolved": [],
    "unresolved": [],
    "new_issue_introduced": []
  },
  "updated_must_fix": [],
  "updated_should_fix": [],
  "next_revision_plan": []
}
```

## Known Failure Modes

- Treating surface edits as substantive resolution.
- Penalizing the user for ignoring feedback that conflicts with teacher guidance.
- Reviewing the whole document from scratch instead of comparing against prior issues.
- Missing new problems introduced by otherwise successful revisions.
- Treating unresolved evidence availability as wording polish.
- Accepting a revised figure or claim without checking whether the analysis/query that generated it changed.
- Inferring resolution status from author intent or memory when the prior issue record is missing.

## Uncertainty Handling

- Mark issue status provisional when previous draft, revised draft, or prior feedback is incomplete.
- Stop rather than compare when both prior feedback and revised material are missing.
- Separate old issue resolution from new issues introduced.
- Do not infer why the author made a change unless revision notes are provided.

## Provenance Expectations

- Use rule IDs such as `REVISION-R1-RESOLUTION-EVIDENCE`, `REVISION-R2-NEW-TRACEABILITY-GAPS`, `REVISION-R3-REANALYSIS-TRACEABILITY`, and `REVISION-R4-REVISION-INPUT-GATE`.
- Each resolution decision must cite location/evidence in the revised draft.
- New data, methods, figures, or claims should be checked against source/provenance rules when relevant.

## Stop Conditions

Stop or mark provisional if:

- prior feedback is unavailable;
- revised draft is unavailable;
- task specialization pack is absent;
- the user asks for score change without rubric and prior score basis.
