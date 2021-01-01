resource "kubernetes_secret" "pycraft" {
  metadata {
    name = "pycraft-config"
    namespace = kubernetes_namespace.minecraft.metadata[0].name
  }

  data = {
    "ops.json" = file("${path.module}/../config/ops.json")
    "whitelist.json" = file("${path.module}/../config/whitelist.json")
  }
}
