""" 
Test files for getting and manipulating data for creating geographical plots
from maps.py. 
"""
import maps

def test_add_map_data_three_dictionaries():
    """
    Test that the function combines dictionaries as expected
    """
    group = {"features": [{"properties":{"NH": "Mark", "MO": "Noah", "CO": "Crazy Noah"}]
    professor = {"Steve": "Some Professor", "Aman": "Another Professor", "Erhardt": "My Professor"}
    course = {"QEA": 100, "SoftDes": 1020, "ISIM": 830}

    assert maps.add_map_data(group, professor, course) == {
        {"NH": "Mark", "Steve": "Some Professor", "QEA": 100}
    }


def test_make_geodata_datatype():
    """
    Test that the functions output is a geodataframe.
    """
    random_dict = {"NH": "Mark", "MO": "Noah", "CO": "Crazy Noah"}
    # Change response to be right
    assert isinstance(maps.make_geodata(random_dict)) == "Geo_Data_Frame"
