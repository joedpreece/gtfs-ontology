from typing import List

from owlready2 import PropertyClass, ThingClass, Thing, Or
from rdflib import Namespace, URIRef, Graph, RDF, BNode, Literal

from gtfs_ontology import gtfs_rml_iri, gtfs_owl_iri, gtfs_kg_iri, MAPPINGS_DIR, \
    AGENCY_RML_FILE, STOP_RML_FILE, ROUTE_RML_FILE, TRIP_RML_FILE, STOP_TIME_RML_FILE
from gtfs_ontology.ontologies import Agency, agency_id, agency_name, agency_url, \
    agency_timezone, agency_lang, agency_phone, agency_fare_url, agency_email, \
    cemv_support, Stop, stop_id, stop_code, stop_name, tts_stop_name, stop_desc, \
    stop_lat, stop_lon, zone_id, stop_url, \
    location_type, parent_station, stop_timezone, wheelchair_boarding, platform_code, \
    stop_access, hasLevel, Route, route_id, route_short_name, route_long_name, \
    route_desc, route_type, route_url, route_color, route_text_color, route_sort_order, \
    continuous_pickup, continuous_drop_off, network_id, operatedBy, hasRoute, hasService, \
    hasShape, trip_headsign, trip_short_name, direction_id, block_id, \
    wheelchair_accessible, bikes_allowed, cars_allowed, safe_duration_factor, \
    safe_duration_offset, trip_id, Trip, hasStop, hasLocation, hasLocationGroup, \
    arrival_time, departure_time, stop_sequence, stop_headsign, \
    start_pickup_drop_off_window, end_pickup_drop_off_window, pickup_type, \
    drop_off_type, shape_dist_traveled, timepoint, pickup_booking_rule_id, \
    drop_off_booking_rule_id

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
        csv_name="stops.txt",
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

def build_route_mapping():

    g = create_graph()

    triples_map = create_triples_map("RouteMapping", g)

    add_logical_source(
        g=g,
        triples_map=triples_map,
        csv_name="routes.txt",
    )

    add_subject_map(
        g=g,
        triples_map=triples_map,
        template=f"{gtfs_kg_iri}/Route/{{route_id}}",
        cost_model_classes=[Route],
    )

    data_properties = [
        ("route_id", route_id),
        ("route_short_name", route_short_name),
        ("route_long_name", route_long_name),
        ("route_desc", route_desc),
        ("route_type", route_type),
        ("route_url", route_url),
        ("route_color", route_color),
        ("route_text_color", route_text_color),
        ("route_sort_order", route_sort_order),
        ("continuous_pickup", continuous_pickup),
        ("continuous_drop_off", continuous_drop_off),
        ("network_id", network_id),
        ("cemv_support", cemv_support),
    ]

    object_properties = [
        (operatedBy, f"{gtfs_kg_iri}/Agency/{{agency_id}}"),
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

    g.serialize((ROUTE_RML_FILE).resolve(), format="ttl")

def build_trips_mapping():

    g = create_graph()

    triples_map = create_triples_map("TripMapping", g)

    add_logical_source(
        g=g,
        triples_map=triples_map,
        csv_name="trips.txt",
    )

    add_subject_map(
        g=g,
        triples_map=triples_map,
        template=f"{gtfs_kg_iri}/Trip/{{trip_id}}",
        cost_model_classes=[Trip],
    )

    data_properties = [
        ("trip_id", trip_id),
        ("trip_headsign", trip_headsign),
        ("trip_short_name", trip_short_name),
        ("direction_id", direction_id),
        ("block_id", block_id),
        ("wheelchair_accessible", wheelchair_accessible),
        ("bikes_allowed", bikes_allowed),
        ("cars_allowed", cars_allowed),
        ("safe_duration_factor", safe_duration_factor),
        ("safe_duration_offset", safe_duration_offset),
    ]

    object_properties = [
        (hasRoute, f"{gtfs_kg_iri}/Route/{{route_id}}"),
        (hasService, f"{gtfs_kg_iri}/Service/{{service_id}}"),
        (hasShape, f"{gtfs_kg_iri}/Shape/{{shape_id}}"),
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

    g.serialize((TRIP_RML_FILE).resolve(), format="ttl")

def build_stop_time_mapping():

    g = create_graph()

    triples_map = create_triples_map("StopTimeMapping", g)

    add_logical_source(
        g=g,
        triples_map=triples_map,
        csv_name="stop_times.txt",
    )

    add_subject_map(
        g=g,
        triples_map=triples_map,
        template=f"{gtfs_kg_iri}/StopTime/{{trip_id}}_{{stop_sequence}}",
        cost_model_classes=[Trip],
    )

    data_properties = [
        ("trip_id", trip_id),
        ("arrival_time", arrival_time),
        ("departure_time", departure_time),
        ("stop_sequence", stop_sequence),
        ("stop_headsign", stop_headsign),
        ("start_pickup_drop_off_window", start_pickup_drop_off_window),
        ("end_pickup_drop_off_window", end_pickup_drop_off_window),
        ("pickup_type", pickup_type),
        ("drop_off_type", drop_off_type),
        ("continuous_pickup", continuous_pickup),
        ("continuous_drop_off", continuous_drop_off),
        ("shape_dist_traveled", shape_dist_traveled),
        ("timepoint", timepoint),
    ]

    object_properties = [
        (hasStop, f"{gtfs_kg_iri}/Stop/{{stop_id}}"),
        (hasLocation, f"{gtfs_kg_iri}/Location/{{location_id}}"),
        (hasLocationGroup, f"{gtfs_kg_iri}/LocationGroup/{{location_group_id}}"),
        (pickup_booking_rule_id, f"{gtfs_kg_iri}/BookingRule/{{pickup_booking_rule_id}}"),
        (drop_off_booking_rule_id, f"{gtfs_kg_iri}/BookingRule/{{drop_off_booking_rule_id}}"),
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

    g.serialize((STOP_TIME_RML_FILE).resolve(), format="ttl")
