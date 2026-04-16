from gtfs_ontology.schedule import *
from gtfs_ontology.schedule.agencies.generate import AgencyFileWithMultipleAgencies, \
    AgencyFileWithSingleAgency
from gtfs_ontology.schedule.core import hasRecord, hasFile
from gtfs_ontology.schedule.files.generate import AgencyFile, StopFile, RouteFile, \
    TripFile, StopTimeFile
from gtfs_ontology.schedule.records.generate import Agency, Stop
from gtfs_ontology.schedule.term_definitions.generate import DatasetFile

with gtfs:

    # 1i
    DatasetFile.is_a.append(
        hasFile.exactly(1, AgencyFile)
    )

    # 1ii
    AgencyFile.is_a.append(
        hasRecord.min(1, Agency)
    )

    # 1iii
    AgencyFileWithMultipleAgencies.equivalent_to.append(
        AgencyFile &
        hasRecord.min(2, Agency)
    )

    # 1iv
    AgencyFileWithSingleAgency.equivalent_to.append(
        AgencyFile &
        hasRecord.exactly(1, Agency)
    )

    # 2i
    DatasetFile.is_a.append(
        hasFile.exactly(1, StopFile)
    )

    # 2ii
    StopFile.is_a.append(
        hasRecord.min(1, Stop)
    )

    # TODO Continue creating DL rules.

    # DatasetFile.is_a.append(
    #     hasFile.exactly(1, AgencyFile) &
    #     hasFile.exactly(1, StopFile) &
    #     hasFile.exactly(1, RouteFile) &
    #     hasFile.exactly(1, TripFile) &
    #     hasFile.exactly(1, StopTimeFile) &
    #     hasFile.exactly(1, CalendarFile) &
    #     hasFile.exactly(1, CalendarDateFile)
    # )