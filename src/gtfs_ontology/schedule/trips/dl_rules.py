from gtfs_ontology.schedule import *
from gtfs_ontology.schedule.core import isRecordOf, isFileOf, hasFile, hasRecord
from gtfs_ontology.schedule.files.generate import RouteFile, StopTimeFile, TripFile
from gtfs_ontology.schedule.records.generate import Route, StopTime
from gtfs_ontology.schedule.routes.generate import continuous_pickup, \
    continuous_drop_off
from gtfs_ontology.schedule.stops.dl_rules import RecordWithAccessibilityInformation
from gtfs_ontology.schedule.term_definitions.generate import Dataset
from gtfs_ontology.schedule.trips.generate import *

with gtfs:

    # route_id

    Trip.is_a.extend([
        route_id.exactly(1),
        service_id.exactly(1),
        trip_id.exactly(1),
        trip_headsign.max(1),
        trip_short_name.max(1),
        direction_id.max(1),
        block_id.max(1),
        shape_id.max(1),
        wheelchair_accessible.max(1),
        bikes_allowed.max(1),
        cars_allowed.max(1)
    ])

    # class TripWithShapeID(Trip):
    #     equivalent_to = [
    #         Trip &
    #         isRecordOf.some(
    #             TripFile &
    #             isFileOf.some(
    #                 Dataset &
    #                 hasFile.some(
    #                     (
    #                         RouteFile &
    #                         hasRecord.some(
    #                             Route &
    #                             (
    #                                 continuous_pickup.exactly(1) |
    #                                 continuous_drop_off.exactly(1)
    #                             )
    #                         )
    #                     ) |
    #                     (
    #                         StopTimeFile &
    #                         hasRecord.some(
    #                             StopTime &
    #                             (
    #                                 continuous_pickup.exactly(1) |
    #                                 continuous_drop_off.exactly(1)
    #                             )
    #                         )
    #                     )
    #                 )
    #             )
    #         )
    #     ]
    #     is_a = [
    #         shape_id.exactly(1)
    #     ]

    class TripInDirectionA(Trip):
        comment = [locstr(DIRECTION_A, "en")]
        equivalent_to = [
            Trip &
            direction_id.value(0)
        ]

    class TripInDirectionB(Trip):
        comment = [locstr(DIRECTION_B, "en")]
        equivalent_to = [
            Trip &
            direction_id.value(1)
        ]

    # block_id

    ## TODO: Add conditional requirement here

    # wheelchair_accessible

    class TripWithNoWheelchairAccessibilityInformation(Trip, RecordWithAccessibilityInformation):
        comment = [locstr(WHEELCHAIR_ACCESSIBLE_0_DEF, "en")]
        equivalent_to = [
            Trip &
            (
                wheelchair_accessible.value(0) |
                wheelchair_accessible.exactly(0)
            )
        ]

    class TripWithAtLeastOneWheelchairSpace(Trip, RecordWithAccessibilityInformation):
        comment = [locstr(WHEELCHAIR_ACCESSIBLE_1_DEF, "en")]
        equivalent_to = [
            Trip &
            wheelchair_accessible.value(1)
        ]

    class TripWithNoWheelchairAccessibility(Trip, RecordWithAccessibilityInformation):
        comment = [locstr(WHEELCHAIR_ACCESSIBLE_2_DEF, "en")]
        equivalent_to = [
            Trip &
            wheelchair_accessible.value(2)
        ]

    # bikes_allowed

    class TripWithNoBikesAllowedInformation(Trip):
        comment = [locstr(BIKES_ALLOWED_0_DEF, "en")]
        equivalent_to = [
            Trip &
            (
                bikes_allowed.value(0) |
                bikes_allowed.exactly(0)
            )
        ]

    class TripWithAtLeastOneBicycleSpace(Trip):
        comment = [locstr(BIKES_ALLOWED_1_DEF, "en")]
        equivalent_to = [
            Trip &
            bikes_allowed.value(1)
        ]

    class TripWithNoBicycleSpaces(Trip):
        comment = [locstr(BIKES_ALLOWED_2_DEF, "en")]
        equivalent_to = [
            Trip &
            bikes_allowed.value(2)
        ]

    # cars_allowed

    class TripWithNoCarsAllowedInformation(Trip):
        comment = [locstr(CARS_ALLOWED_0_DEF, "en")]
        equivalent_to = [
            Trip &
            (
                cars_allowed.value(0) |
                cars_allowed.exactly(0)
            )
        ]

    class TripWithAtLeastOneCarSpace(Trip):
        comment = [locstr(CARS_ALLOWED_1_DEF, "en")]
        equivalent_to = [
            Trip &
            cars_allowed.value(1)
        ]

    class TripWithNoCarSpaces(Trip):
        comment = [locstr(CARS_ALLOWED_2_DEF, "en")]
        equivalent_to = [
            Trip &
            cars_allowed.value(2)
        ]