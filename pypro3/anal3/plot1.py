# 시각화 : 많은 양의 데이터를 효율적으로 봄으로해서 인사이트를 정확하게 얻어 낼 수 있다.

import numpy as np
import matplotlib.pyplot as plt
plt.rc('font',family='malgun gothic') #한글살리기
plt.rcParams['axes.unicode_minus'] = False #음수살리기

x = ["서울", "인천", "수원"] # set X
y = [5,3,7]

#plt.plot(y)
#plt.xlim([-1,3]) # x축 경계값 지정
#plt.ylim([0,10]) # y축
#plt.yticks(list(range(0,11,3)))
#plt.plot(x,y) # 그래프 x,y는 숫자만들어올수있다. 하지만 index는 가능하다
#plt.show()

#data = np.arange(1,11,2)
#print(data)
#plt.plot(data)
#x = [0,1,2,3,4]
#for a, b in zip(x, data):
#   plt.text(a, b, str(b))
#plt.show()

# sin 곡선
#x = np.arange(10)
#y = np.sin(x)
#print(x, y)
#plt.plot(x, y)
#plt.plot(x, y, 'bo')
#plt.plot(x, y, 'r+')
#plt.plot(x, y, 'go--', linewidth=2, markersize=12) # 라인굵기 lw=2, 마커모양 marker='o', 칼러 c='g'
#go-- go-. go:
#plt.show()

#hold
x = np.arange(0, np.pi * 3, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

#plt.figure(figsize=(10, 5))
#plt.plot(x, y_sin, 'r') #직선
#plt.scatter(x, y_cos) #산점도
#plt.xlabel('x축')
#plt.ylabel('y축')
#plt.legend(['sine','cosine']) #범례
#plt.show()

#subplot
#plt.subplot(2,1,1)
#plt.plot(x,y_sin,'r')
#plt.title('사인그래프')
#plt.subplot(2,1,2)
#plt.scatter(x,y_cos)
#plt.title('코사인그래프')
#plt.show()

#꺽은 선 그래프
irum = ['a','b','c','d','e']
kor = [80,50,70,70,90]
eng = [60,70,80,70,60]
plt.plot(irum, kor, 'ro-') #빨강동그라미실선
plt.plot(irum, eng, 'bo-') #파랑동그라미실선
plt.title('시험점수')
plt.ylim([0, 100])
plt.legend(['국어','영어'],loc = 4) #시계반대방향으로 1234~
plt.grid(True)

fig = plt.gcf() #그래프를 이미지로 저장
plt.show()
fig.savefig('plot1.png')

from matplotlib.pyplot import imread # 저장된 그래프를 읽어오기
img = imread('plot1.png')
plt.imshow(img)
plt.show()
