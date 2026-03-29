# Dingyi X Operator OSS Packaging Design

## Goal

Package `dingyi-x-operator` into an open-source-friendly repository that can be reused across Codex, Claude Code, and OpenClaw without maintaining three divergent copies.

## Context

- The current reusable skill already exists in the local Codex skill directory.
- The current workspace is empty and is not inside a git repository.
- The user wants the open-source version to live in the current directory.
- The repository should be publishable without leaking private runtime state from the existing local setup.

## Design Decision

Use a single-source repository with thin platform adapters.

### Why this approach

- It avoids content drift across Codex, Claude Code, and OpenClaw.
- It keeps the skill's operating logic in one place.
- It makes open-source maintenance practical.
- It allows each platform to have only the minimum compatibility wrapper it needs.

## Repository Structure

```text
README.md
dingyi-x-operator/
  core/
    SKILL.md
    references/
      execution-modes.md
      memory-template.md
      output-templates.md
      profile-template.md
      visual-strategy.md
  codex/
    SKILL.md
    agents/
      openai.yaml
  claude-code/
    SKILL.md
  openclaw/
    SKILL.md
  templates/
    PROFILE.example.md
    MEMORY.example.md
```

## Content Model

### Core

`core/SKILL.md` is the canonical source of truth for:

- agent purpose
- prerequisites
- execution safety rules
- confirmation policy
- execution modes
- visual planning behavior
- memory and profile conventions

`core/references/` stores supporting material that should not bloat every adapter.

### Platform Adapters

Each platform directory contains a small wrapper skill that:

- identifies the platform
- points back to the core skill content
- preserves the same operating behavior
- avoids duplicating long reference material

Platform wrappers should stay intentionally thin so future updates mostly happen in `core/`.

### Templates

The open-source repository should not ship the real local runtime files from:

- `~/.dingyi-x-operator/PROFILE.md`
- `~/.dingyi-x-operator/MEMORY.md`

Instead, it should include sanitized examples under `templates/` so users can copy them into their own local state.

## Compatibility Rules

### Codex

- Provide a Codex-friendly `SKILL.md`
- Include `agents/openai.yaml`
- Keep the frontmatter compatible with Codex discovery

### Claude Code

- Provide a Claude Code compatible `SKILL.md`
- Keep instructions self-contained enough that Claude Code users can install the directory directly into their skills path

### OpenClaw

- Provide an OpenClaw-oriented `SKILL.md`
- Keep command examples aligned with `opencli` usage because OpenClaw is part of the intended execution environment

## Open-Source Guardrails

Do not include:

- personal account secrets
- local browser state
- real private memory files
- machine-specific runtime paths unless clearly marked as examples

Do include:

- public installation guidance
- dependency explanation
- sample profile and memory files
- clear notes on what is optional vs required

## README Scope

The root `README.md` should explain:

- what the project is
- who it is for
- supported environments
- how the single-source plus adapter model works
- how to install for Codex, Claude Code, and OpenClaw
- how to customize profile and memory

## Implementation Notes

- Keep the open-source version generic enough to be reusable, but still clearly opinionated toward X operations.
- Preserve the strong execution safety rules from the current local version.
- Use example paths and example workflow language where local-only details would otherwise leak.
- Prefer copying stable references into the repo instead of requiring the open-source package to depend on files outside the repository.

## Non-Goals

- Building an installer script in this pass
- Publishing the repository remotely in this pass
- Adding automation or CI before the base content structure is stable
- Exporting the user's private live profile or memory files

## Success Criteria

The first open-source packaging pass is successful if:

1. The current directory contains a coherent repository structure.
2. The core skill is readable without relying on private local files.
3. Each target platform has a thin adapter entrypoint.
4. The repository includes sanitized templates for customization.
5. The README is good enough for another user to install and understand the project.

## Risks

### Risk: Adapter drift

Mitigation:
- keep adapters thin
- move shared logic to `core/`

### Risk: Private state leakage

Mitigation:
- ship examples only
- avoid copying live files from the home directory

### Risk: Platform assumptions differ

Mitigation:
- keep wrappers explicit about their environment
- preserve one common operating model

## Next Step

After review, scaffold the repository structure in the current directory and populate it from the existing local `dingyi-x-operator` skill plus sanitized example files.
