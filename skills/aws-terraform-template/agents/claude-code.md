# Claude Code Instructions

Use this package when the user asks for `/aws-terraform-template`, `/aws-terraform-template init`, or requests a minimal AWS Terraform project template. Treat `/aws-terraform-template` with no command as `init`.

Ask for each missing project, backend, region, workspace, and authentication input before writing files. Render from `assets/template` with `scripts/init_template.py`. Abort if Terraform files already exist in the destination.
