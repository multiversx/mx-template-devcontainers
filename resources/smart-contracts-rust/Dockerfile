FROM ubuntu:22.04

ARG USERNAME=developer
ARG USER_UID=1000
ARG USER_GID=$USER_UID

ARG VERSION_MXPY="v9.4.0"
ARG VERSION_RUST="nightly-2023-12-11"
ARG VERSION_SC_META="v0.47.1"
ARG VERSION_WASM_OPT="0.112.0"
ARG VERSION_VMTOOLS="v1.5.24"

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
    git \
    pkg-config \
    libssl-dev && \
    rm -rf /var/lib/apt/lists/*

# Switch to regular user
USER $USERNAME
WORKDIR /home/${USERNAME}

# Create "~/multiversx-sdk"
ENV MULTIVERSX=/home/${USERNAME}/multiversx-sdk
RUN mkdir ${MULTIVERSX}

# Install mxpy
RUN pip3 install --no-cache-dir https://github.com/multiversx/mx-sdk-py-cli/archive/refs/tags/${VERSION_MXPY}.zip
ENV PATH="${MULTIVERSX}:${PATH}"
COPY "mxpy" "${MULTIVERSX}/mxpy"

# Install rust and other tools
RUN mxpy config set "dependencies.rust.tag" ${VERSION_RUST} && \
    mxpy config set "dependencies.sc-meta.tag" ${VERSION_SC_META} && \
    mxpy config set "dependencies.wasm-opt.tag" ${VERSION_WASM_OPT} && \
    mxpy config set "dependencies.vmtools.tag" ${VERSION_VMTOOLS}
RUN mxpy deps install rust && rm -rf ${MULTIVERSX}/vendor-rust/registry/*
RUN mxpy deps install vmtools && rm ${MULTIVERSX}/*.tar.gz && sudo rm -rf ${MULTIVERSX}/golang

# Install test wallets
RUN mxpy deps install testwallets && rm ${MULTIVERSX}/*.tar.gz

ENV PATH="${MULTIVERSX}/vmtools:${PATH}"

RUN rustup component add rustfmt && rm -rf ${MULTIVERSX}/vendor-rust/registry/*

# This command will be executed once the devcontainer is created
COPY "post_create_command.py" "${MULTIVERSX}/devcontainer-resources/"
