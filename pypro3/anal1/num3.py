# 배열 연산

import numpy as np

x = np.array([[1,2],[3,4]], dtype=np.float64)
print(x, x.dtype)
y = np.arange(5, 9).reshape((2,2)) #int타입
y = y.astype(np.float64) #형변환 #float타입
print(y, y.dtype)

print()
print(x + y)
print(np.add(x, y))

print()
print(x - y)
print(np.subtract(x, y))

print()
print(x * y)
print(np.multiply(x, y))

print()
print(x / y)
print(np.divide(x, y))

print()
v = np.array([9, 10]) #1차원
w = np.array([11,12])
print(v * w) #[99 120]
print()
print(v.dot(w)) # 벡터 내적 연산 v[0] * w[0] + v[1] * w[1] = 219
print(np.dot(v, w)) # R에선 v %*% w

print(x.dot(v)) # x[0,0] * v[0] + x[0,1] * v[1] = 29 x[1,0] * v[0] + x[1,1] * v[1]
print(np.dot(x, v))

print(x.dot(y))
print(np.dot(x, y)) #2차원과 2차원은 2차원의 결과가 나온다.

print()
print(x)
print(np.sum(x)) # 10
print(np.sum(x,axis=0)) #axis = 0은 칼럼에 대한 합계
print(np.sum(x,axis=1)) #axis=  1은 행에 대한 합
print(np.argmax(x), np.argmin(x)) #max를 많이쓴다 #가장 큰 값과 가장 작은 값의 인덱스 리턴

print()
print(x)
print(x.T) #전치
print(x.transpose())
print(x.swapaxes(0,1))

print()
# Broadcasting 연산 : 크기가 다른 배열간 연산을 하면 작은 배열이 큰 배열의 크기에 자동으로 맞추어 연산
x = np.arange(1,10).reshape(3,3) #2차원
print(x)
y = np.array([1,2,3]) #1차원
print(x+y)

# file io
datas = np.arange(0, 10, 2)
print(datas)
np.save('test1', datas) #binary 형식으로 저장
np.savetxt('test2.txt', datas) #실수타입으로 저장

mydatas = np.loadtxt('test2.txt')
print(mydatas)