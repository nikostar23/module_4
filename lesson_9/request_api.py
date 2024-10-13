import requests

res = requests.get("http://numbersapi.com/8/13/date")
print(res.json)
print(res.text)
