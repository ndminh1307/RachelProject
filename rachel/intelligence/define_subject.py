import re
import wikipedia

from sensecells.tts import tts

def define_subject(speech_text):
    words = speech_text.split()
    words.remove('define')
    cleaned_words = ' '.join(words)

    try:
        wiki_data = wikipedia.summary(cleaned_words, sentences=5)

        regEx = re.compile(r'(^\(]*)\([^\)]*\)*(.*)')
        m = regEx.match(wiki_data)
        while m:
            wiki_data = m.group(1) + m.group(2)
            m = regEx.match(wiki_data)

        wiki_data = wiki_data.replace("'","")
        tts(wiki_data)
    except wikipedia.exceptions.DisambiguationError as e:
        tts('Can you please be more specific? You may choose something from the following.; {0}'.format(e))
        

