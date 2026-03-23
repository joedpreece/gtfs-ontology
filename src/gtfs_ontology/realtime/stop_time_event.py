from gtfs_ontology.realtime.core import *

# region Definitions

DELAY_DEF = """
Delay (in seconds) can be positive (meaning that the vehicle is late) or negative (meaning that the vehicle is ahead of schedule). Delay of 0 means that the vehicle is exactly on time.
Forbidden if StopTimeUpdate.schedule_relationship is NO_DATA.
Required otherwise if time is not given.
"""

TIME_DEF = """
Delay (in seconds) can be positive (meaning that the vehicle is late) or negative (meaning that the vehicle is ahead of schedule). Delay of 0 means that the vehicle is exactly on time.
Forbidden if StopTimeUpdate.schedule_relationship is NO_DATA.
Required otherwise if time is not given.
"""

SCHEDULED_TIME_DEF = """
Scheduled time. In POSIX time (i.e., number of seconds since January 1st 1970 00:00:00 UTC).
Optional if TripUpdate.schedule_relationship is NEW, REPLACEMENT or DUPLICATED, forbidden otherwise.
"""

UNCERTAINTY_DEF = """
If uncertainty is omitted, it is interpreted as unknown. To specify a completely certain prediction, set its uncertainty to 0.
Forbidden if StopTimeUpdate.schedule_relationship is NO_DATA.
"""

# endregion

with gtfs:

    # region Object and Data Properties

    class delay(FieldValue, FunctionalProperty):
        comment = [locstr(DELAY_DEF, "en")]
        domain = [StopTimeEvent]
        range = [int]

    class time(FieldValue, FunctionalProperty):
        comment = [locstr(TIME_DEF, "en")]
        domain = [StopTimeEvent]
        range = [int]

    class scheduled_time(FieldValue, FunctionalProperty):
        comment = [locstr(SCHEDULED_TIME_DEF, "en")]
        domain = [StopTimeEvent]
        range = [int]

    class uncertainty(FieldValue, FunctionalProperty):
        comment = [locstr(UNCERTAINTY_DEF, "en")]
        domain = [StopTimeEvent]
        range = [int]

    # endregion