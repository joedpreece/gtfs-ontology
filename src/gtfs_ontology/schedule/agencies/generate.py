from gtfs_ontology.schedule.agencies.definitions import *
from gtfs_ontology.schedule.field_types.generate import *
from gtfs_ontology.schedule.records.generate import Agency, Route

AGENCY_DEFINITIONS_URL = "https://gtfs.org/documentation/schedule/reference/#agencytxt"

with gtfs:

    class cemv_support_enum(Datatype):
        equivalent_to = [
            OneOf(
                [
                    0,
                    1,
                    2,
                ]
            )
        ]


    class agency_id(id):
        comment = [locstr(AGENCY_ID_DEF, "en")]
        domain = [Agency | Route]
        seeAlso = [AGENCY_DEFINITIONS_URL]


    class agency_name(text):
        comment = [locstr(AGENCY_NAME_DEF, "en")]
        domain = [Agency]
        seeAlso = [AGENCY_DEFINITIONS_URL]


    class agency_url(url):
        comment = [locstr(AGENCY_URL_DEF, "en")]
        domain = [Agency]
        seeAlso = [AGENCY_DEFINITIONS_URL]


    class agency_timezone(timezone):
        comment = [locstr(AGENCY_TIMEZONE_DEF, "en")]
        domain = [Agency]
        seeAlso = [AGENCY_DEFINITIONS_URL]


    class agency_lang(language_code):
        comment = [locstr(AGENCY_LANG_DEF, "en")]
        domain = [Agency]
        seeAlso = [AGENCY_DEFINITIONS_URL]


    class agency_phone(phone_number):
        comment = [locstr(AGENCY_PHONE_DEF, "en")]
        domain = [Agency]
        seeAlso = [AGENCY_DEFINITIONS_URL]


    class agency_fare_url(url):
        comment = [locstr(AGENCY_FARE_URL_DEF, "en")]
        domain = [Agency]
        seeAlso = [AGENCY_DEFINITIONS_URL]


    class agency_email(email):
        comment = [locstr(AGENCY_EMAIL_DEF, "en")]
        domain = [Agency]
        seeAlso = [AGENCY_DEFINITIONS_URL]


    class cemv_support(enum):
        comment = [locstr(CEMV_SUPPORT_DEF, "en")]
        domain = [Agency | Route]
        range = [cemv_support_enum]
        seeAlso = [AGENCY_DEFINITIONS_URL]