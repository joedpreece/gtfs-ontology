#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
IMAGE="obolibrary/robot:v1.9.8"

echo "Pulling ROBOT image from $IMAGE..."
docker pull "$IMAGE"

echo "Validating RL."

docker run --rm \
  -v "$ROOT":/data \
  -w /data \
  $IMAGE \
  robot validate-profile \
  --profile DL \
  --input /data/artefacts/ontologies/ies-common.ttl \
  --output /data/artefacts/ontologies/ies-common-dl-report.txt

echo "Done."