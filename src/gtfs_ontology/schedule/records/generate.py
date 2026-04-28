from gtfs_ontology.schedule import *
from gtfs_ontology.schedule.term_definitions.generate import Record

with gtfs:

    class Agency(Record, foaf.Agent):
        seeAlso = ["https://gtfs.org/documentation/schedule/reference/#agencytxt"]
        closeMatch = [gtfs_linked.Agency]


    class Stop(Record, geo.SpatialThing):
        seeAlso = ["https://gtfs.org/documentation/schedule/reference/#stopstxt"]
        closeMatch = [gtfs_linked.Stop]

    class Route(Record):
        seeAlso = ["https://gtfs.org/documentation/schedule/reference/#routestxt"]
        closeMatch = [gtfs_linked.Route]

    class Trip(Record):
        seeAlso = ["https://gtfs.org/documentation/schedule/reference/#tripstxt"]
        closeMatch = [gtfs_linked.Trip]

    class StopTime(Record):
        seeAlso = ["https://gtfs.org/documentation/schedule/reference/#stop_timestxt"]
        closeMatch = [gtfs_linked.StopTime]

    class Service(Record):
        seeAlso = [
            "https://gtfs.org/documentation/schedule/reference/#calendartxt",
            "https://gtfs.org/documentation/schedule/reference/#calendar_datestxt"
        ]
        closeMatch = [gtfs_linked.Service]