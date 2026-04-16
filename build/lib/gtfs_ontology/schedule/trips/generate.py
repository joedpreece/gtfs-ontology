from gtfs_ontology.schedule import *
from gtfs_ontology.schedule.calendar.generate import service_id
from gtfs_ontology.schedule.field_types.generate import enumerated_datatype, text, id, \
    enum
from gtfs_ontology.schedule.records.generate import Trip
from gtfs_ontology.schedule.routes.generate import route_id
from gtfs_ontology.schedule.trips.definitions import *

TRIPS_URL = "https://gtfs.org/documentation/schedule/reference/#tripstxt"

with gtfs:

    # region Datatypes

    class DirectionIDDatatype(enumerated_datatype):
        equivalent_to = [
            OneOf(
                [
                     0,
                     1
                ]
            )
        ]

    class WheelchairAccessibleDatatype(enumerated_datatype):
        equivalent_to = [
            OneOf(
                [
                    0,
                    1,
                    2
                ]
            )
        ]

    class BikesAllowedDatatype(enumerated_datatype):
        equivalent_to = [
            OneOf(
                [
                    0,
                    1,
                    2
                ]
            )
        ]

    class CarsAllowedDatatype(enumerated_datatype):
        equivalent_to = [
            OneOf(
                [
                    0,
                    1,
                    2
                ]
            )
        ]

    # endregion


    # region Data Properties

    route_id.domain.append(Trip)
    route_id.comment.append(locstr(ROUTE_ID_DEF, "en"))
    route_id.seeAlso.append(TRIPS_URL)

    service_id.domain.append(Trip)
    service_id.comment.append(locstr(SERVICE_ID_DEF, "en"))
    service_id.seeAlso.append(TRIPS_URL)

    class trip_id(id):
        comment = [locstr(TRIP_ID_DEF, "en")]
        domain = [Trip]
        seeAlso = [TRIPS_URL]

    class trip_headsign(text):
        comment = [locstr(TRIP_HEADSIGN_DEF, "en")]
        domain = [Trip]
        seeAlso = [TRIPS_URL]

    class trip_short_name(text):
        comment = [locstr(TRIP_SHORT_NAME_DEF, "en")]
        domain = [Trip]
        seeAlso = [TRIPS_URL]

    class direction_id(enum):
        comment = [locstr(DIRECTION_ID_DEF, "en")]
        domain = [Trip]
        range = [DirectionIDDatatype]
        seeAlso = [TRIPS_URL]

    class block_id(id):
        comment = [locstr(BLOCK_ID_DEF, "en")]
        domain = [Trip]
        seeAlso = [TRIPS_URL]

    class shape_id(id):
        comment = [locstr(SHAPE_ID_DEF, "en")]
        domain = [Trip]
        seeAlso = [TRIPS_URL]

    class wheelchair_accessible(enum):
        comment = [locstr(WHEELCHAIR_ACCESSIBLE_DEF, "en")]
        domain = [Trip]
        range = [WheelchairAccessibleDatatype]
        seeAlso = [TRIPS_URL]

    class bikes_allowed(enum):
        comment = [locstr(BIKES_ALLOWED_DEF, "en")]
        domain = [Trip]
        range = [BikesAllowedDatatype]
        seeAlso = [TRIPS_URL]

    class cars_allowed(enum):
        comment = [locstr(CARS_ALLOWED_DEF, "en")]
        domain = [Trip]
        range = [CarsAllowedDatatype]
        seeAlso = [TRIPS_URL]

    # endregion