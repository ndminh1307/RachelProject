from intelligence import general_conversations, time, weather, define_subject, sleep

def brain(speech_text, name, city_name, city_code):
    def check(keywords):
        words = set(speech_text.split())
        if set(keywords).issubset(words):
            return True
        else:
            return False

    #General Conversation logic engine
    if check(['who', 'are', 'you']):
        general_conversations.who_are_you()
    
    elif check(['who','am','i']):
        general_conversations.who_am_i(name)
    
    elif check(['how', 'are', 'you']):
        general_conversations.how_are_you()
    
    elif check(['how','i','look']):
        general_conversations.how_am_i()
    
    elif check(['where','born','you']):
        general_conversations.where_born()
    
    elif check(['can','you','hear']):
        general_conversations.can_you_hear_me()

    elif check(['what','can','you','do']):
        general_conversations.what_can_you_do()
    
    elif check(['thank','you'] or ['thanks']):
        general_conversations.thank_you()
    
    #Tell me the time
    elif check(['what','time']):
        time.what_time()
    
    #Tell weather in city
    elif check(['weather']):
        weather.weather(city_name, city_code)
        
    #Define subject from wikipedia
    elif check(['define']):
        define_subject.define_subject(speech_text)

    #Sleep mode
    elif check(['sleep']):
        sleep.go_to_sleep()
    
    else:
        general_conversations.undefined()
