
import time
import sys
import requests


print("Start Web Remote : ")

while True:
    time.sleep(1)
    inx = input("Input \"< FW | BW | RT | LT | ST >\" : ")
    url='http://192.168.200.117:8000/' \
         +inx
    print(url)
    requests.get(url)
    
