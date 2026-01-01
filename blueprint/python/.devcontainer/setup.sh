#!/usr/bin/env bash
#
# Setup for python dev-container

# upgrade the world with aptitude
apt update
apt install aptitude -y
aptitude safe-upgrade -y

# install UV
curl -LsSf https://astral.sh/uv/install.sh | env UV_INSTALL_DIR="/usr/local/bin" sh

# update the project environment
uv sync

# ensure dockerd is warmed up
docker version

