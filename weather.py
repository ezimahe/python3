# import requests

# url = 'http://api.weatherapi.com/v1/current.json?key=a6a12d0f4bd041d987c200624240904&q=Maryland, US&aqi=no'

# response = requests.get(url)
# weather_json = response.json()

# temp = weather_json.get('current').get('temp_f')
# description = weather_json.get('current').get('condition').get('text')

# print("Today's weather in Maryland, USA is", description, 'and', temp, 'degrees.')

#----------------------------------------

import requests

city = str(input('What city would you like a weather report for?\n'))
url = 'http://api.weatherapi.com/v1/current.json?key=a6a12d0f4bd041d987c200624240904&q='+city+'&aqi=no'
response = requests.get(url)
weather_json = response.json()

temp = weather_json.get('current').get('temp_f')
description = weather_json.get('current').get('condition').get('text')

print("Today's weather in", city, 'is', description, 'and', temp, 'degrees.')