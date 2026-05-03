# Assess Bioinformatics Methods

## Purpose

Evaluate bioinformatics and genomics methods for reproducibility, data provenance, software/code availability, parameter reporting, statistics, and interpretation limits.

## When To Use

Use for computational biology, genomics, transcriptomics, sequencing, survival analysis, biomarker, enrichment, machine learning, or public-dataset analyses.

## Required Inputs

- specialized review pack
- Methods and Results text
- data source list and accessions, if available
- pipeline/software list, if available
- figures and legends for computational plots
- marking scheme
- source evidence index

## Priority Rules

- Teacher rubric dominates.
- Journal/software/data standards inform scientific risk but do not override the rubric.
- Domain expertise is secondary and must be labeled.

## Evidence Rules

High-confidence findings should cite official guidelines or verified corpus sources such as `JOURNAL-BIOINFORMATICS-AUTHOR-GUIDELINES`, `GUIDE-GEO-MIAME-MINSEQE`, or `PATTERN-REPRO-COMP-2013`.

## Positive Patterns

- public datasets have accession IDs and release/version information;
- software and packages have versions;
- parameters, thresholds, and filtering criteria are stated;
- statistical tests and correction methods match the data structure;
- code/data availability is clear or restrictions are justified;
- computational figures can be traced to source data and scripts;
- RNA-seq or omics pipelines report QC, annotation, normalization, filtering, covariates, model structure, and contrasts;
- public repository analyses report study/accession IDs, release/access dates, filters, and endpoint definitions;
- single-cell analyses expose QC, filtering, annotation, clustering, marker testing, and analysis-object provenance;
- multimodal single-cell analyses identify which modalities were measured, whether modalities are paired or integrated, and how modality-specific preprocessing was handled;
- adaptive immune receptor repertoire analyses expose MiAIRR/AIRR-style sample, receptor, annotation, repository, and tool provenance;
- long-read sequencing analyses expose platform, chemistry, basecalling, read-length/quality, error-correction, alignment/assembly, coverage, and validation context;
- spatial transcriptomics analyses expose tissue/image context, coordinates, segmentation or deconvolution, resolution, and spatial statistics;
- proteomics analyses expose repository accession, sample metadata, raw/processed files, instrument/search or processing workflow, and peptide/protein inference level;
- DIA/DDA proteomics analyses identify acquisition mode, spectral library or library-free strategy, scoring/search workflow, FDR, missingness, and inference level;
- phosphoproteomics analyses identify enrichment, phosphorylation-site localization confidence, protein-level normalization where relevant, kinase/pathway inference, and validation status;
- pathway/enrichment analyses expose background set, resource version, correction, redundancy handling, and exploratory status.

## Negative Patterns

- missing accession IDs;
- undocumented pipeline steps;
- no version/parameter reporting;
- multiple testing correction absent or unclear;
- no validation or sensitivity checks for exploratory findings;
- code/data described as available only on request without justification.
- RNA-seq design matrix, normalization, filtering, or multiple-testing choices absent;
- public cancer-genomics portal query lacks cohort, data release, filters, or endpoint definition;
- exploratory computational association presented as validated mechanism;
- model design, contrasts, covariates, or batch handling absent;
- polished omics figure hides normalization, transformation, or filtering;
- single-cell cluster, trajectory, or cell-type claim lacks QC/annotation evidence;
- multimodal single-cell integration hides modality pairing, integration assumptions, or modality-specific preprocessing;
- AIRR-seq clonotype, diversity, or disease-signature claims lack receptor-chain, annotation, germline-reference, or metadata provenance;
- long-read variant, isoform, methylation, or assembly claims omit platform-specific error/QC/basecalling context;
- spatial neighborhood claim lacks coordinate/image/segmentation or deconvolution context;
- proteomics result cites a repository without accession, metadata, or processing provenance;
- DIA/SWATH/DDA labels are used without acquisition, scoring, library, FDR, missingness, or inference-level detail;
- phosphoproteomic signaling claims lack site-localization, normalization, kinase-inference, or validation context;
- pathway enrichment presented as mechanism without validation.

## Checklist

- What raw data, processed data, and metadata were used?
- Are accessions, repositories, or dataset versions listed?
- Are tools, packages, versions, and parameters listed?
- Is the normalization/filtering strategy explained?
- Are statistical tests, covariates, correction methods, and thresholds reported?
- Can figures/results be reproduced from the described workflow?
- Are claims calibrated to computational evidence strength?
- For RNA-seq or count-data analysis, are sample/replicate structure, design model, normalization, filtering, dispersion/fold-change handling, and multiple-testing correction reported?
- For cBioPortal or other public cancer-genomics portals, are study ID, cohort filters, data profile, query settings, endpoint definitions, and validation status reported?
- Are public datasets cited with accessions, release dates, or persistent identifiers where possible?
- Does each model-based omics claim map to a stated design matrix/model, contrast, covariates, and biological comparison?
- Do omics figures expose QC, normalization/transformation, filtering, scale, and source-data traceability?
- For scRNA-seq, are cell/barcode filtering, QC covariates, doublet/ambient handling, normalization, integration, clustering, and annotation evidence reported?
- For multimodal single-cell analysis, are modalities, pairing/integration design, modality-specific preprocessing, and benchmark-dependent choices reported?
- For AIRR-seq or immune-repertoire analysis, are sample metadata, receptor chain/locus, annotation fields, germline reference, repository representation, and tool provenance reported?
- For long-read sequencing, are platform/chemistry, basecaller, read length/quality, coverage, error correction, alignment/assembly, caller, and validation or benchmark context reported?
- For spatial transcriptomics, are tissue/image context, coordinates, resolution, segmentation/deconvolution, and spatial statistics reported?
- For proteomics/proteogenomics, are accessions, raw/processed files, metadata, processing workflow, and protein/peptide inference levels reported?
- For DIA/DDA/targeted proteomics, is acquisition mode routed correctly and are quantification, scoring/search, FDR, missingness, and inference levels described?
- For phosphoproteomics, are enrichment, site localization, normalization to protein abundance where relevant, kinase/pathway inference, and validation status described?
- For pathway/enrichment analysis, are gene universe/background, database/version, ranking/threshold, correction, redundancy, and directionality reported?

## Output Schema

```json
{
  "bioinformatics_methods_review": {
    "modality_routing": [],
    "data_provenance": [],
    "software_and_code": [],
    "parameters_and_thresholds": [],
    "statistics": [],
    "figure_provenance": [],
    "claim_strength": []
  },
  "must_fix": [],
  "should_fix": [],
  "optional_polish": [],
  "missing_information": []
}
```

## Known Failure Modes

- Accepting named tools without versions or parameters.
- Treating public database use as inherently reproducible.
- Ignoring multiple testing and exploratory analysis limits.
- Applying a software-paper standard to a dissertation unless rubric or review scope warrants it.
- Mandating DESeq2 or cBioPortal because they are in the corpus rather than checking the method actually used.
- Treating public cancer-genomics exploratory findings as validated clinical conclusions.
- Treating limma, DESeq2, SEQC, or RNA-seq best-practices papers as required methods rather than reporting-pattern evidence.
- Missing analysis drift when model design or contrasts are changed but downstream claims remain unchanged.
- Treating Scanpy, single-cell best-practice tutorials, or spatial transcriptomics reviews as required pipelines.
- Treating Reactome/PRIDE/CPTAC/GDC/GENIE presence as sufficient validation rather than provenance.
- Treating a multimodal single-cell best-practice source as a mandatory integration algorithm.
- Applying AIRR metadata expectations to ordinary immune marker expression or non-repertoire immunology.
- Treating long-read sequencing as automatically more valid than short-read sequencing without platform, coverage, error, and validation context.
- Applying DIA/SWATH expectations to DDA, TMT, targeted, or other proteomics designs.
- Treating phosphorylation-site abundance or kinase enrichment as demonstrated causal signaling without validation.

## Uncertainty Handling

- Mark missing pipeline details as reproducibility risk, not automatic invalidity.
- Mark tool-specific critique provisional unless the tool or analysis class is confirmed.
- Preserve privacy, controlled-access, and third-party data restrictions as limitations.

## Provenance Expectations

- Use rule IDs such as `BIOINFO-R1-CODE-DATA-AVAILABILITY`, `BIOINFO-R2-RNASEQ-DESIGN-REPORTING`, `BIOINFO-R3-PUBLIC-CANCER-PORTAL-PROVENANCE`, `BIOINFO-R4-RNASEQ-PIPELINE-QC`, `BIOINFO-R5-DESIGN-MATRIX-CONTRASTS`, `BIOINFO-R6-SCRNASEQ-QC-ANNOTATION`, `BIOINFO-R7-SPATIAL-TRANSCRIPTOMICS-CONTEXT`, `BIOINFO-R8-PROTEOMICS-REPOSITORY-METADATA`, `BIOINFO-R9-PATHWAY-ENRICHMENT-SCOPE`, `BIOINFO-R10-SC-MULTIMODAL-ROUTING`, `BIOINFO-R11-AIRR-METADATA-ANNOTATION`, `BIOINFO-R12-LONG-READ-PLATFORM-QC`, `BIOINFO-R13-DIA-DDA-PROTEOMICS-MODE`, and `BIOINFO-R14-PHOSPHOPROTEOMICS-SITE-INFERENCE`.
- Cite method source IDs only as pattern support, not mandates to choose a specific tool.
- Record data release/access dates for public resources during task specialization.

## Stop Conditions

Stop or mark provisional if:

- pipeline or dataset information is absent;
- methods/results/figures cannot be connected;
- source evidence is insufficient for domain-specific claims;
- scoring is requested without rubric criteria.
