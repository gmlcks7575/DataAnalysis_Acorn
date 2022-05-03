# 회귀분석 문제 2) 
# testdata에 저장된 student.csv 파일을 이용하여 세 과목 점수에 대한 회귀분석 모델을 만든다. 
# 이 회귀문제 모델을 이용하여 아래의 문제를 해결하시오.  수학점수를 종속변수로 하자.
#   - 국어 점수를 입력하면 수학 점수 예측
#   - 국어, 영어 점수를 입력하면 수학 점수 예측

import pandas as pd
import statsmodels.formula.api as smf

datas = pd.read_csv('../testdata/student.csv')
#print(data)
#print(data.corr())

result = smf.ols('수학 ~ 국어', data = datas).fit()
#print(result.summary())

datas.국어 = int(input('국어 점수를 입력:'))
new_pred = result.predict(pd.DataFrame(datas.국어))
print('수학점수는 {}', new_pred[0])

result2 = smf.ols('수학 ~ 국어 + 영어', data = datas).fit()
datas.국어 = int(input("국어 점수를 입력:"))
datas.영어 = int(input("영어 점수를 입력:"))
new_pred2 = result.predict(pd.DataFrame({'국어':datas.국어, '영어':datas.영어}))
print('예상 수학 점수:', new_pred2[0])
