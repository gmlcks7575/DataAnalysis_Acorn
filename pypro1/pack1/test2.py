#연산자
#소괄호 > 산술연산자(*,/,// > +,-) > 관계연산자(>, >=, ==, !=, <, <=) > 논리연산자 (not, and, or) > 치환(=)
v1 = 3 # 치환
v1 = v2 = v3 = 2
print(v1, v2, v3)
print(id(v1),id(v2),id(v3))

v1, v2 = 10, 20
print(v1, v2)

print()
print('packing 연산자 : *, **')
v1, *v2 = [1, 2, 3, 4, 5]
print(v1,v2)
*v1, v2 = [1, 2, 3, 4, 5]
print(v1,v2)

*v1, v2, v3 = [1, 2, 3, 4, 5]
print(v1,v2,v3)

print()
print('-연산자 연습---')
print(5+3, 5-3, 5*3, 5/3, 5//3, 5%3, 5**3)
print(divmod(5,3)) #(1,2) 앞의 수를 뒤의 수로 나눗셈을 하고 몫과 나머지가 나오게한다.
print('연산자 우선 순위:', 3+4*5)
print('연산자 우선 순위:', (3+4)*5)

print(5>3, 5==3, 5!=3)
print(5>3 and 4<3, 5>=3 or 4<=3, not(5>3))

print('문자열 더하기', end='')
print('이어쓰기')
print('대한'+'민'+"국 만세")
print('한국'*20)

print()
a=10
a=a+1
a += 1
#a++ ++a : 자바의 증가연산자는 누적으로 사용 불가
print('누적결과:',a)

print('부호변경:',a,a * -1,-a,--a,+a,++a)

print()
print('문자 숫자 형변환') 
#print(5+'5') #TypeError : unsupported operand type(s) for +: 'int' and 'str', 'float'
print(5+int('5')) #숫자 10
print(str(5)+'5') #문자 55
print('나이는'+str(23)+'살')

print()
print('escape 문자 ---')#\n \b \a \t ...
print('kbs\nmbc')
print('c:\nbc\tbs\abc.txt')#escape 문자를 그냥 데이터 인식하려면 r을 선행

print()
print(True, bool(True),False,bool(False))
print(bool(-1),bool(2.3),bool(123),bool('abc'))
print(bool(0),bool(''),bool(None),bool([]),bool({}))

# print()함수에 서식넣기
print()
print(format(123.45678, '10.3f'))
print(format(123.45678, '10.3'))
print(format(123, '10d'))

print()
print('나는 나이가 %d 이다.'%23)
print('나는 나이가 %s 이다.'%'스물셋')
print('나는 나이가 %d 이고 이름은 %s이다.'%(23, '홍길동'))
print('나는 나이가 %s 이고 이름은 %s이다.'%(23, '홍길동'))
print('나는 키가 %f이고, 에너지가 %d%%.'%(177.7, 100))
print('이름은 {0}, 나이는 {1}'.format('한국인', 33))
print('이름은 {}, 나이는 {}'.format('신선해', 33))
print('이름은 {1}, 나이는 {0}'.format(34, '강나루'))