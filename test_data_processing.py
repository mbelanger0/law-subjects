"""
Unit tests for functions in data_processing.py
"""
import data_processing


def test_count_subject_multiple_subject():
    """
    Tests that a state having multiple subjects returns the counted
    number of those subjects
    """
    state_policy_dict = {
        "MO": ["Congress", "Congress", "Congress", "Congress"],
        "NE": [
            "Finance and Financial Sector",
            "Finance and Financial Sector",
            "Finance and Financial Sector",
        ],
        "MD": ["International Affairs", "International Affairs"],
    }
    assert data_processing.count_subject(state_policy_dict) == 1
