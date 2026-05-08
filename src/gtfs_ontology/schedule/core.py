from gtfs_ontology.schedule import *
from gtfs_ontology.schedule.term_definitions.generate import Dataset, DatasetFile, \
    Record

with gtfs:

    class hasDataset(ObjectProperty):
        domain = [GTFSSchedule]
        range = [Dataset]

    class hasFile(ObjectProperty):
        domain = [Dataset]
        range = [DatasetFile]

    class isFileOf(ObjectProperty):
        inverse_property = hasFile

    class hasRecord(ObjectProperty):
        domain = [DatasetFile]
        range = [Record]

    class isRecordOf(ObjectProperty):
        inverse_property = hasRecord

    class Requirement(Thing):
        pass

    class Recommendation(Thing):
        pass

    class Optional(Thing):
        pass

    AllDisjoint([
        hasDataset,
        hasFile,
        hasRecord,
    ])