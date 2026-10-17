#!/usr/bin/env bash
set -e

# Navigate to project root
cd "$(dirname "$0")/.."

echo "==> Checking virtual environment in .venv..."
if [ ! -d ".venv" ]; then
    echo "Creating new virtual environment..."
    python3 -m venv .venv
else
    echo ".venv already exists."
fi

echo "==> Upgrading pip..."
./.venv/bin/python -m pip install --upgrade pip --quiet

echo "==> Installing requirements..."
./.venv/bin/pip install -r requirements.txt --quiet

echo ""
echo "Virtual environment setup complete!"
echo "To activate in your terminal:"
echo "  source .venv/bin/activate"
