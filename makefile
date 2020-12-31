.EXPORT_ALL_VARIABLES:

include .env

SHELL=/bin/bash -o pipefail
minecraft_version=1.12.2
image_repo=jkutner/pycraft

build:
	@pack build $(image_repo) -e MINECRAFT_VERSION="$(minecraft_version)" -e MINECRAFT_DIST="spigot" --builder jkutner/minecraft-builder:18 --pull-policy if-not-present

publish: build
	@docker push $(image_repo)

bash:
	@docker run -it --entrypoint=bash $(image_repo)

run:
	@docker run -it -e NGROK_API_TOKEN="$(NGROK_API_TOKEN)" -e JAVA_TOOL_OPTIONS="-Xmx2g" -p 4711:4711 -p 8080:8080 -p 25566:25566 $(image_repo)
