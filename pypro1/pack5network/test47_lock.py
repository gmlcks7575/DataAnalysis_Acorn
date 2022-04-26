import threading, time
from threading import Thread, Condition

g_count = 0 # 전역역수는 자동으로 스레드의 공유자원이 됌
lock = Condition() #스레드 공유자원 접근에 제한을 강제하기의한 잠금객체

def threadCount(id, count):
    global g_count
    
    for i in range(count):
        lock.acquire() #특정 스레드가 공유자원(g_count)을 늘릴 때 다른 것은 락걸림
        print('id %s==>count:%s, g_count:%s'%(id, i, g_count))
        g_count += 1
        lock.release() #락걸린거 풀어준다
        
for i in range(1, 6):
    Thread(target = threadCount, args=(i, 5)).start()

time.sleep(1)# .join() 대신사용
   
print('최종 g_count :', g_count)
print('bye')