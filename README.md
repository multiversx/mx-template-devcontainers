# mx-template-vscode-devcontainer-for-sc

Template repository: configuration for a devcontainer to be used in GitHub Codespaces, for Smart Contract development.

## Local setup

 - Clone this repository
 - In VSCode, install the Dev Containers extension (from Microsoft)
 - Launch the command `Dev Containers: Rebuild and Reopen in Container` (for first run), or `Dev Containers: Reopen in Container` (for subsequent runs).
 
The local setup will be simplified once the template is published.

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
