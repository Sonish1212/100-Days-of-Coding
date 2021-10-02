import requests
from datetime import datetime

USERNAME = "sonish"
TOKEN = "sadfgaesdfgasd"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Minutes",
    "unit": "Minute",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

today = datetime(year=2021, month=7, day=19)
date = today.strftime("%Y%m%d")

post_graph = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{date}"
# post_config = {
#     "date": date,
#     "quantity": "150"
# }

response = requests.delete(url=post_graph, headers=headers)
print(response.text)
