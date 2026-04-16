from gtfs_ontology.realtime.core import *
from gtfs_ontology.realtime.stop_time_update import OccupancyStatus
from gtfs_ontology.schedule.stops import stop_id

# region Definitions

# VehiclePosition field descriptions (GTFS Realtime)

VEHICLEPOSITION_TRIP_DEF = """
The Trip that this vehicle is serving. Can be empty or partial if the vehicle can not be identified with a given trip instance.
"""
# Source: message VehiclePosition → trip.

VEHICLEPOSITION_VEHICLE_DEF = """
Additional information on the vehicle that is serving this trip. Each entry should have a **unique** vehicle id.
"""
# Source: message VehiclePosition → vehicle.

VEHICLEPOSITION_POSITION_DEF = """
Current position of this vehicle.
"""
# Source: message VehiclePosition → position.

VEHICLEPOSITION_CURRENT_STOP_SEQUENCE_DEF = """
The stop sequence index of the current stop. The meaning of 
current_stop_sequence (i.e., the stop that it refers to) is determined 
by current_status. If current_status is missing IN_TRANSIT_TO is 
assumed.
"""
# Source: message VehiclePosition → current_stop_sequence.

VEHICLEPOSITION_STOP_ID_DEF = """
Identifies the current stop. The value must be the same as in stops.txt in the corresponding GTFS feed. If `StopTimeProperties.assigned_stop_id` is used to assign a `stop_id`, this field should also reflect the change in `stop_id`.
"""
# Source: message VehiclePosition → stop_id.

VEHICLEPOSITION_CURRENT_STATUS_DEF = """
The exact status of the vehicle with respect to the current stop. Ignored if current_stop_sequence is missing.
"""
# Source: message VehiclePosition → current_status.

VEHICLEPOSITION_TIMESTAMP_DEF = """
Moment at which the vehicle's position was measured. In POSIX time 
(i.e., number of seconds since January 1st 1970 00:00:00 UTC).
"""
# Source: message VehiclePosition → timestamp.

VEHICLEPOSITION_CONGESTION_LEVEL_DEF = """
"""
# Source: message VehiclePosition → congestion_level (enum; description cell blank).

VEHICLEPOSITION_OCCUPANCY_STATUS_DEF = """
The state of passenger occupancy for the vehicle or carriage. If 
multi_carriage_details is populated with per-carriage OccupancyStatus, 
then this field should describe the entire vehicle with all carriages 
accepting passengers considered.

**Caution:** this field is still **experimental**, and subject to change. It may be formally adopted in the future.
"""
# Source: message VehiclePosition → occupancy_status.

VEHICLEPOSITION_OCCUPANCY_PERCENTAGE_DEF = """
A percentage value indicating the degree of passenger occupancy in 
the vehicle. The value 100 should represent the total maximum occupancy 
the vehicle was designed for, including both seating and standing 
capacity, and current operating regulations allow. The value may exceed 
100 if there are more passengers than the maximum designed capacity. The 
 precision of occupancy_percentage should be low enough that individual 
passengers cannot be tracked boarding or alighting the vehicle. If 
multi_carriage_details is populated with per-carriage 
occupancy_percentage, then this field should describe the entire vehicle 
 with all carriages accepting passengers considered.

**Caution:** this field is still **experimental**, and subject to change. It may be formally adopted in the future.
"""
# Source: message VehiclePosition → occupancy_percentage.

VEHICLEPOSITION_MULTI_CARRIAGE_DETAILS_DEF = """
Details of the multiple carriages of this given vehicle. The first occurrence represents the first carriage of the vehicle, **given the current direction of travel**. 
 The number of occurrences of the multi_carriage_details field 
represents the number of carriages of the vehicle. It also includes non 
boardable carriages, like engines, maintenance carriages, etc… as they 
provide valuable information to passengers about where to stand on a 
platform.

**Caution:** this field is still **experimental**, and subject to change. It may be formally adopted in the future.
"""
# Source: message VehiclePosition → multi_carriage_details.

with gtfs:

    # region Datatypes

    class VehicleStopStatus(Datatype):
        equivalent_to = [
            OneOf(
                [
                    "INCOMING_AT",
                    "STOPPED_AT",
                    "IN_TRANSIT_TO"
                ]
            )
        ]

    class CongestionLevel(Datatype):
        equivalent_to = [
            OneOf(
                [
                    "UNKNOWN_CONGESTION_LEVEL",
                    "RUNNING_SMOOTHLY",
                    "STOP_AND_GO",
                    "CONGESTION",
                    "SEVERE_CONGESTION"
                ]
            )
        ]

    # endregion

    # region Object and Data Properties

    class trip(FieldValue, FunctionalProperty):
        comment = [locstr(VEHICLEPOSITION_TRIP_DEF, "en")]
        domain = [VehiclePosition]
        range = [TripDescriptor]

    class vehicle(FieldValue, FunctionalProperty):
        comment = [locstr(VEHICLEPOSITION_VEHICLE_DEF, "en")]
        domain = [VehiclePosition]
        range = [VehicleDescriptor]

    class position(FieldValue, FunctionalProperty):
        comment = [locstr(VEHICLEPOSITION_POSITION_DEF, "en")]
        domain = [VehiclePosition]
        range = [Position]

    class current_stop_sequence(FieldValue, FunctionalProperty):
        comment = [locstr(VEHICLEPOSITION_CURRENT_STOP_SEQUENCE_DEF, "en")]
        domain = [VehiclePosition]
        range = [int]

    stop_id.comment.append(locstr(VEHICLEPOSITION_STOP_ID_DEF, "en"))
    stop_id.domain.append(VehiclePosition)

    class current_status(FieldValue, FunctionalProperty):
        comment = [locstr(VEHICLEPOSITION_CURRENT_STATUS_DEF, "en")]
        domain = [VehiclePosition]
        range = [VehicleStopStatus]

    class timestamp(FieldValue, FunctionalProperty):
        comment = [locstr(VEHICLEPOSITION_TIMESTAMP_DEF, "en")]
        domain = [VehiclePosition]
        range = [datetime.time]

    class congestion_level(FieldValue, FunctionalProperty):
        comment = [locstr(VEHICLEPOSITION_CONGESTION_LEVEL_DEF, "en")]
        domain = [VehiclePosition]
        range = [CongestionLevel]

    class occupancy_status(ExperimentalField, FunctionalProperty):
        comment = [locstr(VEHICLEPOSITION_OCCUPANCY_STATUS_DEF, "en")]
        domain = [VehiclePosition]
        range = [OccupancyStatus]

    class occupancy_percentage(ExperimentalField, FunctionalProperty):
        comment = [locstr(VEHICLEPOSITION_OCCUPANCY_PERCENTAGE_DEF, "en")]
        domain = [VehiclePosition]
        range = [int]

    class multi_carriage_details(ExperimentalField):
        comment = [locstr(VEHICLEPOSITION_MULTI_CARRIAGE_DETAILS_DEF, "en")]
        domain = [VehiclePosition]
        range = [CarriageDetails]


