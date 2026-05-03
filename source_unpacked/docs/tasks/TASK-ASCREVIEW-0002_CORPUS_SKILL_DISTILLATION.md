# TASK-ASCREVIEW-0002 — Corpus Building & Skill Distillation Harness

## Goal

Build a reusable biomedical/cancer/bioinformatics academic writing review library and distill it into ASCReview skills.

## Required corpus assets

```text
library/
  source_policy.md
  acquisition_plan.md
  source_index.schema.json
  source_index.seed.json
  provenance_ledger.schema.json
  provenance_ledger.seed.json
```

## Required pattern assets

```text
patterns/
  introduction/good_introduction_patterns.md
  introduction/introduction_failure_modes.md
  methodology/good_methodology_patterns.md
  methodology/methodology_failure_modes.md
  results/good_results_patterns.md
  results/results_failure_modes.md
  discussion/good_discussion_patterns.md
  discussion/discussion_failure_modes.md
  figures/good_figure_legend_patterns.md
  figures/figure_legend_failure_modes.md
```

## Required skills

```text
skills/review-introduction/SKILL.md
skills/review-methodology/SKILL.md
skills/review-results/SKILL.md
skills/review-discussion/SKILL.md
skills/review-figures-legends/SKILL.md
skills/assess-rubric-alignment/SKILL.md
skills/assess-scientific-claim-strength/SKILL.md
skills/assess-bioinformatics-methods/SKILL.md
skills/revision-round-compare/SKILL.md
```

## Candidate source families

Use these as acquisition targets, but verify availability and license at runtime:

- PubMed / PMC / PMC Open Access Subset;
- PLOS Biology;
- PLOS Computational Biology;
- BMC Cancer;
- Genome Biology;
- Communications Biology;
- npj Precision Oncology;
- Bioinformatics;
- eLife;
- ICMJE Recommendations;
- EQUATOR reporting guidelines;
- PRISMA, STROBE, CONSORT when relevant.

## Required source policy

- Prefer open access and clearly reusable sources.
- Do not store long copyrighted full text unless license permits.
- Store metadata, citation, DOI/PMID/PMCID, section labels, brief permitted excerpts, and distilled patterns.
- If license is unclear, mark source as `metadata_only`.
- Do not fabricate source metadata.

## Domain focus

Prioritize:
- biomedical writing quality;
- cancer biology;
- oncology;
- DDR biology;
- ATM / ATR / synthetic lethality;
- bioinformatics and genomics methods writing.

Do not overfit generic rules to prostate cancer.

## Required adversarial loop

Run LibraryBuilder-Distiller → AdversarialAuditor → Arbiter-Integrator for each major skill family.

At least 2 rounds for:
- Introduction
- Methodology
- Results
- Discussion

At least 1 round for:
- Figures/legends
- Rubric alignment
- Revision-round compare

## Deliverable

End with:

```text
CORPUS_DISTILLATION_COMPLETE
```

Then report:
- SourceLibrarySummary
- SkillLibrarySummary
- AdversarialQCReport
- ProvisionalSkillList
- NextRecommendedCorpusExpansion
