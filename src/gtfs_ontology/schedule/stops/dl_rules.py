from gtfs_ontology.schedule import *
from gtfs_ontology.schedule.records.generate import Stop
from gtfs_ontology.schedule.stops.generate import *
from gtfs_ontology.schedule.term_definitions.generate import Record

with gtfs:

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

    class StopOrPlatform(Stop):
        comment = [locstr(STOP_OR_PLATFORM_DEF, "en")]

    class StopLocation(StopOrPlatform):
        comment = [locstr(STOP_LOCATION_DEF, "en")]

    class Platform(StopOrPlatform):
        comment = [locstr(PLATFORM_DEF, "en")]

    class Station(Stop):
        comment = [locstr(STATION_DEF, "en")]

    class EntranceOrExit(Stop):
        comment = [locstr(ENTRANCE_OR_EXIT_DEF, "en")]

    class GenericNode(Stop):
        comment = [locstr(GENERIC_NODE_DEF, "en")]

    class BoardingArea(Stop):
        comment = [locstr(BOARDING_AREA_DEF, "en")]

    class ParentlessStop(Stop):
        comment = [locstr(PARENTLESS_STOP_DEF, "en")]

    class ChildStop(Stop):
        comment = [locstr(CHILD_STOP_DEF, "en")]

    AllDisjoint([StopLocation, Platform, Station, EntranceOrExit, GenericNode, BoardingArea])

    AllDisjoint([ParentlessStop, ChildStop])

    ChildStop.equivalent_to.append(
        Stop &
        parent_station.exactly(1)
    )

    ParentlessStop.equivalent_to.append(
        Stop &
        parent_station.exactly(0)
    )

    StopOrPlatform.equivalent_to.append(
        Stop &
        (
            location_type.value(0) |
            location_type.exactly(0)
        )
    )

    StopLocation.equivalent_to.append(
        StopOrPlatform &
        ParentlessStop
    )

    Platform.equivalent_to.append(
        StopOrPlatform &
        ChildStop
    )

    Station.equivalent_to.append(
        Stop &
        location_type.value(2)
    )

    EntranceOrExit.equivalent_to.append(
        Stop &
        location_type.value(2)
    )

    GenericNode.equivalent_to.append(
        Stop &
        location_type.value(3)
    )

    BoardingArea.equivalent_to.append(
        Stop &
        location_type.value(4)
    )

    StopOrPlatform.is_a.append(
        stop_name.exactly(1) &
        stop_lat.exactly(1) &
        stop_lon.exactly(1)
    )

    Station.is_a.append(
        stop_name.exactly(1) &
        stop_lat.exactly(1) &
        stop_lon.exactly(1) &
        parent_station.exactly(0)
    )

    EntranceOrExit.is_a.append(
        stop_name.exactly(1) &
        stop_lat.exactly(1) &
        stop_lon.exactly(1) &
        parent_station.exactly(1)
    )

    GenericNode.is_a.append(
        parent_station.exactly(1)
    )

    BoardingArea.is_a.append(
        parent_station.exactly(1)
    )

    # wheelchair_boarding

    class RecordWithAccessibilityInformation(Record):
        comment = [locstr(RECORD_WITH_ACCESSIBILITY_DEF, "en")]

    class StopWithNoAccessibilityInformation(ParentlessStop, RecordWithAccessibilityInformation):
        comment = [locstr(WHEELCHAIR_BOARDING_PARENTLESS_STOP_0_DEF, "en")]

    class StopWithPartialWheelchairAccessibility(ParentlessStop, RecordWithAccessibilityInformation):
        comment = [locstr(WHEELCHAIR_BOARDING_PARENTLESS_STOP_1_DEF, "en")]

    class StopWithNoWheelchairAccessibility(ParentlessStop, RecordWithAccessibilityInformation):
        comment = [locstr(WHEELCHAIR_BOARDING_PARENTLESS_STOP_2_DEF, "en")]


    class StopInheritingAccessibilityFromStation(ChildStop, RecordWithAccessibilityInformation):
        comment = [locstr(WHEELCHAIR_BOARDING_CHILD_STOP_0_DEF, "en")]


    class StopWithAccessiblePathFromOutsideStation(ChildStop, RecordWithAccessibilityInformation):
        comment = [locstr(WHEELCHAIR_BOARDING_CHILD_STOP_1_DEF, "en")]


    class StopWithNoAccessiblePathFromOutsideStation(ChildStop, RecordWithAccessibilityInformation):
        comment = [locstr(WHEELCHAIR_BOARDING_CHILD_STOP_2_DEF, "en")]


    class EntranceInheritingAccessibilityFromStation(EntranceOrExit, RecordWithAccessibilityInformation):
        comment = [locstr(WHEELCHAIR_BOARDING_ENTRANCEEXIT_0_DEF, "en")]


    class WheelchairAccessibleEntrance(EntranceOrExit, RecordWithAccessibilityInformation):
        comment = [locstr(WHEELCHAIR_BOARDING_ENTRANCEEXIT_1_DEF, "en")]


    class EntranceWithNoAccessiblePathToPlatforms(EntranceOrExit, RecordWithAccessibilityInformation):
        comment = [locstr(WHEELCHAIR_BOARDING_ENTRANCEEXIT_2_DEF, "en")]


    StopWithNoAccessibilityInformation.equivalent_to.append(
        ParentlessStop &
        (
            wheelchair_boarding.value(0) |
            wheelchair_boarding.exactly(0)
        )
    )

    StopWithPartialWheelchairAccessibility.equivalent_to.append(
        ParentlessStop &
        wheelchair_boarding.value(1)
    )

    StopWithNoWheelchairAccessibility.equivalent_to.append(
        ParentlessStop &
        wheelchair_boarding.value(2)
    )

    StopInheritingAccessibilityFromStation.equivalent_to.append(
        ChildStop &
        (
            wheelchair_boarding.value(0) |
            wheelchair_boarding.exactly(0)
        )
    )

    StopWithAccessiblePathFromOutsideStation.equivalent_to.append(
        ChildStop &
        wheelchair_boarding.value(1)
    )

    StopWithNoAccessiblePathFromOutsideStation.equivalent_to.append(
        ChildStop &
        wheelchair_boarding.value(2)
    )

    EntranceInheritingAccessibilityFromStation.equivalent_to.append(
        EntranceOrExit &
        (
            wheelchair_boarding.value(0) |
            wheelchair_boarding.exactly(0)
        )
    )

    WheelchairAccessibleEntrance.equivalent_to.append(
        EntranceOrExit &
        wheelchair_boarding.value(1)
    )

    EntranceWithNoAccessiblePathToPlatforms.equivalent_to.append(
        EntranceOrExit &
        wheelchair_boarding.value(1)
    )

    # stop_access
    class StopWithStopAccessInformation(Stop):
        comment = [locstr(STOP_ACCESS_DEF, "en")]

    class StopAccessibleViaStationOnly(StopOrPlatform):
        comment = [locstr(STOP_ACCESS_0_DEF, "en")]

    class StopDirectlyAccessibleFromStreet(StopOrPlatform):
        comment = [locstr(STOP_ACCESS_1_DEF, "en")]


    StopAccessibleViaStationOnly.equivalent_to.append(
        StopOrPlatform &
        stop_access.value(0)
    )

    StopDirectlyAccessibleFromStreet.equivalent_to.append(
        StopOrPlatform &
        stop_access.value(1)
    )

    Station.is_a.append(
        stop_access.exactly(0)
    )

    EntranceOrExit.is_a.append(
        stop_access.exactly(0)
    )

    GenericNode.is_a.append(
        stop_access.exactly(0)
    )

    BoardingArea.is_a.append(
        stop_access.exactly(0)
    )

    ParentlessStop.is_a.append(
        stop_access.exactly(0)
    )