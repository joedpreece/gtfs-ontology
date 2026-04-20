import time
import pytest
from conftest import run_cmd, create_triple, extract_boolean

RULES_AGENCIES = "../artifacts/datalog/dataset_files.dl"

@pytest.fixture(scope="module")
def dataset_rules(rdfox_proc):
    """
    Imports the datalog rules for validating agencies into RDFox.
    """

    run_cmd(rdfox_proc, f'import "{str(RULES_AGENCIES)}"')


def test_rule_1(
        clear_datastore,
        gtfs_onto,
        nt_writer,
        import_into_rdfox,
        rdfox_ask,
        dataset_rules
):

    with gtfs_onto:

        # Create a dataset.

        dataset1 = gtfs_onto.Dataset("TestDataset1")
        dataset2 = gtfs_onto.Dataset("TestDataset2")

        # Create an agency file.
        file = gtfs_onto.AgencyFile("TestFile")

        # Add the agencies to the file.
        create_triple(dataset1, gtfs_onto.hasFile, file)

        nt_path, _ = nt_writer(gtfs_onto)

        import_into_rdfox(nt_path)

    time.sleep(60)

    assert extract_boolean(
        rdfox_ask(
            "{ gtfs:TestDataset1 rdf:type gtfs:Violation }"
        )
    ) is False

    # assert extract_boolean(
    #     rdfox_ask(
    #         "{ gtfs:TestDataset2 rdf:type gtfs:Violation }"
    #     )
    # ) is True