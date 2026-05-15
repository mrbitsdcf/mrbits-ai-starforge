terraform {
  backend "s3" {
    region       = "__REGION__"
    bucket       = "__BACKEND_BUCKET__"
    key          = "__BACKEND_KEY__"
    encrypt      = true
    use_lockfile = true
  }
}

