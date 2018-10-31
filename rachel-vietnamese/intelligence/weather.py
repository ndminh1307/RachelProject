import pywapi

from sensecells.tts import tts

def weather(city_name, city_code):
    weather_com_result = pywapi.get_weather_from_weather_com(city_code)
    result = "Weather.com cho biết: Hôm nay trời có " + weather_com_result['current_conditions']['text'] + " và nhiệt độ vào khoảng " + weather_com_result['current_conditions']['temperature'] + " độ C tại " + city_name

    tts(result)