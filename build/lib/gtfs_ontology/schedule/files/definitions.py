AGENCY_DEF = """
Transit agencies with service represented in this dataset.
"""

STOPS_DEF = """
Stops where vehicles pick up or drop off riders. Also defines stations and station entrances.

Conditionally Required:
- Optional if demand-responsive zones are defined in locations.geojson.
- Required otherwise.
"""

ROUTES_DEF = """
Transit routes. A route is a group of trips that are displayed to riders as a single service.
"""

TRIPS_DEF = """
Trips for each route. A trip is a sequence of two or more stops that occur during a specific time period.
"""

STOP_TIMES_DEF = """
Times that a vehicle arrives at and departs from stops for each trip.
"""

CALENDAR_DEF = """
Service dates specified using a weekly schedule with start and end dates.

Conditionally Required:
- Required unless all dates of service are defined in calendar_dates.txt.
- Optional otherwise.
"""

CALENDAR_DATES_DEF = """
Exceptions for the services defined in the calendar.txt.

Conditionally Required:
- Required if calendar.txt is omitted. In which case calendar_dates.txt must contain all dates of service.
- Optional otherwise.
"""

DATASET_WITHOUT_CALENDAR_FILE_DEF = """
A dataset that does not contain calendar.txt.
"""