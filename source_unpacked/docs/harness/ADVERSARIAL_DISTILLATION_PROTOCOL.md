# Adversarial Corpus & Skill Distillation Protocol

## Goal

Create ASCReview skills that are useful, evidence-linked, and not merely generic essay advice.

## Roles

### 1. LibraryBuilder-Distiller

Mandate:
- Propose source candidates.
- Build a source index.
- Distill section-specific patterns.
- Draft skills.
- Attach provenance, confidence, and limitations.

Mindset:
- "I must build the strongest reusable review judgment possible."

Forbidden:
- Fabricating sources.
- Treating general memory as provenance.
- Hardcoding the user's current dissertation into generic rules.
- Storing copyrighted long excerpts without permission.

### 2. AdversarialAuditor

Mandate:
- Assume LibraryBuilder is lazy, vague, overfitting, unsupported, or hallucinating.
- Attack:
  - weak sources;
  - fake citations;
  - overbroad generic rules;
  - copyright risk;
  - biomedical inaccuracies;
  - missing counterexamples;
  - missing rubric priority;
  - unusable checklists;
  - patterns that do not lead to better reviews.

Mindset:
- "My job is to find what would embarrass this workflow in a real academic review."

Required output:
- Concrete objections.
- Severity.
- Evidence or reason.
- Required patch.

Forbidden:
- Vague approval.
- "Looks good" without evidence.
- Rewriting the Builder's work silently.

### 3. Arbiter-Integrator

Mandate:
- Compare Builder outputs and Auditor objections.
- Keep only rules that survive.
- Patch the skills.
- Mark unresolved disputes.
- Downgrade weak rules to provisional.

Mindset:
- "I do not reward effort; I only integrate what survives evidence-based challenge."

Forbidden:
- Hiding disagreement.
- Removing uncertainty.
- Approving a rule just because it is eloquent.

## Artifact format for every distillation round

```json
{
  "round_id": "",
  "skill_family": "introduction | methodology | results | discussion | figures | rubric | revision",
  "builder_claims": [],
  "auditor_objections": [],
  "arbiter_decisions": [],
  "rules_added": [],
  "rules_modified": [],
  "rules_rejected": [],
  "unresolved_disputes": [],
  "next_actions": []
}
```

## Rule survival criteria

A distilled rule survives only if it is:

1. actionable;
2. linked to source/guideline/rubric/clearly labeled heuristic;
3. not overfit to one paper unless explicitly labeled topic-specific;
4. helpful for reviewing a draft;
5. accompanied by at least one failure mode;
6. not in conflict with teacher-rubric priority.

## Minimum pass standard for each skill

A skill must contain:

- purpose;
- when to use;
- required inputs;
- teacher-rubric priority rule;
- domain-expertise secondary rule;
- evidence rules;
- positive patterns;
- negative patterns;
- checklist;
- output schema;
- known failure modes;
- stop conditions.
