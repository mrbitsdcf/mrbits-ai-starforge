# MrBiTs AI Starforge

Public repository for developing, curating, and distributing AI agent artifacts maintained by MrBiTs.

The goal of this project is to bring together reusable components that accelerate the creation of agents, automations, and AI-assisted workflows. Here you'll find skills, prompts, MCPs, templates, and supporting materials with enough documentation for direct use, public review, and community contribution.

## Table of Contents

- [Artifacts](#artifacts)
- [Repository Structure](#repository-structure)
- [Usage](#usage)
- [Contributing](#contributing)
- [Quality Standards](#quality-standards)
- [Branches](#branches)
- [Distribution](#distribution)
- [License](#license)

## Artifacts

| Artifact | Type | Path | Description |
| --- | --- | --- | --- |
| AWS Terraform Template | Skill | [`skills/aws-terraform-template`](skills/aws-terraform-template/) | Skill to create a minimal, opinionated Terraform AWS repository ready for agents like Codex, Claude Code, Kiro, and Antigravity. |
| Claude Fable 5 | Prompt | [`prompts/CLAUDE-FABLE-5.md`](prompts/CLAUDE-FABLE-5.md) | System prompt for a surface called Claude Fable 5, with product rules, safety, tone, user well-being, knowledge cutoff, memory, artifacts, and MCP Apps. |
| Image Prompts | Collection | [`prompts/image-prompts/`](prompts/image-prompts/) | 10 prompts for image generation and editing via multimodal models (action figure, doodles, stickers, Pixar 3D, isometric room, magazine cover, infographic, yearbook, logo). |
| Prompt Guardrails | Skill | [`skills/prompt-guardrails`](skills/prompt-guardrails/) | Guardrails for LLMs — protection against injection, prompt design patterns, multi-agent debate, RaR, and programmatic validation with Guardrails AI. Based on "Engenharia de Prompts II" (Sandeco, 2025). |
| Prompt Engineering Fundamentals | Skill | [`skills/prompt-engineering-fundamentals`](skills/prompt-engineering-fundamentals/) | Fundamental prompt engineering — basic techniques, interactive prompting, control levels, CoT, CoVe, KD-CoT, and hallucination reduction with self-reflection. Based on "Prompts em Ação" (Sandeco, 2024). |
| Skills | Collection | [`skills/`](skills/) | Directory for reusable skills with instructions, scripts, assets, and self-contained documentation. |
| Prompts | Collection | [`prompts/`](prompts/) | Directory for versioned prompts, instruction templates, and specialized agent surfaces. |
| MCPs | Collection | [`mcps/`](mcps/) | Directory for MCP servers, configurations, examples, and integration documentation. |

## Repository Structure

```text
.
+-- .github/
|   +-- ISSUE_TEMPLATE/
|   +-- PULL_REQUEST_TEMPLATE.md
+-- docs/
|   +-- DISTRIBUTION.md
+-- mcps/
+-- prompts/
|   +-- CLAUDE-FABLE-5.md
|   +-- image-prompts/
+-- skills/
|   +-- aws-terraform-template/
|   +-- prompt-engineering-fundamentals/
|   +-- prompt-guardrails/
+-- CODE_OF_CONDUCT.md
+-- CONTRIBUTING.md
+-- LICENSE
+-- README.md
+-- SECURITY.md
+-- SUPPORT.md
```

## Usage

Clone the repository:

```bash
git clone https://github.com/mrbitsdcf/mrbits-ai-starforge.git
cd mrbits-ai-starforge
```

To use a skill locally with Codex, copy or symlink the desired directory to Codex's skills directory:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
ln -sfn "$PWD/skills/aws-terraform-template" "${CODEX_HOME:-$HOME/.codex}/skills/aws-terraform-template"
```

Restart Codex after installing or updating a skill.

Each artifact should have its own documentation covering installation, usage, parameters, examples, and validation. Check the artifact's README before running scripts or applying templates.

## Contributing

Contributions are welcome. Before opening a pull request:

1. Read [`CONTRIBUTING.md`](CONTRIBUTING.md).
2. Use a short, descriptive branch name.
3. Document the artifact you created or changed.
4. Include usage examples and validation.
5. Fill out the pull request template.

New artifacts should be small, reviewable, and independent. Avoid adding dependencies or global automations without a clear justification.

## Branches

This repository uses `main` as the stable branch and `develop` as the integration branch.

- `main` is protected and does not accept direct pushes.
- Changes to `main` must go through a pull request.
- `develop` receives integrated work before a release.
- Contribution branches should start from `develop`, except for emergency fixes.

## Quality Standards

Every artifact must:

- Explain what it does and when it should be used.
- Declare prerequisites and limitations.
- Include reproducible examples.
- Avoid secrets, tokens, private data, or customer identifiers.
- Prefer simple, portable, easy-to-review formats.
- Have manual or automated validation proportional to the risk.

## Distribution

Publishing, versioning, and packaging instructions are in [`docs/DISTRIBUTION.md`](docs/DISTRIBUTION.md).

Summary:

- Skills go in `skills/<skill-name>/`.
- Prompts go in `prompts/<prompt-name>/` or `prompts/<name>.md`.
- MCPs go in `mcps/<mcp-name>/`.
- Breaking changes must be documented in release notes.
- Public releases must indicate which artifacts were changed.

## Security

To report vulnerabilities, secret exposure, or dangerous behavior, follow [`SECURITY.md`](SECURITY.md).

## License

This repository is distributed under the MIT license. See [`LICENSE`](LICENSE).
