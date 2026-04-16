from gtfs_ontology.schedule import *

# with gtfs:
#
# # region Field type
#
#     class NonNegativeInteger(Datatype):
#         equivalent_to = [ConstrainedDatatype(
#             base_datatype=int,
#             min_inclusive=0
#         )]
#
# # endregion
#
# # region Additional classes
#
#     class DatatypeDescription(Thing):
#         comment = "A description provided to compliment an enumerated datatype."
#
# # endregion
#
# # region Additional object properties
#
#     class hasDataset(ObjectProperty):
#         domain = [GTFSSchedule]
#         range = [Dataset]
#
#     class hasAgency(ObjectProperty):
#         domain = [AgencyFile]
#         range = [Agency]
#
#     class hasFile(ObjectProperty):
#         domain = [Dataset]
#         range = [DatasetFile]
#
# # endregion