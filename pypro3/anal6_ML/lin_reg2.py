# 모델 맛보기 4 : linregress 을 사용. model 생성 O
from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# IQ에 따른 시험성적 값 예측
score_iq = pd.read_csv("../testdata/score_iq.csv")
print(score_iq.info())
print(score_iq.head(3), score_iq.shape) #(150, 6)

x = score_iq.iq
y = score_iq.score

# 상관계수 확인
print(np.corrcoef(x,y)) # numpy
print(score_iq.corr()) # pandas

# plt.scatter(x, y)
# plt.show()

# 선형회귀분석
model = stats.linregress(x, y)
print(model)#LinregressResult(slope=0.6514309527270089,
print('xslope:',model.slope)
print('yintercept:', model.intercept)
print('pvalue:',model.pvalue)
# xslope: 0.6514309527270089
# yintercept: -2.8564471221976504
# pvalue: 2.8476895206666614e-50 < 0.05 유의한 모델
# y = model.slope * x + model.intercept
print('IQ에 따른 점수 예측 :', model.slope * 140 + model.intercept) #88.3438862595836
print('IQ에 따른 점수 예측 :', model.slope * 120 + model.intercept) #75.31526720504341
# linregress는 predict을 지원하지 않음
# 그래서 numpy polyval([slope, bias], x)을 이용
print('IQ에 따른 점수 예측 :', np.polyval([model.slope,model.intercept], 140))
print()
newdf = pd.DataFrame({'iq':[55,66,77,88,150]})
print('새로운 점수 예측 : ', np.polyval([model.slope,model.intercept], newdf).flatten())
