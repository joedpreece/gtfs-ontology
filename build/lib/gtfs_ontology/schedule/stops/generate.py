from gtfs_ontology.realtime.core import Stop
from gtfs_ontology.schedule import *
from gtfs_ontology.schedule.field_types.generate import enumerated_datatype, text, \
    url_field, enum, timezone, id
from gtfs_ontology.schedule.stops.definitions import *
from gtfs_ontology.schedule.term_definitions.generate import Field

STOP_URL = "https://gtfs.org/documentation/schedule/reference/#stopstxt"

with gtfs:

# region Enumerated datatypes

    class LocationTypeDatatype(enumerated_datatype):
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

    # class StopLocation(DatatypeDescription):
    #     comment = locstr("A location where passengers board or disembark from a transit vehicle.", "en")
    #
    # class Platform(DatatypeDescription):
    #     comment = "A location where passengers board or disembark from a transit vehicle. Is called a platform when defined within a parent_station."
    #
    # class Station(DatatypeDescription):
    #     comment = "A physical structure or area that contains one or more platform."
    #
    # class EntranceOrExit(DatatypeDescription):
    #     comment = "A location where passengers can enter or exit a station from the street. If an entrance/exit belongs to multiple stations, it may be linked by pathways to both, but the data provider must pick one of them as parent."
    #
    # class GenericNode(DatatypeDescription):
    #     comment = "A location within a station, not matching any other location_type, that may be used to link together pathways define in pathways.txt."
    #
    # class BoardingArea(DatatypeDescription):
    #     comment = "A specific location on a platform, where passengers can board and/or alight vehicles."

    class WheelchairBoardingType(enumerated_datatype):
        equivalent_to = [
            OneOf(
                [
                    0,
                    1,
                    2,
                ]
            )
        ]

    # class WheelchairBoardingParentlessStop0(DatatypeDescription):
    #     comment = "No accessibility information for the stop."
    #
    # class WheelchairBoardingParentlessStop1(DatatypeDescription):
    #     comment = "Wheelchair boardings are possible from the stop."
    #
    # class WheelchairBoardingParentlessStop2(DatatypeDescription):
    #     comment = "Wheelchair boarding is not possible at this stop."
    #
    # class WheelchairBoardingChildStop0(DatatypeDescription):
    #     comment = "Stop will inherit its wheelchair_boarding behavior from the parent station, if specified in the parent."
    #
    # class WheelchairBoardingChildStop1(DatatypeDescription):
    #     comment = "There exists some accessible path from outside the station to the specific stop/platform."
    #
    # class WheelchairBoardingChildStop2(DatatypeDescription):
    #     comment = "There exists no accessible path from outside the station to the specific stop/platform."
    #
    # class WheelchairBoardingEntranceExit0(DatatypeDescription):
    #     comment = "Station entrance will inherit its wheelchair_boarding behavior from the parent station, if specified for the parent."
    #
    # class WheelchairBoardingEntranceExit1(DatatypeDescription):
    #     comment = "Station entrance is wheelchair accessible."
    #
    # class WheelchairBoardingEntranceExit2(DatatypeDescription):
    #     comment = "No accessible path from station entrance to stops/platforms."

    class StopAccessType(enumerated_datatype):
        equivalent_to = [
            OneOf(
                [
                    0,
                    1,
                ]
            )
        ]

    # class StopAccessTypeDescription0(DatatypeDescription):
    #     comment = "The stop/platform cannot be directly accessed from the street network. It must be accessed from a station entrance if there is one defined for the station, otherwise the station itself. If there are pathways defined for the station, they must be used to access the stop/platform."
    #
    # class StopAccessTypeDescription1(DatatypeDescription):
    #     comment = "Consuming applications should generate directions for access directly to the stop, independent of any entrances or pathways of the parent station."

# endregion

# region Fields

    class stop_id(id):
        comment = [locstr(STOP_ID_DEF, "en")]
        domain = [Stop]
        seeAlso = [STOP_URL]

    class stop_code(text):
        comment = [locstr(STOP_NAME_DEF, "en")]
        domain = [Stop]
        seeAlso = [STOP_URL]

    class stop_name(text):
        comment = [locstr(STOP_ACCESS_DEF, "en")]
        domain = [Stop]
        seeAlso = [STOP_URL]

    class tts_stop_name(text):
        comment = [locstr(TTS_STOP_NAME_DEF, "en")]
        domain = [Stop]
        seeAlso = [STOP_URL]

    class stop_desc(text):
        comment = [locstr(STOP_DESC_DEF, "en")]
        domain = [Stop]
        seeAlso = [STOP_URL]

    class stop_lat(latitude):
        comment = [locstr(STOP_LAT_DEF, "en")]
        domain = [Stop]
        seeAlso = [STOP_URL]

    class stop_lon(longitude):
        comment = [locstr(STOP_LON_DEF, "en")]
        domain = [Stop]
        seeAlso = [STOP_URL]

    class zone_id(id):
        comment = [locstr(ZONE_ID_DEF, "en")]
        domain = [Stop]
        seeAlso = [STOP_URL]

    class stop_url(url_field):
        comment = [locstr(STOP_URL_DEF, "en")]
        domain = [Stop]
        seeAlso = [STOP_URL]

    class location_type(enum):
        comment = [locstr(LOCATION_TYPE_DEF, "en")]
        domain = [Stop]
        range = [LocationTypeDatatype]
        seeAlso = [STOP_URL]

    class parent_station(id):
        comment = [locstr(PARENT_STATION_DEF, "en")]
        domain = [Stop]
        seeAlso = [STOP_URL]

    class stop_timezone(timezone):
        comment = [locstr(STOP_TIMEZONE_DEF, "en")]
        domain = [Stop]
        seeAlso = [STOP_URL]

    class wheelchair_boarding(enum):
        comment = [locstr(WHEELCHAIR_BOARDING_DEF, "en")]
        domain = [Stop]
        range = [WheelchairBoardingType]
        seeAlso = [STOP_URL]

    class level_id(Field):
        comment = [locstr(LEVEL_ID_DEF, "en")]
        domain = [Stop]
        # range = [Level]
        seeAlso = [STOP_URL]

    class platform_code(text):
        comment = [locstr(PLATFORM_CODE_DEF, "en")]
        domain = [Stop]
        seeAlso = [STOP_URL]

    class stop_access(enum):
        comment = [locstr(STOP_ACCESS_DEF, "en")]
        domain = [Stop]
        range = [StopAccessType]
        seeAlso = [STOP_URL]

# endregion