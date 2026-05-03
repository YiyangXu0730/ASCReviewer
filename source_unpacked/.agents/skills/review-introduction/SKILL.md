# Review Introduction

## Purpose

Evaluate an Introduction for context, gap, rationale, aim, scope, rubric alignment, and claim calibration.

## When To Use

Use after task specialization when reviewing an introduction, opening chapter, proposal background, or article introduction. Do not use in build mode to review the user's dissertation.

## Required Inputs

- `ReviewTaskSpec.json`
- `MarkingSchemeMap.json`
- section requirements and weights
- draft Introduction text
- `SourceEvidenceIndex.json`
- relevant pattern files under `patterns/introduction/`

## Priority Rules

- Teacher rubric and section brief have highest priority.
- Domain expertise is secondary and must be labeled.
- If the rubric asks for a specific structure, follow it even if corpus patterns suggest another order.

## Evidence Rules

Use evidence tags:

- `teacher_rubric`
- `official_guideline`
- `source_pattern`
- `domain_expert_heuristic`
- `provisional`

Rules supported only by domain heuristics cannot create a must-fix issue unless they also affect rubric alignment or scientific accuracy.

## Positive Patterns

- `INT-P1`: context -> gap -> aim.
- `INT-P2`: rubric-matched scope.
- `INT-P3`: calibrated rationale claims.
- `INT-P4`: signpost without detailed results.
- `INT-P5`: study-design-aware rationale.
- `INT-P6`: evidence-level rationale.
- `INT-P7`: guideline scope without guideline dumping.

## Negative Patterns

- literature dump without gap;
- hidden or absent aim;
- overstated biomedical significance;
- rubric-irrelevant background;
- topic-specific assumptions in a generic checklist.
- guideline laundering before study design is known;
- public-data or portal-derived overclaiming.

## Checklist

- Can the Introduction's gap be quoted in one sentence?
- Is the aim, objective, hypothesis, or review question explicit?
- Does each paragraph serve context, gap, rationale, scope, or aim?
- Are claim-strength verbs justified by the cited evidence?
- Does the scope match the marking scheme and section brief?
- Are study-design requirements prepared without turning the Introduction into Methods?
- If public datasets or cancer-genomics portals are part of the rationale, is the analysis framed as exploratory, validated, mechanistic, or clinical with the right level of certainty?
- If a reporting guideline seems relevant, has the study design been confirmed before applying it?

## Output Schema

Return findings as:

```json
{
  "section": "introduction",
  "rubric_alignment": [],
  "must_fix": [],
  "should_fix": [],
  "optional_polish": [],
  "claim_calibration_notes": [],
  "missing_information": [],
  "evidence_links": []
}
```

## Known Failure Modes

- Penalizing a valid local dissertation structure because it differs from article conventions.
- Treating domain background preference as rubric requirement.
- Rewriting the Introduction before identifying rubric-critical issues.
- Overfitting to the current prostate cancer/DDR seed topic.
- Treating an official guideline as a teacher scoring criterion before specialization.
- Treating public-data associations as mechanistic or clinical proof.

## Uncertainty Handling

- Mark study-design guideline comments provisional until specialization confirms the design.
- Mark external biomedical accuracy claims provisional unless the source evidence index supports them.
- Separate rationale clarity from factual correctness when sources are incomplete.

## Provenance Expectations

- Use rule IDs such as `INTRO-R1-CONTEXT-GAP-AIM`, `INTRO-R3-STUDY-TYPE-SCOPE-SIGNAL`, `INTRO-R4-PUBLIC-DATA-RATIONALE-LIMITS`, and `CLAIMS-R2-TRANSLATIONAL-EVIDENCE-LADDER`.
- Link claims to source IDs from `library/source_index.seed.json` or task-specific sources.
- Do not cite optional prostate cancer seed sources unless the future task specialization selects them.

## Stop Conditions

Stop or mark provisional if:

- marking scheme is missing and scoring is requested;
- section requirements are missing and the user wants compliance review;
- source evidence is unavailable for biomedical accuracy claims;
- the session is still a build task rather than a real review.
