from picamera import PiCamera
from time import sleep
import time

def camera():
    c=PiCamera()
    c.rotation=0
    try:
        now=time.localtime()
        t="%02d-%02d %02d:%02d:%02d" % (now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
        c.start_preview()
        sleep(3)
        c.capture("image/"+t+".jpg")
        c.stop_preview()
    except KeyboardInterrupt:
        pass
    finally:
        c.stop_preview()