from gtfs_ontology.schedule import *
from gtfs_ontology.schedule.field_types.generate import text, \
    url, enum, timezone, id
from gtfs_ontology.schedule.records.generate import Stop
from gtfs_ontology.schedule.stops.definitions import *
from gtfs_ontology.schedule.term_definitions.generate import field

STOP_URL = "https://gtfs.org/documentation/schedule/reference/#stopstxt"

with gtfs:

# region Enumerated datatypes

    class location_type_enum(Datatype):
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

    class wheelchair_boarding_enum(Datatype):
        equivalent_to = [
            OneOf(
                [
                    0,
                    1,
                    2,
                ]
            )
        ]

    class stop_access_enum(Datatype):
        equivalent_to = [
            OneOf(
                [
                    0,
                    1,
                ]
            )
        ]

# endregion

# region Fields

    class stop_id(id):
        comment = [locstr(STOP_ID_DEF, "en")]
        domain = [Stop | gtfs.StopTime]
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

    class stop_url(url):
        comment = [locstr(STOP_URL_DEF, "en")]
        domain = [Stop]
        seeAlso = [STOP_URL]

    class location_type(enum):
        comment = [locstr(LOCATION_TYPE_DEF, "en")]
        domain = [Stop]
        range = [location_type_enum]
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
        range = [wheelchair_boarding_enum]
        seeAlso = [STOP_URL]

    class level_id(field):
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
        range = [stop_access_enum]
        seeAlso = [STOP_URL]