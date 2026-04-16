ROUTE_ID_DEF = """
Identifies a route.
"""

AGENCY_ID_DEF = """
When used on Route: Agency for the specified route.
"""

ROUTE_SHORT_NAME_DEF = """
Short name of a route. Often a short, abstract identifier (e.g., "32", "100X", "Green") that riders use to identify a route. Both route_short_name and route_long_name may be defined.
"""

ROUTE_LONG_NAME_DEF = """
Full name of a route. This name is generally more descriptive than the route_short_name and often includes the route's destination or stop. Both route_short_name and route_long_name may be defined.
"""

ROUTE_DESC_DEF = """
Description of a route that provides useful, quality information. Should not be a duplicate of route_short_name or route_long_name. 
"""

ROUTE_TYPE_DEF = """
Indicates the type of transportation used on a route. Valid options are:

0 - Tram, Streetcar, Light rail. Any light rail or street level system within a metropolitan area.
1 - Subway, Metro. Any underground rail system within a metropolitan area.
2 - Rail. Used for intercity or long-distance travel.
3 - Bus. Used for short- and long-distance bus routes.
4 - Ferry. Used for short- and long-distance boat service.
5 - Cable tram. Used for street-level rail cars where the cable runs beneath the vehicle (e.g., cable car in San Francisco).
6 - Aerial lift, suspended cable car (e.g., gondola lift, aerial tramway). Cable transport where cabins, cars, gondolas or open chairs are suspended by means of one or more cables.
7 - Funicular. Any rail system designed for steep inclines.
11 - Trolleybus. Electric buses that draw power from overhead wires using poles.
12 - Monorail. Railway in which the track consists of a single rail or a beam.
"""

ROUTE_URL_DEF = """
URL of a web page about the particular route. Should be different from the agency.agency_url value.
"""

ROUTE_COLOR_DEF = """
Route color designation that matches public facing material. Defaults to white (FFFFFF) when omitted or left empty. The color difference between route_color and route_text_color should provide sufficient contrast when viewed on a black and white screen.
"""

ROUTE_TEXT_COLOR_DEF = """
Legible color to use for text drawn against a background of route_color. Defaults to black (000000) when omitted or left empty. The color difference between route_color and route_text_color should provide sufficient contrast when viewed on a black and white screen.
"""

ROUTE_SORT_ORDER_DEF = """
Orders the routes in a way which is ideal for presentation to customers. Routes with smaller route_sort_order values should be displayed first.
"""

CONTINUOUS_PICKUP_DEF = """
Indicates that the rider can board the transit vehicle at any point along the vehicle’s travel path as described by shapes.txt, on every trip of the route. Valid options are:

0 - Continuous stopping pickup.
1 or empty - No continuous stopping pickup.
2 - Must phone agency to arrange continuous stopping pickup.
3 - Must coordinate with driver to arrange continuous stopping pickup.

Values for routes.continuous_pickup may be overridden by defining values in stop_times.continuous_pickup for specific stop_times along the route. 
"""

CONTINUOUS_DROPOFF_DEF = """
Indicates that the rider can alight from the transit vehicle at any point along the vehicle’s travel path as described by shapes.txt, on every trip of the route. Valid options are:

0 - Continuous stopping drop off.
1 or empty - No continuous stopping drop off.
2 - Must phone agency to arrange continuous stopping drop off.
3 - Must coordinate with driver to arrange continuous stopping drop off.

Values for routes.continuous_drop_off may be overridden by defining values in stop_times.continuous_drop_off for specific stop_times along the route. 
"""

NETWORK_ID_DEF = """
Identifies a group of routes. Multiple rows in routes.txt may have the same network_id.
"""

CEMV_SUPPORT_DEF = """
When used on Route:

Indicates if riders can access a transit service (i.e., trip) associated with this route by using a contactless EMV (Europay, Mastercard, and Visa) card or mobile device as fare media at a fare validator (such as in pay-as-you-go or open-loop systems). This field does not indicate that cEMV can be used to purchase other fare products or to add value to another fare media.

Support for cEMVs should only be indicated if all services under this route are accessible with the use of cEMV cards or mobile devices as fare media.

Valid options are:

0 or empty - No cEMV information for trips associated with this route.
1 - Riders may use cEMVs as fare media for trips associated with this route.
2 - cEMVs are not supported as fare media for trips associated with this route.

If both agency.cemv_support and routes.cemv_support are provided for the same service, the value in routes.cemv_support shall take precedence.

This field is independent of all other fare-related files and may be used separately. If there is conflicting information between this field and any fare-related file (such as fare_media.txt, fare_products.txt, or fare_leg_rules.txt), the information in those files shall take precedence over agency.cemv_support.
"""