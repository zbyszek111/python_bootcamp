import urllib.request
import json
import sys

query = input("podaj lokalizacje")

with urllib.request.urlopen(f"https://www.metaweather.com//api/location/search/?query={query}") as f:
    data = f.read()
    data = json.loads(data)
    key = data[0]['woeid']


with urllib.request.urlopen(f"https://www.metaweather.com/api/location/{key}/") as f:
    data = f.read()
    data = json.loads(data)

print(data)
print(key)





