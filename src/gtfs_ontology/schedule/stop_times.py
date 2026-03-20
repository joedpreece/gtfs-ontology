from gtfs_ontology.schedule.core import *
from trips import trip_id
from stops import stop_id

# region Definitions

TRIP_ID_DEF = """
Identifies a trip.
"""

ARRIVAL_TIME_DEF = """
Arrival time at the stop (defined by stop_times.stop_id) for a specific trip (defined by stop_times.trip_id) in the time zone specified by agency.agency_timezone, not stops.stop_timezone. 
"""

DEPARTURE_TIME_DEF = """
Departure time from the stop (defined by stop_times.stop_id) for a specific trip (defined by stop_times.trip_id) in the time zone specified by agency.agency_timezone, not stops.stop_timezone.

If there are not separate times for arrival and departure at a stop, arrival_time and departure_time should be the same.

For times occurring after midnight on the service day, enter the time as a value greater than 24:00:00 in HH:MM:SS.

If exact arrival and departure times (timepoint=1) are not available, estimated or interpolated arrival and departure times (timepoint=0) should be provided.
"""

STOP_ID_DEF = """
Identifies the serviced stop. All stops serviced during a trip must have a record in stop_times.txt. Referenced locations must be stops/platforms, i.e. their stops.location_type value must be 0 or empty. A stop may be serviced multiple times in the same trip, and multiple trips and routes may service the same stop.

On-demand service using stops should be referenced in the sequence in which service is available at those stops. A data consumer should assume that travel is possible from one stop or location to any stop or location later in the trip, provided that the pickup/drop_off_type of each stop_time and the time constraints of each start/end_pickup_drop_off_window do not forbid it.

Conditionally Required:
- Required if stop_times.location_group_id AND stop_times.location_id are NOT defined.
- Forbidden if stop_times.location_group_id or stop_times.location_id are defined.
"""

LOCATION_GROUP_ID_DEF = """
Identifies the serviced location group that indicates groups of stops where riders may request pickup or drop off. All location groups serviced during a trip must have a record in stop_times.txt. Multiple trips and routes may service the same location group.

On-demand service using location groups should be referenced in the sequence in which service is available at those location groups. A data consumer should assume that travel is possible from one stop or location to any stop or location later in the trip, provided that the pickup/drop_off_type of each stop_time and the time constraints of each start/end_pickup_drop_off_window do not forbid it.
"""

LOCATION_ID_DEF = """
Identifies the GeoJSON location that corresponds to serviced zone where riders may request pickup or drop off. All GeoJSON locations serviced during a trip must have a record in stop_times.txt. Multiple trips and routes may service the same GeoJSON location.

On-demand service within locations should be referenced in the sequence in which service is available in those locations. A data consumer should assume that travel is possible from one stop or location to any stop or location later in the trip, provided that the pickup/drop_off_type of each stop_time and the time constraints of each start/end_pickup_drop_off_window do not forbid it.
"""

STOP_SEQUENCE_DEF = """
Order of stops, location groups, or GeoJSON locations for a particular trip. The values must increase along the trip but do not need to be consecutive. Example: The first location on the trip could have a stop_sequence=1, the second location on the trip could have a stop_sequence=23, the third location could have a stop_sequence=40, and so on.

Travel within the same location group or GeoJSON location requires two records in stop_times.txt with the same location_group_id or location_id.
"""

STOP_HEADSIGN_DEF = """
Text that appears on signage identifying the trip's destination to riders. This field overrides the default trips.trip_headsign when the headsign changes between stops. If the headsign is displayed for an entire trip, trips.trip_headsign should be used instead.

A stop_headsign value specified for one stop_time does not apply to subsequent stop_times in the same trip. If you want to override the trip_headsign for multiple stop_times in the same trip, the stop_headsign value must be repeated in each stop_time row.
"""

START_PICKUP_DROP_OFF_WINDOW_DEF = """
Time that on-demand service becomes available in a GeoJSON location, location group, or stop.
"""

END_PICKUP_DROP_OFF_WINDOW_DEF = """
Time that on-demand service ends in a GeoJSON location, location group, or stop.
"""

PICKUP_TYPE_DEF = """
Indicates pickup method.
"""

DROP_OFF_TYPE_DEF = """
Indicates drop off method.
"""

CONTINUOUS_PICKUP_DEF = """
Indicates that the rider can board the transit vehicle at any point along the vehicle’s travel path as described by shapes.txt, from this stop_time to the next stop_time in the trip’s stop_sequence.
"""

CONTINUOUS_DROP_OFF_DEF = """
Indicates that the rider can alight from the transit vehicle at any point along the vehicle’s travel path as described by shapes.txt, from this stop_time to the next stop_time in the trip’s stop_sequence.
"""

SHAPE_DIST_TRAVELED_DEF = """
Actual distance traveled along the associated shape, from the first stop to the stop specified in this record. This field specifies how much of the shape to draw between any two stops during a trip. Must be in the same units used in shapes.txt. Values used for shape_dist_traveled must increase along with stop_sequence; they must not be used to show reverse travel along a route.
"""

TIMEPOINT_DEF = """
Indicates if arrival and departure times for a stop are strictly adhered to by the vehicle or if they are instead approximate and/or interpolated times. This field allows a GTFS producer to provide interpolated stop-times, while indicating that the times are approximate.
"""

PICKUP_BOOKING_RULE_DEF = """
Identifies the boarding booking rule at this stop time.
"""

DROP_OFF_BOOKING_RULE_DEF = """
Identifies the alighting booking rule at this stop time.
"""

# endregion

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

    class arrival_time(FieldValue, FunctionalProperty):
        comment = [locstr(ARRIVAL_TIME_DEF, "en")]
        domain = [StopTime]
        range = [datetime.time]

    class departure_time(FieldValue, FunctionalProperty):
        comment = [locstr(DEPARTURE_TIME_DEF, "en")]
        domain = [StopTime]
        range = [datetime.time]

    stop_id.comment.append(locstr(STOP_ID_DEF, "en"))
    stop_id.domain.append(StopTime)

    class location_group_id(FieldValue, FunctionalProperty):
        comment = [locstr(LOCATION_GROUP_ID_DEF, "en")]
        domain = [StopTime]
        range = [str]

    class location_id(FieldValue, FunctionalProperty):
        comment = [locstr(LOCATION_ID_DEF, "en")]
        domain = [StopTime]
        range = [str]

    class stop_sequence(FieldValue, FunctionalProperty):
        comment = [locstr(STOP_SEQUENCE_DEF, "en")]
        domain = [StopTime]
        range = [NonNegativeInteger]

    class stop_headsign(FieldValue, FunctionalProperty):
        comment = [locstr(STOP_HEADSIGN_DEF, "en")]
        domain = [StopTime]
        range = [str]

    class start_pickup_drop_off_window(FieldValue, FunctionalProperty):
        comment = [locstr(START_PICKUP_DROP_OFF_WINDOW_DEF, "en")]
        domain = [StopTime]
        range = [datetime.time]

    class end_pickup_drop_off_window(FieldValue, FunctionalProperty):
        comment = [locstr(END_PICKUP_DROP_OFF_WINDOW_DEF, "en")]
        domain = [StopTime]
        range = [datetime.time]

    class pickup_type(FieldValue, FunctionalProperty):
        comment = [locstr(PICKUP_TYPE_DEF, "en")]
        domain = [StopTime]
        range = [PickupTypeDatatype]

    class drop_off_type(FieldValue, FunctionalProperty):
        comment = [locstr(DROP_OFF_TYPE_DEF, "en")]
        domain = [StopTime]
        range = [DropOffTypeDatatype]

    class continuous_pickup(FieldValue, FunctionalProperty):
        comment = [locstr(CONTINUOUS_PICKUP_DEF, "en")]
        domain = [StopTime]
        range = [ContinuousPickupDatatype]

    class continuous_drop_off(FieldValue, FunctionalProperty):
        comment = [locstr(CONTINUOUS_DROP_OFF_DEF, "en")]
        domain = [StopTime]
        range = [ContinuousDropOffDatatype]

    class shape_dist_traveled(FieldValue, FunctionalProperty):
        comment = [locstr(SHAPE_DIST_TRAVELED_DEF, "en")]
        domain = [StopTime]
        range = [float]

    class pickup_booking_rule(FieldValue, FunctionalProperty):
        comment = [locstr(PICKUP_BOOKING_RULE_DEF, "en")]
        domain = [StopTime]
        range = [str]

    class drop_off_booking_rule(FieldValue, FunctionalProperty):
        comment = [locstr(DROP_OFF_BOOKING_RULE_DEF, "en")]
        domain = [StopTime]
        range = [str]

    # endregion