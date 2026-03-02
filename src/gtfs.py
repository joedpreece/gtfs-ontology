from owlready2 import get_ontology, Thing, Datatype, OneOf, ObjectProperty, locstr
from config import ONTOLOGY_FILE

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

    class FieldValue(Thing):
        comment = "An individual entry in a field. Represented, in a table, as a single cell."

    # Define the files.

    class File(Thing):
        comment = ""

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

    # Defin the records.

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

    # endregion

    # region Data Types

    # TODO Complete this list.
    class LanguageCode(Datatype):
        comment = "Test comment"
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

    # endregion

    # region Class Properties

    class hasAgency(ObjectProperty):
        domain = [AgencyFile]
        range = [Agency]

    # endregion

gtfs.save(file=ONTOLOGY_FILE, format="rdfxml")