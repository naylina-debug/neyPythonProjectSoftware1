import requests

def kelvin_to_celsius(kelvin_temp):
    """
    Convert Kelvin temperature to Celsius
    Formula: Celsius = Kelvin - 273.15
    """
    return kelvin_temp - 273.15

def get_weather_by_city(city_name, api_key):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

    try:

        response = requests.get(url)

        response.raise_for_status()

        weather_data = response.json()

        temp_kelvin = weather_data['main']['temp']

        temp_celsius = kelvin_to_celsius(temp_kelvin)

        weather_description = weather_data['weather'][0]['description']

        return temp_celsius, weather_description

    except requests.exceptions.HTTPError as e:

        if response.status_code == 401:
            return None, "Error: Invalid API key. Please check your API key."
        elif response.status_code == 404:
            return None, f"Error: City '{city_name}' not found. Please check the city name."
        else:
            return None, f"HTTP error occurred: {e}"

    except requests.exceptions.ConnectionError:
        return None, "Error: No internet connection. Please check your network."

    except requests.exceptions.Timeout:
        return None, "Error: Request timed out. Please try again."

    except Exception as e:
        return None, f"An unexpected error occurred: {e}"


def main():
    """Main function to run the program"""

    API_KEY = "79468311131"

    print("\n" + "=" * 50)
    print("       WEATHER INFORMATION SYSTEM")
    print("=" * 50 + "\n")

    city_name = input("Please enter the city name: ").strip()

    if not city_name:
        print("\nError: Please enter a city name.")
        return

    print(f"\nFetching weather for '{city_name}'...\n")

    temperature, description = get_weather_by_city(city_name, API_KEY)

    if temperature is not None:
        print("-" * 40)
        print(f"City: {city_name.title()}")
        print(f"Temperature: {temperature:.1f}°C")
        print(f"Conditions: {description}")
        print("-" * 40 + "\n")
    else:
        print(f" {description}\n")


if __name__ == "__main__":
    main()