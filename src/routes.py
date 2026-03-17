from core import *

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

    class RouteTypeDatatypeDescription(Thing):
        pass


    class RouteTypeDatatypeDescription0(RouteTypeDatatypeDescription):
        comment = "Tram, Streetcar, Light rail. Any light rail or street level system within a metropolitan area."


    class RouteTypeDatatypeDescription1(RouteTypeDatatypeDescription):
        comment = "Subway, Metro. Any underground rail system within a metropolitan area."


    class RouteTypeDatatypeDescription2(RouteTypeDatatypeDescription):
        comment = "Rail. Used for intercity or long-distance travel."


    class RouteTypeDatatypeDescription3(RouteTypeDatatypeDescription):
        comment = "Bus. Used for short- and long-distance bus routes."


    class RouteTypeDatatypeDescription4(RouteTypeDatatypeDescription):
        comment = "Ferry. Used for short- and long-distance boat service."


    class RouteTypeDatatypeDescription5(RouteTypeDatatypeDescription):
        comment = "Cable tram. Used for street-level rail cars where the cable runs beneath the vehicle (e.g., cable car in San Francisco)."


    class RouteTypeDatatypeDescription6(RouteTypeDatatypeDescription):
        comment = "Aerial lift, suspended cable car (e.g., gondola lift, aerial tramway). Cable transport where cabins, cars, gondolas or open chairs are suspended by means of one or more cables."


    class RouteTypeDatatypeDescription7(RouteTypeDatatypeDescription):
        comment = "Funicular. Any rail system designed for steep inclines."


    class RouteTypeDatatypeDescription11(RouteTypeDatatypeDescription):
        comment = "Trolleybus. Electric buses that draw power from overhead wires using poles."


    class RouteTypeDatatypeDescription12(RouteTypeDatatypeDescription):
        comment = "Monorail. Railway in which the track consists of a single rail or a beam."


    class ContinuousPickupDatatypeDescription(Thing):
        pass

    class ContinuousPickupDatatypeDescription0(ContinuousPickupDatatypeDescription):
        comment = "Continuous stopping pickup."

    class ContinuousPickupDatatypeDescription1(ContinuousPickupDatatypeDescription):
        comment = "No continuous stopping pickup."

    class ContinuousPickupDatatypeDescription2(ContinuousPickupDatatypeDescription):
        comment = "Must phone agency to arrange continuous stopping pickup."

    class ContinuousPickupDatatypeDescription3(ContinuousPickupDatatypeDescription):
        comment = "Must coordinate with driver to arrange continuous stopping pickup."


    class ContinuousDropOffDatatypeDescription(Thing):
        pass

    class ContinuousDropOffDatatypeDescription0(ContinuousDropOffDatatypeDescription):
        comment = "Continuous stopping drop off."

    class ContinuousDropOffDatatypeDescription1(ContinuousDropOffDatatypeDescription):
        comment = "No continuous stopping drop off."

    class ContinuousDropOffDatatypeDescription2(ContinuousDropOffDatatypeDescription):
        comment = "Must phone agency to arrange continuous stopping drop off."

    class ContinuousDropOffDatatypeDescription3(ContinuousDropOffDatatypeDescription):
        comment = "Must coordinate with driver to arrange continuous stopping drop off. "

    class CEMVSupportDatatypeDescriptionRoute(Thing):
        pass

    class CEMVSupportDatatypeDescriptionRoute0(CEMVSupportDatatypeDescriptionRoute):
        comment = "No cEMV information for trips associated with this route."

    class CEMVSupportDatatypeDescriptionRoute1(CEMVSupportDatatypeDescriptionRoute):
        comment = "Riders may use cEMVs as fare media for trips associated with this route. "

    class CEMVSupportDatatypeDescriptionRoute2(CEMVSupportDatatypeDescriptionRoute):
        comment = "cEMVs are not supported as fare media for trips associated with this route."

    # endregion

    # region Data Properties

    class route_id(FieldValue, FunctionalProperty):
        comment = "Identifies a route."
        domain = [Route]
        range = [str]

    # TODO This is a problem because it is already defined. Work out a way around this!
#     class agency_id(FieldValue, FunctionalProperty):
#         comment = """
# Agency for the specified route.
#
# Conditionally Required:
# - Required if multiple agencies are defined in agency.txt.
# - Recommended otherwise."""
#         domain = [Route]
#         range = [str]

    class route_short_name(FieldValue, FunctionalProperty):
        comment = """
Short name of a route. Often a short, abstract identifier (e.g., "32", "100X", "Green") that riders use to identify a route. Both route_short_name and route_long_name may be defined.

Conditionally Required:
- Required if routes.route_long_name is empty.
- Recommended if there is a brief service designation. This should be the commonly-known passenger name of the service, and should be no longer than 12 characters."""
        domain = [Route]
        range = [str]

    class route_long_name(FieldValue, FunctionalProperty):
        comment = """
Full name of a route. This name is generally more descriptive than the route_short_name and often includes the route's destination or stop. Both route_short_name and route_long_name may be defined.

Conditionally Required:
- Required if routes.route_short_name is empty.
- Optional otherwise."""
        domain = [Route]
        range = [str]

    class route_desc(FieldValue, FunctionalProperty):
        comment = """
 	Description of a route that provides useful, quality information. Should not be a duplicate of route_short_name or route_long_name. """
        domain = [Route]
        range = [str]

    class route_type(FieldValue, FunctionalProperty):
        comment = "Indicates the type of transportation used on a route."
        domain = [Route]
        range = [RouteTypeDatatype]

    class route_url(FieldValue, FunctionalProperty):
        comment = "URL of a web page about the particular route. Should be different from the agency.agency_url value."
        domain = [Route]
        range = [str]

    class route_color(FieldValue, FunctionalProperty):
        comment = "Route color designation that matches public facing material. Defaults to white (FFFFFF) when omitted or left empty. The color difference between route_color and route_text_color should provide sufficient contrast when viewed on a black and white screen."
        domain = [Route]
        range = [Color]

    class route_text_color(FieldValue, FunctionalProperty):
        comment = "Legible color to use for text drawn against a background of route_color. Defaults to black (000000) when omitted or left empty. The color difference between route_color and route_text_color should provide sufficient contrast when viewed on a black and white screen."
        domain = [Route]
        range = [Color]

    class route_sort_order(FieldValue, FunctionalProperty):
        comment = "Orders the routes in a way which is ideal for presentation to customers. Routes with smaller route_sort_order values should be displayed first."
        domain = [Route]
        range = [NonNegativeInteger]

    class continuous_pickup(FieldValue, FunctionalProperty):
        comment = "Indicates that the rider can board the transit vehicle at any point along the vehicle’s travel path as described by shapes.txt, on every trip of the route."
        domain = [Route]
        range = [ContinuousPickupDatatype]

    class continuous_drop_off(FieldValue, FunctionalProperty):
        comment = "Indicates that the rider can alight from the transit vehicle at any point along the vehicle’s travel path as described by shapes.txt, on every trip of the route."
        domain = [Route]
        range = [ContinuousDropOffDatatype]

    class network_id(FieldValue, FunctionalProperty):
        comment = "Identifies a group of routes. Multiple rows in routes.txt may have the same network_id."
        domain = [Route]
        range = [str]

    class cemv_support_routes(FieldValue, FunctionalProperty):
        comment = """
Indicates if riders can access a transit service (i.e., trip) associated with this route by using a contactless EMV (Europay, Mastercard, and Visa) card or mobile device as fare media at a fare validator (such as in pay-as-you-go or open-loop systems). This field does not indicate that cEMV can be used to purchase other fare products or to add value to another fare media.

Support for cEMVs should only be indicated if all services under this route are accessible with the use of cEMV cards or mobile devices as fare media."""
        domain = [Route]
        range = [CEMVSupportDatatype]

    # endregion