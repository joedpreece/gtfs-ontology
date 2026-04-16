from gtfs_ontology.realtime.core import *

# region Definitions

TRIP_ID_DEF = """
Defines the identifier of a new trip that is a duplicate of an existing trip defined in (CSV) GTFS trips.txt but will start at a different service date and/or time (defined using TripProperties.start_date and TripProperties.start_time). See definition of trips.trip_id in (CSV) GTFS. Its value must be different than the ones used in the (CSV) GTFS. This field is required if schedule_relationship is DUPLICATED, otherwise this field must not be populated and will be ignored by consumers.
"""

START_DATE_DEF = """
Service date on which the duplicated trip will be run. Must be provided in YYYYMMDD format. This field is required if schedule_relationship is DUPLICATED, otherwise this field must not be populated and will be ignored by consumers.
"""

START_TIME_DEF = """
Defines the departure start time of the trip when it’s duplicated. See definition of stop_times.departure_time in (CSV) GTFS. Scheduled arrival and departure times for the duplicated trip are calculated based on the offset between the original trip departure_time and this field. For example, if a GTFS trip has stop A with a departure_time of 10:00:00 and stop B with departure_time of 10:01:00, and this field is populated with the value of 10:30:00, stop B on the duplicated trip will have a scheduled departure_time of 10:31:00. Real-time prediction delay values are applied to this calculated schedule time to determine the predicted time. For example, if a departure delay of 30 is provided for stop B, then the predicted departure time is 10:31:30. Real-time prediction time values do not have any offset applied to them and indicate the predicted time as provided. For example, if a departure time representing 10:31:30 is provided for stop B, then the predicted departure time is 10:31:30. This field is required if schedule_relationship is DUPLICATED, otherwise this field must not be populated and will be ignored by consumers.
"""

TRIP_HEADSIGN_DEF = """
Specifies the headsign for this trip when it differs from the original.
"""

TRIP_SHORT_NAME_DEF = """
Specifies the name for this trip when it differs from the original.
"""

SHAPE_ID_DEF = """
Specifies the identifier of the shape of the vehicle travel path when the trip shape differs from the shape specified in (CSV) GTFS or to specify it in real-time when it's not provided by (CSV) GTFS, such as a vehicle that takes differing paths based on rider demand. See definition of trips.shape_id in (CSV) GTFS.
If a shape is neither defined in (CSV) GTFS nor in real-time, the shape is considered unknown. This field can refer to a shape defined in the (CSV) GTFS in shapes.txt or a Shape in the same (protobuf) real-time feed. The order of stops (stop sequences) for this trip must remain the same as (CSV) GTFS. If it refers to a Shape entity in the same real-time feed, the value of this field should be the one of the shape_id inside the entity, and not the id of FeedEntity.
Stops that are a part of the original trip but will no longer be made, such as when a detour occurs, should be marked as schedule_relationship=SKIPPED or more details can be provided via a TripModifications message.
"""

# endregion

with gtfs:

    # region Object and Data Properties

    class trip_id(ExperimentalField, FunctionalProperty):
        comment = [locstr(TRIP_ID_DEF, "en")]
        domain = [TripProperties]
        range = [str]

    class start_date(ExperimentalField, FunctionalProperty):
        comment = [locstr(START_DATE_DEF, "en")]
        domain = [TripProperties]
        range = [datetime.date]

    class start_time(ExperimentalField, FunctionalProperty):
        comment = [locstr(START_TIME_DEF, "en")]
        domain = [TripProperties]
        range = [datetime.time]

    class trip_headsign(ExperimentalField, FunctionalProperty):
        comment = [locstr(TRIP_HEADSIGN_DEF, "en")]
        domain = [TripProperties]
        range = [str]

    class trip_short_name(ExperimentalField, FunctionalProperty):
        comment = [locstr(TRIP_SHORT_NAME_DEF, "en")]
        domain = [TripProperties]
        range = [str]

    class shape_id(ExperimentalField, FunctionalProperty):
        pass
        # comment = [locstr(SHAPE_ID_DEF, "en")]
        # domain = [TripProperties]
        # range = [str]

    shape_id.comment.append(locstr(SHAPE_ID_DEF, "en"))
    shape_id.domain.append(TripProperties)

    # endregion