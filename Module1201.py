import requests
import json

def get_random_chuck_norris_joke():
    """
    Fetch a random Chuck Norris joke from the Chuck Norris API.
    Returns the joke text or an error message.
    """
    url = "https://api.chucknorris.io/jokes/random"

    try:
        response = requests.get(url)

        response.raise_for_status()

        joke_data = response.json()

        return joke_data['value']

    except requests.exceptions.RequestException as e:
        return f"Error fetching joke: {e}"
    except KeyError:
        return "Error: Unexpected API response format"
    except json.JSONDecodeError:
        return "Error: Invalid JSON response from API"

def main():
    """Main function to run the program."""

    joke = get_random_chuck_norris_joke()
    print(joke)

if __name__ == "__main__":
    main()