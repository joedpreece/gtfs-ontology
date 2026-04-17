from gtfs_ontology.schedule import *
from gtfs_ontology.schedule.term_definitions.generate import Dataset, DatasetFile, \
    Record

with gtfs:

#     class NonNegativeInteger(Datatype):
#         equivalent_to = [ConstrainedDatatype(
#             base_datatype=int,
#             min_inclusive=0
#         )]

#     class DatatypeDescription(Thing):
#         comment = "A description provided to compliment an enumerated datatype."


    class hasDataset(ObjectProperty):
        domain = [GTFSSchedule]
        range = [Dataset]

    class hasFile(ObjectProperty):
        domain = [Dataset]
        range = [DatasetFile]

    class hasRecord(ObjectProperty):
        domain = [DatasetFile]
        range = [Record]

    class isRecordOf(ObjectProperty):
        inverse_of = hasRecord