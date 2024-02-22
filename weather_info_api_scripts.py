import requests
from api_consts import WEATHER_INFO_API_URL
from api_key import API_KEY #FILE NOT INCLUDED IN REPOSITORY
from game_consts import METRIC
from city_info_api_scripts import get_location_by_city_name
from request_response_handler import process_response
from dict_scripts import print_dict
from safedict import SafeDict
from date_converters import convert_unix_to_datetime_txt, convert_timezone_offset_from_seconds_to_hours


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
        print_dict(0, original_response)
        return None

def print_weather_by_city_name(city_name):
    print_dict(0, get_weather_by_city_name(city_name))


def print_weather_by_location(lat, lon):
    print_dict(0, get_weather_by_location(lat, lon))

def print_facts_about_city(most_recent_weather_data, city_info, measurement_system = METRIC):
    temperature_unit = "*C" if measurement_system == METRIC else 'F'
    main_weather_info = most_recent_weather_data['main']
    temperature = main_weather_info['temp']
    pressure = main_weather_info['pressure']
    humidity = main_weather_info['humidity']
    visibility = most_recent_weather_data['visibility']
    probability_of_precipitation = most_recent_weather_data['pop']
    snow = most_recent_weather_data['snow']#not always implemented
    rain = most_recent_weather_data['rain']#not always implemented
    population = city_info['population']
    timezone_in_seconds = city_info['timezone']
    timezone = convert_timezone_offset_from_seconds_to_hours(timezone_in_seconds)
    sunrise = convert_unix_to_datetime_txt(city_info['sunrise'], '%H:%M:%S', timezone_in_seconds)
    sunset = convert_unix_to_datetime_txt(city_info['sunset'], '%H:%M:%S', timezone_in_seconds)
    date = most_recent_weather_data['dt']
    if date:
        print(f"Weather info fetched at {convert_unix_to_datetime_txt(date, '%H:%M:%S', timezone_in_seconds)}")
    if temperature:
        print(f'Temperature: {temperature}')
    if pressure:
        print(f'Pressure: {pressure} hPa')
    if humidity:
        print(f'Humidity: {humidity}%')
    if visibility:
        print(f'Visibility: {visibility}')
    if probability_of_precipitation:
        print(f'Probability of precipitation: {probability_of_precipitation*100}%')
    if snow:
        print(f"Snow volume in the last 3h: {snow['3h']} mm")
    if rain:
        print(f"Rain volume in the last 3h: {rain['3h']} mm")
    if population:
        print(f'Population: {population}')#{">" if population > 1000000 else ""}
    if timezone:
        print(f'Timezone: {timezone}')
    if sunrise:
        print(f'Sunrise: {sunrise}')    
    if sunset:
        print(f'Sunset: {sunset}')
