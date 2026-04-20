# Rules

## Dataset Files

1. `AgencyFile`

   1. A `Dataset` must have an `AgencyFile`.
   2. An `AgencyFile` must have at least one `Agency`.
   3. An `AgencyFile` is an `AgencyFileWithMultipleAgencies` if it has more than one `Agency`.
   4. An `AgencyFile` is an `AgencyFileWithSingleAgency` if it has more than one `Agency`.

2. `StopFile`

   1. A `Dataset` must have a `StopFile`.
   2. A `StopFile` must have at least one `Stop`.

3. `RouteFile`

   1. A `Dataset` must have a `RouteFile`.
   2. A `RouteFile` must have at least one `Route`.

4. `TripFile`

   1. A `Dataset` must have a `TripFile`.
   2. A `TripFile` must have at least one `Trip`.

5. `StopTimeFile`

   1. A `Dataset` must have a `StopTimeFile`.
   2. A `StopTimeFile` must have at least one `StopTime`.
    
6. `CalendarFile`

   1. A `CalendarFile` must have at least one `Service`.
   2. A `DatasetWihtoutCalendarFile` is a `Dataset` with no `CalendarFile`.
   3. A `Dataset` has a maximum of one `CalendarFile`.

7. `CalendarDatesFile`

   1. A `Dataset` must have a `CalendarDatesFile` if there is no `CalendarFile`.
   2. A `CalendarDatesFile` must have at least one `Service`.
   3. A `Dataset` has a maximum of one `CalendarDatesFile`.



## Agencies

1. `agency_id`

   1. An `Agency` must have an `agency_id` if the `AgencyFile` is an `AgencyFileWithMultipleAgencies`.
   2. The `agency_id` must be unique to all other `Agency` in the `AgencyFile`.

2. `agency_name`

   1. An `Agency` must have one `agency_name`.

3. `agency_url`

   1. An `Agency` must have one `agency_url`.

4. `agency_timezone`

   1. An `Agency` must have one `agency_timezone`.

5. `agency_lang`

   1. An `Agency` must have at most one `agency_lang`. 

6. `agency_phone`
7. `agency_fare_url`
8. `agency_email`
9. `cemv_support`

## Stops

1. `stop_id`

   1. A `Stop` must have a `stop_id`.
   2. The `stop_id` must be unique to all other `Stop` in the `StopFile`.

2. `stop_code`
3. `stop_name`

   1. A `Stop` must have a `stop_name` if the `Stop` is a `StopLocation` or `Platform`.
   2. A `Stop` must have a `stop_name` if the `Stop` is a `Station`. 
   3. A `Stop` must have a `stop_name` if the `Stop` is an `EntranceOrExit`.

4. `tts_stop_name`
5. `stop_desc`
6. `stop_lat`

   1. A `Stop` must have a `stop_lat` if the `Stop` is a `StopLocation` or `Platform`.
   2. A `Stop` must have a `stop_lat` if the `Stop` is a `Station`. 
   3. A `Stop` must have a `stop_lat` if the `Stop` is an `EntranceOrExit`.

7. `stop_lon`

   1. A `Stop` must have a `stop_lon` if the `Stop` is a `StopLocation` or `Platform`.
   2. A `Stop` must have a `stop_lon` if the `Stop` is a `Station`. 
   3. A `Stop` must have a `stop_lon` if the `Stop` is an `EntranceOrExit`.
    
8. `zone_id`
9. `stop_url`
10. `location_type`

    1. A `Stop` is a `StopLocation` if `location_type` is `0` or empty, and is a `ParentlessStop`.
    2. A `Stop` is a `Platform` if `location_type` is `0` or empty, and is a `ChildStop`.
    3. A `Stop` is a `Station` if `location_type` is `1`.
    4. A `Stop` is an `EntranceOrExit` if `location_type` is `2`.
    5. A `Stop` is a `GenericNode` if `location_type` is `3`.
    6. A `Stop` is a `BoardingArea` if `location_type` is `4`.

11. `parent_station`

    1. A `Stop` is a `ChildStop` if it has a `parent_station`.
    2. A `Stop` is a `ParentlessStop` if it does not have a `parent_station`.
    3. An `EntranceOrExit` must be a `ChildStop`.
    4. A `GenericNode` must be a `ChildStop`.
    5. A `BoardingArea` must be a `ChildStop`.
    6. A `Station` must not be a `ChildStop`.

12. `stop_timezone`
13. `wheelchair_boarding`
14. `level_id`
15. `platform_code`
16. `stop_access`

    1. A `Stop` must not have a `stop_access` if it is a `Station`, `EntranceOrExit`, `GenericNode`, or `BoardingArea`.
    2. A `Stop` must not have a `stop_access` if it is `ParentlessStop`.

## Routes

1. `route_id`

   1. A `Route` must have a `route_id`.
   2. The `route_id` must be unique to all other `Route` in the `RouteFile`.

2. `agency_id`

   1. A `Route` must have an `agency_id` if the `AgencyFile` in the `Dataset` is an `AgencyFileWithMultipleAgencies`.

3. `route_short_name`

   1. A `Route` must have a `route_short_name` if `route_long_name` is empty.

4. `route_long_name`

   1. A `Route` must have a `route_long_name` if `route_short_name` is empty.

5. `route_desc`
6. `route_type`

   1. A `Route` must have a `route_type`.

7. `route_url`
8. `route_color`
9. `route_text_color`
10. `route_sort_order`
11. `continuous_pickup`

    1. A `Route` must not have a `continuous_pickup` of `0` if `start_pickup_drop_off_window` or `end_pickup_drop_off_window` are defined for the `Trip` of the `Route`.
    2. A `Route` must not have a `continuous_pickup` of `2` if `start_pickup_drop_off_window` or `end_pickup_drop_off_window` are defined for the `Trip` of the `Route`.
    3. A `Route` must not have a `continuous_pickup` of `3` if `start_pickup_drop_off_window` or `end_pickup_drop_off_window` are defined for the `Trip` of the `Route`.

12. `continuous_drop_off`

    1. A `Route` must not have a `continuous_drop_off` of `0` if `start_pickup_drop_off_window` or `end_pickup_drop_off_window` are defined for the `Trip` of the `Route`.
    2. A `Route` must not have a `continuous_drop_off` of `2` if `start_pickup_drop_off_window` or `end_pickup_drop_off_window` are defined for the `Trip` of the `Route`.
    3. A `Route` must not have a `continuous_drop_off` of `3` if `start_pickup_drop_off_window` or `end_pickup_drop_off_window` are defined for the `Trip` of the `Route`.

13. `network_id`

    1. A `Route` must not have a `network_id` if there exists a `RouteNetworksFile` or `NetworksFile`.

14. `cemv_support`

## Trips

1. `route_id`

   1. A `Trip` must have a `route_id`.

2. `service_id`

   1. A `Trip` must have a `service_id`.

3. `trip_id`

   1. A `Trip` must have a `trip_id`.
   2. The `trip_id` must be unique to all other `Trip` in the `TripFile`.

4. `trip_headsign`
5. `trip_short_name`
6. `direction_id`
7. `block_id`
8. `shape_id`

   1. A `Trip` must have a `shape_id` if `continuous_pickup` or `continuous_drop_off` is defined in the associated `Route` or `StopTime`.

9. `wheelchair_accessible`
10. `bikes_allowed`
11. `cars_allowed`

## Stop Times

1. `trip_id`

   1. A `StopTime` must have a `trip_id`.

2. `arrival_time`

   1. A `StopTime` must have an `arrival_time` if it is a `FirstStopTime`.
   2. A `StopTime` must have an `arrival_time` if it is a `LastStopTime`.
   3. A `StopTime` must have an `arrival_time` if the value of `timepoint` is `1`.
   4. A `StopTime` must not have an `arrival_time` if `start_pickup_drop_off_window` or `end_pickup_drop_off_window` are defined.

3. `departure_time`

   1. A `StopTime` must have an `departure_time` if the value of `timepoint` is `1`.
   2. A `StopTime` must not have an `departure_time` if `start_pickup_drop_off_window` or `end_pickup_drop_off_window` are defined.

4. `stop_id`

   1. A `StopTime` must have a `stop_id` id `location_group_id` and `location_id` are not defined.
   2. A `StopTime` must not have a `stop_id` if `location_group_id` or `location_id` are defined.

5. `location_group_id`

   1. A `StopTime` must not have a `location_group_id` if `stop_id` or `location_id` are defined.

6. `location_id`

   1. A `StopTime` must not have a `location_id` if `stop_id` or `location_group_id` are defined.

7. `stop_sequence`

   1. A `StopTime` must have a `stop_sequence`.
   2. A `StopTime` is `FirstStopTime` if `stop_sequence` is the lowest integer.
   3. A `StopTime` is `LastStopTime` if `stop_sequence` is the highest integer.

8. `stop_headsign`
9. `start_pickup_drop_off_window`

   1. A `StopTime` must have a `start_pickup_drop_off_window` if `location_group_id` or `location_id` is defined.
   2. A `StopTime` must have a `start_pickup_drop_off_window` if `end_pickup_drop_off_window` is defined.
   3. A `StopTime` must not have a `start_pickup_drop_off_window` if `arrival_time` or `departure_time` is defined.

10. `end_pickup_drop_off_window`

    1. A `StopTime` must have a `end_pickup_drop_off_window` if `location_group_id` or `location_id` is defined.
    2. A `StopTime` must have a `end_pickup_drop_off_window` if `start_pickup_drop_off_window` is defined.
    3. A `StopTime` must not have a `end_pickup_drop_off_window` if `arrival_time` or `departure_time` is defined.

11. `pickup_type`

    1. A `StopTime` must not have a `pickup_type` of `0` if `start_pickup_drop_off_window` or `end_pickup_drop_off_window` are defined.
    2. A `StopTime` must not have a `pickup_type` of `3` if `start_pickup_drop_off_window` or `end_pickup_drop_off_window` are defined.

12. `drop_off_type`

    1. A `StopTime` must not have a `drop_off_type` of `0` if `start_pickup_drop_off_window` or `end_pickup_drop_off_window` are defined.

13. `continuous_pickup`

    1. A `StopTime` must not have a `continuous_pickup` of `0` if `start_pickup_drop_off_window` or `end_pickup_drop_off_window` are defined.
    2. A `StopTime` must not have a `continuous_pickup` of `2` if `start_pickup_drop_off_window` or `end_pickup_drop_off_window` are defined.
    3. A `StopTime` must not have a `continuous_pickup` of `3` if `start_pickup_drop_off_window` or `end_pickup_drop_off_window` are defined.

14. `continuous_drop_off`

    1. A `StopTime` must not have a `continuous_drop_off` of `0` if `start_pickup_drop_off_window` or `end_pickup_drop_off_window` are defined.
    2. A `StopTime` must not have a `continuous_drop_off` of `2` if `start_pickup_drop_off_window` or `end_pickup_drop_off_window` are defined.
    3. A `StopTime` must not have a `continuous_drop_off` of `3` if `start_pickup_drop_off_window` or `end_pickup_drop_off_window` are defined.

15. `shape_dist_traveled`
16. `timepoint`
17. `pickup_booking_rule_id`
18. `drop_off_booking_rule_id`

## Calendar

1. `service_id`

   1. A `Service` must have a `service_id`.
   2. The `service_id` must be unique to all other `Service`.

2. `monday`

    1. A `Service` must have a `monday`.

3. `tuesday`

    1. A `Service` must have a `tuesday`.

4. `wednesday`

    1. A `Service` must have a `wednesday`.

5. `thursday`

    1. A `Service` must have a `thursday`.

6. `friday`

    1. A `Service` must have a `friday`.

7. `saturday`

    1. A `Service` must have a `saturday`.

8. `sunday`

    1. A `Service` must have a `sunday`.

9. `start_date`

    1. A `Service` must have a `start_date`.

10. `end_date`

    1. A `Service` must have an `end_date`.

## Calendar Dates

1. `service_id`

   1. A `Service` must have a `service_id`.

2. `date`

   1. A `Service` must have a `date`.

3. `exception_type`

   1. A `Service` must have an `exception_type`.
