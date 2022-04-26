# 단순 Client
from socket import *

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1',8888))
clientSock.send('안녕 반가워'.encode(encoding='UTF-8', errors='strict'))
clientSock.close()