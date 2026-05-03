# Good Discussion Patterns

## DISC-P1: Answer the Aim With Calibrated Interpretation

- Description: Discussion should return to the aim and explain what the findings do and do not support.
- When it applies: all empirical, review, and dissertation discussion sections.
- Source/provenance ID: `DISCUSSION-R1-INTERPRET-WITH-LIMITS`; `CLAIMS-R1-EVIDENCE-CALIBRATION`.
- Positive example summary: The opening discussion paragraph states the main finding in relation to the aim and immediately qualifies evidence strength.
- Failure mode: summary repeats results without explaining significance or limitations.
- Review checklist use: Compare the aim sentence to the first discussion paragraph.

## DISC-P2: Integrate Prior Evidence Without Hiding Conflict

- Description: Discussion should compare findings with prior literature, including conflicting results or alternative explanations when important.
- When it applies: literature-based, biomedical, and mechanism-heavy work.
- Source/provenance ID: `GUIDE-ICMJE-MANUSCRIPT`; `GUIDE-STROBE-2007`; `GUIDE-REMARK-2012`.
- Positive example summary: The draft explains why findings agree or conflict with earlier studies and whether differences may arise from design, sample, assay, analysis, or context.
- Failure mode: cherry-picked agreement with no discussion of contradiction.
- Review checklist use: Look for at least one limitation or alternative explanation for each major claim.

## DISC-P3: Limitations Are Specific and Consequential

- Description: Limitations should identify how design, sample, methods, measurement, data availability, or analysis affects interpretation.
- When it applies: all assessed scientific writing.
- Source/provenance ID: `DISCUSSION-R1-INTERPRET-WITH-LIMITS`.
- Positive example summary: A limitation states what could bias, weaken, or restrict a finding and how future work could address it.
- Failure mode: generic "more research is needed" with no connection to evidence strength.
- Review checklist use: For every limitation, ask which claim this limits.

## DISC-P4: Implications Match Evidence Type

- Description: Clinical, translational, theoretical, or methodological implications should be proportional to study design and result strength.
- When it applies: biomedical and cancer biology writing.
- Source/provenance ID: `CLAIMS-R1-EVIDENCE-CALIBRATION`; `GUIDE-REMARK-2012`; `PATTERN-STAT-PRACTICE-2016`.
- Positive example summary: A preclinical result is described as hypothesis-generating or mechanistically suggestive unless supported by clinical evidence.
- Failure mode: exploratory association is framed as a treatment recommendation.
- Review checklist use: Label each implication as direct, indirect, preliminary, speculative, or unsupported.

## DISC-P5: Future Work Solves a Specific Limitation

- Description: Future work should follow from unresolved gaps, not appear as a disconnected wish list.
- When it applies: dissertations, proposals, and papers.
- Source/provenance ID: `DISCUSSION-R1-INTERPRET-WITH-LIMITS`.
- Positive example summary: A limitation about cohort size leads to a concrete validation study, not a vague call for larger studies.
- Failure mode: future work repeats the topic at a higher level of ambition without a design link.
- Review checklist use: Pair each future work item with the limitation or unanswered question it addresses.

## DISC-P6: Preclinical and Animal Model Boundary

- Description: Discussion should separate what a model directly shows from what it suggests for human biology, clinical translation, or future validation.
- When it applies: in vivo animal, cell-line, organoid, xenograft, and other preclinical studies.
- Source/provenance ID: `DISCUSSION-R3-PRECLINICAL-MODEL-LIMITS`; `CLAIMS-R2-TRANSLATIONAL-EVIDENCE-LADDER`.
- Positive example summary: A preclinical result is framed as mechanistic support or hypothesis generation, with model limitations and validation needs named.
- Failure mode: model findings are promoted as clinical efficacy or therapeutic recommendation.
- Review checklist use: Label each implication as direct model finding, plausible mechanism, translational hypothesis, or clinical evidence.
- When it does not apply: fully clinical trials or non-biomedical writing unless model evidence is discussed.

## DISC-P7: Prediction Model Interpretation Boundary

- Description: Prediction-model discussions should distinguish model development, internal validation, external validation, performance metrics, calibration, clinical utility, and deployment limits.
- When it applies: diagnostic/prognostic models, machine-learning classifiers, risk scores, and AI-assisted clinical prediction.
- Source/provenance ID: `DISCUSSION-R4-PREDICTION-MODEL-LIMITS`.
- Positive example summary: A model's AUC is interpreted alongside calibration, validation setting, cohort representativeness, and intended use.
- Failure mode: high apparent performance is treated as clinical readiness without validation or utility evidence.
- Review checklist use: Ask what evidence supports deployment, not merely discrimination.
- When it does not apply: descriptive clustering or exploratory bioinformatics not framed as a clinical prediction model.

## DISC-P8: Public-Data Association Caveat

- Description: Public cancer-genomics or portal analyses should discuss cohort provenance, data-release limits, filters, endpoint definitions, and validation status before making mechanistic or clinical claims.
- When it applies: cBioPortal, TCGA, GEO, CPTAC, GENIE, or similar public-data analyses.
- Source/provenance ID: `BIOINFO-R3-PUBLIC-CANCER-PORTAL-PROVENANCE`; `INTRO-R4-PUBLIC-DATA-RATIONALE-LIMITS`.
- Positive example summary: A portal-derived survival association is presented as exploratory unless validated in an independent cohort or supported by direct mechanistic evidence.
- Failure mode: public-data association is discussed as causal or therapeutically actionable.
- Review checklist use: Identify cohort, query, endpoint, and validation before accepting the implication.
- When it does not apply: primary experiments not using public databases.

## DISC-P9: Real-World Data Limit Boundary

- Description: Real-world, registry, or public clinico-genomic data should be interpreted as design-constrained evidence, with selection, missingness, linkage, endpoint, and confounding limits named before clinical or mechanistic implications.
- When it applies: registry studies, electronic health record studies, public clinico-genomic datasets, and real-world precision-oncology analyses.
- Source/provenance ID: `DISCUSSION-R5-REAL-WORLD-DATA-LIMITS`; `GUIDE-RECORD-2015`; `RESOURCE-AACR-GENIE`.
- Positive example summary: A registry-derived association is framed as hypothesis-generating or externally supportive, with cohort and endpoint constraints named.
- Failure mode: a registry or public-database association is discussed as clinical efficacy, treatment recommendation, or direct mechanism.
- Review checklist use: Ask whether the design supports association, prediction, mechanism, or intervention claims.
- When it does not apply: randomized trials, direct functional experiments, or non-data-driven theoretical discussion.

## DISC-P10: Pan-Cancer Generalization Boundary

- Description: Cross-tumor or pan-cancer analyses should distinguish shared patterns from tumor-type-specific biology, platform effects, cohort differences, data-access tiers, and validation gaps.
- When it applies: TCGA, PCAWG, GDC, CPTAC, GENIE, or other cross-cancer consortium analyses.
- Source/provenance ID: `DISCUSSION-R6-PANCANCER-GENERALIZATION-LIMITS`; `DOMAIN-PCAWG-2020`; `DOMAIN-TCGA-PANCAN-2013`.
- Positive example summary: A pan-cancer driver/pathway finding is discussed as a cross-cohort pattern while noting tumor lineage heterogeneity and need for functional or clinical validation.
- Failure mode: a cross-cancer association is generalized to all cancers or to treatment implications without lineage, platform, cohort, or validation caveats.
- Review checklist use: Identify which cancer types, platforms, cohorts, and data tiers support the claim before accepting generalized language.
- When it does not apply: single-cohort, single-disease, or non-cancer analyses unless pan-cancer evidence is invoked.

## DISC-P11: Enrichment Is Hypothesis Support

- Description: Pathway enrichment, gene-set association, cluster markers, spatial co-localization, or proteogenomic correlation should be framed as interpretive or hypothesis-generating unless direct validation supports mechanism.
- When it applies: pathway analysis, single-cell/spatial interpretation, proteogenomics, and omics-driven mechanistic claims.
- Source/provenance ID: `CLAIMS-R4-ENRICHMENT-NOT-MECHANISM`; `METHOD-PATHWAY-ANALYSIS-2012`.
- Positive example summary: An enriched DNA repair pathway is described as consistent with a hypothesis and followed by validation needs rather than asserted as demonstrated pathway activation.
- Failure mode: enrichment terms are treated as mechanism, causality, or therapeutic actionability.
- Review checklist use: Ask what evidence beyond the enrichment or cluster label establishes mechanism.
- When it does not apply: directly validated functional experiments where pathway activity is experimentally measured.
