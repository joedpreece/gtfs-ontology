import time
import pytest
from config import RULES_STOPS
from conftest import run_cmd, create_triple, extract_boolean

# Module-scoped so we load the .dl only once per this file
@pytest.fixture(scope="module")
def stop_rules(rdfox_proc):

    run_cmd(rdfox_proc, f'import "{str(RULES_STOPS)}"')

    return True

def test_should_classify_as_multiple_when_file_has_two_agencies(
        clear_datastore,
        gtfs_onto,
        nt_writer,
        import_into_rdfox,
        rdfox_ask,
        agency_rules
):