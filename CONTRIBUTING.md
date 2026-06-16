# Contribution Guide

Thank you for considering a contribution to MrBiTs AI Starforge.

This repository accepts AI agent artifacts, including skills, prompts, MCPs, templates, and supporting documentation. The focus is to keep everything reusable, auditable, and simple to install.

## Before Contributing

- Open an issue for large, breaking changes or those that add dependencies.
- For small fixes, documentation, and new examples, a direct pull request is sufficient.
- Never include secrets, tokens, private keys, customer data, or real test credentials.
- Prefer small, cohesive changes.

## Types of Contribution

| Type | Suggested Path | Requirements |
| --- | --- | --- |
| Skill | `skills/<name>/` | `SKILL.md`, README, examples, and validation. |
| Prompt | `prompts/<name>.md` or `prompts/<name>/` | Purpose, usage context, expected inputs, and examples. |
| MCP | `mcps/<name>/` | README, execution instructions, configuration, and security. |
| Documentation | `docs/` or the artifact's README | Must reflect the actual state of the files. |

## Standard for New Skills

A skill must contain, at minimum:

```text
skills/<name>/
+-- SKILL.md
+-- README.md
```

Use `scripts/` for automations and `assets/` for templates, examples, or static files. Scripts should be deterministic and avoid external dependencies when possible.

## Standard for Prompts

Prompts must document:

- Purpose.
- When to use.
- Expected inputs.
- Expected output.
- Risks or limitations.
- Usage example.

## Standard for MCPs

MCPs must document:

- How to install and run.
- Required environment variables.
- Permission scopes.
- Data accessed or persisted.
- How to test locally.
- Known threats and security boundaries.

## Pull Requests

Before opening a pull request:

1. Update the documentation for the changed artifact.
2. Update the index in `README.md` if you create or remove artifacts.
3. Run the applicable validation.
4. Fill out all fields in the pull request template.

## Style

- Use clear English for all repository documentation.
- Prefer copyable examples.
- Avoid new dependencies without a real need.
- Keep directory names in `kebab-case`.

## License for Contributions

By contributing, you agree that your contribution will be licensed under this repository's MIT license.
