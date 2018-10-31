from gtts import gTTS
from mutagen.mp3 import MP3
from subprocess import Popen, PIPE

import os
import time

def tts(speech_text):

    print("MINH TUỆ: " + speech_text)
    
    language = 'vi'
    voice = gTTS(text=speech_text, lang=language, slow=False)
    voice.save("temp.mp3")

    audio = MP3("temp.mp3")
    audio_length = audio.info.length

    Popen(['play', 'temp.mp3'], stdout=PIPE, stderr=PIPE)
    time.sleep(audio_length + 0.25)
    
    os.system("rm -f temp.mp3")