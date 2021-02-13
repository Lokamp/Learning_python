import requests

app_id = "b6159862"
app_key = "795624631bffb219a056d778ea595375"
language = "en-gb"
word_id = "hell-bent"


url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id
r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})


if r.status_code == 200:
    print("Ответ получен")
    print(r.text)
else:
    print("Что-то не удалось")
    print(r.text)

print(dir(requests))
print(dir(r))
