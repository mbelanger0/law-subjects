"""
Contains a function to get data from the US Congress API.
"""
import requests
import pandas as pd


def get_data(start_congress, end_congress, api_key):
    """
    This function takes a state congress, an end congress and an API key and
    gets data about bills proposed during those congresses from the US Congress
    API.The function saves the data to a file called "bills_data.csv"

    Args:
        start_congress is an integer representing the first congress that the
            function will get data from.

        end_congress is an integer representing the last congress that the
            function will get data from.

        API_KEY is the API key given to the user to access the US Congress API.
            It is stored in the form of a string.

        Returns: None
    """
    all_data = []
    for congress in range(start_congress, end_congress + 1):
        bills = requests.get(
            f"https://api.congress.gov/v3/bill/{congress}/s?limit=250&api_key={api_key}"
        )
        bill_data = bills.json()
        bills_list = bill_data["bills"]
        for bill in bills_list:
            bill_number = bill["number"]
            individual_bill = requests.get(
                f"https://api.congress.gov/v3/bill/{congress}/s/{bill_number}?api_key={api_key}"
            )
            bill_dict = individual_bill.json()["bill"]
            for sponsor in bill_dict["sponsors"]:
                if "policyArea" in bill_dict:
                    all_data.append(
                        [
                            bill_dict["congress"],
                            bill_dict["number"],
                            sponsor["fullName"],
                            sponsor["state"],
                            bill_dict["policyArea"]["name"],
                        ]
                    )
    bills_dataframe = pd.DataFrame(all_data)
    bills_dataframe.columns = ["Congress", "Number", "Senator", "State", "Policy Areas"]
    bills_dataframe.to_csv("bills_data.csv", index=False)
    pd.read_csv(
        "bills_data.csv",
        names=["Congress", "Number", "Senator", "State", "Policy Areas"],
    )
