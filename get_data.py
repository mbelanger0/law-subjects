import requests, json
import pandas as pd


def get_data(start_congress, end_congress, API_KEY):
    """
    this is a docstring.
    """
    all_data = []
    for congress in range(start_congress, end_congress + 1):
        bills = requests.get(
            f"https://api.congress.gov/v3/bill/{congress}/s?limit=90&api_key={API_KEY}"
        )
        bill_nye = bills.json()
        bills_list = bill_nye["bills"]
        for bill in bills_list:
            bill_number = bill["number"]
            individual_bill = requests.get(
                f"https://api.congress.gov/v3/bill/{congress}/s/{bill_number}?api_key={API_KEY}"
            )
            bill_dict = individual_bill.json()["bill"]
            for sponsor in bill_dict["sponsors"]:
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
