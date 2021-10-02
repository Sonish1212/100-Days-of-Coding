import requests

SHETTY_ENDPOINTS = "https://api.sheety.co/f0a09b074d793494e045abc7873356ff/flightDeals"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(f"{SHETTY_ENDPOINTS}/prices")
        response.raise_for_status()
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }

            }
            response = requests.put(url=f"{SHETTY_ENDPOINTS}/{city['id']}", json=new_data)
            response.raise_for_status()
            print(response.text)

    def get_customer_details(self):
        customers_endpoint = f"{SHETTY_ENDPOINTS}/users"
        # first_name = input("Enter your first name: ")
        # last_name = input("Enter your last name: ")
        # email = input("Enter your email: ")
        # re_email = input("Enter your email again: ")
        # if email == re_email:
        #     body = {
        #         "user": {
        #             "firstName": first_name,
        #             "lastName": last_name,
        #             "email": email
        #         }
        #     }
        #     header = {
        #         "Content-Type": "application/json"
        #     }
        #     response = requests.post(url=f"{SHETTY_ENDPOINTS}/users", json=body, headers=header)
        #     response.raise_for_status()
        #     print(response.text)
        response = requests.get(url=customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
