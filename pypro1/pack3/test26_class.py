# 클래스는 새로운 타입을 만든다.
# 행위 : function로 처리 행위 + 속성 : class로 처리  
class Singer:
    title_song = '화이팅 코리아' #무조건 public 접근지정자 X
    
    def sing(self):
        msg = "노래는"
        print(msg, self.title_song, '랄라라 ~~~~')
        
    def hello(self):
        print('안녕하세요 저 가수에요')
        
    # ...    

print()    
# ---아래 내용은 별도의 모듈을 만들었던 가정 ------
bts = Singer()
bts.hello()
bts.sing()

print()
blackpink = Singer()
blackpink.hello()
blackpink.sing()
blackpink.title_song = "마지막 처럼"
blackpink.sing()
blackpink.co = 'SM'
print('blackping 소속사:',blackpink.co)
#print('bts 소속사 :',bts.co) 소속사를 안넣어줬다.
bts.sing()

print()
print(id(bts), id(blackpink)) # 주소가 다르다
print(type(bts), type(blackpink)) # singer타입

#클래스 has a 포함관계 is a 상속관계
