from owlready2 import locstr, Thing, DataProperty

from gtfs_ontology.core import gtfs, dcat
from gtfs_ontology.schedule.term_definitions.definitions import *

TERM_DEFINITIONS_URL = "https://gtfs.org/documentation/schedule/reference/#term-definitions"

with gtfs:

    class Dataset(dcat.Dataset):
        comment = [locstr(DATASET_DEF, "en")]
        seeAlso = [TERM_DEFINITIONS_URL]

    class Record(Thing):
        comment = [locstr(RECORD_DEF, "en")]
        seeAlso = [TERM_DEFINITIONS_URL]

    class Field(DataProperty):
        comment = [locstr(FIELD_DEF, "en")]
        seeAlso = [TERM_DEFINITIONS_URL]

    class FieldValue(DataProperty):
        comment = [locstr(FIELD_VALUE, "en")]
        seeAlso = [TERM_DEFINITIONS_URL]

    class ServiceDay(Thing):
        comment = [locstr(SERVICE_DAY_DEF, "en")]
        seeAlso = [TERM_DEFINITIONS_URL]

    class TextToSpeechField(Field):
        comment = [locstr(TEXT_TO_SPEECH_FIELD_DEF, "en")]
        seeAlso = [TERM_DEFINITIONS_URL]

    class Leg(Thing):
        comment = [locstr(LEG_DEF, "en")]
        seeAlso = [TERM_DEFINITIONS_URL]

    class Journey(Thing):
        comment = [locstr(JOURNEY_DEF, "en")]
        seeAlso = [TERM_DEFINITIONS_URL]

    class SubJourney(Thing):
        comment = [locstr(SUB_JOURNEY_DEF, "en")]
        seeAlso = [TERM_DEFINITIONS_URL]

    class FareProduct(Thing):
        comment = [locstr(FARE_PRODUCT_DEF, "en")]
        seeAlso = [TERM_DEFINITIONS_URL]

    class EffectiveFareLeg(Thing):
        comment = [locstr(EFFECTIVE_FARE_LEG_DEF, "en")]
        seeAlso = [TERM_DEFINITIONS_URL]

    # This is an additional concept that is not part of the GTFS specification.
    class DatasetFile(Thing):
        # comment = [locstr(FIELD_DEF, "en")]
        seeAlso = ["https://gtfs.org/documentation/schedule/reference/#dataset-files"]