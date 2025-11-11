import requests
from datetime import datetime

def get_weather_data(latitude, longitude, location_name):
    """
    Fetch current weather data for a given location.

    Args:
        latitude (float): Latitude of the location
        longitude (float): Longitude of the location
        location_name (str): Name of the location for display
    """
    # Open-Meteo API endpoint
    url = "https://api.open-meteo.com/v1/forecast"

    # Parameters for current weather
    params = {
        'latitude': latitude,
        'longitude': longitude,
        'current': 'temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code',
        'temperature_unit': 'celsius',
        'wind_speed_unit': 'kmh'
    }

    print(f"\nFetching weather data for {location_name}...")
    print("-" * 50)

    try:
        # Make the GET request
        response = requests.get(url, params=params, timeout=10)

        # Check if request was successful
        response.raise_for_status()  # Raises HTTPError for bad status codes

        # Parse JSON response
        data = response.json()

        # Extract current weather data
        current = data['current']

        print(f"Location: {location_name}")
        print(f"Coordinates: {latitude}°N, {longitude}°E")
        print(f"Time: {current['time']}")
        print(f"Temperature: {current['temperature_2m']}°C")
        print(f"Humidity: {current['relative_humidity_2m']}%")
        print(f"Wind Speed: {current['wind_speed_10m']} km/h")
        print(f"Weather Code: {current['weather_code']}")

        return data

    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please try again.")
        return None
    except requests.exceptions.ConnectionError:
        print("Error: Failed to connect to the API. Check your internet connection.")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"Error: HTTP error occurred: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error: An error occurred: {e}")
        return None
    except KeyError as e:
        print(f"Error: Unexpected response format. Missing key: {e}")
        return None


def get_forecast(latitude, longitude, location_name, days=3):
    """
    Fetch weather forecast for the next few days.

    Args:
        latitude (float): Latitude of the location
        longitude (float): Longitude of the location
        location_name (str): Name of the location for display
        days (int): Number of days to forecast
    """
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        'latitude': latitude,
        'longitude': longitude,
        'daily': 'temperature_2m_max,temperature_2m_min,precipitation_sum',
        'temperature_unit': 'celsius',
        'forecast_days': days
    }

    print(f"\nFetching {days}-day forecast for {location_name}...")
    print("-" * 50)

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()
        daily = data['daily']

        print(f"\n{days}-Day Forecast for {location_name}:\n")
        for i in range(len(daily['time'])):
            print(f"Date: {daily['time'][i]}")
            print(f"  Max Temp: {daily['temperature_2m_max'][i]}°C")
            print(f"  Min Temp: {daily['temperature_2m_min'][i]}°C")
            print(f"  Precipitation: {daily['precipitation_sum'][i]} mm")
            print()

        return data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching forecast: {e}")
        return None


def main():
    """Main function to demonstrate the weather API usage."""
    print("=" * 60)
    print("WEATHER API EXAMPLE - Open-Meteo")
    print("=" * 60)

    # Example locations (latitude, longitude, name)
    locations = [
        (40.7128, -74.0060, "New York City, USA"),
        (51.5074, -0.1278, "London, UK"),
        (35.6762, 139.6503, "Tokyo, Japan")
    ]

    # Get current weather for each location
    for lat, lon, name in locations:
        get_weather_data(lat, lon, name)

    # Get detailed forecast for one location
    print("\n" + "=" * 60)
    get_forecast(40.7128, -74.0060, "New York City, USA", days=5)

    print("=" * 60)
    print("Weather API Demo Complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
