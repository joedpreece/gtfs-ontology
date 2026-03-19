from owlready2 import *
from config import GTFS_ONTOLOGY_NT, GTFS_ONTOLOGY_RDF

gtfs = get_ontology("http://www.transit.ac.uk/ontologies/gtfs")

gtfs.metadata.label = [locstr("The GTFS Ontology", "en")]
gtfs.metadata.comment = [locstr(
    "An OWL ontology describing entities, relationships, and data structures found in the General Transit Feed Specification (GTFS).", "en"
)]
gtfs.metadata.versionInfo = "0.1.0"

with gtfs:

    # region Classes

    class Dataset(Thing):
        comment = "A complete set of files defined by this specification reference. Altering the dataset creates a new version of the dataset. Datasets should be published at a public, permanent URL, including the zip file name. (e.g., https://www.agency.org/gtfs/gtfs.zip)."

    class Record(Thing):
        comment = "A basic data structure comprised of a number of different field values describing a single entity (e.g. transit agency, stop, route, etc.). Represented, in a table, as a row."

    class Field(Thing):
        comment = "A property of an object or entity. Represented, in a table, as a column. The field exists if added in a file as a header. It may or may not have field values defined."

    class FieldValue(DataProperty):
        comment = "An individual entry in a field. Represented, in a table, as a single cell."

    class File(Thing):
        comment = ""

    class ServiceDay(Thing):
        comment = "A service day is a time period used to indicate route scheduling. The exact definition of service day varies from agency to agency but service days often do not correspond with calendar days. A service day may exceed 24:00:00 if service begins on one day and ends on a following day. For example, service that runs from 08:00:00 on Friday to 02:00:00 on Saturday, could be denoted as running from 08:00:00 to 26:00:00 on a single service day."

    class TextToSpeechField(Field):
        comment = "The field should contain the same information than its parent field (on which it falls back if it is empty). It is aimed to be read as text-to-speech, therefore, abbreviation should be either removed (\"St\" should be either read as \"Street\" or \"Saint\"; \"Elizabeth I\" should be \"Elizabeth the first\") or kept to be read as it (\"JFK Airport\" is said abbreviated)."

    class Leg(Thing):
        comment = "Travel in which a rider boards and alights between a pair of subsequent locations along a trip."

    class Journey(Thing):
        comment = "Overall travel from origin to destination, including all legs and transfers in-between."

    class SubJourney(Thing):
        comment = "Two or more legs that comprise a subset of a journey."

    class FareProduct(Thing):
        comment = "Purchassable fare products that can be used to pay for or validate travel."

    class DatatypeDescription(Thing):
        comment = "A description provided to compliment an enumerated datatype."

    # Define the files.

    class AgencyFile(File):
        comment = "Transit agencies with service represented in this dataset."

    class StopFile(File):
        comment = "Stops where vehicles pick up or drop off riders. Also defines stations and station entrances."

    class RouteFile(File):
        comment = "Transit routes. A route is a group of trips that are displayed to riders as a single service."

    class TripFile(File):
        comment = "Trips for each route. A trip is a sequence of two or more stops that occur during a specific time period."

    class StopTimeFile(File):
        comment = "Times that a vehicle arrives at and departs from stops for each trip."

    class CalendarFile(File):
        comment = "Service dates specified using a weekly schedule with start and end dates."

    class CalendarDateFile(File):
        comment = "Exceptions for the services defined in the calendar.txt."

    # Define the records.

    class Agency(Record):
        pass

    class Stop(Record):
        pass

    class Route(Record):
        pass

    class Trip(Record):
        pass

    class StopTime(Record):
        pass

    class Calendar(Record):
        pass

    class CalendarDate(Record):
        pass

    class Level(Record):
        pass

    # endregion

    # region Datatypes

    class Color(Datatype):
        equivalent_to = [ConstrainedDatatype(
            base_datatype=str,
            pattern=r"^[0-9A-F]{6}$"  # uppercase only
        )]

    class NonNegativeInteger(Datatype):
        equivalent_to = ConstrainedDatatype(
            base_datatype=int,
            min_inclusive=0
        )

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

    class CEMVSupportDatatype(Datatype):
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

    # region Class Properties

    class hasAgency(ObjectProperty):
        domain = [AgencyFile]
        range = [Agency]

    class hasFile(ObjectProperty):
        domain = [Dataset]
        range = [File]

    # endregion

    # region Data Properties



    # endregion