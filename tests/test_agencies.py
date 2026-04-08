import time
import pytest
from conftest import run_cmd, create_triple, extract_boolean

RULES_AGENCIES = "/home/joe/Projects/research/transit/gtfs-ontology/artifacts/datalog/agencies.dl"

# Module-scoped so we load the .dl only once per this file
@pytest.fixture(scope="module")
def agency_rules(rdfox_proc):

    run_cmd(rdfox_proc, f'import "{str(RULES_AGENCIES)}"')

    return True


def test_should_classify_as_multiple_when_file_has_two_agencies(
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

    time.sleep(60)

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

def test_should_classify_as_single_when_file_has_one_agency(
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

def test_should_flag_violation_when_file_has_no_agencies(
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

def test_should_flag_agency_as_violation_when_required_fields_missing(
        clear_datastore,
        gtfs_onto,
        nt_writer,
        import_into_rdfox,
        rdfox_ask,
        agency_rules
):

    with gtfs_onto:
        gtfs_onto.Agency("Agency1")

        nt_path, _ = nt_writer(gtfs_onto)

    import_into_rdfox(nt_path)

    assert extract_boolean(
        rdfox_ask(
            "{ gtfs:Agency1 rdf:type gtfs:Violation }"
        )
    ) is True

def test_should_not_flag_violation_when_agency_has_required_fields(
        clear_datastore,
        gtfs_onto,
        nt_writer,
        import_into_rdfox,
        rdfox_ask,
        agency_rules
):

    with gtfs_onto:
        a = gtfs_onto.Agency("Agency1")

        create_triple(a, gtfs_onto.agency_name, "Name 1")
        create_triple(a, gtfs_onto.agency_timezone, "Europe/London")
        create_triple(a, gtfs_onto.agency_url, "URL 1")

        nt_path, _ = nt_writer(gtfs_onto)

    import_into_rdfox(nt_path)

    assert extract_boolean(
        rdfox_ask(
            "{ gtfs:Agency1 rdf:type gtfs:Violation }"
        )
    ) is False

def test_should_flag_agency_missing_id_in_multi_agency_file(
        clear_datastore,
        gtfs_onto,
        nt_writer,
        import_into_rdfox,
        rdfox_ask,
        agency_rules
):

    with gtfs_onto:
        file = gtfs_onto.AgencyFile("TestFile")

        agency1 = gtfs_onto.Agency("Agency1")
        agency2 = gtfs_onto.Agency("Agency2")

        # create_triple(agency1, gtfs_onto.agency_id, "ID1")
        create_triple(agency1, gtfs_onto.agency_name, "Name 1")
        create_triple(agency1, gtfs_onto.agency_timezone, "Europe/London")
        create_triple(agency1, gtfs_onto.agency_url, "URL 1")

        create_triple(agency2, gtfs_onto.agency_id, "ID2")
        create_triple(agency2, gtfs_onto.agency_name, "Name 2")
        create_triple(agency2, gtfs_onto.agency_timezone, "Europe/London")
        create_triple(agency2, gtfs_onto.agency_url, "URL 2")

        create_triple(
            subject=file,
            predicate=gtfs_onto.hasAgency,
            object=agency1
        )

        create_triple(
            subject=file,
            predicate=gtfs_onto.hasAgency,
            object=agency2
        )

        nt_path, _ = nt_writer(gtfs_onto)

    import_into_rdfox(nt_path)

    time.sleep(60)

    assert extract_boolean(
        rdfox_ask(
            "{ gtfs:TestFile rdf:type gtfs:AgencyFileWithMultipleAgencies }"
        )
    ) is True

    assert extract_boolean(
        rdfox_ask(
            "{ gtfs:Agency1 rdf:type gtfs:Violation }"
        )
    ) is True

    assert extract_boolean(
        rdfox_ask(
            "{ gtfs:Agency2 rdf:type gtfs:Violation }"
        )
    ) is False


def test_cemv_support_description_mapping(
    clear_datastore,
    gtfs_onto,
    nt_writer,
    import_into_rdfox,
    rdfox_ask,
    agency_rules
):
    """
    Ensure that cemv_support values (0/1/2) correctly map
    to cemv_supportDescription individuals via Datalog rules.
    """

    with gtfs_onto:
        # --- Agency A: support = 0 ---
        a0 = gtfs_onto.Agency("Agency0")
        create_triple(a0, gtfs_onto.cemv_support, 0)

        # --- Agency B: support = 1 ---
        a1 = gtfs_onto.Agency("Agency1")
        create_triple(a1, gtfs_onto.cemv_support, 1)

        # --- Agency C: support = 2 ---
        a2 = gtfs_onto.Agency("Agency2")
        create_triple(a2, gtfs_onto.cemv_support, 2)

        nt_path, _ = nt_writer(gtfs_onto)
        import_into_rdfox(nt_path)

    time.sleep(60)

    # ---- Agency 0 ----
    assert extract_boolean(
        rdfox_ask(
            "{ gtfs:Agency0 gtfs:cemv_support_description gtfs:CEMVSupportTypeDescription0 }"
        )
    ) is True

    # Should not match wrong descriptions
    assert extract_boolean(
        rdfox_ask(
            "{ gtfs:Agency0 gtfs:cemv_support_description gtfs:CEMVSupportTypeDescription1 }"
        )
    ) is False

    assert extract_boolean(
        rdfox_ask(
            "{ gtfs:Agency0 gtfs:cemv_support_description gtfs:CEMVSupportTypeDescription2 }"
        )
    ) is False

    # ---- Agency 1 ----
    assert extract_boolean(
        rdfox_ask(
            "{ gtfs:Agency1 gtfs:cemv_support_description gtfs:CEMVSupportTypeDescription1 }"
        )
    ) is True

    assert extract_boolean(
        rdfox_ask(
            "{ gtfs:Agency1 gtfs:cemv_support_description gtfs:CEMVSupportTypeDescription0 }"
        )
    ) is False

    assert extract_boolean(
        rdfox_ask(
            "{ gtfs:Agency1 gtfs:cemv_support_description gtfs:CEMVSupportTypeDescription2 }"
        )
    ) is False

    # ---- Agency 2 ----
    assert extract_boolean(
        rdfox_ask(
            "{ gtfs:Agency2 gtfs:cemv_support_description gtfs:CEMVSupportTypeDescription2 }"
        )
    ) is True

    assert extract_boolean(
        rdfox_ask(
            "{ gtfs:Agency2 gtfs:cemv_support_description gtfs:CEMVSupportTypeDescription0 }"
        )
    ) is False

    assert extract_boolean(
        rdfox_ask(
            "{ gtfs:Agency2 gtfs:cemv_support_description gtfs:CEMVSupportTypeDescription1 }"
        )
    ) is False

