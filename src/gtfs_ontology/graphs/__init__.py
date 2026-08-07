from zipfile import ZipFile

import morph_kgc
import numpy as np
import pandas as pd
import requests
from dotenv import load_dotenv
import os

from gtfs_ontology import AGENCY_RML_FILE, DATA_DIR, AGENCY_FILE, GTFS, AGENCY_KG_FILE


def pull_tfwm_gtfs_data():
    load_dotenv()
    url = "http://api.tfwm.org.uk/gtfs/tfwm_gtfs.zip"

    app_id = os.getenv("TFWM_APP_ID")
    app_key = os.getenv("TFWM_APP_KEY")

    r = requests.get(
        url,
        params={
            "app_id": app_id,
            "app_key": app_key
        }
    )

    zip_path = DATA_DIR / "tfwm_gtfs.zip"
    zip_path.write_bytes(r.content)

    # with open(zip_path, "wb") as f:
    #     f.write(r.content)

    with ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(DATA_DIR)

def materialize_graph(
    csv_file,
    rml_file,
    output_file,
    required_columns,
    source_name,
):
    config = f"""
    [DataSource]
    mappings={rml_file}
    """

    df = pd.read_csv(csv_file)

    for col in required_columns:
        if col not in df.columns:
            df[col] = np.nan

    graph = morph_kgc.materialize(
        config,
        {source_name: df}
    )

    graph.bind("", GTFS)
    graph.serialize(destination=output_file, format="turtle")

def build_agencies_graph():

    config = f"""
    [DataSource]
    mappings={AGENCY_RML_FILE}
    """

    df = pd.read_csv(AGENCY_FILE)

    AGENCY_COLUMNS = {
        "agency_id": np.nan,
        "agency_name": np.nan,
        "agency_url": np.nan,
        "agency_timezone": np.nan,
        "agency_lang": np.nan,
        "agency_phone": np.nan,
        "agency_fare_url": np.nan,
        "agency_email": np.nan,
        "cemv_support": np.nan,
    }

    for col, default in AGENCY_COLUMNS.items():
        if col not in df.columns:
            df[col] = default

    data_dict = {
        "agency.txt": df,
    }

    graph = morph_kgc.materialize(config, data_dict)

    graph.bind("", GTFS)

    graph.serialize(destination=AGENCY_KG_FILE, format="turtle")

def build_agencies_graph():

    config = f"""
    [DataSource]
    mappings={AGENCY_RML_FILE}
    """

    df = pd.read_csv(AGENCY_FILE)

    AGENCY_COLUMNS = {
        "agency_id": np.nan,
        "agency_name": np.nan,
        "agency_url": np.nan,
        "agency_timezone": np.nan,
        "agency_lang": np.nan,
        "agency_phone": np.nan,
        "agency_fare_url": np.nan,
        "agency_email": np.nan,
        "cemv_support": np.nan,
    }

    for col, default in AGENCY_COLUMNS.items():
        if col not in df.columns:
            df[col] = default

    data_dict = {
        "agency.txt": df,
    }

    graph = morph_kgc.materialize(config, data_dict)

    graph.bind("", GTFS)

    graph.serialize(destination=AGENCY_KG_FILE, format="turtle")