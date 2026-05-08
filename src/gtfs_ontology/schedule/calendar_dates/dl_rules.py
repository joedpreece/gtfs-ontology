from gtfs_ontology.schedule import *
from gtfs_ontology.schedule.calendar_dates.generate import *


with gtfs:

    class CalendarDateService(Service):
        is_a = [
            calendar_dates_date.exactly(1),
            exception_type.exactly(1)
        ]