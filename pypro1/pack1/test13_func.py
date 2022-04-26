#변수의 생존 범위 (scope rule) : 전역변수, 지역변수
#접근 우선 순서 : Local > Encolsing function > Global

player = '전국대표' # 전역변수 : 현재 모듈의 어디서든 공유가 가능
print(player)

def funcSoccer():
    name = '신선해' # 지역변수 : 현재 함수 내에서만 유효
    player = '지역대표'
    print(name, player)
    
funcSoccer()
#print(name) #NameError: name 'name' is not defined (name은 지역변수)
print(player)

print('-----------')
a = 10; b = 20; c = 30
print('1)a:{} b:{} c:{}'.format(a,b,c))

def foo():
    a=40
    b=50
    def bar():
        #c=60
        global c # 전역변수
        nonlocal b # foo 함수 수준의 변수
        print('2)a:{} b:{} c:{}'.format(a,b,c))
        c=60 # UnboundLocalError: local variable 'c' referenced before assignment
        b=70
    bar()
    print('3)a:{} b:{} c:{}'.format(a,b,c))
    
foo()    
print('처리 후)a:{} b:{} c:{}'.format(a,b,c))

print('----')
g=1
def func():
    global g #안하면 오류
    a = g
    g = 2
    return [a,g] #tuple에서 list로 넘어가게해준다.

print(func())