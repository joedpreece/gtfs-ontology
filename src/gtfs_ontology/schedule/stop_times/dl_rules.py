from gtfs_ontology.schedule import *
from gtfs_ontology.schedule.stop_times.generate import *


with gtfs:

    StopTime.is_a.append(
        trip_id.exactly(1) &
        arrival_time.max(1) &
        departure_time.max(1) &
        stop_id.max(1) &
        location_group_id.max(1) &
        location_id.max(1) &
        stop_sequence.exactly(1) &
        stop_headsign.max(1) &
        start_pickup_drop_off_window.max(1) &
        end_pickup_drop_off_window.max(1) &
        pickup_type.max(1) &
        drop_off_type.max(1) &
        continuous_pickup.max(1) &
        continuous_drop_off.max(1) &
        shape_dist_traveled.max(1) &
        timepoint.max(1) &
        pickup_booking_rule_id.max(1) &
        drop_off_booking_rule_id.max(1)
    )

    class StopTimeFirst(StopTime):
        is_a = [
            arrival_time.exactly(1)
        ]

    class StopTimeLast(StopTime):
        is_a = [
            arrival_time.exactly(1)
        ]

    class StopTimeApproximateTime(StopTime):
        comment = [locstr("Times are considered approximate.", "en")]
        equivalent_to = [
            timepoint.value(0)
        ]

    class StopTimeExactTime(StopTime):
        comment = [locstr("Times are considered exact.", "en")]
        is_a = [
            arrival_time.exactly(1) |
            departure_time.exactly(1)
        ]
        equivalent_to = [
            timepoint.value(1)
        ]

    class StopTimeWithPickupDropOffWindow(StopTime):
        is_a = [
            arrival_time.exactly(0) |
            departure_time.exactly(0)
        ]
        equivalent_to = [
            start_pickup_drop_off_window.exactly(1) |
            end_pickup_drop_off_window.exactly(1)
        ]

    # stop_id

    class StopTimeWithStopID(StopTime):
        is_a = [
            stop_id.exactly(1)
        ]
        equivalent_to = [
            location_id.exactly(0) &
            location_group_id.exactly(0)
        ]

    class StopTimeWithNoStopID(StopTime):
        is_a = [
            stop_id.exactly(0)
        ]
        equivalent_to = [
            location_id.exactly(1) |
            location_group_id.exactly(1)
        ]

    class StopTimeWithNoLocationGroupID(StopTime):
        is_a = [
            location_group_id.exactly(0)
        ]
        equivalent_to = [
            stop_id.exactly(1) |
            location_id.exactly(1)
        ]

    class StopTimeWithNoLocationID(StopTime):
        is_a = [
            location_id.exactly(0)
        ]
        equivalent_to = [
            stop_id.exactly(1) |
            location_group_id.exactly(1)
        ]

    class StopTimeWithStartPickupDropOffWindow(StopTime):
        is_a = [
            start_pickup_drop_off_window.exactly(1)
        ]
        equivalent_to = [
            (
                location_id.exactly(1) |
                location_group_id.exactly(1)
            ) &
            end_pickup_drop_off_window.exactly(1)
        ]

    class StopTimeWithNoStartPickupDropOffWindow(StopTime):
        is_a = [
            start_pickup_drop_off_window.exactly(0)
        ]
        equivalent_to = [
            arrival_time.exactly(0) |
            departure_time.exactly(0)
        ]


    class StopTimeWithEndPickupDropOffWindow(StopTime):
        is_a = [
            end_pickup_drop_off_window.exactly(1)
        ]
        equivalent_to = [
            (
                location_id.exactly(1) |
                location_group_id.exactly(1)
            ) &
            start_pickup_drop_off_window.exactly(1)
        ]


    class StopTimeWithNoEndPickupDropOffWindow(StopTime):
        is_a = [
            start_pickup_drop_off_window.exactly(0)
        ]
        equivalent_to = [
            arrival_time.exactly(0) |
            departure_time.exactly(0)
        ]

    class RegularlyScheduledPickup(StopTime):
        comment = [locstr("Regularly scheduled pickup. ", "en")]
        equivalent_to = [
            (
                pickup_type.value(0) |
                pickup_type.exactly(0)
            ) &
            (
                start_pickup_drop_off_window.exactly(0) |
                end_pickup_drop_off_window.exactly(0)
            )
        ]

    # AllDisjoint([StopTimeWithStartPickupDropOffWindow, ])

    class NoPickupAvailable(StopTime):
        comment = [locstr("No pickup available.", "en")]
        equivalent_to = [
            pickup_type.value(1)
        ]

    class AgencyArrangedPickup(StopTime):
        comment = [locstr("Must phone agency to arrange pickup.", "en")]
        equivalent_to = [
            pickup_type.value(2)
        ]

    class DriverCoordinatedPickup(StopTime):
        comment = [locstr("Driver coordinated pickup.", "en")]
        equivalent_to = [
            pickup_type.value(3) &
            (
                start_pickup_drop_off_window.exactly(0) |
                end_pickup_drop_off_window.exactly(0)
            )
        ]

    class RegularlyScheduledDropOff(StopTime):
        comment = [locstr("Regularly scheduled drop off. ", "en")]
        equivalent_to = [
            (
                drop_off_type.value(0) |
                drop_off_type.exactly(0)
            ) &
            (
                start_pickup_drop_off_window.exactly(0) |
                end_pickup_drop_off_window.exactly(0)
            )
        ]

    class NoDropOffAvailable(StopTime):
        comment = [locstr("No drop off available.", "en")]
        equivalent_to = [
            drop_off_type.value(1)
        ]

    class AgencyArrangedDropOff(StopTime):
        comment = [locstr("Must phone agency to arrange drop off.", "en")]
        equivalent_to = [
            drop_off_type.value(2)
        ]

    class DriverCoordinatedDropOff(StopTime):
        comment = [locstr("Must coordinate with driver to arrange drop off.", "en")]
        equivalent_to = [
            drop_off_type.value(3)
        ]

    class ContinuousStoppingPickup(StopTime):
        comment = [locstr("Continuous stopping pickup.", "en")]
        equivalent_to = [
            continuous_pickup.value(0) &
            (
                start_pickup_drop_off_window.exactly(0) |
                end_pickup_drop_off_window.exactly(0)
            )
        ]

    class NoContinuousStoppingPickup(StopTime):
        comment = [locstr("No continuous stopping pickup.", "en")]
        equivalent_to = [
            continuous_pickup.value(1) |
            continuous_pickup.exactly(0)
        ]

    class AgencyArrangedContinuousStoppingPickup(StopTime):
        comment = [locstr("Must phone agency to arrange continuous stopping pickup.", "en")]
        equivalent_to = [
            continuous_pickup.value(2) &
            (
                start_pickup_drop_off_window.exactly(0) |
                end_pickup_drop_off_window.exactly(0)
            )
        ]

    class DriverCoordinatedContinuousStoppingPickup(StopTime):
        comment = [locstr("Must coordinate with driver to arrange continuous stopping pickup. ", "en")]
        equivalent_to = [
            continuous_pickup.value(3) &
            (
                start_pickup_drop_off_window.exactly(0) |
                end_pickup_drop_off_window.exactly(0)
            )
        ]

    class ContinuousStoppingDropOff(StopTime):
        comment = [locstr("Continuous stopping drop off.", "en")]
        equivalent_to = [
            continuous_drop_off.value(0) &
            (
                start_pickup_drop_off_window.exactly(0) |
                end_pickup_drop_off_window.exactly(0)
            )
        ]

    class NoContinuousStoppingDropOff(StopTime):
        comment = [locstr("No continuous stopping drop off.", "en")]
        equivalent_to = [
            continuous_drop_off.value(1) |
            continuous_drop_off.exactly(0)
        ]

    class AgencyArrangedContinuousStoppingDropOff(StopTime):
        comment = [locstr("Must phone agency to arrange continuous stopping drop off.", "en")]
        equivalent_to = [
            continuous_drop_off.value(2) &
            (
                start_pickup_drop_off_window.exactly(0) |
                end_pickup_drop_off_window.exactly(0)
            )
        ]

    class DriverCoordinatedContinuousStoppingDropOff(StopTime):
        comment = [locstr("Must coordinate with driver to arrange continuous stopping drop off.", "en")]
        equivalent_to = [
            continuous_drop_off.value(3) &
            (
                start_pickup_drop_off_window.exactly(0) |
                end_pickup_drop_off_window.exactly(0)
            )
        ]