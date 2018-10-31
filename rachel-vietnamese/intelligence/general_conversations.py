from sensecells.tts import tts
import random


def who_are_you():
    replies = ['Tôi tên là Minh Tuệ. Tôi là robot thông minh đến từ khoa Cơ khí, Đại học Bách Khoa.', 'Tôi là Minh Tuệ. Tôi ở đây để giúp bạn mọi thứ']
    tts(random.choice(replies))

def who_am_i(name):
    replies = ['Bạn là ' + name + ', một người rất tốt bụng và dễ thương. Tôi rất thích bạn. I like you', 'Tên của bạn là ' + name + '. Bạn đã tạo ra Minh Tuệ']
    tts(random.choice(replies))

def how_am_i():
    replies = ['Trông bạn rất ngầu như trái bầu. Tôi rất thích bạn.', 'Bạn trông rất đáng yêu', 'Bạn là người tốt nhất thế gian. Tôi yêu bạn mất rồi']
    tts(random.choice(replies))

def where_born():
    tts('Tôi được tạo ra bởi Đăng Minh, sinh viên năm thứ 5 của Đại học Bách Khoa thành phố Hồ Chí Minh')

def how_are_you():
    replies = ['Tôi rất ổn. Cảm ơn!', 'Chưa bao giờ tốt hơn thế này. Cảm ơn bạn rất nhiều']
    tts(random.choice(replies))

def can_you_hear_me():
    replies = ['Vâng, tôi đang chờ bạn nói', 'Mọi thứ rất ổn. Tôi vẫn đang nghe']
    tts(random.choice(replies))

def what_can_you_do():
    replies = ['Tôi là robot thông minh cho gia đình đến từ bộ môn Cơ Điện tử trường Đại học Bách Khoa Hồ Chí Minh. Tôi ở đây để trò chuyện với bạn. Tôi có thể thực hiện một số lệnh từ bạn. Tôi có khả năng nhận diện các thành viên trong gia đình bạn.']
    tts(random.choice(replies))

def thank_you():
    replies = ['Không có chi. Đó là nhiệm vụ của tôi', 'Rất vui được phục vụ bạn']
    tts(random.choice(replies))

def compliment():
    replies = ['Cám ơn', 'Lời khen làm tôi ngại quá! Cám ơn']
    tts(random.choice(replies))

def undefined():
    replies = ['Tôi chưa hiểu những gì bạn nói', 'Bạn có thể nói lại lần nữa không? Tôi vẫn chưa hiểu']
    tts(random.choice(replies))

