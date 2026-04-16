import requests

def get_location():
    url = "http://ip-api.com/json/"
    response = requests.get(url)
    data = response.json()

    print("City:", data['city'])
    print("Country:", data['country'])

get_location()

