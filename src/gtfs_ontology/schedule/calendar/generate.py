from gtfs_ontology.schedule import *
from gtfs_ontology.schedule.calendar.definitions import *
from gtfs_ontology.schedule.field_types.generate import enum, id, date
from gtfs_ontology.schedule.records.generate import Service

CALENDAR_URL = "https://gtfs.org/documentation/schedule/reference/#calendartxt"

with gtfs:

    # region Datatypes

    class weekday_enum(Datatype):
        equivalent_to = [
            OneOf(
                [
                     0,
                     1
                ]
            )
        ]

    # endregion

    # region Data Properties

    class service_id(id):
        comment = [locstr(SERVICE_ID_DEF, "en")]
        domain = [Service | Trip]
        seeAlso = [CALENDAR_URL]

    class monday(enum):
        comment = [locstr(MONDAY_DEF, "en")]
        domain = [Service]
        range = [weekday_enum]
        seeAlso = [CALENDAR_URL]
        closeMatch = [gtfs_linked.monday]

    class tuesday(enum):
        comment = [locstr(TUESDAY_DEF, "en")]
        domain = [Service]
        range = [weekday_enum]
        seeAlso = [CALENDAR_URL]
        closeMatch = [gtfs_linked.tuesday]

    class wednesday(enum):
        comment = [locstr(WEDNESDAY_DEF, "en")]
        domain = [Service]
        range = [weekday_enum]
        seeAlso = [CALENDAR_URL]
        closeMatch = [gtfs_linked.wednesday]

    class thursday(enum):
        comment = [locstr(THURSDAY_DEF, "en")]
        domain = [Service]
        range = [weekday_enum]
        seeAlso = [CALENDAR_URL]
        closeMatch = [gtfs_linked.thursday]

    class friday(enum):
        comment = [locstr(FRIDAY_DEF, "en")]
        domain = [Service]
        range = [weekday_enum]
        seeAlso = [CALENDAR_URL]
        closeMatch = [gtfs_linked.friday]

    class saturday(enum):
        comment = [locstr(SATURDAY_DEF, "en")]
        domain = [Service]
        range = [weekday_enum]
        seeAlso = [CALENDAR_URL]
        closeMatch = [gtfs_linked.saturday]

    class sunday(enum):
        comment = [locstr(SUNDAY_DEF, "en")]
        domain = [Service]
        range = [weekday_enum]
        seeAlso = [CALENDAR_URL]
        closeMatch = [gtfs_linked.sunday]

    class start_date(date):
        comment = [locstr(START_DATE_DEF, "en")]
        domain = [Service]
        seeAlso = [CALENDAR_URL]

    class end_date(date):
        comment = [locstr(END_DATE_DEF, "en")]
        domain = [Service]
        seeAlso = [CALENDAR_URL]

    # endregion