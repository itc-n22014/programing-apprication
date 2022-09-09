import requests
import json

url = 'https://api.chucknorris.io/jokes/random'
res = requests.get(url)
res_json = res.json()
yp = res.json()["value"]
yo = f'https://script.google.com/macros/s/AKfycbwMFaS2o-wXUtbgLaiUyYyf7GxFKVQwIoypzR31UmOG7uhw-zwkzmetseA7jTWopf8A/exec?text="{yp}"&source=en&target=ja'

yo = requests.get(yo)
yo = json.loads(yo.content)
print(yo['text'])
print(yp)
