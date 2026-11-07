
# Python Weather App 🌤️

A command-line weather application built using Python and the Open-Meteo API. It retrieves current weather information for Indian cities using their geographical coordinates.

## Features

- Search for cities in India by name.
- Retrieve geographical coordinates using the Open-Meteo Geocoding API.
- Fetch current weather information using the Open-Meteo Forecast API.
- Display temperature and feels-like temperature.
- Display humidity and wind speed.
- Show weather conditions using WMO weather codes.
- Handle invalid city names and API request failures.

## Technologies Used

- Python
- Requests Library
- REST APIs
- JSON

## APIs Used

This project uses the following Open-Meteo APIs:

1. **Geocoding API** – Finds the geographical coordinates of a city.
2. **Forecast API** – Retrieves current weather information using latitude and longitude.

API documentation:
- https://open-meteo.com/en/docs/geocoding-api
- https://open-meteo.com/en/docs

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project folder

```bash
cd python-weather-app
```

### 3. Install the required library

```bash
pip install requests
```

### 4. Run the application

```bash
python main.py
```

### 5. Enter a city name

Enter an Indian city name when prompted to view its current weather information.

## Sample Output

```text
Enter a city in India: Kochi

--- Current Weather Report ---
City: Kochi
State: Kerala
Country: India
Temperature: 29.0 °C
Feels like: 33.0 °C
Weather: Partly cloudy
Humidity: 75%
Wind speed: 12.0 km/h
```

*Sample values are illustrative; actual weather data changes.*

## Python Concepts Practiced

- Functions and modular programming
- Dictionaries and JSON handling
- HTTP requests and API integration
- Exception handling
- Conditional statements
- Working with external data

## Data Source

Weather information is provided by [Open-Meteo](https://open-meteo.com/).

## License

This project is available for learning and educational purposes.
