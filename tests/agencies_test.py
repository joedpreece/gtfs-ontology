import os
import subprocess
import tempfile
import time
import unittest
from pathlib import Path

import requests
from owlready2 import get_ontology

from config import GTFS_ONTOLOGY_NT, GTFS_ONTOLOGY_RDF, TEST_ONTOLOGY


def run_cmd(process, cmd, timeout=2):
    marker = f"__END__{time.time()}"
    full = f"{cmd}\necho {marker}\n"
    process.stdin.write(full)
    process.stdin.flush()

    # Read until we see the marker
    output = []
    start = time.time()
    while time.time() - start < timeout:
        line = process.stdout.readline()
        if not line:
            break
        if marker in line:
            break
        output.append(line)

    # Read stderr NON-BLOCKING
    # err = []
    # try:
    #     while True:
    #         line = process.stderr.readline()
    #         if not line:
    #             break
    #         err.append(line)
    # except:
    #     pass

    # # Optionally print stderr so you see errors during tests
    # if err:
    #     print("RDFOX STDERR:", "".join(err))

    return "".join(output)

class AgenciesTest(unittest.TestCase):

    DATASTORE_NAME = "transit"

    @classmethod
    def setUpClass(cls):
        cls.base = "http://localhost:12110"

        cls.process = subprocess.Popen(
            ["RDFox", "sandbox"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        run_cmd(
            cls.process,
            "set output out\n"
        )

        run_cmd(
            cls.process,
            "endpoint start\n"
        )

        run_cmd(
            cls.process,
            f"dstore create {cls.DATASTORE_NAME}"
        )

        run_cmd(
            cls.process,
            f"active {cls.DATASTORE_NAME}"
        )

        run_cmd(
            cls.process,
            f"prefix gtfs: <http://www.transit.ac.uk/ontologies/gtfs#>\n"
        )

        cls.gtfs = get_ontology(f"file://{str(GTFS_ONTOLOGY_RDF)}").load()

        # run_cmd(
        #     cls.process,
        #     f"import \"{GTFS_ONTOLOGY_NT}\""
        # )

    @classmethod
    def tearDownClass(cls):
        cls.process.terminate()
        try:
            cls.process.wait(timeout=3)
            print("Sandbox process terminated.")
        except subprocess.TimeoutExpired:
            cls.process.kill()
            print("Sandbox process killed.")

    def test_something(self):

        with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir = Path(tmpdir)
            tmp_path = tmpdir / "ontology.nt"

            with self.gtfs:

                self.gtfs.AgencyFile("TestFileSingleAgency")

                self.gtfs.Agency("Agency0")

                self.gtfs.save(file=tmp_path.as_posix(), format="ntriples")

            run_cmd(
                self.process,
                f"import \"{TEST_ONTOLOGY}\""
            )

            time.sleep(60)


if __name__ == '__main__':
    unittest.main()
