terraform {
  required_providers {
    digitalocean = {
      source  = "digitalocean/digitalocean"
      version = "~> 2.0"
    }
  }

  backend "s3" {
    skip_requesting_account_id  = true
    skip_credentials_validation = true
    skip_get_ec2_platforms      = true
    skip_metadata_api_check     = true
    region                      = "us-east-1"
    key                         = "production/terraform.tfstate"
  }
}

locals {
  prefix = "${terraform.workspace}-${var.prefix}"
}