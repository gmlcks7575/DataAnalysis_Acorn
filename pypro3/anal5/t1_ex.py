import numpy as np
import scipy.stats as stats
import pandas as pd

# [one-sample t 검정 : 문제1]  
# 영사기에 사용되는 구형 백열전구의 수명은 250시간이라고 알려졌다. 
# 한국연구소에서 수명이 50시간 더 긴 새로운 백열전구를 개발하였다고 발표하였다. 
# 연구소의 발표결과가 맞는지 새로 개발된 백열전구를 임의로 수집하여 수명시간을 수집하여 다음의 자료를 얻었다. 
# 한국연구소의 발표가 맞는지 새로운 백열전구의 수명을 분석하라.
sample = [305, 280, 296, 313, 287, 240, 259, 266, 318, 280, 325, 295, 315, 278]
# 귀무 : 영사기에 사용되는 구형 백열전구의 수명은 250시간이다.
# 대립 : 영사기에 사용되는 구형 백열전구의 수명은 300시간이다.
print(np.array(sample).mean()) # 289.7857 // 300
print(stats.shapiro(sample)) # pvalue=0.820862 > 0.05 정규성 만족
result = stats.ttest_1samp(sample, popmean = 300) #t-test one sample
print('t값:%.3f, p-value:%.3f'%result) # t값:-1.556, p-value:0.144
# 해석 : p-value:0.144 > 0.05 이므로 귀무가설 채택. 한국연구소의 발표가 틀렸다.

# [one-sample t 검정 : 문제2] 
# 국내에서 생산된 대다수의 노트북 평균 사용 시간이 5.2 시간으로 파악되었다. 
# A회사에서 생산된 노트북 평균시간과 차이가 있는지를 검정하기 위해서 A회사 노트북 150대를 랜덤하게 선정하여 검정을 실시한다.
# 실습 파일 : one_sample.csv
# 참고 : time에 공백을 제거할 땐 ***.time.replace("     ", "")
data2=pd.read_csv('../testdata/one_sample.csv')
data2=data2.replace("     ", "")
data2.time=pd.to_numeric(data2.time)
data2 = data2.time.dropna(axis=0)
print(np.mean(data2)) # 5.5568807339449515
print(stats.shapiro(data2)) #ShapiroResult(statistic=0.9913735389709473, pvalue=0.7242600917816162)
result = stats.ttest_1samp(data2, popmean = 5.2)
print('t값:%.7f, p-value:%.7f'%result) # t값:3.946,p-value:0.0001417
# 해석 : p-value:0.0001417 < 0.05 이므로 귀무가설 기각. 국내에서 생산된 대다수의 노트북 평균 사용 시간이 5.2 시간이 아니다.

# https://www.price.go.kr/tprice/portal/main/main.do 에서 
# 메뉴 중  가격동향 -> 개인서비스요금 -> 조회유형:지역별, 품목:미용 자료를 파일로 받아 미용 요금을 얻도록 하자. 
# 정부에서는 전국 평균 미용 요금이 15000원이라고 발표하였다. 이 발표가 맞는지 검정하시오.

data3 = pd.read_excel('../testdata/test3.xls')
df = pd.DataFrame(data3)
df = df.T
df = df.dropna()
df2= df[2:]
df2.columns = ['가격']
print(df2)

print(np.mean(df2['가격'])) # 16743.5625
print(stats.shapiro(df2['가격'])) # ShapiroResult(statistic=0.9382560849189758, pvalue=0.3281988501548767)
result = stats.ttest_1samp(df2['가격'], popmean = 15000)
print('t값:%.3f, p-value:%.3f'%result) # t값:3.990, p-value:0.001
# 해석 : p-value:0.001 < 0.05 이므로 귀무가설 기각. 전국 평균 미용 요금은 15000이 아니다.