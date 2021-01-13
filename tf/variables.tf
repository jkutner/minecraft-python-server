variable "namespace" {
  default = "minecraft"
}

variable "aws_s3_bucket" {}

variable "image_repo" {
  default = "ghcr.io/jkutner/apps/pycraft"
}
