# Assess Scientific Claim Strength

## Purpose

Check whether scientific claims are proportional to evidence type, study design, data strength, and uncertainty.

## When To Use

Use during Introduction, Results, Discussion, abstract, and full-draft reviews, especially in biomedical, cancer biology, genomics, and translational writing.

## Required Inputs

- draft text containing claims
- source evidence index
- domain background pack
- study design and evidence type
- marking scheme, if claims affect scoring

## Priority Rules

- Rubric-required claims or interpretations have priority.
- Domain expertise is secondary and must be labeled.
- If sources are missing, claim-strength judgments should be provisional unless the issue is internal inconsistency.

## Evidence Rules

Classify each claim as:

- direct support;
- indirect support;
- preliminary/exploratory support;
- conflicting evidence;
- unsupported;
- outside provided evidence.

## Positive Patterns

- association, causation, mechanism, prediction, and clinical implication are distinguished;
- uncertainty language matches evidence strength;
- limitations constrain conclusions;
- claims trace to Results or cited sources.
- data/code/materials gaps are classified as reproducibility or policy risks unless evidence supports stronger allegations.
- enrichment, clustering, spatial co-localization, and proteogenomic correlations are separated from demonstrated mechanism.
- phosphorylation-site abundance, kinase enrichment, and phosphoproteomic pathway signatures are separated from validated causal signaling.

## Negative Patterns

- association framed as causation;
- preclinical evidence framed as clinical recommendation;
- exploratory finding framed as validated mechanism;
- broad novelty claim without source comparison;
- result claim introduced only in Discussion.
- translational evidence ladder skipped;
- public-database association framed as causation;
- prediction-model performance framed as clinical utility without validation;
- missing repository or code link framed as misconduct without evidence;
- pathway enrichment, cluster labels, or spatial neighborhoods framed as causal mechanism.
- phosphoproteomic abundance or kinase-substrate enrichment framed as proven pathway activation without site-localization confidence, protein-level context, perturbation, or validation.

## Checklist

- What exact claim is being made?
- What evidence type supports it?
- Is the evidence direct or indirect?
- Does study design allow causal, mechanistic, predictive, or clinical language?
- Are limitations stated near the claim?
- Does the claim conflict with the rubric or source evidence?
- Is the claim supported by in vitro, animal, biospecimen, public-data, prediction-model, observational, or clinical intervention evidence?
- Does the wording leap across evidence levels?
- Is an availability or traceability gap being described precisely rather than escalated beyond the evidence?
- Is an omics interpretation based on association/enrichment/visualization, or on direct functional or causal validation?
- For phosphoproteomic or kinase claims, is the evidence site-level, protein-normalized where relevant, inferred from enrichment, or directly validated?

## Output Schema

```json
{
  "claim_strength_review": [
    {
      "claim": "",
      "location": "",
      "evidence_type": "",
      "support_level": "",
      "risk": "",
      "suggested_revision": ""
    }
  ],
  "must_fix": [],
  "should_fix": [],
  "provisional_items": []
}
```

## Known Failure Modes

- Over-correcting every assertive sentence into weak prose.
- Making biomedical fact judgments without source evidence.
- Ignoring that a teacher may expect a strong thesis argument while still requiring accurate calibration.
- Treating model, portal, or biomarker association as clinical actionability.
- Treating missing validation as proof a claim is false rather than unsupported or preliminary.
- Treating data-sharing or code-availability gaps as misconduct without direct evidence.
- Treating enriched pathways, UMAP clusters, spatial proximity, or proteogenomic correlations as mechanism by default.
- Treating kinase enrichment or phosphorylation-site abundance as causal pathway activation by default.

## Uncertainty Handling

- Classify support level and uncertainty rather than forcing true/false judgments.
- Mark external factual claims provisional when task-specific domain sources are missing.
- Distinguish overclaiming from legitimate argument strength required by a thesis.

## Provenance Expectations

- Use rule IDs such as `CLAIMS-R1-EVIDENCE-CALIBRATION`, `CLAIMS-R2-TRANSLATIONAL-EVIDENCE-LADDER`, `CLAIMS-R3-DATA-SHARING-NOT-MISCONDUCT`, `CLAIMS-R4-ENRICHMENT-NOT-MECHANISM`, and `BIOINFO-R14-PHOSPHOPROTEOMICS-SITE-INFERENCE`.
- Cite source IDs for evidence-level guidance and task-specific literature sources when available.
- Do not use optional prostate cancer seed metadata as generic evidence.

## Stop Conditions

Stop or mark provisional if:

- source evidence is missing for external factual claims;
- the domain background pack is absent and claims require fact adjudication;
- the user asks for unsupported biomedical validation.
