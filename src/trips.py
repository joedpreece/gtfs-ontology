from core import *
from routes import route_id

# region Definitions

ROUTE_ID_DEF = """
Identifies a route.
"""

SERVICE_ID_DEF = """
Identifies a set of dates when service is available for one or more routes.
"""

TRIP_ID_DEF = """
Identifies a trip.
"""

TRIP_HEADSIGN_DEF = """
Text that appears on signage identifying the trip's destination to riders. This field is recommended for all services with headsign text displayed on the vehicle which may be used to distinguish amongst trips in a route.

If the headsign changes during a trip, values for trip_headsign may be overridden by defining values in stop_times.stop_headsign for specific stop_times along the trip.
"""

TRIP_SHORT_NAME_DEF = """
Public facing text used to identify the trip to riders, for instance, to identify train numbers for commuter rail trips. If riders do not commonly rely on trip names, trip_short_name should be empty. A trip_short_name value, if provided, should uniquely identify a trip within a service day; it should not be used for destination names or limited/express designations.
"""

DIRECTION_ID_DEF = """
Indicates the direction of travel for a trip. This field should not be used in routing; it provides a way to separate trips by direction when publishing time tables. Valid options are:

0 - Travel in one direction (e.g. outbound travel).
1 - Travel in the opposite direction (e.g. inbound travel).
"""

BLOCK_ID_DEF = """
Identifies the block to which the trip belongs. A block consists of a single trip or many sequential trips made using the same vehicle, defined by shared service days and block_id. A block_id may have trips with different service days, making distinct blocks. See the example below. To provide in-seat transfers information, transfers of transfer_type 4 should be provided instead.
"""

SHAPE_ID_DEF = """
Identifies a geospatial shape describing the vehicle travel path for a trip.

Conditionally Required:
- Required if the trip has a continuous pickup or drop-off behavior defined either in routes.txt or in stop_times.txt.
- Optional otherwise.
"""

WHEELCHAIR_ACCESSIBLE_DEF = """
Indicates wheelchair accessibility. Valid options are:

0 or empty - No accessibility information for the trip.
1 - Vehicle being used on this particular trip can accommodate at least one rider in a wheelchair.
2 - No riders in wheelchairs can be accommodated on this trip.
"""

BIKES_ALLOWED_DEF = """
Indicates whether bikes are allowed. Valid options are:

0 or empty - No bike information for the trip.
1 - Vehicle being used on this particular trip can accommodate at least one bicycle.
2 - No bicycles are allowed on this trip.
"""

CARS_ALLOWED_DEF = """
Indicates whether cars are allowed. Valid options are:

0 or empty - No car information for the trip.
1 - Vehicle being used on this particular trip can accommodate at least one car.
2 - No cars are allowed on this trip.
"""

# endregion

with gtfs:

    # region Classes

    class DirectionIDDatatypeDescription(DatatypeDescription):
        pass

    class DirectionIDDatatypeDescription0(DirectionIDDatatypeDescription):
        comment = "Travel in one direction (e.g. outbound travel)."

    class DirectionIDDatatypeDescription1(DirectionIDDatatypeDescription):
        comment = "Travel in the opposite direction (e.g. inbound travel)."

    class WheelchairAccessibleDatatypeDescription(DatatypeDescription):
        pass

    class WheelchairAccessibleDatatypeDescription0(WheelchairAccessibleDatatypeDescription):
        comment = "No accessibility information for the trip."

    class WheelchairAccessibleDatatypeDescription1(WheelchairAccessibleDatatypeDescription):
        comment = "Vehicle being used on this particular trip can accommodate at least one rider in a wheelchair."

    class WheelchairAccessibleDatatypeDescription2(WheelchairAccessibleDatatypeDescription):
        comment = "No riders in wheelchairs can be accommodated on this trip."

    class BikesAllowedDatatypeDescription(DatatypeDescription):
        pass

    class BikesAllowedDatatypeDescription0(BikesAllowedDatatypeDescription):
        comment = "No bike information for the trip."

    class BikesAllowedDatatypeDescription1(BikesAllowedDatatypeDescription):
        comment = "Vehicle being used on this particular trip can accommodate at least one bicycle."

    class BikesAllowedDatatypeDescription2(BikesAllowedDatatypeDescription):
        comment = "No bicycles can be accommodated on this trip."

    class CarsAllowedDatatypeDescription(DatatypeDescription):
        pass

    class CarsAllowedDatatypeDescription0(CarsAllowedDatatypeDescription):
        comment = "No car information for the trip."

    class CarsAllowedDatatypeDescription1(CarsAllowedDatatypeDescription):
        comment = "Vehicle being used on this particular trip can accommodate at least one car."

    class CarsAllowedDatatypeDescription2(CarsAllowedDatatypeDescription):
        comment = "No cars are allowed on this trip."

    # endregion

    # region Datatypes

    class DirectionIDDatatype(Datatype):
        equivalent_to = [
            OneOf(
                [
                     0,
                     1
                ]
            )
        ]

    class WheelchairAccessibleDatatype(Datatype):
        equivalent_to = [
            OneOf(
                [
                    0,
                    1,
                    2
                ]
            )
        ]

    class BikesAllowedDatatype(Datatype):
        equivalent_to = [
            OneOf(
                [
                    0,
                    1,
                    2
                ]
            )
        ]

    class CarsAllowedDatatype(Datatype):
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

    class service_id(FieldValue, FunctionalProperty):
        comment = [locstr(SERVICE_ID_DEF, "en")]
        domain = [Trip]
        range = [str]

    class trip_id(FieldValue, FunctionalProperty):
        comment = [locstr(TRIP_ID_DEF, "en")]
        domain = [Trip]
        range = [str]

    class trip_headsign(FieldValue, FunctionalProperty):
        comment = [locstr(TRIP_HEADSIGN_DEF, "en")]
        domain = [Trip]
        range = [str]

    class trip_short_name(FieldValue, FunctionalProperty):
        comment = [locstr(TRIP_SHORT_NAME_DEF, "en")]
        domain = [Trip]
        range = [str]

    class direction_id(FieldValue, FunctionalProperty):
        comment = [locstr(DIRECTION_ID_DEF, "en")]
        domain = [Trip]
        range = [DirectionIDDatatype]

    class block_id(FieldValue, FunctionalProperty):
        comment = [locstr(BLOCK_ID_DEF, "en")]
        domain = [Trip]
        range = [str]

    class shape_id(FieldValue, FunctionalProperty):
        comment = [locstr(SHAPE_ID_DEF, "en")]
        domain = [Trip]
        range = [str]

    class wheelchair_accessible(FieldValue, FunctionalProperty):
        comment = [locstr(WHEELCHAIR_ACCESSIBLE_DEF, "en")]
        domain = [Trip]
        range = [WheelchairAccessibleDatatype]

    class bikes_allowed(FieldValue, FunctionalProperty):
        comment = [locstr(BIKES_ALLOWED_DEF, "en")]
        domain = [Trip]
        range = [BikesAllowedDatatype]

    class cars_allowed(FieldValue, FunctionalProperty):
        comment = [locstr(CARS_ALLOWED_DEF, "en")]
        domain = [Trip]
        range = [CarsAllowedDatatype]

    # endregion