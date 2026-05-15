# AWS Terraform Template Skill

Bootstrap a minimal, opinionated AWS Terraform repository from a reusable Codex skill.

This skill generates the baseline files most AWS infrastructure repositories need before real resources are added: Terraform version constraints, AWS provider configuration, S3 backend configuration, workspace-specific YAML settings, quality-tool configuration, lightweight test scaffolds, and agent instructions.

## What It Does

- Creates a Terraform project skeleton for AWS.
- Uses S3 remote state with encryption and native S3 lockfile support.
- Stores environment settings in `env/<environment>/tfsettings.yaml`.
- Keeps root `variables.tf` empty and avoids `*.tfvars`.
- Configures required AWS tags: `environment`, `project`, and `owner`.
- Supports AWS authentication via environment variables, named profile, SSO profile, or assume-role.
- Adds quality and validation scaffolding for `terraform fmt`, `tflint`, `terraform-docs`, pre-commit, Terratest, and Kitchen-Terraform.
- Renders optional agent instructions for Codex, Claude Code, Kiro, or Antigravity.

The generated template intentionally does not create AWS resources. It gives the repository a clean Terraform baseline so teams can add modules and infrastructure deliberately.

## Supported Agents

- Codex
- Claude Code
- Kiro
- Antigravity

## Installation

### Install Locally

Copy the skill folder into your Codex skills directory:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/aws-terraform-template "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Restart Codex after installing or updating the skill.

### Install for Development

Use a symlink when you are editing the skill and want Codex to read the latest files from your working tree:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
ln -sfn "$PWD/skills/aws-terraform-template" "${CODEX_HOME:-$HOME/.codex}/skills/aws-terraform-template"
```

Restart Codex after creating or changing the symlink.

### Install from GitHub

After publishing this repository, install the skill with Codex's skill installer by pointing it at the skill directory:

```text
$skill-installer install https://github.com/<owner>/<repo>/tree/main/skills/aws-terraform-template
```

Replace `<owner>/<repo>` with the GitHub repository that contains this skill.

## Usage

Invoke the skill from Codex:

```text
/aws-terraform-template
```

or explicitly:

```text
/aws-terraform-template init
```

Calling the skill without a command assumes `init`. If required parameters are missing, the skill asks for each one before rendering files.

Example fully specified invocation:

```text
/aws-terraform-template init --agent codex --project-key network-core --project-tag Network --owner platform-team --environment Network --region sa-east-1 --backend-bucket example-tf-state --backend-key network-core/Network/terraform.tfstate --auth-method profile --profile sandbox
```

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `agent` | Yes | Agent instruction file to render: `codex`, `claude-code`, `kiro`, or `antigravity`. Defaults to `codex` during interactive runs. |
| `project-key` | Yes | Lowercase Terraform naming prefix, for example `network-core`. Use hyphens instead of underscores. |
| `project-tag` | Yes | Value for the required AWS `project` tag. |
| `owner` | Yes | Value for the required AWS `owner` tag. |
| `environment` | Yes | Terraform workspace and environment directory name. The skill creates `env/<environment>/tfsettings.yaml`. |
| `region` | Yes | Primary AWS region, for example `sa-east-1`. |
| `backend-bucket` | Yes | Existing S3 bucket used for Terraform state. |
| `backend-key` | Yes | S3 object key for Terraform state. Must end with `terraform.tfstate`. |
| `auth-method` | Yes | AWS authentication mode: `environment`, `profile`, `sso`, or `assume-role`. |
| `profile` | Conditional | Required when `auth-method` is `profile` or `sso`. Optional source profile for `assume-role`. |
| `role-arn` | Conditional | Required when `auth-method` is `assume-role`. |

Advanced version flags are available in `scripts/init_template.py` for maintainers who need to update Terraform or provider constraints.

## Generated Structure

The rendered repository includes:

```text
.
+-- .agent-instructions/
+-- .editorconfig
+-- .gitignore
+-- .kitchen.yml
+-- .pre-commit-config.yaml
+-- .terraform-docs.yaml
+-- .tflint.hcl
+-- backend.tf
+-- data.tf
+-- env/
|   +-- <environment>/
|       +-- backend.hcl
|       +-- tfsettings.yaml
+-- locals.tf
+-- main.tf
+-- modules/
+-- outputs.tf
+-- providers.tf
+-- README.md
+-- test/
|   +-- integration/
|   +-- terratest/
+-- variables.tf
+-- versions.tf
```

The environment directory is derived from the `environment` parameter. For example, `--environment Network` creates:

```text
env/Network/backend.hcl
env/Network/tfsettings.yaml
```

## Direct Script Usage

The skill uses `scripts/init_template.py` internally. You can also run it directly for local testing:

```bash
python3 skills/aws-terraform-template/scripts/init_template.py \
  --destination /tmp/network-core \
  --agent codex \
  --project-key network-core \
  --project-tag Network \
  --owner platform-team \
  --environment Network \
  --region sa-east-1 \
  --backend-bucket example-tf-state \
  --backend-key network-core/Network/terraform.tfstate \
  --auth-method profile \
  --profile sandbox
```

If arguments are omitted, the script prompts for missing required values.

## Validation

Use a clean temporary directory for smoke testing:

```bash
tmpdir="$(mktemp -d)"
python3 skills/aws-terraform-template/scripts/init_template.py \
  --destination "$tmpdir" \
  --agent codex \
  --project-key network-core \
  --project-tag Network \
  --owner platform-team \
  --environment Network \
  --region sa-east-1 \
  --backend-bucket example-tf-state \
  --backend-key network-core/Network/terraform.tfstate \
  --auth-method environment \
  --skip-fmt
(cd "$tmpdir" && find env -maxdepth 3 -type f | sort)
```

Expected result:

```text
env/Network/backend.hcl
env/Network/tfsettings.yaml
```

For a full validation run in an environment with Terraform installed, omit `--skip-fmt` and confirm `terraform fmt -recursive` passes in the generated project.

## Design Choices

- **No base AWS resources:** The template establishes project structure without creating infrastructure by default.
- **Workspace-first environments:** Terraform reads settings from `env/${terraform.workspace}/tfsettings.yaml`.
- **No root input variables:** Environment and account configuration live in YAML, not root variables or `*.tfvars`.
- **Explicit backend configuration:** Backend settings are rendered into `env/<environment>/backend.hcl`.
- **Small, deterministic renderer:** The Python script copies static assets and replaces placeholders without external Python dependencies.

## Repository Layout

```text
aws-terraform-template/
+-- SKILL.md
+-- README.md
+-- agents/
|   +-- antigravity.md
|   +-- claude-code.md
|   +-- codex.md
|   +-- kiro.md
+-- assets/
|   +-- template/
+-- scripts/
    +-- init_template.py
```

## Publishing Checklist

Before publishing this skill on GitHub:

- Confirm `SKILL.md` has the final `name` and `description` metadata.
- Run the validation command above.
- Test installation into `${CODEX_HOME:-$HOME/.codex}/skills`.
- Restart Codex and invoke `/aws-terraform-template` from a clean directory.
- Add repository-level license and contribution files if this will be distributed publicly.
