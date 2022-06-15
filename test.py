import requests

BASE = "http://127.0.0.1:5000"
dictToSend = {
    "name": "test",
    "age": 100,
    "gender": "female",
    "email":"test@gmail.com"
}

response = requests.post(BASE + "/api/carla",json=dictToSend)
print(response.json())
