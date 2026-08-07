from owlready2 import locstr, DataProperty

from gtfs_ontology.ontologies import definitions, Agency



# class agency_id(id):
#     comment = [locstr(definitions, "en")]
#     domain = [Agency | Route]
#     seeAlso = [AGENCY_DEFINITIONS_URL]


# class agency_name(text):
#     comment = [locstr(definitions["agency_name"], "en")]
#     domain = [Agency]
#     # seeAlso = [AGENCY_DEFINITIONS_URL]


class agency_url(DataProperty):
    comment = [locstr(definitions["agency_url"], "en")]
    domain = [Agency]
    # range = [str]
    # seeAlso = [AGENCY_DEFINITIONS_URL]
#
#
# class agency_timezone(timezone):
#     comment = [locstr(AGENCY_TIMEZONE_DEF, "en")]
#     domain = [Agency]
#     seeAlso = [AGENCY_DEFINITIONS_URL]
#
#
# class agency_lang(language_code):
#     comment = [locstr(AGENCY_LANG_DEF, "en")]
#     domain = [Agency]
#     seeAlso = [AGENCY_DEFINITIONS_URL]
#
#
# class agency_phone(phone_number):
#     comment = [locstr(AGENCY_PHONE_DEF, "en")]
#     domain = [Agency]
#     seeAlso = [AGENCY_DEFINITIONS_URL]
#
#
# class agency_fare_url(url):
#     comment = [locstr(AGENCY_FARE_URL_DEF, "en")]
#     domain = [Agency]
#     seeAlso = [AGENCY_DEFINITIONS_URL]
#
#
# class agency_email(email):
#     comment = [locstr(AGENCY_EMAIL_DEF, "en")]
#     domain = [Agency]
#     seeAlso = [AGENCY_DEFINITIONS_URL]
#
#
# class cemv_support(enum):
#     comment = [locstr(CEMV_SUPPORT_DEF, "en")]
#     domain = [Agency | Route]
#     range = [cemv_support_enum]
#     seeAlso = [AGENCY_DEFINITIONS_URL]