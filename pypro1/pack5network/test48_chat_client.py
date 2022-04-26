# 멀티 채팅 클라이언트 : socket, thread
import socket
import threading
import sys

def handle(socket):
    while True:
        data = socket.recv(1024)
        if not data: continue #넘어오는 데이터가 없으면 찍지않는다.
        print(data.decode('UTF_8'))
        
sys.stdout.flush()  #파이썬의 표준 출력은 버퍼링이 된다 #버퍼를 깨끗하게 지워주는 작업

name = input('채팅명 입력 :')
cs = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cs.connect(('127.0.0.1',5555))
cs.send(name.encode('UTF_8'))

th = threading.Thread(target=handle, args=(cs,)) 
th.start()

while True:
    msg = input() #채팅 메시지를 입력
    sys.stdout.flush()
    if not msg:continue #메세지 입력x > send x
    cs.send(msg.encode('UTF_8'))

cs.close()