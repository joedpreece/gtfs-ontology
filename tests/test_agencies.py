import time
from pathlib import Path
import pytest

from config import RULES_AGENCIES
from conftest import run_cmd, create_triple


# Module-scoped so we load the .dl only once per this file
@pytest.fixture(scope="module")
def agency_rules(rdfox_proc):

    run_cmd(rdfox_proc, f'import "{str(RULES_AGENCIES)}"')

    return True

def test_agency_file_with_multiple_agencies(empty_datastore, gtfs_onto, nt_writer, import_into_rdfox, rdfox_query, agency_rules):

    with gtfs_onto:
        file = gtfs_onto.AgencyFile("TestFile")
        agency0 = gtfs_onto.Agency("Agency0")
        agency1 = gtfs_onto.Agency("Agency1")

        create_triple(
            subject=file,
            predicate=gtfs_onto.hasAgency,
            object=agency0
        )

        create_triple(
            subject=file,
            predicate=gtfs_onto.hasAgency,
            object=agency1
        )

        rdfox_query("ASK WHERE { gtfs:TestFile rdf:type gtfs:AgencyAgencyFileWithMultipleAgencies . }")

        print(rdfox_query)

def test_single_agency(empty_datastore, gtfs_onto, nt_writer, import_into_rdfox, rdfox_query, agency_rules):

    with gtfs_onto:
        file = gtfs_onto.AgencyFile("TestFile")
        agency = gtfs_onto.Agency("Agency0")

        create_triple(
            subject=file,
            predicate=gtfs_onto.hasAgency,
            object=agency
        )

    nt_path, _ = nt_writer(gtfs_onto)

    import_into_rdfox(nt_path)

    time.sleep(60)

    # result = rdfox_query("ASK WHERE { ?a a gtfs:Agency }")
    #
    # assert "true" in result.lower()