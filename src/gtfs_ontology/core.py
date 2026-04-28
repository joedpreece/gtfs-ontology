# Imports
from gtfs_ontology import *
from importlib.metadata import version

__version__ = version("gtfs-ontology")

# Namespaces and external ontologies
gtfs = get_ontology(f"https://w3id.org/gtfs#")

skos = gtfs.get_namespace("http://www.w3.org/2004/02/skos/core#")
dcterms = gtfs.get_namespace("http://purl.org/dc/terms/")
geo = gtfs.get_namespace("http://www.w3.org/2003/01/geo/wgs84_pos#")
schema = gtfs.get_namespace("https://schema.org/")
foaf = gtfs.get_namespace("http://xmlns.com/foaf/0.1/")
dcat = gtfs.get_namespace("http://www.w3.org/ns/dcat#")
gtfs_linked = gtfs.get_namespace("http://vocab.gtfs.org/terms#")

# Where ontologies are not loaded, define the terms used here
with gtfs:

    class creator(AnnotationProperty):
        namespace = dcterms  # => http://purl.org/dc/terms/creator

    class SpatialThing(Thing):
        namespace = geo

    class latitude(DataProperty):
        namespace = geo

    class longitude(DataProperty):
        namespace = geo

    class email(DataProperty):
        namespace = schema

    class telephone(DataProperty):
        namespace = schema

    class url(Datatype):
        namespace = schema

    class Agent(Thing):
        namespace = foaf

    class Dataset(Thing):
        namespace = dcat

    class closeMatch(AnnotationProperty):
        namespace = skos

    class relatedMatch(AnnotationProperty):
        namespace = skos

    class Feed(Thing):
        namespace = gtfs_linked

    class Agency(Thing):
        namespace = gtfs_linked

    class Route(Thing):
        namespace = gtfs_linked

    class RouteType(Thing):
        namespace = gtfs_linked

    class Service(Thing):
        namespace = gtfs_linked

    class Station(Thing):
        namespace = gtfs_linked

    class Stop(Thing):
        namespace = gtfs_linked

    class StopTime(Thing):
        namespace = gtfs_linked

    class Trip(Thing):
        namespace = gtfs_linked

    # class BusStop(Thing):
    #     namespace = schema

# Define the metadata for the ontology
with gtfs:
    gtfs.metadata.label = [locstr("A GTFS Ontology", "en")]
    gtfs.metadata.comment = [locstr(
        "An OWL ontology describing entities, relationships, and data structures found in the General Transit Feed Specification (GTFS).",
        "en"
    )]
    # gtfs.metadata.versionIRI = [f"{gtfs.base_iri}/v{__version__}"]
    gtfs.metadata.versionInfo = f"{__version__}"
    gtfs.metadata.creator = ["Joseph D. Preece"]

# region Definitions

GTFS_SCHEDULE_DEF = """
GTFS Schedule is a feed specification that defines a common format for static public transportation information. It is composed of a collection of simple files, mostly text files (.txt) that are contained in a single ZIP file.

Each file describes a particular aspect of transit information such as stops, routes, trips, etc. At its most basic form, a GTFS Schedule dataset is composed of 7 files: agency.txt, routes.txt, trips.txt, stops.txt, stop_times.txt, calendar.txt and calendar_dates.txt.

Along with this basic set of files, additional (optional) files can also be grouped to provide information of other service elements, such as fares, translations, transfers, in-station pathways, etc. Currently there are more than 15 optional files that extend the basic elements of GTFS, including locations.geojson which introduced a new format besides text files (.txt) which can be used to represent geographical areas. 
"""

GTFS_REALTIME_DEF = """
GTFS Realtime is a feed specification that allows public transportation agencies to provide up-to-date information about current arrival and departure times, service alerts, and vehicle position, allowing users to smoothly plan their trips.

The specification currently supports the following types of information:

    Trip updates - delays, cancellations, changed routes
    Service alerts - stop moved, unforeseen events affecting a station, route or the entire network
    Vehicle positions - information about the vehicles including location and congestion level
"""

# endregion

# region Define the high-level classes

with gtfs:

    class FeedSpecification(Thing):
        comment = [locstr("A specification for a transit feed.", "en")]

    class GTFSSchedule(FeedSpecification):
        comment = [locstr(GTFS_SCHEDULE_DEF, "en")]
        seeAlso = ["https://gtfs.org/documentation/overview/#gtfs-schedule"]

    class GTFSRealtime(FeedSpecification):
        comment = [locstr(GTFS_REALTIME_DEF, "en")]
        seeAlso = ["https://gtfs.org/documentation/overview/#gtfs-realtime"]

    # class Violation(Thing):
    #     comment = [locstr("A violation of a GTFS specification.", "en")]
    #
    # class violationDetail(DataProperty):
    #     comment = [locstr("A description of the violation.", "en")]
    #     domain = [Violation]
    #     range = [str]

# endregion