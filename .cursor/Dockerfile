FROM python:3.9-bookworm

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        git \
        curl \
        sudo \
        mysql-server \
        default-libmysqlclient-dev \
        pkg-config \
        python3-venv \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -s /bin/bash ubuntu 2>/dev/null || true \
    && echo 'ubuntu ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers.d/ubuntu

USER ubuntu
WORKDIR /home/ubuntu
