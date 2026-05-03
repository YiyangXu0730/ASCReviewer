# ASCReview Adversarial QC Report

## Scope

This report records the build-time LibraryBuilder-Distiller -> AdversarialAuditor -> Arbiter-Integrator loop for ASCReview Core, corpus patterns, distilled skills, non-dissertation toy fixtures, and validation harness behavior.

The user's dissertation was not reviewed.

## Current Counts

- Source records: 65
- Provenance rules: 58
- Distillation/adversarial rounds: 58
- Skills: 9 root skills mirrored to `.agents/skills`

## Minimum Cycle Coverage

| Skill family | Required rounds | Completed rounds | Status |
|---|---:|---:|---|
| Introduction | 2 | 4 | exceeded |
| Methodology | 2 | 7 | exceeded |
| Results | 2 | 7 | exceeded |
| Discussion | 2 | 6 | exceeded |
| Figures/legends | 2 | 7 | exceeded |
| Rubric alignment | 1 | 3 | exceeded |
| Revision round compare | 1 | 4 | exceeded |
| Bioinformatics methods | 2 | 14 | exceeded because domain priority is high |
| Scientific claim strength | extra | 2 dedicated rounds | also audited inside discussion, bioinformatics, and revision rounds |
| Non-dissertation toy fixtures | extra | 4 rounds | added as regression harness coverage |

## Main Accepted Rules

- The specialization gate must run before any review.
- The specialization input contract must record draft, marking scheme, figures/assets, source constraints, and assessment context before enabling the corresponding review permissions.
- Teacher rubric dominates all other evidence.
- Study-design guidelines must be selected by design, not topic.
- Corpus rules must carry evidence tags, source IDs, confidence, limitations, and failure modes.
- Heuristic-only rules are secondary and should not create must-fix items unless tied to rubric, scientific validity, or internal inconsistency.
- Missing figures, methods, source evidence, or prior feedback must trigger stop/provisional status rather than fabricated review.
- Revision-round comparison must have revised material and prior feedback/review record before classifying issue resolution or score movement.
- Figure review must record whether figure assets, legends, source data, and citing Results text are available before making visual, panel-level, or figure-text findings.
- ARRIVE, BRISQ, TRIPOD/TRIPOD+AI, SAMPL, STARD, TIDieR, and similar guidelines are applied only after study design is confirmed.
- Diagnostic-accuracy and intervention-description checks are routing options, not generic biomedical Methods requirements.
- Public cancer-genomics and portal analyses require cohort/query/release/endpoint provenance and should not be treated as validated mechanism or clinical actionability without supporting evidence.
- RNA-seq, single-cell, spatial transcriptomics, proteomics, and pathway sources support reportability, provenance, and claim-calibration checks without mandating one pipeline or software package.
- Single-cell review may ask for QC/filtering, normalization, annotation, clustering, marker-testing, and analysis-object provenance when single-cell assays are in scope.
- Single-cell multimodal review may ask which modalities were measured, whether modalities were paired or integrated across datasets, and how modality-specific preprocessing and integration were handled.
- Adaptive immune receptor repertoire review may ask for MiAIRR/AIRR-style metadata, receptor chain/locus, annotation, germline reference/database context, repository representation, and tool provenance when AIRR-seq is actually in scope.
- Long-read sequencing review may ask for platform/chemistry, basecaller, read length/quality, coverage, error correction or polishing, alignment or assembly, caller, benchmark or validation context, and platform-specific limitations.
- Spatial transcriptomics review may ask for tissue/image context, coordinate or spot/cell mapping, platform/resolution, segmentation/deconvolution assumptions, and spatial-statistics provenance when spatial assays are in scope.
- Proteomics/proteogenomics review may ask for repository accession, sample metadata, raw/processed files, workflow, inference level, and access/harmonization caveats.
- DIA/DDA proteomics review must route by acquisition and quantification mode before applying method-specific expectations.
- Phosphoproteomics review may ask for enrichment/sample preparation, phosphorylation-site localization confidence, protein-level normalization where relevant, kinase/pathway inference method, multiplicity correction, and validation status.
- Pathway and gene-set enrichment review may ask for background universe, resource/version, ranking or threshold, multiplicity correction, redundancy handling, and interpretation limits.
- High-dimensional plots must be traceable to analysis object, counts, transformations, grouping, Methods, and source data, with cross-reference allowed.
- Embedding and spatial figures need legend decoding for object provenance, annotations, coordinates/embedding, scales, counts, and claim scope.
- Pan-cancer or cross-tumor claims need tumor-type heterogeneity, cohort/platform/data-tier, and validation boundaries.
- Enrichment, clustering, spatial co-localization, and proteogenomic correlation are hypothesis-supporting evidence unless direct functional, perturbational, causal, or independent validation supports mechanism.
- Phosphorylation-site abundance or kinase enrichment is hypothesis-supporting evidence unless direct perturbational, functional, causal, or independent validation supports pathway activation.
- Journal data/code/material guidance is treated as reporting or scientific-risk support unless a teacher rubric incorporates it.
- Routinely collected health-data and registry analyses require source-system, linkage, code/algorithm, cleaning, missingness, and access-condition transparency, but RECORD is not applied to all public datasets.
- Sex/gender reporting checks are relevance-gated and may allow justified non-applicability rather than forcing subgroup analysis.
- qPCR, ENCODE, SEQC, limma, DESeq2, and RNA-seq best-practice sources support assay/method reporting patterns, not universal thresholds or mandatory software choices.
- Data/code/material availability gaps are classified as reproducibility, verification, or policy-compliance risks unless direct evidence supports stronger integrity language.
- The biomedical/genomics toy fixture is a validation regression example only; it is not source evidence, a grading model, or dissertation specialization.
- The partial-input specialization fixture may output missing-information triage only; it cannot review draft text, score, review figures, adjudicate domain facts, or export a final report.
- The revision partial fixture may output revision-input triage only; it cannot classify resolution or score movement.
- The figure permission fixture splits absent-asset blocking from present-asset limited review and still blocks scoring without rubric.

## Rejected or Downgraded Rules

| Candidate rule | Decision | Reason |
|---|---|---|
| "All biomedical dissertations should follow journal IMRaD expectations." | Rejected | Overbroad; dissertation rubrics may differ. |
| "PRISMA should guide any literature-heavy dissertation." | Rejected | PRISMA applies to systematic reviews, not all literature reviews. |
| "Bioinformatics work is invalid if code is unavailable." | Downgraded | Restrictions can be legitimate; mark reproducibility risk and ask for availability/constraint details. |
| "Results must never contain interpretation." | Modified | Brief local interpretation may be acceptable; evidence must remain distinguishable. |
| "Figure aesthetics are a must-fix issue." | Downgraded | Only must-fix when readability, data interpretation, rubric compliance, or scientific validity is affected. |
| "ARRIVE applies to any preclinical study." | Rejected | ARRIVE 2.0 is for in vivo animal research; cell-line-only or computational work needs different checks. |
| "DESeq2 should be required for RNA-seq analysis." | Rejected | DESeq2 is a source pattern for reportable design elements, not a universal tool mandate. |
| "Public cancer-genomics portal findings are clinical evidence." | Rejected | Portal analyses are often exploratory unless validated and tied to appropriate clinical endpoints. |
| "All repository/code gaps are misconduct." | Downgraded | Some controlled-access, privacy, ethical, licensing, or draft-stage constraints are legitimate; the issue is traceability and access conditions. |
| "RECORD applies to every public-data analysis." | Rejected | RECORD is for routinely collected health data; public omics repositories need different provenance fields. |
| "Sex/gender disaggregation is always required." | Rejected | SAGER-derived checks require relevance and feasibility; non-applicability can be justified. |
| "MIQE/ENCODE minimum-information fields apply to all molecular methods." | Rejected | Assay-specific standards must be selected by assay type. |
| "RNA-seq analyses must follow a single canonical pipeline." | Rejected | Sources support reportable QC/model/provenance fields, not a universal workflow. |
| "A polished omics figure is interpretable without preprocessing detail." | Rejected | QC, normalization, transformation, filtering, scale, and provenance affect interpretation. |
| "Apply STARD/TIDieR to every biomedical Methods section." | Rejected | These are design-specific guidelines for diagnostic accuracy and intervention-description tasks. |
| "Single-cell analysis must use Scanpy or one best-practice workflow." | Rejected | Scanpy and best-practice sources support reportability patterns, not a mandated pipeline. |
| "Apply spatial-coordinate checks to all transcriptomics." | Rejected | Spatial-specific checks apply only to spatially resolved assays. |
| "Proteomics repository accession alone is enough." | Rejected | Reuse and interpretation also need metadata, raw/processed files, workflow, inference level, and access context. |
| "Enriched pathway equals demonstrated mechanism." | Rejected | Pathway enrichment is not direct causal or functional evidence by itself. |
| "Embedding separation proves biology." | Rejected | UMAP, t-SNE, spatial colors, and related displays require provenance and calibrated interpretation. |
| "Pan-cancer finding applies to all cancers without qualification." | Rejected | Cross-tumor generalization needs tumor-type, cohort, platform, and validation boundaries. |
| "Use toy biomedical rubric for real dissertation review." | Rejected | The toy fixture exists only for package regression testing. |
| "SpecializationInputContract can replace the actual marking scheme." | Rejected | The contract records input status and permissions; scoring still requires supplied rubric/brief/teacher guidance. |
| "Missing marking scheme blocks all non-scored formative review." | Modified | Missing rubric blocks scoring, but non-scored formative review may proceed only with explicit user permission and limitations. |
| "All single-cell studies require multimodal integration." | Rejected | Multimodal checks apply only when multiple modalities are measured or integrated. |
| "AIRR metadata standards apply to all immunology or all single-cell studies." | Rejected | AIRR checks are for adaptive immune receptor repertoire data. |
| "Long-read sequencing is automatically more valid than short-read sequencing." | Rejected | Platform choice must fit the claim, coverage, error model, and validation evidence. |
| "DIA/SWATH is the default requirement for proteomics review." | Rejected | Proteomics checks must route by acquisition/quantification mode. |
| "Phosphorylation or kinase enrichment proves causal pathway activation." | Rejected | Site abundance and kinase enrichment require validation before causal signaling language. |
| "MITI metadata checks apply to every figure." | Rejected | MITI-style checks apply to highly multiplexed tissue imaging or related imaging-based spatial assays. |
| "Partial specialization context permits draft review or rubric scoring." | Rejected | Missing draft and marking scheme keep review/scoring permissions false; the fixture only exercises missing-input triage. |
| "Revision partial context permits resolution classification or score movement." | Rejected | Revision comparison requires revised material plus prior feedback/review record; score movement requires rubric and prior score basis. |
| "Visual figure critique can be generated from absent assets." | Rejected | Visual and panel-level findings require figure assets or sufficiently detailed descriptions. |
| "Figure asset present means rubric scoring is allowed." | Rejected | Figure assets enable only relevant non-scored figure checks; scoring still requires rubric criteria. |

## Unresolved Disputes

- Supervisor tolerance for assertive thesis language cannot be known until specialization.
- Institution-specific dissertation structure may override article-style conventions.
- Severity for data/code/resource availability gaps depends on draft maturity, target venue, and teacher rubric.
- Prediction-model guidance applies only when the task is truly diagnostic/prognostic prediction, not every machine-learning analysis.
- Public portal metadata fields differ by platform and must be specialized to the actual source used.
- Boundary cases between routinely collected clinical data and public research repositories need task-specific source identification.
- Sex/gender relevance and subgroup power require the future study design and statistical context.
- Single-cell multiome, immune-repertoire, long-read, DIA/DDA proteomics, targeted proteomics, and phosphoproteomics analyses now have first-pass routing rules, but stronger threshold-level rules need deeper source modules.
- Some public portals lack stable release IDs; access date and query parameters may be the fallback provenance.
- Spatial transcriptomics modality families differ enough that high-resolution imaging-based methods need future source-specific rules.
- Database choice, pathway redundancy reduction, and enrichment background depend on the analysis question.
- Mechanistic sufficiency requires task-specific evidence; the generic core can only enforce claim calibration.
- Figure-review severity depends on whether actual figure image files are available.
- Some newly added method sources remain metadata-only because article-level reuse status was not fully verified.
- The specialization input contract still needs real-session exercise against a user-supplied input set before it can be considered mature.
- Partial-input behavior is covered by a toy fixture, but it does not replace real-session testing.
- Revision and figure permission gates are covered by toy fixtures, but real-session behavior still needs actual materials.

## Corpus Risk Review

- No copyrighted full text was stored.
- ICMJE, EQUATOR, NIH, NCI, and journal pages are used as metadata/link or policy sources.
- Open access PLOS, PRISMA, STROBE, CONSORT, REMARK, RNA-seq, single-cell, spatial, proteomics, pathway, AIRR, long-read, phosphoproteomics, multiplexed imaging, and pan-cancer sources are used for distilled patterns, not copied article bodies.
- PMC Open Access policy is included to prevent treating free-to-read as reusable.
- Metadata-only sources are used for rule provenance and source IDs only; no full text was stored.
- Optional prostate cancer and advanced prostate cancer sources remain specialization seed metadata, not generic review rules.
- MIQE, SEQC, STARD, TIDieR, Reactome, Nature Reviews Genetics, AIRR sharing, long-read, DIA/SWATH, MITI, and selected database/resource pages remain metadata-only or conservative unless reuse is verified.
- GEO, GDC, ENCODE, AACR GENIE, PRIDE, CPTAC, Reactome, AIRR, PCAWG, TCGA Pan-Cancer, and MITI sources are used for provenance and limitation patterns; repository or standard names alone are not treated as validation.

## Skill Risk Review

- Skills include stop conditions for missing rubric, missing study design, missing figures, missing Methods/Results dependencies, and missing source evidence.
- Skills preserve the hierarchy between teacher rubric, official guideline, source pattern, domain heuristic, and provisional judgment.
- Pattern files include both positive patterns and failure modes.
- Skills include uncertainty handling and provenance expectations sections.
- Skills include source-specific applicability limits for animal studies, biospecimens, prediction models, diagnostic accuracy, intervention description, public cancer-genomics portals, RNA-seq, single-cell, spatial, proteomics, and pathway/enrichment methods.
- Skills include source-specific applicability limits for animal studies, biospecimens, prediction models, diagnostic accuracy, intervention description, public cancer-genomics portals, RNA-seq, single-cell, multimodal single-cell, AIRR, long-read, spatial, DIA/DDA proteomics, phosphoproteomics, multiplexed tissue imaging, and pathway/enrichment methods.
- Skills include relevance gates for routine-data, assay-specific, modality-routing, sex/gender, omics-figure, model-contrast, severity-classification, specialization-input, and reanalysis-traceability checks.
- Skills explicitly prevent unsupported misconduct language for missing data/code/material availability.
- The toy biomedical fixture is validated as a regression test, but it must not be used as source evidence or a real grading rubric.
- The partial-input toy fixture is validated as a regression test for blocked review permissions and missing-information output.
- The revision partial and figure permission toy fixtures are validated as regression tests for blocked permissions, score movement boundaries, and visual-review asset gating.

## Next QC Actions

- Add deeper verified examples for modality-specific submodules before threshold-level rules are created.
- Exercise `SpecializationInputContract.template.json` against a non-dissertation fixture with partial inputs.
- Add JSON Schema validation for `ReviewTaskSpec`, `ReviewReport`, and dry-run finding artifacts, not just source/provenance ledgers.
- Add task-specific QC only after the real marking scheme and dissertation sections are provided.
- Continue refining severity-classification behavior with regression examples.

## Completion Marker

CORPUS_DISTILLATION_COMPLETE
