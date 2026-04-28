from gtfs_ontology.schedule import *
from gtfs_ontology.schedule.agencies.generate import agency_id, cemv_support
from gtfs_ontology.schedule.field_types.generate import text, enum, url, color, \
    num_int, id
from gtfs_ontology.schedule.records.generate import Route
from gtfs_ontology.schedule.routes.definitions import *

ROUTES_URL = "https://gtfs.org/documentation/schedule/reference/#routestxt"

with gtfs:

    # region Datatypes

    class route_type_enum(Datatype):
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

    class continuous_pickup_enum(Datatype):
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

    class continuous_drop_off_enum(Datatype):
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

    class route_id(id):
        comment = [locstr(ROUTE_ID_DEF, "en")]
        domain = [Route]
        seeAlso = [ROUTES_URL]

    agency_id.domain.append(Route)
    agency_id.comment.append(locstr(AGENCY_ID_DEF, "en"))
    agency_id.seeAlso.append(ROUTES_URL)

    class route_short_name(text):
        comment = [locstr(ROUTE_SHORT_NAME_DEF, "en")]
        domain = [Route]
        seeAlso = [ROUTES_URL]

    class route_long_name(text):
        comment = [locstr(ROUTE_LONG_NAME_DEF, "en")]
        domain = [Route]
        seeAlso = [ROUTES_URL]

    class route_desc(text):
        comment = [locstr(ROUTE_DESC_DEF, "en")]
        domain = [Route]
        seeAlso = [ROUTES_URL]

    class route_type(enum):
        comment = [locstr(ROUTE_TYPE_DEF, "en")]
        domain = [Route]
        range = [route_type_enum]
        seeAlso = [ROUTES_URL]
        relatedMatch = [gtfs_linked.RouteType]

    class route_url(url):
        comment = [locstr(ROUTE_URL_DEF, "en")]
        domain = [Route]
        seeAlso = [ROUTES_URL]

    class route_color(color):
        comment = [locstr(ROUTE_COLOR_DEF, "en")]
        domain = [Route]
        seeAlso = [ROUTES_URL]

    class route_text_color(color):
        comment = [locstr(ROUTE_TEXT_COLOR_DEF, "en")]
        domain = [Route]
        seeAlso = [ROUTES_URL]

    class route_sort_order(num_int):
        comment = [locstr(ROUTE_SORT_ORDER_DEF, "en")]
        domain = [Route]
        seeAlso = [ROUTES_URL]

    class continuous_pickup(enum):
        comment = [locstr(CONTINUOUS_PICKUP_DEF, "en")]
        domain = [Route]
        range = [continuous_pickup_enum]
        seeAlso = [ROUTES_URL]

    class continuous_drop_off(enum):
        comment = [locstr(CONTINUOUS_DROPOFF_DEF, "en")]
        domain = [Route]
        range = [continuous_drop_off_enum]
        seeAlso = [ROUTES_URL]

    class network_id(id):
        comment = [locstr(NETWORK_ID_DEF, "en")]
        domain = [Route]
        seeAlso = [ROUTES_URL]

    cemv_support.domain.append(Route)
    cemv_support.comment.append(locstr(CEMV_SUPPORT_DEF, "en"))
    cemv_support.seeAlso.append(ROUTES_URL)

    # endregion