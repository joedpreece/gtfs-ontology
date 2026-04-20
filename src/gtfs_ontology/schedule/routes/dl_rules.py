from gtfs_ontology.schedule import *
from gtfs_ontology.schedule.records.generate import StopTime
from gtfs_ontology.schedule.routes.generate import *

with gtfs:

    # route_id

    Route.is_a.append(
        route_id.exactly(1)
    )

    # agency_id

    Route.is_a.append(
        agency_id.max(1)
    )

    # route_short_name

    class RouteWithNoLongName(Route):
        equivalent_to = [
            Route &
            route_long_name.exactly(0)
        ]

    Route.is_a.append(
        route_short_name.max(1)
    )

    RouteWithNoLongName.is_a.append(
        route_short_name.exactly(1)
    )

    # route_long_name

    class RouteWithNoShortName(Route):
        equivalent_to = [
            Route &
            route_short_name.exactly(0)
        ]


    Route.is_a.append(
        route_long_name.max(1)
    )

    RouteWithNoShortName.is_a.append(
        route_long_name.exactly(1)
    )

    # route_desc

    Route.is_a.append(
        route_desc.max(1)
    )

    # route_type

    Route.is_a.append(
        route_type.exactly(1)
    )

    class TramRoute(Route):
        comment = [locstr(TRAM_ROUTE_DEF, "en")]
        equivalent_to = [
            Route &
            route_type.value(0)
        ]

    class SubwayRoute(Route):
        comment = [locstr(SUBWAY_ROUTE_DEF, "en")]
        equivalent_to = [
            Route &
            route_type.value(1)
        ]

    class RailRoute(Route):
        comment = [locstr(RAIL_DEF, "en")]
        equivalent_to = [
            Route &
            route_type.value(2)
        ]

    class BusRoute(Route):
        comment = [locstr(BUS_DEF, "en")]
        equivalent_to = [
            Route &
            route_type.value(3)
        ]

    class FerryRoute(Route):
        comment = [locstr(FERRY_DEF, "en")]
        equivalent_to = [
            Route &
            route_type.value(4)
        ]

    class CableTramRoute(Route):
        comment = [locstr(CABLE_TRAM_DEF, "en")]
        equivalent_to = [
            Route &
            route_type.value(5)
        ]

    class AerialLiftRoute(Route):
        comment = [locstr(AERIAL_LIFT_DEF, "en")]
        equivalent_to = [
            Route &
            route_type.value(6)
        ]

    class FunicularRoute(Route):
        comment = [locstr(FUNICULAR_DEF, "en")]
        equivalent_to = [
            Route &
            route_type.value(7)
        ]

    class TrolleybusRoute(Route):
        comment = [locstr(TROLLEYBUS_DEF, "en")]
        equivalent_to = [
            Route &
            route_type.value(11)
        ]

    class MonorailRoute(Route):
        comment = [locstr(MONORAIL_DEF, "en")]
        equivalent_to = [
            Route &
            route_type.value(12)
        ]

    # route_url

    Route.is_a.append(
        route_url.max(1)
    )

    # route_color

    Route.is_a.append(
        route_color.max(1)
    )

    # route_text_color

    Route.is_a.append(
        route_text_color.max(1)
    )

    # route_sort_order

    Route.is_a.append(
        route_sort_order.max(1)
    )

    # continuous_pickup

    Route.is_a.append(
        continuous_pickup.max(1)
    )

    ## TODO: Encode the conditionally forbidden
    class StopTimeWithPickupDropOffWindow(StopTime):
        pass

    # continuous_drop_off

    Route.is_a.append(
        continuous_drop_off.max(1)
    )

    ## TODO: Encode the conditionally forbidden

    # network_id

    Route.is_a.append(
        network_id.max(1)
    )

    # cemv_support

    Route.is_a.append(
        cemv_support.max(1)
    )

    class RouteWithNoCEMVInformation(Route):
        comment = [locstr(CEMV_NO_INFORMATION, "en")]
        equivalent_to = [
            Route &
            cemv_support.value(0)
        ]

    class RouteWithCEMVSupport(Route):
        comment = [locstr(CEMV_SUPPORTED, "en")]
        equivalent_to = [
            Route &
            cemv_support.value(1)
        ]

    class RouteWithNoCEMVSupport(Route):
        comment = [locstr(CEMV_NOT_SUPPORTED, "en")]
        equivalent_to = [
            Route &
            cemv_support.value(2)
        ]