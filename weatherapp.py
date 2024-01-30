import requests
import json
from urllib.request import urlopen
 
url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)
 
MY_CITY = data['city']
print(data['city'])
 
# Enter your API key here
api_key = "63301fc60836eeeabd987a157522aa15"
 

base_url = "http://api.openweathermap.org/data/2.5/weather?"


city_name = MY_CITY 
 

complete_url = base_url + "appid=" + api_key + "&q=" + city_name
 
location = [float(coord) for coord in data['loc'].split(',')]
lat = location[0]
lng = location[1]
units = 'metric'
complete_url = f"https://api.openweathermap.org/data/2.5/weather?&units={units}&lat={lat}&lon={lng}&appid={api_key}"
# print(complete_url)
# get method of requests module
# return response object
response = requests.get(complete_url)
 
# json method of response object
# convert json format data into
# python format data
x = response.json()
 
# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
if x["cod"] != "404":
 
    # store the value of "main"
    # key in variable y
    y = x["main"]
 
    # store the value corresponding
    # to the "temp" key of y
    current_temperature = y["temp"]
 
    # store the value corresponding
    # to the "pressure" key of y
    current_pressure = y["pressure"]
 
    # store the value corresponding
    # to the "humidity" key of y
    current_humidity = y["humidity"]
 
    # store the value of "weather"
    # key in variable z
    z = x["weather"]
 
    # store the value corresponding
    # to the "description" key at
    # the 0th index of z
    weather_description = z[0]["description"]
 
    # print following values
    print(" Temperature (in celcius unit) = " +
                    str(current_temperature) +
          "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\n humidity (in percentage) = " +
                    str(current_humidity) +
          "\n description = " +
                    str(weather_description))
 
else:
    print(" City Not Found ")