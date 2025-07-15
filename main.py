# Погода через API

import requests
from PIL import Image
import io


API_KEY ='834a33a3b254afec64a1af4a1e90efe0'                 # если код не работает то зайти на сайт openweathermap.org
URL = 'https://api.openweathermap.org/data/2.5/weather'
CITY = 'Дубай'

params = {
    'q': CITY,
    'appid': API_KEY,
    'units': 'metric',
    'lang': 'ru'
}

response = requests.get(URL, params=params)
result = response.json()
# print(result)

weather = result['weather'][0]['description']
temperature = result['main']['temp']
humidity = result['main']['humidity']
wind = result['wind']['speed']
data = result['coord']
ll = f'{data['lon']},{data['lat']}'
# print(ll)


print(f'Сегодня в городе {CITY}: {weather}')
print(f'Температура: {temperature:.1f}\xB0C')
print(f'Влажность: {humidity}%')
print(f'Скорость ветра: {wind} м/с')
link = f'https://static-maps.yandex.ru/1.x/?ll={ll}&spn=0.005,0.005&l=sat&pt={ll},pm2dgl'
image = requests.get(link).content

if image:
    Image.open(io.BytesIO(image))                                           # вывести картинку на экран
    #im = Image.open(io.BytesIO(image))                                     # сохранить картинку
    #APIim.save('map.jpg')                                                  # сохранить картинку