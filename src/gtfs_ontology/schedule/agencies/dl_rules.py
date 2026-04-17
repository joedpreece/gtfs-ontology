from gtfs_ontology.schedule import *
from gtfs_ontology.schedule.agencies.generate import AgencyFileWithMultipleAgencies, \
    agency_id, agency_name, agency_timezone, agency_url, agency_lang, agency_phone, \
    agency_fare_url, agency_email, cemv_support
from gtfs_ontology.schedule.core import hasRecord, isRecordOf
from gtfs_ontology.schedule.records.generate import Agency
from rdflib import RDF, OWL

with gtfs:

    class AgencyOfAgencyFileWithMultipleAgencies(Agency):
        pass

    # TODO Consider that `agency_id` must be unique.

    # 1i
    AgencyOfAgencyFileWithMultipleAgencies.equivalent_to.append(
        Agency &
        isRecordOf.only(AgencyFileWithMultipleAgencies)
    )

    AgencyOfAgencyFileWithMultipleAgencies.is_a.append(
        agency_id.exactly(1)
    )

    Agency.is_a.append(
        agency_id.max(1)
    )

    Agency.is_a.append(
        agency_name.exactly(1)
    )

    Agency.is_a.append(
        agency_url.exactly(1)
    )

    Agency.is_a.append(
        agency_timezone.exactly(1)
    )

    Agency.is_a.append(
        agency_lang.max(1)
    )

    Agency.is_a.append(
        agency_phone.max(1)
    )

    Agency.is_a.append(
        agency_fare_url.max(1)
    )

    Agency.is_a.append(
        agency_email.max(1)
    )

    Agency.is_a.append(
        cemv_support.max(1)
    )

