
import subprocess
import sys
import time
import tempfile
import uuid

import pytest
from pathlib import Path
from owlready2 import get_ontology

from config import GTFS_ONTOLOGY_RDF


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
    print(f"\n▶ RDFox $ {cmd}")
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


# def run_cmd(proc, cmd, timeout=3):
#
#
#     marker = f"__END__{time.time()}"
#     proc.stdin.write(f"{cmd}\necho {marker}\n")
#     proc.stdin.flush()
#
#     output = []
#     start = time.time()
#     while time.time() - start < timeout:
#         line = proc.stdout.readline()
#         if marker in line:
#             break
#         output.append(line)
#
#     print(output)
#
#     return "".join(output)


def create_triple(
        subject,
        predicate,
        object,
):

    if subject is None or object is None:
        return None

    predicate[subject].append(object)
    return predicate


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
    run_cmd(proc, "prefix gtfs: <http://www.transit.ac.uk/ontologies/gtfs#>")

    yield proc

    # Teardown
    proc.terminate()


@pytest.fixture
def empty_datastore(rdfox_proc):
    """Clear datastore before every test."""
    yield
    run_cmd(rdfox_proc, f"clear facts force")


@pytest.fixture(scope="session")
def gtfs_onto():
    """Load GTFS ontology once."""
    return get_ontology(f"file://{GTFS_ONTOLOGY_RDF}").load()


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
def rdfox_query(rdfox_proc):
    """Run SPARQL queries."""
    def _query(q):
        return run_cmd(rdfox_proc, f'query "{q}"')
    return _query
