import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "091663312d2a88fac4c9be898560ff17"
account_sid = 'ACbb1904b33ebaec888a6c6426deb8f29c'
auth_token = '29072fa0f1580edbf3b90eee376d9acb'

parameters = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_key,
    "exclude": "current,minutely,daily,"
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
# print(weather_data)
hourly_weather_data = weather_data["hourly"][:12]

will_rain = False

for hours in hourly_weather_data:
    condition_code = hours["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Hey today sky seems to be upset. Get yourself a ☂️",
        from_="+1 646 461 4749",
        to="+9779866126473"
    )

    print(message.status)


