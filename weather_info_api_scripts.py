import requests
from api_consts import WEATHER_INFO_API_URL
from api_key import API_KEY #FILE NOT INCLUDED IN REPOSITORY
from game_consts import METRIC
from city_info_api_scripts import get_location_by_city_name
from request_response_handler import process_response
from dict_scripts import print_dict
from safedict import SafeDict

def get_weather_by_city_name(city_name, measurement_system = METRIC):
    lat, lon = get_location_by_city_name(city_name)
    return get_weather_by_location(lat, lon, measurement_system)

def get_weather_by_location(lat, lon, measurement_system = METRIC):
    parameters = {
        'lat': lat,
        'lon': lon,
        'appid': API_KEY,
        'units': measurement_system
    }
    original_response = requests.get(WEATHER_INFO_API_URL, parameters)
    processed_response = process_response(original_response)
    if processed_response:
        results = processed_response.json()
        return SafeDict(**results)
    else:
        # print_dict(0, original_response.json()) #only for tests
        return None

def print_weather_by_city_name(city_name):
    print_dict(0, get_weather_by_city_name(city_name))


def print_weather_by_location(lat, lon):
    print_dict(0, get_weather_by_location(lat, lon))
