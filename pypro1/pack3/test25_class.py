# class

kor = 100 #전역변수

def abc(): #function
    print('함수라고 해')
    
class myClass: #상속이 아니라 () 쓸필요가 없다. #클래스
    kor = 90 # 멤버 변수
    
    def abc(self): #멤버 메소드
        print('난 메소드야')
        
    def show(self):
        # kor = 88
        print(self.kor)
        print(kor) #지역변수가 없으면 모듈의 변수를 찾아간다.
        self.abc()
        abc()
        
my = myClass()
my.show()

print('-----------')
class ourClass:
    a = 1

print(ourClass.a)

our1 = ourClass()
print(our1.a)

our2 = ourClass()
print(our2.a)
our2.b = 2
print(our2.b)

#오류 print(our1.b) # 오류