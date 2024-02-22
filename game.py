import random
from weather_info_api_scripts import get_weather_by_city_name, print_facts_about_city
from city_info_api_scripts import get_local_names
from datetime import datetime as dt
from safedict import SafeDict
from game_consts import METRIC, IMPERIAL, NUMBER_OF_FETCH_ATTEMPTS

class Game:

    def __init__(self):
        self.current_city = None
        self.acceptable_city_names = []
        self.full_weather_info = None
        self.most_recent_weather_data = SafeDict()
        self.measurement_system = None
        self.start_game()

    def start_game(self):
        self.choose_measurement_system()
        self.fetch_weather_info()
        if self.full_weather_info == None:
            print('Conntection error')
            return

        self.most_recent_weather_data = self.full_weather_info['list'][-1]

        print_facts_about_city(self.most_recent_weather_data, self.full_weather_info['city'])

    def choose_measurement_system(self):
        print('Choose measurement system:')
        print('1. Metric')
        print('2. Imperial')
        while self.measurement_system == None:
            chosen_option = input()
            if chosen_option == '1':
                self.measurement_system = METRIC
            elif chosen_option == '2':
                self.measurement_system = IMPERIAL
            else: 
                print('Try again!')
        print(f'{self.measurement_system.capitalize()} sytem chosen')
        print_devider()
        

    def fetch_weather_info(self):
        reconnection_attempt = 0
        while not self.full_weather_info and reconnection_attempt < NUMBER_OF_FETCH_ATTEMPTS:
            self.pick_city()
            self.full_weather_info = get_weather_by_city_name(self.current_city, self.measurement_system)
            reconnection_attempt += 1
            
    def pick_city(self):
        self.current_city = pick_random_city()
        # self.current_city = "Los Angeles"
        self.acceptable_city_names = get_local_names(self.current_city)
        print(f'Chosen city: {self.current_city}')

def pick_random_city():
    with open('cities.txt', 'r') as file:
        cities =  [line.strip() for line in file]
        return cities[random.randint(0,len(cities))]
    
def print_devider():
    print('==============================')
if __name__ == '__main__':
    game = Game()