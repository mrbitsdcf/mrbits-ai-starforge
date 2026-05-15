terraform {
  required_version = ">= __TERRAFORM_VERSION__"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> __AWS_PROVIDER_VERSION__"
    }

    random = {
      source  = "hashicorp/random"
      version = "~> __RANDOM_PROVIDER_VERSION__"
    }

    template = {
      source  = "hashicorp/template"
      version = "~> __TEMPLATE_PROVIDER_VERSION__"
    }

    null = {
      source  = "hashicorp/null"
      version = "~> __NULL_PROVIDER_VERSION__"
    }

    archive = {
      source  = "hashicorp/archive"
      version = "~> __ARCHIVE_PROVIDER_VERSION__"
    }
  }
}

