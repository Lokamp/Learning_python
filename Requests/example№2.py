import requests

response = requests.get("https://stepik.org/api/steps/1844064")
json_data = response.json()

if response:
    print("Ответ получен")
    print(json_data)
else:
    print("Что-то не удалось")
    print(json_data)
