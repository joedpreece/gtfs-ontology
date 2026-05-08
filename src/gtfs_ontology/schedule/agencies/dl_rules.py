from gtfs_ontology.schedule.agencies.generate import *
from gtfs_ontology.schedule.core import isRecordOf, Requirement, Recommendation
from gtfs_ontology.schedule.files.dl_rules import AgencyFileWithMultipleAgencies, AgencyFileWithSingleAgency
from gtfs_ontology.schedule.records.generate import Agency
from gtfs_ontology.schedule.term_definitions.generate import Record

with gtfs:

    # Agency requirements
    Agency.is_a.extend([
        agency_id.max(1),
        agency_name.exactly(1),
        agency_url.exactly(1),
        agency_timezone.exactly(1),
        agency_lang.max(1),
        agency_phone.max(1),
        agency_fare_url.max(1),
        agency_email.max(1),
        cemv_support.max(1)
    ])

    required_agency_id = agency_id.exactly(1)

    # An agency within an agency file with multiple agencies must have exactly one agency_id.
    class RequiredAgencyID(Requirement):
        is_a = [
            agency_id.exactly(1)
        ]
        equivalent_to = [
            Agency &
            isRecordOf.only(AgencyFileWithMultipleAgencies)
        ]

    class OptionalAgencyID(Requirement):
        is_a = [
            agency_id.max(1)
        ]

    class AgencyRecommendedAgencyID(Recommendation):
        equivalent_to = [
            Agency &
            isRecordOf.only(AgencyFileWithSingleAgency)
        ]

    class RecordWithCEMVInformation(Record):
        pass

    class AgencyWithNoCEMVInformation(RecordWithCEMVInformation):
        equivalent_to = [
            Agency &
            (
                cemv_support.value(0) |
                cemv_support.exactly(0)
            )
        ]

    class AgencyWithCEMVSupport(RecordWithCEMVInformation):
        equivalent_to = [
            Agency &
            cemv_support.value(1)
        ]

    class AgencyWithoutCEMVSupport(RecordWithCEMVInformation):
        equivalent_to = [
            Agency &
            cemv_support.value(2)
        ]