# Results Failure Modes

## RES-F1: Discussion Disguised as Results

- What it looks like: paragraphs lead with implications, mechanisms, or clinical significance before presenting data.
- Why it hurts: weakens evidence flow and encourages overclaiming.
- How to detect it: interpretation verbs dominate before values, figures, or observations.
- Suggested revision action: reorder each paragraph around comparison -> evidence -> limited observation.

## RES-F2: Missing Numerical Support

- What it looks like: qualitative claims such as higher, lower, marked, or significant lack values, sample sizes, uncertainty, or tests.
- Why it hurts: readers cannot judge magnitude or reliability.
- How to detect it: comparative claims cannot be copied into a results table.
- Suggested revision action: add values, units, n, effect sizes, confidence intervals or adjusted p-values as appropriate.

## RES-F3: Orphan Result

- What it looks like: a result has no corresponding method, dataset, figure, table, or analysis plan.
- Why it hurts: makes the finding appear unsupported or accidental.
- How to detect it: Methods-to-Results trace table has a missing method or missing result cell.
- Suggested revision action: add the missing method, remove the unsupported result, or move exploratory material to an explicitly labeled subsection.

## RES-F4: Figure/Text Mismatch

- What it looks like: text, panel labels, legends, and statistical symbols do not agree.
- Why it hurts: confuses evidence and may signal data handling errors.
- How to detect it: group names, units, n values, or p-value symbols differ across text and figure.
- Suggested revision action: standardize labels and recheck every panel citation.

## RES-F5: Selective Reporting

- What it looks like: planned outcomes or obvious comparisons are absent without explanation.
- Why it hurts: raises bias and completeness concerns.
- How to detect it: aims/methods list analyses that never appear in Results.
- Suggested revision action: report the missing result, explain exclusion, or revise the aim/method to match actual scope.

## RES-F6: Hidden Denominator

- What it looks like: the result reports an effect or comparison but analyzed n, exclusions, missing data, or group definitions are unclear.
- Why it hurts: readers cannot judge magnitude, reliability, or possible selection bias.
- How to detect it: a result cannot be reconstructed into group-by-group counts or feature/sample denominators.
- Suggested revision action: add analyzed n, excluded cases, missing data note, and group definitions.

## RES-F7: Untraceable Plot

- What it looks like: a central plot or table cannot be linked to source data, supplementary table, repository accession, or script.
- Why it hurts: evidence cannot be verified or reused.
- How to detect it: reviewer cannot answer "what exact data generated this panel?"
- Suggested revision action: add source-data table, accession, code reference, or availability statement.

## RES-F8: Public Data Without Query Provenance

- What it looks like: a result cites GEO, GDC, TCGA, GENIE, cBioPortal, or another repository without study ID, access date/release, filters, sample counts, endpoint, profile, or normalization state.
- Why it hurts: readers cannot reproduce the result or judge cohort comparability.
- How to detect it: a second reviewer cannot rerun the public-data query from the Results and Methods.
- Suggested revision action: add repository, accession/study ID, query settings, case/sample counts, endpoint definitions, and data-processing state.

## RES-F9: Sex/Gender Blind Generalization

- What it looks like: composition or disaggregation is absent despite human, animal, cell, tissue, or translational context where sex/gender may matter.
- Why it hurts: conclusions may overgeneralize or hide untested heterogeneity.
- How to detect it: general claims are made while sex/gender composition is unknown or exclusions are unexplained.
- Suggested revision action: report composition, disaggregate when justified and powered, or state why the analysis is not applicable.

## RES-F10: Self-Evident Omics Plot

- What it looks like: a UMAP, heatmap, spatial map, pathway dot plot, or proteomics summary is presented without object provenance, counts, filtering, transformation, grouping, or analysis choices.
- Why it hurts: visual separation or enrichment can be driven by preprocessing and cannot be interpreted without provenance.
- How to detect it: a reviewer cannot say what exact matrix, cells/samples/features, transformation, and method generated the plot.
- Suggested revision action: add a plot provenance sentence and link to Methods, source-data table, or analysis object.
