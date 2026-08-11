import numpy as np

from gtfs_ontology import AGENCY_FILE, AGENCY_RML_FILE, AGENCY_KG_FILE, STOP_FILE, \
    STOP_RML_FILE, STOP_KG_FILE, ROUTE_FILE, ROUTE_RML_FILE, ROUTE_KG_FILE, TRIP_FILE, \
    TRIP_RML_FILE, TRIP_KG_FILE, STOP_TIME_FILE, STOP_TIME_RML_FILE, STOP_TIME_KG_FILE
from gtfs_ontology.graphs import materialize_graph

# pull_tfwm_gtfs_data()

materialize_graph(
    csv_file=AGENCY_FILE,
    rml_file=AGENCY_RML_FILE,
    output_file=AGENCY_KG_FILE,
    source_name="agency.txt",
    required_columns=[
        "agency_id",
        "agency_name",
        "agency_url",
        "agency_timezone",
        "agency_lang",
        "agency_phone",
        "agency_fare_url",
        "agency_email",
        "cemv_support"
    ]
)
#
# materialize_graph(
#     csv_file=STOP_FILE,
#     rml_file=STOP_RML_FILE,
#     output_file=STOP_KG_FILE,
#     source_name="stops.txt",
#     required_columns=[
#         "stop_id",
#         "stop_code",
#         "stop_name",
#         "tts_stop_name",
#         "stop_desc",
#         "stop_lat",
#         "stop_lon",
#         "zone_id",
#         "stop_url",
#         "location_type",
#         "parent_station",
#         "stop_timezone",
#         "wheelchair_boarding",
#         "level_id",
#         "platform_code",
#         "stop_access",
#     ]
# )
#
# materialize_graph(
#     csv_file=ROUTE_FILE,
#     rml_file=ROUTE_RML_FILE,
#     output_file=ROUTE_KG_FILE,
#     source_name="routes.txt",
#     required_columns=[
#         "route_id",
#         "agency_id",
#         "route_short_name",
#         "route_long_name",
#         "route_desc",
#         "route_type",
#         "route_url",
#         "route_color",
#         "route_text_color",
#         "route_sort_order",
#         "continuous_pickup",
#         "continuous_drop_off",
#         "network_id",
#         "cemv_support",
#     ]
# )

# materialize_graph(
#     csv_file=TRIP_FILE,
#     rml_file=TRIP_RML_FILE,
#     output_file=TRIP_KG_FILE,
#     source_name="trips.txt",
#     required_columns=[
#         "route_id",
#         "service_id",
#         "shape_id"
#         "trip_id",
#         "trip_headsign",
#         "trip_short_name",
#         "direction_id",
#         "block_id",
#         "wheelchair_accessible",
#         "bikes_allowed",
#         "cars_allowed",
#         "safe_duration_factor",
#         "safe_duration_offset",
#     ]
# )

# materialize_graph(
#     csv_file=STOP_TIME_FILE,
#     rml_file=STOP_TIME_RML_FILE,
#     output_file=STOP_TIME_KG_FILE,
#     source_name="stop_times.txt",
#     required_columns=[
#         "trip_id",
#         "arrival_time",
#         "departure_time",
#         "stop_id",
#         "location_group_id",
#         "location_id",
#         "stop_sequence",
#         "stop_headsign",
#         "start_pickup_drop_off_window",
#         "end_pickup_drop_off_window",
#         "pickup_type",
#         "drop_off_type",
#         "continuous_pickup",
#         "continuous_drop_off",
#         "shape_dist_traveled",
#         "timepoint",
#         "pickup_booking_rule_id",
#         "drop_off_booking_rule_id",
#     ]
# )