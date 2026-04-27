from gtfs_ontology.schedule import *
from gtfs_ontology.schedule.term_definitions.generate import Field
from gtfs_ontology.schedule.field_types.definitions import *
from gtfs_ontology.schedule.field_types.currency_codes import *
from gtfs_ontology.schedule.field_types.timezones import *

with gtfs:

    class color_pattern(Datatype):
        equivalent_to = [ConstrainedDatatype(
            base_datatype=str,
            pattern=r"^[0-9A-F]{6}$"  # uppercase only
        )]

    class currency_code_enum(Datatype):
        equivalent_to = [
            OneOf(
                currency_codes
            )
        ]

    class timezone_enum(Datatype):
        equivalent_to = [
            OneOf(
                timezone_ids
            )
        ]

    class color(Field):
        comment = [locstr(COLOR_DEF, "en")]
        range = [color_pattern]
        seeAlso = ["https://htmlcolorcodes.com/"]

    class currency_code(Field):
        comment = [locstr(CURRENCY_CODE_DEF, "en")]
        range = [currency_code_enum]
        seeAlso = ["https://en.wikipedia.org/wiki/ISO_4217#Active_codes"]

    class currency_amount(Field):
        comment = [locstr(CURRENCY_AMOUNT_DEF, "en")]
        range = [float]
        seeAlso = ["https://en.wikipedia.org/wiki/ISO_4217#Active_codes"]

    class date(Field):
        comment = [locstr(DATE_DEF, "en")]
        range = [datetime.date]

    class email_field(Field, email):
        comment = [locstr(EMAIL_DEF, "en")]
        range = [str]

    class enum(Field):
        comment = [locstr(ENUM_DEF, "en")]

    class id(Field):
        comment = [locstr(ID_DEF, "en")]
        range = [str]

    class language_code(Field):
        comment = [locstr(LANGUAGE_CODE_DEF, "en")]
        range = [str]
        seeAlso = [
            "http://www.rfc-editor.org/rfc/bcp/bcp47.txt",
            "https://www.w3.org/International/articles/language-tags/"
        ]

    class latitude(Field):
        comment = [locstr(LATITUDE_DEF, "en")]
        range = [geo.latitude]

    class longitude(Field):
        comment = [locstr(LONGITUDE_DEF, "en")]
        range = [geo.longitude]

    class num_float(Field):
        name = "float"
        comment = [locstr(NUM_FLOAT_DEF, "en")]
        range = [float]

    class num_int(Field):
        name = "integer"
        comment = [locstr(NUM_INT_DEF, "en")]
        range = [int]

    class phone_number(Field):
        comment = [locstr(PHONE_NUMBER_DEF, "en")]
        range = [str]

    class time(Field):
        comment = [locstr(TIME_DEF, "en")]
        range = [datetime.time]

    class local_time(Field):
        comment = [locstr(LOCAL_TIME_DEF, "en")]
        range = [datetime.time]

    class text(Field):
        comment = [locstr(TEXT_DEF, "en")]
        range = [str]

    class timezone(Field):
        comment = [locstr(TIMEZONE_DEF, "en")]
        range = [timezone_enum]
        seeAlso = [
            "https://www.iana.org/time-zones",
            "https://en.wikipedia.org/wiki/List_of_tz_zones",
        ]

    class url_field(Field):
        comment = [locstr(URL_DEF, "en")]
        range = [schema.url]
        seeAlso = ["http://www.w3.org/Addressing/URL/4_URI_Recommentations.html"]