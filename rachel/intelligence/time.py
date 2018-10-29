from sensecells.tts import tts
from datetime import datetime

def what_time():
    tts("The time is " + datetime.strftime(datetime.now(), '%H:%M'))
