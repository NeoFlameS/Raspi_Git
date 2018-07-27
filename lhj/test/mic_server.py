# -*- coding: utf-8 -*-
import socketserver
import transcribe
import threading

HOST = 'localhost'
PORT = 8080
num=1


class MyTcpHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print('[%d]. [%s] 연결됨' %(num, self.client_address[0]))
        
        filename = self.request.recv(1024) # 클라이언트로 부터 파일이름을 전달받음
        filename = filename.decode() # 파일이름 이진 바이트 스트림 데이터를 일반 문자열로 변환

        with open(filename, 'wb') as f:
            try:
                while data:
                    f.write(data)
                    data = sock.request.recv(1024)
            except Exception as e:
                print(e)

        print('파일 전송종료.')
        transcribe.transcribe_file(filename)

def runServer():
    print('서버 시작')
    try:
        server = socketserver.TCPServer((HOST,PORT),MyTcpHandler)
        t=threading.Thread(target=server.serve_forever())
        t.start()
        
    except KeyboardInterrupt:
        print('서버를 종료합니다.')

runServer()
