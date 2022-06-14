import requests

BASE = "http://127.0.0.1:5000"
dictToSend = {
    "name": "Brian",
    "age": 75,
    "gender": "male",
    "email":"b@gmail.com"
}

response = requests.post(BASE + "/api/carla",json=dictToSend)
print(response.json())
