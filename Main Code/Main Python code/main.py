import requests
import matplotlib.pyplot as plt

# Ask the user for their choice
print("Would you like the weather for:")
print("1. Current Location (detected automatically)")
print("2. A City You Enter")

choice = input("Enter your choice (1 or 2): ").strip()

if choice == '1':
    try:
        # Get the current location using IP
        res = requests.get('https://ipinfo.io/')
        if res.status_code == 200:
            data = res.json()
            city = data.get('city', 'Unknown')
            print(f"Detected City: {city}")
        else:
            city = "Unknown"
            print("Unable to detect current city. Please enter a city name instead.")
    except Exception as e:
        city = "Unknown"
        print(f"An error occurred while detecting location: {e}")
elif choice == '2':
    city = input("Enter the city name: ").strip()
else:
    print("Invalid choice. Exiting.")
    exit()

if city != "Unknown":
    try:
        # Fetch the schematic weather information
        url_schematic = f'https://wttr.in/{city}'
        schematic_response = requests.get(url_schematic)
        if schematic_response.status_code == 200:
            print("Schematic Weather Information:")
            print(schematic_response.text)  # Display the full schematic weather output

        # Fetch JSON data for plotting
        url_json = f'https://wttr.in/{city}?format=j1'
        json_response = requests.get(url_json)
        if json_response.status_code == 200:
            weather_data = json_response.json()

            # Extract temperatures for the graph
            days = ["Today", "Tomorrow", "Day-After Tomorrow"]
            temperatures = [
                max(int(hour['tempC']) for hour in weather_data['weather'][0]['hourly']),  # Today
                max(int(hour['tempC']) for hour in weather_data['weather'][1]['hourly']),  # Tomorrow
                max(int(hour['tempC']) for hour in weather_data['weather'][2]['hourly'])   # Day after tomorrow
            ]

            # Plot the data
            plt.plot(days, temperatures, marker='o', label='Temperature', color='blue')
            plt.title(f'Temperature Trend Over 3 Days in {city}', fontsize=14)
            plt.xlabel('Day', fontsize=12)
            plt.ylabel('Temperature (°C)', fontsize=12)
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.legend()
            plt.show()
        else:
            print("Unable to fetch weather details for the graph.")
    except Exception as e:
        print(f"An error occurred: {e}")
else:
    print("No city provided. Cannot fetch weather details.")
