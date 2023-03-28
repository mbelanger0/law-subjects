import maps


def test_make_geodata_datatype():
    """
    Test that the functions output is a geodataframe.
    """
    random_dict = {"NH": "Mark", "MO": "Noah", "CO": "Crazy Noah"}
    # Change response to be right
    assert isinstance(maps.make_geodata(random_dict)) == "Geo_Data_Frame"
