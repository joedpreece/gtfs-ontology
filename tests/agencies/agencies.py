# #%%
# from owlready2 import get_ontology
#
# from config import ONTOLOGY_FILE
#
# gtfs = get_ontology(f"file://{ONTOLOGY_FILE}").load()
#
# with gtfs:
#
#     agency_file = gtfs.AgencyFile("Test File Single Agency")
#
#     agency = gtfs.Agency("Agency 0")
#
#     for index, row in df_agencies.iterrows():
#
#         # Create an agency record.
#         agency = gtfs.Agency(row["agency_id"])
#
#         create_triple(
#             subject=agency_file,
#             predicate=gtfs.hasAgency,
#             object=agency,
#         )
#
#         for column in row.index:
#
#             value = row[column]
#
#             if value is None:
#                 continue
#
#             predicate = getattr(gtfs, f"{column}")
#
#             # print(column)
#             # print(agency, predicate, value)
#             # print(column, type(predicate))
#
#             create_triple(
#                 subject=agency,
#                 predicate=predicate,
#                 object=value,
#             )
#
# gtfs.save(file=OUTPUT_ONTOLOGY, format="ntriples")