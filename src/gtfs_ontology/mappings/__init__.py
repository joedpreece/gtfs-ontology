from typing import List

from owlready2 import PropertyClass, ThingClass, Thing, Or
from rdflib import Namespace, URIRef, Graph, RDF, BNode, Literal

from gtfs_ontology import gtfs_rml_iri, gtfs_owl_iri, gtfs_kg_iri, MAPPINGS_DIR, \
    AGENCY_RML_FILE, STOP_RML_FILE
from gtfs_ontology.ontologies import Agency, agency_id, agency_name, agency_url, \
    agency_timezone, agency_lang, agency_phone, agency_fare_url, agency_email, \
    cemv_support, Stop, stop_id, stop_code, stop_name, tts_stop_name, stop_desc, stop_lat, stop_lon, zone_id, stop_url, \
    location_type, parent_station, stop_timezone, wheelchair_boarding, platform_code, stop_access, hasLevel

GTFS_RML = Namespace(f"{gtfs_rml_iri}#")
gtfs_rml_uri_ref = URIRef(gtfs_rml_iri)

RR = Namespace("http://www.w3.org/ns/r2rml#")
RML = Namespace("http://semweb.mmlab.be/ns/rml#")
SD = Namespace("https://w3id.org/okn/o/sd#")
GTFS = Namespace(f"{gtfs_owl_iri}#")

def create_graph():
    g = Graph()

    g.bind("", GTFS_RML)
    g.bind("gtfs", GTFS)
    g.bind("rr", RR)
    g.bind("rml", RML)
    g.bind("sd", SD)

    return g

def create_triples_map(
        name: str,
        g: Graph
):
    g.add((
        GTFS_RML[name],
        RDF.type,
        RR.TriplesMap,
    ))

    return GTFS_RML[name]

def add_logical_source(
        g: Graph,
        triples_map: URIRef,
        csv_name: str,
):
    logical_source = BNode()
    source = BNode()

    g.add((source, RDF.type, SD.DatasetSpecification))
    g.add((source, SD.name, Literal(csv_name)))

    g.add((logical_source, RML.source, source))
    g.add((logical_source, RML.referenceFormulation, RML.CSV))

    g.add((triples_map, RML.logicalSource, logical_source))

def add_subject_map(
        g: Graph,
        triples_map: URIRef,
        template: str,
        cost_model_classes: List,
):
    subject_map = BNode()
    g.add((subject_map, RR.template, Literal(template)))

    for cost_model_class in cost_model_classes:
        g.add((subject_map, RR["class"], URIRef(cost_model_class.iri)))
    g.add((triples_map, RR.subjectMap, subject_map))

def add_predicate_object_map_data_property(
        g: Graph,
        triples_map: URIRef,
        column_name: str,
        cost_model_property,
):

    predicate_object_map = BNode()

    g.add((predicate_object_map, RR.predicate, URIRef(cost_model_property.iri)))
    object_map = BNode()
    g.add((object_map, RML.reference, Literal(column_name)))
    g.add((object_map, RR.datatype, URIRef(cost_model_property.range_iri[0])))

    g.add((predicate_object_map, RR.objectMap, object_map))
    g.add((triples_map, RR.predicateObjectMap, predicate_object_map))

def add_predicate_object_map_object_property(
        g: Graph,
        triples_map: URIRef,
        cost_model_property: PropertyClass,
        template: str,
):

    predicate_object_map = BNode()
    g.add((predicate_object_map, RR.predicate, URIRef(cost_model_property.iri)))

    object_map = BNode()
    g.add((object_map, RR.template, Literal(template)))
    g.add((object_map, RR.termType, RR.IRI))

    g.add((predicate_object_map, RR.objectMap, object_map))
    g.add((triples_map, RR.predicateObjectMap, predicate_object_map))

    return predicate_object_map


def build_agency_mapping():

    g = create_graph()

    triples_map = create_triples_map("AgencyMapping", g)

    add_logical_source(
        g=g,
        triples_map=triples_map,
        csv_name="agency.txt",
    )

    add_subject_map(
        g=g,
        triples_map=triples_map,
        template=f"{gtfs_kg_iri}/Agency/{{agency_id}}",
        cost_model_classes=[Agency],
    )

    data_properties = [
        ("agency_id", agency_id),
        ("agency_name", agency_name),
        ("agency_url", agency_url),
        ("agency_timezone", agency_timezone),
        ("agency_lang", agency_lang),
        ("agency_phone", agency_phone),
        ("agency_fare_url", agency_fare_url),
        ("agency_email", agency_email),
        ("cemv_support", cemv_support),
    ]

    for column_name, data_property in data_properties:
        add_predicate_object_map_data_property(
            g=g,
            triples_map=triples_map,
            column_name=column_name,
            cost_model_property=data_property,
        )

    g.serialize((AGENCY_RML_FILE).resolve(), format="ttl")


def build_stop_mapping():

    g = create_graph()

    triples_map = create_triples_map("StopMapping", g)

    add_logical_source(
        g=g,
        triples_map=triples_map,
        csv_name="stop.txt",
    )

    add_subject_map(
        g=g,
        triples_map=triples_map,
        template=f"{gtfs_kg_iri}/Stop/{{stop_id}}",
        cost_model_classes=[Stop],
    )

    data_properties = [
        ("stop_id", stop_id),
        ("stop_code", stop_code),
        ("stop_name", stop_name),
        ("tts_stop_name", tts_stop_name),
        ("stop_desc", stop_desc),
        ("stop_lat", stop_lat),
        ("stop_lon", stop_lon),
        ("zone_id", zone_id),
        ("stop_url", stop_url),
        ("location_type", location_type),
        ("stop_timezone", stop_timezone),
        ("wheelchair_boarding", wheelchair_boarding),
        ("platform_code", platform_code),
        ("stop_access", stop_access),
    ]

    object_properties = [
        (parent_station, f"{gtfs_kg_iri}/Stop/{{stop_id}}"),
        (hasLevel, f"{gtfs_kg_iri}/Level/{{level_id}}"),
    ]

    for column_name, data_property in data_properties:
        add_predicate_object_map_data_property(
            g=g,
            triples_map=triples_map,
            column_name=column_name,
            cost_model_property=data_property,
        )

    for property, template in object_properties:
        add_predicate_object_map_object_property(
            g=g,
            triples_map=triples_map,
            cost_model_property=property,
            template=template,
        )

    g.serialize((STOP_RML_FILE).resolve(), format="ttl")
