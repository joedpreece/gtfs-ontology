from gtfs_ontology.realtime.core import *
from gtfs_ontology.realtime.vehicle_position import OccupancyStatus

# CarriageDetails field descriptions (GTFS Realtime)

CARRIAGEDETAILS_ID_DEF = """
Identification of the carriage. Should be unique per vehicle. 

**Caution:** this field is still **experimental**, and subject to change. It may be formally adopted in the future.
"""
# Source: message CarriageDetails → id.

CARRIAGEDETAILS_LABEL_DEF = """
User visible label that may be shown to the passenger to help identify the carriage. Example: "7712", "Car ABC-32", etc... 
**Caution:** this field is still **experimental**, and subject to change. It may be formally adopted in the future.
"""
# Source: message CarriageDetails → label.

CARRIAGEDETAILS_OCCUPANCY_STATUS_DEF = """
Occupancy status for this given carriage, in this vehicle. Default is set to `NO_DATA_AVAILABLE`.

**Caution:** this field is still **experimental**, and subject to change. It may be formally adopted in the future.
"""
# Source: message CarriageDetails → occupancy_status.

CARRIAGEDETAILS_OCCUPANCY_PERCENTAGE_DEF = """
Occupancy percentage for this given carriage, in this vehicle. 
Follows the same rules as "VehiclePosition.occupancy_percentage". Use -1 
 in case data is not available for this given carriage.

**Caution:** this field is still **experimental**, and subject to change. It may be formally adopted in the future.
"""
# Source: message CarriageDetails → occupancy_percentage.

CARRIAGEDETAILS_CARRIAGE_SEQUENCE_DEF = """
Identifies the order of this carriage with respect to the other 
carriages in the vehicle's list of CarriageStatus. The first carriage in 
 the direction of travel must have a value of 1. The second value 
corresponds to the second carriage in the direction of travel and must 
have a value of 2, and so forth. For example, the first carriage in the 
direction of travel has a value of 1. If the second carriage in the 
direction of travel has a value of 3, consumers will discard data for 
all carriages (i.e., the multi_carriage_details field). Carriages 
without data must be represented with a valid carriage_sequence number 
and the fields without data should be omitted (alternately, those fields 
 could also be included and set to the "no data" values). 

**Caution:** this field is still **experimental**, and subject to change. It may be formally adopted in the future.
"""
# Source: message CarriageDetails → carriage_sequence.

with gtfs:

    class id(ExperimentalField, FunctionalProperty):
        comment = [locstr(CARRIAGEDETAILS_ID_DEF, "en")]
        domain = [CarriageDetails]
        range = [str]

    class label(ExperimentalField, FunctionalProperty):
        comment = [locstr(CARRIAGEDETAILS_LABEL_DEF, "en")]
        domain = [CarriageDetails]
        range = [str]

    class occupancy_status(ExperimentalField, FunctionalProperty):
        comment = [locstr(CARRIAGEDETAILS_OCCUPANCY_STATUS_DEF, "en")]
        domain = [CarriageDetails]
        range = [OccupancyStatus]

    class occupancy_percentage(ExperimentalField, FunctionalProperty):
        comment = [locstr(CARRIAGEDETAILS_OCCUPANCY_PERCENTAGE_DEF, "en")]
        domain = [CarriageDetails]
        range = [int]

    class carriage_sequence(ExperimentalField, FunctionalProperty):
        comment = [locstr(CARRIAGEDETAILS_CARRIAGE_SEQUENCE_DEF, "en")]
        domain = [CarriageDetails]
        range = [int]