# Advertising.csv : 여러 매체를 통한 광고비 판매량 추정치 얻기 

import statsmodels.formula.api as smf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.tests.frame.methods.test_sort_values import ascending
from networkx.drawing.tests.test_pylab import plt
plt.rc('font', family = 'malgun gothic')

advdf = pd.read_csv('../testdata/Advertising.csv', usecols = [1,2,3,4])
print(advdf.head(3), advdf.shape) #(200, 4) 

print('상관계수(r):',advdf.loc[:,['sales','tv']].corr()) # 0.782
print('상관계수(r):',advdf.loc[:,['sales','newspaper']].corr()) #0.228
print('상관계수(r):',advdf.loc[:,['sales','radio']].corr()) #0.576

print()
# 단순 선형회귀
lm = smf.ols(formula = 'sales ~ tv', data = advdf).fit()
print(lm.summary())
print('설명력:', lm.rsquared)
print('p값:',lm.pvalues[1])

# 시각화
# plt.scatter(advdf.tv, advdf.sales)
# plt.xlabel('tv')
# plt.ylabel('sales')
# x = pd.DataFrame({'tv':[advdf.tv.min(), advdf.tv.max()]})
# y_pred = lm.predict(x)
# plt.plot(x, y_pred, c='red')
# plt.show()

# 미지의 tv 광고비에 따른 상품 판매량 추정
x_new = pd.DataFrame({'tv':[220.12, 55.66, 10]})
pred_new = lm.predict(x_new)
print('상품판매량추정치:',pred_new.values)

print('-------------')
print(advdf.corr()) # sales와의 상관관계 : tv > radio > newspaper
# lm_mul = smf.ols(formula = 'sales ~ tv+radio+newspaper', data=advdf).fit()
# print(lm_mul.summary()) #Adj. R-squared:0.896 p-value:1.58e-96 < 0.05 유의한 모델
# newpaper p-value : 0.860 > 0.05이므로 독립변수에서 제거를 고려.

lm_mul = smf.ols(formula = 'sales ~ tv+radio', data=advdf).fit()
#print(lm_mul.summary()) #Adj. R-squared:0.896 p-value:4.83e-98 < 0.05 유의한 모델
# newpapers는 모델의 성능에 영향을 주지 못하는 변수

# 새로운 독립변수 값으로 종속되는 sales를 예측해서 추정치를 얻기
x_new2 = pd.DataFrame({'tv':[220.12,55.66,10], 'radio':[30.3, 40.4, 50.5]})
pred_new2 = lm.predict(x_new2)
#print('상품 판매량 추정치:', pred_new2.values)

print('*** 선형회귀분석의 기존 가정 충족 조건 ***')
# 선형성 : 독립변수(feature)의 변화에 따라 종속변수도 일정 크기로 변화해야 한다.
# 정규성 : 잔차항이 정규분포를 따라야 한다.
# 독립성 : 독립변수의 값이 서로 관련되지 않아야 한다.
# 등분산성 : 그룹간의 분산이 유사해야 한다. 독립변수의 모든 값에 대한 오차들의 분산은 일정해야 한다.
# 다중공선성 : 다중회귀 분석 시 두 개 이상의 독립변수 간에 강한 상관관계가 있어서는 안된다.

# 잔차항 구하기 (실제값 - 예측값)
fitted = lm_mul.predict(advdf.iloc[:,0:2]) #tv radio
# print(fitted) # 예측값
residual = advdf['sales'] - fitted
print(np.mean(residual)) #1.873168287147564e-14

import seaborn as sns
print('선형성 : 예측값과 잔차의 분포가 유사----- ')
sns.regplot(fitted, residual, lowess = True, line_kws = {'color':'red'}) 
# 선형회귀 모델의 적합성을 그릴대 사용 - 잔차의 추세선을 시각화
plt.plot([fitted.min(), fitted.max()], [0, 0], '--', color='gray')
plt.show() # 선형성을 만족하지 못한다 : 다형회귀(비선형) 모델을 추천 - PolynomialFeatures

print('\n 정규성 : 잔차가 정규분포를 따르는지 확인 Q-Q plot ---- ')
import scipy.stats

sr = scipy.stats.zscore(residual)
(x, y), _ = scipy.stats.probplot(sr)
sns.scatterplot(x, y)
plt.plot([-3,3],[-3,3], '--', color='gray')
plt.show()
# 정규성을 만족하지 않음 : 데이터에 대해 표준화, 정규화, log를 씌우는 등의 작업을 시도
print('shapiro test:', scipy.stats.shapiro(residual))
# shapiro test: ShapiroResult(statistic=0.9180378317832947, pvalue=4.190036317908152e-09)
# pvalue=4.190036317908152e-09 < 0.05 이므로 정규성을 만족하지 않음

print('\n 독립성 : 잔차가 자기상관을 따르는지 확인 ---- ')
# Durbin-Watson : 2.081 자기상관: 0에가까우면 -자기상관 4에 가까우면 +자기상관 > 2에가까울수록 독립성 만족

print('\n 등분산성 : 잔차의 분산이 일정해야함')
sr = scipy.stats.zscore(residual)
sns.regplot(fitted, np.sqrt(np.abs(sr)), lowess = True, line_kws = {'color':'red'}) 
plt.show() 
# 등분산성 만족 못함 : 비선형인지 확인, 이상 값 확인
# 정규성은 만족하나 등분산성은 만족하지 못한 경우 가중회귀분석(weighted regression)분석 

print('\n 다중공선성 : 독립 변수들 간에 상관관계 확인')
from statsmodels.stats.outliers_influence import variance_inflation_factor
# VIF (Variable Inflaction Factors : 분산 팽창 계수) 값 확인 : 10을 넘으면 다중공선성을 의심
print(variance_inflation_factor(advdf.values, 1)) #tv
print(variance_inflation_factor(advdf.values, 2)) #radio
vifdf = pd.DataFrame() #dataframe으로 확인하기
vifdf['vif_value'] = [variance_inflation_factor(advdf.values,i)for i in range(1,3)] 
print(vifdf)

print("\n참고 : 극단치(이상치) 확인 - Cook's distance ")
from statsmodels.stats.outliers_influence import OLSInfluence
cd, _ = OLSInfluence(lm_mul).cooks_distance # 극단값을 나타내는 지표 반환
print(cd.sort_values(ascending =False).head())

import statsmodels.api as sm
sm.graphics.influence_plot(lm_mul, criterion = 'cooks')
plt.show()

print(advdf.iloc[[130,5,35,178,126]])