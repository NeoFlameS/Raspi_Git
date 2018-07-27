import logging
import re
import subprocess
import sys

import vlc
import youtube_dl
import time


class MusicPlayer:
    
    
    def __init__(self):
        self.ydl_opts={'default_search':'ytsearch1:','format':'bestaudio/best','noplaylist':True,'quiet':True}
        self.vlc_instance = vlc.get_default_instance()
        self.vlc_player = self.vlc_instance.media_player_new()
        
    def play(self,name):
        try:
            with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
                meta = ydl.extract_info(name,download=False)
        except Exception:
            print("Can not Found Music Try another")
            return
        
        if meta:
            info = meta['entries'][0]
            print("Music Founded now play")
            self.vlc_player.set_media(self.vlc_instance.media_new(info['url']))
            self.vlc_player.play()
            
            
    def stop_now(self):
        self.vlc_player.stop()

def test_main():
    player = MusicPlayer()
    a=input("What do you want to play music : ")
    player.play(a)
    a=input("Press Char + Enter to Stop : ")
    print(a)
    player.stop_now()
    
if __name__ == '__main__':
    test_main()