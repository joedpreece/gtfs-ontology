import yaml
from rdflib.collection import Collection
from pathlib import Path

from owlready2 import *
from rdflib import Namespace, Graph, OWL, DCTERMS, VANN, URIRef, Literal, XSD, BNode, \
    RDF, RDFS

from gtfs_ontology import gtfs_owl_iri, ONTOLOGY_FILE, ONTOLOGY_PREFIX

# Set the ontology version
ONTOLOGY_VERSION = "0.1.0"

# Set the creation date
creation_date = datetime.date(2026, 6 ,19)

# Import the definitions and WIDOCO documentation
FILE_DIR = Path(__file__).resolve()
DEFINITIONS = FILE_DIR / ".." / "definitions.yaml"
ABSTRACT = FILE_DIR / ".." / "abstract.md"
INTRODUCTION = FILE_DIR / ".." / "intro.md"
DESCRIPTION = FILE_DIR / ".." / "description.md"

with open(DEFINITIONS.resolve(), "r") as f:
    definitions = yaml.safe_load(f)

# with open(INTRODUCTION.resolve(), "r", encoding="utf-8") as f:
#     intro_text = f.read()
#
# with open(ABSTRACT.resolve(), "r", encoding="utf-8") as f:
#     abstract_text = f.read()
#
# with open(DESCRIPTION.resolve(), "r", encoding="utf-8") as f:
#     description_text = f.read()

# Create additional namespaces required for the ontology
GTFS = Namespace(f"{gtfs_owl_iri}#")
SCHEMA = Namespace("https://schema.org/")
BIBO = Namespace("http://purl.org/ontology/bibo/")
WIDOCO = Namespace("https://w3id.org/widoco/vocab#")

gtfs = get_ontology(gtfs_owl_iri)
gtfs_uri_ref = URIRef(gtfs_owl_iri)

# Ontology metadata
with gtfs:

    g = default_world.as_rdflib_graph()

    gtfs.metadata.label = [locstr(ONTOLOGY_PREFIX, "en")]
    
    g.add((gtfs_uri_ref, OWL.versionIRI, URIRef(f"{gtfs_owl_iri}/{ONTOLOGY_VERSION}")))
    g.add((gtfs_uri_ref, OWL.versionInfo, Literal(ONTOLOGY_VERSION)))
    g.add((gtfs_uri_ref, DCTERMS.title, Literal("A GTFS Application Ontology")))
    g.add((gtfs_uri_ref, DCTERMS.source, URIRef("https://gtfs.org/documentation/overview/")))
    g.add((gtfs_uri_ref, DCTERMS.license, URIRef("https://creativecommons.org/licenses/by/4.0")))
    g.add((gtfs_uri_ref, DCTERMS.created, Literal(creation_date, datatype=XSD.date)))
    g.add((gtfs_uri_ref, VANN.preferredNamespaceUri, gtfs_uri_ref))
    g.add((gtfs_uri_ref, VANN.preferredNamespacePrefix, Literal("dvla")))
    # g.add((bustimes_uri_ref, BIBO.doi, Literal("10.5281/zenodo.6940891"))) # TODO Change before release
    # g.add((gtfs_uri_ref, WIDOCO.introduction, Literal(intro_text)))
    # g.add((gtfs_uri_ref, DCTERMS.abstract, Literal(abstract_text)))
    # g.add((gtfs_uri_ref, DCTERMS.description, Literal(description_text)))

    # Add the annotation properties to comply with DL profile.
    g.add((DCTERMS.title, RDF.type, OWL.AnnotationProperty))
    g.add((DCTERMS.source, RDF.type, OWL.AnnotationProperty))
    g.add((DCTERMS.license, RDF.type, OWL.AnnotationProperty))
    g.add((DCTERMS.created, RDF.type, OWL.AnnotationProperty))
    g.add((VANN.preferredNamespaceUri, RDF.type, OWL.AnnotationProperty))
    g.add((VANN.preferredNamespacePrefix, RDF.type, OWL.AnnotationProperty))

    # Add the datatypes to comply with DL profile.
    g.add((XSD.date, RDF.type, RDFS.Datatype))
    g.add((XSD.time, RDF.type, RDFS.Datatype))

# Define the classes
with gtfs:

    class Agency(Thing):
        pass

    class Stop(Thing):
        pass

    class Route(Thing):
        pass

    class Trip(Thing):
        pass

    class StopTime(Thing):
        pass

    class Service(Thing):
        pass

    class CalendarService(Service):
        pass

    class CalendarDateService(Service):
        pass

    class FareMedium(Thing):
        pass

    class FareProduct(Thing):
        pass

    class Level(Thing):
        pass

    class Shape(Thing):
        pass

    class LocationGroup(Thing):
        pass

    class Location(Thing):
        pass

    class BookingRule(Thing):
        pass

    AllDisjoint([Agency, Stop, Route, Trip, StopTime, Service, CalendarService, CalendarDateService, Level, Shape, LocationGroup, Location, BookingRule])

with gtfs:

    class agency_id(DataProperty):
        comment = [locstr(definitions["agency_id"], "en")]
        label = [locstr("agency ID", "en")]
        domain = [Agency]
        range = [str]

    # Add the agency_id as the primary key
    list_node = BNode()
    Collection(g, list_node, [URIRef(agency_id.iri)])
    g.add((URIRef(Agency.iri), OWL.hasKey, list_node))

    class agency_name(DataProperty):
        comment = [locstr(definitions["agency_name"], "en")]
        label = [locstr("agency name", "en")]
        domain = [Agency]
        range = [str]

    class agency_url(DataProperty):
        comment = [locstr(definitions["agency_url"], "en")]
        label = [locstr("agency URL", "en")]
        domain = [Agency]
        range = [str]

    class agency_timezone(DataProperty):
        comment = [locstr(definitions["agency_timezone"], "en")]
        label = [locstr("agency timezone", "en")]
        domain = [Agency]
        range = [str]

    class agency_lang(DataProperty):
        comment = [locstr(definitions["agency_lang"], "en")]
        label = [locstr("agency language", "en")]
        domain = [Agency]
        range = [str]

    class agency_phone(DataProperty):
        comment = [locstr(definitions["agency_phone"], "en")]
        label = [locstr("agency phone number", "en")]
        domain = [Agency]
        range = [str]

    class agency_fare_url(DataProperty):
        comment = [locstr(definitions["agency_fare_url"], "en")]
        label = [locstr("agency fare URL", "en")]
        domain = [Agency]
        range = [str]

    class agency_email(DataProperty):
        comment = [locstr(definitions["agency_email"], "en")]
        label = [locstr("agency email address", "en")]
        domain = [Agency]
        range = [str]

    class cemv_support(DataProperty):
        comment = [locstr(definitions["cemv_support"], "en")]
        label = [locstr("CEMV Support", "en")]
        domain = [Agency | Route]
        range = [int]

with gtfs:

    class stop_id(DataProperty):
        # comment = [locstr(definitions["stop_id"], "en")]
        domain = [Stop]
        range = [str]

    class stop_code(DataProperty):
        domain = [Stop]
        range = [str]

    class stop_name(DataProperty):
        domain = [Stop]
        range = [str]

    class tts_stop_name(DataProperty):
        domain = [Stop]
        range = [str]

    class stop_desc(DataProperty):
        domain = [Stop]
        range = [str]

    class stop_lat(DataProperty):
        domain = [Stop]
        range = [float]

    class stop_lon(DataProperty):
        domain = [Stop]
        range = [float]

    class zone_id(DataProperty):
        domain = [Stop]
        range = [str]

    class stop_url(DataProperty):
        domain = [Stop]
        range = [str]

    class location_type(DataProperty):
        domain = [Stop]
        range = [int]

    class hasParentStation(ObjectProperty):
        domain = [Stop]
        range = [Stop]

    class isParentStationOf(ObjectProperty):
        domain = [Stop]
        range = [Stop]
        inverse_property = hasParentStation

    class stop_timezone(DataProperty):
        domain = [Stop]
        range = [str]

    class wheelchair_boarding(DataProperty):
        domain = [Stop]
        range = [int]

    class hasLevel(ObjectProperty):
        domain = [Stop]
        range = [Level]

    class platform_code(DataProperty):
        domain = [Stop]
        range = [str]

    class stop_access(DataProperty):
        domain = [Stop]
        range = [int]

with gtfs:

    class route_id(DataProperty):
        domain = [Route]
        range = [str]

    class operatedBy(ObjectProperty):
        domain = [Route]
        range = [Agency]

    class operatesRoute(ObjectProperty):
        inverse_property = operatedBy

    class route_short_name(DataProperty):
        domain = [Route]
        range = [str]

    class route_long_name(DataProperty):
        domain = [Route]
        range = [str]

    class route_desc(DataProperty):
        domain = [Route]
        range = [str]

    class route_type(DataProperty):
        domain = [Route]
        range = [int]

    class route_url(DataProperty):
        domain = [Route]
        range = [str]

    class route_color(DataProperty):
        domain = [Route]
        range = [str]

    class route_text_color(DataProperty):
        domain = [Route]
        range = [str]

    class route_sort_order(DataProperty):
        domain = [Route]
        range = [int]

    class continuous_pickup(DataProperty):
        domain = [Route | StopTime]
        range = [int]

    class continuous_drop_off(DataProperty):
        domain = [Route | StopTime]
        range = [int]

    class network_id(DataProperty):
        domain = [Route]
        range = [int]

with gtfs:

    class hasRoute(ObjectProperty):
        domain = [Trip]
        range = [Route]

    class hasService(ObjectProperty):
        domain = [Trip]
        range = [Service]

    class trip_id(DataProperty):
        domain = [Trip]
        range = [str]

    class trip_headsign(DataProperty):
        domain = [Trip]
        range = [str]

    class trip_short_name(DataProperty):
        domain = [Trip]
        range = [str]

    class direction_id(DataProperty):
        domain = [Trip]
        range = [int]

    class block_id(DataProperty):
        domain = [Trip]
        range = [str]

    class hasShape(ObjectProperty):
        domain = [Trip]
        range = [Shape]

    class wheelchair_accessible(DataProperty):
        domain = [Trip]
        range = [int]

    class bikes_allowed(DataProperty):
        domain = [Trip]
        range = [int]

    class cars_allowed(DataProperty):
        domain = [Trip]
        range = [int]

    class safe_duration_factor(DataProperty):
        domain = [Trip]
        range = [float]

    class safe_duration_offset(DataProperty):
        domain = [Trip]
        range = [float]

with gtfs:

    class hasTrip(ObjectProperty):
        domain = [StopTime]
        range = [Trip]

    class arrival_time(DataProperty):
        domain = [StopTime]
        range = [str]

    class departure_time(DataProperty):
        domain = [StopTime]
        range = [str]

    class hasStop(ObjectProperty):
        domain = [StopTime]
        range = [Stop]

    class hasLocationGroup(ObjectProperty):
        domain = [StopTime]
        range = [LocationGroup]

    class hasLocation(ObjectProperty):
        domain = [StopTime]
        range = [Location]

    class stop_sequence(DataProperty):
        domain = [StopTime]
        range = [str]

    class stop_headsign(DataProperty):
        domain = [StopTime]
        range = [str]

    class start_pickup_drop_off_window(DataProperty):
        domain = [StopTime]
        range = [datetime.time]

    class end_pickup_drop_off_window(DataProperty):
        domain = [StopTime]
        range = [datetime.time]

    class pickup_type(DataProperty):
        domain = [StopTime]
        range = [int]

    class drop_off_type(DataProperty):
        domain = [StopTime]
        range = [int]

    class shape_dist_traveled(DataProperty):
        domain = [StopTime]
        range = [float]

    class timepoint(DataProperty):
        domain = [StopTime]
        range = [int]

    class pickup_booking_rule_id(ObjectProperty):
        domain = [StopTime]
        range = [BookingRule]

    class drop_off_booking_rule_id(ObjectProperty):
        domain = [StopTime]
        range = [BookingRule]

with gtfs:

    class service_id(DataProperty):
        domain = [Service]
        range = [str]

    class monday(DataProperty):
        domain = [Service]
        range = [int]

    class tuesday(DataProperty):
        domain = [Service]
        range = [int]

    class wednesday(DataProperty):
        domain = [Service]
        range = [int]

    class thursday(DataProperty):
        domain = [Service]
        range = [int]

    class friday(DataProperty):
        domain = [Service]
        range = [int]

    class saturday(DataProperty):
        domain = [Service]
        range = [int]

    class sunday(DataProperty):
        domain = [Service]
        range = [int]

    class start_date(DataProperty):
        domain = [Service]
        range = [datetime.date]

    class end_date(DataProperty):
        domain = [Service]
        range = [datetime.date]

    class date(DataProperty):
        domain = [Service]
        range = [datetime.date]

    class exception_type(DataProperty):
        domain = [Service]
        range = [int]

def build_ontology():

    with tempfile.NamedTemporaryFile(suffix=".rdf", delete=True) as tmp:
        gtfs.save(file=tmp.name)

        g = Graph()
        g.parse(tmp.name, format="xml")

        g.bind("", GTFS)
        g.bind("widoco", WIDOCO)

        g.serialize(ONTOLOGY_FILE.resolve(), format="ttl")

    return gtfs