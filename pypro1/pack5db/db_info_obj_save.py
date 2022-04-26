#DB 연결 정보를 객체로 저장ㅇ
import pickle

config = { #dict type 사용
    'host':'127.0.0.1',
    'user':'root',
    'password':'',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

with open(file= 'mydb.dat', mode='wb') as obj:
    pickle.dump(config,obj)
    