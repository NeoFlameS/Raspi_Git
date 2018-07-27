from BaseHTTPServer \ import BaseHTTPRequestHandler,HTTPServer
from gpiozero import PWMOutputDevice
import time

state=0
num=0
pin1=23
pin2=24
pin3=17
pin4=27
fr=PWMOutputDevice(pin1,Ture,0,1000)
rr=PWMOutputDevice(pin2,Ture,0,1000)
fl=PWMOutputDevice(pin3,Ture,0,1000)
rl=PWMOutputDevice(pin4,Ture,0,1000)
x=0.5
y=0.5

def init():
    forwardRight.value=0
    forwardLeft.value=0
    reverseRight.value=0
    reverseLeft.value=0

def Forward():
    print('state : ' + state)
    print('forward')
    if state==1:
        if num <2:
            num+=1
        fr.value=x+(0.25*num)
        fl.value=y+(0.25*num)
        time.sleep(1)
        
        init()
    else:
        state=1
        num=0
        fr.value=x
        fl.value=y
        time.sleep(1)
        
        init()
def backward():
    print('state : ' + state)
    print('backward')
    if state==2:
        if num<2:
            num+=1
        rr.value=x+(0.25*num)
        rl.value=y+(0.25*num)
        time.sleep(1)
        
        init()
    else:
        state=2
        num=0
        rr.value=x
        rl.value=y
        time.sleep(1)
        
        init()
        
def RightTurn():
    state=3
    print('right turn')
    print('state' + state)
    fl.value=0.6
    time.sleep(1)
    
    init()
def LeftTurn():
    state=4
    print('left turn')
    print('state' + state)
    fr.value=0.6
    time.sleep(1)

def:
    state=0
    print('STOP')
    print('state' + state)
    
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path=='/favicon.ico':
            return
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        
        message='<a href=fw>Forward</a><br>'\
                 '<a href=bw>Backward</a><br>'\
                 '<a href=lt>LeftTurn</a><br>'\
                 '<a href=rt>RightTurn</a><br>'\
                 '<a href=stop>STOP</a><br>'
        self.wfile.write(bytes(message))
        print(selp.path)
        if self.path=='fw':
            Forward()
        elif self.path=='bw':
            Backward()
        elif self.path=='lt':
            LeftTurn()
        elif self.path=='rt':
            RightTurn()
        else:
            STOP()
        
        return

def run():
    server_addr('0,0,0,0', 8000)
    httpd=HTPServer(server_addr, MyHandler)
    print'start server')
    httpd.serve_forever()
    
run()