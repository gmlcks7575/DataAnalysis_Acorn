# 위키백과 사이트에서 검색단어 관련 글 스크래핑 후 형태소 분석
import urllib
from bs4 import BeautifulSoup
from konlpy.tag import Okt
from urllib import parse # 한글 인코딩용 모듈

okt = Okt()
para = parse.quote('이순신') #이순신을 한글 인코딩해준다
url = "http://ko.wikipedia.org/wiki/"+para
page = urllib.request.urlopen(url)

soup = BeautifulSoup(page.read(), 'lxml')
#print(soup)

# 한글 형태소 분석으로 명사만 추출 기억장소에 담기
wordlist = []
# #mw-content-text > div.mw-parser-output > p:nth-child(5)
for item in soup.select("#mw-content-text > div > p "):
    if item.string != None:
        #print(item.string)
        wordlist += okt.nouns(item.string)

print('wordlist 출력:', wordlist)
print('단어 수 :', len(wordlist))
print('중복 제거 후 단어 수 :',len(set(wordlist)))

print()
word_dict = {} #단어의 발생 회수 ex : {"이순신" : 5}
for i in wordlist:
    if i in word_dict:
        word_dict[i] += 1
    else:
        word_dict[i] = 1

print('word_dict 출력:', word_dict)

import pandas as pd
print('DataFrame에 담기 --')
df1 = pd.DataFrame(wordlist, columns=['단어'])
print(df1.head(3))
print()
df2 = pd.DataFrame([word_dict.keys(),word_dict.values()])
print(df2)
df2 = df2.T
df2.columns = ['단어','빈도수']
print(df2.head(5))

print('------------------------')
# 파일로 저장
df2.to_csv('이순신.csv', sep=',', index=False)

df3 = pd.read_csv('이순신.csv')
print(df3)