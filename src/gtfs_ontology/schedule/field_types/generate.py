from gtfs_ontology.core import *
from gtfs_ontology.schedule.term_definitions.generate import Field
from gtfs_ontology.schedule.field_types.definitions import *

with gtfs:

    class Color(Datatype):
        equivalent_to = [ConstrainedDatatype(
            base_datatype=str,
            pattern=r"^[0-9A-F]{6}$"  # uppercase only
        )]

    # TODO Complete this list.
    class LanguageCode(Datatype):
        equivalent_to = [
            OneOf(
                [
                    "EN",
                ]
            )
        ]

    class Timezone(Datatype):
        equivalent_to = [
            OneOf(
                [
                    "Europe/London",
                ]
            )
        ]

    class enumerated_datatype(Datatype):
        pass

    class color(Field):
        range = [Color]
        seeAlso = ["https://htmlcolorcodes.com/"]

    class currency_code(Field):
        range = [str]

    class currency_amount(Field):
        range = [float]

    class date(Field):
        range = [datetime.date]

    class email_field(Field, email):
        comment = [locstr(EMAIL_DEF, "en")]
        range = [str]

    class enum(Field):
        range = [enumerated_datatype]

    class id(Field):
        range = [str]

    class language_code(Field):
        range = [LanguageCode]

    class latitude(Field):
        range = [geo.latitude]

    class longitude(Field):
        range = [geo.longitude]

    class num_float(Field):
        range = [float]

    class num_int(Field):
        range = [int]

    class phone_number(Field):
        range = [str]

    class time(Field):
        range = [datetime.time]

    class local_time(Field):
        range = [datetime.time]

    class text(Field):
        range = [str]

    class timezone(Field):
        range = [Timezone]

    class url_field(Field):
        range = [schema.url]