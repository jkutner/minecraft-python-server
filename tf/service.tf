resource "kubernetes_service" "pycraft" {
  metadata {
    name = "pycraft-service"
    namespace = kubernetes_namespace.minecraft.metadata[0].name
    labels = {
      app = "pycraft"
    }
  }
  spec {
    selector = {
      app = "pycraft"
    }
    port {
      name        = "minecraft"
      protocol    = "TCP"
      port        = 25566
      target_port = 25566
    }
    port {
      name        = "python"
      protocol    = "TCP"
      port        = 4711
      target_port = 4711
    }
    port {
      name        = "web"
      protocol    = "TCP"
      port        = 8080
      target_port = 8080
    }

    type = "LoadBalancer"
  }
}
