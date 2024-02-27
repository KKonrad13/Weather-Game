import requests
from api_consts import CITY_INFO_API_URL
from api_key import API_KEY #FILE NOT INCLUDED IN REPOSITORY
from dict_scripts import print_dict
from request_response_handler import process_response

def get_location_by_city_name(city_name):
    parameters = {
        'q' : city_name,
        'limit' : 1,
        'appid' : API_KEY 
    }
    response = process_response(requests.get(CITY_INFO_API_URL, parameters))
    if response:
        city_info = response.json()[0]
        return city_info['lat'], city_info['lon']
    else:
        return None, None

def check_different_city_names_by_country(city_name):
    local_names = get_local_names(city_name)
    if local_names:
        if isinstance(local_names, dict):
            print(f'City name: {city_name}')
            for region_code in local_names:
                print(f'Region: {region_code}, name: {local_names[region_code]}')
        else:
            print(f'No results about different names for this city: {city_name}')

def get_local_names(city_name):
    parameters = {
        'q' : city_name,
        'appid' : API_KEY 
    }
    response = process_response(requests.get(CITY_INFO_API_URL, parameters))

    if response:
        data = response.json()[0]
        local_names = data.get('local_names')
        if isinstance(local_names, dict):
            return [local_names[key] for key in local_names]
        else:
            return None

def print_all_info_about_city(city_name):
    parameters = {
        'q' : city_name,
        'appid' : API_KEY 
    }
    response = process_response(requests.get(CITY_INFO_API_URL, parameters))

    if response:
        results = response.json()
        for result in results:
            print_dict(0, result)