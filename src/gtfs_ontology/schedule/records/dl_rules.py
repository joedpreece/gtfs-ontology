from gtfs_ontology.schedule import *
from gtfs_ontology.schedule.records.generate import *

with gtfs:

    AllDisjoint([
        Agency,
        Stop,
        Route,
        Service,
        StopTime,
        Trip
    ])