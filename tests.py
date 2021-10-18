import requests

data = {
    "value_1": 1,
    "value_2": 2,
}


res = requests.post("http://127.0.0.1:8080/calc/add", data=data)

print(res.text)


res = requests.post("http://127.0.0.1:8080/calc/multiply", data=data)

print(res.text)


