# Good Results Patterns

## RES-P1: Evidence Before Interpretation

- Description: Results should report findings, numbers, comparisons, statistics, and figure/table links before broad interpretation.
- When it applies: empirical dissertation sections, biomedical articles, computational analyses, and results chapters.
- Source/provenance ID: `RESULTS-R1-EVIDENCE-BEFORE-INTERPRETATION`.
- Positive example summary: A paragraph begins with the tested comparison, reports values/effects/uncertainty, cites the figure panel, then states a limited observation.
- Failure mode: mechanistic interpretation appears before the data are shown.
- Review checklist use: Mark each sentence as evidence, observation, or interpretation; interpretation should not dominate.

## RES-P2: Results Follow Methods

- Description: Each result should trace back to a described method, dataset, assay, model, or analysis.
- When it applies: all empirical and computational work.
- Source/provenance ID: `RESULTS-R2-EXTRACTABLE-NUMBERS`; `METHODS-R1-REPRODUCIBLE-DETAIL`.
- Positive example summary: The result sequence mirrors the analysis pipeline or experimental logic introduced in Methods.
- Failure mode: a figure or result appears with no method, group definition, or statistical plan.
- Review checklist use: Create a Methods-to-Results trace table.

## RES-P3: Extractable Quantitative Claims

- Description: Important quantitative findings should include the needed values, units, sample sizes, effect sizes, uncertainty, thresholds, and statistical tests.
- When it applies: quantitative biomedical, bioinformatics, and dissertation results.
- Source/provenance ID: `GUIDE-EQUATOR-WRITING`; `GUIDE-STROBE-2007`; `GUIDE-CONSORT-2010`.
- Positive example summary: A comparison reports group labels, n, effect direction, effect size or summary value, confidence interval or adjusted p-value where appropriate.
- Failure mode: "significantly increased" without values, tests, or sample sizes.
- Review checklist use: Highlight every comparative adjective and check whether the numbers support it.

## RES-P4: Figure-Text Consistency

- Description: Text should cite figure panels in logical order and describe what the panel actually shows.
- When it applies: any result that depends on visual data.
- Source/provenance ID: `FIGURES-R1-STANDALONE-LEGEND`; `PATTERN-BETTER-FIGURES-2014`.
- Positive example summary: Text discusses Figure 2A before Figure 2B and uses the same group names, units, and statistical symbols as the legend.
- Failure mode: text claims a result not visible in the panel or cites panels out of order.
- Review checklist use: For each paragraph, list cited panels and compare terms, units, and claims.

## RES-P5: Negative and Null Results Are Still Results

- Description: Non-significant, failed, or null findings should be reported clearly when they answer the aim, constrain interpretation, or affect the conclusion.
- When it applies: empirical and computational work with planned analyses.
- Source/provenance ID: `PATTERN-STAT-PRACTICE-2016`; `GUIDE-STROBE-2007`.
- Positive example summary: The result reports absence of an expected association with enough information to interpret uncertainty and limitations.
- Failure mode: inconvenient null findings disappear but reappear as limitations in Discussion without evidence.
- Review checklist use: Compare aims/methods to reported outcomes; flag planned results that are missing.

## RES-P6: Denominators and Exclusions Stay Visible

- Description: Results should preserve analyzed denominators, exclusions, missing data, and group definitions when these affect the interpretation of an experiment, cohort, animal study, or computational analysis.
- When it applies: quantitative biomedical, clinical, animal, observational, and high-throughput analyses.
- Source/provenance ID: `RESULTS-R3-DENOMINATORS-EXCLUSIONS`.
- Positive example summary: A result paragraph reports analyzed n per group and notes excluded samples or failed quality-control cases.
- Failure mode: effect sizes or plots appear without knowing what was included or excluded.
- Review checklist use: Match every figure/result to analyzed sample count and exclusion logic.
- When it does not apply: purely conceptual discussion or qualitative synthesis where denominators are not relevant.

## RES-P7: Underlying Data Trace

- Description: Central results should be traceable to underlying data values, supplementary tables, repository accessions, or code/data availability statements when verification depends on them.
- When it applies: figure-heavy, genomics, bioinformatics, public-data, and statistical analyses.
- Source/provenance ID: `RESULTS-R4-UNDERLYING-DATA-TRACE`.
- Positive example summary: A volcano plot is paired with a supplementary result table, dataset accession, and method/code reference.
- Failure mode: a major figure supports the conclusion but the plotted data or source table is unavailable.
- Review checklist use: For each main claim, locate the data artifact that lets a reader verify it.
- When it does not apply: formative drafts where repositories are not yet expected; still mark as pre-submission risk if relevant.

## RES-P8: Public Repository Query Trace

- Description: Results based on public genomics or cancer data repositories should report enough query provenance to reconstruct the cohort, molecular profile, endpoint, filters, and transformed values.
- When it applies: GEO, GDC, TCGA, GENIE, cBioPortal, ENCODE, or similar public-data analyses.
- Source/provenance ID: `RESULTS-R6-PUBLIC-REPOSITORY-QUERY-TRACE`.
- Positive example summary: A survival or alteration result states repository, study ID, data release/access date, profile, endpoint definition, filters, sample/case count, and validation status.
- Failure mode: a result cites a portal or dataset name but not the cohort/query that generated the plotted value.
- Review checklist use: Ask whether a second reviewer could rerun the same query and obtain the same result.
- When it does not apply: primary experiments with locally generated data unless those data are deposited in a repository.

## RES-P9: Relevance-Gated Sex/Gender Reporting

- Description: When sex, gender, or sex-derived biological material is relevant, Results should report composition, disaggregation, exclusions, or a justification for why such analysis is not informative.
- When it applies: human studies, animal studies, cell/tissue studies, and translational claims where sex/gender could affect interpretation.
- Source/provenance ID: `RESULTS-R5-SEX-GENDER-RELEVANCE`; `GUIDE-SAGER-2016`.
- Positive example summary: A cohort result reports sex distribution and either disaggregates relevant outcomes or explains why the analysis was not powered or applicable.
- Failure mode: general biological or clinical claims hide composition or exclusions.
- Review checklist use: Decide relevance first; then check reporting. Do not demand sex/gender analysis where it is not biologically, clinically, or methodologically relevant.
- When it does not apply: irrelevant contexts or drafts where the task explicitly scopes out sex/gender analysis.

## RES-P10: High-Dimensional Plot Trace

- Description: Embeddings, clusters, spatial domains, heatmaps, pathway plots, and proteogenomic summaries should be traceable to their analysis object, transformations, sample/cell/feature counts, grouping, and key analysis choices.
- When it applies: single-cell, spatial transcriptomics, proteomics, pathway/enrichment, pan-cancer, and other high-dimensional analyses.
- Source/provenance ID: `RESULTS-R7-HIGH-DIMENSIONAL-PLOT-TRACE`.
- Positive example summary: A UMAP result states cells/samples included, filtering/QC state, embedding method, cluster annotation source, marker testing, and where the analysis object or source table can be found.
- Failure mode: a high-dimensional visual result is treated as self-evident and cannot be traced back to methods or source data.
- Review checklist use: For each plotted conclusion, identify the object, counts, transformation, grouping, and source-data path.
- When it does not apply: simple descriptive results without high-dimensional plots or computational summaries.
