import pywapi

from sensecells.tts import tts

def weather(city_name, city_code):
    weather_com_result = pywapi.get_weather_from_weather_com(city_code)
    result = "Weather.com says: It is " + weather_com_result['current_conditions']['text'] + " and temperature is about " + weather_com_result['current_conditions']['temperature'] + " in " + city_name + " city."

    tts(result)