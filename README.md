# Weather Game
Welcome to Weather Game, a command-line game where you'll put your weather knowledge to the test! Can you guess the city based on the provided weather facts?

## Table of Contents
- [Overview](#overview)
- [How to Play](#how-to-play)
- [API Integration](#api-integration)
- [How to Run](#how-to-run)
- [How to get API key](#how-to-get-api-key)

## Overview <a name="overview"></a>
In Weather Game, you'll be presented with various weather-related facts about a specific city. Your challenge is to guess which city the facts are describing. Use your intuition, weather knowledge, and deductive skills to make the correct guess!

## How to Play <a name="how-to-play"></a>
1. Run the game in your command line interface.
2. Read the provided weather facts carefully.
3. Make your guess by typing in the name of the city you think matches the facts.
4. See whether your guess is correct. If it's incorrect, find out how close you were to the correct answer!

## API Integration <a name="api-integration"></a>
Weather Game integrates with the OpenWeatherMap API to provide accurate and up-to-date weather data. I utilize the [5 Day / 3 Hour Forecast](https://openweathermap.org/forecast5) endpoint for detailed weather information and the [Geocoding API](https://openweathermap.org/api/geocoding-api) to convert coordinates to city names.

## How to Run <a name="how-to-run"></a>
To run Weather Game on your local machine:

1. Clone this repository to your computer.
2. Create api_key.py file and add your Open Weather Map API key as API_KEY field.
3. Run the game script by executing python game.py.

## How to get API key <a name="how-to-get-api-key"></a>
Check 'How to call OpenWeather APIs with a freemium plan' section on the [Open Weather Map](https://openweathermap.org/appid) site to get your free API key.
