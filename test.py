import requests

data = requests.get('https://instagram.com/garyvee/')
print(data.text)