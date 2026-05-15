# Antigravity Rules

Trigger on `/aws-terraform-template` or `/aws-terraform-template init`. Treat the commandless form as `init`.

Render the bundled minimal AWS Terraform template into the target repository. Ask for each missing required parameter. Abort on existing Terraform project files. Run `terraform fmt -recursive` after rendering.
