import geopandas as gpd
import pandas as pd
import geoplot as gplt
import geoplot.crs as gcrs
import json

abbreviations = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "District of Columbia": "DC",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}


def get_map_data():
    """
    Takes map data for the continguous US from the geoplot library, saves it in
    a geojson file and updates it so the states are listes as abbreviations not
    full state names.

    Args: None

    Returns: map_data is the updated json object, which is also saved to the
    file "usa_map_data.geojson"
    """
    contiguous_usa = gpd.read_file(gplt.datasets.get_path("contiguous_usa"))
    gpd.GeoDataFrame.to_file(contiguous_usa, "usa_map_data.geojson")
    with open("usa_map_data.geojson") as usa_map_data:
        map_data = json.load(usa_map_data)
    for feature in map_data["features"]:
        if feature["properties"]["state"] in abbreviations:
            feature["properties"]["state"] = abbreviations[
                feature["properties"]["state"]
            ]

    return map_data
