# 회귀분석 문제 3) 
# kaggle.com에서 carseats.csv 파일을 다운 받아 Sales 변수에 영향을 주는 변수들을 선택하여 선형회귀분석을 실시한다.
# 변수 선택은 모델.summary() 함수를 활용하여 타당한 변수만 임의적으로 선택한다.
# 회귀분석모형의 적절성을 위한 조건도 체크하시오.
# 완성된 모델로 Sales를 예측.
import pandas as pd
import matplotlib.pyplot as plt

datas = pd.read_csv('../testdata/carseats.csv')
df = pd.DataFrame(datas)
print(df.corr()) # income, advertising, price, age

import statsmodels.formula.api as smf
lm = smf.ols(formula = 'Sales ~ Income + Advertising + Price + Age', data = df).fit()
print('결과:',lm.summary()) #< 0.05이므로 유의하다

# 잔차항 (실제값 - 예측값)
fitted = lm.predict(df)
import numpy as np
residual = df['Sales'] - fitted
print('잔차의 평균 : ',np.mean(residual)) # -5.933031843596836e-15

# 선형성 : 예측값과 잔차의 분포가 유사
import seaborn as sns
sns.regplot(fitted, residual, lowess = True, line_kws = {'color':'red'}) 
# 선형회귀 모델의 적합성을 그릴대 사용 - 잔차의 추세선을 시각화
plt.plot([fitted.min(), fitted.max()], [0, 0], '--', color='gray')
plt.show()

# 정규성 : 잔차가 정규분포를 따르는지 확인 Q-Q plot
import scipy.stats
sr = scipy.stats.zscore(residual)
(x, y), _ = scipy.stats.probplot(sr)
sns.scatterplot(x, y)
plt.plot([-3,3],[-3,3], '--', color='gray')
plt.show()
print('shapiro test:', scipy.stats.shapiro(residual))

# 독립성 : 잔차가 자기상관을 따르는지 확인
# Durbin-Watson:1.931

# 등분산성 : 잔차의 분산이 일정해야함
sr = scipy.stats.zscore(residual)
sns.regplot(fitted, np.sqrt(np.abs(sr)), lowess = True, line_kws = {'color':'red'}) 
plt.show() 


# 다중공선성 : 독립 변수들 간에 상관관계 확인
from statsmodels.stats.outliers_influence import variance_inflation_factor
# VIF (Variable Inflaction Factors : 분산 팽창 계수) 값 확인 : 10을 넘으면 다중공선성을 의심
df2 = df[['Price','Income','Advertising','Age']]
vifdf = pd.DataFrame() #dataframe으로 확인하기
vifdf['vif_value'] = [variance_inflation_factor(df2.values,i)for i in range(df2.shape[1])] 
print(vifdf)

# 새로운 값
new_df = pd.DataFrame({'Price':[105,89,75],'Income':[35,62,24], 'Advertising':[6,3,11],'Age':[35,42,21]})
pred = lm.predict(new_df)
print(pred)