import requests
import datetime as dt
import smtplib
import time

MY_LAT = 27.717245
MY_LONG = 85.323959
my_email = 'loooksoook@gmail.com'
my_pass = '143Muller'

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    'formatted': 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
print(data)
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
print(sunset)
print(sunrise)

time_now = dt.datetime.utcnow()

hour = time_now.hour
print(hour)

while True:
    time.sleep(60)
    if sunrise < hour < sunset:
        iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
        iss_response.raise_for_status()
        data_iss = iss_response.json()
        print(data_iss)
        longitude = float(data_iss["iss_position"]['longitude'])
        latitude = float(data_iss["iss_position"]['latitude'])
        if MY_LAT == latitude and MY_LONG == longitude:
            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_pass)
                connection.sendmail(from_addr=my_email, to_addrs='sonishkhanal@gmail.com',
                                    msg="Subject: ISS Satellite\n\nThe satellite is over your roof watch out")

