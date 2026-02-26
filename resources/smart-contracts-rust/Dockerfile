FROM ubuntu:24.04

ARG USERNAME=ubuntu
ARG VERSION_MXPY="11.3.1"
ARG VERSION_RUST="1.90.0"
ARG VERSION_SC_META="0.64.2"

ENV DEBIAN_FRONTEND=noninteractive

# Base system dependencies
RUN apt-get update && apt-get install -y \
    sudo \
    curl \
    git \
    build-essential \
    pkg-config \
    libssl-dev \
    python3 \
    python3-venv \
    python3-pip \
    pipx \
    ca-certificates \
 && rm -rf /var/lib/apt/lists/*

# Give sudo access to the user without password
RUN echo ${USERNAME} ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/${USERNAME} \
    && chmod 0440 /etc/sudoers.d/${USERNAME}

USER ${USERNAME}
WORKDIR /home/${USERNAME}

# Environment variables
ENV MULTIVERSX="/home/${USERNAME}/multiversx-sdk"
ENV PATH="/home/${USERNAME}/.local/bin:${PATH}"
ENV PATH="/home/${USERNAME}/.cargo/bin:${PATH}"

# Install mxpy via pipx
RUN pipx install multiversx-sdk-cli==${VERSION_MXPY}

# Install Rust
RUN curl https://sh.rustup.rs -sSf | \
    sh -s -- -y --profile minimal --default-toolchain ${VERSION_RUST}

# Install sc-meta tools
RUN cargo install multiversx-sc-meta --version ${VERSION_SC_META} --locked \
    && sc-meta install all

# Install test wallets
RUN mxpy deps install testwallets

# Rust components + cleanup
RUN rustup component add rustfmt \
    && rm -rf /home/${USERNAME}/.cargo/registry \
    && rm -rf /home/${USERNAME}/.cargo/git

# Devcontainer resources
COPY post_create_command.py ${MULTIVERSX}/devcontainer-resources/

CMD ["bash"]
