#!/usr/bin/env bash
set -euo pipefail

cd /workspace

if [ ! -d .venv ]; then
  python3 -m venv .venv
fi

. .venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
pip install 'numpy<2'
