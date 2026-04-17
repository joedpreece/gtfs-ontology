STOP_ID_DEF = """
Identifies a location: stop/platform, station, entrance/exit, generic node or boarding area (see location_type).

ID must be unique across all stops.stop_id, locations.geojson id, and location_groups.location_group_id values.

Multiple routes may use the same stop_id.
"""

STOP_CODE_DEF = """
Short text or a number that identifies the location for riders. These codes are often used in phone-based transit information systems or printed on signage to make it easier for riders to get information for a particular location. The stop_code may be the same as stop_id if it is public facing. This field should be left empty for locations without a code presented to riders.
"""

STOP_NAME_DEF = """
Name of the location. The stop_name should match the agency's rider-facing name for the location as printed on a timetable, published online, or represented on signage. For translations into other languages, use translations.txt.

When the location is a boarding area (location_type=4), the stop_name should contains the name of the boarding area as displayed by the agency. It could be just one letter (like on some European intercity railway stations), or text like “Wheelchair boarding area” (NYC’s Subway) or “Head of short trains” (Paris’ RER).
"""

TTS_STOP_NAME_DEF = """
Readable version of the stop_name.
"""

STOP_DESC_DEF = """
Description of the location that provides useful, quality information. Should not be a duplicate of stop_name.
"""

STOP_LAT_DEF = """
Latitude of the location.

For stops/platforms (location_type=0) and boarding area (location_type=4), the coordinates must be the ones of the bus pole — if exists — and otherwise of where the travelers are boarding the vehicle (on the sidewalk or the platform, and not on the roadway or the track where the vehicle stops). 
"""

STOP_LON_DEF = """
Longitude of the location.

For stops/platforms (location_type=0) and boarding area (location_type=4), the coordinates must be the ones of the bus pole — if exists — and otherwise of where the travelers are boarding the vehicle (on the sidewalk or the platform, and not on the roadway or the track where the vehicle stops).
"""

ZONE_ID_DEF = """
Identifies the fare zone for a stop. If this record represents a station or station entrance, the zone_id is ignored.
"""

STOP_URL_DEF = """
URL of a web page about the location. This should be different from the agency.agency_url and the routes.route_url field values.
"""

LOCATION_TYPE_DEF = """
Location type. Valid options are:

0 (or empty) - Stop (or Platform). A location where passengers board or disembark from a transit vehicle. Is called a platform when defined within a parent_station.
1 - Station. A physical structure or area that contains one or more platform.
2 - Entrance/Exit. A location where passengers can enter or exit a station from the street. If an entrance/exit belongs to multiple stations, it may be linked by pathways to both, but the data provider must pick one of them as parent.
3 - Generic Node. A location within a station, not matching any other location_type, that may be used to link together pathways define in pathways.txt.
4 - Boarding Area. A specific location on a platform, where passengers can board and/or alight vehicles.
"""

PARENT_STATION_DEF = """
Defines hierarchy between the different locations defined in stops.txt. It contains the ID of the parent location, as followed:

- Stop/platform (location_type=0): the parent_station field contains the ID of a station.
- Station (location_type=1): this field must be empty.
- Entrance/exit (location_type=2) or generic node (location_type=3): the parent_station field contains the ID of a station (location_type=1)
- Boarding Area (location_type=4): the parent_station field contains ID of a platform.
"""

STOP_TIMEZONE_DEF = """
Timezone of the location. If the location has a parent station, it inherits the parent station’s timezone instead of applying its own. Stations and parentless stops with empty stop_timezone inherit the timezone specified by agency.agency_timezone. The times provided in stop_times.txt are in the timezone specified by agency.agency_timezone, not stop_timezone. This ensures that the time values in a trip always increase over the course of a trip, regardless of which timezones the trip crosses.
"""

WHEELCHAIR_BOARDING_DEF = """
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

LEVEL_ID_DEF = """
Level of the location. The same level may be used by multiple unlinked stations.
"""

PLATFORM_CODE_DEF = """
Platform identifier for a platform stop (a stop belonging to a station). This should be just the platform identifier (eg. "G" or "3"). Words like “platform” or "track" (or the feed’s language-specific equivalent) should not be included. This allows feed consumers to more easily internationalize and localize the platform identifier into other languages.
"""

STOP_ACCESS_DEF = """
Indicates how the stop is accessed for a particular station. Valid options are:

0 - The stop/platform cannot be directly accessed from the street network. It must be accessed from a station entrance if there is one defined for the station, otherwise the station itself. If there are pathways defined for the station, they must be used to access the stop/platform.
1 - Consuming applications should generate directions for access directly to the stop, independent of any entrances or pathways of the parent station.

When stop_access is empty, the access for the specified stop or platform is considered undefined.

Conditionally Forbidden:
- Forbidden for locations which are stations (location_type=1), entrances (location_type=2), generic nodes (location_type=3) or boarding areas (location_type=4).
- Forbidden if parent_station is empty.
- Optional otherwise.
"""

STOP_OR_PLATFORM_DEF = """
A location where passengers board or disembark from a transit vehicle.
"""

STOP_LOCATION_DEF = """
A location where passengers board or disembark from a transit vehicle.
"""

PLATFORM_DEF = """
Is called a platform when defined within a parent_station.
"""

STATION_DEF = """
A physical structure or area that contains one or more platform.
"""

ENTRANCE_OR_EXIT_DEF = """
A location where passengers can enter or exit a station from the street. If an entrance/exit belongs to multiple stations, it may be linked by pathways to both, but the data provider must pick one of them as parent.
"""

GENERIC_NODE_DEF = """
A location within a station, not matching any other location_type, that may be used to link together pathways define in pathways.txt.
"""

BOARDING_AREA_DEF = """
A specific location on a platform, where passengers can board and/or alight vehicles.
"""

PARENTLESS_STOP_DEF = """
A parentless stop is a stop that does not reference a parent station.
It represents a standalone boarding or alighting location that is not a child of another stop.
"""

CHILD_STOP_DEF = """
A child stop is a sub-location of a station rather than a standalone stop or station.
"""

RECORD_WITH_ACCESSIBILITY_DEF = """
Indicates whether wheelchair boardings are possible from the location. 
"""

WHEELCHAIR_BOARDING_PARENTLESS_STOP_0_DEF = """
No accessibility information for the stop.
"""

WHEELCHAIR_BOARDING_PARENTLESS_STOP_1_DEF = """
Some vehicles at this stop can be boarded by a rider in a wheelchair.
"""

WHEELCHAIR_BOARDING_PARENTLESS_STOP_2_DEF = """
Wheelchair boarding is not possible at this stop. 
"""

WHEELCHAIR_BOARDING_CHILD_STOP_0_DEF = """
Stop will inherit its wheelchair_boarding behavior from the parent station, if specified in the parent.
"""

WHEELCHAIR_BOARDING_CHILD_STOP_1_DEF = """
There exists some accessible path from outside the station to the specific stop/platform.
"""

WHEELCHAIR_BOARDING_CHILD_STOP_2_DEF = """
There exists no accessible path from outside the station to the specific stop/platform.
"""

WHEELCHAIR_BOARDING_ENTRANCEEXIT_0_DEF = """
Station entrance will inherit its wheelchair_boarding behavior from the parent station, if specified for the parent.
"""

WHEELCHAIR_BOARDING_ENTRANCEEXIT_1_DEF = """
Station entrance is wheelchair accessible.
"""

WHEELCHAIR_BOARDING_ENTRANCEEXIT_2_DEF = """
No accessible path from station entrance to stops/platforms.
"""

STOP_ACCESS_0_DEF = """
The stop/platform cannot be directly accessed from the street network. It must be accessed from a station entrance if there is one defined for the station, otherwise the station itself. If there are pathways defined for the station, they must be used to access the stop/platform.
"""

STOP_ACCESS_1_DEF = """
Consuming applications should generate directions for access directly to the stop, independent of any entrances or pathways of the parent station.
"""