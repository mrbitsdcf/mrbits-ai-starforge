#!/usr/bin/env python3
"""Render the AWS Terraform template into a target repository."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


TEMPLATE_DIR = Path(__file__).resolve().parents[1] / "assets" / "template"
CONFLICT_NAMES = {
    ".editorconfig",
    ".gitignore",
    ".kitchen.yml",
    ".pre-commit-config.yaml",
    ".terraform-docs.yaml",
    ".tflint.hcl",
    "README.md",
    "backend.tf",
    "data.tf",
    "locals.tf",
    "main.tf",
    "outputs.tf",
    "providers.tf",
    "variables.tf",
    "versions.tf",
    "env",
    "modules",
    "test",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", nargs="?", default="init", choices=["init"], help="Command to run. Defaults to init.")
    parser.add_argument("--destination", default=".", help="Repository or directory to initialize.")
    parser.add_argument("--agent", choices=["codex", "claude-code", "kiro", "antigravity"], help="Agent instructions to render.")
    parser.add_argument("--project-key", help="Lowercase Terraform naming prefix.")
    parser.add_argument("--project-tag", help="Required AWS tag value for project.")
    parser.add_argument("--owner", help="Required AWS tag value for owner.")
    parser.add_argument("--environment", help="Required AWS tag value for environment.")
    parser.add_argument("--region", help="Primary AWS region.")
    parser.add_argument("--backend-bucket", help="Existing S3 bucket for Terraform state.")
    parser.add_argument("--backend-key", help="S3 key for Terraform state.")
    parser.add_argument(
        "--auth-method",
        choices=["environment", "profile", "sso", "assume-role"],
        help="AWS authentication mode.",
    )
    parser.add_argument("--profile", default="", help="AWS profile or SSO profile when selected.")
    parser.add_argument("--account", default="", help="Optional AWS account identifier for documentation/settings.")
    parser.add_argument("--role-arn", default="", help="Assume-role ARN when auth-method is assume-role.")
    parser.add_argument("--secondary-region", default="", help="Optional secondary provider region.")
    parser.add_argument("--terraform-version", default="1.15.3")
    parser.add_argument("--aws-provider-version", default="6.45.0")
    parser.add_argument("--random-provider-version", default="3.8.1")
    parser.add_argument("--template-provider-version", default="2.2.0")
    parser.add_argument("--null-provider-version", default="3.2.4")
    parser.add_argument("--archive-provider-version", default="2.8.0")
    parser.add_argument("--skip-fmt", action="store_true", help="Do not run terraform fmt after rendering.")
    return parser.parse_args()


def prompt_required(label: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    while True:
        value = input(f"{label}{suffix}: ").strip()
        if value:
            return value
        if default:
            return default
        print(f"{label} is required.")


def prompt_choice(label: str, choices: list[str], default: str = "") -> str:
    choice_list = ", ".join(choices)
    suffix = f" [{default}]" if default else ""
    while True:
        value = input(f"{label} ({choice_list}){suffix}: ").strip()
        if not value and default:
            value = default
        if value in choices:
            return value
        print(f"Choose one of: {choice_list}.")


def collect_missing_args(args: argparse.Namespace) -> argparse.Namespace:
    if not args.agent:
        args.agent = prompt_choice("agent", ["codex", "claude-code", "kiro", "antigravity"], "codex")
    if not args.project_key:
        args.project_key = prompt_required("project-key")
    if not args.project_tag:
        args.project_tag = prompt_required("project-tag")
    if not args.owner:
        args.owner = prompt_required("owner")
    if not args.environment:
        args.environment = prompt_required("environment")
    if not args.region:
        args.region = prompt_required("region")
    if not args.backend_bucket:
        args.backend_bucket = prompt_required("backend-bucket")
    if not args.backend_key:
        args.backend_key = prompt_required("backend-key")
    if not args.auth_method:
        args.auth_method = prompt_choice("auth-method", ["environment", "profile", "sso", "assume-role"])
    if args.auth_method in {"profile", "sso"} and not args.profile:
        args.profile = prompt_required("profile")
    if args.auth_method == "assume-role" and not args.role_arn:
        args.role_arn = prompt_required("role-arn")
    return args


def validate_args(args: argparse.Namespace) -> None:
    if args.project_key != args.project_key.lower():
        raise ValueError("--project-key must be lowercase.")
    if "_" in args.project_key:
        raise ValueError("--project-key must use hyphens instead of underscores.")
    if any(separator in args.environment for separator in ("/", "\\")):
        raise ValueError("--environment must be a directory name, not a path.")
    if args.environment in {".", ".."}:
        raise ValueError("--environment must not be . or ..")
    if args.auth_method in {"profile", "sso"} and not args.profile:
        raise ValueError("--profile is required when --auth-method is profile or sso.")
    if args.auth_method == "assume-role" and not args.role_arn:
        raise ValueError("--role-arn is required when --auth-method is assume-role.")
    if not args.backend_key.endswith("terraform.tfstate"):
        raise ValueError("--backend-key must end with terraform.tfstate.")


def abort_on_conflicts(destination: Path) -> None:
    existing = sorted(name for name in CONFLICT_NAMES if (destination / name).exists())
    if existing:
        joined = ", ".join(existing)
        raise FileExistsError(f"Destination already contains template-managed files: {joined}")


def render_text(text: str, replacements: dict[str, str]) -> str:
    for key, value in replacements.items():
        text = text.replace(f"__{key}__", value)
    return text


def render_relative_path(path: Path, replacements: dict[str, str]) -> Path:
    parts = list(path.parts)
    if len(parts) >= 2 and parts[0] == "env" and parts[1] == "default":
        parts[1] = replacements["ENVIRONMENT_DIR"]
    rendered_parts = [render_text(part, replacements) for part in parts]
    return Path(*rendered_parts)


def copy_template(destination: Path, replacements: dict[str, str]) -> None:
    for source in TEMPLATE_DIR.rglob("*"):
        relative = source.relative_to(TEMPLATE_DIR)
        relative = render_relative_path(relative, replacements)
        target = destination / relative
        if source.is_dir():
            target.mkdir(parents=True, exist_ok=True)
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        text = source.read_text(encoding="utf-8")
        target.write_text(render_text(text, replacements), encoding="utf-8")


def render_agent_file(skill_root: Path, destination: Path, agent: str) -> None:
    source = skill_root / "agents" / f"{agent}.md"
    if not source.exists():
        return
    target_dir = destination / ".agent-instructions"
    target_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target_dir / f"aws-terraform-template-{agent}.md")


def run_fmt(destination: Path) -> None:
    result = subprocess.run(
        ["terraform", "fmt", "-recursive"],
        cwd=destination,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if result.returncode != 0:
        sys.stdout.write(result.stdout)
        raise RuntimeError("terraform fmt -recursive failed.")


def main() -> int:
    args = parse_args()
    try:
        collect_missing_args(args)
        validate_args(args)
        destination = Path(args.destination).resolve()
        destination.mkdir(parents=True, exist_ok=True)
        abort_on_conflicts(destination)
        secondary_region = args.secondary_region or args.region
        replacements = {
            "PROJECT_KEY": args.project_key,
            "PROJECT_TAG": args.project_tag,
            "OWNER": args.owner,
            "ENVIRONMENT": args.environment,
            "ENVIRONMENT_DIR": args.environment,
            "REGION": args.region,
            "SECONDARY_REGION": secondary_region,
            "BACKEND_BUCKET": args.backend_bucket,
            "BACKEND_KEY": args.backend_key,
            "AUTH_METHOD": args.auth_method,
            "PROFILE": args.profile,
            "ACCOUNT": args.account,
            "ROLE_ARN": args.role_arn,
            "TERRAFORM_VERSION": args.terraform_version,
            "AWS_PROVIDER_VERSION": args.aws_provider_version,
            "RANDOM_PROVIDER_VERSION": args.random_provider_version,
            "TEMPLATE_PROVIDER_VERSION": args.template_provider_version,
            "NULL_PROVIDER_VERSION": args.null_provider_version,
            "ARCHIVE_PROVIDER_VERSION": args.archive_provider_version,
        }
        copy_template(destination, replacements)
        render_agent_file(Path(__file__).resolve().parents[1], destination, args.agent)
        if not args.skip_fmt:
            run_fmt(destination)
    except Exception as exc:
        print(f"aws-terraform-template: {exc}", file=sys.stderr)
        return 1
    print(f"Generated AWS Terraform template at {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
