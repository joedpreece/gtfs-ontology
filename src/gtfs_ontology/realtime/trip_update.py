from gtfs_ontology.realtime.core import *

# region Definitions

TRIP_DEF = """
The Trip that this message applies to. There can be at most one TripUpdate entity for each actual
trip instance. If there is none, that means there is no prediction information available. It does
not mean that the trip is progressing according to schedule.
"""

VEHICLE_DEF = """
Additional information on the vehicle that is serving this trip.
"""

STOP_TIME_UPDATE_DEF = """
Updates to StopTimes for the trip (both future, i.e., predictions, and in some cases, past ones,
i.e., those that already happened). The updates must be sorted by stop_sequence, and apply for all
the following stops of the trip up to the next specified stop_time_update.

If trip.schedule_relationship is SCHEDULED or UNSCHEDULED, at least one stop_time_update must be
provided for the trip.

If trip.schedule_relationship is NEW or REPLACEMENT, stop_time_updates must be provided for all
stops in the new or replacement trip, including stops with times in the past, and the stop times in
the static GTFS are not used.

If the trip is canceled or deleted, no stop_time_updates need to be provided. If stop_time_updates
are provided for a canceled or deleted trip then the trip.schedule_relationship takes precedence
over any stop_time_updates and their associated schedule_relationship. If the trip is duplicated,
stop_time_updates may be provided to indicate real-time information for the new trip.
"""

TIMESTAMP_DEF = """
The most recent moment at which the vehicle's real-time progress was measured to estimate StopTimes
in the future. When StopTimes in the past are provided, arrival/departure times may be earlier than
this value. In POSIX time (i.e., the number of seconds since January 1st 1970 00:00:00 UTC).
"""

DELAY_DEF = """
The current schedule deviation for the trip. Delay should only be specified when the prediction is
given relative to some existing schedule in GTFS.

Delay (in seconds) can be positive (meaning that the vehicle is late) or negative (meaning that the
vehicle is ahead of schedule). Delay of 0 means that the vehicle is exactly on time.

Delay information in StopTimeUpdates take precedent of trip-level delay information, such that
trip-level delay is only propagated until the next stop along the trip with a StopTimeUpdate delay
value specified.

Feed providers are strongly encouraged to provide a TripUpdate.timestamp value indicating when the
delay value was last updated, in order to evaluate the freshness of the data.

Caution: this field is still experimental, and subject to change. It may be formally adopted in the
future.
"""

TRIP_PROPERTIES_DEF = """
Provides the updated properties for the trip.

Caution: this message is still experimental, and subject to change. It may be formally adopted in
the future.
"""

# endregion

with gtfs:
    class trip(FieldValue, FunctionalProperty):
        # Required, One
        comment = [locstr(TRIP_DEF, "en")]
        domain = [FeedEntity]
        range = [TripDescriptor]


    class vehicle(FieldValue, FunctionalProperty):
        # Optional, One
        comment = [locstr(VEHICLE_DEF, "en")]
        domain = [FeedEntity]
        range = [VehicleDescriptor]


    class stop_time_update(FieldValue):
        # Conditionally required, Many  → not FunctionalProperty
        comment = [locstr(STOP_TIME_UPDATE_DEF, "en")]
        domain = [FeedEntity]
        range = [StopTimeUpdate]


    class timestamp(FieldValue, FunctionalProperty):
        # Optional, One
        comment = [locstr(TIMESTAMP_DEF, "en")]
        domain = [FeedEntity]
        # uint64 represented as POSIX seconds
        range = [int]


    class delay(FieldValue, FunctionalProperty):
        # Optional, One
        comment = [locstr(DELAY_DEF, "en")]
        domain = [FeedEntity]
        # int32 seconds (negative = early, positive = late)
        range = [int]


    class trip_properties(FieldValue, FunctionalProperty):
        # Optional, One
        comment = [locstr(TRIP_PROPERTIES_DEF, "en")]
        domain = [FeedEntity]
        range = [TripProperties]