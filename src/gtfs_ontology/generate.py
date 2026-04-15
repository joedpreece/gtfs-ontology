from pathlib import Path

from gtfs_ontology.core import gtfs

import gtfs_ontology.schedule.core

# import gtfs_ontology.schedule.term_definitions.generate
# import gtfs_ontology.schedule.field_types.generate
# import gtfs_ontology.schedule.files.generate
# import gtfs_ontology.schedule.records.generate

import gtfs_ontology.schedule.agencies.generate
# import gtfs_ontology.schedule.stops.generate
# import gtfs_ontology.schedule.routes.generate

# import gtfs_ontology.schedule.stops
# import gtfs_ontology.schedule.routes
# import gtfs_ontology.schedule.trips

# import gtfs_ontology.realtime.core
# import gtfs_ontology.realtime.feed_message
# import gtfs_ontology.realtime.feed_header
# import gtfs_ontology.realtime.feed_entity
# import gtfs_ontology.realtime.trip_update
# import gtfs_ontology.realtime.stop_time_event
# import gtfs_ontology.realtime.stop_time_update
# import gtfs_ontology.realtime.stop_time_properties
# import gtfs_ontology.realtime.trip_properties
# import gtfs_ontology.realtime.vehicle_position
# import gtfs_ontology.realtime.alert

def generate_ontology(
        path: Path
):
    gtfs.save(file=str(path.resolve()))