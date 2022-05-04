# 회귀분석 문제 1) scipy.stats.linregress() <= 꼭 하기 : 심심하면 해보기 => statsmodels ols(), LinearRegression 사용
# 나이에 따라서 지상파와 종편 프로를 좋아하는 사람들의 하루 평균 시청 시간과 운동량 대한 데이터는 아래와 같다.
#  - 지상파 시청 시간을 입력하면 어느 정도의 운동 시간을 갖게 되는지 회귀분석 모델을 작성한 후에 예측하시오.
#  - 지상파 시청 시간을 입력하면 어느 정도의 종편 시청 시간을 갖게 되는지 회귀분석 모델을 작성한 후에 예측하시오.
#     참고로 결측치는 해당 칼럼의 평균 값을 사용하기로 한다. 이상치가 있는 행은 제거. 10시간 초과는 이상치로 한다. 

import pandas as pd
import numpy as np
from scipy import stats
data = pd.read_csv("../testdata/운동.csv")

# 결측치 평균 값으로 사용하기
data = data.fillna(data['지상파'].mean())
# 이상치 제거
data = data[data['운동'] <= 10]
# 지상파 시청 시간, 운동 시간 분류
print(data)
x = data.지상파
y = data.운동

# 상관계수 확인
#print(data.corr()) # 지상파 시청 시간과 운동 시간은 음의 상관관계이다.

# 선형회귀분석
model = stats.linregress(x, y)
print(model) #slope=-0.6684550167105406, intercept=4.709676019780582, pvalue=6.347578533142469e-05 < 0.05
# y = model.slope * x + model.intercept
new_df = pd.DataFrame({'지상파':[0.9,1.2,1.2,1.9,3.3,4.1,5.8,2.8,3.8,2.707,0.9,3.0,2.2,2.0]})
print('지상파 신청 시간에 따른 운동 시간 예측 :', np.polyval([model.slope,model.intercept], new_df).flatten())

# 선형회귀분석2
import statsmodels.formula.api as smf
x1 = x
y1 = y
model2 = smf.ols(formula = 'y1 ~ x1', data = data).fit()
#print(model2.summary()) # Intercept : 4.7097 x : -0.6685
new_df2=pd.DataFrame({'x1':[0.9,1.2,1.2,1.9,3.3,4.1,5.8,2.8,3.8,2.707,0.9,3.0,2.2,2.0]}) # 기존자료로 예측값 확인
new_pred = model2.predict(new_df2)
print('모델이 예측한 값(method):\n',new_pred)

# 선형회귀분석3
from sklearn.linear_model import LinearRegression
model3 = LinearRegression()
xx = np.array(x)
yy = np.array(y)
# print(type(xx))
# print(type(yy))
fit_model3 = model3.fit(xx.reshape(-1,1),y)
print('slope',fit_model3.coef_)
print('bias',fit_model3.intercept_)
y_new = fit_model3.predict(xx.reshape(-1,1))
print('모델이 예측한 값(method):',y_new[0])
