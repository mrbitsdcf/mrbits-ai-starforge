# Codex Instructions

When the user invokes `/aws-terraform-template` or `/aws-terraform-template init`, use `skills/aws-terraform-template/SKILL.md`. Treat the commandless form as `init`.

Ask for each missing required parameter before writing files. Run `scripts/init_template.py` with the collected parameters, then run only:

```bash
terraform fmt -recursive
```

Do not run `terraform init` unless the user explicitly asks.
