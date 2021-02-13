import requests

URL = 'https://stepik.org/api/users/2'

response = requests.get(URL)

json_obj = response.json()

print(
    json_obj['users'][0]['first_name'],
    json_obj['users'][0]['last_name'],
    json_obj['users'][0]['created_courses_count'],
    sep='\n'
)
