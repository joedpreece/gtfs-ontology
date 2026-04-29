from gtfs_ontology.schedule import *
from gtfs_ontology.schedule.core import isRecordOf, isFileOf, hasFile, hasRecord
from gtfs_ontology.schedule.files.dl_rules import AgencyFileWithMultipleAgencies
from gtfs_ontology.schedule.files.generate import RouteFile, StopTimeFile
from gtfs_ontology.schedule.records.generate import StopTime
from gtfs_ontology.schedule.routes.generate import *
from gtfs_ontology.schedule.stop_times.generate import start_pickup_drop_off_window, \
    end_pickup_drop_off_window
from gtfs_ontology.schedule.term_definitions.generate import Dataset

with gtfs:

    # Requirements

    Route.is_a.append(
        route_id.exactly(1) &
        agency_id.max(1) &
        route_short_name.max(1) &
        route_long_name.max(1) &
        route_desc.max(1) &
        route_type.exactly(1) &
        route_url.max(1) &
        route_color.max(1) &
        route_text_color.max(1) &
        route_sort_order.max(1) &
        continuous_pickup.max(1) &
        continuous_drop_off.max(1) &
        network_id.max(1) &
        cemv_support.max(1)
    )

    class RouteWithAgencyID(Route):
        equivalent_to = [
            isRecordOf.only(
                RouteFile &
                isFileOf.only(
                    Dataset &
                    hasFile.some(AgencyFileWithMultipleAgencies)
                )
            )
        ]
        is_a = [
            agency_id.exactly(1)
        ]

    # route_short_name

    class RouteWithNoLongName(Route):
        equivalent_to = [
            route_long_name.exactly(0)
        ]
        is_a = [
            route_short_name.exactly(1)
        ]

    # route_long_name

    class RouteWithNoShortName(Route):
        equivalent_to = [
            route_short_name.exactly(0)
        ]
        is_a = [
            route_long_name.exactly(1)
        ]

    class TramRoute(Route):
        comment = [locstr(TRAM_ROUTE_DEF, "en")]
        equivalent_to = [
            route_type.value(0)
        ]
        broadMatch = [gtfs_linked.RouteType]

    class SubwayRoute(Route):
        comment = [locstr(SUBWAY_ROUTE_DEF, "en")]
        equivalent_to = [
            route_type.value(1)
        ]
        broadMatch = [gtfs_linked.RouteType]

    class RailRoute(Route):
        comment = [locstr(RAIL_DEF, "en")]
        equivalent_to = [
            route_type.value(2)
        ]
        broadMatch = [gtfs_linked.RouteType]

    class BusRoute(Route):
        comment = [locstr(BUS_DEF, "en")]
        equivalent_to = [
            route_type.value(3)
        ]
        broadMatch = [gtfs_linked.RouteType]

    class FerryRoute(Route):
        comment = [locstr(FERRY_DEF, "en")]
        equivalent_to = [
            route_type.value(4)
        ]
        broadMatch = [gtfs_linked.RouteType]

    class CableTramRoute(Route):
        comment = [locstr(CABLE_TRAM_DEF, "en")]
        equivalent_to = [
            route_type.value(5)
        ]
        broadMatch = [gtfs_linked.RouteType]

    class AerialLiftRoute(Route):
        comment = [locstr(AERIAL_LIFT_DEF, "en")]
        equivalent_to = [
            route_type.value(6)
        ]
        broadMatch = [gtfs_linked.RouteType]

    class FunicularRoute(Route):
        comment = [locstr(FUNICULAR_DEF, "en")]
        equivalent_to = [
            route_type.value(7)
        ]
        broadMatch = [gtfs_linked.RouteType]

    class TrolleybusRoute(Route):
        comment = [locstr(TROLLEYBUS_DEF, "en")]
        equivalent_to = [
            route_type.value(11)
        ]
        broadMatch = [gtfs_linked.RouteType]

    class MonorailRoute(Route):
        comment = [locstr(MONORAIL_DEF, "en")]
        equivalent_to = [
            route_type.value(12)
        ]
        broadMatch = [gtfs_linked.RouteType]

    class RouteWithContinuousPickup(Route):
        equivalent_to = [
            isFileOf.only(
                RouteFile &
                isRecordOf.only(
                    Dataset
                    & hasFile.some(
                        StopTimeFile &
                        hasRecord.some(
                            StopTime &
                            (
                                start_pickup_drop_off_window.exactly(1) |
                                end_pickup_drop_off_window.exactly(1)
                            )
                        )
                    )
                )
            )
        ]
        is_a = [
            continuous_pickup.exactly(1)
        ]

    class RouteWithContinuousDropOff(Route):
        equivalent_to = [
            isFileOf.only(
                RouteFile &
                isRecordOf.only(
                    Dataset
                    & hasFile.some(
                        StopTimeFile &
                        hasRecord.some(
                            StopTime &
                            (
                                start_pickup_drop_off_window.exactly(1) |
                                end_pickup_drop_off_window.exactly(1)
                            )
                        )
                    )
                )
            )
        ]
        is_a = [
            continuous_drop_off.exactly(1)
        ]

    ## TODO: Encode the conditionally forbidden

    # network_id

    class RouteWithNoCEMVInformation(Route):
        comment = [locstr(CEMV_NO_INFORMATION, "en")]
        equivalent_to = [
            cemv_support.value(0)
        ]

    class RouteWithCEMVSupport(Route):
        comment = [locstr(CEMV_SUPPORTED, "en")]
        equivalent_to = [
            cemv_support.value(1)
        ]

    class RouteWithNoCEMVSupport(Route):
        comment = [locstr(CEMV_NOT_SUPPORTED, "en")]
        equivalent_to = [
            cemv_support.value(2)
        ]