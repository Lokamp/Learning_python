import requests

URL = 'https://api.github.com/search/repositories'
PARAMS = {'q': 'language:python'}

response = requests.get(URL, params=PARAMS)
print(response.url)

items_response = response.json()['items'][0]
l_comp = [value for key, value in items_response.items() if key == 'id']

print(items_response, '**' * 10, sep='\n')
print(l_comp)
