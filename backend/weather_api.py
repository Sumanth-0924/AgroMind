import requests

API_KEY = "2106d9b400a3213cf2b1d3e248dfae9d"

def get_weather(city):

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={"2106d9b400a3213cf2b1d3e248dfae9d"}&units=metric"

    response = requests.get(url)
    data = response.json()

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]

    # rainfall may not always exist
    rainfall = data.get("rain", {}).get("1h", 0)

    return temperature, humidity, rainfall