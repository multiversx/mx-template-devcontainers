# mx-template-devcontainers

MultiversX devcontainer templates to be used in **VSCode** or **GitHub Codespaces**, for Smart Contract development (others to come).

## For users of the templates

Before everything, please follow the Visual Studio Code series on dev containers:
 - [Beginner's Series to Dev Containers](https://youtube.com/playlist?list=PLj6YeMhvp2S5G_X6ZyMc8gfXPMFPg3O31)
 - [Dev Container How To](https://youtube.com/playlist?list=PLj6YeMhvp2S6GjVyDHTPp8tLOR0xLGLYb)
 - [Developing inside a Container](https://code.visualstudio.com/docs/devcontainers/containers)

In Visual Studio code, the following MultiversX dev containers are available:

 - [MultiversX: Smart Contracts Development (Rust)](src/smart-contracts-rust)
 - ...

### Using the Docker images without VSCode

If you'd like to use the Docker image(s) to invoke `mxpy` commands and build contracts directly from a terminal, without VSCode's devcontainers feature, below are a few examples.

First, let's export some environment variables:

```
export IMAGE=multiversx/devcontainer-smart-contracts-rust:next
export DOCKER_USER=$(id -u):$(id -g)

# Mandatory: run the container as the current user (should be 1000:1000), not as root.
# Suggestion: use a stateless container; remove it after use (--rm).
# Suggestion: map the current directory to "/data" in the container.
export RUN="docker run --user=${DOCKER_USER} --rm -it --volume $(pwd):/data"
```

Run the container and do a quick inspection:

```
${RUN} ${IMAGE} whoami
${RUN} ${IMAGE} mxpy --version
${RUN} ${IMAGE} mxpy deps check rust
```

Clone `mx-contracts-rs` locally, then build a few contracts within the container:

```
git clone https://github.com/multiversx/mx-contracts-rs.git  --single-branch --depth=1

${RUN} ${IMAGE} mxpy contract build /data/mx-contracts-rs/contracts/adder
stat ./mx-contracts-rs/contracts/adder/output/adder.wasm

${RUN} ${IMAGE} mxpy contract build /data/mx-contracts-rs/contracts/ping-pong-egld
stat ./mx-contracts-rs/contracts/ping-pong-egld/output/ping-pong-egld.wasm
```

Deploy a previously-built smart contract on Testnet:

```
${RUN} ${IMAGE} mxpy contract deploy \
    --bytecode /data/mx-contracts-rs/contracts/adder/output/adder.wasm \
    --arguments 0 \
    --pem /home/developer/multiversx-sdk/testwallets/latest/users/frank.pem \
    --recall-nonce \
    --gas-limit 5000000 \
    --chain T \
    --proxy https://testnet-gateway.multiversx.com \
    --send
```

Call a function of a previously-deployed smart contract:

```
${RUN} ${IMAGE} mxpy contract call \
    erd1qqqqqqqqqqqqqpgq5v3ra8mxjkv6g2pues9tdkkzwmtm9fdht7asp8wtnr \
    --function "add" \
    --arguments 42 \
    --pem /home/developer/multiversx-sdk/testwallets/latest/users/frank.pem \
    --recall-nonce \
    --gas-limit 5000000 \
    --chain T \
    --proxy https://testnet-gateway.multiversx.com \
    --send
```

Query a smart contract:

```
${RUN} ${IMAGE} mxpy contract query \
    erd1qqqqqqqqqqqqqpgq5v3ra8mxjkv6g2pues9tdkkzwmtm9fdht7asp8wtnr \
    --function "getSum" \
    --proxy https://testnet-gateway.multiversx.com
```

Setup a localnet (make sure to set the `--workdir`, as well), then inspect the generated files (on the mapped volume):

```
${RUN} --workdir /data ${IMAGE} mxpy localnet setup
cat ./localnet.toml
tree -L 1 ./localnet
```

Start the localnet (make sure to publish the necessary ports; see the generated `localnet.toml`):

```
${RUN} --workdir /data --publish 7950:7950 ${IMAGE} mxpy localnet start
```

You can pause the localnet by simply stopping the container, then restart it by invoking the `start` command again.

In a separate terminal, inspect an endpoint of the localnet's Proxy (as a smoke test):

```
curl http://127.0.0.1:7950/network/config | jq
```

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
docker build ./resources/smart-contracts-rust -t multiversx/devcontainer-smart-contracts-rust:next -f ./resources/smart-contracts-rust/Dockerfile
```

### Test the templates

```
rm -rf "/tmp/test-workspace" && mkdir -p "/tmp/test-workspace" && \
cp -R "src/smart-contracts-rust/.devcontainer" "/tmp/test-workspace" && \
code "/tmp/test-workspace/"
```

Then, in VSCode, launch the command `Dev Containers: Rebuild and Reopen in Container`, wait, then inspect the environment (e.g. check version of `mxpy`, `rust`, build the sample smart contracts, verify output of rust-analyzer).

### Publish images

Locally:

```
docker build ./resources/smart-contracts-rust -t multiversx/devcontainer-smart-contracts-rust:next -f ./resources/smart-contracts-rust/Dockerfile
docker push multiversx/devcontainer-smart-contracts-rust:next
```

On Github, trigger the GitHub workflow(s) `publish-image-*.yml` to publish the image(s). Ideally, do this on the `main` branch.

### Publish templates

Trigger the GitHub workflow `publish-templates.yml` to publish the templates. Ideally, do this on the `main` branch.
