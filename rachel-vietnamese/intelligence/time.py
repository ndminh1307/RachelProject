from sensecells.tts import tts
from datetime import datetime

def what_time():
    tts("Bây giờ là " + datetime.strftime(datetime.now(), '%H:%M'))
