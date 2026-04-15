from gtfs_ontology.schedule.core import *
from gtfs_ontology.schedule.stop_times.definitions import *
from gtfs_ontology.schedule.stops.generate import stop_id
from gtfs_ontology.schedule.trips.generate import trip_id

STOP_TIMES_URL = "https://gtfs.org/documentation/schedule/reference/#stoptxt"

with gtfs:

    # region Classes

    class PickupTypeDatatypeDescription(DatatypeDescription):
        pass

    class PickupTypeDatatypeDescription0(PickupTypeDatatypeDescription):
        comment = [locstr("Regularly scheduled pickup.", "en")]

    class PickupTypeDatatypeDescription1(PickupTypeDatatypeDescription):
        comment = [locstr("No pickup available.", "en")]

    class PickupTypeDatatypeDescription2(PickupTypeDatatypeDescription):
        comment = [locstr("Must phone agency to arrange pickup.", "en")]

    class PickupTypeDatatypeDescription3(PickupTypeDatatypeDescription):
        comment = [locstr("Must coordinate with driver to arrange pickup.", "en")]

    # endregion

    # region Datatypes

    class PickupTypeDatatype(Datatype):
        equivalent_to = [
            OneOf(
                [
                      0,
                      1,
                      2,
                      3
                ]
            )
        ]

    class DropOffTypeDatatype(Datatype):
        equivalent_to = [
            OneOf(
                [
                      0,
                      1,
                      2,
                      3
                ]
            )
        ]

    class ContinuousPickupDatatype(Datatype):
        equivalent_to = [
            OneOf(
                [
                      0,
                      1,
                      2,
                      3
                ]
            )
        ]

    class ContinuousDropOffDatatype(Datatype):
        equivalent_to = [
            OneOf(
                [
                      0,
                      1,
                      2,
                      3
                ]
            )
        ]

    class TimepointDatatype(Datatype):
        equivalent_to = [
            OneOf(
                [
                      0,
                      1,
                ]
            )
        ]

    # endregion

    # region Data Properties

    trip_id.comment.append(locstr(TRIP_ID_DEF, "en"))
    trip_id.domain.append(StopTime)
    trip_id.seeAlso.append(STOP_TIMES_URL)

    class arrival_time(time):
        comment = [locstr(ARRIVAL_TIME_DEF, "en")]
        domain = [StopTime]
        seeAlso = [STOP_TIMES_URL]

    class departure_time(time):
        comment = [locstr(DEPARTURE_TIME_DEF, "en")]
        domain = [StopTime]
        seeAlso = [STOP_TIMES_URL]

    stop_id.comment.append(locstr(STOP_ID_DEF, "en"))
    stop_id.domain.append(StopTime)
    stop_id.seeAlso.append(STOP_TIMES_URL)

    class location_group_id(id):
        comment = [locstr(LOCATION_GROUP_ID_DEF, "en")]
        domain = [StopTime]
        seeAlso = [STOP_TIMES_URL]

    class location_id(FieldValue, FunctionalProperty):
        comment = [locstr(LOCATION_ID_DEF, "en")]
        domain = [StopTime]
        seeAlso = [STOP_TIMES_URL]

    class stop_sequence(num_int):
        comment = [locstr(STOP_SEQUENCE_DEF, "en")]
        domain = [StopTime]
        range = [NonNegativeInteger]
        seeAlso = [STOP_TIMES_URL]

    class stop_headsign(text):
        comment = [locstr(STOP_HEADSIGN_DEF, "en")]
        domain = [StopTime]
        seeAlso = [STOP_TIMES_URL]

    class start_pickup_drop_off_window(time):
        comment = [locstr(START_PICKUP_DROP_OFF_WINDOW_DEF, "en")]
        domain = [StopTime]
        seeAlso = [STOP_TIMES_URL]

    class end_pickup_drop_off_window(time):
        comment = [locstr(END_PICKUP_DROP_OFF_WINDOW_DEF, "en")]
        domain = [StopTime]
        seeAlso = [STOP_TIMES_URL]

    class pickup_type(enum):
        comment = [locstr(PICKUP_TYPE_DEF, "en")]
        domain = [StopTime]
        range = [PickupTypeDatatype]
        seeAlso = [STOP_TIMES_URL]

    class drop_off_type(enum):
        comment = [locstr(DROP_OFF_TYPE_DEF, "en")]
        domain = [StopTime]
        range = [DropOffTypeDatatype]
        seeAlso = [STOP_TIMES_URL]

    class continuous_pickup(enum):
        comment = [locstr(CONTINUOUS_PICKUP_DEF, "en")]
        domain = [StopTime]
        range = [ContinuousPickupDatatype]
        seeAlso = [STOP_TIMES_URL]

    class continuous_drop_off(enum):
        comment = [locstr(CONTINUOUS_DROP_OFF_DEF, "en")]
        domain = [StopTime]
        range = [ContinuousDropOffDatatype]
        seeAlso = [STOP_TIMES_URL]

    class shape_dist_traveled(num_float):
        comment = [locstr(SHAPE_DIST_TRAVELED_DEF, "en")]
        domain = [StopTime]
        seeAlso = [STOP_TIMES_URL]

    class timepoint(enum):
        comment = [locstr(TIMEPOINT_DEF, "en")]
        domain = [StopTime]
        range = [TimepointDatatype]
        seeAlso = [STOP_TIMES_URL]

    class pickup_booking_rule_id(id):
        comment = [locstr(PICKUP_BOOKING_RULE_DEF, "en")]
        domain = [StopTime]
        seeAlso = [STOP_TIMES_URL]

    class drop_off_booking_rule_id(id):
        comment = [locstr(DROP_OFF_BOOKING_RULE_DEF, "en")]
        domain = [StopTime]
        seeAlso = [STOP_TIMES_URL]

    # endregion