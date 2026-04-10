from gtfs_ontology.schedule.core import *
from gtfs_ontology.schedule.term_definitions.generate import DatasetFile


with gtfs:

    class AgencyFile(DatasetFile):
        comment = "Transit agencies with service represented in this dataset."

    class StopFile(DatasetFile):
        comment = "Stops where vehicles pick up or drop off riders. Also defines stations and station entrances."

    class RouteFile(DatasetFile):
        comment = "Transit routes. A route is a group of trips that are displayed to riders as a single service."

    class TripFile(DatasetFile):
        comment = "Trips for each route. A trip is a sequence of two or more stops that occur during a specific time period."

    class StopTimeFile(DatasetFile):
        comment = "Times that a vehicle arrives at and departs from stops for each trip."

    class CalendarFile(DatasetFile):
        comment = "Service dates specified using a weekly schedule with start and end dates."

    class CalendarDateFile(DatasetFile):
        comment = "Exceptions for the services defined in the calendar.txt."