# ASCReview Toy Biomedical Genomics Dry Run Report

## Metadata

- Task ID: `ASCREVIEW-TOY-BIOMED-0001`
- Draft version: `toy_biomed_genomics_draft.md`
- Draft stage: `early_draft`
- Review round: workflow dry run
- Specialization pack status: `toy_partial`
- Marking scheme source: `MarkingSchemeMap.toy_biomed.json`
- Dissertation review: not performed

## Executive Verdict

The generic ASCReview workflow correctly identifies this toy draft as reviewable only for workflow testing. The toy rubric supports limited formative scoring, but factual oncology and mechanism judgments remain provisional because the fixture has no real source pack, accession, code, analysis object, or figure files.

Estimated toy score: `21-27 / 50`, low confidence.

## Stop Conditions Checked

| Stop condition | Status | Note |
|---|---|---|
| Full draft scope defined | pass | Toy biomedical full-draft scope is explicit. |
| Marking scheme available for scored review | pass | Toy rubric is available and limited to this fixture. |
| Section weights available where needed | pass | Section weights sum to 50. |
| Dataset/accession available | provisional | Fictional dataset name only; no repository/accession/release. |
| Figures/legends available where relevant | partial | Legend text exists, but figure files and source data are absent. |
| Domain sources available for factual review | provisional | No real oncology source pack. |

## Section-Level Score Estimates

| Section | Estimated score | Confidence | Main risks | Priority |
|---|---:|---|---|---|
| Introduction | 5-6 / 8 | low | Aim is clear but factual background is unsourced. | should-fix |
| Methods | 4-6 / 16 | low | Dataset provenance, QC, normalization, annotation, enrichment method, software, and code are missing. | must-fix |
| Results | 4-6 / 12 | low | UMAP/spatial/pathway claims lack traceability; mechanism and pan-cancer claims overreach. | must-fix |
| Discussion | 6-8 / 10 | medium | Limitations are partly acknowledged, but claim calibration must be aligned with Results. | should-fix |
| Figures/legends | 2-3 / 4 | low | Legend lacks object provenance, counts, scales, and pathway method detail. | must-fix |

## Bioinformatics Reproducibility Audit

| Item | Status | Needed detail | Evidence tag | Rule IDs |
|---|---|---|---|---|
| Dataset provenance | absent | Repository, accession, release/access date, sample source. | `teacher_rubric` | `RESULTS-R6-PUBLIC-REPOSITORY-QUERY-TRACE` |
| scRNA-seq QC | absent | Cell/barcode filtering, QC covariates, doublet/ambient handling if relevant. | `source_pattern` | `BIOINFO-R6-SCRNASEQ-QC-ANNOTATION` |
| Spatial context | absent | Tissue image, coordinates, spot/cell resolution, segmentation or deconvolution method. | `source_pattern` | `BIOINFO-R7-SPATIAL-TRANSCRIPTOMICS-CONTEXT` |
| Enrichment method | absent | Gene universe, Reactome/database version, ranking/threshold, correction, redundancy handling. | `source_pattern` | `BIOINFO-R9-PATHWAY-ENRICHMENT-SCOPE` |
| Code/software | absent | Tools, versions, parameters, notebook or repository. | `source_pattern` | `BIOINFO-R1-CODE-DATA-AVAILABILITY` |

## Methods-To-Results Trace

| Result claim | Trace status | Problem | Evidence tag |
|---|---|---|---|
| Three clusters are tumor, immune, stromal | weak | Annotation method and marker evidence absent. | `source_pattern` |
| Immune cells are outside tumor region | weak | Spatial registration, resolution, and counts absent. | `source_pattern` |
| Cytokine mechanism blocks immune infiltration | unsupported | Enrichment and spatial association do not establish mechanism. | `source_pattern` |
| Across cancer types | unsupported | Toy sample is single fictional sample; pan-cancer support absent. | `source_pattern` |

## Figure And Legend Provenance

| Figure/panel | Status | Traceability need | Evidence tag | Rule IDs |
|---|---|---|---|---|
| UMAP | weak | Object provenance, cell count, embedding method, cluster annotation, color mapping. | `source_pattern` | `FIGURES-R5-EMBEDDING-SPATIAL-PLOT-DECODE` |
| Spatial map | weak | Tissue/image context, coordinate system, spot/cell resolution, registration method, scale. | `source_pattern` | `FIGURES-R5-EMBEDDING-SPATIAL-PLOT-DECODE` |
| Pathway dots | weak | Pathway database/version, background, correction, dot scale, directionality. | `source_pattern` | `FIGURES-R4-GENOMICS-QC-DECODABILITY` |

## Scientific Claim Calibration

| Claim | Evidence type | Support level | Calibration risk | Evidence tag | Source/rule IDs |
|---|---|---|---|---|---|
| Immune cells are outside tumor region | spatial association | weak/provisional | Requires spatial resolution and registration detail. | `source_pattern` | `BIOINFO-R7-SPATIAL-TRANSCRIPTOMICS-CONTEXT` |
| Cytokine mechanism blocks immune infiltration | mechanism | unsupported | Enrichment and co-localization do not demonstrate mechanism. | `source_pattern` | `CLAIMS-R4-ENRICHMENT-NOT-MECHANISM` |
| Across cancer types | pan-cancer generalization | unsupported | Single fictional sample cannot support cross-cancer language. | `source_pattern` | `DISCUSSION-R6-PANCANCER-GENERALIZATION-LIMITS` |

## Policy, Guideline, And Rubric Boundaries

- Teacher-rubric requirements: dataset provenance, reproducibility, figure decoding, and calibrated claims inside this toy fixture.
- Source-pattern support: single-cell QC, spatial context, pathway scope, figure provenance, claim calibration.
- Provisional comments: factual oncology and mechanism claims because no real source pack exists.

## Evidence Tags Used

- `teacher_rubric`: toy score estimate and required rubric elements.
- `source_pattern`: bioinformatics, figure, pathway, and claim-calibration checks.
- `provisional`: factual oncology claims without source evidence.

## Must-Fix Before Submission

1. Add repository/accession/release, sample/cell/spot counts, and data/source provenance.
2. Add QC/filtering, normalization, integration, clustering, annotation, and enrichment method details.
3. Decode UMAP, spatial map, and pathway dots in figure legends or Methods/supplement.
4. Replace "prove" and "across cancer types" claims with evidence-level calibrated wording.
5. Add source evidence or remove factual oncology mechanism claims.

## Draft-Stage Caveats

- Early-draft status allows missing code, source data, and source pack to be treated as must-fix development tasks rather than final-submission violations.
- The toy rubric and score are not portable to real dissertation review.
