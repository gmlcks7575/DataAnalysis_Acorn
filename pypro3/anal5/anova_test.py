# [ANOVA 예제 1]
# 빵을 기름에 튀길 때 네 가지 기름의 종류에 따라 빵에 흡수된 기름의 양을 측정하였다.
# 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 존재하는지를 분산분석을 통해 알아보자.
# 조건 : NaN이 들어 있는 행은 해당 칼럼의 평균값으로 대체하여 사용한다.
import pandas as pd
import numpy as np
import scipy.stats as stats
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import matplotlib.pyplot as plt
from statsmodels.stats.multicomp import pairwise_tukeyhsd
plt.rc('font', family =('malgun gothic'))

df = pd.DataFrame({'kind':[1,2,3,4,2,1,3,4,2,1,2,3,4,1,2,1,1,3,4,2],
                  'quantity':[64, 72, 68, 77, 56, np.nan, 95, 78, 55, 91, 63, 49, 70, 80, 90, 33, 44, 55, 66, 77]}
                   )
# 귀무 : 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 존재한다.
# 대립 : 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 존재하지 않는다.
#print(df, df.shape) # 20, 2
df = df.fillna(np.mean(df['quantity']))#nan값 평균대체
# 기름의 종류별로 나누기
df1 = df[df['kind']==1]
df2 = df[df['kind']==2]
df3 = df[df['kind']==3]
df4 = df[df['kind']==4]

data1 = np.array(df1.quantity)
data2 = np.array(df2.quantity)
data3 = np.array(df3.quantity)
data4 = np.array(df4.quantity)

# 정규성 검사
print(stats.shapiro(data1).pvalue)#0.8680403232574463
print(stats.shapiro(data2).pvalue)#0.5923936367034912
print(stats.shapiro(data3).pvalue)#0.4860108494758606
print(stats.shapiro(data4).pvalue)#0.41621729731559753
print(stats.ks_2samp(data1, data2).pvalue) #0.9307359307359307
print(stats.ks_2samp(data1, data3).pvalue) #0.9238095238095237
print(stats.ks_2samp(data1, data4).pvalue) #0.5523809523809524
print(stats.ks_2samp(data2, data3).pvalue) #0.9238095238095237
print(stats.ks_2samp(data2, data4).pvalue) #0.5523809523809524
print(stats.ks_2samp(data3, data4).pvalue) #0.7714285714285716

# 등분산성
print(stats.levene(data1,data2,data3,data4).pvalue) #0.3268969935062273
print(stats.bartlett(data1,data2,data3,data4).pvalue) # 0.19342011099507922 > 0.05 등분산성 만족

# 일원분산분석 방법1 : anova_lm #statsmodels 제공
lmodel = ols('quantity ~ C(kind)',data=df).fit() #학습하시오 fit
print(anova_lm(lmodel, typ=1))
# PR(>F) 0.848244 > 0.05이므로 귀무 채택.
# 귀무 : 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 존재한다.

# 일원분산분석 방법2 : f_oneway scipy 가 제공
f_statistic, pvalue = stats.f_oneway(data1, data2, data3, data4)
print('f_statistic:',f_statistic) #f_statistic: 0.26693511759829797
print('pvalue:',pvalue) #pvalue: 0.8482436666841788 > 0.05이므로 귀무 채택.

#사후 검정
turkey_result = pairwise_tukeyhsd(endog= df.quantity, groups = df.kind)
print(turkey_result)

turkey_result.plot_simultaneous(xlabel='mean', ylabel='group')
plt.show()

# [ANOVA 예제 2]
# DB에 저장된 buser와 jikwon 테이블을 이용하여 총무부, 영업부, 전산부, 관리부 직원의 연봉의 평균에 차이가 있는지 검정하시오.
# 만약에 연봉이 없는 직원이 있다면 작업에서 제외한다.

# 귀무 : 총무부, 영업부, 전산부, 관리부 직원의 연봉의 평균에 차이가 있다.
# 대립 : 총무부, 영업부, 전산부, 관리부 직원의 연봉의 평균에 차이가 없다.
import MySQLdb
import pickle

try:
    with open('mydb.dat', mode = 'rb') as obj:
        config = pickle.load(obj)
except Exception as e:
    print('연결 오류:', e)

try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = """
        select buser_name, jikwon_pay
        from jikwon inner join buser
        on buser_num = buser_no
    """
    cursor.execute(sql)
    jdf = pd.DataFrame(cursor.fetchall(), columns=['buser_name', 'jikwon_pay'])   
    print(jdf)
    
    jdf1 = jdf[jdf['buser_name']=='총무부']
    jdf2 = jdf[jdf['buser_name']=='영업부']
    jdf3 = jdf[jdf['buser_name']=='전산부']
    jdf4 = jdf[jdf['buser_name']=='관리부']
    
    jdata1 = np.array(jdf1.jikwon_pay)
    jdata2 = np.array(jdf2.jikwon_pay)
    jdata3 = np.array(jdf3.jikwon_pay)
    jdata4 = np.array(jdf4.jikwon_pay)
    
    # 정규성 검사
    print(stats.shapiro(jdata1).pvalue)#0.02604489028453827
    print(stats.shapiro(jdata2).pvalue)#0.025608452036976814
    print(stats.shapiro(jdata3).pvalue)#0.4194071292877197
    print(stats.shapiro(jdata4).pvalue)#0.9078023433685303
    print(stats.ks_2samp(jdata1, jdata2).pvalue) #0.33577439072795107
    print(stats.ks_2samp(jdata1, jdata3).pvalue) #0.5751748251748252
    print(stats.ks_2samp(jdata1, jdata4).pvalue) #0.5363636363636364
    print(stats.ks_2samp(jdata2, jdata3).pvalue) #0.33577439072795107
    print(stats.ks_2samp(jdata2, jdata4).pvalue) #0.6406593406593406
    print(stats.ks_2samp(jdata3, jdata4).pvalue) #0.5363636363636364
    
    # 등분산성
    print(stats.levene(jdata1,jdata2,jdata3,jdata4).pvalue) #0.7980753526275928
    print(stats.bartlett(jdata1,jdata2,jdata3,jdata4).pvalue) # 0.6290955395410989

    # 일원분산분석 방법1 : anova_lm #statsmodels 제공
    lmodel = ols('jikwon_pay ~ C(buser_name)',data=jdf).fit() #학습하시오 fit
    print(anova_lm(lmodel, typ=1))
    # PR(>F) 0.745442 > 0.05이므로 귀무 채택.
    # 귀무 : 총무부, 영업부, 전산부, 관리부 직원의 연봉의 평균에 차이가 있다.

    # 일원분산분석 방법2 : f_oneway scipy 가 제공
    f_statistic, pvalue = stats.f_oneway(jdata1, jdata2, jdata3, jdata4)
    print('f_statistic:',f_statistic) #f_statistic: 0.41244077160708414
    print('pvalue:',pvalue) #pvalue: 0.7454421884076983 > 0.05이므로 귀무 채택.
    #귀무 : 총무부, 영업부, 전산부, 관리부 직원의 연봉의 평균에 차이가 있다.
    
    #사후 검정
    turkey_result = pairwise_tukeyhsd(endog= jdf.jikwon_pay, groups = jdf.buser_name)
    print(turkey_result)
    turkey_result.plot_simultaneous(xlabel='mean', ylabel='group')
    plt.show()
    
except Exception as e:
    print('연결 오류:', e)