# Dingyi X Operator

[中文说明](README.zh-CN.md)

> Cross-platform X/Twitter operator skill for Codex, Claude Code, and OpenClaw.

[![Release](https://img.shields.io/github/v/release/fuyalan126/dingyi-x-operator)](https://github.com/fuyalan126/dingyi-x-operator/releases)
[![License](https://img.shields.io/github/license/fuyalan126/dingyi-x-operator)](LICENSE)
[![Platforms](https://img.shields.io/badge/platform-Codex%20%7C%20Claude%20Code%20%7C%20OpenClaw-111827)](README.md)

`dingyi-x-operator` is an opinionated X/Twitter operating agent for people who care about signal, taste, and reputation safety.

Best for:

- founders, builders, and operators who want help running X without turning into spam
- people who want AI help with replies, original posts, source-to-post workflows, and visual briefs
- teams or individuals who use Codex, Claude Code, or OpenClaw as their agent runtime

What it does:

- finding good tweets to engage with
- drafting replies that sound specific and human
- planning original posts and threads
- turning source material into X-ready posts
- adapting content between Chinese and English
- deciding whether a post needs a visual and writing the visual brief
- executing approved actions through `opencli`

## Quick start

Copy the adapter for your runtime into your skills directory:

```bash
# Codex
cp -R "/path/to/repo/dingyi-x-operator/codex" "$HOME/.codex/skills/dingyi-x-operator"

# Claude Code
cp -R "/path/to/repo/dingyi-x-operator/claude-code" "$HOME/.claude/skills/dingyi-x-operator"

# OpenClaw
cp -R "/path/to/repo/dingyi-x-operator/openclaw" "/path/to/openclaw/skills/dingyi-x-operator"
```

Then customize local state with:

- `dingyi-x-operator/templates/PROFILE.example.md`
- `dingyi-x-operator/templates/MEMORY.example.md`

## What this repository is

This repository is packaged as a single-source skill with thin adapters for:

- Codex
- Claude Code
- OpenClaw

The shared operating logic lives in:

- [`dingyi-x-operator/core/SKILL.md`](dingyi-x-operator/core/SKILL.md)

Platform entrypoints live in:

- [`dingyi-x-operator/codex/SKILL.md`](dingyi-x-operator/codex/SKILL.md)
- [`dingyi-x-operator/claude-code/SKILL.md`](dingyi-x-operator/claude-code/SKILL.md)
- [`dingyi-x-operator/openclaw/SKILL.md`](dingyi-x-operator/openclaw/SKILL.md)

This keeps one canonical skill body in `core/`, while shipping installable adapter copies for each platform.

## Repository layout

```text
dingyi-x-operator/
  core/
    SKILL.md
    references/
  codex/
    SKILL.md
    agents/openai.yaml
  claude-code/
    SKILL.md
  openclaw/
    SKILL.md
  templates/
    PROFILE.example.md
    MEMORY.example.md
marketing/
  release-kit.md
  banner-brief.md
```

## Core dependencies

Required for live X execution:

- `opencli`
- a running Chrome session
- the OpenCLI browser bridge extension
- a logged-in X account

Recommended helper skills when your environment supports them:

- `social-media-strategist`
- `content-creator`
- `twitter-engager`
- `baoyu-url-to-markdown`
- `baoyu-translate`

## Installation

Recommended installation method: copy or symlink the platform adapter into your agent's skills directory.

Why this works:

- each adapter is self-contained at runtime
- symlinks are optional, not required
- the shared `core/` content can regenerate adapter copies with the build script

### Codex

```bash
cp -R "/path/to/repo/dingyi-x-operator/codex" "$HOME/.codex/skills/dingyi-x-operator"
```

### Claude Code

```bash
cp -R "/path/to/repo/dingyi-x-operator/claude-code" "$HOME/.claude/skills/dingyi-x-operator"
```

### OpenClaw

Install the `openclaw/` adapter into your OpenClaw skills directory using your preferred local path convention.

Example:

```bash
cp -R "/path/to/repo/dingyi-x-operator/openclaw" "/path/to/openclaw/skills/dingyi-x-operator"
```

If you prefer symlinks instead of copies, that also works.

## Customization

Do not commit your real operating memory or account-specific preferences.

Start from:

- [`dingyi-x-operator/templates/PROFILE.example.md`](dingyi-x-operator/templates/PROFILE.example.md)
- [`dingyi-x-operator/templates/MEMORY.example.md`](dingyi-x-operator/templates/MEMORY.example.md)

Typical local locations:

- `$X_OPERATOR_STATE_DIR/PROFILE.md`
- `$X_OPERATOR_STATE_DIR/MEMORY.md`
- `.x-operator/PROFILE.md`
- `.x-operator/MEMORY.md`
- `~/.x-operator/PROFILE.md`
- `~/.x-operator/MEMORY.md`
- `.dingyi-x-operator/PROFILE.md`
- `.dingyi-x-operator/MEMORY.md`
- `~/.dingyi-x-operator/PROFILE.md`
- `~/.dingyi-x-operator/MEMORY.md`

Recommended for new installs:

- use `.x-operator/` or `~/.x-operator/`
- use `X_OPERATOR_STATE_DIR` when you want per-project or per-account isolation
- keep `dingyi-x-operator` paths only for backward compatibility

## Design principles

- credibility over volume
- shortlist before public actions
- preflight before write operations
- exact wording approval before posting
- visual planning is built in
- image generation is optional execution, not core identity

## Included references

The core skill ships with reusable references for:

- execution modes
- profile template
- memory template
- output templates
- visual strategy

## Launch assets

This repository also ships lightweight launch copy and visual planning files:

- [`marketing/release-kit.md`](marketing/release-kit.md)
- [`marketing/banner-brief.md`](marketing/banner-brief.md)

## Maintenance

If you update the shared skill in `core/`, regenerate the installable adapters with:

```bash
python3 dingyi-x-operator/scripts/build_adapters.py
```

## License

This repository is released under the [MIT License](LICENSE).

## Contributing

Contribution guidance lives in [CONTRIBUTING.md](CONTRIBUTING.md).

## Not included yet

- installer scripts
- CI workflows
- publishing automation

Those can be added later once the repository shape is stable.
