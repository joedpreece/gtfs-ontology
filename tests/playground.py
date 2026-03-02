#%%
from owlready2 import get_ontology

from config import ONTOLOGY_FILE
from data_retriever import get_df_agencies
from utils import generate_identifier, create_individual_from_df_cell, create_triple

df_agencies = get_df_agencies()

gtfs = get_ontology(f"file://{ONTOLOGY_FILE}").load()

with gtfs:

    for index, row in df_agencies.iterrows():

        # Create an agency record.
        agency = gtfs.Agency(row["agency_id"])

        for column in row.index:

            value = row[column]

            if value is None:
                continue

            predicate = getattr(gtfs, f"{column}")

            # print(column)
            # print(agency, predicate, value)
            # print(column, type(predicate))

            create_triple(
                subject=agency,
                predicate=predicate,
                object=value,
            )

gtfs.save(file="./tests/tfwm_artifacts/gtfs_tfwm.nt", format="ntriples")