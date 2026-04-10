from gtfs_ontology.schedule.agencies.generate import CEMVSupportDatatypeDescription0, \
    CEMVSupportDatatypeDescription1, CEMVSupportDatatypeDescription2, agency_id, \
    cemv_support
from gtfs_ontology.schedule.core import *
from gtfs_ontology.schedule.routes.definitions import *


with gtfs:

    # region Datatypes

    class RouteTypeDatatype(Datatype):
        equivalent_to = [
            OneOf(
                [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    11,
                    12,
                ]
            )
        ]

    class ContinuousPickupDatatype(Datatype):
        equivalent_to = [
            OneOf(
                [
                    0,
                    1,
                    2,
                    3,
                ]
            )
        ]

    class ContinuousDropOffDatatype(Datatype):
        equivalent_to = [
            OneOf(
                [
                    0,
                    1,
                    2,
                    3,
                ]
            )
        ]

    # endregion

    # region Classes

    class RouteTypeDatatypeDescription0(DatatypeDescription):
        comment = "Tram, Streetcar, Light rail. Any light rail or street level system within a metropolitan area."


    class RouteTypeDatatypeDescription1(DatatypeDescription):
        comment = "Subway, Metro. Any underground rail system within a metropolitan area."


    class RouteTypeDatatypeDescription2(DatatypeDescription):
        comment = "Rail. Used for intercity or long-distance travel."


    class RouteTypeDatatypeDescription3(DatatypeDescription):
        comment = "Bus. Used for short- and long-distance bus routes."


    class RouteTypeDatatypeDescription4(DatatypeDescription):
        comment = "Ferry. Used for short- and long-distance boat service."


    class RouteTypeDatatypeDescription5(DatatypeDescription):
        comment = "Cable tram. Used for street-level rail cars where the cable runs beneath the vehicle (e.g., cable car in San Francisco)."


    class RouteTypeDatatypeDescription6(DatatypeDescription):
        comment = "Aerial lift, suspended cable car (e.g., gondola lift, aerial tramway). Cable transport where cabins, cars, gondolas or open chairs are suspended by means of one or more cables."


    class RouteTypeDatatypeDescription7(DatatypeDescription):
        comment = "Funicular. Any rail system designed for steep inclines."


    class RouteTypeDatatypeDescription11(DatatypeDescription):
        comment = "Trolleybus. Electric buses that draw power from overhead wires using poles."


    class RouteTypeDatatypeDescription12(DatatypeDescription):
        comment = "Monorail. Railway in which the track consists of a single rail or a beam."


    class ContinuousPickupDatatypeDescription0(DatatypeDescription):
        comment = "Continuous stopping pickup."

    class ContinuousPickupDatatypeDescription1(DatatypeDescription):
        comment = "No continuous stopping pickup."

    class ContinuousPickupDatatypeDescription2(DatatypeDescription):
        comment = "Must phone agency to arrange continuous stopping pickup."

    class ContinuousPickupDatatypeDescription3(DatatypeDescription):
        comment = "Must coordinate with driver to arrange continuous stopping pickup."


    class ContinuousDropOffDatatypeDescription0(DatatypeDescription):
        comment = "Continuous stopping drop off."

    class ContinuousDropOffDatatypeDescription1(DatatypeDescription):
        comment = "No continuous stopping drop off."

    class ContinuousDropOffDatatypeDescription2(DatatypeDescription):
        comment = "Must phone agency to arrange continuous stopping drop off."

    class ContinuousDropOffDatatypeDescription3(DatatypeDescription):
        comment = "Must coordinate with driver to arrange continuous stopping drop off. "

    CEMVSupportDatatypeDescription0.comment.append(
        locstr("No cEMV information for trips associated with this route.", "en"))
    CEMVSupportDatatypeDescription1.comment.append(
        locstr("Riders may use cEMVs as fare media for trips associated with this route.", "en"))
    CEMVSupportDatatypeDescription2.comment.append(
        locstr("cEMVs are not supported as fare media for trips associated with this route.", "en"))

    # endregion

    # region Data Properties

    class route_id(id, FunctionalProperty):
        comment = [locstr(ROUTE_ID_DEF, "en")]
        domain = [Route]
        range = [str]

    agency_id.domain.append(Route)
    agency_id.comment.append(locstr(AGENCY_ID_DEF, "en"))

    class route_short_name(text, FunctionalProperty):
        comment = [locstr(ROUTE_SHORT_NAME_DEF, "en")]
        domain = [Route]

    class route_long_name(text, FunctionalProperty):
        comment = [locstr(ROUTE_LONG_NAME_DEF, "en")]
        domain = [Route]

    class route_desc(text, FunctionalProperty):
        comment = [locstr(ROUTE_DESC_DEF, "en")]
        domain = [Route]

    class route_type(enum, FunctionalProperty):
        comment = [locstr(ROUTE_TYPE_DEF, "en")]
        domain = [Route]
        range = [RouteTypeDatatype]

    class route_url(url_field, FunctionalProperty):
        comment = [locstr(ROUTE_URL_DEF, "en")]
        domain = [Route]

    class route_color(color, FunctionalProperty):
        comment = [locstr(ROUTE_COLOR_DEF, "en")]
        domain = [Route]

    class route_text_color(color, FunctionalProperty):
        comment = [locstr(ROUTE_TEXT_COLOR_DEF, "en")]
        domain = [Route]

    class route_sort_order(num_int, FunctionalProperty):
        comment = [locstr(ROUTE_SORT_ORDER_DEF, "en")]
        domain = [Route]
        range = [NonNegativeInteger]

    class continuous_pickup(enum, FunctionalProperty):
        comment = [locstr(CONTINUOUS_PICKUP_DEF, "en")]
        domain = [Route, StopTime]
        range = [ContinuousPickupDatatype]

    class continuous_drop_off(enum, FunctionalProperty):
        comment = [locstr(CONTINUOUS_DROPOFF_DEF, "en")]
        domain = [Route, StopTime]
        range = [ContinuousDropOffDatatype]

    class network_id(id, FunctionalProperty):
        comment = [locstr(NETWORK_ID_DEF, "en")]
        domain = [Route]

    cemv_support.domain.append(Route)
    cemv_support.comment.append(locstr(CEMV_SUPPORT_DEF, "en"))

    # endregion