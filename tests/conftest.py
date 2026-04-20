import json
import re
import subprocess
import sys
import time
import tempfile
import uuid

import pytest
from pathlib import Path
from owlready2 import get_ontology

GTFS_ONTOLOGY_RDF = "/home/joe/Projects/research/transit/gtfs-ontology/artifacts/gtfs.rdf"

def run_cmd(proc, cmd, timeout=5):
    """
    Send a command to the RDFox shell and use a unique marker (echo <marker>)
    to detect when the command has fully completed.
    Streams output to the Python console as it arrives.
    Returns the captured output (excluding the marker).
    """

    # 1. Make a unique end marker
    marker = f"__END__{uuid.uuid4().hex}"

    # 2. Build the full payload
    full_cmd = f"{cmd}\necho {marker}\n"

    # Print the command being run
    # print(f"\n▶ RDFox $ {cmd}")
    sys.stdout.write(f"\n▶ RDFox $ {cmd}")
    sys.stdout.flush()

    proc.stdin.write(full_cmd)
    proc.stdin.flush()

    # 3. Collect lines until we see the marker
    output_lines = []
    start = time.time()

    while time.time() - start < timeout:
        line = proc.stdout.readline()

        if not line:
            continue

        # Stream to Python console
        sys.stdout.write(line)
        sys.stdout.flush()

        # Stop when the marker appears
        if marker in line:
            break

        output_lines.append(line)

    return "".join(output_lines)


def create_triple(
        subject,
        predicate,
        object,
):

    if subject is None or object is None:
        return None

    predicate[subject].append(object)
    return predicate

def extract_json_object(text: str) -> dict:
    """
    Extract the first full top-level JSON object from RDFox output,
    even if the JSON contains nested braces (e.g., 'head': {}).
    """
    start = text.find("{")
    if start == -1:
        raise ValueError("No JSON object found.")

    depth = 0
    for i in range(start, len(text)):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                json_str = text[start:i+1]
                import json
                return json.loads(json_str)

    raise ValueError("JSON braces did not balance.")


def extract_boolean(text: str) -> bool:
    obj = extract_json_object(text)
    return obj["boolean"]


@pytest.fixture(scope="session")
def rdfox_proc():
    """Start RDFox once per session."""
    proc = subprocess.Popen(
        ["RDFox", "sandbox"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    run_cmd(proc, "set output out")
    run_cmd(proc, "endpoint start")
    run_cmd(proc, "dstore create test")
    run_cmd(proc, "active test")
    run_cmd(proc, "prefix gtfs: <https://w3id.org/gtfs#>")
    run_cmd(proc, "set query.answer-format application/sparql-results+json")

    yield proc

    # Teardown
    proc.terminate()


@pytest.fixture
def clear_datastore(rdfox_proc):
    """Clear datastore before every test."""
    yield
    run_cmd(rdfox_proc, f"clear facts axioms force")


@pytest.fixture
def gtfs_onto():
    """Load GTFS ontology once."""
    onto = get_ontology(f"file://{GTFS_ONTOLOGY_RDF}").load()
    yield onto
    onto.destroy()


@pytest.fixture
def nt_writer():
    """Utility fixture: Write ontology instances to a temp NT file."""
    def _write(onto):
        tmp = tempfile.TemporaryDirectory()
        path = Path(tmp.name) / "data.nt"
        onto.save(file=str(path), format="ntriples")
        return path, tmp  # tmp keeps directory alive
    return _write


@pytest.fixture
def import_into_rdfox(rdfox_proc):
    """Import a file and wait until RDFox finishes processing."""
    def _import(path):
        run_cmd(rdfox_proc, f'import "{path}"')
    return _import



@pytest.fixture
def rdfox_ask(rdfox_proc):
    """Run SPARQL queries."""
    def _query(q):
        return run_cmd(rdfox_proc, f'ask {q}')
    return _query

@pytest.fixture(scope="module")
def import_rules(rdfox_proc, rules_path: str):
    """
    Imports the datalog rules for validating agencies into RDFox.
    """

    run_cmd(rdfox_proc, f'import "{str(rules_path)}"')