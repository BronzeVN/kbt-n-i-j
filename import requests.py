import requests

def get_weather(aadca78afb69a52bc4aeef924f9319e49, HaiDuong):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={HaiDuong}&appid={apiadca78afb69a52bc4aeef924f9319e49}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def main():
    api_key = "adca78afb69a52bc4aeef924f9319e49"  # Replace with your API key
    city = input("Enter city name: ")
    weather_data = get_weather(adca78afb69a52bc4aeef924f9319e49, HaiDuong)
    
    if weather_data["cod"] == 200:
        print(f"Weather in {city}:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Description: {weather_data['weather'][0]['description']}")
    else:
        print("City not found.")

if __name__ == "__main__":
    main()