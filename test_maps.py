"""
Test files for getting and manipulating data for creating geographical plots
from maps.py.
"""

import geoplot as gplt
import geopandas as gpd
import maps


def test_add_map_data_three_dictionaries():
    """
    Test that the function combines dictionaries as expected
    """
    state = {
        "features": [
            {"properties": {"state": "MO"}},
            {"properties": {"state": "CO"}},
            {"properties": {"state": "NH"}},
        ]
    }
    subject_area = {"MO": "Noah", "CO": "Other Noah", "NH": "Mark"}
    bill_count = {"MO": 100, "CO": 1020, "NH": 830}

    assert maps.add_map_data(state, bill_count, subject_area) == {
        "features": [
            {
                "properties": {
                    "state": "MO",
                    "bill count": 100,
                    "policy area": "Noah",
                }
            },
            {
                "properties": {
                    "state": "CO",
                    "bill count": 1020,
                    "policy area": "Other Noah",
                }
            },
            {
                "properties": {
                    "state": "NH",
                    "bill count": 830,
                    "policy area": "Mark",
                }
            },
        ]
    }


def test_make_geodata_datatype():
    """
    Test that the functions output is a geodataframe.
    """
    random_dict = {
        "features": [
            {
                "properties": {"person": "Mark"},
                "geometry": {"type": "Point", "coordinates": [0, 0]},
            },
            {
                "properties": {"person": "Noah"},
                "geometry": {"type": "Point", "coordinates": [0, 1]},
            },
            {
                "properties": {"person": "Other Noah"},
                "geometry": {"type": "Point", "coordinates": [1, 0]},
            },
        ]
    }
    # Change response to be right
    assert isinstance(maps.make_geodata(random_dict)) == isinstance(
        gpd.read_file(gplt.datasets.get_path("contiguous_usa"))
    )
