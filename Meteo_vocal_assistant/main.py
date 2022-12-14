import requests
import json

api_key = "my_api_key"
city = input("Enter the city you want the weather for: ")

try:
    response = requests.request('GET', f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric')
except requests.exceptions.RequestException as e:
    raise SystemExit(e)

if response.status_code != 200:
    print('An error occurred please try again !')
else:
    data = json.loads(response.text)

    temperature = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']

    cleared_data = f"{data['name']} - Temperature: {temperature}C - Feels like: {feels_like}C - Humidity: {humidity}% - Description: {description}"
    print (cleared_data)
