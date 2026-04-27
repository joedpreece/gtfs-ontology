from gtfs_ontology.schedule import *
from gtfs_ontology.schedule.term_definitions.generate import DatasetFile, Dataset
from gtfs_ontology.schedule.files.definitions import *

DATASET_FILES_URL = "https://gtfs.org/documentation/schedule/reference/#dataset-files"

with gtfs:

    class AgencyFile(DatasetFile):
        comment = [locstr(AGENCY_DEF, "en")]
        seeAlso = [DATASET_FILES_URL]

    class StopFile(DatasetFile):
        comment = [locstr(STOPS_DEF, "en")]
        seeAlso = [DATASET_FILES_URL]

    class RouteFile(DatasetFile):
        comment = [locstr(ROUTES_DEF, "en")]
        seeAlso = [DATASET_FILES_URL]

    class TripFile(DatasetFile):
        comment = [locstr(TRIPS_DEF, "en")]
        seeAlso = [DATASET_FILES_URL]

    class StopTimeFile(DatasetFile):
        comment = [locstr(STOP_TIMES_DEF, "en")]
        seeAlso = [DATASET_FILES_URL]

    class CalendarFile(DatasetFile):
        comment = [locstr(CALENDAR_DEF, "en")]
        seeAlso = [DATASET_FILES_URL]

    class CalendarDateFile(DatasetFile):
        comment = [locstr(CALENDAR_DATES_DEF, "en")]
        seeAlso = [DATASET_FILES_URL]

    AllDisjoint([AgencyFile, StopFile, RouteFile, TripFile, StopTimeFile, CalendarFile, CalendarDateFile])