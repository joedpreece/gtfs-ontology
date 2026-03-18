from core import *

with gtfs:

    # region Classes

    class CalendarDatatypeDescription(DatatypeDescription):
        pass

    class CalendarDatatypeDescription0(CalendarDatatypeDescription):
        comment = "Service is available for all Mondays in the date range."

    class CalendarDatatypeDescription1(CalendarDatatypeDescription):
        comment = "Service is not available for Mondays in the date range."

    # endregion

    # region Datatypes

    class CalendarDatatype(Datatype):
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

    class service_id(FieldValue, FunctionalProperty):
        comment = "Identifies a set of dates when service is available for one or more routes."
        domain = [CalendarDate, Calendar, Trip]
        range = [str]

    class monday(FieldValue, FunctionalProperty):
        comment = "Indicates whether the service operates on all Mondays in the date range specified by the start_date and end_date fields."
        domain = [Calendar]
        range = [CalendarDatatype]

    class tuesday(FieldValue, FunctionalProperty):
        comment = "Indicates whether the service operates on all Tuesdays in the date range specified by the start_date and end_date fields."
        domain = [Calendar]
        range = [CalendarDatatype]

    class wednesday(FieldValue, FunctionalProperty):
        comment = "Indicates whether the service operates on all Wednesdays in the date range specified by the start_date and end_date fields."
        domain = [Calendar]
        range = [CalendarDatatype]

    class thursday(FieldValue, FunctionalProperty):
        comment = "Indicates whether the service operates on all Thursdays in the date range specified by the start_date and end_date fields."
        domain = [Calendar]
        range = [CalendarDatatype]

    class friday(FieldValue, FunctionalProperty):
        comment = "Indicates whether the service operates on all Fridays in the date range specified by the start_date and end_date fields."
        domain = [Calendar]
        range = [CalendarDatatype]

    class saturday(FieldValue, FunctionalProperty):
        comment = "Indicates whether the service operates on all Saturdays in the date range specified by the start_date and end_date fields."
        domain = [Calendar]
        range = [CalendarDatatype]

    class sunday(FieldValue, FunctionalProperty):
        comment = "Indicates whether the service operates on all Sundays in the date range specified by the start_date and end_date fields."
        domain = [Calendar]
        range = [CalendarDatatype]

    class start_date(FieldValue, FunctionalProperty):
        comment = "Start service day for the service interval."
        domain = [Calendar]
        range = [datetime.date]

    class end_date(FieldValue, FunctionalProperty):
        comment = "End service day for the service interval. This service day is included in the interval."
        domain = [Calendar]
        range = [datetime.date]


    # endregion