import random
from weather_info_api_scripts import get_weather_by_city_name
from city_info_api_scripts import get_local_names
from datetime import datetime as dt
from safedict import SafeDict
from game_consts import METRIC, IMPERIAL, NUMBER_OF_FETCH_ATTEMPTS
from CityFacts import CityFacts

class Game:

    def __init__(self):
        self.current_city = None
        self.acceptable_city_names = []
        self.full_weather_info = None
        self.most_recent_weather_data = SafeDict()
        self.measurement_system = METRIC
        self.city_guessed = ''

    def print_menu(self):
        print("Guess the city!")
        print("1. Start")
        print("2. Change measurement system")
        print("Anything else to exit.")
        chosen_option = input()
        if chosen_option == "1":
            self.start_game()
        elif chosen_option == "2":
            self.measurement_system = None
            self.choose_measurement_system()
        print_divider()

    def start_game(self):
        self.fetch_weather_info()
        if self.full_weather_info == None:
            print("Conntection error")
            return

        self.most_recent_weather_data = self.full_weather_info["list"][-1]
        self.original_cityfacts = CityFacts(
            self.most_recent_weather_data,
            self.full_weather_info["city"],
            self.measurement_system,
        )
        self.original_cityfacts.print_city_facts()
        print_divider()

        while not self.is_game_won():
            self.guess_city()

    def choose_measurement_system(self):
        print("Choose measurement system:")
        print("1. Metric")
        print("2. Imperial")
        while self.measurement_system == None:
            chosen_option = input()
            if chosen_option == "1":
                self.measurement_system = METRIC
            elif chosen_option == "2":
                self.measurement_system = IMPERIAL
            else:
                print("Try again!")
        print(f"{self.measurement_system.capitalize()} sytem chosen")
        print_divider()

    def fetch_weather_info(self):
        reconnection_attempt = 0
        while (
            not self.full_weather_info
            and reconnection_attempt < NUMBER_OF_FETCH_ATTEMPTS
        ):
            self.pick_city()
            self.full_weather_info = get_weather_by_city_name(
                self.current_city, self.measurement_system
            )
            reconnection_attempt += 1

    def pick_city(self):
        self.current_city = pick_random_city()
        self.acceptable_city_names = get_local_names(self.current_city)
        print(f"Chosen city: {self.current_city}")

    def guess_city(self):
        self.city_guessed = input("Give your guess: ")
        if self.is_game_won():
            self.game_won()
        else:
            guessed_city_weather_info = get_weather_by_city_name(
                self.city_guessed, self.measurement_system
            )
            if not guessed_city_weather_info:
                print("Could not fetch data about this city. Try again!")
            else:
                most_recent_weather_data = guessed_city_weather_info["list"][-1]
                guessed_cityfacts = CityFacts(
                    most_recent_weather_data,
                    guessed_city_weather_info["city"],
                    self.measurement_system,
                )
                self.original_cityfacts.print_difference_between_cities(guessed_cityfacts)
                print_divider()
                print('Try again!')

    def handle_possible_guessed_city_fetch_error(self):
        pass

    def is_game_won(self):
        return self.city_guessed.strip().lower() in [city_name.strip().lower() for city_name in self.acceptable_city_names]

    def game_won(self):
        print(
            f"Congratulations! You won! The city that you were looking for was indeed {self.current_city}!"
        )


def pick_random_city():
    with open("cities.txt", "r") as file:
        cities = [line.strip() for line in file]
        return cities[random.randint(0, len(cities) - 1)]


def print_divider():
    print("==============================")

if __name__ == "__main__":
    game = Game()
    game.print_menu()
