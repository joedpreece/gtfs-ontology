from builtins import float

from gtfs_ontology.core import *

# region Definitions

DATASET_DEF = """
A complete set of files defined by this specification reference. Altering the dataset creates a new version of the dataset. Datasets should be published at a public, permanent URL, including the zip file name. (e.g., https://www.agency.org/gtfs/gtfs.zip).
"""

RECORD_DEF = """
A basic data structure comprised of a number of different field values describing a single entity (e.g. transit agency, stop, route, etc.). Represented, in a table, as a row.
"""

FIELD_DEF = """
A property of an object or entity. Represented, in a table, as a column. The field exists if added in a file as a header. It may or may not have field values defined.
"""

FIELD_VALUE = """
An individual entry in a field. Represented, in a table, as a single cell.
"""

SERVICE_DAY_DEF = """
A service day is a time period used to indicate route scheduling. The exact definition of service day varies from agency to agency but service days often do not correspond with calendar days. A service day may exceed 24:00:00 if service begins on one day and ends on a following day. For example, service that runs from 08:00:00 on Friday to 02:00:00 on Saturday, could be denoted as running from 08:00:00 to 26:00:00 on a single service day.
"""

TEXT_TO_SPEECH_FIELD_DEF = """
The field should contain the same information than its parent field (on which it falls back if it is empty). It is aimed to be read as text-to-speech, therefore, abbreviation should be either removed ("St" should be either read as "Street" or "Saint"; "Elizabeth I" should be "Elizabeth the first") or kept to be read as it ("JFK Airport" is said abbreviated).
"""

LEG_DEF = """
Travel in which a rider boards and alights between a pair of subsequent locations along a trip.
"""

JOURNEY_DEF = """
Overall travel from origin to destination, including all legs and transfers in-between.
"""

SUB_JOURNEY_DEF = """
Two or more legs that comprise a subset of a journey.
"""

FARE_PRODUCT_DEF = """
Purchassable fare products that can be used to pay for or validate travel.
"""

EFFECTIVE_FARE_LEG_DEF = """
A sub-journey of two or more legs that should be treated as a single leg for matching rules in fare_leg_rules.txt for the purposes of fare calculation.
"""

COLOR_DEF = """
A color encoded as a six-digit hexadecimal number. Refer to https://htmlcolorcodes.com to generate a valid value (the leading "#" must not be included).
Example: FFFFFF for white, 000000 for black or 0039A6 for the A,C,E lines in NYMTA.
"""

CURRENCY_CODE_DEF = """
An ISO 4217 alphabetical currency code. For the list of current currency, refer to https://en.wikipedia.org/wiki/ISO_4217#Active_codes.
Example: CAD for Canadian dollars, EUR for euros or JPY for Japanese yen.
"""

CURRENCY_AMOUNT_DEF = """
A decimal value indicating a currency amount. The number of decimal places is specified by ISO 4217 for the accompanying Currency code. All financial calculations should be processed as decimal, currency, or another equivalent type suitable for financial calculations depending on the programming language used to consume data. Processing currency amounts as float is discouraged due to gains or losses of money during calculations.
"""

DATE_DEF = """
Service day in the YYYYMMDD format. Since time within a service day may be above 24:00:00, a service day may contain information for the subsequent day(s).
Example: 20180913 for September 13th, 2018.
"""

EMAIL_DEF = """
An email address.
Example: example@example.com
"""

ENUM_DEF = """
An option from a set of predefined constants defined in the "Description" column.
Example: The route_type field contains a 0 for tram, a 1 for subway...
"""

ID_DEF = """
An ID field value is an internal ID, not intended to be shown to riders, and is a sequence of any UTF-8 characters. Using only printable ASCII characters is recommended. An ID is labeled "unique ID" when it must be unique within a file. IDs defined in one .txt file are often referenced in another .txt file. IDs that reference an ID in another table are labeled "foreign ID".
Example: The stop_id field in stops.txt is a "unique ID". The parent_station field in stops.txt is a "foreign ID referencing stops.stop_id".
"""

LANGUAGE_CODE_DEF = """
An IETF BCP 47 language code. For an introduction to IETF BCP 47, refer to http://www.rfc-editor.org/rfc/bcp/bcp47.txt and https://www.w3.org/International/articles/language-tags/.
Example: en for English, en-US for American English or de for German.
"""

LATITUDE_DEF = """
WGS84 latitude in decimal degrees. The value must be greater than or equal to -90.0 and less than or equal to 90.0.
Example: 41.890169 for the Colosseum in Rome.
"""

LONGITUDE_DEF = """
WGS84 longitude in decimal degrees. The value must be greater than or equal to -180.0 and less than or equal to 180.0.
Example: 12.492269 for the Colosseum in Rome.
"""

NUM_FLOAT_DEF = """
A floating point number.
"""

NUM_INT_DEF = """
An integer.
"""

PHONE_NUMBER_DEF = """
A phone number.
"""

TIME_DEF = """
Time in the HH:MM:SS format (H:MM:SS is also accepted). The time is measured from "noon minus 12h" of the service day (effectively midnight except for days on which daylight savings time changes occur). For times occurring after midnight on the service day, enter the time as a value greater than 24:00:00 in HH:MM:SS.
Example: 14:30:00 for 2:30PM or 25:35:00 for 1:35AM on the next day.
"""

LOCAL_TIME_DEF = """
Time in the HH:MM:SS format (H:MM:SS is also accepted). Represents a wall-clock time shown in the local time of the specified location.
"""

TEXT_DEF = """
A string of UTF-8 characters, which is aimed to be displayed and which must therefore be human readable.
"""

TIMEZONE_DEF = """
TZ timezone from the https://www.iana.org/time-zones. Timezone names never contain the space character but may contain an underscore. Refer to http://en.wikipedia.org/wiki/List_of_tz_zones for a list of valid values.
Example: Asia/Tokyo, America/Los_Angeles or Africa/Cairo.
"""

URL_DEF = """
TZ timezone from the https://www.iana.org/time-zones. Timezone names never contain the space character but may contain an underscore. Refer to http://en.wikipedia.org/wiki/List_of_tz_zones for a list of valid values.
Example: Asia/Tokyo, America/Los_Angeles or Africa/Cairo.
"""

# endregion

# region Term definitions
with gtfs:

    term_definitions_url = "https://gtfs.org/documentation/schedule/reference/#term-definitions"

    class Dataset(dcat.Dataset):
        comment = [locstr(DATASET_DEF, "en")]
        seeAlso = [term_definitions_url]

    class Record(Thing):
        comment = [locstr(RECORD_DEF, "en")]
        seeAlso = [term_definitions_url]

    class Field(DataProperty):
        comment = [locstr(FIELD_DEF, "en")]
        seeAlso = [term_definitions_url]

    class FieldValue(DataProperty):
        comment = [locstr(FIELD_VALUE, "en")]
        seeAlso = [term_definitions_url]

    class ServiceDay(Thing):
        comment = [locstr(SERVICE_DAY_DEF, "en")]
        seeAlso = [term_definitions_url]

    class TextToSpeechField(Field):
        comment = [locstr(TEXT_TO_SPEECH_FIELD_DEF, "en")]
        seeAlso = [term_definitions_url]

    class Leg(Thing):
        comment = [locstr(LEG_DEF, "en")]
        seeAlso = [term_definitions_url]

    class Journey(Thing):
        comment = [locstr(JOURNEY_DEF, "en")]
        seeAlso = [term_definitions_url]

    class SubJourney(Thing):
        comment = [locstr(SUB_JOURNEY_DEF, "en")]
        seeAlso = [term_definitions_url]

    class FareProduct(Thing):
        comment = [locstr(FARE_PRODUCT_DEF, "en")]
        seeAlso = [term_definitions_url]

    class EffectiveFareLeg(Thing):
        comment = [locstr(EFFECTIVE_FARE_LEG_DEF, "en")]
        seeAlso = [term_definitions_url]

    class DatasetFile(Thing):
        # comment = [locstr(FIELD_DEF, "en")]
        seeAlso = ["https://gtfs.org/documentation/schedule/reference/#dataset-files"]

# endregion

# region Field type
with gtfs:

    class Color(Datatype):
        equivalent_to = [ConstrainedDatatype(
            base_datatype=str,
            pattern=r"^[0-9A-F]{6}$"  # uppercase only
        )]

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

    class enumerated_datatype(Datatype):
        pass

    class color(Field):
        range = [Color]
        seeAlso = ["https://htmlcolorcodes.com/"]

    class currency_code(Field):
        range = [str]

    class currency_amount(Field):
        range = [float]

    class date(Field):
        range = [datetime.date]

    class email_field(Field, email):
        comment = [locstr(EMAIL_DEF, "en")]
        range = [str]

    class enum(Field):
        range = [enumerated_datatype]

    class id(Field):
        range = [str]

    class language_code(Field):
        range = [LanguageCode]

    class latitude(Field):
        range = [geo.latitude]

    class longitude(Field):
        range = [geo.longitude]

    class num_float(Field):
        range = [float]

    class num_int(Field):
        range = [int]

    class phone_number(Field):
        range = [str]

    class time(Field):
        range = [datetime.time]

    class local_time(Field):
        range = [datetime.time]

    class text(Field):
        range = [str]

    class timezone(Field):
        range = [Timezone]

    class url_field(Field):
        range = [schema.url]

    class NonNegativeInteger(Datatype):
        equivalent_to = [ConstrainedDatatype(
            base_datatype=int,
            min_inclusive=0
        )]

    class CEMVSupportDatatype(Datatype):
        equivalent_to = [
            OneOf(
                [
                    0,
                    1,
                    2,
                ]
            )
        ]

    # endregion

    # region Dataset files (and records)

    class AgencyFile(DatasetFile):
        comment = "Transit agencies with service represented in this dataset."

    class StopFile(DatasetFile):
        comment = "Stops where vehicles pick up or drop off riders. Also defines stations and station entrances."

    class RouteFile(DatasetFile):
        comment = "Transit routes. A route is a group of trips that are displayed to riders as a single service."

    class TripFile(DatasetFile):
        comment = "Trips for each route. A trip is a sequence of two or more stops that occur during a specific time period."

    class StopTimeFile(DatasetFile):
        comment = "Times that a vehicle arrives at and departs from stops for each trip."

    class CalendarFile(DatasetFile):
        comment = "Service dates specified using a weekly schedule with start and end dates."

    class CalendarDateFile(DatasetFile):
        comment = "Exceptions for the services defined in the calendar.txt."

    class Agency(Record, foaf.Agent):
        seeAlso = ["<https://gtfs.org/documentation/schedule/reference/#agencytxt>"]

    class Stop(Record, geo.SpatialThing):
        pass

    class Route(Record):
        pass

    class Trip(Record):
        pass

    class StopTime(Record):
        pass

    class Calendar(Record):
        pass

    class CalendarDate(Record):
        pass

    class Level(Record):
        pass

    # endregion

    # region Additional classes

    class DatatypeDescription(Thing):
        comment = "A description provided to compliment an enumerated datatype."

    # endregion

    # region Additional object properties

    class hasDataset(ObjectProperty):
        domain = [GTFSSchedule]
        range = [Dataset]

    class hasAgency(ObjectProperty):
        domain = [AgencyFile]
        range = [Agency]

    class hasFile(ObjectProperty):
        domain = [Dataset]
        range = [DatasetFile]

    # endregion