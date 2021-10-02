import requests
import datetime

PIXELAENDPOINT = "https://pixe.la/v1/users"

header = {
    "X-USER-TOKEN": "dsafsdnkdnfsfvf"
}

# body = {
#     "token": "dsafsdnkdnfsfvf",
#     "username": "sonishkhanal",
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
#
# response = requests.post(url=PIXELAENDPOINT, json=body)
# response.raise_for_status()
# data = response.text
# print(data)

# body = {
#     "id": "graph1",
#     "name": "Reading Books",
#     "unit": "pages",
#     "type": "int",
#     "color": "sora"
# }
#
# response = requests.post(url=f"{PIXELAENDPOINT}/sonishkhanal/graphs", json=body, headers=header)
# response.raise_for_status()
# data = response.text
# print(data)
today = datetime.datetime.today()
date = today.strftime("%Y%m%d")
post_config = {
    "date": date,
    "quantity": input("Enter how many pages have you read today: ")
}

response = requests.post(url=f"{PIXELAENDPOINT}/sonishkhanal/graphs/graph1", json=post_config, headers=header)
response.raise_for_status()
data = response.text
print(data)
