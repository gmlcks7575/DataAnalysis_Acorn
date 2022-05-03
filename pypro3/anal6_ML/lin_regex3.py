# 회귀분석 문제 3) 
# kaggle.com에서 carseats.csv 파일을 다운 받아 Sales 변수에 영향을 주는 변수들을 선택하여 선형회귀분석을 실시한다.
# 변수 선택은 모델.summary() 함수를 활용하여 타당한 변수만 임의적으로 선택한다.
# 회귀분석모형의 적절성을 위한 조건도 체크하시오.
# 완성된 모델로 Sales를 예측.
import pandas as pd

datas = pd.read_csv('../testdata/carseats.csv')
df = pd.DataFrame(datas)
print(df.corr()) # income, advertising, price, age

import statsmodels.formula.api as smf
lm = smf.ols(formula = 'Sales ~ Income + Advertising + Price + Age', data = df).fit()
print(lm.summary())