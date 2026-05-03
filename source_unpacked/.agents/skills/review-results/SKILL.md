# Review Results

## Purpose

Evaluate whether Results present evidence clearly, quantitatively, and in a sequence that follows Methods and supports later interpretation.

## When To Use

Use after specialization for Results sections, result chapters, figure-driven empirical sections, and computational analysis outputs.

## Required Inputs

- specialized review pack
- draft Results text
- Methods section or methods summary
- figures, tables, legends, or descriptions
- marking scheme and section requirements
- source evidence index
- `patterns/results/`

## Priority Rules

- Teacher rubric and section requirements dominate.
- Domain expertise can flag overinterpretation and statistical concerns, but must be labeled secondary.
- If scoring is requested, only score where the rubric supports it.

## Evidence Rules

Each finding should state whether the problem is a rubric issue, guideline issue, source-pattern issue, or scientific-claim issue.

## Positive Patterns

- `RES-P1`: evidence before interpretation.
- `RES-P2`: results follow methods.
- `RES-P3`: extractable quantitative claims.
- `RES-P4`: figure-text consistency.
- `RES-P5`: negative and null results are still results.
- `RES-P6`: denominators and exclusions stay visible.
- `RES-P7`: underlying data trace.
- `RES-P8`: public repository query trace.
- `RES-P9`: relevance-gated sex/gender reporting.
- `RES-P10`: high-dimensional plot trace.

## Negative Patterns

- discussion disguised as results;
- missing numerical support;
- orphan result;
- figure/text mismatch;
- selective reporting.
- hidden denominator;
- untraceable plot or source data;
- public data without query provenance;
- sex/gender blind generalization;
- self-evident omics plot.

## Checklist

- Does each result trace to a method, dataset, analysis, figure, or table?
- Are comparisons supported by values, units, n, uncertainty, and tests where needed?
- Are figures cited in order and accurately described?
- Are result paragraphs organized around evidence before interpretation?
- Are planned aims or methods missing corresponding results?
- Are null or negative results reported when they matter?
- Are analyzed n, exclusions, missing data, and group definitions visible where they affect interpretation?
- Can central result claims be traced to source data, supplementary tables, accessions, or code/data availability statements?
- For public repository analyses, are repository, study/accession ID, access date/release, filters, endpoints, and transformed values reported?
- Where sex/gender relevance is established, are composition, disaggregation, exclusions, or non-applicability justified?
- For embeddings, clusters, spatial maps, heatmaps, pathway plots, or proteogenomic summaries, is the plotted object and transformation traceable?

## Output Schema

```json
{
  "section": "results",
  "methods_results_trace": [],
  "figure_text_consistency": [],
  "quantitative_reporting_gaps": [],
  "overinterpretation_flags": [],
  "rubric_alignment": [],
  "must_fix": [],
  "should_fix": [],
  "optional_polish": [],
  "evidence_links": []
}
```

## Known Failure Modes

- Editing for style while ignoring missing statistics or figure mismatches.
- Treating all interpretation as forbidden even when local convention allows brief result-level interpretation.
- Missing selective reporting because Methods were not read.
- Accepting a plot as evidence without asking for denominators, exclusions, or underlying data trace.
- Treating repository readiness as a final-submission requirement in an early formative draft without noting scope.
- Treating a public database name as a reproducible query.
- Demanding sex/gender analysis without first establishing relevance and feasibility.
- Accepting UMAP, spatial, pathway, or proteomics plots without object/count/transformation provenance.

## Uncertainty Handling

- Mark figure/data trace comments provisional if figures, source data, or supplementary tables are absent.
- Distinguish missing reporting in the draft from invalid underlying analysis.
- Do not infer sample counts or excluded cases.

## Provenance Expectations

- Use rule IDs such as `RESULTS-R1-EVIDENCE-BEFORE-INTERPRETATION`, `RESULTS-R3-DENOMINATORS-EXCLUSIONS`, `RESULTS-R4-UNDERLYING-DATA-TRACE`, `RESULTS-R5-SEX-GENDER-RELEVANCE`, `RESULTS-R6-PUBLIC-REPOSITORY-QUERY-TRACE`, and `RESULTS-R7-HIGH-DIMENSIONAL-PLOT-TRACE`.
- Link numerical-reporting comments to selected study-design guidance when specialization confirms applicability.
- Record whether a finding is a rubric issue, guideline issue, source-pattern issue, or provisional scientific risk.

## Stop Conditions

Stop or mark provisional if:

- Methods or figure/table material needed to verify Results is absent;
- the marking scheme is missing and scoring is requested;
- figure claims cannot be checked because figures/legends are unavailable;
- numerical claims require source data not provided.
