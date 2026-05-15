# frozen_string_literal: true

control "terraform-template-files" do
  impact 1.0
  title "Terraform template files exist"

  describe file("versions.tf") do
    it { should exist }
  end

  describe file("variables.tf") do
    it { should exist }
    its("content") { should_not match(/^variable\s+"/) }
  end

  describe file("env/__ENVIRONMENT__/tfsettings.yaml") do
    it { should exist }
    its("content") { should match(/environment:/) }
    its("content") { should match(/project:/) }
    its("content") { should match(/owner:/) }
  end
end
