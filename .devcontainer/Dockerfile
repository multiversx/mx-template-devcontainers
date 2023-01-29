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
    python3.10 python3-pip \
    git && \
    rm -rf /var/lib/apt/lists/*

# Switch to regular user
USER $USERNAME
WORKDIR /home/${USERNAME}

# Install mxpy with rust and other tools
RUN pip3 install --no-cache-dir https://github.com/multiversx/mx-sdk-py-cli/archive/refs/heads/devcontainer.zip

ENV MULTIVERSX=/home/${USERNAME}/multiversx-sdk

RUN python3 -m multiversx_sdk_cli.cli deps install rust && rm -rf ${MULTIVERSX}/vendor-rust/registry/*
RUN python3 -m multiversx_sdk_cli.cli deps install wasm-opt && rm ${MULTIVERSX}/*.tar.gz
RUN python3 -m multiversx_sdk_cli.cli deps install vmtools && rm ${MULTIVERSX}/*.tar.gz && sudo rm -rf ${MULTIVERSX}/golang

ENV PATH="${MULTIVERSX}/vendor-rust/bin:${MULTIVERSX}/vmtools:${PATH}"
ENV CARGO_HOME="${MULTIVERSX}/vendor-rust"
ENV RUSTUP_HOME="${MULTIVERSX}/vendor-rust"

RUN rustup component add rustfmt && rm -rf ${MULTIVERSX}/vendor-rust/registry/*
RUN cargo install multiversx-sc-meta && rm -rf ${MULTIVERSX}/vendor-rust/registry/*
