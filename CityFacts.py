from date_converters import (
    convert_timezone_offset_from_seconds_to_UTC,
    convert_unix_to_datetime_txt,
    seconds_to_hms
)
from game_consts import METRIC, IMPERIAL
from string_formats import format_to_max_one_decimal_place
import datetime as dt

class CityFacts:

    def __init__(self, most_recent_weather_data, city_info, measurement_system):
        main_weather_info = most_recent_weather_data["main"]
        self.temperature = main_weather_info["temp"]
        self.pressure = main_weather_info["pressure"]
        self.humidity = main_weather_info["humidity"]
        self.visibility = most_recent_weather_data["visibility"]
        self.probability_of_precipitation = most_recent_weather_data["pop"]
        self.snow = most_recent_weather_data["snow"]  # not always implemented
        self.rain = most_recent_weather_data["rain"]  # not always implemented
        self.population = city_info["population"]
        self.timezone_in_seconds = city_info["timezone"]
        self.timezone = convert_timezone_offset_from_seconds_to_UTC(
            self.timezone_in_seconds
        )
        self.sunrise = convert_unix_to_datetime_txt(
            city_info["sunrise"], "%H:%M:%S", self.timezone_in_seconds
        )
        self.sunset = convert_unix_to_datetime_txt(
            city_info["sunset"], "%H:%M:%S", self.timezone_in_seconds
        )
        self.date = most_recent_weather_data["dt"]
        degree_sign = "\N{DEGREE SIGN}"
        self.temperature_unit = (
            f"{degree_sign}C" if measurement_system == METRIC else f"{degree_sign}F"
        )
        self.length_unit = "m" if measurement_system == METRIC else "ft"

    def print_difference_between_cities(self, other):
        print("Difference between city facts:")
        self.print_temperature_diff(other)
        self.print_pressure_diff(other)
        self.print_humidity_diff(other)
        self.print_visibility_diff(other)
        self.print_probability_of_precipitation_diff(other)
        self.print_snow_diff(other)
        self.print_rain_diff(other)
        self.print_population_diff(other)
        self.print_timezone_diff(other)
        self.print_sunrise_diff(other)
        self.print_sunset_diff(other)

    def print_temperature_diff(self, other):
        self.print_simple_diff(
            self.temperature,
            other.temperature,
            "The original temperature is greater by",
            "The original temperature is smaller by",
            "Temperature",
            self.temperature_unit,
        )

    def print_pressure_diff(self, other):
        self.print_simple_diff(
            self.pressure,
            other.pressure,
            "The original pressure is greater by",
            "The original pressure is smaller by",
            "Pressure",
            " hPa",
        )

    def print_humidity_diff(self, other):
        self.print_simple_diff(
            self.humidity,
            other.humidity,
            "The original humidity is greater by",
            "The original humidity is smaller by",
            "Humidity",
            "% points",
        )

    def print_visibility_diff(self, other):
        self.print_simple_diff(
            self.visibility,
            other.visibility,
            "The original visibility is greater by",
            "The original visibility is smaller by",
            "Visibility",
            f" {self.length_unit}",
        )

    def print_probability_of_precipitation_diff(self, other):
        self.print_simple_diff(
            self.probability_of_precipitation * 100,
            other.probability_of_precipitation * 100,
            "The original probability of precipitation is greater by",
            "The original probability of precipitation is smaller by",
            "Probability of precipitation",
            "% points",
        )

    def print_snow_diff(self, other):
        if self.snow and other.snow:
            self.print_simple_diff(
                self.snow["3h"],
                other.snow["3h"],
                "The original volume of snow is greater by",
                "The original volume of snow is smaller by",
                "Volume of snow",
            )

    def print_rain_diff(self, other):
        if self.rain and other.rain:
            self.print_simple_diff(
                self.rain["3h"],
                other.rain["3h"],
                "The original volume of rain is greater by",
                "The original volume of rain is smaller by",
                "Volume of rain",
            )

    def print_population_diff(self, other):
        self.print_simple_diff(
            self.population,
            other.population,
            "The original population is larger by",
            "The original population is smaller by",
            "Population size",
        )

    def print_timezone_diff(self, other):
        if self.timezone_in_seconds and other.timezone_in_seconds:
            timezone_diff = format_to_max_one_decimal_place(
                abs(self.timezone_in_seconds - other.timezone_in_seconds) / 3600
            )
            if self.timezone_in_seconds > other.timezone_in_seconds:
                print(f"The original timezone is ahead {timezone_diff} h.")
            else:
                print(f"The original timezone is behind {timezone_diff} h.")

    def print_sunrise_diff(self, other):
        if self.sunrise and other.sunrise:
            sunrise_diff = (dt.datetime.strptime(self.sunrise, "%H:%M:%S") - dt.datetime.strptime(other.sunrise, "%H:%M:%S")).total_seconds()
            formatted_sunrise_diff = seconds_to_hms(abs(sunrise_diff))
            if sunrise_diff > 0:
                print(f"The original sunrise is {formatted_sunrise_diff} later.")
            else:
                print(f"The original sunrise is {formatted_sunrise_diff} earlier.")

    def print_sunset_diff(self, other):
        if self.sunset and other.sunset:
            sunset_diff = (dt.datetime.strptime(self.sunset, "%H:%M:%S") - dt.datetime.strptime(other.sunset, "%H:%M:%S")).total_seconds()
            formatted_sunset_diff = seconds_to_hms(abs(sunset_diff))
            if sunset_diff > 0:
                print(f"The original sunset is {formatted_sunset_diff} later.")
            else:
                print(f"The original sunset is {formatted_sunset_diff} earlier.")

    def print_simple_diff(
        self,
        original,
        other,
        start_message_larger,
        start_message_smaller,
        start_equals_message,
        unit="",
    ):
        if original and other:
            diff = format_to_max_one_decimal_place(abs(original - other))
            if original > other:
                print(f"{start_message_larger} {diff}{unit}.")
            elif original < other:
                print(f"{start_message_smaller} {diff}{unit}.")
            else:
                print(f"{start_equals_message} is exacly the same for both cities.")

    def print_city_facts(self):
        if self.date:
            print(
                f"Weather info fetched at {convert_unix_to_datetime_txt(self.date, '%H:%M:%S', self.timezone_in_seconds)}"
            )
        if self.temperature:
            print(f"Temperature: {self.temperature}")
        if self.pressure:
            print(f"Pressure: {self.pressure} hPa")
        if self.humidity:
            print(f"Humidity: {self.humidity}%")
        if self.visibility:
            print(f"Visibility: {self.visibility}")
        if self.probability_of_precipitation:
            print(
                f"Probability of precipitation: {self.probability_of_precipitation*100}%"
            )
        if self.snow:
            print(f"Snow volume in the last 3h: {self.snow['3h']} mm")
        if self.rain:
            print(f"Rain volume in the last 3h: {self.rain['3h']} mm")
        if self.population:
            print(f"Population: {self.population}")
        if self.timezone:
            print(f"Timezone: {self.timezone}")
        if self.sunrise:
            print(f"Sunrise: {self.sunrise}")
        if self.sunset:
            print(f"Sunset: {self.sunset}")
