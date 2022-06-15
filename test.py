import requests

BASE = "http://127.0.0.1:5000"
dictToSend = {
    "name": "Nicole",
    "age": 22,
    "gender": "female",
    "email":"n@gmail.com"
}

response = requests.post(BASE + "/api/carla",json=dictToSend)
print(response.json())
