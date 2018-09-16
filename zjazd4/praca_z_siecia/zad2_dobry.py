import sys
import requests
from collections import namedtuple

Weather = namedtuple("Weather", ["location", 'the_temp', 'air_pressure', 'humidity'])


def get_location_id(location_name):
    """to jest docstring"""
    with requests.get(f"https://www.metaweather.com/api/location/search/?query={location_name}") as f:
        data = f.json()
        # data = json.loads(data)
    return data[0]["woeid"]


def get_location_weather(location_id):
    with requests.get(f"https://www.metaweather.com/api/location/{location_id}/") as f:
        data = f.json()

    weather = Weather(
        location=data['title'],
        the_temp=data['consolidated_weather'][0]['the_temp'],
        air_pressure=data['consolidated_weather'][0]['air_pressure'],
        humidity=data['consolidated_weather'][0]['humidity'],
    )
    return weather


def present_results(weather):
    output = f"""Pogoda w lokalizacji: {weather.location}\n""" \
             f"""temperatura = {weather.the_temp} °C\n""" \
             f"""ciśnienie powietrza = {weather.air_pressure} hPa\n""" \
             f"""wilgotność = {weather.humidity} %\n\n"""
    print(output)


if __name__ == "__main__":
    id_ = get_location_id(sys.argv[1])
    weather = get_location_weather(id_)
    present_results(weather)