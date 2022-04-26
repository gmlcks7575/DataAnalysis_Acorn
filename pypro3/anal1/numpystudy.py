
import numpy as np

print('--- 조건연산 where(조건, 참, 거짓)---')
x = np.array([1,2,3])
y = np.array([4,5,6])
print()
kbs = np.concatenate([x,y])
print(kbs) #배열 결합
v1, v2 = np.split(kbs, 2) #배열 분할
print(v1)
print(v2)
print()
a = np.arange(1, 17).reshape(4,4)
print(a)
x1, x2 = np.hsplit(a, 2) #좌우 분리
print(x1)
print(x2)

print()
x1, x2 = np.vsplit(a, 2) #상하 분리
print(x1)
print(x2)

# 복원 / 비복원 추출
li = np.array([1,2,3,4,5,6,7])

# 복원 추출
for _ in range(5):
    print(li[np.random.randint(0,len(li) - 1)], end = ' ')

print()
# 비복원 추출
import random
print(random.sample(list(li), k=5))
print(random.sample(range(1, 46), k=6))

print()
print(list(np.random.choice(range(1,46),6))) #비복원
print(list(np.random.choice(range(1,46),6, replace=True))) #복원

print()
arr = 'air book cat d e f god'
arr = arr.split(' ')
print(arr)
print(np.random.choice(arr, 3, p=[0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.4])) #p= 확률값을 부여