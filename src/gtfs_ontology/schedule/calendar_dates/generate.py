from gtfs_ontology.schedule import *
from gtfs_ontology.schedule.calendar.generate import service_id
from gtfs_ontology.schedule.calendar_dates.definitions import *
from gtfs_ontology.schedule.field_types.generate import date, enum
from gtfs_ontology.schedule.records.generate import Service

CALENDAR_DATES_URL = "https://gtfs.org/documentation/schedule/reference/#calendar_datestxt"

with gtfs:

    class exception_type_enum(Datatype):
        equivalent_to = [
            OneOf(
                [
                     1,
                     2
                ]
            )
        ]

    service_id.comment.append(locstr(SERVICE_ID, "en"))
    service_id.domain.append(Service)
    service_id.seeAlso.append(CALENDAR_DATES_URL)

    class calendar_dates_date(date):
        comment = [locstr(DATE_DEF, "en")]
        domain = [Service]
        seeAlso = [CALENDAR_DATES_URL]

    class exception_type(enum):
        comment = [locstr(EXCEPTION_TYPE_DEF, "en")]
        domain = [Service]
        range = [exception_type_enum]
        seeAlso = [CALENDAR_DATES_URL]

    # endregion