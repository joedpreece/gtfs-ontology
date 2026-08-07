import numpy as np

from gtfs_ontology import AGENCY_FILE, AGENCY_RML_FILE, AGENCY_KG_FILE
from gtfs_ontology.graphs import pull_tfwm_gtfs_data, build_agencies_graph, \
    materialize_graph

# pull_tfwm_gtfs_data()

materialize_graph(
    csv_file=AGENCY_FILE,
    rml_file=AGENCY_RML_FILE,
    output_file=AGENCY_KG_FILE,
    source_name="agency.txt",
    required_columns=[
        "agency_id",
        "agency_name",
        "agency_url",
        "agency_timezone",
        "agency_lang",
        "agency_phone",
        "agency_fare_url",
        "agency_email",
        "cemv_support"
    ]
)