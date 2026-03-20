from gtfs_ontology.schedule.core import *

with gtfs:

    # region Classes

    class ExceptionTypeDatatypeDescription(DatatypeDescription):
        pass

    class ExceptionTypeDatatypeDescription1(ExceptionTypeDatatypeDescription):
        comment = "Service has been added for the specified date."

    class ExceptionTypeDatatypeDescription2(ExceptionTypeDatatypeDescription):
        comment = "Service has been removed for the specified date."

    # endregion

    # region Datatypes

    class ExceptionTypeDatatype(Datatype):
        equivalent_to = [
            OneOf(
                [
                     1,
                     2
                ]
            )
        ]

    # endregion

    # region Data Properties

    class date(FieldValue, FunctionalProperty):
        comment = "Date when service exception occurs."
        domain = [CalendarDate]
        range = [datetime.date]

    class exception_type(FieldValue, FunctionalProperty):
        comment = "Indicates whether service is available on the date specified in the date field."
        domain = [CalendarDate]
        range = [ExceptionTypeDatatype]

    # endregion