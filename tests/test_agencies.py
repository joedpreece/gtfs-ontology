import time
import pytest
from conftest import run_cmd, create_triple, extract_boolean

RULES_AGENCIES = "/home/joe/Projects/research/transit/gtfs-ontology/artifacts/datalog/agencies.dl"

@pytest.fixture(scope="module")
def agency_rules(rdfox_proc):
    """
    Imports the datalog rules for validating agencies into RDFox.
    """

    run_cmd(rdfox_proc, f'import "{str(RULES_AGENCIES)}"')


def test_should_classify_as_multiple_when_file_has_two_agencies(
        clear_datastore,
        gtfs_onto,
        nt_writer,
        import_into_rdfox,
        rdfox_ask,
        agency_rules
):
    """
    Tests that an AgencyFile with two Agency instances is correctly classified as a AgencyFileWithMultipleAgencies.
    """

    with gtfs_onto:

        # Create an agency file.
        file = gtfs_onto.AgencyFile("TestFile")

        # Create an agency.
        agency1 = gtfs_onto.Agency("Agency1")
        create_triple(agency1, gtfs_onto.agency_id, "ID1")
        create_triple(agency1, gtfs_onto.agency_name, "Name 1")
        create_triple(agency1, gtfs_onto.agency_timezone, "Europe/London")
        create_triple(agency1, gtfs_onto.agency_url, "URL 1")

        # Create a second agency.
        agency2 = gtfs_onto.Agency("Agency2")
        create_triple(agency2, gtfs_onto.agency_id, "ID2")
        create_triple(agency2, gtfs_onto.agency_name, "Name 2")
        create_triple(agency2, gtfs_onto.agency_timezone, "Europe/London")
        create_triple(agency2, gtfs_onto.agency_url, "URL 2")

        # Add the agencies to the file.
        create_triple(file, gtfs_onto.hasAgency, agency1)
        create_triple(file, gtfs_onto.hasAgency, agency2)

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

def test_should_classify_as_single_when_file_has_one_agency(
        clear_datastore,
        gtfs_onto,
        nt_writer,
        import_into_rdfox,
        rdfox_ask,
        agency_rules
):
    """
    Tests that a file with one agency is correctly classified as having a single agency.
    """

    with gtfs_onto:
        # Create an agency file.
        file = gtfs_onto.AgencyFile("TestFile")

        # Create an agency.
        agency1 = gtfs_onto.Agency("Agency1")
        create_triple(agency1, gtfs_onto.agency_id, "ID1")
        create_triple(agency1, gtfs_onto.agency_name, "Name 1")
        create_triple(agency1, gtfs_onto.agency_timezone, "Europe/London")
        create_triple(agency1, gtfs_onto.agency_url, "URL 1")

        # Add the agencies to the file.
        create_triple(file, gtfs_onto.hasAgency, agency1)

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
        # Create an agency file.
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

def test_violate_when_agency_has_duplicate_id(
        clear_datastore,
        gtfs_onto,
        nt_writer,
        import_into_rdfox,
        rdfox_ask,
        agency_rules
):

    with gtfs_onto:

        # Create an agency file.
        file = gtfs_onto.AgencyFile("TestFile")

        # Create an agency.
        agency1 = gtfs_onto.Agency("Agency1")
        create_triple(agency1, gtfs_onto.agency_id, "ID")
        create_triple(agency1, gtfs_onto.agency_name, "Name 1")
        create_triple(agency1, gtfs_onto.agency_timezone, "Europe/London")
        create_triple(agency1, gtfs_onto.agency_url, "URL 1")

        # Create a different agency with the same ID.
        agency2 = gtfs_onto.Agency("Agency2")
        create_triple(agency2, gtfs_onto.agency_id, "ID")
        create_triple(agency2, gtfs_onto.agency_name, "Name 2")
        create_triple(agency2, gtfs_onto.agency_timezone, "Europe/London")
        create_triple(agency2, gtfs_onto.agency_url, "URL 2")

        # Add the agencies to the file.
        create_triple(file, gtfs_onto.hasAgency, agency1)
        create_triple(file, gtfs_onto.hasAgency, agency2)

        nt_path, _ = nt_writer(gtfs_onto)

    import_into_rdfox(nt_path)

    # Assert that Agency1 is flagged as a violation.
    assert extract_boolean(
        rdfox_ask(
            "{ gtfs:Agency1 rdf:type gtfs:Violation }"
        )
    ) is True

    # Assert that Agency2 is flagged as a violation.
    assert extract_boolean(
        rdfox_ask(
            "{ gtfs:Agency2 rdf:type gtfs:Violation }"
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
        # Create an agency file.
        file = gtfs_onto.AgencyFile("TestFile")

        # Create an agency with a missing name.
        agency1 = gtfs_onto.Agency("Agency1")
        create_triple(agency1, gtfs_onto.agency_id, "ID1")
        create_triple(agency1, gtfs_onto.agency_timezone, "Europe/London")
        create_triple(agency1, gtfs_onto.agency_url, "URL 1")

        # Create an agency with a missing timezone.
        agency2 = gtfs_onto.Agency("Agency2")
        create_triple(agency2, gtfs_onto.agency_id, "ID2")
        create_triple(agency2, gtfs_onto.agency_name, "Name 2")
        create_triple(agency2, gtfs_onto.agency_url, "URL 2")

        # Create an agency with a missing URL.
        agency3 = gtfs_onto.Agency("Agency3")
        create_triple(agency3, gtfs_onto.agency_id, "ID3")
        create_triple(agency3, gtfs_onto.agency_name, "Name 3")
        create_triple(agency3, gtfs_onto.agency_timezone, "Europe/London")

        # Create an agency with no missing fields.
        agency4 = gtfs_onto.Agency("Agency4")
        create_triple(agency4, gtfs_onto.agency_id, "ID4")
        create_triple(agency4, gtfs_onto.agency_name, "Name 4")
        create_triple(agency4, gtfs_onto.agency_timezone, "Europe/London")
        create_triple(agency4, gtfs_onto.agency_url, "URL 4")

        # Add the agencies to the file.
        create_triple(file, gtfs_onto.hasAgency, agency1)
        create_triple(file, gtfs_onto.hasAgency, agency2)
        create_triple(file, gtfs_onto.hasAgency, agency3)
        create_triple(file, gtfs_onto.hasAgency, agency4)

        nt_path, _ = nt_writer(gtfs_onto)

    import_into_rdfox(nt_path)

    assert extract_boolean(
        rdfox_ask(
            "{ gtfs:Agency1 rdf:type gtfs:Violation }"
        )
    ) is True

    assert extract_boolean(
        rdfox_ask(
            "{ gtfs:Agency2 rdf:type gtfs:Violation }"
        )
    ) is True

    assert extract_boolean(
        rdfox_ask(
            "{ gtfs:Agency3 rdf:type gtfs:Violation }"
        )
    ) is True

    assert extract_boolean(
        rdfox_ask(
            "{ gtfs:Agency4 rdf:type gtfs:Violation }"
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

        # Create an agency file.
        file = gtfs_onto.AgencyFile("TestFile")

        # Create an agency with a missing ID.
        agency1 = gtfs_onto.Agency("Agency1")
        create_triple(agency1, gtfs_onto.agency_name, "Name 1")
        create_triple(agency1, gtfs_onto.agency_timezone, "Europe/London")
        create_triple(agency1, gtfs_onto.agency_url, "URL 1")

        # Create a second agency.
        agency2 = gtfs_onto.Agency("Agency2")
        create_triple(agency2, gtfs_onto.agency_id, "ID")
        create_triple(agency2, gtfs_onto.agency_name, "Name 2")
        create_triple(agency2, gtfs_onto.agency_timezone, "Europe/London")
        create_triple(agency2, gtfs_onto.agency_url, "URL 2")

        # Add the agencies to the file.
        create_triple(file, gtfs_onto.hasAgency, agency1)
        create_triple(file, gtfs_onto.hasAgency, agency2)

        nt_path, _ = nt_writer(gtfs_onto)

    import_into_rdfox(nt_path)

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
    Ensure that cemv_support values (0/1/2) correctly map to cemv_supportDescription individuals via Datalog rules.
    """

    with gtfs_onto:

        # Create an agency file.
        file = gtfs_onto.AgencyFile("TestFile")

        # Create an agency with CEMVSupport of 0.
        agency1 = gtfs_onto.Agency("Agency1")
        create_triple(agency1, gtfs_onto.agency_id, "ID1")
        create_triple(agency1, gtfs_onto.agency_name, "Name 1")
        create_triple(agency1, gtfs_onto.agency_timezone, "Europe/London")
        create_triple(agency1, gtfs_onto.agency_url, "URL 1")
        create_triple(agency1, gtfs_onto.cemv_support, 0)

        # Create an agency with CEMVSupport of 1.
        agency2 = gtfs_onto.Agency("Agency2")
        create_triple(agency2, gtfs_onto.agency_id, "ID2")
        create_triple(agency2, gtfs_onto.agency_name, "Name 2")
        create_triple(agency2, gtfs_onto.agency_timezone, "Europe/London")
        create_triple(agency2, gtfs_onto.agency_url, "URL 2")
        create_triple(agency2, gtfs_onto.cemv_support, 1)

        # Create an agency with CEMVSupport of 2.
        agency3 = gtfs_onto.Agency("Agency3")
        create_triple(agency3, gtfs_onto.agency_id, "ID3")
        create_triple(agency3, gtfs_onto.agency_name, "Name 3")
        create_triple(agency3, gtfs_onto.agency_timezone, "Europe/London")
        create_triple(agency3, gtfs_onto.agency_url, "URL 3")
        create_triple(agency3, gtfs_onto.cemv_support, 2)

        # Add the agencies to the file.
        create_triple(file, gtfs_onto.hasAgency, agency1)
        create_triple(file, gtfs_onto.hasAgency, agency2)
        create_triple(file, gtfs_onto.hasAgency, agency3)

        nt_path, _ = nt_writer(gtfs_onto)
        import_into_rdfox(nt_path)

    # ---- Agency 0 ----
    assert extract_boolean(
        rdfox_ask(
            "{ gtfs:Agency1 gtfs:cemv_support_description gtfs:CEMVSupportDatatypeDescriptionAgency0 }"
        )
    ) is True

    # Should not match wrong descriptions
    assert extract_boolean(
        rdfox_ask(
            "{ gtfs:Agency1 gtfs:cemv_support_description gtfs:CEMVSupportDatatypeDescriptionAgency1 }"
        )
    ) is False

    assert extract_boolean(
        rdfox_ask(
            "{ gtfs:Agency1 gtfs:cemv_support_description gtfs:CEMVSupportDatatypeDescriptionAgency2 }"
        )
    ) is False

    # ---- Agency 1 ----
    assert extract_boolean(
        rdfox_ask(
            "{ gtfs:Agency2 gtfs:cemv_support_description gtfs:CEMVSupportDatatypeDescriptionAgency1 }"
        )
    ) is True

    assert extract_boolean(
        rdfox_ask(
            "{ gtfs:Agency2 gtfs:cemv_support_description gtfs:CEMVSupportDatatypeDescriptionAgency0 }"
        )
    ) is False

    assert extract_boolean(
        rdfox_ask(
            "{ gtfs:Agency2 gtfs:cemv_support_description gtfs:CEMVSupportDatatypeDescriptionAgency2 }"
        )
    ) is False

    # ---- Agency 2 ----
    assert extract_boolean(
        rdfox_ask(
            "{ gtfs:Agency3 gtfs:cemv_support_description gtfs:CEMVSupportDatatypeDescriptionAgency2 }"
        )
    ) is True

    assert extract_boolean(
        rdfox_ask(
            "{ gtfs:Agency3 gtfs:cemv_support_description gtfs:CEMVSupportDatatypeDescriptionAgency0 }"
        )
    ) is False

    assert extract_boolean(
        rdfox_ask(
            "{ gtfs:Agency3 gtfs:cemv_support_description gtfs:CEMVSupportDatatypeDescriptionAgency1 }"
        )
    ) is False


def test_cemv_support_data_validation(
    clear_datastore,
    gtfs_onto,
    nt_writer,
    import_into_rdfox,
    rdfox_ask,
    agency_rules
):
    """
    Ensure that cemv_support values (0/1/2) correctly map to cemv_supportDescription individuals via Datalog rules.
    """

    with gtfs_onto:

        # Create an agency file.
        file = gtfs_onto.AgencyFile("TestFile")

        # Create an agency with CEMVSupport of 3.
        agency1 = gtfs_onto.Agency("Agency1")
        create_triple(agency1, gtfs_onto.agency_id, "ID1")
        create_triple(agency1, gtfs_onto.agency_name, "Name 1")
        create_triple(agency1, gtfs_onto.agency_timezone, "Europe/London")
        create_triple(agency1, gtfs_onto.agency_url, "URL 1")
        create_triple(agency1, gtfs_onto.cemv_support, 3)

        # Add the agencies to the file.
        create_triple(file, gtfs_onto.hasAgency, agency1)

        nt_path, _ = nt_writer(gtfs_onto)
        import_into_rdfox(nt_path)

    # ---- Agency 0 ----
    assert extract_boolean(
        rdfox_ask(
            "{ gtfs:Agency1 rdf:type gtfs:Violation }"
        )
    ) is True

