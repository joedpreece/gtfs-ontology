from gtfs_ontology.schedule.core import *
from gtfs_ontology.schedule.agencies.definitions import *


with gtfs:

# region Additional classes

    class AgencyFileWithSingleAgency(AgencyFile):
        comment = "An agency file with a single agency."


    class AgencyFileWithMultipleAgencies(AgencyFile):
        comment = "An agency file with multiple agencies."


    AllDisjoint([AgencyFileWithSingleAgency, AgencyFileWithMultipleAgencies])

# endregion

# region Agency specific datatypes and descriptions

    class CEMVSupportDatatype(enumerated_datatype):
        equivalent_to = [
            OneOf(
                [
                    0,
                    1,
                    2,
                ]
            )
        ]


    class CEMVSupportDatatypeDescription0(DatatypeDescription):
        comment = [
            locstr("No cEMV information for trips associated with this agency.", "en")]


    class CEMVSupportDatatypeDescription1(DatatypeDescription):
        comment = [locstr(
            "Riders may use cEMVs as fare media for trips associated with this agency.",
            "en")]


    class CEMVSupportDatatypeDescription2(DatatypeDescription):
        comment = [locstr(
            "cEMVs are not supported as fare media for trips associated with this agency.",
            "en")]


# endregion

# region Fields

    AGENCY_DEFINITIONS_URL = "https://gtfs.org/documentation/schedule/reference/#agencytxt"

    class agency_id(id, FunctionalProperty):
        comment = [locstr(AGENCY_ID_DEF, "en")]
        domain = [Agency]
        seeAlso = [AGENCY_DEFINITIONS_URL]


    class agency_name(text, FunctionalProperty):
        comment = [locstr(AGENCY_NAME_DEF, "en")]
        domain = [Agency]
        seeAlso = [AGENCY_DEFINITIONS_URL]


    class agency_url(url_field, FunctionalProperty):
        comment = [locstr(AGENCY_URL_DEF, "en")]
        domain = [Agency]
        seeAlso = [AGENCY_DEFINITIONS_URL]


    class agency_timezone(timezone, FunctionalProperty):
        comment = [locstr(AGENCY_TIMEZONE_DEF, "en")]
        domain = [Agency]
        seeAlso = [AGENCY_DEFINITIONS_URL]


    class agency_lang(language_code, FunctionalProperty):
        comment = [locstr(AGENCY_LANG_DEF, "en")]
        domain = [Agency]
        seeAlso = [AGENCY_DEFINITIONS_URL]


    class agency_phone(phone_number, FunctionalProperty):
        comment = [locstr(AGENCY_PHONE_DEF, "en")]
        domain = [Agency]
        seeAlso = [AGENCY_DEFINITIONS_URL]


    class agency_fare_url(url_field, FunctionalProperty):
        comment = [locstr(AGENCY_FARE_URL_DEF, "en")]
        domain = [Agency]
        seeAlso = [AGENCY_DEFINITIONS_URL]


    class agency_email(email_field, FunctionalProperty):
        comment = [locstr(AGENCY_EMAIL_DEF, "en")]
        domain = [Agency]
        seeAlso = [AGENCY_DEFINITIONS_URL]


    class cemv_support(enum, FunctionalProperty):
        comment = [locstr(CEMV_SUPPORT_DEF, "en")]
        domain = [Agency]
        range = [CEMVSupportDatatype]
        seeAlso = [AGENCY_DEFINITIONS_URL]

# endregion

# region OWLDL Rules

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
        gtfs.hasAgency.min(2, gtfs.Agency)
    )

    # If an agency file has exactly one agency, then it is a single agency file.
    AgencyFileWithSingleAgency.equivalent_to.append(
        gtfs.AgencyFile &
        gtfs.hasAgency.exactly(1, gtfs.Agency)
    )

# endregion