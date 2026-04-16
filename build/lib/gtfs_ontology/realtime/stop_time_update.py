from gtfs_ontology.realtime.core import *

# region Definitions

STOP_SEQUENCE_DEF = """
Must be the same as in stop_times.txt in the corresponding GTFS feed. Either stop_sequence or stop_id must be provided within a StopTimeUpdate - both fields cannot be empty. stop_sequence is required for trips that visit the same stop_id more than once (e.g., a loop) to disambiguate which stop the prediction is for. If StopTimeProperties.assigned_stop_id is populated, then stop_sequence must be populated. Required if TripUpdate.schedule_relationship is NEW or REPLACEMENT, and the value must be increasing along the trip.
"""

STOP_ID_DEF = """
Must be the same as in stops.txt in the corresponding GTFS feed. Either stop_sequence or stop_id must be provided within a StopTimeUpdate - both fields cannot be empty. If StopTimeProperties.assigned_stop_id is populated, it is preferred to omit stop_id and use only stop_sequence. If StopTimeProperties.assigned_stop_id and stop_id are populated, stop_id must match assigned_stop_id. Required if TripUpdate.schedule_relationship is NEW or REPLACEMENT.
"""

ARRIVAL_DEF = """
If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate - both fields cannot be empty. arrival and departure may both be empty when schedule_relationship is SKIPPED. Required if TripUpdate.schedule_relationship is NEW or REPLACEMENT.
"""

DEPARTURE_DEF = """
If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate - both fields cannot be empty. arrival and departure may both be empty when schedule_relationship is SKIPPED. Required if TripUpdate.schedule_relationship is NEW or REPLACEMENT.
"""

DEPARTURE_OCCUPANCY_STATUS_DEF = """
The predicted state of passenger occupancy for the vehicle immediately after departure from the given stop. If provided, stop_sequence must be provided. To provide departure_occupancy_status without providing any real-time arrival or departure predictions, populate this field and set StopTimeUpdate.schedule_relationship = NO_DATA.

Caution: this field is still experimental, and subject to change. It may be formally adopted in the future.
"""

SCHEDULE_RELATIONSHIP_DEF = """
The default relationship is SCHEDULED.
"""

SCHEDULE_RELATIONSHIP_DATATYPE_DEF = """
The default relationship is SCHEDULED.
"""

SCHEDULE_RELATIONSHIP_SCHEDULED_DEF = """
The vehicle is proceeding in accordance with its static schedule of stops, although not necessarily according to the times of the schedule. This is the default behavior. At least one of arrival and departure must be provided. Frequency-based trips (GTFS frequencies.txt with exact_times = 0) should not have a SCHEDULED value and should use UNSCHEDULED instead.
"""

SCHEDULE_RELATIONSHIP_SKIPPED_DEF = """
The stop is skipped, i.e., the vehicle will not stop at this stop. Arrival and departure are optional. When set SKIPPED is not propagated to subsequent stops in the same trip (i.e., the vehicle will stop at subsequent stops in the trip unless those stops also have a stop_time_update with schedule_relationship: SKIPPED). Delay from a previous stop in the trip does propagate over the SKIPPED stop. In other words, if a stop_time_update with an arrival or departure prediction is not set for a stop after the SKIPPED stop, the prediction upstream of the SKIPPED stop will be propagated to the stop after the SKIPPED stop and subsequent stops in the trip until a stop_time_update for a subsequent stop is provided.
"""

SCHEDULE_RELATIONSHIP_NO_DATA_DEF = """
No real-time data is given for this stop. It indicates that there is no realtime timing information available. When set NO_DATA is propagated through subsequent stops so this is the recommended way of specifying from which stop you do not have realtime timing information. When NO_DATA is set, arrival or departure must not be supplied, unless TripDescriptor.schedule_relationship is NEW or REPLACEMENT, in such case only the scheduled time, but not predictions, must be supplied. When TripDescriptor.schedule_relationship is NEW or REPLACEMENT, arrival and departure must still be given with scheduled times, as the StopTimeUpdate defines the stop list of the trip. In this case it indicates that the schedule is unrelated to the static GTFS, but real-time prediction is not available yet.
"""

SCHEDULE_RELATIONSHIP_UNSCHEDULED_DEF = """
The vehicle is operating a frequency-based trip (GTFS frequencies.txt with exact_times = 0). This value should not be used for trips that are not defined in GTFS frequencies.txt, or trips in GTFS frequencies.txt with exact_times = 1. Trips containing stop_time_updates with schedule_relationship: UNSCHEDULED must also set the TripDescriptor schedule_relationship: UNSCHEDULED
"""

STOP_TIME_PROPERTIES_DEF = """
Realtime updates for certain properties defined within GTFS stop_times.txt
"""

# endregion

with gtfs:

    # region Datatypes

    class ScheduleRelationshipDatatype(Datatype):
        equivalent_to = [
            OneOf(
                [
                     "SCHEDULED",
                     "SKIPPED",
                     "NO_DATA",
                     "UNSCHEDULED",
                ]
            )
        ]

    class OccupancyStatus(Datatype):
        equivalent_to = [
            OneOf(
                [
                    "EMPTY",
                    "MANY_SEATS_AVAILABLE",
                    "FEW_SEATS_AVAILABLE",
                    "STANDING_ROOM_ONLY",
                    "CRUSHED_STANDING_ROOM_ONLY",
                    "FULL",
                    "NOT_ACCEPTING_PASSENGERS",
                    "NO_DATA_AVAILABLE",
                    "NOT_BOARDABLE"
                ]
            )
        ]

    # endregion

    # region Classes

    class ScheduleRelationshipDatatypeDescription(DatatypeDescription):
        comment = [locstr(SCHEDULE_RELATIONSHIP_DATATYPE_DEF, "en")]

    class ScheduleRelationshipDatatypeDescriptionScheduled(ScheduleRelationshipDatatypeDescription):
        comment = [locstr(SCHEDULE_RELATIONSHIP_SCHEDULED_DEF, "en")]

    class ScheduleRelationshipDatatypeDescriptionSkipped(ScheduleRelationshipDatatypeDescription):
        comment = [locstr(SCHEDULE_RELATIONSHIP_SKIPPED_DEF, "en")]

    class ScheduleRelationshipDatatypeDescriptionNoData(ScheduleRelationshipDatatypeDescription):
        comment = [locstr(SCHEDULE_RELATIONSHIP_NO_DATA_DEF, "en")]

    class ScheduleRelationshipDatatypeDescriptionUnscheduled(ScheduleRelationshipDatatypeDescription):
        comment = [locstr(SCHEDULE_RELATIONSHIP_UNSCHEDULED_DEF, "en")]

    # endregion

    # region Object and Data Properties

    class stop_sequence(FieldValue, FunctionalProperty):
        comment = [locstr(STOP_SEQUENCE_DEF, "en")]
        domain = [StopTimeUpdate]
        range = [int]

    class stop_id(FieldValue, FunctionalProperty):
        comment = [locstr(STOP_ID_DEF, "en")]
        domain = [StopTimeUpdate]
        range = [str]

    class arrival(FieldValue, FunctionalProperty):
        comment = [locstr(ARRIVAL_DEF, "en")]
        domain = [StopTimeUpdate]
        range = [StopTimeEvent]

    class departure(FieldValue, FunctionalProperty):
        comment = [locstr(DEPARTURE_DEF, "en")]
        domain = [StopTimeUpdate]
        range = [StopTimeEvent]

    class departure_occupancy_status(ExperimentalField, FunctionalProperty):
        comment = [locstr(DEPARTURE_OCCUPANCY_STATUS_DEF, "en")]
        domain = [StopTimeUpdate]
        range = [OccupancyStatus]

    class schedule_relationship(FieldValue, FunctionalProperty):
        comment = [locstr(SCHEDULE_RELATIONSHIP_DEF, "en")]
        domain = [StopTimeUpdate]
        range = [ScheduleRelationshipDatatype]

    class stop_time_properties(ExperimentalField, FunctionalProperty):
        comment = [locstr(STOP_TIME_PROPERTIES_DEF, "en")]
        domain = [StopTimeUpdate]
        range = [StopTimeProperties]