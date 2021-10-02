import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
APP_ID = os.environ.get('APP_ID')
API_KEY = os.environ.get('API_KEY')
# USERNAME = os.environ.get('USERNAME')
PROJECTNAME = "Workouts Tracking"
SHEETNAME = os.environ.get('SHEETNAME')

exercise_config = {
    "query": input("What Exercise Did you perform: "),
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
}
response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=exercise_config,
                         headers=headers)
print(response.json())
exercise = response.json()['exercises'][0]['user_input']
duration = response.json()['exercises'][0]['duration_min']
Calorie = response.json()['exercises'][0]['nf_calories']

today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")

# workout = {
#     "Duration": duration,
#     "Exercise": exercise,
#     "Calorie": Calorie,
#     "Date": today.strftime("%d/%m/%Y"),
#     "Time": today.strftime("%H:%M:%S"),
# }

for exercise in response.json()["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["user_input"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    basic_headers = {
        "Authorization": f"Basic {os.environ.get('TOKEN')}"
    }

    sheet_response = requests.post(url=os.environ.get('SHEETENDPOINTS'),
                                   json=sheet_inputs,
                                   auth=(os.environ.get('USERNAME_NAME'), os.environ.get('PASSWORD')),
                                   headers=basic_headers)
    print(sheet_response.text)

