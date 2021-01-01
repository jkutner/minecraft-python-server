resource "kubernetes_deployment" "pycraft" {
  metadata {
    name = "pycraft"
    namespace = kubernetes_namespace.minecraft.metadata[0].name
    labels = {
      app = "pycraft"
    }
  }

  spec {
    replicas = 1
    selector {
      match_labels = {
        app = "pycraft"
      }
    }
    template {
      metadata {
        labels = {
          app = "pycraft"
        }
      }
      spec {
        volume {
          name = "pycraft-config"
          secret {
            secret_name = "pycraft-config"
          }
        }
        container {
          image = "jkutner/pycraft"
          name  = "pycraft-server"

          port {
            container_port = 8080
          }
          port {
            container_port = 25566
          }
          port {
            container_port = 4711
          }

          volume_mount {
            name = "pycraft-config"
            read_only = true
            mount_path = "/workspace/config"
          }

          resources {
            limits {
              cpu    = "0.5"
              memory = "2Gi"
            }
            requests {
              cpu    = "250m"
              memory = "512Mi"
            }
          }

          readiness_probe {
            tcp_socket {
              port = 25566
            }
          }
        }
      }
    }
  }
}
