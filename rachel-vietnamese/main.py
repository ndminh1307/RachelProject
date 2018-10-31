import speech_recognition as sr
import yaml
import sys

from intelligence.sensecells.tts import tts
from brain import brain

with open("profile.yaml.default", "r") as profile:
    data = yaml.safe_load(profile)
    profile.close()

#Personal data
name = data['name']
city_name = data['city_name']
city_code = data['city_code']
music_path = data['music_path']


def main():
    
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, phrase_time_limit=7)

    try:
        speech_text = r.recognize_google(audio, language='vi-VN').lower().replace("'","")
        print("BẠN NÓI: " + speech_text.capitalize())

    except sr.UnknownValueError:
        tts("Không nhận được giọng nói. Bạn đã nói chưa?")
    
    except sr.RequestError:
        tts("Không phản hồi")
    
    try:
        brain(speech_text, name, city_name, city_code, music_path)
    except UnboundLocalError:
        pass

main()
