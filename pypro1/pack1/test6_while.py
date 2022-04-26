# 반복문 : while 조건
a=1

while a<=5:
    print(a, end=' ')
    a = a+1
    
print('\nwhile 종료')    

print()
i = 1
while i <= 3:
    j = 1 # 첫 번째가 참일때 수행
    while j <= 4: # 첫 번째가 참일 때 수행
        print('i:' + str(i) + ',j:' + str(j)) # 두 번째가 참일 때 수행
        j += 1
    i += 1

print('\nwhile 종료2')

print('1~100 사이의 정수 중 3의 배수의 합')
i=1; hap=0
while i <= 100:
    #print(i,end= ' ')
    if i % 3 == 0:
        #print(i, end= ' ')
        hap += i
    i += 1    
print('합은', hap)    

print()
colors = ['r','g','b']
print(len(colors))
a = 0
while a < len(colors):
    print(colors[a], end = ':')
    a+=1
    
print()
while colors:
    print(colors.pop()) #pop은 뒤에서부터 하나씩 빠져 나간다.
     
print(len(colors))

print()
i=1
while i<=10:
    j=1
    res = ''
    while j <= i:
        res = res+'*'
        j += 1
    print(res)
    i+=1    
    
#python while 연습문제
#1번 1~100 사이의 숫자 중 3의 배수이나 2의 배수가 아닌 수를 출력하고, 합을 출력
i=1
hap=0
while i<=100:
    if i % 3 == 0:
        if i % 2 != 0:
            print(i)
            hap+=i
    i +=1
    
print('합:',hap)

#2번 2~5 까지의 구구단 출력
print()
i=2
while i<=5:
    j=1
    while j<=9: 
        print(str(i)+'*'+str(j)+'='+str(i*j))
        j+=1
    i+=1

#3번 -1, 3, -5, 7, -9, 11 ~ 99 까지의 합을 출력 \
print()
i=-1
j=3
hap=0
while i>=-100:
    hap += i
    while j<=100:
        hap +=j
        j+=4
    i-=4

print(hap)    

#4번 1~1000 사이의 소수(1보다 크며 1과 자신의 수 이외에는 나눌 수 없는 수)와 그 갯수를 출력
aa = 2; count = 0
while aa <= 1000:
    imsi = False
    bb = 2
    
    while bb <= aa - 1:
        if aa % bb == 0:
            imsi = True
        bb += 1
    if imsi == False:
        print(aa, end =' ')
        count +=1
    aa += 1
print()
print('갯수:',count)    