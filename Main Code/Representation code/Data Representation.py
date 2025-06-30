import requests

print("Would you like the weather for:")
print("1. Current Location (detected automatically)")
print("2. A City You Enter")

choice = input("Enter your choice (1 or 2): ").strip()

if choice == '1':
    try:
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
    url = f'https://wttr.in/{city}'
    try:
        res = requests.get(url)
        if res.status_code == 200:
            print("Weather Information:")
            print(res.text)
        else:
            print("Unable to fetch weather details. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")
else:
    print("No city provided. Cannot fetch weather details.")
