import requests

url = "https://nominatim.openstreetmap.org/search"
params = {"q": "Lviv", "format": "json", "limit": 1}

headers = {"User-Agent": "Student/1.0"}

response = requests.get(url, params=params, headers=headers)
data = response.json()

print(data)