output "repo_endpoint" {
  value = data.digitalocean_container_registry.manihot_repo.endpoint
}

output "container_url" {
  value = digitalocean_app.app.live_url
}