"""
Переделать программу с погодой так что бы она 
запрашивала город а в ответ выдавала подробную информацию 
о погоде в этом городе в красивом формате.
"""

from pyowm import OWM
from pprint import pprint

owm = OWM('3b7520cfa14d8220f49bed37a19a7b4d')
mgr = owm.weather_manager()

city_input = input('Введите город: ')

weather = mgr.weather_at_place(city_input).weather
mydict = mgr.weather_at_place(city_input).to_dict()
wind = weather.wind()
temp = weather.temperature('celsius')
humidity = weather.humidity
rain = weather.rain
clouds = weather.clouds
status = weather.status
pprint(mydict)
print(f"ПОГОДА В ГОРОДЕ: {city_input.upper()}")
print(f"       Наблюдаем :{status}")
print(f"🌡️    Температура:{temp['temp']}°C")
print(f"       Ощущается как: {temp['feels_like']}°C")
print(f"       Минимум: {temp['temp_min']}°C")
print(f"       Максимум: {temp['temp_max']}°C")
    
print(f"💧   Влажность:{humidity}%")
print(f"🌪️    Ветер:{wind['speed']} м/с")
print(f"💭    Облачность:{clouds} ")
if rain and len(rain) > 0:
    print(f"🌧️  Дождь: {rain} мм/час")
else:
     print("🌤️  Дождь: без осадков")
