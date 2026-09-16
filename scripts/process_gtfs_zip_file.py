import os
import zipfile
import pandas as pd
from pathlib import Path

# Master GTFS specification headers (Required + Optional fields)
GTFS_SCHEMAS = {
    "agency": [
        "agency_id", "agency_name", "agency_url", "agency_timezone",
        "agency_lang", "agency_phone", "agency_fare_url", "agency_email", "cemv_support"
    ],
    "stops": [
        "stop_id", "stop_code", "stop_name", "tts_stop_name", "stop_desc", "stop_lat", "stop_lon",
        "zone_id", "stop_url", "location_type", "parent_station", "stop_timezone",
        "wheelchair_boarding", "level_id", "platform_code", "stop_access"
    ],
    "routes": [
        "route_id", "agency_id", "route_short_name", "route_long_name", "route_desc",
        "route_type", "route_url", "route_color", "route_text_color",
        "route_sort_order",
        "continuous_pickup", "continuous_drop_off", "network_id", "cemv_support"
    ],
    "trips": [
        "route_id", "service_id", "trip_id", "trip_headsign", "trip_short_name",
        "direction_id", "block_id", "shape_id", "wheelchair_accessible", "bikes_allowed", "cars_allowed", "safe_duration_factor", "safe_duration_offset"
    ],
    "stop_times": [
        "trip_id", "arrival_time", "departure_time", "stop_id", "location_group_id", "location_id", "stop_sequence",
        "stop_headsign", "start_pickup_drop_off_window", "end_pickup_drop_off_window", "pickup_type", "drop_off_type", "continuous_pickup",
        "continuous_drop_off", "shape_dist_traveled", "timepoint", "pickup_booking_rule_id", "drop_off_booking_rule_id"
    ],
    "calendar": [
        "service_id", "monday", "tuesday", "wednesday", "thursday", "friday",
        "saturday", "sunday", "start_date", "end_date"
    ],
    "calendar_dates": [
        "service_id", "date", "exception_type"
    ]
}


def process_gtfs_zip(zip_path: str, output_dir: str):
    zip_file = Path(zip_path)
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    if not zip_file.exists():
        raise FileNotFoundError(f"GTFS zip file not found: {zip_file}")

    print(f"Extracting and processing {zip_file}...")

    with zipfile.ZipFile(zip_file, 'r') as z:
        for file_info in z.infolist():
            filename = file_info.filename
            stem = Path(filename).stem.lower()

            if not filename.endswith('.txt'):
                continue

            print(f"Processing {filename}...")

            # Read raw TXT from zip without extracting to disk first
            with z.open(file_info) as f:
                df = pd.read_csv(f, dtype=str, encoding='utf-8-sig')

            # Pad missing columns if file schema is defined
            if stem in GTFS_SCHEMAS:
                expected = GTFS_SCHEMAS[stem]
                missing = [col for col in expected if col not in df.columns]

                if missing:
                    print(f"  └─ Injecting missing columns: {missing}")
                    for col in missing:
                        df[col] = None  # Saved as empty/NaN in CSV

            # Save as clean .csv
            csv_output = out_path / f"{stem}.csv"
            df.to_csv(csv_output, index=False, encoding='utf-8')
            print(f"  └─ Saved to {csv_output}")

    print("\nGTFS pre-processing complete!")


if __name__ == "__main__":
    import sys

    # Default relative paths if no CLI args passed
    default_zip = "../data/tfwm_gtfs.zip"
    default_out = "../data"

    zip_arg = sys.argv[1] if len(sys.argv) > 1 else default_zip
    out_arg = sys.argv[2] if len(sys.argv) > 2 else default_out

    process_gtfs_zip(zip_arg, out_arg)