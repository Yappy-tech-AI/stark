# Stark — AI Product Manager and Product Orchestrator

Stark helps a founder understand a product, discover real user problems, make product decisions, coordinate approved work, and learn from outcomes. It works through the AI model and tools already available in Codex, Claude Code, or another compatible host. It has no hosted model, backend, API key, account, subscription, MCP server, or payment system.

Stark can recommend building, improving, simplifying, testing, postponing, rejecting, or keeping the current product as it is. It distinguishes evidence from assumptions and recommendations from approved or completed work. The founder remains in control of goals, approvals, permissions, and consequential actions.

## Download and install

[Download Stark v1.0.0](https://github.com/Yappy-tech-AI/stark/raw/refs/heads/main/release/Stark-Skill-v1.0.0.zip) · [SHA-256 checksum](https://github.com/Yappy-tech-AI/stark/raw/refs/heads/main/release/Stark-Skill-v1.0.0.zip.sha256).

See [INSTALL.md](INSTALL.md) for the current local Skill directories and exact steps for Codex and Claude Code. For a copyable request to give an agent, see [COPYABLE_INSTALL_PROMPT.md](COPYABLE_INSTALL_PROMPT.md).

- Codex: manual install to `.agents/skills/stark/` (project) or `~/.agents/skills/stark/` (personal).
- Claude Code: manual install to `.claude/skills/stark/` (project) or `~/.claude/skills/stark/` (personal).

A ZIP link does not provide a universal “install from URL” mechanism. Use the copyable request or follow the manual steps. This release has not been installed or host-tested in Codex or Claude Code. Claude Code cloud/Cowork sessions do not read a local personal Skill folder; see the official documentation linked in INSTALL.md.

## Work with Vision and Jarvis

Stark is the product owner for product questions. Vision owns design decisions. Jarvis owns engineering decisions. Stark consults them only when their Skills are installed and accessible and their input could materially help. It never claims a missing director ran. See `references/authority-and-collaboration.md`.

## Package contents

- `SKILL.md` — activation guidance and the core operating loop.
- `references/` — decision, authority, orchestration, memory, and host-capability details, loaded when relevant.
- `templates/` — optional portable product-memory, decision, work, and learning records.
- `examples/` and `fixtures/` — fictional offline examples; not customer evidence or evaluation results.
- `scripts/package_release.py` — reproducibly build the local ZIP and checksum.
- `VERSION` — package version.

## Use

After installing, start a new session and say: **“I'm building a product. Help me manage it.”** Or invoke `$stark` in Codex / `/stark` in Claude Code with a specific product decision.

## Version and license

Version: **1.0.0**. Stark is released under the [MIT License](LICENSE). The repository includes the complete Skill source and a downloadable release ZIP. Installation instructions document host paths; host-level installation has not been verified.
