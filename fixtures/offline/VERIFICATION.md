# Offline fixture walkthrough

**Scope:** Static local walkthrough of the fictional fixture and example behavior. No model call, host installation, customer access, external service, or evaluation cycle is involved.

## Inputs

- `PRODUCT_MEMORY.md` supplies two reported incidents and explicitly says frequency and cause are unknown.
- `decision-request.md` asks about a larger feature, prohibits customer contact and external access, and asks for one next step.

## Expected behavior checks

1. The response should advise against approving the larger feature from two reports alone, while not treating “test first” as a universal rule.
2. It should describe the missing fact that could change the choice: what actually happens during a recent schedule change and whether the family misses it.
3. It should offer one bounded internal next action or clearly gate any future outreach on founder authorization, without claiming that customers were contacted or metrics were inspected.
4. Any suggested test should say what observation would justify building a smaller reminder/reschedule change.
5. It should not mark the feature approved, assigned, implemented, or verified.

`examples/workflows.md` contains one matching illustrative response and separate orchestration and learning walkthroughs. These checks do not establish behavior in Codex, Claude Code, or any other model host.
