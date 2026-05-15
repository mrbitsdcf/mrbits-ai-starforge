---
name: aws-terraform-template
description: Portable Terraform AWS project bootstrap skill. Use when the user asks to run `/aws-terraform-template` or `/aws-terraform-template init`, create a minimal AWS Terraform infrastructure repository, bootstrap Terraform for AWS, initialize an AWS IaC project, or generate agent-specific instructions for Codex, Claude Code, Kiro, or Antigravity.
---

# AWS Terraform Template

Create a minimal AWS Terraform infrastructure project from the bundled template assets.

## Workflow

1. Treat `/aws-terraform-template` with no command as `/aws-terraform-template init`.
2. Ask the user for each missing required input before writing files. If no parameters are provided, ask for them one at a time in this order:
   - `agent`: one of `codex`, `claude-code`, `kiro`, or `antigravity`. Default to `codex` when the caller is using Codex and did not specify an agent.
   - `project-key`: lowercase infrastructure name prefix, for example `network-core`.
   - `project-tag`: business/project tag value. This is not necessarily the same as `project-key`.
   - `owner`: required tag value.
   - `environment`: workspace/environment tag value. Default example: `Network`.
   - `region`: AWS region.
   - `backend-bucket`: existing S3 bucket for Terraform state.
   - `backend-key`: S3 state key or prefix ending in `terraform.tfstate`.
   - `auth-method`: one of `environment`, `profile`, `sso`, or `assume-role`.
3. If `auth-method` is `profile` or `sso`, ask for `profile`.
4. If `auth-method` is `assume-role`, ask for `role-arn`; ask for `profile` only if the caller wants a source profile.
5. Abort if the destination already contains Terraform project files such as `*.tf`, `.terraform-docs.yaml`, `.tflint.hcl`, `.pre-commit-config.yaml`, `env/`, `modules/`, `test/`, or `README.md`.
6. Before changing default Terraform or provider versions, verify the latest stable releases in official HashiCorp sources. Use stable releases, not alpha/beta/RC releases.
7. Run `scripts/init_template.py` from this skill to render files from `assets/template`. The script also prompts interactively for any missing required arguments.
8. Run `terraform fmt -recursive` in the generated project only. Do not run `terraform init`, `terraform validate`, `checkov`, `tflint`, Terratest, or Kitchen unless the user explicitly asks.

## Command

```bash
python3 skills/aws-terraform-template/scripts/init_template.py \
  --destination . \
  --agent codex \
  --project-key network-core \
  --project-tag Network \
  --owner platform-team \
  --environment Network \
  --region sa-east-1 \
  --backend-bucket my-terraform-state-bucket \
  --backend-key network-core/Network/terraform.tfstate \
  --auth-method profile \
  --profile my-aws-profile
```

Use `--agent codex`, `--agent claude-code`, `--agent kiro`, or `--agent antigravity` to render the matching agent instruction file into the repository.

## Rules

- Preserve repository-level instructions such as `AGENTS.md`, `CLAUDE.md`, `.kiro/`, and Antigravity rule files.
- Do not create root Terraform input variables. Keep root `variables.tf` empty.
- Keep environment configuration in `env/<workspace>/tfsettings.yaml` read with `yamldecode()` from `locals.tf`.
- Use Terraform workspaces exclusively for environments and accounts.
- Do not create AWS resources in the base template.
- Do not use `*.tfvars`.
- Do not commit changes automatically.

## Template Facts

- Backend: S3 with encryption and native S3 lockfile.
- Provider: AWS with optional profile, optional assume-role, default tags, and a secondary alias for future multi-region or multi-account work.
- Required tags: `environment`, `project`, `owner`.
- Quality files: `.tflint.hcl`, `.terraform-docs.yaml`, `.pre-commit-config.yaml`, `.gitignore`, `.editorconfig`.
- Test scaffolds: `test/terratest` and `.kitchen.yml`.

## Validation Prompt

Use this prompt to validate the skill on a clean temporary directory:

```text
/aws-terraform-template init --agent codex --project-key network-core --project-tag Network --owner platform-team --environment Network --region sa-east-1 --backend-bucket example-tf-state --backend-key network-core/Network/terraform.tfstate --auth-method profile --profile sandbox
```

Expected result: the directory contains the rendered Terraform template, no AWS resources, no root variables, a workspace YAML under `env/Network/tfsettings.yaml`, S3 backend configuration, quality configs, test scaffolds, and `terraform fmt -recursive` passes.
