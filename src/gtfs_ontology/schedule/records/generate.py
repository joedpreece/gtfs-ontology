from gtfs_ontology.schedule.core import *
from gtfs_ontology.schedule.term_definitions.generate import Record

with gtfs:

    class Agency(Record, foaf.Agent):
        seeAlso = ["https://gtfs.org/documentation/schedule/reference/#agencytxt"]


    class Stop(Record, geo.SpatialThing, schema.BusStop):
        seeAlso = ["https://gtfs.org/documentation/schedule/reference/#stopstxt"]


    class Route(Record):
        seeAlso = ["https://gtfs.org/documentation/schedule/reference/#routestxt"]


    class Trip(Record):
        seeAlso = ["https://gtfs.org/documentation/schedule/reference/#tripstxt"]


    class StopTime(Record):
        seeAlso = ["https://gtfs.org/documentation/schedule/reference/#stop_timestxt"]


    class Calendar(Record):
        seeAlso = ["https://gtfs.org/documentation/schedule/reference/#calendartxt"]


    class CalendarDate(Record):
        seeAlso = ["https://gtfs.org/documentation/schedule/reference/#calendar_datestxt"]


    class Level(Record):
        seeAlso = ["https://gtfs.org/documentation/schedule/reference/#agencytxt"]