# from owlready2 import get_ontology, Thing, Datatype, OneOf, FunctionalProperty, \
#     DataProperty, Imp
# from config import ONTOLOGY_FILE
#
# gtfs = get_ontology(f"file://{ONTOLOGY_FILE}").load()
#
# with gtfs:
#
#     # region Classes
#
#     class AgencyFileWithSingleAgency(gtfs.AgencyFile):
#         comment = "An agency file with a single agency."
#
#     class AgencyFileWithMultipleAgencies(gtfs.AgencyFile):
#         comment = "An agency file with multiple agencies."
#
#     # end region
#
#     # region Data Types
#
#     class CEMVSupportType(Datatype):
#         equivalent_to = [
#             OneOf(
#                 [
#                     0,
#                     1,
#                     2,
#                 ]
#             )
#         ]
#
#     # endregion
#
#     # region Data Properties
#
#     class agency_id(gtfs.FieldValue, FunctionalProperty):
#         comment = "Identifies a transit brand which is often synonymous with a transit agency. Note that in some cases, such as when a single agency operates multiple separate services, agencies and brands are distinct. This document uses the term \"agency\" in place of \"brand\". A dataset may contain data from multiple agencies. "
#         domain = [gtfs.Agency]
#         range = [str]
#
#     class agency_name(gtfs.FieldValue, FunctionalProperty):
#         comment = "Full name of the transit agency."
#         domain = [gtfs.Agency]
#         range = [str]
#
#     class agency_url(gtfs.FieldValue, FunctionalProperty):
#         comment = "URL of the transit agency."
#         domain = [gtfs.Agency]
#         range = [str]
#
#     class agency_timezone(gtfs.FieldValue, FunctionalProperty):
#         comment = "Timezone where the transit agency is located. If multiple agencies are specified in the dataset, each must have the same agency_timezone."
#         domain = [gtfs.Agency]
#         range = [gtfs.Timezone]
#
#     class agency_lang(gtfs.FieldValue, FunctionalProperty):
#         comment = "The language of an agency."
#         domain = [gtfs.Agency]
#         range = [gtfs.LanguageCode]
#
#     class agency_phone(gtfs.FieldValue, FunctionalProperty):
#         comment = "The phone number of an agency."
#         domain = [gtfs.Agency]
#         range = [str]
#
#     class agency_fare_url(gtfs.FieldValue, FunctionalProperty):
#         comment = "The URL of an agency's fare rules."
#         domain = [gtfs.Agency]
#         range = [str]
#
#     class agency_email(gtfs.FieldValue, FunctionalProperty):
#         comment = "The email address of an agency."
#         domain = [gtfs.Agency]
#         range = [str]
#
#     class cemv_support(gtfs.FieldValue, FunctionalProperty):
#         comment = """
# Indicates if riders can access a transit service (i.e., trip) associated with this agency by using a contactless EMV (Europay, Mastercard, and Visa) card or mobile device as fare media at a fare validator (such as in pay-as-you-go or open-loop systems). This field does not indicate that cEMV can be used to purchase other fare products or to add value to another fare media.
#
# Support for cEMVs should only be indicated if all services under this agency are accessible with the use of cEMV cards or mobile devices as fare media.
#
# Valid options are:
#
# 0 or empty - No cEMV information for trips associated with this agency.
# 1 - Riders may use cEMVs as fare media for trips associated with this agency.
# 2 - cEMVs are not supported as fare media for trips associated with this agency.
#
# If both agency.cemv_support and routes.cemv_support are provided for the same service, the value in routes.cemv_support shall take precedence.
#
# This field is independent of all other fare-related files and may be used separately. If there is conflicting information between this field and any fare-related file (such as fare_media.txt, fare_products.txt, or fare_leg_rules.txt), the information in those files shall take precedence over agency.cemv_support.
#         """
#         domain = [gtfs.Agency]
#         range = [gtfs.CEMVSupportType]
#
#     # endregion
#
#     # region Rules
#
#     # An agency has exactly one agency_name, agency_url, and agency_timezone.
#     gtfs.Agency.is_a.append(
#         agency_name.exactly(1) &
#         agency_url.exactly(1) &
#         agency_timezone.exactly(1)
#     )
#
#     # An agency file has at least one agency.
#     gtfs.AgencyFile.is_a.append(
#         gtfs.hasAgency.min(1)
#     )
#
#     # An agency dataset with multiple agents is equivalent to an agency dataset with a minimum of two agencies
#     AgencyFileWithMultipleAgencies.equivalent_to.append(
#         gtfs.AgencyFile &
#         gtfs.hasAgency.min(2)
#     )
#
#     # An agency dataset with multiple agents is equivalent to an agency dataset with a minimum of two agencies
#     AgencyFileWithMultipleAgencies.equivalent_to.append(
#         gtfs.AgencyFile &
#         gtfs.hasAgency.min(2, gtfs.Agency)
#     )
#
#     # An agency dataset with a single agency is equivalent to an agency dataset with a single agency.
#     AgencyFileWithSingleAgency.equivalent_to.append(
#         gtfs.AgencyFile &
#         gtfs.hasAgency.exactly(1)
#     )
#
#     # endregion
#
# gtfs.save(file=ONTOLOGY_FILE, format="rdfxml")