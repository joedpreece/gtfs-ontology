from gtfs_ontology.schedule import *
from gtfs_ontology.schedule.agencies.generate import AgencyFileWithMultipleAgencies, \
    AgencyFileWithSingleAgency
from gtfs_ontology.schedule.core import hasRecord, hasFile
from gtfs_ontology.schedule.files.generate import AgencyFile, StopFile, RouteFile, \
    TripFile, StopTimeFile, CalendarDateFile, CalendarFile, DatasetWithoutCalendarFile
from gtfs_ontology.schedule.records.generate import Agency, Stop, Service, StopTime, \
    Trip, Route
from gtfs_ontology.schedule.term_definitions.generate import Dataset

with gtfs:

    # 1i
    Dataset.is_a.append(
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
    Dataset.is_a.append(
        hasFile.exactly(1, StopFile)
    )

    # 2ii
    StopFile.is_a.append(
        hasRecord.min(1, Stop)
    )

    # 3i
    Dataset.is_a.append(
        hasFile.exactly(1, RouteFile)
    )

    # 3ii
    RouteFile.is_a.append(
        hasRecord.min(1, Route)
    )

    # 4i
    Dataset.is_a.append(
        hasFile.exactly(1, TripFile)
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

    # 6ii
    DatasetWithoutCalendarFile.equivalent_to.append(
        Dataset &
        hasFile.exactly(0, CalendarFile)
    )

    # 6iii
    Dataset.is_a.append(
        hasFile.max(1, CalendarFile)
    )

    # 7i
    DatasetWithoutCalendarFile.is_a.append(
        hasFile.exactly(1, CalendarDateFile)
    )

    # 7ii
    CalendarDateFile.is_a.append(
        hasRecord.min(1, Service)
    )

    # 7iii
    Dataset.is_a.append(
        hasFile.max(1, CalendarDateFile)
    )
