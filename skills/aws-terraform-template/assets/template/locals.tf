locals {
  default_tfsettings = {
    region           = "__REGION__"
    secondary_region = "__SECONDARY_REGION__"
    project_name     = "__PROJECT_KEY__"

    auth = {
      method  = "__AUTH_METHOD__"
      profile = "__PROFILE__"
      account = "__ACCOUNT__"

      assume_role = {
        role_arn     = "__ROLE_ARN__"
        session_name = "__PROJECT_KEY__-${terraform.workspace}"
        external_id  = null
      }
    }

    tags = {
      environment = "__ENVIRONMENT__"
      project     = "__PROJECT_TAG__"
      owner       = "__OWNER__"
    }
  }

  # Default tags that are applied after workspace tags.
  default_tags = {
    managed_by = "terraform"
  }

  # Collect workspace settings from env/<workspace>/tfsettings.yaml.
  tfsettingsfile        = "./env/${terraform.workspace}/tfsettings.yaml"
  tfsettingsfilecontent = fileexists(local.tfsettingsfile) ? file(local.tfsettingsfile) : "tfsettingsFileNotFound: true"
  tfworkspacesettings   = yamldecode(local.tfsettingsfilecontent)

  tfsettings = merge(local.default_tfsettings, local.tfworkspacesettings)

  auth                = merge(local.default_tfsettings.auth, try(local.tfworkspacesettings.auth, {}))
  auth_assume_role    = merge(local.default_tfsettings.auth.assume_role, try(local.tfworkspacesettings.auth.assume_role, {}))
  auth_profile        = contains(["profile", "sso", "assume-role"], try(local.auth.method, "")) && try(local.auth.profile, "") != "" ? local.auth.profile : null
  assume_role_enabled = try(local.auth.method, "") == "assume-role" && try(local.auth_assume_role.role_arn, "") != ""

  required_tags = ["environment", "project", "owner"]
  tags          = merge(local.default_tfsettings.tags, try(local.tfworkspacesettings.tags, {}), local.default_tags)

  project_name = lower(local.tfsettings.project_name)
  name_prefix  = "${local.project_name}-${terraform.workspace}"
  account_id   = data.aws_caller_identity.current.account_id
}

check "required_tags" {
  assert {
    condition     = alltrue([for tag in local.required_tags : contains(keys(local.tags), tag) && trimspace(local.tags[tag]) != ""])
    error_message = "Required tags must be present and non-empty: environment, project, owner."
  }
}

