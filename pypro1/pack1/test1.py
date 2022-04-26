'''
여러 줄
주석
'''

"""
여러 줄
주석
"""
#한 줄 주석

print("환영합니다. python 세상")
print('환영합니다. python 세상');
a = "안녕" # 객체의 주소를 기억. 참조형 기억 장소
a = '반가워'
a = 10; b=20.5
c = b # 주소 치환
print(a, b, c)
print(id(a),id(b),id(c))
a=10
b=10
print(a==b, a is b) # == 값 비교 연산자, is 주소 비교 연산자
aa = [10]
bb = [10]
print(aa==bb, aa is bb)

print()
A = 1; a = 2
print(A, a, id(A), id(a))

print()
import keyword
print('예약어 : ', keyword.kwlist)

print('자료형 확인')
print(3, type(3))
print(3.4, type(3.4))
print(3+4j, type(3+4j))
print(True, type(True))
print('kbs', type('kbs'))

print((1,), type((1,)))
print([1], type([1]))
print({1}, type({1}))
print({'key':1}, type({'key':1}))
