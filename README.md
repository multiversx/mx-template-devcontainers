# mx-template-vscode-devcontainer-for-sc

Template repository: configuration for a devcontainer to be used in GitHub Codespaces, for Smart Contract development.

## Maintenance

Skip this section if you are not a maintainer of this repository.

Build the Docker image for local testing:

```
docker buildx build --output type=docker . -t template-vscode-devcontainer-for-sc:next -f ./Dockerfile
```

Build and publish the Docker image:

```
docker buildx build --push --platform=linux/amd64 . -t multiversx/template-vscode-devcontainer-for-sc:next -f ./Dockerfile
```
