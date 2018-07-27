# -*- coding: utf-8 -*-
#! /usr/bin/python
import socket

HOST = '0.0.0.0'
PORT = 8080

def sendFile(filename):
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.connect((HOST,PORT))
    print('서버 연결')
    sock.sendall(filename.encode('utf-8'))
    print('파일[%s] 전송 시작...' %filename)
    
    with open(filename, 'rb') as f:
        try:
            data = f.read(1024) # 파일을 1024바이트 읽음
            while data: # 파일이 빈 문자열일때까지 반복
                data = f.read(1024)
        except Exception as e:
            print(e)
    print('전송완료[%s]' %(filename))
    
    sock.close()


if __name__ == '__main__':
    sendFile(filename)
