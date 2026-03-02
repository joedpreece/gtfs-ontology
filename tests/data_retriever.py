import os
import tempfile
import zipfile
from typing import TypeAlias, Literal

import pandas as pd
from dotenv import load_dotenv
from joblib import Memory
from config import CACHE

GTFS_FILES: TypeAlias = Literal[
    "agency",
    "calendar",
    "calendar_dates",
    "routes",
    "shapes",
    "stop_times",
    "stops",
    "trips",
]

memory = Memory(location=CACHE, verbose=0)

import requests

@memory.cache
def get_response(
        url: str
) -> requests.Response:
    response = requests.get(url)
    return response

@memory.cache
def get_df(
        dataset: GTFS_FILES,
) -> pd.DataFrame:

    # Create a temporary file to store the zip content
    with tempfile.TemporaryFile() as tmp:
        tmp.write(gtfs.content)
        tmp.seek(0)

        # Open the zip file
        with zipfile.ZipFile(tmp, 'r') as zip_ref:

            if f'{dataset}.txt' not in zip_ref.namelist():
                raise FileNotFoundError(f"{dataset}.txt not found in the ZIP archive.")

            with zip_ref.open(f'{dataset}.txt') as file:
                df = pd.read_csv(file, delimiter=',')  # Adjust delimiter if

    return df

load_dotenv()

app_id = os.getenv("TFWM_APP_ID")
api_key = os.getenv("TFWM_API_KEY")

gtfs = get_response(
    url=f"http://api.tfwm.org.uk/gtfs/tfwm_gtfs.zip?app_id={app_id}&app_key={api_key}"
)

@memory.cache
def get_df_agencies() -> pd.DataFrame:
    return get_df(dataset='agency')

@memory.cache
def get_df_calendar() -> pd.DataFrame:
    return get_df(dataset='calendar')

@memory.cache
def get_df_calendar_dates() -> pd.DataFrame:
    return get_df(dataset='calendar_dates')

@memory.cache
def get_df_routes() -> pd.DataFrame:
    return get_df(dataset='routes')

@memory.cache
def get_df_shapes() -> pd.DataFrame:
    return get_df(dataset='shapes')