from gtfs_ontology.schedule import *
from gtfs_ontology.schedule.agencies.generate import *
from gtfs_ontology.schedule.core import isRecordOf
from gtfs_ontology.schedule.files.dl_rules import AgencyFileWithMultipleAgencies
from gtfs_ontology.schedule.records.generate import Agency

with gtfs:

    # TODO Consider that `agency_id` must be unique.

    # Agency requirements
    Agency.is_a.append(
        agency_id.max(1) &
        agency_name.exactly(1) &
        agency_url.exactly(1) &
        agency_timezone.exactly(1) &
        agency_lang.max(1) &
        agency_phone.max(1) &
        agency_fare_url.max(1) &
        agency_email.max(1) &
        cemv_support.max(1)
    )

    # An agency within an agency file with multiple agencies must have exactly one agency_id.
    class AgencyWithinAgencyFileWithMultipleAgencies(Agency):
        is_a = [
            agency_id.exactly(1)
        ]
        equivalent_to = [
            Agency &
            isRecordOf.only(AgencyFileWithMultipleAgencies)
        ]
