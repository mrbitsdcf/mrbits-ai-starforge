# __PROJECT_KEY__

Minimal AWS Terraform infrastructure template.

This repository uses Terraform workspaces and per-workspace YAML settings from `env/<workspace>/tfsettings.yaml`. Root `*.tfvars` files are intentionally not used.

## Prerequisites

- Terraform `>= __TERRAFORM_VERSION__`
- AWS CLI v2
- `tflint`
- `checkov`
- `terraform-docs`
- `pre-commit`
- Go, for Terratest
- Ruby and Bundler, for Kitchen-Terraform

## Backend Bootstrap

Terraform state is stored in S3 with encryption and native S3 lockfile support.

Create the state bucket before running `terraform init`:

```bash
aws s3api create-bucket \
  --bucket __BACKEND_BUCKET__ \
  --region __REGION__ \
  --create-bucket-configuration LocationConstraint=__REGION__

aws s3api put-bucket-versioning \
  --bucket __BACKEND_BUCKET__ \
  --versioning-configuration Status=Enabled

aws s3api put-bucket-encryption \
  --bucket __BACKEND_BUCKET__ \
  --server-side-encryption-configuration '{"Rules":[{"ApplyServerSideEncryptionByDefault":{"SSEAlgorithm":"AES256"}}]}'

aws s3api put-public-access-block \
  --bucket __BACKEND_BUCKET__ \
  --public-access-block-configuration BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true
```

## Authentication

### AWS SSO

```bash
aws sso login --profile __PROFILE__
AWS_PROFILE=__PROFILE__ terraform init -backend-config=env/__ENVIRONMENT__/backend.hcl
```

### AWS Profile

```bash
AWS_PROFILE=__PROFILE__ terraform init -backend-config=env/__ENVIRONMENT__/backend.hcl
```

### Environment Variables

```bash
export AWS_ACCESS_KEY_ID="..."
export AWS_SECRET_ACCESS_KEY="..."
export AWS_SESSION_TOKEN="..."
terraform init -backend-config=env/__ENVIRONMENT__/backend.hcl
```

### Assume Role

Set `auth.method: assume-role` and `auth.assume_role.role_arn` in the workspace YAML.

## Commands

```bash
terraform workspace list
terraform workspace new __ENVIRONMENT__ || terraform workspace select __ENVIRONMENT__
terraform init -backend-config=env/__ENVIRONMENT__/backend.hcl
terraform fmt -recursive
terraform validate
terraform plan
terraform apply
```

## Workspaces and Environments

Each Terraform workspace must have a matching directory:

```text
env/<workspace>/tfsettings.yaml
env/<workspace>/backend.hcl
```

Use Terraform workspaces exclusively for environment and account separation.

## Tags

Required tags:

- `environment`
- `project`
- `owner`

Tag keys are always English. Tag values may be English or Portuguese.

## Naming

Use `local.name_prefix` for resources:

```hcl
name = "${local.name_prefix}-example"
```

The project name prefix is lowercase and comes from `project_name` in the workspace YAML.

## Security

- Do not commit secrets.
- Do not use `*.tfvars`.
- Use IAM least privilege.
- Use S3 encryption and block public access for state buckets.
- Enable CloudTrail in managed AWS accounts.
- Prefer AWS SSO, named profiles, or assume-role over hard-coded credentials.

## Quality

```bash
terraform fmt -recursive
terraform validate
tflint --config .tflint.hcl
checkov -d .
terraform-docs markdown table --output-file README.md --output-mode inject .
pre-commit run --all-files
```

## Tests

Terratest scaffold:

```bash
cd test/terratest
go test ./...
```

Kitchen-Terraform scaffold:

```bash
bundle install
kitchen test
```

## Troubleshooting

- If `terraform init` cannot access the backend, verify bucket name, region, credentials, and S3 permissions.
- If authentication fails, verify `auth.method`, `auth.profile`, `AWS_PROFILE`, or `auth.assume_role.role_arn`.
- If workspace settings fail to load, verify `env/<workspace>/tfsettings.yaml` exists.
- If required tags fail validation, set `environment`, `project`, and `owner`.

<!-- BEGIN_TF_DOCS -->
<!-- END_TF_DOCS -->
