from gtfs_ontology.schedule import *
from gtfs_ontology.schedule.calendar.generate import *


with gtfs:

    class CalendarService(Service):
        is_a = [
            service_id.exactly(1) &
            monday.exactly(1) &
            tuesday.exactly(1) &
            wednesday.exactly(1) &
            thursday.exactly(1) &
            friday.exactly(1) &
            saturday.exactly(1) &
            sunday.exactly(1) &
            start_date.exactly(1) &
            end_date.exactly(1)
        ]