from intelligence import general_conversations, time, weather, define_subject, sleep, troll

def brain(speech_text, name, city_name, city_code):
    def check(keywords):
        words = set(speech_text.split())
        if set(keywords).issubset(words):
            return True
        else:
            return False

    #General Conversation logic engine
    if check(['bạn', 'là', 'ai']):
        general_conversations.who_are_you()
    
    elif check(['tôi', 'là', 'ai']):
        general_conversations.who_am_i(name)
    
    elif check(['bạn', 'khỏe', 'không']) or check(['bạn', 'thế', 'nào']):
        general_conversations.how_are_you()
    
    elif check(['trông', 'tôi']):
        general_conversations.how_am_i()
    
    elif check(['bạn', 'sinh']):
        general_conversations.where_born()
    
    elif check(['nghe', 'tôi', 'không']):
        general_conversations.can_you_hear_me()

    elif check(['bạn', 'có', 'thể', 'làm']):
        general_conversations.what_can_you_do()
    
    elif check(['cám', 'ơn']) or check(['cảm', 'ơn']):
        general_conversations.thank_you()

    elif check(['bạn', 'đẹp']) or check(['bạn', 'xinh']) or check(['bạn', 'thông', 'minh']) or check(['bạn', 'tốt']):
        general_conversations.compliment()
    
    #Troll
    elif check(['toàn']):
        troll.toan()
    
    elif check(['tính']):
        troll.tinh()

    elif check(['khương']):
        troll.khuong()
        
    #Tell me the time
    elif check(['mấy', 'giờ']):
        time.what_time()
    
    #Tell weather in city
    elif check(['thời', 'tiết']) or check(['nhiệt', 'độ']):
        weather.weather(city_name, city_code)
        
    #Define subject from wikipedia
    elif check(['định', 'nghĩa']):
        define_subject.define_subject(speech_text)

    #Sleep mode
    elif check(['tạm', 'biệt']):
        sleep.go_to_sleep()
    
    else:
        general_conversations.undefined()
