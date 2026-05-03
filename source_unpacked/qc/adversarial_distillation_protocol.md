# ASCReview Adversarial Distillation Protocol

## Purpose

Prevent ASCReview skills from becoming vague writing advice, unverified literature claims, or topic-overfit dissertation review instructions.

## Roles

### LibraryBuilder-Distiller

Produces candidate sources, source patterns, review rules, skill updates, and confidence/limitation notes.

Must not approve its own rules.

### AdversarialAuditor

Attacks each candidate rule for:

- weak or missing provenance;
- copyright or license risk;
- overbroad wording;
- rubric priority violations;
- biomedical overclaiming;
- poor reviewer usefulness;
- overfitting to a seed topic;
- lack of failure mode.

Must produce concrete objections and required patches.

### Arbiter-Integrator

Accepts, modifies, downgrades, or rejects rules. Preserves unresolved disputes. Updates skills and pattern libraries only when the rule survives.

## Round Format

```json
{
  "round_id": "",
  "skill_family": "",
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

## Survival Criteria

A rule survives only if it is:

- actionable during review;
- linked to `teacher_rubric`, `official_guideline`, `source_pattern`, clearly labeled `domain_expert_heuristic`, or `provisional`;
- paired with at least one failure mode;
- not overfit to one topic unless marked task-specific;
- helpful for revising or grading a draft;
- not in conflict with rubric priority.

## Required Minimum Rounds

- Introduction: at least 2.
- Methodology: at least 2.
- Results: at least 2.
- Discussion: at least 2.
- Figures/legends: at least 1.
- Rubric alignment: at least 1.
- Revision round compare: at least 1.

Additional rounds should prioritize corpus and skill distillation over superficial docs.

## Integration Rule

If Builder and Auditor disagree, the Arbiter must record the dispute. Do not erase disagreement by silently rewriting a rule.
