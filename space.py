# Note you need to run 'pip install requests' to use the requests module
import requests

response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()
print(json)

print('The people currently in space are:ve')
for person in json['people']:
    print(person['name'])



