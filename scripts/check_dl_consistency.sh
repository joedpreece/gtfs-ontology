#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
IMAGE="obolibrary/robot:v1.9.8"

echo "Pulling ROBOT image from $IMAGE..."
docker pull "$IMAGE"

echo "Checking for unsatisfiable classes..."

docker run --rm \
  -v "$ROOT":/data \
  -w /data \
  $IMAGE \
  robot reason \
    --reasoner hermit \
    --input /data/artefacts/ontologies/gtfs.owl.ttl \
    --output /data/artefacts/ontologies/reasoned.owl.ttl