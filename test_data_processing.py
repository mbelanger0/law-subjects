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
    }
    assert data_processing.count_subject(state_policy_dict) == {
        "MO": {
            "Agriculture and Food": 0,
            "Animals": 0,
            "Armed Forces and National Security": 0,
            "Arts, Culture, Religion": 0,
            "Civil Rights and Liberties, Minority Issues": 0,
            "Commerce": 0,
            "Congress": 4,
            "Crime and Law Enforcement": 0,
            "Economics and Public Finance": 0,
            "Education": 0,
            "Emergency Management": 0,
            "Energy": 0,
            "Environmental Protection": 0,
            "Families": 0,
            "Finance and Financial Sector": 0,
            "Foreign Trade and International Finance": 0,
            "Government Operations and Politics": 0,
            "Health": 0,
            "Housing and Community Development": 0,
            "Immigration": 0,
            "International Affairs": 0,
            "Labor and Employment": 0,
            "Law": 0,
            "Native Americans": 0,
            "Public Lands and Natural Resources": 0,
            "Science, Technology, Communications": 0,
            "Social Sciences and History": 0,
            "Social Welfare": 0,
            "Sports and Recreation": 0,
            "Taxation": 0,
            "Transportation and Public Works": 0,
            "Water Resources Development": 0,
        }
    }


def test_count_subject_single_subject():
    """
    Tests that a state having a single subject returns the counted
    number of that subject.
    """
    state_policy_dict = {"CO": ["Water Resources Development"]}
    assert data_processing.count_subject(state_policy_dict) == {
        "CO": {
            "Agriculture and Food": 0,
            "Animals": 0,
            "Armed Forces and National Security": 0,
            "Arts, Culture, Religion": 0,
            "Civil Rights and Liberties, Minority Issues": 0,
            "Commerce": 0,
            "Congress": 0,
            "Crime and Law Enforcement": 0,
            "Economics and Public Finance": 0,
            "Education": 0,
            "Emergency Management": 0,
            "Energy": 0,
            "Environmental Protection": 0,
            "Families": 0,
            "Finance and Financial Sector": 0,
            "Foreign Trade and International Finance": 0,
            "Government Operations and Politics": 0,
            "Health": 0,
            "Housing and Community Development": 0,
            "Immigration": 0,
            "International Affairs": 0,
            "Labor and Employment": 0,
            "Law": 0,
            "Native Americans": 0,
            "Public Lands and Natural Resources": 0,
            "Science, Technology, Communications": 0,
            "Social Sciences and History": 0,
            "Social Welfare": 0,
            "Sports and Recreation": 0,
            "Taxation": 0,
            "Transportation and Public Works": 0,
            "Water Resources Development": 1,
        }
    }


def test_count_subject_different_subjects():
    """
    Tests that a state having multiple different subjects returns the counted
    number of those subjects.
    """
    state_policy_dict = {
        "NH": ["Congress", "Congress", "Congress", "Congress"],
        "CO": ["Water Resources Development"],
    }
    assert data_processing.count_subject(state_policy_dict) == {
        "NH": {
            "Agriculture and Food": 0,
            "Animals": 0,
            "Armed Forces and National Security": 0,
            "Arts, Culture, Religion": 0,
            "Civil Rights and Liberties, Minority Issues": 0,
            "Commerce": 0,
            "Congress": 4,
            "Crime and Law Enforcement": 0,
            "Economics and Public Finance": 0,
            "Education": 0,
            "Emergency Management": 0,
            "Energy": 0,
            "Environmental Protection": 0,
            "Families": 0,
            "Finance and Financial Sector": 0,
            "Foreign Trade and International Finance": 0,
            "Government Operations and Politics": 0,
            "Health": 0,
            "Housing and Community Development": 0,
            "Immigration": 0,
            "International Affairs": 0,
            "Labor and Employment": 0,
            "Law": 0,
            "Native Americans": 0,
            "Public Lands and Natural Resources": 0,
            "Science, Technology, Communications": 0,
            "Social Sciences and History": 0,
            "Social Welfare": 0,
            "Sports and Recreation": 0,
            "Taxation": 0,
            "Transportation and Public Works": 0,
            "Water Resources Development": 0,
        },
        "CO": {
            "Agriculture and Food": 0,
            "Animals": 0,
            "Armed Forces and National Security": 0,
            "Arts, Culture, Religion": 0,
            "Civil Rights and Liberties, Minority Issues": 0,
            "Commerce": 0,
            "Congress": 0,
            "Crime and Law Enforcement": 0,
            "Economics and Public Finance": 0,
            "Education": 0,
            "Emergency Management": 0,
            "Energy": 0,
            "Environmental Protection": 0,
            "Families": 0,
            "Finance and Financial Sector": 0,
            "Foreign Trade and International Finance": 0,
            "Government Operations and Politics": 0,
            "Health": 0,
            "Housing and Community Development": 0,
            "Immigration": 0,
            "International Affairs": 0,
            "Labor and Employment": 0,
            "Law": 0,
            "Native Americans": 0,
            "Public Lands and Natural Resources": 0,
            "Science, Technology, Communications": 0,
            "Social Sciences and History": 0,
            "Social Welfare": 0,
            "Sports and Recreation": 0,
            "Taxation": 0,
            "Transportation and Public Works": 0,
            "Water Resources Development": 1,
        },
    }


def test_count_subject_no_states():
    """
    Tests that not imputing any states results an empty dict.
    """
    state_policy_dict = {}
    assert not data_processing.count_subject(state_policy_dict)
