import requests

def get_weather_by_city(city_name, api_key):
    """Fetch current weather for a given city"""

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        weather_data = response.json()

        temp_celsius = weather_data['main']['temp']
        weather_description = weather_data['weather'][0]['description']

        return temp_celsius, weather_description

    except requests.exceptions.HTTPError as e:
        if e.response is not None:
            if e.response.status_code == 401:
                return None, "Error: Invalid API key"
            elif e.response.status_code == 404:
                return None, f"Error: City '{city_name}' not found"
        return None, f"HTTP error: {e}"

    except requests.exceptions.ConnectionError:
        return None, "Error: No internet connection"

    except requests.exceptions.Timeout:
        return None, "Error: Request timed out"

    except Exception as e:
        return None, f"Error: {e}"


def main():
    """Main function"""

    api_key = "79468e206cb5c3cb53e36e6742311131"

    print("\n" + "=" * 50)
    print("       WEATHER INFORMATION SYSTEM")
    print("=" * 50 + "\n")

    city_name = input("Please enter the city name: ").strip()

    if not city_name:
        print("\nError: Please enter a city name")
        return

    print(f"\nFetching weather for '{city_name}'...\n")

    temperature, description = get_weather_by_city(city_name, api_key)

    if temperature is not None:
        print("-" * 40)
        print(f"City: {city_name.title()}")
        print(f"Temperature: {temperature:.1f}°C")
        print(f"Conditions: {description}")
        print("-" * 40 + "\n")
    else:
        print(f"{description}\n")


if __name__ == "__main__":
    main()