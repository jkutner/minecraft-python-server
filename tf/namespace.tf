resource "kubernetes_namespace" "minecraft" {
  metadata {
    name = "minecraft"
  }
}
