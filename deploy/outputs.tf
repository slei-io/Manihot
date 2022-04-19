output "repo_endpoint" {
  value = data.digitalocean_container_registry.manihot_repo.endpoint
}

output "container_url" {
  value = digitalocean_app.app.live_url
}

output "container_default_ingress" {
  value = digitalocean_app.app.default_ingress
}

output "deployed_tag" {
  value = var.image_tag
}