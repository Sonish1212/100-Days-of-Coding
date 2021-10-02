import requests
from flight_data import FlightData

SEARCH_ENDPOINT = "https://tequila-api.kiwi.com/v2"
APIKEY = "Rx7K4rPzuL2JMTqlJEDAdqcrBfaZ_kbT"
TEQPOINT = "https://tequila-api.kiwi.com"
TEQKEY = "Rx7K4rPzuL2JMTqlJEDAdqcrBfaZ_kbT"


class FlightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQPOINT}/locations/query"
        headers = {"apikey": TEQKEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        result = response.json()['locations'][0]['code']
        return result

    def search_flights(self, fly_from, date_from, date_to, fly_to):
        query = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        headers = {
            "apikey": APIKEY
        }
        response = requests.get(url=f"{SEARCH_ENDPOINT}/search", headers=headers, params=query)
        response.raise_for_status()
        try:
            data = response.json()['data'][0]

        except IndexError:
            query["max_stopovers"] = 1
            response = requests.get(
                url=f"{SEARCH_ENDPOINT}/search",
                headers=headers,
                params=query,
            )
            data = response.json()["data"][0]
            print(data)
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][1]["cityTo"],
                destination_airport=data["route"][1]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][2]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )
            return flight_data
        else:
            flight_data = FlightData(
                price=data['price'],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            return flight_data



