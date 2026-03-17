from core import *

with gtfs:

    # region Classes

    class AgencyFileWithSingleAgency(AgencyFile):
        comment = "An agency file with a single agency."

    class AgencyFileWithMultipleAgencies(AgencyFile):
        comment = "An agency file with multiple agencies."

    AllDisjoint([AgencyFileWithSingleAgency, AgencyFileWithMultipleAgencies])

    class CEMVSupportDatatypeDescriptionAgency(DatatypeDescription):
        pass

    class CEMVSupportDatatypeDescriptionAgency0(CEMVSupportDatatypeDescriptionAgency):
        comment = "No cEMV information for trips associated with this agency."

    class CEMVSupportDatatypeDescriptionAgency1(CEMVSupportDatatypeDescriptionAgency):
        comment = "Riders may use cEMVs as fare media for trips associated with this agency."

    class CEMVSupportDatatypeDescriptionAgency2(CEMVSupportDatatypeDescriptionAgency):
        comment = "cEMVs are not supported as fare media for trips associated with this agency."

    # endregion

    # region Data Properties

    class agency_id(FieldValue, FunctionalProperty):
        comment = """
Identifies a transit brand which is often synonymous with a transit agency. Note that in some cases, such as when a single agency operates multiple separate services, agencies and brands are distinct. This document uses the term "agency" in place of "brand". A dataset may contain data from multiple agencies.
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

If both agency.cemv_support and routes.cemv_support are provided for the same service, the value in routes.cemv_support shall take precedence.

This field is independent of all other fare-related files and may be used separately. If there is conflicting information between this field and any fare-related file (such as fare_media.txt, fare_products.txt, or fare_leg_rules.txt), the information in those files shall take precedence over agency.cemv_support.
        """
        domain = [Agency]
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