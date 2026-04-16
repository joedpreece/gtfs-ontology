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

Support for cEMVs should only be indicated if all services under this agency are accessible with the use of cEMV cards or mobile devices as fare media.

Valid options are:

0 or empty - No cEMV information for trips associated with this agency.
1 - Riders may use cEMVs as fare media for trips associated with this agency.
2 - cEMVs are not supported as fare media for trips associated with this agency.

If both agency.cemv_support and routes.cemv_support are provided for the same service, the value in routes.cemv_support shall take precedence.

This field is independent of all other fare-related files and may be used separately. If there is conflicting information between this field and any fare-related file (such as fare_media.txt, fare_products.txt, or fare_leg_rules.txt), the information in those files shall take precedence over agency.cemv_support.
"""