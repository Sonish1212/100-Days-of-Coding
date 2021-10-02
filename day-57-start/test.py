import requests

param = {
    "name": "sonish"
}
response = requests.get("https://api.agify.io", params=param)
data = response.json()
print(data["age"])

response2 = requests.get("https://api.genderize.io", params=param)
dat = response2.json()
print(dat["gender"])

print(dat)
