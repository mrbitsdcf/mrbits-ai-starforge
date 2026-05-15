package test

import (
	"os"
	"path/filepath"
	"testing"

	"github.com/gruntwork-io/terratest/modules/terraform"
)

func TestTemplateValidates(t *testing.T) {
	t.Parallel()

	root, err := filepath.Abs("../..")
	if err != nil {
		t.Fatal(err)
	}

	options := &terraform.Options{
		TerraformDir: root,
		NoColor:      true,
		EnvVars: map[string]string{
			"AWS_REGION": "__REGION__",
		},
	}

	terraform.RunTerraformCommand(t, options, "fmt", "-check", "-recursive")

	if os.Getenv("RUN_TERRAFORM_VALIDATE") == "1" {
		terraform.InitAndValidate(t, options)
	}
}

