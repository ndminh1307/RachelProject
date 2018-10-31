import sys
import os
import random

from subprocess import Popen, PIPE
from sensecells.tts import tts

def mp3gen(music_path):
    music_list = []
    for root, dirs, files in os.walk(music_path):
        for filename in files:
            if os.path.splitext(filename)[1]==".mp3":
                music_list.append(os.path.join(root, filename))
    return music_list

def play_random(music_path):
    try:
        music_list = mp3gen(music_path)
        music_playing = random.choice(music_list)
        music_filename = music_playing.replace("/home/ndminh/Music/", "")
        music_filename = music_filename.replace(".mp3","")
        
        music_filename_lst = music_filename.split("-")
        music_filename = ' '.join(music_filename_lst)
        
        tts("Now playing: " + music_filename)
        Popen(['play', music_playing], stdout=PIPE, stderr=PIPE)
    except IndexError:
        tts("Music files not found")

def stop_playing():
        os.system("pkill -f play")