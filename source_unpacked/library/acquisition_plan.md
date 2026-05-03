# ASCReview Corpus Acquisition Plan

## Goal

Build a reusable biomedical, cancer, genomics, and bioinformatics writing-review corpus that supports task-specific specialization without replacing the teacher rubric.

## Initial Source Families

### Official Guideline and Policy Sources

- ICMJE Recommendations for biomedical manuscript structure and ethics.
- EQUATOR Network library and writing toolkits for study-design-specific reporting guidelines.
- PRISMA 2020 for systematic reviews and review-paper evidence flow.
- STROBE for observational studies.
- CONSORT for randomized trials.
- REMARK for tumor marker and prognostic biomarker studies.
- TRIPOD and TRIPOD+AI for prediction models when relevant.
- MDAR for life-science transparency across materials, design, analysis, and reporting.
- NCBI GEO MIAME/MINSEQE for transcriptomics/high-throughput sequencing data reporting.
- Bioinformatics journal author guidelines for software, data, and reproducibility expectations.
- PMC Open Access Subset policy for reuse decisions.

### Open Access Pattern Sources

- PLOS Computational Biology "Ten Simple Rules" articles on paper structure, figures, statistics, reproducibility, and computational research.
- Open access biomedical methods and reporting articles with explicit CC licenses.
- Peer-reviewed cancer biology or genomics articles only after DOI/PMID/PMCID and license verification.

## Acquisition Workflow

1. Identify candidate source and intended corpus use.
2. Verify title, URL, DOI, PMID, PMCID where available.
3. Verify license and assign reuse status.
4. Store metadata in `library/source_index.seed.json`.
5. Record any rule distilled from the source in `library/provenance_ledger.seed.json`.
6. Run adversarial audit against:
   - source credibility;
   - copyright risk;
   - overgeneralization;
   - biomedical accuracy;
   - usefulness for draft review;
   - conflict with teacher rubric priority.
7. Integrate accepted rules into pattern files and skills.
8. Keep rejected or unresolved rules in the QC ledger.

## Domain Expansion Order

1. General biomedical manuscript reporting and section structure.
2. Bioinformatics reproducibility: software, databases, parameters, versions, code, data availability.
3. Cancer biology writing: mechanism, model system limits, assay validity, translational caution.
4. DDR/ATM/ATR/synthetic lethality literature as optional task seed, not generic core.
5. Dissertation-specific marking schemes and supervisor preferences in future specialization sessions only.

## Minimum Metadata

Each source entry should contain:

- `source_id`
- `title`
- `source_type`
- `journal_or_body`
- `doi`
- `pmid`
- `pmcid`
- `url`
- `license`
- `reuse_status`
- `evidence_scope`
- `notes`

## Distillation Criteria

A rule enters a skill only if it is:

- actionable during review;
- linked to a source, official guideline, teacher rubric, or labeled heuristic;
- paired with a failure mode;
- general enough for reuse or clearly labeled task-specific;
- not in conflict with rubric priority;
- audited by the AdversarialAuditor role.

## Next Expansion Queue

- Add study-design-specific extensions from EQUATOR once a real task declares the design.
- Add current biomedical dissertation handbook rules when provided by the user.
- Add verified open access examples from cancer biology and genomics articles.
- Add topic-specific DDR/ATM/ATR sources only inside a specialization pack.
