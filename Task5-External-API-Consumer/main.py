import requests
from config import API_KEY

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:
            data = response.json()

            city_name = data["name"]
            country = data["sys"]["country"]
            weather = data["weather"][0]["description"].title()
            temperature = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            print("\n========== Weather Report ==========")
            print(f"City        : {city_name}, {country}")
            print(f"Weather     : {weather}")
            print(f"Temperature : {temperature} °C")
            print(f"Feels Like  : {feels_like} °C")
            print(f"Humidity    : {humidity}%")
            print(f"Wind Speed  : {wind_speed} m/s")
            print("====================================")

        elif response.status_code == 404:
            print("City not found.")

        else:
            print("Something went wrong.")
            print(response.text)

    except requests.exceptions.RequestException:
        print("Network Error! Please check your internet connection.")


def main():
    print("========== Weather App ==========")

    city = input("Enter City Name: ")

    get_weather(city)


if __name__ == "__main__":
    main()