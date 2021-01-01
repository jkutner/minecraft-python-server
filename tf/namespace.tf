resource "kubernetes_namespace" "minecraft" {
  metadata {
    name = var.namespace
  }
}
