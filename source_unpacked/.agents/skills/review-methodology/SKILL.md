# Review Methodology

## Purpose

Evaluate Methods for reproducibility, design logic, controls, statistics, software/data provenance, parameters, and reporting-guideline fit.

## When To Use

Use after specialization for Methods, Materials and Methods, computational pipeline, systematic review methods, bioinformatics methods, or dissertation methodology chapters.

## Required Inputs

- `ReviewTaskSpec.json`
- `MarkingSchemeMap.json`
- section requirements and weights
- draft Methods text
- declared study design
- source evidence index
- relevant reporting guideline selected by design
- `patterns/methodology/`

## Priority Rules

- Teacher rubric dominates.
- Journal/reporting guidelines apply only when selected during specialization or clearly relevant to study design.
- Domain expertise is secondary and must not invent required methods.

## Evidence Rules

Every methods finding must identify whether it comes from rubric, official guideline, source pattern, domain heuristic, or provisional judgment.

## Positive Patterns

- `METH-P1`: reproducible detail.
- `METH-P2`: design before procedure.
- `METH-P3`: study-design guideline fit.
- `METH-P4`: analysis assumptions and uncertainty.
- `METH-P5`: ethical, access, and availability declarations.
- `METH-P6`: in vivo animal study transparency.
- `METH-P7`: biospecimen preanalytical reporting.
- `METH-P8`: key resource and access traceability.
- `METH-P9`: routinely collected data provenance.
- `METH-P10`: assay-specific minimum information.
- `METH-P11`: design-specific diagnostic and intervention detail.

## Negative Patterns

- irreproducible pipeline;
- ambiguous design;
- wrong reporting guideline;
- unreported statistical strategy;
- data/code availability gap.
- biospecimen context gap;
- vague access conditions;
- guideline overreach before study design is confirmed;
- irreconstructable registry cohort;
- assay name without assay conditions;
- wrong diagnostic or intervention checklist.

## Checklist

- Can the study design be named clearly?
- Are sample/data sources, inclusion/exclusion criteria, groups, and measurements defined?
- Are software, versions, databases, parameters, thresholds, and dependencies present where relevant?
- Is the statistical/computational plan sufficient to support Results?
- Are data, code, accession IDs, and availability statements present or justified as unavailable?
- Has the appropriate guideline been selected by design rather than topic?
- For animal studies, are ARRIVE-relevant design, bias-control, outcome, and animal details present?
- For human biospecimen studies, are preanalytical variables and unknown specimen factors reported?
- Are central resources identifiable through RRIDs, catalog numbers, accessions, stable URLs, or versions?
- For registry or routinely collected data, can the cohort, codes/algorithms, linkage, cleaning, and missingness be reconstructed?
- For qPCR or other platform-dependent assays, are assay-specific minimum-information details present?
- If diagnostic accuracy or intervention/comparator work is present, are STARD/TIDieR-style details applicable and present?

## Output Schema

```json
{
  "section": "methodology",
  "design_assessment": "",
  "reproducibility_gaps": [],
  "statistics_and_analysis_gaps": [],
  "data_code_availability_gaps": [],
  "rubric_alignment": [],
  "must_fix": [],
  "should_fix": [],
  "optional_polish": [],
  "evidence_links": []
}
```

## Known Failure Modes

- Demanding journal-level details when a dissertation rubric only asks for a conceptual methodology description.
- Missing bioinformatics reproducibility issues because prose sounds polished.
- Applying PRISMA, STROBE, or CONSORT without confirming study design.
- Applying ARRIVE, BRISQ, TRIPOD, or SAMPL solely because a topic is biomedical.
- Treating restricted access as misconduct instead of requesting precise access conditions.
- Treating a public registry or repository name as sufficient provenance.
- Applying qPCR, ENCODE, or other assay-specific minimum information outside the relevant assay type.
- Applying STARD to non-diagnostic biomarker work or TIDieR to non-intervention analysis.

## Uncertainty Handling

- Mark guideline-specific findings provisional until study design and task requirements are confirmed.
- Classify missing data/code/resource details as reproducibility or traceability risk unless the rubric makes them scoring requirements.
- Preserve legitimate privacy, ethics, licensing, or third-party constraints as limitations rather than automatic failures.

## Provenance Expectations

- Use rule IDs such as `METHODS-R1-REPRODUCIBLE-DETAIL`, `METHODS-R3-ANIMAL-STUDY-ARRIVE`, `METHODS-R4-BIOSPECIMEN-BRISQ`, `METHODS-R5-KEY-RESOURCE-TRACEABILITY`, `METHODS-R6-DATA-CODE-ACCESS-CONDITIONS`, `METHODS-R7-ROUTINE-DATA-PROVENANCE`, `METHODS-R8-QPCR-MINIMUM-INFORMATION`, and `METHODS-R9-DIAGNOSTIC-INTERVENTION-SCOPE`.
- Cite source IDs for all guideline-specific comments.
- Do not use source-pattern methods papers as mandates to use one software tool.

## Stop Conditions

Stop or mark provisional if:

- study design cannot be determined;
- rubric or section brief is absent and compliance review is requested;
- source, code, or data availability cannot be assessed from provided materials;
- the requested review would require fabricating methods details.
