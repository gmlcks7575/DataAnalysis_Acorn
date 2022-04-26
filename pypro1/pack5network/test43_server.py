# 단순 Echo Server

from socket import *

serverSock = socket(AF_INET, SOCK_STREAM) # scoket(소켓종류, 소켓유형)
serverSock.bind(('127.0.0.1', 8888))#IP, PORT NUM 바인딩
serverSock.listen(1) #리스너 설정
print('server start')

conn, addr = serverSock.accept() #클라이언트 요청을 기다리다
print('client addr:',addr)
print('from client message:',conn.recv(1024).decode()) #리시브
conn.close()
serverSock.close() #무한루프 종료