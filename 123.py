import requests
import json

print(requests.get("http://spb.hh.ru/"))
print(requests.get('http://www.kinopoisk.ru/'))

# Задание 2

city_name = input('Enter city name: ')
id_key = '9624f063104d99a703ba671897a047b2'
url_weather = 'http://api.openweathermap.org/data/2.5/weather?'

url_new = url_weather + 'appid=' + id_key + '&q=' + city_name
resp_weather = requests.get(url_new)
response_weather = resp_weather.json()

if resp_weather.status_code != 404:
    main_response_weather = response_weather['main']

    temperature = round(main_response_weather['temp'] -273,15 )
    pressure = main_response_weather['pressure']
    humidity = main_response_weather ['humidity']
    weather_response = response_weather['weather']
    weather_description = weather_response[0]['description']

    print (f'Temperature:  {temperature} °C')
    print (f'Atmospheric pressure:  {pressure} hPa')
    print (f'Humidity:  {humidity} %')
    print(f'Description:  {weather_description}')

else:
    print('City not found')
print('\n')

'''
# Задание 3
def getAreas():
    req = requests.get('https://api.hh.ru/areas')
    data = req.content.decode()
    req.close()
    jsObj = json.loads(data)
    areas = []
    for k in jsObj:
        for i in range(len(k['areas'])):
            if len(k['areas'][i]['areas']) != 0:                      # Если у зоны есть внутренние зоны
                for j in range(len(k['areas'][i]['areas'])):
                    areas.append([k['id'],
                                  k['name'],
                                  k['areas'][i]['areas'][j]['id'],
                                  k['areas'][i]['areas'][j]['name']])
            else:                                                                # Если у зоны нет внутренних зон
                areas.append([k['id'],
                              k['name'],
                              k['areas'][i]['id'],
                              k['areas'][i]['name']])
    return areas

areas = getAreas()
print(areas)
'''
