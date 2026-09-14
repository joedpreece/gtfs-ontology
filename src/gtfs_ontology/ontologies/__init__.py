import pandas as pd
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

# region Ontology metadata
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

# region Add the datatypes to comply with DL profile.

with gtfs:

    # g.add((XSD.date, RDF.type, RDFS.Datatype))
    # g.add((XSD.time, RDF.type, RDFS.Datatype))

    class color(Datatype):
        equivalent_to = [
            ConstrainedDatatype(base_datatype=str, pattern=r"^[0-9A-F]{6}$")
        ]
    g.add((URIRef(color.iri), RDFS.label, Literal("color", "en")))

    class currency_code(Datatype):
        dfs = pd.read_html("https://en.wikipedia.org/wiki/ISO_4217#Active_codes",
                           storage_options={'User-Agent': 'Mozilla/5.0'})
        equivalent_to = [OneOf(dfs[1]["Code"].tolist())]
    g.add((URIRef(currency_code.iri), RDFS.label, Literal("currency code", "en")))

    class currency_amount(Datatype):
        equivalent_to = [
            ConstrainedDatatype(base_datatype=str)
        ]
    g.add((URIRef(currency_amount.iri), RDFS.label, Literal("currency amount", "en")))

    class dateType(Datatype):
        equivalent_to = [
            ConstrainedDatatype(base_datatype=str, pattern=r"^\d{4}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])$")
        ]
    g.add((URIRef(dateType.iri), RDFS.label, Literal("date", "en")))

    class email(Datatype):
        equivalent_to = [
            ConstrainedDatatype(base_datatype=str, pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
        ]
    g.add((URIRef(email.iri), RDFS.label, Literal("email", "en")))

    class id(Datatype):
        pass
    g.add((URIRef(id.iri), RDFS.label, Literal("id", "en")))
    g.add((URIRef(id.iri), OWL.equivalentClass, XSD.string))

    class language_code(Datatype):
        equivalent_to = [
            ConstrainedDatatype(base_datatype=str, pattern=r"^[A-Za-z]{2,3}(?:-[A-Za-z0-9]{2,8})*$")
        ]
    g.add((URIRef(language_code.iri), RDFS.label, Literal("language code", "en")))

    class latitude(Datatype):
        equivalent_to = [
            ConstrainedDatatype(base_datatype=float, min_inclusive=-90, max_inclusive=90)
        ]
    g.add((URIRef(language_code.iri), RDFS.label, Literal("latitude", "en")))

    class longitude(Datatype):
        equivalent_to = [
            ConstrainedDatatype(base_datatype=float, min_inclusive=-180, max_inclusive=180)
        ]
    g.add((URIRef(language_code.iri), RDFS.label, Literal("longitude", "en")))

    class nonNegativeFloat(Datatype):
        equivalent_to = [
            ConstrainedDatatype(base_datatype=float, min_inclusive=0)
        ]
    g.add((URIRef(nonNegativeFloat.iri), RDFS.label, Literal("non-negative float", "en")))

    class phone_number(Datatype):
        equivalent_to = [
            ConstrainedDatatype(base_datatype=str, pattern=r"^\+?[1-9]\d{1,14}$")
        ]
    g.add((URIRef(phone_number.iri), RDFS.label, Literal("phone number", "en")))

    class time(Datatype):
        equivalent_to = [
            ConstrainedDatatype(base_datatype=str, pattern=r"^\d+:[0-5]\d:[0-5]\d$")
        ]
    g.add((URIRef(time.iri), RDFS.label, Literal("time", "en")))

    class local_time(Datatype):
        equivalent_to = [
            ConstrainedDatatype(base_datatype=str, pattern=r"^\d+:[0-5]\d:[0-5]\d$")
        ]
    g.add((URIRef(local_time.iri), RDFS.label, Literal("local time", "en")))

    class text(Datatype):
        pass
    g.add((URIRef(text.iri), RDFS.label, Literal("text", "en")))
    g.add((URIRef(id.iri), OWL.equivalentClass, XSD.string))

    class timezone(Datatype):
        dfs = pd.read_html(
            "https://en.wikipedia.org/wiki/List_of_tz_database_time_zones",
            storage_options={'User-Agent': 'Mozilla/5.0'})
        equivalent_to = [OneOf(dfs[0][('TZ identifier', 'TZ identifier')].tolist())]
    g.add((URIRef(timezone.iri), RDFS.label, Literal("timezone", "en")))

    class url(Datatype):
        equivalent_to = [
            ConstrainedDatatype(base_datatype=str, pattern=r"^https?:\/\/(?:www\.)?[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?:\/[^\s]*)?$")
        ]
    g.add((URIRef(url.iri), RDFS.label, Literal("url", "en")))

# region Define the classes
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

    AllDisjoint([Agency, Stop, Route, Trip, StopTime, Service, Level, Shape, LocationGroup, Location, BookingRule])

    AllDisjoint(
        [CalendarService, CalendarDateService])



# region Agency
with gtfs:

    class agency_id(DataProperty, FunctionalProperty):
        comment = [locstr(definitions["agency_id"], "en")]
        label = [locstr("agency ID", "en")]
        domain = [Agency]
        range = [id]

    # Add the agency_id as the primary key
    list_node = BNode()
    Collection(g, list_node, [URIRef(agency_id.iri)])
    g.add((URIRef(Agency.iri), OWL.hasKey, list_node))

    class agency_name(DataProperty, FunctionalProperty):
        comment = [locstr(definitions["agency_name"], "en")]
        label = [locstr("agency name", "en")]
        domain = [Agency]
        range = [text]

    class agency_url(DataProperty, FunctionalProperty):
        comment = [locstr(definitions["agency_url"], "en")]
        label = [locstr("agency URL", "en")]
        domain = [Agency]
        range = [url]

    class agency_timezone(DataProperty, FunctionalProperty):
        comment = [locstr(definitions["agency_timezone"], "en")]
        label = [locstr("agency timezone", "en")]
        domain = [Agency]
        range = [timezone]

    class agency_lang(DataProperty, FunctionalProperty):
        comment = [locstr(definitions["agency_lang"], "en")]
        label = [locstr("agency language", "en")]
        domain = [Agency]
        range = [language_code]

    class agency_phone(DataProperty, FunctionalProperty):
        comment = [locstr(definitions["agency_phone"], "en")]
        label = [locstr("agency phone number", "en")]
        domain = [Agency]
        range = [phone_number]

    class agency_fare_url(DataProperty, FunctionalProperty):
        comment = [locstr(definitions["agency_fare_url"], "en")]
        label = [locstr("agency fare URL", "en")]
        domain = [Agency]
        range = [url]

    class agency_email(DataProperty, FunctionalProperty):
        comment = [locstr(definitions["agency_email"], "en")]
        label = [locstr("agency email address", "en")]
        domain = [Agency]
        range = [email]

    class cemv_support(DataProperty, FunctionalProperty):
        comment = [locstr(definitions["cemv_support"], "en")]
        label = [locstr("CEMV Support", "en")]
        domain = [Or([Agency, Route])]
        range = [OneOf([0, 1, 2])]

    class CEMVSupportedRecord(Thing):
        pass

    class CEMVUnsupportedRecord(Thing):
        pass

# region Stops

with gtfs:

    class stop_id(DataProperty, FunctionalProperty):
        # comment = [locstr(definitions["stop_id"], "en")]
        domain = [Stop]
        range = [id]

    # Add the stop_id as the primary key
    list_node = BNode()
    Collection(g, list_node, [URIRef(stop_id.iri)])
    g.add((URIRef(Stop.iri), OWL.hasKey, list_node))

    class stop_code(DataProperty, FunctionalProperty):
        domain = [Stop]
        range = [text]

    class stop_name(DataProperty, FunctionalProperty):
        domain = [Stop]
        range = [text]

    class tts_stop_name(DataProperty, FunctionalProperty):
        domain = [Stop]
        range = [text]

    class stop_desc(DataProperty, FunctionalProperty):
        domain = [Stop]
        range = [text]

    class stop_lat(DataProperty, FunctionalProperty):
        domain = [Stop]
        range = [latitude]

    class stop_lon(DataProperty, FunctionalProperty):
        domain = [Stop]
        range = [longitude]

    class zone_id(DataProperty, FunctionalProperty):
        domain = [Stop]
        range = [id]

    class stop_url(DataProperty, FunctionalProperty):
        domain = [Stop]
        range = [url]

    class location_type(DataProperty, FunctionalProperty):
        domain = [Stop]
        range = [OneOf([0, 1, 2, 3, 4])]

    class hasParentStation(ObjectProperty, FunctionalProperty):
        domain = [Stop]
        range = [Stop]

    class isParentStationOf(ObjectProperty):
        domain = [Stop]
        range = [Stop]
        inverse_property = hasParentStation

    class stop_timezone(DataProperty, FunctionalProperty):
        domain = [Stop]
        range = [timezone]

    class wheelchair_boarding(DataProperty, FunctionalProperty):
        domain = [Stop]
        range = [OneOf([0, 1, 2])]

    class hasLevel(ObjectProperty, FunctionalProperty):
        domain = [Stop]
        range = [Level]

    class platform_code(DataProperty, FunctionalProperty):
        domain = [Stop]
        range = [text]

    class stop_access(DataProperty, FunctionalProperty):
        domain = [Stop]
        range = [OneOf([0, 1])]

# region Stop DL

    class ParentlessStop(Stop):
        equivalent_to = [
            Stop &
            hasParentStation.exactly(0)
        ]

    class ChildStop(Stop):
        equivalent_to = [
            Stop &
            hasParentStation.exactly(1)
        ]

    AllDisjoint([ParentlessStop, ChildStop])

    class StopOrPlatform(Stop):
        is_a = [
            stop_name.exactly(1),
            stop_lat.exactly(1),
            stop_lon.exactly(1),
        ]
        equivalent_to = [
            And([
                Stop,
                Or([
                    location_type.value(0),
                    location_type.exactly(0)
                ])
            ])

        ]

    class StopLocation(StopOrPlatform):
        equivalent_to = [
            StopOrPlatform &
            ParentlessStop
        ]

    class Platform(StopOrPlatform):
        equivalent_to = [
            StopOrPlatform &
            ChildStop
        ]

    class Station(ParentlessStop):
        is_a = [
            stop_name.exactly(1),
            stop_lat.exactly(1),
            stop_lon.exactly(1),
        ]
        equivalent_to = [
            Stop &
            location_type.value(1)
        ]

    class EntranceOrExit(ChildStop):
        is_a = [
            stop_name.exactly(1),
            stop_lat.exactly(1),
            stop_lon.exactly(1),
        ]
        equivalent_to = [
            Stop &
            location_type.value(2)
        ]

    class GenericNode(ChildStop):
        equivalent_to = [
            Stop &
            location_type.value(3)
        ]

    class BoardingArea(ChildStop):
        equivalent_to = [
            Stop &
            location_type.value(4)
        ]

    AllDisjoint([StopLocation, Platform, Station, EntranceOrExit, GenericNode, BoardingArea])

# region Routes

with gtfs:

    class route_id(DataProperty, FunctionalProperty):
        domain = [Route]
        range = [id]

    # Add the route_id as the primary key
    list_node = BNode()
    Collection(g, list_node, [URIRef(route_id.iri)])
    g.add((URIRef(Route.iri), OWL.hasKey, list_node))

    class operatedBy(ObjectProperty, FunctionalProperty):
        domain = [Route]
        range = [Agency]

    class operatesRoute(ObjectProperty):
        inverse_property = operatedBy

    class route_short_name(DataProperty, FunctionalProperty):
        domain = [Route]
        range = [text]

    class route_long_name(DataProperty, FunctionalProperty):
        domain = [Route]
        range = [text]

    class route_desc(DataProperty, FunctionalProperty):
        domain = [Route]
        range = [text]

    class route_type(DataProperty, FunctionalProperty):
        domain = [Route]
        range = [OneOf([0, 1, 2, 3, 4, 5, 6, 7, 11, 12])]

    class route_url(DataProperty, FunctionalProperty):
        domain = [Route]
        range = [url]

    class route_color(DataProperty, FunctionalProperty):
        domain = [Route]
        range = [color]

    class route_text_color(DataProperty, FunctionalProperty):
        domain = [Route]
        range = [color]

    class route_sort_order(DataProperty, FunctionalProperty):
        domain = [Route]
    g.add((URIRef(route_sort_order.iri), RDFS.range, XSD.nonNegativeInteger))

    class continuous_pickup(DataProperty, FunctionalProperty):
        domain = [Or([Route, StopTime])]
        range = [OneOf([0, 1, 2, 3])]

    class continuous_drop_off(DataProperty, FunctionalProperty):
        domain = [Or([Route, StopTime])]
        range = [OneOf([0, 1, 2, 3])]

    class network_id(DataProperty, FunctionalProperty):
        domain = [Route]
        range = [id]

# region Trips

with gtfs:

    class hasRoute(ObjectProperty, FunctionalProperty):
        domain = [Trip]
        range = [Route]

    class hasService(ObjectProperty, FunctionalProperty):
        domain = [Trip]
        range = [Service]

    class trip_id(DataProperty, FunctionalProperty):
        domain = [Trip]
        range = [id]

    # Add the trip_id as the primary key
    list_node = BNode()
    Collection(g, list_node, [URIRef(trip_id.iri)])
    g.add((URIRef(Trip.iri), OWL.hasKey, list_node))

    class trip_headsign(DataProperty, FunctionalProperty):
        domain = [Trip]
        range = [text]

    class trip_short_name(DataProperty, FunctionalProperty):
        domain = [Trip]
        range = [text]

    class direction_id(DataProperty, FunctionalProperty):
        domain = [Trip]
        range = [OneOf([0, 1])]

    class block_id(DataProperty, FunctionalProperty):
        domain = [Trip]
        range = [id]

    class hasShape(ObjectProperty, FunctionalProperty):
        domain = [Trip]
        range = [Shape]

    class wheelchair_accessible(DataProperty, FunctionalProperty):
        domain = [Trip]
        range = [OneOf([0, 1, 2])]

    class bikes_allowed(DataProperty, FunctionalProperty):
        domain = [Trip]
        range = [OneOf([0, 1, 2])]

    class cars_allowed(DataProperty, FunctionalProperty):
        domain = [Trip]
        range = [OneOf([0, 1, 2])]

    class safe_duration_factor(DataProperty, FunctionalProperty):
        domain = [Trip]
        range = [float]

    class safe_duration_offset(DataProperty, FunctionalProperty):
        domain = [Trip]
        range = [float]

# region Stop Times

with gtfs:

    class hasTrip(ObjectProperty, FunctionalProperty):
        domain = [StopTime]
        range = [Trip]

    class arrival_time(DataProperty, FunctionalProperty):
        domain = [StopTime]
        range = [time]

    class departure_time(DataProperty, FunctionalProperty):
        domain = [StopTime]
        range = [time]

    class hasStop(ObjectProperty, FunctionalProperty):
        domain = [StopTime]
        range = [Stop]

    class hasLocationGroup(ObjectProperty, FunctionalProperty):
        domain = [StopTime]
        range = [LocationGroup]

    class hasLocation(ObjectProperty, FunctionalProperty):
        domain = [StopTime]
        range = [Location]

    class stop_sequence(DataProperty, FunctionalProperty):
        domain = [StopTime]
    g.add((URIRef(stop_sequence.iri), RDFS.range, XSD.nonNegativeInteger))

    # Add the trip_id and stop_sequence as the primary key
    list_node = BNode()
    Collection(g, list_node, [URIRef(stop_sequence.iri), URIRef(hasTrip.iri)])
    g.add((URIRef(StopTime.iri), OWL.hasKey, list_node))

    class stop_headsign(DataProperty, FunctionalProperty):
        domain = [StopTime]
        range = [text]

    class start_pickup_drop_off_window(DataProperty, FunctionalProperty):
        domain = [StopTime]
        range = [time]

    class end_pickup_drop_off_window(DataProperty, FunctionalProperty):
        domain = [StopTime]
        range = [time]

    class pickup_type(DataProperty, FunctionalProperty):
        domain = [StopTime]
        range = [OneOf([0, 1, 2, 3])]

    class drop_off_type(DataProperty, FunctionalProperty):
        domain = [StopTime]
        range = [OneOf([0, 1, 2, 3])]

    class shape_dist_traveled(DataProperty, FunctionalProperty):
        domain = [StopTime]
        range = [nonNegativeFloat]

    class timepoint(DataProperty, FunctionalProperty):
        domain = [StopTime]
        range = [OneOf([0, 1])]

    class pickup_booking_rule_id(ObjectProperty, FunctionalProperty):
        domain = [StopTime]
        range = [BookingRule]

    class drop_off_booking_rule_id(ObjectProperty, FunctionalProperty):
        domain = [StopTime]
        range = [BookingRule]

# region Services

with gtfs:

    class service_id(DataProperty, FunctionalProperty):
        domain = [Service]
        range = [id]

    # Add the trip_id and stop_sequence as the primary key
    list_node = BNode()
    Collection(g, list_node, [URIRef(service_id.iri)])
    g.add((URIRef(CalendarService.iri), OWL.hasKey, list_node))

    class monday(DataProperty, FunctionalProperty):
        domain = [CalendarService]
        range = [OneOf([0, 1])]

    class tuesday(DataProperty, FunctionalProperty):
        domain = [CalendarService]
        range = [OneOf([0, 1])]

    class wednesday(DataProperty, FunctionalProperty):
        domain = [CalendarService]
        range = [OneOf([0, 1])]

    class thursday(DataProperty, FunctionalProperty):
        domain = [CalendarService]
        range = [OneOf([0, 1])]

    class friday(DataProperty, FunctionalProperty):
        domain = [CalendarService]
        range = [OneOf([0, 1])]

    class saturday(DataProperty, FunctionalProperty):
        domain = [CalendarService]
        range = [OneOf([0, 1])]

    class sunday(DataProperty, FunctionalProperty):
        domain = [CalendarService]
        range = [OneOf([0, 1])]

    class start_date(DataProperty, FunctionalProperty):
        domain = [CalendarService]
        range = [dateType]

    class end_date(DataProperty, FunctionalProperty):
        domain = [CalendarService]
        range = [dateType]

    class date(DataProperty, FunctionalProperty):
        domain = [CalendarDateService]
        range = [dateType]

    # Add the trip_id and stop_sequence as the primary key
    list_node = BNode()
    Collection(g, list_node, [URIRef(service_id.iri), URIRef(date.iri)])
    g.add((URIRef(CalendarDateService.iri), OWL.hasKey, list_node))

    class exception_type(DataProperty, FunctionalProperty):
        domain = [CalendarDateService]
        range = [OneOf([1, 2])]

def build_ontology():

    with tempfile.NamedTemporaryFile(suffix=".rdf", delete=True) as tmp:
        gtfs.save(file=tmp.name)

        g = Graph()
        g.parse(tmp.name, format="xml")

        g.bind("", GTFS)
        g.bind("widoco", WIDOCO)

        g.serialize(ONTOLOGY_FILE.resolve(), format="ttl")

    return gtfs