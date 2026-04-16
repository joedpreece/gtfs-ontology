from gtfs_ontology.realtime.core import *

# region Definitions

ASSIGNED_STOP_ID_DEF = """
Supports real-time stop assignments. Refers to a stop_id defined in the GTFS stops.txt.
The new assigned_stop_id should not result in a significantly different trip experience for the end user than the stop_id defined in GTFS stop_times.txt. In other words, the end user should not view this new stop_id as an "unusual change" if the new stop was presented within an app without any additional context. For example, this field is intended to be used for platform assignments by using a stop_id that belongs to the same station as the stop originally defined in GTFS stop_times.txt.
To assign a stop without providing any real-time arrival or departure predictions, populate this field and set StopTimeUpdate.schedule_relationship = NO_DATA.
If this field is populated, StopTimeUpdate.stop_sequence must be populated and StopTimeUpdate.stop_id should not be populated. Stop assignments should be reflected in other GTFS-realtime fields as well (e.g., VehiclePosition.stop_id).
"""

STOP_HEADSIGN_DEF = """
The updated headsign of the vehicle at the stop.
"""

DROP_OFF_TYPE_DEF = """
The updated drop off of the vehicle at the stop.
"""

PICKUP_TYPE_DEF = """
The updated pickup of the vehicle at the stop.
"""

DROP_OFF_PICKUP_TYPE_REGULAR_DEF = """
Regularly scheduled pickup/dropoff.
"""

DROP_OFF_PICKUP_TYPE_NONE_DEF = """
No pickup/dropoff available.
"""

DROP_OFF_PICKUP_TYPE_PHONE_AGENCY_DEF = """
Must phone agency to arrange pickup/dropoff.
"""

DROP_OFF_PICKUP_TYPE_COORDINATE_WITH_DRIVER_DEF = """
Must coordinate with driver to arrange pickup/dropoff.
"""

# endregion

with gtfs:

    # region Datatypes

    class DropOffPickupTypeDatatype(Datatype):
        equivalent_to = [
            OneOf(
                [
                    "REGULAR",
                    "NONE",
                    "PHONE_AGENCY",
                    "COORDINATE_WITH_DRIVER",
                ]
            )
        ]

    # endregion

    # region Classes

    class DropOffPickupTypeDatatypeDescription(DatatypeDescription):
        pass

    class DropOffPickupTypeDatatypeDescriptionRegular(DropOffPickupTypeDatatypeDescription):
        comment = [locstr(DROP_OFF_PICKUP_TYPE_REGULAR_DEF, "en")]

    class DropOffPickupTypeDatatypeDescriptionNone(DropOffPickupTypeDatatypeDescription):
        comment = [locstr(DROP_OFF_PICKUP_TYPE_NONE_DEF, "en")]

    class DropOffPickupTypeDatatypeDescriptionPhoneAgency(DropOffPickupTypeDatatypeDescription):
        comment = [locstr(DROP_OFF_PICKUP_TYPE_PHONE_AGENCY_DEF, "en")]

    class DropOffPickupTypeDatatypeDescriptionCoordinateWithDriver(DropOffPickupTypeDatatypeDescription):
        comment = [locstr(DROP_OFF_PICKUP_TYPE_COORDINATE_WITH_DRIVER_DEF, "en")]


    # endregion

    # region Object and Data Properties

    class assigned_stop_id(ExperimentalField, FunctionalProperty):
        comment = [locstr(ASSIGNED_STOP_ID_DEF, "en")]
        domain = [StopTimeProperties]
        range = [str]

    class stop_headsign(ExperimentalField, FunctionalProperty):
        comment = [locstr(STOP_HEADSIGN_DEF, "en")]
        domain = [StopTimeProperties]
        range = [str]

    class drop_off_type(ExperimentalField, FunctionalProperty):
        comment = [locstr(DROP_OFF_TYPE_DEF, "en")]
        domain = [StopTimeProperties]
        range = [DropOffPickupTypeDatatype]

    class pickup_type(ExperimentalField, FunctionalProperty):
        comment = [locstr(PICKUP_TYPE_DEF, "en")]
        domain = [StopTimeProperties]
        range = [DropOffPickupTypeDatatype]