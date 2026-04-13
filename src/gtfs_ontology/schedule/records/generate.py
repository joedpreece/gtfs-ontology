from gtfs_ontology.schedule.core import *

with gtfs:

    class Agency(Record, foaf.Agent):
        seeAlso = ["<https://gtfs.org/documentation/schedule/reference/#agencytxt>"]


    class Stop(Record, geo.SpatialThing, schema.BusStop):
        pass


    class Route(Record):
        pass


    class Trip(Record):
        pass


    class StopTime(Record):
        pass


    class Calendar(Record):
        pass


    class CalendarDate(Record):
        pass


    class Level(Record):
        pass