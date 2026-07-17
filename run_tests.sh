#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

if [[ -f ".venv/Scripts/activate" ]]; then
  source .venv/Scripts/activate
elif [[ -f ".venv/bin/activate" ]]; then
  source .venv/bin/activate
else
  echo "Virtual environment not found" >&2
  exit 1
fi

pytest -q
