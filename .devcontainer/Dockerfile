FROM ubuntu:22.04

ARG USERNAME=developer
ARG USER_UID=1000
ARG USER_GID=$USER_UID

ARG VERSION_RUST="nightly-2022-10-16"
ARG VERSION_BINARYEN="105-1"
ARG VERSION_WABT="1.0.27-1"

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    #
    # [Optional] Add sudo support. Omit if you don't need to install software after connecting.
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# Install some dependencies as root
RUN apt-get update && apt-get install -y \
    wget \ 
    build-essential \
    python3.10 python-is-python3 python3-pip \
    git

# Switch to regular user
USER $USERNAME
WORKDIR /home/${USERNAME}

# Install mxpy with rust and other tools
RUN pip3 install --no-cache-dir https://github.com/multiversx/mx-sdk-py-cli/archive/refs/heads/devcontainer.zip

RUN python -m multiversx_sdk_cli.cli deps install rust && \
    python -m multiversx_sdk_cli.cli deps install wasm-opt && \
    python -m multiversx_sdk_cli.cli deps install vmtools

ENV HOME=/home/${USERNAME}
ENV PATH="${HOME}/multiversx-sdk:${HOME}/multiversx-sdk/vendor-rust/bin:${HOME}/multiversx-sdk/vmtools:${PATH}"
ENV CARGO_HOME="${HOME}/multiversx-sdk/vendor-rust"
ENV RUSTUP_HOME="${HOME}/multiversx-sdk/vendor-rust"

RUN rustup component add rustfmt && \
    cargo install multiversx-sc-meta
