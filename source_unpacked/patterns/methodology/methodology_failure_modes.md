# Methodology Failure Modes

## METH-F1: Irreproducible Pipeline

- What it looks like: software, databases, versions, filters, parameters, or scripts are missing.
- Why it hurts: undermines reproducibility and weakens trust in downstream results.
- How to detect it: a reader cannot rerun or audit the analysis from the method description and source links.
- Suggested revision action: add a pipeline table with tool, version, purpose, input, output, key parameters, and repository/accession.

## METH-F2: Study Design Ambiguity

- What it looks like: the section describes actions but not the design, sample/data source, inclusion/exclusion logic, or comparison groups.
- Why it hurts: results cannot be interpreted against a valid design.
- How to detect it: the design cannot be named after reading the first methods paragraphs.
- Suggested revision action: add a design overview before procedural details.

## METH-F3: Wrong Reporting Guideline

- What it looks like: the review uses a guideline because the topic seems biomedical, not because the study design matches it.
- Why it hurts: creates irrelevant criticism and misses real reporting duties.
- How to detect it: no explicit study-type decision connects the guideline to the work.
- Suggested revision action: run guideline selection through EQUATOR/study-design routing during specialization.

## METH-F4: Unreported Statistical Strategy

- What it looks like: Results include statistical significance, models, or thresholds that Methods did not define.
- Why it hurts: makes numerical claims impossible to audit.
- How to detect it: each p-value, confidence interval, model output, or adjusted value lacks a corresponding methods explanation.
- Suggested revision action: add test/model rationale, assumptions, adjustment strategy, and interpretation thresholds.

## METH-F5: Data/Code Availability Gap

- What it looks like: claims rely on external data or code but no repository, accession, license, or access constraint is stated.
- Why it hurts: prevents verification and may violate journal or dissertation expectations.
- How to detect it: data/software names appear without stable identifiers or availability statements.
- Suggested revision action: add accessions, repository links, citation details, or a justified restriction statement.

## METH-F6: Biospecimen Context Gap

- What it looks like: human tissue, blood, cfDNA, or biobank-derived samples are used without specimen type, site, disease/pathology context, collection, stabilization, or preservation details.
- Why it hurts: preanalytical variables can affect molecular measurements and comparability.
- How to detect it: assay results depend on biospecimens but the sample lifecycle cannot be reconstructed.
- Suggested revision action: add a biospecimen metadata table and explicitly acknowledge unknown handling factors.

## METH-F7: Vague Access Conditions

- What it looks like: "data available on request" or "public database was used" appears without repository, access conditions, restrictions, identifiers, or third-party limits.
- Why it hurts: readers cannot verify or reuse the evidence base.
- How to detect it: availability statements lack persistent IDs, URLs, conditions, or responsible access route.
- Suggested revision action: state repository/accession, controlled-access conditions, restriction reason, and access mechanism.

## METH-F8: Guideline Overreach

- What it looks like: a review applies ARRIVE, TRIPOD, PRISMA, CONSORT, or BRISQ because the topic is biomedical rather than because the design requires it.
- Why it hurts: generates irrelevant criticism and hides real design-specific reporting gaps.
- How to detect it: no specialization artifact records the study-design decision.
- Suggested revision action: downgrade guideline comments to provisional until design is confirmed.

## METH-F9: Irreconstructable Registry Cohort

- What it looks like: a registry or routinely collected dataset is named, but source systems, linkage logic, code/phenotype definitions, missingness, cleaning, or exclusion flow are absent.
- Why it hurts: associations cannot be reproduced or judged for selection and measurement bias.
- How to detect it: the reviewer cannot rebuild the cohort definition or variable construction from the Methods.
- Suggested revision action: add a cohort-construction table with data source, access date, code lists, linkage, exclusions, and missing-data handling.

## METH-F10: Assay Name Without Assay Conditions

- What it looks like: qPCR, sequencing, antibody, or imaging methods are named without sample quality, controls, reagent identity, normalization, platform, or analysis conditions.
- Why it hurts: readers cannot judge whether the assay supports the result.
- How to detect it: the same high-level assay name could describe many technically different experiments.
- Suggested revision action: add assay-specific minimum information and justify unavailable details.

## METH-F11: Wrong Diagnostic or Intervention Checklist

- What it looks like: STARD-style diagnostic checks are applied to a non-diagnostic biomarker project, or TIDieR-style intervention checks are applied to a purely observational or omics analysis.
- Why it hurts: creates irrelevant criticism and misses the real design-specific gaps.
- How to detect it: the review cannot name the index test/reference standard or intervention/comparator before invoking the checklist.
- Suggested revision action: confirm study design first, then apply STARD or TIDieR only if the design matches.

## METH-F12: Modality Checklist Leakage

- What it looks like: single-cell, AIRR, long-read, DIA/SWATH, phosphoproteomics, or multiplexed imaging expectations are applied because the topic sounds omics-heavy, not because the actual modality requires them.
- Why it hurts: creates irrelevant criticism while missing the real reproducibility and interpretation gaps for the method actually used.
- How to detect it: no routing decision identifies the data modality, acquisition mode, platform, or analysis family before checklist application.
- Suggested revision action: add a modality-routing table and apply only the checklist justified by the confirmed modality and review scope.
