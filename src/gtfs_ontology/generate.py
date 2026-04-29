from pathlib import Path

from rdflib import Namespace, Graph
from rdflib.namespace import NamespaceManager

from gtfs_ontology.core import gtfs

import gtfs_ontology.core
import gtfs_ontology.schedule.core

import gtfs_ontology.schedule.term_definitions.generate

import gtfs_ontology.schedule.files.generate
import gtfs_ontology.schedule.files.dl_rules

import gtfs_ontology.schedule.field_types.generate
import gtfs_ontology.schedule.records.generate

import gtfs_ontology.schedule.agencies.generate
import gtfs_ontology.schedule.agencies.dl_rules

import gtfs_ontology.schedule.stops.generate
import gtfs_ontology.schedule.stops.dl_rules

import gtfs_ontology.schedule.routes.generate
import gtfs_ontology.schedule.routes.dl_rules

import gtfs_ontology.schedule.trips.generate
import gtfs_ontology.schedule.trips.dl_rules

import gtfs_ontology.schedule.stop_times.generate
import gtfs_ontology.schedule.stop_times.dl_rules

import gtfs_ontology.schedule.calendar.generate
import gtfs_ontology.schedule.calendar.dl_rules

import gtfs_ontology.schedule.calendar_dates.generate
import gtfs_ontology.schedule.calendar_dates.dl_rules

def generate_ontology(
        path: Path
):

    gtfs.save(file=str(path.resolve()))

    g = Graph()
    g.parse(str(path.resolve()), format="xml")
    path.unlink()

    new_manager = NamespaceManager(g)
    g.namespace_manager = new_manager

    g.bind("gtfs_linked", Namespace("http://vocab.gtfs.org/terms#"), override=True)
    g.serialize(destination="artifacts/gtfs.ttl", format="turtle")