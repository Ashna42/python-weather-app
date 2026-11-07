import requests
weather_descriptions={
            0:"Clear sky",
            1:"Mainly clear",
            2:"Partly cloudy",
            3:"Overcast",
            45:"Fog",48:"Fog",
            51:"Drizzle",52:"Drizzle",53:"Drizzle",54:"Drizzle",55:"Drizzle",56:"Drizzle",57:"Drizzle",
            61:"Rain",62:"Rain",63:"Rain",64:"Rain",65:"Rain",66:"Rain",67:"Rain",
            71:"Snow",72:"Snow",73:"Snow",74:"Snow",75:"Snow",76:"Snow",77:"Snow",
            80:"Rain showers",81:"Rain showers",82:"Rain showers",
            85:"Snow showers",86:"Snow showers",
            95:"Thunderstorm",
            96:"Thunderstorm with hail",97:"Thunderstorm with hail",98:"Thunderstorm with hail",99:"Thunderstorm with hail"
        }
def make_request(url,params):
    try:
        response=requests.get(url,params=params,timeout=5)
        response.raise_for_status()
        return (response.json(),"success")
    except requests.exceptions.RequestException as e:
        return (None,"request_failed")
def get_coordinates(city):
    params = {
    "name": city,
    "countryCode": "IN"
}
    url="https://geocoding-api.open-meteo.com/v1/search"

    data,status=make_request(url,params)
    if status=="request_failed":
        return (None, "request_failed")
    elif status=="success":
        results=data.get("results") 
        if results:
            details={
                "name":data["results"][0]["name"],
                "state":data["results"][0]["admin1"],
                "country":data["results"][0]["country"],
                "latitude":data["results"][0]["latitude"],
                 "longitude": data["results"][0]["longitude"]
            }
            return (details, "success")
        else:
            return (None, "city_not_found")
    
def get_weather(latitude,longitude):
        params={
                "latitude":latitude,
                "longitude":longitude,
                "current":"temperature_2m,wind_speed_10m,weather_code,relative_humidity_2m,apparent_temperature"
                
        
        }
        url="https://api.open-meteo.com/v1/forecast"
        data,status=make_request(url,params)
        if status=="request_failed":
            return (None,"weather_data_unavailable")
        elif status=="success":
            current=data.get('current')
            if current:
                code=current["weather_code"]
                results={
                    "temperature":current["temperature_2m"],
                    "temperature_unit":data["current_units"]["temperature_2m"],
                    "wind_speed":current["wind_speed_10m"],
                    "wind_unit":data["current_units"]["wind_speed_10m"],
                    "humidity":current["relative_humidity_2m"],
                    "humidity_unit":data["current_units"]["relative_humidity_2m"],
                    "condition":weather_descriptions.get(code),
                    "feels_like":data["current"]["apparent_temperature"],
                    "feels_like_unit":data["current_units"]["apparent_temperature"]
                }
                return (results, "success")


city=input("Enter a city: ")
info,status = get_coordinates(city)
if status == "success":
    print("Request succeeded and city was found")
    latitude,longitude=info['latitude'], info['longitude']
    weather,status=get_weather(latitude,longitude)
    if status=="success":
        print(f"Name:{info['name']}\nCountry: {info['country']}\nState: {info['state']}\n")
        print(f"Weather in {city}\nTemperature: {weather['temperature']}{weather['temperature_unit']}\nWind: {weather['wind_speed']}{weather['wind_unit']}\nHumidity: {weather['humidity']}{weather['humidity_unit']}\nConditions: {weather['condition']}\nFeels like: {weather['feels_like']}{weather['feels_like_unit']}")
    elif status=="request_failed":
        print("Failed to get weather")
    elif status=="weather_data_unavailable":
        print("Weather data is unavailable")
elif status=="city_not_found":
    print("City not found")
elif status=="request_failed":
    print("request failed")

