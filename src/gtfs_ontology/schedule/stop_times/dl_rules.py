from gtfs_ontology.schedule import *
from gtfs_ontology.schedule.stop_times.generate import *


with gtfs:

    # trip_id

    StopTime.is_a.append(
        trip_id.exactly(1)
    )

    # arrival_time

    StopTime.is_a.append(
        arrival_time.max(1)
    )

    class StopTimeFirst(StopTime):
        pass

    class StopTimeLast(StopTime):
        pass

    class StopTimeExactTime(StopTime):
        pass

    class StopTimeApproximateTime(StopTime):
        pass

    class StopTimeWithPickupDropOffWindow(StopTime):
        equivalent_to = [
            StopTime &
            (
                start_pickup_drop_off_window.exactly(1) |
                end_pickup_drop_off_window.exactly(1)
            )
        ]

    StopTimeFirst.is_a.append(
        arrival_time.exactly(1)
    )

    StopTimeLast.is_a.append(
        arrival_time.exactly(1)
    )

    StopTimeExactTime.is_a.append(
        arrival_time.exactly(1)
    )

    StopTimeWithPickupDropOffWindow.is_a.append(
        arrival_time.exactly(0)
    )

    # departure_time

    StopTime.is_a.append(
        departure_time.max(1)
    )

    StopTimeExactTime.is_a.append(
        departure_time.exactly(1)
    )

    StopTimeWithPickupDropOffWindow.is_a.append(
        departure_time.exactly(0)
    )

    # stop_id

    StopTime.is_a.append(
        stop_id.exactly(1)
    )

    # location_group_id

    StopTime.is_a.append(
        location_group_id.max(1)
    )

    # location_id

    StopTime.is_a.append(
        location_id.max(1)
    )

    # stop_sequence

    StopTime.is_a.append(
        stop_sequence.exactly(1)
    )

    # stop_headsign

    StopTime.is_a.append(
        stop_headsign.max(1)
    )

    # start_pickup_drop_off_window

    StopTime.is_a.append(
        start_pickup_drop_off_window.max(1)
    )

    # end_pickup_drop_off_window

    StopTime.is_a.append(
        end_pickup_drop_off_window.max(1)
    )

    # pickup_type

    StopTime.is_a.append(
        pickup_type.max(1)
    )

    # drop_off_type

    StopTime.is_a.append(
        drop_off_type.max(1)
    )

    # continuous_pickup

    StopTime.is_a.append(
        continuous_pickup.max(1)
    )

    # continuous_dropoff

    StopTime.is_a.append(
        continuous_drop_off.max(1)
    )

    # shape_dist_traveled

    StopTime.is_a.append(
        shape_dist_traveled.max(1)
    )

    # timepoint

    StopTime.is_a.append(
        timepoint.max(1)
    )

    # pickup_booking_rule_id

    StopTime.is_a.append(
        pickup_booking_rule_id.max(1)
    )

    # drop_off_booking_rule_id

    StopTime.is_a.append(
        drop_off_booking_rule_id.max(1)
    )