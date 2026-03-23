from gtfs_ontology.core import *

MESSAGE_DEF = """
Complex type
"""

FEED_MESSAGE_DEF = """
The contents of a feed message. Each message in the stream is obtained as a response to an appropriate HTTP GET request. A realtime feed is always defined with relation to an existing GTFS feed. All the entity ids are resolved with respect to the GTFS feed.
"""

FEED_HEADER_DEF = """
Metadata about a feed, included in feed messages.
"""

FEED_ENTITY_DEF = """
A definition (or update) of an entity in the transit feed. If the entity is not being deleted, exactly one of 'trip_update', 'vehicle', 'alert', 'shape', 'stop' or 'trip_modification' fields should be populated.
"""

TRIP_UPDATE_DEF = """
Realtime update on the progress of a vehicle along a trip. Please also refer to the general discussion of the trip updates entities. upd Depending on the value of ScheduleRelationship, a TripUpdate can specify:

    A trip that proceeds along the schedule.
    A trip that proceeds along a route but has no fixed schedule.
    A trip that has been added or removed with regard to schedule.
    A trip that replaces an existing trip in static GTFS.
    A new trip that is a copy of an existing trip in static GTFS. It will run at the service date and time specified in TripProperties.

The updates can be for future, predicted arrival/departure events, or for past events that already occurred. In most cases information about past events is a measured value thus its uncertainty value is recommended to be 0. Although there could be cases when this does not hold so it is allowed to have uncertainty value different from 0 for past events. If an update's uncertainty is not 0, either the update is an approximate prediction for a trip that has not completed or the measurement is not precise or the update was a prediction for the past that has not been verified after the event occurred.

If a vehicle is serving multiple trips within the same block (for more information about trips and blocks, please refer to GTFS trips.txt):

    the feed should include a TripUpdate for the trip currently being served by the vehicle. Producers are encouraged to include TripUpdates for one or more trips after the current trip in this vehicle's block if the producer is confident in the quality of the predictions for these future trip(s). Including multiple TripUpdates for the same vehicle avoids prediction "pop-in" for riders as the vehicle transitions from one trip to another and also gives riders advance notice of delays that impact downstream trips (e.g., when the known delay exceeds planned layover times between trips).
    the respective TripUpdate entities are not required to be added to the feed in the same order that they are scheduled in the block. For example, if there are trips with trip_ids 1, 2, and 3 that all belong to one block, and the vehicle travels trip 1, then trip 2, and then trip 3, the trip_update entities may appear in any order - for example, adding trip 2, then trip 1, and then trip 3 is allowed.

Note that the update can describe a trip that has already completed. To this end, it is enough to provide an update for the last stop of the trip. If the time of arrival at the last stop is in the past, the client will conclude that the whole trip is in the past (it is possible, although inconsequential, to also provide updates for preceding stops). This option is most relevant for a trip that has completed ahead of schedule, but according to the schedule, the trip is still proceeding at the current time. Removing the updates for this trip could make the client assume that the trip is still proceeding. Note that the feed provider is allowed, but not required, to purge past updates - this is one case where this would be practically useful.
"""

STOP_TIME_EVENT_DEF = """
Timing information for a single predicted event (either arrival or departure). Timing consists of delay and/or estimated time, and uncertainty. A scheduled time can also be added for NEW, REPLACEMENT, or DUPLICATED trips.

    delay should be used when the prediction is given relative to some existing schedule in GTFS.
    time should be given whether there is a predicted schedule or not, and must be given for new or replacement trips. If both time and delay are specified, time will take precedence (although normally, time, if given for a scheduled trip, should be equal to scheduled time in GTFS + delay).
    scheduled time may be given if the trip is a new, replacement or duplicated trip.

Uncertainty applies equally to both time and delay. The uncertainty roughly specifies the expected error in true delay (but note, we don't yet define its precise statistical meaning). It's possible for the uncertainty to be 0, for example for trains that are driven under computer timing control.
"""

STOP_TIME_UPDATE_DEF = """
Realtime update for arrival and/or departure events for a given stop on a trip. Please also refer to the general discussion of stop time updates in the TripDescriptor and trip updates entities documentation.

Updates can be supplied for both past and future events. The producer is allowed, although not required, to drop past events, unless if TripUpdate.schedule_relationship is NEW or REPLACEMENT, in such case past stops must not be dropped as they define the trip the vehicle is on, until the whole trip has been finished. The update is linked to a specific stop either through stop_sequence or stop_id, so one of these fields must necessarily be set. If the same stop_id is visited more than once in a trip, then stop_sequence should be provided in all StopTimeUpdates for that stop_id on that trip.

In new or replacement trips, updates are used to specify the stops visited by the trip without referring to an existing trip in the GTFS Static. In such trips, stop_id, stop_sequence, departure and arrival must all be set.
"""

STOP_TIME_PROPERTIES_DEF = """
Realtime update for certain properties defined within GTFS stop_times.txt.
"""

TRIP_PROPERTIES_DEF = """
Defines updated properties of the trip.
"""

EXPERIMENTAL_FIELD_DEF = """
Caution: this field is still experimental, and subject to change. It may be formally adopted in the future.
"""

EXPERIMENTAL_MESSAGE_DEF = """
Caution: this message is still experimental, and subject to change. It may be formally adopted in the future.
"""

with gtfs:

    class ProtocolBufferDataTypes(Thing):
        pass

    class Message(ProtocolBufferDataTypes):
        comment = [locstr(MESSAGE_DEF, "en")]

    class ExperimentalField(FieldValue):
        comment = [locstr(EXPERIMENTAL_FIELD_DEF, "en")]

    class ExperimentalMessage(Message):
        comment = [locstr(EXPERIMENTAL_MESSAGE_DEF, "en")]

    class FeedMessage(Message):
        comment = [locstr(FEED_MESSAGE_DEF, "en")]

    class FeedHeader(Message):
        comment = [locstr(FEED_HEADER_DEF, "en")]

    class FeedEntity(Message):
        comment = [locstr(FEED_HEADER_DEF, "en")]

    class TripUpdate(Message):
        comment = [locstr(TRIP_UPDATE_DEF, "en")]

    class StopTimeEvent(Message):
        comment = [locstr(STOP_TIME_EVENT_DEF, "en")]

    class StopTimeUpdate(Message):
        comment = [locstr(STOP_TIME_UPDATE_DEF, "en")]
        
    class StopTimeProperties(ExperimentalMessage):
        comment = [locstr(STOP_TIME_PROPERTIES_DEF, "en")]
        
    class TripProperties(ExperimentalMessage):
        comment = [locstr(TRIP_PROPERTIES_DEF, "en")]

    class TripModifications(Message):
        pass

    class VehiclePosition(Message):
        pass

    class Alert(Message):
        pass

    class Shape(Message):
        pass

    class Stop(Message):
        pass

    class TripDescriptor(Message):
        pass

    class VehicleDescriptor(Message):
        pass

    class TripProperties(Message):
        pass

    class OccupancyStatus(Message):
        pass

    class ScheduleRelationship(Message):
        pass