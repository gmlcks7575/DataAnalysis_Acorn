#정규표현식 : 대량의 문자열에 대해 일정한 패턴에 부여해 원하는 문자열만 취할 수 있다.
import re

ss = "12345 abc 가나다 abcABCfun_123555_6 Python is fun"
print(ss)
print(re.findall('123', ss))
aa = re.findall(r'123', ss) #r
print(aa[0])
print(re.findall('가나', ss))
print(re.findall('[12]', ss))
print(re.findall('[0-9]', ss))
print(re.findall('\d\d', ss)) #\D \s \S \w \W
# \d : 숫자와매치 \D : 숫자제외 \s 공백 \S 공백제외 \w 문자+숫자 \W 문자+숫자 제외
print(re.findall('[0-9]+', ss)) #1회 이상
print(re.findall('[0-9]?', ss)) #0, 1
print(re.findall('[0-9]*', ss)) #0회 이상
print(re.findall('[0-9]{2}', ss)) #2개씩
print(re.findall('[0-9]{2,3}', ss)) #2~3개씩
print(re.findall('[a-z]', ss))
print(re.findall('[a-zA-Z]', ss)) #영문만 
print(re.findall('[가-힣]', ss)) #한글만
print(re.findall('[^가-힣]', ss)) #한글만빼고

print()
print(re.findall('.bc', ss))#첫글자는 아무거나 그다음bc
print(re.findall('a..', ss))
print(re.findall('^123', ss)) # ^이 글자로 시작되는
print(re.findall('fun', ss))
print(re.findall('fun$', ss)) #fun으로 끝나는
print(re.findall('12|34', ss)) #12 or 34
print(re.findall('(ab)+(c)', ss)) #그룹화

print()
p = re.compile('abc')
print(re.findall(p,ss))
print(p)
p = re.compile('the',re.IGNORECASE) #대소문자 전부 찾는다
print(p.findall('The DoG the dog')) 
p = re.compile('the')
print(p.findall('The DoG the dog'))