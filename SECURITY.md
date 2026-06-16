# Security Policy

## Supported Versions

This repository distributes artifacts versioned via GitHub tags and releases. The supported version is the most recent public release.

## How to Report a Vulnerability

Do not open a public issue for:

- Exposed secrets or credentials.
- Exploitable vulnerabilities.
- MCPs with excessive permissions or data leaks.
- Prompts or skills that induce unsafe execution.

Use GitHub's private vulnerability reporting feature when available, or contact the maintainers privately.

Include:

- Affected artifact.
- Version, commit, or branch.
- Steps to reproduce.
- Expected impact.
- Suggested mitigation, if any.

## Scope

In scope:

- Scripts and templates included in the repository.
- Agent instructions that could execute dangerous actions.
- MCP configurations that access data, network, files, or credentials.
- Examples that could leak sensitive data.

Out of scope:

- Vulnerabilities in third-party services not configured by this repository.
- Misuse caused by local modifications outside the published artifacts.

## Security Principles

- No artifact should require real credentials in the repository.
- Examples must use placeholder values.
- MCPs must document permissions and environment variables.
- Scripts must avoid destructive actions by default.
- Templates must favor secure configurations.
