# Review Discussion

## Purpose

Evaluate interpretation, limitations, alternative explanations, prior-literature integration, implications, and whether conclusions stay within evidence.

## When To Use

Use after specialization for Discussion sections, conclusion chapters, proposal implications, and manuscript interpretation sections.

## Required Inputs

- specialized review pack
- draft Discussion text
- aims and Results summary
- marking scheme and section requirements
- source evidence index
- relevant prior literature pack
- `patterns/discussion/`

## Priority Rules

- Teacher rubric dominates.
- Domain interpretation is secondary and must be labeled.
- Official guidelines and corpus patterns support transparency and claim calibration.

## Evidence Rules

For every major critique, record whether it is based on rubric, official guideline, source pattern, domain heuristic, or provisional concern.

## Positive Patterns

- `DISC-P1`: answer the aim with calibrated interpretation.
- `DISC-P2`: integrate prior evidence without hiding conflict.
- `DISC-P3`: specific and consequential limitations.
- `DISC-P4`: implications match evidence type.
- `DISC-P5`: future work solves a specific limitation.
- `DISC-P6`: preclinical and animal model boundary.
- `DISC-P7`: prediction model interpretation boundary.
- `DISC-P8`: public-data association caveat.
- `DISC-P9`: real-world data limit boundary.
- `DISC-P10`: pan-cancer generalization boundary.
- `DISC-P11`: enrichment is hypothesis support.

## Negative Patterns

- results summary without interpretation;
- overstated translation;
- generic limitations;
- missing contradictory evidence;
- new unsourced claims.
- translational leap;
- prediction model readiness overclaim;
- public-data association treated as causal or validated;
- real-world data causal inflation;
- pan-cancer overgeneralization;
- enrichment treated as mechanism.

## Checklist

- Does the opening answer the aim?
- Are the main findings interpreted rather than merely repeated?
- Are limitations specific and linked to claims?
- Are alternative explanations or conflicting evidence acknowledged where important?
- Are clinical, mechanistic, or translational implications proportional to evidence?
- Does future work address a named unresolved limitation or gap?
- For preclinical work, are model limits and exploratory outcomes acknowledged before translation?
- For prediction models, are validation, calibration, discrimination, utility, and generalizability separated?
- For public-data analyses, are cohort/query/endpoints and validation status discussed?
- For registry or real-world data, are selection, linkage, missingness, endpoint, and confounding limits named before clinical implications?
- For pan-cancer analyses, are tumor-type heterogeneity, platform/cohort differences, and validation needs discussed?
- For pathway/enrichment or cluster/spatial claims, is mechanism separated from hypothesis support?

## Output Schema

```json
{
  "section": "discussion",
  "aim_answer_alignment": [],
  "interpretation_quality": [],
  "limitations_quality": [],
  "alternative_explanations": [],
  "claim_strength_flags": [],
  "rubric_alignment": [],
  "must_fix": [],
  "should_fix": [],
  "optional_polish": [],
  "evidence_links": []
}
```

## Known Failure Modes

- Rewarding a confident Discussion that overclaims.
- Demanding a full literature review when the rubric expects concise interpretation.
- Missing new claims introduced without source or result support.
- Treating high model performance as clinical readiness.
- Treating public cancer-genomics association as mechanism without experimental or validation support.
- Treating real-world or registry association as treatment effect without appropriate design evidence.
- Treating pan-cancer patterns as universally applicable across tumor types.
- Treating enrichment or cluster labels as direct mechanism.

## Uncertainty Handling

- Mark biomedical interpretation provisional when task-specific literature evidence is missing.
- Separate claim calibration from factual adjudication if source evidence is incomplete.
- Preserve alternative explanations and validation needs rather than forcing a stronger conclusion.

## Provenance Expectations

- Use rule IDs such as `DISCUSSION-R1-INTERPRET-WITH-LIMITS`, `DISCUSSION-R3-PRECLINICAL-MODEL-LIMITS`, `DISCUSSION-R4-PREDICTION-MODEL-LIMITS`, `DISCUSSION-R5-REAL-WORLD-DATA-LIMITS`, `DISCUSSION-R6-PANCANCER-GENERALIZATION-LIMITS`, `CLAIMS-R2-TRANSLATIONAL-EVIDENCE-LADDER`, and `CLAIMS-R4-ENRICHMENT-NOT-MECHANISM`.
- Cite source IDs for model, prediction, and public-data caveats.
- Do not use optional domain seed sources unless task specialization selects them.

## Stop Conditions

Stop or mark provisional if:

- Results or aims are unavailable;
- source evidence is insufficient to judge literature integration;
- marking scheme is missing and scoring is requested;
- the requested review asks for biomedical fact adjudication without sources.
