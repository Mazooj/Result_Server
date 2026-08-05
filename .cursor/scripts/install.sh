#!/usr/bin/env bash
set -euo pipefail

cd /workspace

PYTHON=python3
if command -v python3.9 >/dev/null 2>&1; then
  PYTHON=python3.9
fi

if [ ! -d .venv ]; then
  "$PYTHON" -m venv .venv
fi

. .venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
pip install 'numpy<2'
