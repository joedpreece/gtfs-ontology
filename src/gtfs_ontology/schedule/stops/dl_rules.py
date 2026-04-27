from gtfs_ontology.schedule import *
from gtfs_ontology.schedule.records.generate import Stop
from gtfs_ontology.schedule.stops.generate import *
from gtfs_ontology.schedule.term_definitions.generate import Record

with gtfs:

    # Requirements
    Stop.is_a.append(
        stop_id.exactly(1) &
        stop_code.max(1) &
        stop_name.max(1) &
        tts_stop_name.max(1) &
        stop_desc.max(1) &
        stop_lat.max(1) &
        stop_lon.max(1) &
        zone_id.max(1) &
        stop_url.max(1) &
        location_type.max(1) &
        parent_station.max(1) &
        stop_timezone.max(1) &
        wheelchair_boarding.max(1) &
        level_id.max(1) &
        platform_code.max(1) &
        stop_access.max(1)
    )

    class ParentlessStop(Stop):
        comment = [locstr(PARENTLESS_STOP_DEF, "en")]
        equivalent_to = [
            Stop &
            parent_station.exactly(0)
        ]

    class ChildStop(Stop):
        comment = [locstr(CHILD_STOP_DEF, "en")]
        equivalent_to = [
            Stop &
            parent_station.exactly(1)
        ]

    AllDisjoint([ParentlessStop, ChildStop])

    class StopOrPlatform(Stop):
        comment = [locstr(STOP_OR_PLATFORM_DEF, "en")]
        is_a = [
            stop_name.exactly(1) &
            stop_lat.exactly(1) &
            stop_lon.exactly(1)
        ]
        equivalent_to = [
            Stop &
            (
                location_type.value(0) |
                location_type.exactly(0)
            )
        ]

    class StopLocation(StopOrPlatform):
        comment = [locstr(STOP_LOCATION_DEF, "en")]
        equivalent_to = [
            StopOrPlatform &
            ParentlessStop
        ]

    class Platform(StopOrPlatform):
        comment = [locstr(PLATFORM_DEF, "en")]
        equivalent_to = [
            StopOrPlatform &
            ChildStop
        ]

    class Station(ParentlessStop):
        comment = [locstr(STATION_DEF, "en")]
        is_a = [
            stop_name.exactly(1) &
            stop_lat.exactly(1) &
            stop_lon.exactly(1)
        ]
        equivalent_to = [
            Stop &
            location_type.value(1)
        ]

    class EntranceOrExit(ChildStop):
        comment = [locstr(ENTRANCE_OR_EXIT_DEF, "en")]
        is_a = [
            stop_name.exactly(1) &
            stop_lat.exactly(1) &
            stop_lon.exactly(1)
        ]
        equivalent_to = [
            Stop &
            location_type.value(2)
        ]

    class GenericNode(ChildStop):
        comment = [locstr(GENERIC_NODE_DEF, "en")]
        equivalent_to = [
            Stop &
            location_type.value(3)
        ]

    class BoardingArea(ChildStop):
        comment = [locstr(BOARDING_AREA_DEF, "en")]
        equivalent_to = [
            Stop &
            location_type.value(4)
        ]

    AllDisjoint([StopLocation, Platform, Station, EntranceOrExit, GenericNode, BoardingArea])

    # wheelchair_boarding

    class RecordWithAccessibilityInformation(Record):
        comment = [locstr(RECORD_WITH_ACCESSIBILITY_DEF, "en")]

    class StopWithNoAccessibilityInformation(ParentlessStop, RecordWithAccessibilityInformation):
        comment = [locstr(WHEELCHAIR_BOARDING_PARENTLESS_STOP_0_DEF, "en")]
        equivalent_to = [
            ParentlessStop &
            (
                    wheelchair_boarding.value(0) |
                    wheelchair_boarding.exactly(0)
            )
        ]

    class StopWithPartialWheelchairAccessibility(ParentlessStop, RecordWithAccessibilityInformation):
        comment = [locstr(WHEELCHAIR_BOARDING_PARENTLESS_STOP_1_DEF, "en")]
        equivalent_to = [
            ParentlessStop &
            wheelchair_boarding.value(1)
        ]

    class StopWithNoWheelchairAccessibility(ParentlessStop, RecordWithAccessibilityInformation):
        comment = [locstr(WHEELCHAIR_BOARDING_PARENTLESS_STOP_2_DEF, "en")]
        equivalent_to = [
            ParentlessStop &
            wheelchair_boarding.value(2)
        ]


    class StopInheritingAccessibilityFromStation(ChildStop, RecordWithAccessibilityInformation):
        comment = [locstr(WHEELCHAIR_BOARDING_CHILD_STOP_0_DEF, "en")]
        equivalent_to = [
            ChildStop &
            (
                    wheelchair_boarding.value(0) |
                    wheelchair_boarding.exactly(0)
            )
        ]


    class StopWithAccessiblePathFromOutsideStation(ChildStop, RecordWithAccessibilityInformation):
        comment = [locstr(WHEELCHAIR_BOARDING_CHILD_STOP_1_DEF, "en")]
        equivalent_to = [
            ChildStop &
            wheelchair_boarding.value(1)
        ]


    class StopWithNoAccessiblePathFromOutsideStation(ChildStop, RecordWithAccessibilityInformation):
        comment = [locstr(WHEELCHAIR_BOARDING_CHILD_STOP_2_DEF, "en")]
        equivalent_to = [
            ChildStop &
            wheelchair_boarding.value(2)
        ]


    class EntranceInheritingAccessibilityFromStation(EntranceOrExit, RecordWithAccessibilityInformation):
        comment = [locstr(WHEELCHAIR_BOARDING_ENTRANCEEXIT_0_DEF, "en")]
        equivalent_to = [
            EntranceOrExit &
            (
                    wheelchair_boarding.value(0) |
                    wheelchair_boarding.exactly(0)
            )
        ]


    class WheelchairAccessibleEntrance(EntranceOrExit, RecordWithAccessibilityInformation):
        comment = [locstr(WHEELCHAIR_BOARDING_ENTRANCEEXIT_1_DEF, "en")]
        equivalent_to = [
            EntranceOrExit &
            wheelchair_boarding.value(1)
        ]


    class EntranceWithNoAccessiblePathToPlatforms(EntranceOrExit, RecordWithAccessibilityInformation):
        comment = [locstr(WHEELCHAIR_BOARDING_ENTRANCEEXIT_2_DEF, "en")]
        equivalent_to = [
            EntranceOrExit &
            wheelchair_boarding.value(2)
        ]

    # stop_access
    class StopWithStopAccessInformation(Stop):
        comment = [locstr(STOP_ACCESS_DEF, "en")]

    class StopAccessibleViaStationOnly(ChildStop, StopOrPlatform):
        comment = [locstr(STOP_ACCESS_0_DEF, "en")]
        equivalent_to = [
            stop_access.value(0)
        ]

    class StopDirectlyAccessibleFromStreet(ChildStop, StopOrPlatform):
        comment = [locstr(STOP_ACCESS_1_DEF, "en")]
        equivalent_to = [
            stop_access.value(1)
        ]