from gtfs_ontology.realtime.core import *

# region Definitions

HEADER_DEF = """
Metadata about this feed and feed message.
"""

ENTITY_DEF = """
Contents of the feed. If there is real-time information available for the transit system, this field must be provided. If this field is empty, consumers should assume there is no real-time information available for the system.
"""

# endregion

with gtfs:

    # region Object and Data Properties

    class header(FieldValue, FunctionalProperty):
        comment = [locstr(HEADER_DEF, "en")]
        domain = [FeedMessage]
        range = [FeedHeader]

    class entity(FieldValue):
        comment = [locstr(ENTITY_DEF, "en")]
        domain = [FeedMessage]
        range = [FeedEntity]

    # endregion