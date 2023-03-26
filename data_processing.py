""" A file containing the data processing functions."""

subject_list = [
    "Agriculture and Food",
    "Animals",
    "Armed Forces and National Security",
    "Arts, Culture, Religion",
    "Civil Rights and Liberties, Minority Issues",
    "Commerce",
    "Congress",
    "Crime and Law Enforcement",
    "Economics and Public Finance",
    "Education",
    "Emergency Management",
    "Energy",
    "Environmental Protection",
    "Families",
    "Finance and Financial Sector",
    "Foreign Trade and International Finance",
    "Government Operations and Politics",
    "Health",
    "Housing and Community Development",
    "Immigration",
    "International Affairs",
    "Labor and Employment",
    "Law",
    "Native Americans",
    "Public Lands and Natural Resources",
    "Science, Technology, Communications",
    "Social Sciences and History",
    "Social Welfare",
    "Sports and Recreation",
    "Taxation",
    "Transportation and Public Works",
    "Water Resources Development",
]


def count_subject(state_policy_dict):
    """
    Counts the number of times each state presents bills with each
    policy subject

    Args:
        state_policy_dict: a dictionary where the keys are each state
            that proposed legislation, and the values are lists containing
            each category of legislation.

    Returns:
        state_subject_dict: a dictionary where the keys are each state, and the
            values are dictionaries where each each key is a law subject and
            each value is the number of times the state passed legislation of that
            subject.
    """
    state_subject_dict = {}
    for state in state_policy_dict:
        state_subject_dict[state] = {}
        for subject in subject_list:
            state_subject_dict[state][subject] = state_policy_dict[state].count(subject)
    return state_subject_dict


def common_subject(state_subject_dict):
    """
    Returns each state's most common legislation subject. If there are multiple
    equally preferred subjects, returns the alphabetically first
    (based on the subject_list variable).

    Args:
        state_subject_dict: a dictionary where the keys are each state, and the
            values are dictionaries where each each key is a law subject and
            each value is the number of times the state passed legislation of that
            subject.
    Returns:
        most_common_policy_area: a dictionary where the keys are each state, and the
            most common policy subject.
    """
    most_common_policy_area = {}
    for state in state_subject_dict:
        most_common_policy_area[state] = max(
            state_subject_dict[state], key=state_subject_dict[state].get
        )
    return most_common_policy_area
