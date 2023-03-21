import requests, json


def get_data(start_congress, end_congress, API_KEY):
    """
    this is a docstring.
    """
    with open("bill_data.csv", "w") as bill_data:
        for congress in range(start_congress, end_congress + 1):
            bills = requests.get(
                f"https://api.congress.gov/v3/bill/{congress}/s?&api_key={API_KEY}"
            )
            bill_nye = bills.json()
            bill_values = []
            bills_list = bill_nye["bills"]
            for bill in bills_list:
                bill_number = bill["number"]
                individual_bill = requests.get(
                    f"https://api.congress.gov/v3/bill/{congress}/s/{bill_number}?api_key={API_KEY}"
                )
                bill_dict = individual_bill.json()["bill"]
                for sponsor in bill_dict["sponsors"]:
                    bill_values = [
                        bill_dict["number"],
                        sponsor["fullName"],
                        sponsor["state"],
                        bill_dict["policyArea"]["name"],
                    ]
                    print(bill_values, file=bill_data)
