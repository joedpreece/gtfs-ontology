from owlready2 import get_ontology, Thing, Datatype, OneOf, FunctionalProperty, \
    DataProperty
from config import ONTOLOGY_FILE

gtfs = get_ontology(f"file://{ONTOLOGY_FILE}").load()

with gtfs:

    # region Classes

    class AgencyFileWithMultipleAgents(gtfs.AgencyFile):
        pass

    # end region

    # region Data Types

    class CEMVSupportType(Datatype):
        equivalent_to = [
            OneOf(
                [
                    0,
                    1,
                    2,
                ]
            )
        ]

    # endregion

    # region Data Properties

    class agency_id(DataProperty, FunctionalProperty):
        comment = "Identifies a transit brand which is often synonymous with a transit agency. Note that in some cases, such as when a single agency operates multiple separate services, agencies and brands are distinct. This document uses the term \"agency\" in place of \"brand\". A dataset may contain data from multiple agencies. "
        domain = [gtfs.Agency]
        range = [str]

    class agency_name(DataProperty, FunctionalProperty):
        comment = "Full name of the transit agency."
        domain = [gtfs.Agency]
        range = [str]

    class agency_url(DataProperty, FunctionalProperty):
        comment = "URL of the transit agency."
        domain = [gtfs.Agency]
        range = [str]

    class agency_timezone(DataProperty, FunctionalProperty):
        comment = "Timezone where the transit agency is located. If multiple agencies are specified in the dataset, each must have the same agency_timezone."
        domain = [gtfs.Agency]
        range = [gtfs.Timezone]

    class agency_lang(DataProperty, FunctionalProperty):
        comment = "The language of an agency."
        domain = [gtfs.Agency]
        range = [gtfs.LanguageCode]

    class agency_phone(DataProperty, FunctionalProperty):
        comment = "The phone number of an agency."
        domain = [gtfs.Agency]
        range = [str]

    class agency_fare_url(DataProperty, FunctionalProperty):
        comment = "The URL of an agency's fare rules."
        domain = [gtfs.Agency]
        range = [str]

    class agency_email(DataProperty, FunctionalProperty):
        comment = "The email address of an agency."
        domain = [gtfs.Agency]
        range = [str]

    class cemv_support(DataProperty, FunctionalProperty):
        comment = "The agency supports CEMV."
        domain = [gtfs.Agency]
        range = [gtfs.CEMVSupportType]

    # endregion

    # region Rules

    gtfs.Agency.is_a.append(
        agency_name.exactly(1, str) &
        agency_url.exactly(1, str) &
        agency_timezone.exactly(1, gtfs.Timezone)
    )

    # An agency dataset has at least one agency
    gtfs.AgencyFile.is_a.append(
        gtfs.hasAgency.some(gtfs.Agency)
    )

    # An agency dataset with multiple agents is equivalent to an agency dataset with a minimum of two agencies
    AgencyFileWithMultipleAgents.equivalent_to.append(
        gtfs.AgencyFile & gtfs.hasAgency.min(2, gtfs.Agency)
    )

    # endregion

gtfs.save(file=ONTOLOGY_FILE, format="rdfxml")