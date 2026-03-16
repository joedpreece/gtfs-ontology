from core import *

with gtfs:

    # region Datatypes

    class LocationTypeType(Datatype):
        equivalent_to = [
            OneOf(
                [
                    0,
                    1,
                    2,
                    3,
                    4,
                ]
            )
        ]

    class LocationTypeTypeDescription(Thing):
        pass

    # endregion

    # region Classes

    class StopLocation(LocationTypeTypeDescription):
        comment = "A location where passengers board or disembark from a transit vehicle."

    class Platform(LocationTypeTypeDescription):
        comment = "A location where passengers board or disembark from a transit vehicle. Is called a platform when defined within a parent_station."

    class Station(LocationTypeTypeDescription):
        comment = "A physical structure or area that contains one or more platform."

    class EntranceOrExit(LocationTypeTypeDescription):
        comment = "A location where passengers can enter or exit a station from the street. If an entrance/exit belongs to multiple stations, it may be linked by pathways to both, but the data provider must pick one of them as parent."

    class GenericNode(LocationTypeTypeDescription):
        comment = "A location within a station, not matching any other location_type, that may be used to link together pathways define in pathways.txt."

    class BoardingArea(LocationTypeTypeDescription):
        comment = "A specific location on a platform, where passengers can board and/or alight vehicles."

    class WheelchairBoardingType(Datatype):
        equivalent_to = [
            OneOf(
                [
                    0,
                    1,
                    2,
                ]
            )
        ]

    class WheelchairBoardingTypeDescription(Thing):
        pass

    class WheelchairBoardingParentlessStop(WheelchairBoardingTypeDescription):
        pass

    class WheelchairBoardingParentlessStop0(WheelchairBoardingParentlessStop):
        comment = "No accessibility information for the stop."

    class WheelchairBoardingParentlessStop1(WheelchairBoardingParentlessStop):
        comment = "Wheelchair boardings are possible from the stop."

    class WheelchairBoardingParentlessStop2(WheelchairBoardingParentlessStop):
        comment = "Wheelchair boarding is not possible at this stop."

    class WheelchairBoardingChildStop(WheelchairBoardingTypeDescription):
        pass

    class WheelchairBoardingChildStop0(WheelchairBoardingChildStop):
        comment = "Stop will inherit its wheelchair_boarding behavior from the parent station, if specified in the parent."

    class WheelchairBoardingChildStop1(WheelchairBoardingChildStop):
        comment = "There exists some accessible path from outside the station to the specific stop/platform."

    class WheelchairBoardingChildStop2(WheelchairBoardingChildStop):
        comment = "There exists no accessible path from outside the station to the specific stop/platform."

    class WheelchairBoardingEntranceExit(WheelchairBoardingTypeDescription):
        pass

    class WheelchairBoardingEntranceExit0(WheelchairBoardingEntranceExit):
        comment = "Station entrance will inherit its wheelchair_boarding behavior from the parent station, if specified for the parent."

    class WheelchairBoardingEntranceExit1(WheelchairBoardingEntranceExit):
        comment = "Station entrance is wheelchair accessible."

    class WheelchairBoardingEntranceExit2(WheelchairBoardingEntranceExit):
        comment = "No accessible path from station entrance to stops/platforms."

    class StopAccessType(Datatype):
        equivalent_to = [
            OneOf(
                [
                    0,
                    1,
                ]
            )
        ]

    class StopAccessTypeDescription(Thing):
        pass

    class StopAccessTypeDescription0(StopAccessTypeDescription):
        comment = "The stop/platform cannot be directly accessed from the street network. It must be accessed from a station entrance if there is one defined for the station, otherwise the station itself. If there are pathways defined for the station, they must be used to access the stop/platform."

    class StopAccessTypeDescription1(StopAccessTypeDescription):
        comment = "Consuming applications should generate directions for access directly to the stop, independent of any entrances or pathways of the parent station."

    # region Data Properties

    class stop_id(FieldValue, FunctionalProperty):
        comment = """
Identifies a location: stop/platform, station, entrance/exit, generic node or boarding area (see location_type).

ID must be unique across all stops.stop_id, locations.geojson id, and location_groups.location_group_id values.

Multiple routes may use the same stop_id.
"""
        domain = [Stop]
        range = [str]

    class stop_code(FieldValue, FunctionalProperty):
        comment = """
Short text or a number that identifies the location for riders. These codes are often used in phone-based transit information systems or printed on signage to make it easier for riders to get information for a particular location. The stop_code may be the same as stop_id if it is public facing. This field should be left empty for locations without a code presented to riders.
"""
        domain = [Stop]
        range = [str]

    class stop_name(FieldValue, FunctionalProperty):
        comment = """
Name of the location. The stop_name should match the agency's rider-facing name for the location as printed on a timetable, published online, or represented on signage. For translations into other languages, use translations.txt.

When the location is a boarding area (location_type=4), the stop_name should contains the name of the boarding area as displayed by the agency. It could be just one letter (like on some European intercity railway stations), or text like “Wheelchair boarding area” (NYC’s Subway) or “Head of short trains” (Paris’ RER).

Conditionally Required:
- Required for locations which are stops (location_type=0), stations (location_type=1) or entrances/exits (location_type=2).
- Optional for locations which are generic nodes (location_type=3) or boarding areas (location_type=4).
"""
        domain = [Stop]
        range = [str]

    class tts_stop_name(FieldValue, FunctionalProperty):
        comment = """
Readable version of the stop_name. See "Text-to-speech field" in the Term Definitions for more.
"""
        domain = [Stop]
        range = [str]

    class stop_desc(FieldValue, FunctionalProperty):
        comment = """
Description of the location that provides useful, quality information. Should not be a duplicate of stop_name.
"""
        domain = [Stop]
        range = [str]

    class stop_lat(FieldValue, FunctionalProperty):
        comment = """
Latitude of the location.

For stops/platforms (location_type=0) and boarding area (location_type=4), the coordinates must be the ones of the bus pole — if exists — and otherwise of where the travelers are boarding the vehicle (on the sidewalk or the platform, and not on the roadway or the track where the vehicle stops).

Conditionally Required:
- Required for locations which are stops (location_type=0), stations (location_type=1) or entrances/exits (location_type=2).
- Optional for locations which are generic nodes (location_type=3) or boarding areas (location_type=4).
"""
        domain = [Stop]
        range = [float]

    class stop_lon(FieldValue, FunctionalProperty):
        comment = """
Longitude of the location.

For stops/platforms (location_type=0) and boarding area (location_type=4), the coordinates must be the ones of the bus pole — if exists — and otherwise of where the travelers are boarding the vehicle (on the sidewalk or the platform, and not on the roadway or the track where the vehicle stops).

Conditionally Required:
- Required for locations which are stops (location_type=0), stations (location_type=1) or entrances/exits (location_type=2).
- Optional for locations which are generic nodes (location_type=3) or boarding areas (location_type=4).
"""
        domain = [Stop]
        range = [float]

    class zone_id(FieldValue, FunctionalProperty):
        comment = """
Identifies the fare zone for a stop. If this record represents a station or station entrance, the zone_id is ignored.
"""
        domain = [Stop]
        range = [str]

    class stop_url(FieldValue, FunctionalProperty):
        comment = """
URL of a web page about the location. This should be different from the agency.agency_url and the routes.route_url field values.
"""
        domain = [Stop]
        range = [str]

    class location_type(FieldValue, FunctionalProperty):
        comment = """
    Location type. Valid options are:

0 (or empty) - Stop (or Platform). A location where passengers board or disembark from a transit vehicle. Is called a platform when defined within a parent_station.
1 - Station. A physical structure or area that contains one or more platform.
2 - Entrance/Exit. A location where passengers can enter or exit a station from the street. If an entrance/exit belongs to multiple stations, it may be linked by pathways to both, but the data provider must pick one of them as parent.
3 - Generic Node. A location within a station, not matching any other location_type, that may be used to link together pathways define in pathways.txt.
4 - Boarding Area. A specific location on a platform, where passengers can board and/or alight vehicles.
"""
        domain = [Stop]
        range = [LocationTypeType]

    class parent_station(ObjectProperty, FunctionalProperty):
        comment = """
Defines hierarchy between the different locations defined in stops.txt. It contains the ID of the parent location, as followed:

- Stop/platform (location_type=0): the parent_station field contains the ID of a station.
- Station (location_type=1): this field must be empty.
- Entrance/exit (location_type=2) or generic node (location_type=3): the parent_station field contains the ID of a station (location_type=1)
- Boarding Area (location_type=4): the parent_station field contains ID of a platform.

Conditionally Required:
- Required for locations which are entrances (location_type=2), generic nodes (location_type=3) or boarding areas (location_type=4).
- Optional for stops/platforms (location_type=0).
- Forbidden for stations (location_type=1).
"""
        domain = [Stop]
        range = [Stop]

    class stop_timezone(FieldValue, FunctionalProperty):
        comment = """
Timezone of the location. If the location has a parent station, it inherits the parent station’s timezone instead of applying its own. Stations and parentless stops with empty stop_timezone inherit the timezone specified by agency.agency_timezone. The times provided in stop_times.txt are in the timezone specified by agency.agency_timezone, not stop_timezone. This ensures that the time values in a trip always increase over the course of a trip, regardless of which timezones the trip crosses.
"""
        domain = [Stop]
        range = [Timezone]

    class wheelchair_boarding(FieldValue, FunctionalProperty):
        comment = """
Indicates whether wheelchair boardings are possible from the location. Valid options are:

For parentless stops:
0 or empty - No accessibility information for the stop.
1 - Some vehicles at this stop can be boarded by a rider in a wheelchair.
2 - Wheelchair boarding is not possible at this stop.

For child stops:
0 or empty - Stop will inherit its wheelchair_boarding behavior from the parent station, if specified in the parent.
1 - There exists some accessible path from outside the station to the specific stop/platform.
2 - There exists no accessible path from outside the station to the specific stop/platform.

For station entrances/exits:
0 or empty - Station entrance will inherit its wheelchair_boarding behavior from the parent station, if specified for the parent.
1 - Station entrance is wheelchair accessible.
2 - No accessible path from station entrance to stops/platforms.
"""
        domain = [Stop]
        range = [WheelchairBoardingType]

    # class level_id(FieldValue, FunctionalProperty):
    #     pass

    class platform_code(FieldValue, FunctionalProperty):
        comment = """
Platform identifier for a platform stop (a stop belonging to a station). This should be just the platform identifier (eg. "G" or "3"). Words like “platform” or "track" (or the feed’s language-specific equivalent) should not be included. This allows feed consumers to more easily internationalize and localize the platform identifier into other languages.
"""
        domain = [Stop]
        range = [str]

    class stop_access(FieldValue, FunctionalProperty):
        comment = """
    Indicates how the stop is accessed for a particular station. Valid options are:

0 - The stop/platform cannot be directly accessed from the street network. It must be accessed from a station entrance if there is one defined for the station, otherwise the station itself. If there are pathways defined for the station, they must be used to access the stop/platform.
1 - Consuming applications should generate directions for access directly to the stop, independent of any entrances or pathways of the parent station.

When stop_access is empty, the access for the specified stop or platform is considered undefined.

Conditionally Forbidden:
- Forbidden for locations which are stations (location_type=1), entrances (location_type=2), generic nodes (location_type=3) or boarding areas (location_type=4).
- Forbidden if parent_station is empty.
- Optional otherwise.
"""
        domain = [Stop]
        range = [StopAccessType]

    # endregion