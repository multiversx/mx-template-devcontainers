# mx-template-vscode-devcontainer-for-sc

Template repository: configuration for a devcontainer to be used in GitHub Codespaces, for Smart Contract development.

## For users of the templates

Before everything, please follow the Visual Studio Code series on dev containers:
 - [Beginner's Series to Dev Containers](https://youtube.com/playlist?list=PLj6YeMhvp2S5G_X6ZyMc8gfXPMFPg3O31)
 - [Dev Container How To](https://youtube.com/playlist?list=PLj6YeMhvp2S6GjVyDHTPp8tLOR0xLGLYb)
 - [Developing inside a Container](https://code.visualstudio.com/docs/devcontainers/containers)

In Visual Studio code, the following MultiversX dev containers are available:
 - TBD
 - TBD


## For maintainers of the templates

Skip this section if you are not a maintainer of this repository.

Resources:
 - [Create a Dev Container](https://code.visualstudio.com/docs/devcontainers/create-dev-container)
 - [devcontainers/templates](https://github.com/devcontainers/templates)
 - [devcontainers/template-starter](https://github.com/devcontainers/template-starter)
 - [Public index of templates](https://containers.dev/templates)


### Build images

Build the Docker images for local testing:

```
docker buildx build --output type=docker ./resources/smart-contracts-rust -t multiversx/template-devcontainer-smart-contracts-rust:next -f ./resources/smart-contracts-rust/Dockerfile
```

### Test the templates

```
rm -rf "/tmp/test-workspace" && mkdir -p "/tmp/test-workspace" && \
cp -R "src/smart-contracts-rust/.devcontainer" "/tmp/test-workspace" && \
code "/tmp/test-workspace/"
```

Then, in VSCode, launch the command `Dev Containers: Rebuild and Reopen in Container`, wait, then inspect the environment.

### Publish images

Build and publish the Docker images:

```
docker buildx build --push --platform=linux/amd64 ./resources/smart-contracts-rust -t multiversx/template-devcontainer-smart-contracts-rust:next -f ./resources/smart-contracts-rust/Dockerfile
```

### Publish templates

Trigger the GitHub workflow `publish.yml` to publish the templates. Ideally, do this on the `main` branch.
