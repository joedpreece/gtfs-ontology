from gtfs_ontology.schedule.core import *

# region Definitions

AGENCY_ID_DEF = """
Identifies a transit brand which is often synonymous with a transit agency. In some cases, a single agency operates multiple separate services and agencies and brands are distinct. This document uses the term “agency” in place of “brand”. A dataset may contain data from multiple agencies.
"""

AGENCY_NAME_DEF = """
Full name of the transit agency.
"""

AGENCY_URL_DEF = """
URL of the transit agency.
"""

AGENCY_TIMEZONE_DEF = """
Timezone where the transit agency is located. If multiple agencies are specified in the dataset, each must have the same agency_timezone.
"""

AGENCY_LANG_DEF = """
Primary language used by this transit agency. Should be provided to help GTFS consumers choose capitalization rules and other language-specific settings for the dataset.
"""

AGENCY_PHONE_DEF = """
A voice telephone number for the specified agency. This field is a string value that presents the telephone number as typical for the agency's service area. It may contain punctuation marks to group the digits of the number. Dialable text (for example, TriMet's "503-238-RIDE") is permitted, but the field must not contain any other descriptive text.
"""

AGENCY_FARE_URL_DEF = """
URL of a web page where a rider can purchase tickets or other fare instruments for that agency, or a web page containing information about that agency's fares.
"""

AGENCY_EMAIL_DEF = """
Email address actively monitored by the agency’s customer service department. This email address should be a direct contact point where transit riders can reach a customer service representative at the agency.
"""

CEMV_SUPPORT_DEF = """
Indicates if riders can access a transit service (i.e., trip) associated with this agency by using a contactless EMV (Europay, Mastercard, and Visa) card or mobile device as fare media at a fare validator (such as in pay-as-you-go or open-loop systems). This field does not indicate that cEMV can be used to purchase other fare products or to add value to another fare media. 
"""

# endregion

with gtfs:

    # region Classes

    class AgencyFileWithSingleAgency(AgencyFile):
        comment = "An agency file with a single agency."

    class AgencyFileWithMultipleAgencies(AgencyFile):
        comment = "An agency file with multiple agencies."

    AllDisjoint([AgencyFileWithSingleAgency, AgencyFileWithMultipleAgencies])

    class CEMVSupportDatatypeDescription(DatatypeDescription):
        pass

    class CEMVSupportDatatypeDescription0(CEMVSupportDatatypeDescription):
        comment = [locstr("No cEMV information for trips associated with this agency.", "en")]

    class CEMVSupportDatatypeDescription1(CEMVSupportDatatypeDescription):
        comment = [locstr("Riders may use cEMVs as fare media for trips associated with this agency.", "en")]

    class CEMVSupportDatatypeDescription2(CEMVSupportDatatypeDescription):
        comment = [locstr("cEMVs are not supported as fare media for trips associated with this agency.", "en")]

    # endregion

    # region Data Properties

    class agency_id(FieldValue, FunctionalProperty):
        comment = [locstr(AGENCY_ID_DEF, "en")]
        domain = [Agency]
        range = [str]

    class agency_name(FieldValue, FunctionalProperty):
        comment = [locstr(AGENCY_NAME_DEF, "en")]
        domain = [Agency]
        range = [str]

    class agency_url(FieldValue, FunctionalProperty):
        comment = [locstr(AGENCY_URL_DEF, "en")]
        domain = [Agency]
        range = [str]

    class agency_timezone(FieldValue, FunctionalProperty):
        comment = [locstr(AGENCY_TIMEZONE_DEF, "en")]
        domain = [Agency]
        range = [Timezone]

    class agency_lang(FieldValue, FunctionalProperty):
        comment = [locstr(AGENCY_LANG_DEF, "en")]
        domain = [Agency]
        range = [LanguageCode]

    class agency_phone(FieldValue, FunctionalProperty):
        comment = [locstr(AGENCY_PHONE_DEF, "en")]
        domain = [Agency]
        range = [str]

    class agency_fare_url(FieldValue, FunctionalProperty):
        comment = [locstr(AGENCY_FARE_URL_DEF, "en")]
        domain = [Agency]
        range = [str]

    class agency_email(FieldValue, FunctionalProperty):
        comment = [locstr(AGENCY_EMAIL_DEF, "en")]
        domain = [Agency]
        range = [str]

    class cemv_support(FieldValue, FunctionalProperty):
        comment = [locstr(CEMV_SUPPORT_DEF, "en")]
        domain = [Agency, Route]
        range = [CEMVSupportDatatype]

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