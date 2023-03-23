import requests

API_key = ''

city_list = ['青岛市,CN']

# http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}


for city in city_list:
    geocoding_url = "http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_key}".format(city=city,API_key=API_key)

    r = requests.get(geocoding_url)
    print('城市：' + r.json()[0]['name'])
    lat = r.json()[0]['lat']
    lon = r.json()[0]['lon']

    weather_url = 'https://api.openweathermap.org/data/2.5/weather?units=metric&lat={lat}&lon={lon}&appid={API_key}'.format(lat=lat,lon=lon,API_key=API_key)

    r2 = requests.get(weather_url)
    print('温度： {} 摄氏度'.format(r2.json()['main']['temp']))
    print('湿度： {}%'.format(r2.json()['main']['humidity']))
