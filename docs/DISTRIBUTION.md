# Distribution and Versioning

This repository distributes AI agent artifacts via GitHub branches, tags, and releases.

## Channels

| Channel | Purpose |
| --- | --- |
| `main` | Stable mainline for direct consumption. |
| Tags | Versioned milestones, e.g., `v0.1.0`. |
| Releases | Public change notes and highlighted artifacts. |

## Versioning

Use semantic versioning for repository releases:

- `MAJOR`: breaking changes in structure, installation, or artifact contracts.
- `MINOR`: new compatible artifacts or features.
- `PATCH`: compatible fixes, documentation, and improvements.

Individual artifacts may have their own versioning in their README when needed.

## Packaging

### Skills

Skills must reside in:

```text
skills/<skill-name>/
```

Minimum structure:

```text
SKILL.md
README.md
```

Optional structure:

```text
agents/
assets/
examples/
scripts/
tests/
```

### Prompts

Simple prompts can be Markdown files:

```text
prompts/<prompt-name>.md
```

Prompts with examples, assets, or tests should use their own directory:

```text
prompts/<prompt-name>/
```

### MCPs

MCPs must reside in:

```text
mcps/<mcp-name>/
```

Each MCP must document installation, execution, configuration, permissions, environment variables, and local validation.

## Release Checklist

Before publishing a release:

1. Confirm that the root README lists new or removed artifacts.
2. Confirm that each changed artifact has its own documentation.
3. Run the applicable validations.
4. Verify that there are no secrets, tokens, or local files.
5. Write release notes with changed artifacts and user impact.

## Consumer Installation

Consumers can use the repository in three ways:

- Clone the repository and reference artifacts locally.
- Copy an artifact directory to the desired tool.
- Install directly from a GitHub path when the tool supports that format.
