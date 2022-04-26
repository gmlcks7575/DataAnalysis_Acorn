# 다중상속
# 복수의 클래스를 상속 가능 : 순서가 중요
class Donkey:
    data = ' 당나귀 만세 '
    
    def skill(self):
        print('당나귀 : 짐 나르기')
        
class Horse:
    def skill(self):
        print('말 : 달리기')
    
    def hobby(self):
        print('프로그램 짜기')

class Mule1(Donkey, Horse):
    pass

mu1 = Mule1()
print(mu1.data)
mu1.skill() # 동일한 이름이면 우선순위가 먼저온 Donkey한테 있다.
mu1.hobby()

print()
class Mule2(Horse, Donkey):
    def play(self):
        print('노새 고유 메소드')
        
    def hobby(self):
        print('논새는 걷기를 좋아함')
        
    def showHobby(self):
        self.hobby()
        super().hobby()
        print(self.data, super().data)
        
mu2 = Mule2()
mu2.skill() # Horse를 먼저적어서 Horse가가진 스킬이 넘어옴
mu2.hobby() # 오버라이딩해서 논새는 걷기를 좋아함이 나온다
mu2.play() #고유의 메소드
mu2.showHobby()