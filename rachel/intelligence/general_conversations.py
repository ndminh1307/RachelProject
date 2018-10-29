from sensecells.tts import tts
import random


def who_are_you():
    replies = ['I am Rachel. A smart home robot from Mechatronics BKU','Rachel, didnt I tell you before', 'My name is Rachel. I am here to help your life to become better']
    tts(random.choice(replies))

def who_am_i(name):
    replies = ['You are ' + name + ', a brilliant person. I like you', 'Your name is ' + name + '. You created me']
    tts(random.choice(replies))

def how_am_i():
    replies = ['You are so awesome. I like you', 'You are a lovely guys', 'You look like the kindest person in the world']
    tts(random.choice(replies))

def where_born():
    tts('I am created by Dang Minh from his own personal computer')

def how_are_you():
    replies = ['Im fine. Thank you!', 'Never better. Thanks']
    tts(random.choice(replies))

def can_you_hear_me():
    replies = ['Yes. I am waiting for you', 'Everything is ok. I can still hear you']
    tts(random.choice(replies))

def what_can_you_do():
    replies = ['I am a smart home robot from BK University. I can listen to you and carry out your command. I can reply when you call me, follow you, recognize everyone in your family.']
    tts(random.choice(replies))

def thank_you():
    replies = 'You are welcome'
    tts(replies)
    
def undefined():
    replies = ['I could not understand', 'I dont know what that means!', 'Can you say again? I dont know what you said']
    tts(random.choice(replies))

