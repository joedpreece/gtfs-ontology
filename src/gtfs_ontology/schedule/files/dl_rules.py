from gtfs_ontology.schedule import *
from gtfs_ontology.schedule.core import hasRecord, hasFile
from gtfs_ontology.schedule.files.definitions import AGENCY_FILE_WITH_SINGLE_AGENCY_DEF, \
    AGENCY_FILE_WITH_MULTIPLE_AGENCIES_DEF
from gtfs_ontology.schedule.files.generate import AgencyFile, StopFile, RouteFile, \
    TripFile, StopTimeFile, CalendarDateFile, CalendarFile
from gtfs_ontology.schedule.records.generate import Agency, Stop, Service, StopTime, \
    Trip, Route
from gtfs_ontology.schedule.term_definitions.generate import Dataset

with gtfs:

    # 1i
    Dataset.is_a.append(
        hasFile.exactly(1, AgencyFile) &
        hasFile.exactly(1, StopFile) &
        hasFile.exactly(1, RouteFile) &
        hasFile.exactly(1, TripFile) &
        hasFile.exactly(1, StopTimeFile) &
        hasFile.max(1, CalendarDateFile) &
        hasFile.max(1, CalendarFile)
    )

    # 1ii
    AgencyFile.is_a.append(
        hasRecord.min(1, Agency)
    )

    class AgencyFileWithSingleAgency(AgencyFile):
        comment = [locstr(AGENCY_FILE_WITH_SINGLE_AGENCY_DEF, "en")]#
        equivalent_to = [
            hasRecord.exactly(1, Agency)
        ]

    class AgencyFileWithMultipleAgencies(AgencyFile):
        comment = [locstr(AGENCY_FILE_WITH_MULTIPLE_AGENCIES_DEF, "en")]
        equivalent_to = [
            hasRecord.min(2, Agency)
        ]

    AllDisjoint([AgencyFileWithSingleAgency, AgencyFileWithMultipleAgencies])

    # 2ii
    StopFile.is_a.append(
        hasRecord.min(1, Stop)
    )

    # 3ii
    RouteFile.is_a.append(
        hasRecord.min(1, Route)
    )

    # 4ii
    TripFile.is_a.append(
        hasRecord.min(1, Trip)
    )

    # 5i
    Dataset.is_a.append(
        hasFile.exactly(1, StopTimeFile)
    )

    # 5ii
    StopTimeFile.is_a.append(
        hasRecord.min(1, StopTime)
    )

    # 6i
    CalendarFile.is_a.append(
        hasRecord.min(1, Service)
    )

    CalendarDateFile.is_a.append(
        hasRecord.min(1, Service)
    )

    class DatasetWithoutCalendarFile(Dataset):
        comment = [locstr("A dataset with a calendar file.", "en")]
        seeAlso = [CalendarFile]
        is_a = [
            hasFile.exactly(1, CalendarDateFile)
        ]
        equivalent_to = [
            hasFile.exactly(0, CalendarFile)
        ]