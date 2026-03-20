from pathlib import Path

from gtfs_ontology.core import gtfs

import gtfs_ontology.schedule.core
import gtfs_ontology.schedule.agencies
import gtfs_ontology.schedule.stops
import gtfs_ontology.schedule.routes
import gtfs_ontology.schedule.trips

import gtfs_ontology.realtime.core
import gtfs_ontology.realtime.feed_message
import gtfs_ontology.realtime.feed_header
import gtfs_ontology.realtime.feed_entity
import gtfs_ontology.realtime.trip_update

def generate_ontology(
        path: Path
):
    gtfs.save(file=str(path.resolve()))