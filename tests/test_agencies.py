import time
from pathlib import Path
import pytest

from config import RULES_AGENCIES
from conftest import run_cmd, create_triple, extract_boolean


# Module-scoped so we load the .dl only once per this file
@pytest.fixture(scope="module")
def agency_rules(rdfox_proc):

    run_cmd(rdfox_proc, f'import "{str(RULES_AGENCIES)}"')

    return True

def test_agency_file_with_multiple_agencies(
        clear_datastore,
        gtfs_onto,
        nt_writer,
        import_into_rdfox,
        rdfox_ask,
        agency_rules
):

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

        nt_path, _ = nt_writer(gtfs_onto)

    import_into_rdfox(nt_path)

    assert extract_boolean(
        rdfox_ask(
            "{ gtfs:TestFile rdf:type gtfs:AgencyFileWithMultipleAgencies }"
        )
    ) is True

    assert extract_boolean(
        rdfox_ask(
            "{ gtfs:TestFile rdf:type gtfs:AgencyFileWithSingleAgency }"
        )
    ) is False

    assert extract_boolean(
        rdfox_ask(
            "{ gtfs:TestFile rdf:type gtfs:Violation }"
        )
    ) is False

def test_agency_file_with_single_agency(
        clear_datastore,
        gtfs_onto,
        nt_writer,
        import_into_rdfox,
        rdfox_ask,
        agency_rules
):

    with gtfs_onto:
        file = gtfs_onto.AgencyFile("TestFile")
        agency0 = gtfs_onto.Agency("Agency0")

        create_triple(
            subject=file,
            predicate=gtfs_onto.hasAgency,
            object=agency0
        )

        nt_path, _ = nt_writer(gtfs_onto)

    import_into_rdfox(nt_path)

    assert extract_boolean(
        rdfox_ask(
            "{ gtfs:TestFile rdf:type gtfs:AgencyFileWithMultipleAgencies }"
        )
    ) is False

    assert extract_boolean(
        rdfox_ask(
            "{ gtfs:TestFile rdf:type gtfs:AgencyFileWithSingleAgency }"
        )
    ) is True

    assert extract_boolean(
        rdfox_ask(
            "{ gtfs:TestFile rdf:type gtfs:Violation }"
        )
    ) is False

def test_agency_file_with_no_agenies(
        clear_datastore,
        gtfs_onto,
        nt_writer,
        import_into_rdfox,
        rdfox_ask,
        agency_rules
):

    with gtfs_onto:
        file = gtfs_onto.AgencyFile("TestFile")

        nt_path, _ = nt_writer(gtfs_onto)

    import_into_rdfox(nt_path)

    assert extract_boolean(
        rdfox_ask(
            "{ gtfs:TestFile rdf:type gtfs:AgencyFileWithMultipleAgencies }"
        )
    ) is False

    assert extract_boolean(
        rdfox_ask(
            "{ gtfs:TestFile rdf:type gtfs:AgencyFileWithSingleAgency }"
        )
    ) is False

    assert extract_boolean(
        rdfox_ask(
            "{ gtfs:TestFile rdf:type gtfs:Violation }"
        )
    ) is True