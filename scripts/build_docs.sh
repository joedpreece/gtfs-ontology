#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
#IMAGE="widoco:1.4.25"
IMAGE="ghcr.io/dgarijo/widoco:v1.4.25"

echo "Pulling Widoco image from $IMAGE..."
docker pull "$IMAGE"

echo "Done."

docker run --rm \
  -v "$ROOT":/data \
  $IMAGE \
  -ontFile /data/artefacts/ontologies/gtfs.owl.ttl \
  -outFolder /data/docs \
  -rewriteAll \
  -webVowl \
  -oops \
  -includeImportedOntologies \
  -noPlaceHolderText