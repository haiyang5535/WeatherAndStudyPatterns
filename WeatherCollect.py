import requests
import csv

# NWS API details
BASE_URL = "https://api.weather.gov/gridpoints/BOX/70,76/forecast"
HEADERS = {
    "User-Agent": "(myweatherapp.com, contact@myweatherapp.com)"
}

# Function to fetch weather forecast data
def fetch_weather_forecast():
    response = requests.get(BASE_URL, headers=HEADERS)
    if response.status_code == 200:
        data = response.json()
        forecast_periods = data["properties"]["periods"]
        forecast_data = []
        print("Weather forecast for the next 7 days:")
        for period in forecast_periods:
            date = period['startTime'][:10]
            temp = period['temperature']
            unit = period['temperatureUnit']
            forecast = period['shortForecast']
            print(f"Date: {date} | Temp: {temp} {unit} | Forecast: {forecast}")
            forecast_data.append([date, temp, unit, forecast])
        return forecast_data
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

# Function to save forecast data to a CSV file
def save_to_csv(forecast_data, filename="weather_forecast.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Temperature", "Unit", "Forecast"])
        writer.writerows(forecast_data)
    print(f"Forecast data saved to {filename}")

# Main script logic
def main():
    print("Fetching weather forecast...")
    forecast_data = fetch_weather_forecast()
    if forecast_data:
        save_to_csv(forecast_data)

if __name__ == "__main__":
    main()
