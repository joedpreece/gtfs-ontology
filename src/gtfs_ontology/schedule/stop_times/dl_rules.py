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

    # stop_sequence

    StopTime.is_a.append(
        stop_sequence.exactly(1)
    )