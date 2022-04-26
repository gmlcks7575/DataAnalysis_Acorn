# 상속
class Person:
    say = '난 사람이야'
    nai = 20
    __abc = 'good' # private
    
    def __init__(self, nai):
        print('Person 생성자')
        self.nai = nai
        
    def printInfo(self):
        print('나이:{}, 이야기:{}'.format(self.nai, self.say))
    
    def hello(self):
        print('안녕')
        print(self.__abc)
        
    @staticmethod
    def sbs(tel):
        print('sbs_static metehod',tel)    
        
print(Person.say, Person.nai)    
p = Person(22)
p.printInfo()
p.hello()

print('***'*10)
class Employee(Person):
    say = '일하는 동물'
    subject = '근로자' #고유의 멤버 필드 Employee만 가지고 있다.
    def __init__(self):
        print('Employee 생성자')
    
    def printInfo(self): # method override
        print('Employee 클래스 내의 printInfo')
        
    def eprintInfo(self):
        self.printInfo() #Empolyee 내부에있는 printInfo
        super().printInfo() #부모에 있는 printInfo를 찾는다
        print(self.say, super().say) #self.say는 일하는 동물 super().say는 난 사람이야
        self.hello()
        
e = Employee()
print(e.say,e.nai) #나이 : 20 (부모에게올라가서 20) 이야기 : 일하는 동물(자기자신 찾아서 일하는 동물)
print(e.subject)
e.printInfo() #Employee에 없어서 부모에게 올라가 찾는다
e.eprintInfo() #employeee의 self.printInfo를 찾고 없어서 부모에게 올라간다.

print('---'*10)
class Worker(Person):
    def __init__(self, nai):
        print('Worker 생성자')
        super().__init__(nai) #부모 생성자 호출 #Bound method call
        
    def wprintInfo(self):
        super().printInfo()

w = Worker('25')
print(w.say, w.nai)
w.printInfo()
w.wprintInfo()

print('~~~'*10)
class Programmer(Worker):
    def __init__(self, nai):
        print('Programmer 생성자')
        Worker.__init__(self, nai) # unBound method call
        
    def wprintInfo(self): # Worker에 있는 오버라이딩
        print('Programmer 내에 작성된 wprintInfo')
    
    def hello2(self):
        print(super().__abc)   
        
pr = Programmer(33)
print(pr.say, pr.nai)
pr.printInfo()
pr.wprintInfo()
        
print()
p.hello()
#pr.hello2() #err
w.sbs('111-111')   
pr.sbs('222-2222')

print('클래스 타입---')
a = 10
print(type(a))
print(type(pr))
print(Programmer.__bases__)
print(Worker.__bases__)
print(Person.__bases__)