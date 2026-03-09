from owlready2 import get_ontology, Thing, Datatype, OneOf, ObjectProperty, locstr, \
    DataProperty, FunctionalProperty
from config import GTFS_ONTOLOGY_NT, GTFS_ONTOLOGY_RDF

gtfs = get_ontology("http://www.transit.ac.uk/ontologies/gtfs")

gtfs.metadata.label = [locstr("The GTFS Ontology", "en")]
gtfs.metadata.comment = [locstr(
    "An OWL ontology describing entities, relationships, and data structures found in the General Transit Feed Specification (GTFS).", "en"
)]
gtfs.metadata.versionInfo = "0.1.0"

with gtfs:

    # region Classes

    class Dataset(Thing):
        comment = "A complete set of files defined by this specification reference. Altering the dataset creates a new version of the dataset. Datasets should be published at a public, permanent URL, including the zip file name. (e.g., https://www.agency.org/gtfs/gtfs.zip)."

    class Record(Thing):
        comment = "A basic data structure comprised of a number of different field values describing a single entity (e.g. transit agency, stop, route, etc.). Represented, in a table, as a row."

    class Field(Thing):
        comment = "A property of an object or entity. Represented, in a table, as a column. The field exists if added in a file as a header. It may or may not have field values defined."

    class FieldValue(DataProperty):
        comment = "An individual entry in a field. Represented, in a table, as a single cell."

    class File(Thing):
        comment = ""

    class ServiceDay(Thing):
        comment = "A service day is a time period used to indicate route scheduling. The exact definition of service day varies from agency to agency but service days often do not correspond with calendar days. A service day may exceed 24:00:00 if service begins on one day and ends on a following day. For example, service that runs from 08:00:00 on Friday to 02:00:00 on Saturday, could be denoted as running from 08:00:00 to 26:00:00 on a single service day."

    class TextToSpeechField(Field):
        comment = "The field should contain the same information than its parent field (on which it falls back if it is empty). It is aimed to be read as text-to-speech, therefore, abbreviation should be either removed (\"St\" should be either read as \"Street\" or \"Saint\"; \"Elizabeth I\" should be \"Elizabeth the first\") or kept to be read as it (\"JFK Airport\" is said abbreviated)."

    class Leg(Thing):
        comment = "Travel in which a rider boards and alights between a pair of subsequent locations along a trip."

    class Journey(Thing):
        comment = "Overall travel from origin to destination, including all legs and transfers in-between."

    class SubJourney(Thing):
        comment = "Two or more legs that comprise a subset of a journey."

    class FareProduct(Thing):
        comment = "Purchassable fare products that can be used to pay for or validate travel."

    # Define the files.

    class AgencyFile(File):
        comment = "Transit agencies with service represented in this dataset."

    class StopFile(File):
        comment = "Stops where vehicles pick up or drop off riders. Also defines stations and station entrances."

    class RouteFile(File):
        comment = "Transit routes. A route is a group of trips that are displayed to riders as a single service."

    class TripFile(File):
        comment = "Trips for each route. A trip is a sequence of two or more stops that occur during a specific time period."

    class StopTimeFile(File):
        comment = "Times that a vehicle arrives at and departs from stops for each trip."

    class CalendarFile(File):
        comment = "Service dates specified using a weekly schedule with start and end dates."

    class CalendarDateFile(File):
        comment = "Exceptions for the services defined in the calendar.txt."

    # Define the records.

    class Agency(Record):
        pass

    class Stop(Record):
        pass

    class Route(Record):
        pass

    class Trip(Record):
        pass

    class StopTime(Record):
        pass

    class Service(Record):
        pass

    # endregion

    # region Data Types

    # TODO Complete this list.
    class LanguageCode(Datatype):
        equivalent_to = [
            OneOf(
                [
                    "EN",
                ]
            )
        ]

    class Timezone(Datatype):
        equivalent_to = [
            OneOf(
                [
                    "Europe/London",
                ]
            )
        ]

    # endregion

    # region Class Properties

    class hasAgency(ObjectProperty):
        domain = [AgencyFile]
        range = [Agency]

    # endregion

# region Agencies
with gtfs:

    # region Classes

    class AgencyFileWithSingleAgency(gtfs.AgencyFile):
        comment = "An agency file with a single agency."

    class AgencyFileWithMultipleAgencies(gtfs.AgencyFile):
        comment = "An agency file with multiple agencies."

    # end region

    # region Data Types

    class CEMVSupportType(Datatype):
        equivalent_to = [
            OneOf(
                [
                    0,
                    1,
                    2,
                ]
            )
        ]

    class CEMVSupport(Thing):
        pass

    class CEMVSupport0(CEMVSupport):
        comment = "No cEMV information for trips associated with this agency."

    class CEMVSupport1(CEMVSupport):
        comment = "Riders may use cEMVs as fare media for trips associated with this agency."

    class CEMVSupport2(CEMVSupport):
        comment = "cEMVs are not supported as fare media for trips associated with this agency."

    # endregion

    # region Data Properties

    class agency_id(FieldValue, FunctionalProperty):
        comment = """
Identifies a transit brand which is often synonymous with a transit agency. Note that in some cases, such as when a single agency operates multiple separate services, agencies and brands are distinct. This document uses the term "agency" in place of "brand". A dataset may contain data from multiple agencies.

Conditionally Required:
- Required when the dataset contains data for multiple transit agencies.
- Recommended otherwise.
"""
        domain = [gtfs.Agency]
        range = [str]

    class agency_name(FieldValue, FunctionalProperty):
        comment = "Full name of the transit agency."
        domain = [gtfs.Agency]
        range = [str]

    class agency_url(FieldValue, FunctionalProperty):
        comment = "URL of the transit agency."
        domain = [gtfs.Agency]
        range = [str]

    class agency_timezone(FieldValue, FunctionalProperty):
        comment = """
Timezone where the transit agency is located. If multiple agencies are specified in the dataset, each must have the same agency_timezone.
"""
        domain = [gtfs.Agency]
        range = [gtfs.Timezone]

    class agency_lang(FieldValue, FunctionalProperty):
        comment = """
Primary language used by this transit agency. Should be provided to help GTFS consumers choose capitalization rules and other language-specific settings for the dataset.
"""
        domain = [gtfs.Agency]
        range = [gtfs.LanguageCode]

    class agency_phone(FieldValue, FunctionalProperty):
        comment = """
A voice telephone number for the specified agency. This field is a string value that presents the telephone number as typical for the agency's service area. It may contain punctuation marks to group the digits of the number. Dialable text (for example, TriMet's "503-238-RIDE") is permitted, but the field must not contain any other descriptive text.
"""
        domain = [gtfs.Agency]
        range = [str]

    class agency_fare_url(FieldValue, FunctionalProperty):
        comment = """
URL of a web page where a rider can purchase tickets or other fare instruments for that agency, or a web page containing information about that agency's fares.
"""
        domain = [gtfs.Agency]
        range = [str]

    class agency_email(FieldValue, FunctionalProperty):
        comment = """
Email address actively monitored by the agency’s customer service department. This email address should be a direct contact point where transit riders can reach a customer service representative at the agency.
"""
        domain = [gtfs.Agency]
        range = [str]

    class cemv_support(FieldValue, FunctionalProperty):
        comment = """
Indicates if riders can access a transit service (i.e., trip) associated with this agency by using a contactless EMV (Europay, Mastercard, and Visa) card or mobile device as fare media at a fare validator (such as in pay-as-you-go or open-loop systems). This field does not indicate that cEMV can be used to purchase other fare products or to add value to another fare media.

Support for cEMVs should only be indicated if all services under this agency are accessible with the use of cEMV cards or mobile devices as fare media.

Valid options are:

0 or empty - No cEMV information for trips associated with this agency.
1 - Riders may use cEMVs as fare media for trips associated with this agency.
2 - cEMVs are not supported as fare media for trips associated with this agency.

If both agency.cemv_support and routes.cemv_support are provided for the same service, the value in routes.cemv_support shall take precedence.

This field is independent of all other fare-related files and may be used separately. If there is conflicting information between this field and any fare-related file (such as fare_media.txt, fare_products.txt, or fare_leg_rules.txt), the information in those files shall take precedence over agency.cemv_support.
        """
        domain = [gtfs.Agency]
        range = [gtfs.CEMVSupportType]

    # region Rules

    # Every agency has to have exactly one agency_name, agency_url, and agency_timezone.
    gtfs.Agency.is_a.append(
        agency_name.exactly(1) &
        agency_url.exactly(1) &
        agency_timezone.exactly(1)
    )

    # An agency file must have at least one agency.
    gtfs.AgencyFile.is_a.append(
        gtfs.hasAgency.min(1)
    )

    # If an agency file has multiple agencies, then it is a multiple agency file, and all agencies must have agency ids.
    AgencyFileWithMultipleAgencies.equivalent_to.append(
        gtfs.AgencyFile &
        gtfs.hasAgency.only(agency_id.exactly(1)) &
        gtfs.hasAgency.min(2)
    )

    # If an agency file has exactly one agency, then it is a single agency file.
    AgencyFileWithSingleAgency.equivalent_to.append(
        gtfs.AgencyFile &
        gtfs.hasAgency.exactly(1)
    )

# region Stops
with gtfs:

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

    class LocationType(Thing):
        pass

    class Station(Thing):
        comment = "A physical structure or area that contains one or more platform."

    class EntranceOrExit(Thing):
        comment = "A location where passengers can enter or exit a station from the street. If an entrance/exit belongs to multiple stations, it may be linked by pathways to both, but the data provider must pick one of them as parent."

    class GenericNode(Thing):
        comment = "A location within a station, not matching any other location_type, that may be used to link together pathways define in pathways.txt."

    class BoardingArea(Thing):
        comment = "A specific location on a platform, where passengers can board and/or alight vehicles."

    class WheelchairBoardingType(Datatype):
        comment = "Indicates whether wheelchair boardings are possible from the location. Valid options are: "

    class WheelchairBoardingParentlessStop(Thing):
        pass

    class WheelchairBoardingParentlessStop0(Thing):
        comment = "No accessibility information for the stop."

    class WheelchairBoardingParentlessStop1(Thing):
        comment = "Wheelchair boardings are possible from the stop."

    class WheelchairBoardingParentlessStop2(Thing):
        comment = "Wheelchair boarding is not possible at this stop."

    class WheelchairBoardingChildStop(Thing):
        pass

    class WheelchairBoardingChildStop0(WheelchairBoardingChildStop):
        comment = "Stop will inherit its wheelchair_boarding behavior from the parent station, if specified in the parent."

    class WheelchairBoardingChildStop1(WheelchairBoardingChildStop):
        comment = "There exists some accessible path from outside the station to the specific stop/platform."

    class WheelchairBoardingChildStop2(WheelchairBoardingChildStop):
        comment = "There exists no accessible path from outside the station to the specific stop/platform."

    class WheelchairBoardingEntranceExit(Thing):
        pass

    class WheelchairBoardingEntranceExit0(WheelchairBoardingEntranceExit):
        comment = "Station entrance will inherit its wheelchair_boarding behavior from the parent station, if specified for the parent."

    class WheelchairBoardingEntranceExit1(WheelchairBoardingEntranceExit):
        comment = "Station entrance is wheelchair accessible."

    class WheelchairBoardingEntranceExit2(WheelchairBoardingEntranceExit):
        comment = "No accessible path from station entrance to stops/platforms."

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

gtfs.save(file=str(GTFS_ONTOLOGY_RDF))
gtfs.save(file=str(GTFS_ONTOLOGY_NT), format="ntriples")