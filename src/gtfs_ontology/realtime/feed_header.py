from gtfs_ontology.realtime.core import *

# region Definitions

VERSION_DEF = """
Version of the feed specification. The current version is 2.0.
"""

TIMESTAMP_DEF = """
This timestamp identifies the moment when the content of this feed has been created (in server time). In POSIX time (i.e., number of seconds since January 1st 1970 00:00:00 UTC). To avoid time skew between systems producing and consuming realtime information it is strongly advised to derive timestamp from a time server. It is completely acceptable to use Stratum 3 or even lower strata servers since time differences up to a couple of seconds are tolerable.
"""

FEED_VERSION_DEF = """
String that matches the feed_info.feed_version from the GTFS feed that the realtime data is based on. Consumers can use this to identify which GTFS feed is currently active or when a new one is available to download.
"""

# endregion

with gtfs:

    # region Datatypes

    class IncrementalityDatatype(Datatype):
        equivalent_to = [
            OneOf(
                [
                     "FULL_DATASET",
                     "DIFFERENTIAL"
                ]
            )
        ]

    #

    # region Object and Data Properties

    class gtfs_realtime_version(FieldValue, FunctionalProperty):
        comment = [locstr(VERSION_DEF, "en")]
        domain = [FeedHeader]
        range = [str]

    class incrementality(FieldValue, FunctionalProperty):
        domain = [FeedHeader]
        range = [IncrementalityDatatype]

    class timestamp(FieldValue, FunctionalProperty):
        comment = [locstr(TIMESTAMP_DEF, "en")]
        domain = [FeedHeader]
        range = [int]

    class feed_version(FieldValue, FunctionalProperty):
        comment = [locstr(FEED_VERSION_DEF, "en")]
        domain = [FeedHeader]
        range = [str]

    # endregion