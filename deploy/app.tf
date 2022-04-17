resource "digitalocean_app" "app" {
  spec {
    name   = "${local.prefix}-consumer"
    region = var.region

    service {
      name               = "${local.prefix}-consumer"
      instance_count     = 1
      instance_size_slug = var.app_instance_size
      http_port          = 80

      image {
        registry_type = "DOCR"
        repository    = var.app_name
        tag           = "latest"
      }
    }
  }
}