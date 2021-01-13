.EXPORT_ALL_VARIABLES:

include .env

SHELL=/bin/bash -o pipefail
IMAGE_REPO ?= jkutner/pycraft
K8S_NAMESPACE ?= minecraftasdfsa

build:
	@pack trust-builder jkutner/minecraft-builder:18
	@pack build $(IMAGE_REPO) --builder jkutner/minecraft-builder:18 --pull-policy if-not-present

publish: build
	@docker push $(IMAGE_REPO)

bash:
	@docker run -it --entrypoint=bash $(IMAGE_REPO)

run:
	@mkdir -p world
	@docker run -it --env-file .env -e JAVA_TOOL_OPTIONS="-Xmx2g" -v $(shell pwd)/config:/workspace/config:ro -v $(shell pwd)/world:/workspace/world -p 4711:4711 -p 8080:8080 -p 25566:25566 $(IMAGE_REPO)

tf:
	@test -f config/ops.json && : || echo "[]" > config/ops.json
	@test -f config/whitelist.json && : || echo "[]" > config/whitelist.json
	terraform apply -var "namespace=$(K8S_NAMESPACE)" -var "aws_s3_bucket=$(AWS_S3_BUCKET)" tf

restart:
	kubectl -n $(K8S_NAMESPACE) rollout restart deployment pycraft

logs:
	kubectl logs -n $(K8S_NAMESPACE) -l app=pycraft -f

.PHONY: build publish bash run tf
