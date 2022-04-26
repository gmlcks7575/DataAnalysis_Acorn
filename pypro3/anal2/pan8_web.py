# 웹 문서 읽기
# import requests
import urllib.request as req
from bs4 import BeautifulSoup

# 위키백과 사이트에서 이순신으로 검색된 자료 읽기
url = "https://ko.wikipedia.org/wiki/%EC%9D%B4%EC%88%9C%EC%8B%A0"
wiki = req.urlopen(url)
#print(wiki.read()) 렉

soup = BeautifulSoup(wiki, 'html.parser')
print(soup)
print(soup.select("div.mw-parser-output > p"))

#ss = soup.select("div.mw-parser-output > p > b ")#p태그의 b태그만 찍기
ss = soup.select("div.mw-parser-output > p ") 
for s in ss: 
    if s.string != None: #none이 아닌값만 찍기
        print(s.string)
        
print('-------------------------')
url2 = "https://news.daum.net/society#1"
daum = req.urlopen(url2)
soup2 = BeautifulSoup(daum, 'lxml')
print(soup2.select_one("body > div.direct-link > a").string)

datas = soup2.select("div.direct-link > a")
print(datas)
for i in datas:
    href = i.attrs['href']
    ss = i.string
    print('href:%s, text:%s'%(href,ss))

print()
datas = soup2.findAll('a')
#print(datas)
for i in datas[:10]: #10개만 가져오기
    href = i.attrs['href']
    ss = i.string
    print('href:%s, text:%s'%(href,ss))