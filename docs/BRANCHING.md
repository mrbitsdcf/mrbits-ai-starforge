# Branch Policy

This repository uses a simple flow with two permanent branches:

| Branch | Purpose | Policy |
| --- | --- | --- |
| `main` | Stable line and base for public releases. | Protected; does not accept direct pushes. Changes enter via pull request. |
| `develop` | Integration of changes before release. | Accepts feature, fix, and documentation branches. |

## Rules for `main`

- Direct push to `main` is not allowed.
- Force push is not allowed.
- Branch deletion is not allowed.
- Changes must go through a pull request.
- Protection should also apply to administrators when supported by GitHub.

## Recommended Workflow

1. Create a branch from `develop`.
2. Make small, documented commits.
3. Open a pull request to `develop`.
4. Promote `develop` to `main` via a release pull request.

## Branch Names

Use short names in `kebab-case`:

```text
feature/new-skill
fix/terraform-template
docs/branch-policy
security/mcp-permissions
```
