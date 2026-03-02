import pathlib

import yaml

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]

def _read_yaml(path: pathlib.Path):
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


defaults = _read_yaml(path=REPO_ROOT / "config" / "defaults.yaml")

ONTOLOGY_FILE = defaults["ontology_file"]
CACHE = defaults["test_cache"]