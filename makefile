.EXPORT_ALL_VARIABLES:

include .env

SHELL=/bin/bash -o pipefail
image_repo=jkutner/pycraft
K8S_NAMESPACE ?= minecraftasdfsa

build:
	@pack build $(image_repo) --builder jkutner/minecraft-builder:18 --pull-policy if-not-present

publish: build
	@docker push $(image_repo)

bash:
	@docker run -it --entrypoint=bash $(image_repo)

run:
	@mkdir -p world
	@docker run -it --env-file .env -e JAVA_TOOL_OPTIONS="-Xmx2g" -v $(shell pwd)/config:/workspace/config:ro -v $(shell pwd)/world:/workspace/world -p 4711:4711 -p 8080:8080 -p 25566:25566 $(image_repo)

tf:
	terraform apply -var "namespace=$(K8S_NAMESPACE)" tf

restart:
	kubectl -n $(K8S_NAMESPACE) rollout restart deployment pycraft

logs:
	kubectl logs -n $(K8S_NAMESPACE) -l app=pycraft -f

.PHONY: build publish bash run tf
