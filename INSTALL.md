# Install Stark

Stark is a local, model-agnostic Skill. The ZIP contains instructions and supporting files; it does not install a model, server, account, API key, MCP service, or background monitor.

## Download and verify

[Download the Stark 1.0.0 ZIP](https://github.com/Yappy-tech-AI/stark/raw/refs/heads/main/release/Stark-Skill-v1.0.0.zip) and its [SHA-256 sidecar](https://github.com/Yappy-tech-AI/stark/raw/refs/heads/main/release/Stark-Skill-v1.0.0.zip.sha256). Put both files in one folder, then run:

```sh
cd /path/to/downloads
shasum -a 256 -c Stark-Skill-v1.0.0.zip.sha256
mkdir -p ~/stark-release
unzip -q Stark-Skill-v1.0.0.zip -d ~/stark-release
```

Replace `/path/to/downloads` with the folder containing the ZIP and sidecar. The extracted Skill directory is `~/stark-release/stark/`.

## Codex

OpenAI documents `.agents/skills/` in a project and `~/.agents/skills/` for all projects when the Codex environment supports local Skills. Install personally with:

```sh
mkdir -p ~/.agents/skills
cp -R ~/stark-release/stark ~/.agents/skills/stark
```

For one repository only, use that repository's `.agents/skills/` instead:

```sh
mkdir -p .agents/skills
cp -R ~/stark-release/stark .agents/skills/stark
```

Start a new Codex session and ask: `Use $stark to help me manage my product and decide what to do next.`

## Claude Code

Claude Code local Skills use `~/.claude/skills/<name>/SKILL.md` for all local projects or `.claude/skills/<name>/SKILL.md` for one repository. Install personally with:

```sh
mkdir -p ~/.claude/skills
cp -R ~/stark-release/stark ~/.claude/skills/stark
```

For one repository only:

```sh
mkdir -p .claude/skills
cp -R ~/stark-release/stark .claude/skills/stark
```

Start a new Claude Code session and invoke `/stark` or ask Claude to use the Stark Skill. The personal local path is for local Claude Code sessions; Claude Code cloud and Cowork sessions use account-enabled/synced Skills or supported project distribution, not this machine-local folder.

## Copyable installation request

See [COPYABLE_INSTALL_PROMPT.md](COPYABLE_INSTALL_PROMPT.md). It tells an agent to inspect the archive, copy only the Stark folder to the selected host's Skill directory, and report the exact path. A pasted URL does not guarantee that every agent interface can download or install it.

## Update

1. Download and inspect the new version's ZIP.
2. Back up the existing `stark` Skill folder if you have local edits.
3. Replace only the installed `stark` folder with the new archive's `stark/` folder.
4. Start a new host session. If you installed a project Skill, commit the intentional update to your project as usual.

## Uninstall

Delete only the `stark` directory from the Skill location you used:

- Codex personal: `~/.agents/skills/stark`
- Codex project: `.agents/skills/stark`
- Claude Code personal: `~/.claude/skills/stark`
- Claude Code project: `.claude/skills/stark`

## Documentation checked

Installation paths were checked against [OpenAI's coding-agent Skill installation guidance](https://developers.openai.com/api/reference/cli) and [Claude Code's Skills documentation](https://code.claude.com/docs/en/skills) on 7 November 2026. The Skill was not installed or tested in Codex or Claude Code as an end user.
