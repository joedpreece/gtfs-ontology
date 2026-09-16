#!/usr/bin/env bash
set -euo pipefail

# Get the absolute path of the project root directory (one level up from scripts/)
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "Starting Morph-KGC RML materialisation..."

python -m morph_kgc "${PROJECT_DIR}/scripts/config.ini"

echo "Materialisation complete."