# Orchestration and learning

Use this reference after the founder accepts a product direction or requests execution within a clear scope.

## Make approved work actionable

A work brief should be short enough to execute and include only what is needed:

- Product outcome and intended user benefit.
- Approved scope and explicit exclusions.
- Decision owner and actual assignee, if known.
- Dependencies and constraints.
- Acceptance checks expressed as observable behavior.
- Verification method and who can perform it.
- Current status using the definitions in `SKILL.md`.

Break work down only far enough to expose a real dependency, owner, or acceptance boundary. Do not add ceremony, milestones, or generic backlog fields without a practical use. Use `templates/WORK_BRIEF.template.md` when a durable handoff is useful.

## Execute through real capabilities

Before acting, inspect applicable project instructions and the relevant files. Use tools actually available in this host. Coordinate Vision or Jarvis only when installed and accessible. If a capability is missing, state the limitation and provide a usable handoff instead of inventing an execution path.

The user's request may itself authorize implementation. Preserve its scope and any stated constraints; do not ask for approval again when the user already authorized the same action. Ask when a decision materially changes scope or when the action has not been authorized. External communications, publishing, deployment, deletion, spending, permission changes, and sharing sensitive data need the appropriate authorization. Do not install another Skill or alter host configuration as part of ordinary product work.

## Verify honestly

Tie each acceptance check to evidence the host actually obtained. Say exactly what passed, failed, or was not run. A plan, code inspection, successful build, screenshot, user report, or production observation proves different things; do not present one as another. Keep verification within the responsible domain. For example, implementation evidence alone does not establish that customers value a feature or that a rendered interface is usable.

## Learn from the result

Before work begins, capture the expected outcome and what evidence would change the next decision. Afterward, compare expected with actual. Consider whether the result came from the feature, changed exposure, user mix, seasonality, or another known factor; mark causality unknown when the evidence cannot distinguish them. Record the learning and any revised priority with its source. Use `templates/LEARNING_NOTE.template.md` when it will help the next session.

Do not report an unmeasured target as achieved. Do not keep a decision open just to generate more analysis; use a follow-up only when new evidence could change the next action.
