terraform {
  required_providers {
    kubernetes = {
      source = "hashicorp/kubernetes"
      version = "1.13.3"
    }
  }

  backend "kubernetes" {
    secret_suffix    = "pycraft"
    load_config_file = true
    namespace        = "terraform"
  }
}

provider "kubernetes" {}
