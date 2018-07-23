from BaseHTTPServer \
	import BaseHTTPRequestHandler,HTTPServer
from gpiozero import PWMOutputDevice
import time

pin1 = 23
pin2 = 24

pin3 = 17
pin4 = 27

forwardRight=PWMOutputDevice(pin1, True, 0, 1000)
reverseRight=PWMOutputDevice(pin2, True, 0, 1000)

forwardLeft=PWMOutputDevice(pin3, True, 0, 1000)
reverseLeft=PWMOutputDevice(pin4, True, 0, 1000)

state=0
num = 0

state_dict={"Forward":[0.5,0.5,0,0,1,0],
            "Backward":[0,0,0.5,0.5,0,1],
            "RightTurn":[0.5,0,0,0,0,0],
            "LeftTurn":[0,0.5,0,0,0,0],
            "Stop":[0,0,0,0,0,0]
            }

def Move(status):#,fr,fl,rer,rel,Fo,Bw): 
    global num,state_dict
    fr,fl,rer,rel,Fo,Bw = state_dict[status]
    print(status)
    forwardRight.value=fr+(a*0.25*num)
    reverseRight.value=rer+(a*0.25*num)
    forwardLeft.value=fl+(a*0.25*num)
    reverseLeft.value=rel+(a*0.25*num)
    time.sleep(1)
    
    
def State_Change(stat):
    global state
    if state == stat:
        num+=1
    else:
        num=0
        state=stat
    
class MyHandler(BaseHTTPRequestHandler):
	def do_GET(self):
            if self.path =='favicon.ico': return
            self.send_response(200)
            self.send_header('Content-type','texthtml')
            self.end_headers()
            
            message= '<a href=/FW>Forward</a><br>'\
                     '<a href=/BW>Backward</a><br>'\
                     '<a href=/LT>LeftTurn</a><br>'\
                     '<a href=/RT>RightTurn</a><br>'\
                     '<a href=/ST>STOP</a>'
            self.wfile.write(bytes(message))
            print(self.path)
            if self.path=='/FW':
                State_Change(1)
                Move("Forward")#,0.5,0.5,0,0,1,0)
                Move("Pasue")#,0,0,0,0,0,0)
            elif self.path=='/BW':
                State_Change(2)
                Move("BackWard")#,0,0,0.5,0.5,0,1)
                Move("Pasue")#,0,0,0,0,0,0)
            elif self.path=='/LT':
                State_Change(3)
                Move("LeftTurn")#,0,0.5,0,0,0,0)
                Move("Pasue")#,0,0,0,0,0,0)
            elif self.path=='/RT':
                State_Change(4)
                Move("RightTurn")#,0.5,0,0,0,0,0)
                Move("Pasue")#,0,0,0,0,0,0)
            elif self.path=='/ST':
                State_Change(0)
                Move("Stop")#,0,0,0,0,0,0)
            
            return
def run():
	server_addr=('0.0.0.0', 8000)
	httpd=HTTPServer(server_addr, MyHandler)
	print('starting web server...')
	httpd.serve_forever()
	
run()

