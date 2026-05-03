# Good Methodology Patterns

## METH-P1: Reproducible Detail

- Description: Methods should include enough detail for a competent reader to understand and, where appropriate, reproduce the design, materials, data, software, parameters, thresholds, and analysis.
- When it applies: all empirical, computational, biomedical, and bioinformatics work.
- Source/provenance ID: `METHODS-R1-REPRODUCIBLE-DETAIL`; `GUIDE-MDAR-2021`; `PATTERN-REPRO-COMP-2013`; `JOURNAL-BIOINFORMATICS-AUTHOR-GUIDELINES`.
- Positive example summary: A pipeline description includes database release, software version, command-critical parameters, filtering thresholds, multiple-testing approach, and code/data availability.
- Failure mode: "standard pipeline was used" with no reproducible detail.
- Review checklist use: Try to list data, tools, versions, parameters, thresholds, and statistical tests from the section alone.

## METH-P2: Design Before Procedure

- Description: The section should first make the design logic clear, then describe procedures and analysis in an order that matches Results.
- When it applies: dissertations, articles, systematic reviews, wet-lab experiments, observational studies, and computational pipelines.
- Source/provenance ID: `GUIDE-STROBE-2007`; `GUIDE-CONSORT-2010`; `GUIDE-PRISMA-2020`; `GUIDE-EQUATOR-LIBRARY`.
- Positive example summary: Sample selection, inclusion/exclusion, measurement, and analysis are presented before detailed tools.
- Failure mode: procedural detail appears before the reader knows what design problem it solves.
- Review checklist use: Check whether study design, sample/data source, and analysis plan can be summarized before reading results.

## METH-P3: Study-Design Guideline Fit

- Description: Methods should be evaluated against the reporting guideline that matches the study design.
- When it applies: observational studies, randomized trials, systematic reviews, prognostic biomarker studies, prediction modeling, and genomics datasets.
- Source/provenance ID: `METHODS-R2-STUDY-DESIGN-GUIDELINE`.
- Positive example summary: A systematic review Methods section specifies search strategy, eligibility, selection, extraction, risk-of-bias, and synthesis plan.
- Failure mode: wrong guideline checklist is applied because the topic, not the design, drove selection.
- Review checklist use: Identify design first; then select STROBE, CONSORT, PRISMA, REMARK, TRIPOD, MDAR, MIAME/MINSEQE, or task-specific guidance.

## METH-P4: Analysis Assumptions and Uncertainty

- Description: Statistical and computational methods should state assumptions, comparison strategy, correction methods, validation approach, and criteria for interpreting results.
- When it applies: quantitative, bioinformatics, genomics, and biomedical experimental work.
- Source/provenance ID: `PATTERN-STAT-PRACTICE-2016`; `GUIDE-REMARK-2012`; `GUIDE-STROBE-2007`.
- Positive example summary: Differential expression analysis reports normalization, model, covariates, false-discovery correction, thresholds, and validation or sensitivity checks.
- Failure mode: p-values are reported later but test selection, correction, or assumptions are absent.
- Review checklist use: For every statistical claim in Results, locate the method that generated it.

## METH-P5: Ethical, Access, and Availability Declarations

- Description: Methods or associated declarations should identify approvals, data availability, repository IDs, code availability, and restrictions.
- When it applies: human data, public datasets, sequencing, software, and computational manuscripts.
- Source/provenance ID: `GUIDE-ICMJE-MANUSCRIPT`; `GUIDE-GEO-MIAME-MINSEQE`; `JOURNAL-BIOINFORMATICS-AUTHOR-GUIDELINES`.
- Positive example summary: Human dataset use explains approval/consent status where relevant, cites accession IDs, and states data/code access constraints.
- Failure mode: no accessions or availability statement for data-dependent conclusions.
- Review checklist use: Build an availability table for all data, code, software, and materials.

## METH-P6: In Vivo Animal Study Transparency

- Description: Animal-study Methods should report the design details needed to assess bias, reproducibility, and interpretation, including allocation, blinding, sample-size rationale, exclusions, outcomes, statistics, and animal characteristics.
- When it applies: in vivo animal experiments and preclinical animal-model dissertation chapters.
- Source/provenance ID: `METHODS-R3-ANIMAL-STUDY-ARRIVE`; `GUIDE-ARRIVE-2-2020`.
- Positive example summary: The Methods section identifies experimental units, randomization/blinding, inclusion/exclusion criteria, primary outcome, and statistical plan before presenting animal results.
- Failure mode: animal details and bias controls are omitted while translational conclusions are later made.
- Review checklist use: Run ARRIVE applicability only after specialization confirms an animal study.
- When it does not apply: cell-line-only, computational-only, human-only, or literature-only projects.

## METH-P7: Biospecimen Preanalytical Reporting

- Description: Human biospecimen studies should describe relevant specimen type, anatomical source, disease and pathology context, collection, stabilization, preservation, and unknown preanalytical factors.
- When it applies: cancer biomarker, pathology, tissue, blood, cfDNA, biobank, and human-sample assays.
- Source/provenance ID: `METHODS-R4-BIOSPECIMEN-BRISQ`; `GUIDE-BRISQ-2011`.
- Positive example summary: A biomarker Methods section states tissue source, diagnosis/pathology context, preservation method, and known missing specimen metadata.
- Failure mode: biomarker findings are interpreted without specimen handling context.
- Review checklist use: Ask which sample-handling factors could alter the measured molecule or assay.
- When it does not apply: studies without human biospecimens or where the rubric only requests a high-level conceptual plan.

## METH-P8: Key Resource and Access Traceability

- Description: Central resources should be identifiable through RRIDs, catalog numbers, accessions, software versions, stable URLs, repository records, or controlled-access explanations.
- When it applies: wet-lab, bioinformatics, genomics, figures generated by code, and public-dataset work.
- Source/provenance ID: `METHODS-R5-KEY-RESOURCE-TRACEABILITY`; `METHODS-R6-DATA-CODE-ACCESS-CONDITIONS`.
- Positive example summary: A Methods table lists antibody RRID, cell-line authentication/source, software version, dataset accession, code repository, and restrictions where relevant.
- Failure mode: named resources cannot be uniquely identified or accessed.
- Review checklist use: For each central resource, ask "could another researcher identify the same item or data source?"
- When it does not apply: purely conceptual essays without empirical resources.

## METH-P9: Routinely Collected Data Provenance

- Description: Registry, electronic-record, and routinely collected health-data Methods should report source systems, linkage logic, phenotype/code definitions, inclusion/exclusion logic, cleaning steps, missingness, and access conditions.
- When it applies: observational studies using registry, electronic health record, insurance/administrative, clinico-genomic, or public real-world datasets.
- Source/provenance ID: `METHODS-R7-ROUTINE-DATA-PROVENANCE`; `GUIDE-RECORD-2015`.
- Positive example summary: A database study states the data source, date range, code list or algorithm, linkage variables, cleaning/exclusion flow, missing-data handling, and whether the data were collected for care rather than research.
- Failure mode: a registry association appears reproducible only in principle because the cohort construction cannot be reconstructed.
- Review checklist use: Ask whether another reader could rebuild the same cohort and variables from the stated database fields.
- When it does not apply: primary wet-lab experiments, narrative reviews, or public-data analyses that do not use routinely collected health records.

## METH-P10: Assay-Specific Minimum Information

- Description: Assay-specific methods should include the minimum information needed to judge technical validity, not only the name of the assay.
- When it applies: qPCR/RT-qPCR, sequencing, public omics reuse, antibody-based assays, and other platform-dependent biomedical methods.
- Source/provenance ID: `METHODS-R8-QPCR-MINIMUM-INFORMATION`; `GUIDE-MIQE-2009`; `RESOURCE-ENCODE-DATA-STANDARDS`.
- Positive example summary: A qPCR validation section reports sample handling, RNA quality, primer/probe identity, normalization/reference strategy, reaction conditions, and replicate handling.
- Failure mode: a molecular validation claim rests on an assay name with no conditions, controls, or normalization rationale.
- Review checklist use: Identify the assay family first, then check the relevant minimum-information fields; do not apply qPCR-specific fields to unrelated assays.
- When it does not apply: conceptual writing without assay-generated evidence.

## METH-P11: Design-Specific Diagnostic and Intervention Detail

- Description: Diagnostic accuracy studies and intervention/comparator studies require design-specific details before their results can be evaluated.
- When it applies: diagnostic index-test/reference-standard studies, intervention studies, comparator arms, treatment protocols, and implementation-like methods.
- Source/provenance ID: `METHODS-R9-DIAGNOSTIC-INTERVENTION-SCOPE`; `GUIDE-STARD-2015`; `GUIDE-TIDIER-2014`.
- Positive example summary: A diagnostic study names participant selection, index test, reference standard, timing, and accuracy estimates; an intervention study names materials, provider, mode, dose/intensity, tailoring, comparator, and fidelity.
- Failure mode: a test or intervention is named but cannot be reproduced or evaluated because essential design-specific details are absent.
- Review checklist use: Identify whether the work is diagnostic accuracy, intervention description, both, or neither before applying STARD/TIDieR-derived checks.
- When it does not apply: exploratory omics analyses, mechanistic experiments, narrative reviews, or non-intervention dissertations.

## METH-P12: Modality-Specific Computational Routing

- Description: Computational and omics Methods should first name the data modality and acquisition/analysis family before applying modality-specific reporting expectations.
- When it applies: single-cell multimodal, AIRR-seq, long-read sequencing, DIA/DDA proteomics, phosphoproteomics, spatial transcriptomics, and imaging-based spatial methods.
- Source/provenance ID: `BIOINFO-R10-SC-MULTIMODAL-ROUTING`; `BIOINFO-R11-AIRR-METADATA-ANNOTATION`; `BIOINFO-R12-LONG-READ-PLATFORM-QC`; `BIOINFO-R13-DIA-DDA-PROTEOMICS-MODE`; `BIOINFO-R14-PHOSPHOPROTEOMICS-SITE-INFERENCE`.
- Positive example summary: A Methods section states that paired scRNA/scATAC data were integrated, AIRR sequences used a named germline reference, long reads used a specific basecaller and polishing route, DIA proteomics used a defined library strategy, or phosphoproteomics used a site-localization threshold.
- Failure mode: a draft uses modality labels as if they were self-explanatory and omits the acquisition, preprocessing, or inference details that make the method reviewable.
- Review checklist use: Route the method by modality first, then apply the matching checklist; do not import irrelevant fields from another modality.
- When it does not apply: purely conceptual writing, ordinary non-omics statistics, or modalities outside the verified corpus.
