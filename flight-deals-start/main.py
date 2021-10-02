from data_manager import DataManager
from flight_search import FlightSearch
from datetime import *
from notification_manager import NotificationManager

sheety_data = DataManager()
sheet_data = sheety_data.get_destination_data()

notification_manager = NotificationManager()

flight_search = FlightSearch()

if sheet_data[0]['iataCode'] == "":
    for row in sheet_data:
        row['iataCode'] = flight_search.get_destination_code(row['city'])

    sheety_data.destination_data = sheet_data
    sheety_data.update_destination_code()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.search_flights(
        fly_from='LON',
        date_from=tomorrow,
        date_to=six_month_from_today,
        fly_to=destination['iataCode']
    )

    if flight is None:
        continue

    if flight.price < destination['lowestPrice']:
        users = sheety_data.get_customer_details()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]
        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

        link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"
        notification_manager.send_mail(emails, message, link)

        # notification_manager.send_mail(
        #     message=f"Low Price Alert! Only ${flight.price} to fly from "
        #             f"{flight.origin_city}-{flight.origin_airport}"
        #             f"to {flight.destination_city=}-{flight.destination_airport},"
        #             f"from {flight.out_date} to {flight.return_date}"
        # )
