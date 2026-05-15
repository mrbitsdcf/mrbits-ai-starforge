provider "aws" {
  region  = local.tfsettings.region
  profile = local.auth_profile

  dynamic "assume_role" {
    for_each = local.assume_role_enabled ? [local.auth_assume_role] : []

    content {
      role_arn     = assume_role.value.role_arn
      session_name = try(assume_role.value.session_name, null)
      external_id  = try(assume_role.value.external_id, null)
    }
  }

  default_tags {
    tags = local.tags
  }
}

provider "aws" {
  alias   = "secondary"
  region  = try(local.tfsettings.secondary_region, local.tfsettings.region)
  profile = local.auth_profile

  dynamic "assume_role" {
    for_each = local.assume_role_enabled ? [local.auth_assume_role] : []

    content {
      role_arn     = assume_role.value.role_arn
      session_name = try(assume_role.value.session_name, null)
      external_id  = try(assume_role.value.external_id, null)
    }
  }

  default_tags {
    tags = local.tags
  }
}

