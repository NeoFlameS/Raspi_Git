import logging
import re
import subprocess
import sys

import vlc
import youtube_dl
import time

ydl_opts = {
    'default_search':'ytsearch1:',
    'format':'bestaudio/best',
    'noplaylist':True,
    'quiet':True
    }
vlc_instance = vlc.get_default_instance()
vlc_player = vlc_instance.media_player_new()

def play_music(name):
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            meta = ydl.extract_info(name,download=False)
            print(meta)
    except Exception:
        print("Can not Found Music")
        return
    
    if meta:
        info = meta['entries'][0]
        print("Music Founded now play")
        print(info['url'])
        vlc_player.set_media(vlc_instance.media_new(info['url']))
        """Media = vlc_instance.media_new('https://r7---sn-ab02a0nfpgxapox-bh2y.googlevideo.com/videoplayback?expire=1530627762&gir=yes&gcr=kr&fvip=2&requiressl=yes&keepalive=yes&pl=24&ipbits=0&itag=250&key=yt6&mime=audio%2Fwebm&lmt=1509073272645293&c=WEB&usequic=no&mn=sn-ab02a0nfpgxapox-bh2y%2Csn-a5meknlz&source=youtube&mm=31%2C26&fexp=23709359&ms=au%2Conr&mv=m&mt=1530606034&dur=218.521&clen=1884913&ei=UTI7W9TzNaP5qQHBl7mICQ&ip=122.35.219.29&initcwndbps=1348750&sparams=clen%2Cdur%2Cei%2Cgcr%2Cgir%2Cid%2Cinitcwndbps%2Cip%2Cipbits%2Citag%2Ckeepalive%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cpl%2Crequiressl%2Csource%2Cusequic%2Cexpire&id=o-AInSgOv3z19YfjzBQtgFpvhrbwKJ1quycNYLpQcXPHWw&signature=65682EBE4CBCBB3F73EF41424B45A1617DF84456.DC1867B38FF247CE7985BD500EF76E11F9D8A0E0&ratebypass=yes')
        Media.get_mrl()
        vlc_player.set_media(Media)"""
        vlc_player.play()
        time.sleep(100)
        
if __name__="__main__":
    play_music("Havana")