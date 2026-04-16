from gtfs_ontology.realtime.core import *

# region Definitions

ID_DEF = """
Feed-unique identifier for this entity. The ids are used only to provide incrementality support.
The actual entities referenced by the feed must be specified by explicit selectors
(see EntitySelector below for more info).
"""

IS_DELETED_DEF = """
Whether this entity is to be deleted. Should be provided only for feeds with Incrementality of
DIFFERENTIAL - this field should NOT be provided for feeds with Incrementality of FULL_DATASET.
"""

TRIP_UPDATE_DEF = """
Data about the realtime departure delays of a trip. At least one of the fields trip_update, vehicle,
alert, or shape must be provided - all these fields cannot be empty.
"""

VEHICLE_DEF = """
Data about the realtime position of a vehicle. At least one of the fields trip_update, vehicle,
alert, or shape must be provided - all these fields cannot be empty.
"""

ALERT_DEF = """
Data about the realtime alert. At least one of the fields trip_update, vehicle, alert, or shape
must be provided - all these fields cannot be empty.
"""

SHAPE_DEF = """
Data about the realtime added shapes, such as for a detour. At least one of the fields trip_update,
vehicle, alert, or shape must be provided - all these fields cannot be empty.
"""

STOP_DEF = """
A new stop added to the feed dynamically.
"""

TRIP_MODIFICATIONS_DEF = """
List of trips affected by a particular modification, such as a detour.
"""

# endregion

with gtfs:

    class id(FieldValue, FunctionalProperty):
        comment = [locstr(ID_DEF, "en")]
        domain = [FeedEntity]
        range = [str]


    class is_deleted(FieldValue, FunctionalProperty):
        comment = [locstr(IS_DELETED_DEF, "en")]
        domain = [FeedEntity]
        range = [bool]


    class trip_update(FieldValue, FunctionalProperty):
        comment = [locstr(TRIP_UPDATE_DEF, "en")]
        domain = [FeedEntity]
        range = [TripUpdate]


    class vehicle(FieldValue, FunctionalProperty):
        comment = [locstr(VEHICLE_DEF, "en")]
        domain = [FeedEntity]
        range = [VehiclePosition]


    class alert(FieldValue, FunctionalProperty):
        comment = [locstr(ALERT_DEF, "en")]
        domain = [FeedEntity]
        range = [Alert]


    class shape(ExperimentalField, FunctionalProperty):
        comment = [locstr(SHAPE_DEF, "en")]
        domain = [FeedEntity]
        range = [Shape]


    class stop(ExperimentalField, FunctionalProperty):
        comment = [locstr(STOP_DEF, "en")]
        domain = [FeedEntity]
        range = [Stop]


    class trip_modifications(ExperimentalField, FunctionalProperty):
        comment = [locstr(TRIP_MODIFICATIONS_DEF, "en")]
        domain = [FeedEntity]
        range = [TripModifications]