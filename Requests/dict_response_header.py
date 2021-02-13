import requests
import json

url = 'https://yandex.ru/'

response = requests.get(url)

dict_js = dict(response.headers)

with open('file1.txt', 'w') as file:
    json.dump(dict_js, file, indent=2)

print(response.headers)
