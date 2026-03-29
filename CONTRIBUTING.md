# Contributing

Thanks for contributing to `dingyi-x-operator`.

## Ground rules

- keep `dingyi-x-operator/core/` as the source of truth
- do not hand-edit one adapter and forget the others
- prefer small, reviewable pull requests
- keep safety and reputation guardrails intact
- never commit private account state, cookies, or local runtime secrets

## Repository workflow

1. Update the shared content in `dingyi-x-operator/core/` first.
2. If references or templates need changes, update them in `core/` or `templates/`.
3. Regenerate installable adapters:

```bash
python3 dingyi-x-operator/scripts/build_adapters.py
```

4. Review the generated adapter copies under:
   - `dingyi-x-operator/codex/`
   - `dingyi-x-operator/claude-code/`
   - `dingyi-x-operator/openclaw/`
5. Update `README.md` if installation or compatibility behavior changed.

## Before opening a PR

- verify the adapters were regenerated after core changes
- check that `README.md` still matches the repo layout
- check that no private state files are included
- keep `.DS_Store` and similar local files out of the diff

## Scope expectations

Good contributions include:

- stronger X operating heuristics
- clearer installation guidance
- safer execution rules
- better reusable templates
- platform compatibility improvements

Out of scope for casual drive-by changes:

- weakening confirmation or preflight rules
- adding platform-specific behavior directly into one adapter only
- committing account-specific profile or memory data
