# function : 자원의 재활용 가능. 여러 개의 수행문을 하나의 이름으로 묶은 실행 단위이다.
# 사용자 정의 함수 형식 : def 함수명(para...): ~~
# 내장 함수 : maker가 제공하는 함수
print('표준 출력장치로 데이터를 출력하는 내장 함수')
print(sum([3,5,7]))
print(bin(8))
print(int(1.7), float(2), str(5)+'5')
a = 10
b = eval('a + 5') #수식의 모양을 하고 있는 문자열을 연산에 포함
print(b)

print(all([True, False])) # 전부
print(any([True, False])) # 하나라도
a = [1,3,2,5,7,61]
res = all(i<10 for i in a)
print('모든 숫자가 10 미만이냐', res)

print()
x = [1,2,3]; y = ['a','b']
for i in zip(x,y): #묶어줌
    print(i)
    
print(round(1.2), round(1.6)) #반올림

import math
print(math.ceil(1.2), math.ceil(1.6)) #올림
print(math.floor(1.2), math.floor(1.6)) #내림
print(math.pi)