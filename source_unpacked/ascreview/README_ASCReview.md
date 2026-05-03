# ASCReview

ASCReview is a reusable academic and scientific writing review workflow. It is designed for dissertations, thesis chapters, biomedical manuscripts, review papers, proposals, and revision rounds.

ASCReview is not a universal rubric. Every real review begins by compiling a task-specific specialization pack from the draft, marking scheme, figures/assets, source constraints, assessment context, and any prior feedback. The system must not review a draft until that pack exists and the relevant review permissions are enabled.

## Architecture

```text
ASCReview Core
  -> Corpus Library
  -> Distilled Review Skills
  -> Adversarial QC Protocol
  -> Specialization Input Contract
  -> Task Specialization Pack
  -> Section Review / Full Draft Review / Revision Round Review
```

## Priority Order

1. Teacher marking scheme, dissertation handbook, journal instructions, or assignment brief.
2. Section-specific requirements and weights.
3. Official reporting guidelines selected for the study type.
4. Verified corpus patterns from the ASCReview library.
5. Domain expert heuristics, explicitly labeled secondary.

If the marking scheme conflicts with a domain heuristic, the marking scheme wins. If the marking scheme is missing, ASCReview asks for it instead of inventing criteria.

## Required Specialization Pack

Future review sessions must create:

```text
sessions/<task_id>/
  SpecializationInputContract.json
  ReviewTaskSpec.json
  MarkingSchemeMap.json
  SectionRubricMap.json
  DomainBackgroundPack.md
  SourceEvidenceIndex.json
  SectionReviewContract.json
  ReportTemplate.md
  IterationLedger.json
  MissingInformationRequest.md
```

`SpecializationInputContract.json` records five input groups:

- draft;
- marking scheme;
- figures/assets;
- source constraints;
- assessment context.

It also records review permissions, routing decisions, and severity categories. Missing inputs block only the review modes they actually affect.

## Severity Categories

ASCReview findings should use these generic severity categories unless a supplied teacher rubric defines a stricter mapping:

- `rubric_failure`
- `scientific_validity_risk`
- `reporting_completeness_risk`
- `reproducibility_risk`
- `policy_compliance_risk`
- `draft_stage_todo`
- `style_or_clarity_polish`

`rubric_failure` is allowed only when a supplied marking scheme, assignment brief, dissertation handbook, or teacher feedback supports that label.

## Non-Goals

- Do not review a dissertation during the workflow build phase.
- Do not hardcode prostate cancer, ATM, ATR, DDR, or any other seed topic into the generic core.
- Do not fabricate papers, PMIDs, PMCIDs, DOIs, journal policies, or marking criteria.
- Do not store copyrighted full text unless reuse rights are verified.
- Do not let the same role propose and approve a rule.

## Main Prompts

- `ASCReview_CORE_PROMPT.md`: base operating contract.
- `ASCReview_SPECIALIZATION_PROMPT.md`: compiles a task-specific environment.
- `ASCReview_SECTION_REVIEW_PROMPT.md`: reviews one section after specialization.
- `ASCReview_FULL_DRAFT_REVIEW_PROMPT.md`: reviews cross-section coherence.
- `ASCReview_REVISION_ROUND_PROMPT.md`: compares prior feedback with revised drafts.

## Evidence Tags

Every rule or comment should carry one of:

- `teacher_rubric`
- `official_guideline`
- `source_pattern`
- `domain_expert_heuristic`
- `provisional`

Rules supported only by `domain_expert_heuristic` or `provisional` evidence are lower confidence and must not override task requirements.

## Validation

Run both validators after package changes:

```text
python scripts\validate_pack.py
python scripts\validate_ascreview_build.py
```

The ASCReview validator performs schema-backed checks for source, provenance, distillation rounds, specialization input contracts, task specs, marking maps, section contracts, and toy dry-run findings.
