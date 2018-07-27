import RPi.GPIO as GPIO
import time

BUZZ=18
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZ, GPIO.OUT)

def buzz(pitch, beats):
    period = 1.0/pitch
    cycles=int(pitch*beats)
    for i in range(cycles):
        GPIO.output(BUZZ, True)
        time.sleep(period/1.0)
        GPIO.output(BUZZ, False)
        time.sleep(period/2.0)
        
        
tone=[261,294,330,349,392,440,494,523]
buzz(tone[4],.5)
buzz(tone[4],.5)
buzz(tone[5],.5)
buzz(tone[5],.5)
buzz(tone[4],.5)
buzz(tone[4],.5)
buzz(tone[2],1)
buzz(tone[4],.5)
buzz(tone[4],.5)
buzz(tone[2],.5)
buzz(tone[2],.5)
buzz(tone[1],1)