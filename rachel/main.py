import speech_recognition as sr
import yaml

from intelligence.sensecells.tts import tts
from brain import brain

with open("profile.yaml.default", "r") as profile:
    data = yaml.safe_load(profile)
    profile.close()

#Personal data
name = data['name']
city_name = data['city_name']
city_code = data['city_code']


tts('My name is Rachel. Can I help you?')

def main():
    
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, phrase_time_limit=10)

    try:
        speech_text = r.recognize_google(audio).lower().replace("'","")
        print("You said: " + speech_text.capitalize())

    except sr.UnknownValueError:
        tts("No voice detected. Can you say again?")
    
    except sr.RequestError:
        tts("No request")
    
    try:
        brain(speech_text, name, city_name, city_code)
    except UnboundLocalError:
        pass
    
while True:
    main()
