# Rules

## Agencies

## Stops

1. `stop_id`

   1. A `Stop` must have a `stop_id`. 
   2. All `stop_id` in a `StopFile` must be unique.

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
    6. A `Station`

12. `stop_timezone`
13. `wheelchair_boarding`
14. `level_id`
15. `platform_code`
16. `stop_access`