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


def add_map_data(map_data_dict, bills_per_state_dict, most_common_policy_area):
    """
    Takes the map data dictionary and two dictionaries with data on the states
    and combines them into a single dictionary that is then returned.

    Args:
        map_data_dict is the geojson file for the states of the contiguous USA
            with the state names written as abbreviations, formatted as a
            dictionary. Each state is listed as a feature with geometry and a
            state abbreviation
        bills_per_state_dict is a dictionary containing the state abbreviations
            as keys and the number of bills proposed by senators of that state
            as values. The number of bills is an integer
        most_common_policy_area is a dictionary containing the state
            abbreviations as keys and the most common policy area of bills
            proposed by senators of that state as values. The policy areas are
            strings

        Returns:
            returns the map_data_dict dictionary formatted as a geojson where
            the properties of the features include the state abbreviation, the
            number of bills proposed by a senator from that state and the most
            common policy area of bills proposed by senators of that state
    """
    for index in range(len(map_data_dict["features"])):
        if (
            map_data_dict["features"][index]["properties"]["state"]
            in bills_per_state_dict
        ):
            map_data_dict["features"][index]["properties"][
                "bill count"
            ] = bills_per_state_dict[
                map_data_dict["features"][index]["properties"]["state"]
            ]
        else:
            map_data_dict["features"][index]["properties"]["bill count"] = 0
    for index in range(len(map_data_dict["features"])):
        if (
            map_data_dict["features"][index]["properties"]["state"]
            in most_common_policy_area
        ):
            map_data_dict["features"][index]["properties"][
                "policy area"
            ] = most_common_policy_area[
                map_data_dict["features"][index]["properties"]["state"]
            ]
        else:
            map_data_dict["features"][index]["properties"]["policy area"] = ""
    return map_data_dict
