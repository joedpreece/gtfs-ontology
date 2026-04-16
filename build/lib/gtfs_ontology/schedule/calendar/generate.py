from gtfs_ontology.schedule import *
from gtfs_ontology.schedule.calendar.definitions import *
from gtfs_ontology.schedule.field_types.generate import enum, id, date, \
    enumerated_datatype
from gtfs_ontology.schedule.records.generate import CalendarDate, Calendar

CALENDAR_URL = "https://gtfs.org/documentation/schedule/reference/#calendartxt"

with gtfs:

    # region Classes

    # class CalendarDatatypeDescription(DatatypeDescription):
    #     pass
    #
    # class CalendarDatatypeDescription0(CalendarDatatypeDescription):
    #     comment = "Service is available for all Mondays in the date range."
    #
    # class CalendarDatatypeDescription1(CalendarDatatypeDescription):
    #     comment = "Service is not available for Mondays in the date range."

    # endregion

    # region Datatypes

    class CalendarDatatype(enumerated_datatype):
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
        domain = [Calendar]
        seeAlso = [CALENDAR_URL]

    class monday(enum):
        comment = [locstr(MONDAY_DEF, "en")]
        domain = [Calendar]
        range = [CalendarDatatype]
        seeAlso = [CALENDAR_URL]

    class tuesday(enum):
        comment = [locstr(TUESDAY_DEF, "en")]
        domain = [Calendar]
        range = [CalendarDatatype]
        seeAlso = [CALENDAR_URL]

    class wednesday(enum):
        comment = [locstr(WEDNESDAY_DEF, "en")]
        domain = [Calendar]
        range = [CalendarDatatype]
        seeAlso = [CALENDAR_URL]

    class thursday(enum):
        comment = [locstr(THURSDAY_DEF, "en")]
        domain = [Calendar]
        range = [CalendarDatatype]
        seeAlso = [CALENDAR_URL]

    class friday(enum):
        comment = [locstr(FRIDAY_DEF, "en")]
        domain = [Calendar]
        range = [CalendarDatatype]
        seeAlso = [CALENDAR_URL]

    class saturday(enum):
        comment = [locstr(SATURDAY_DEF, "en")]
        domain = [Calendar]
        range = [CalendarDatatype]
        seeAlso = [CALENDAR_URL]

    class sunday(enum):
        comment = [locstr(SUNDAY_DEF, "en")]
        domain = [Calendar]
        range = [CalendarDatatype]
        seeAlso = [CALENDAR_URL]

    class start_date(date):
        comment = [locstr(START_DATE_DEF, "en")]
        domain = [Calendar]
        seeAlso = [CALENDAR_URL]

    class end_date(date):
        comment = [locstr(END_DATE_DEF, "en")]
        domain = [Calendar]
        seeAlso = [CALENDAR_URL]

    # endregion