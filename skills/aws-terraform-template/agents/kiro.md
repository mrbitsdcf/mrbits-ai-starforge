# Kiro Steering

Use this steering note for `/aws-terraform-template` or `/aws-terraform-template init`. Treat the commandless form as `init`.

Create a minimal AWS Terraform infrastructure repository from the bundled assets. Preserve `env/<workspace>/tfsettings.yaml`, `yamldecode()` loading, Terraform workspaces, and an empty root `variables.tf`.

Ask for each missing required parameter before writing files.

Do not add AWS resources to the base template.
