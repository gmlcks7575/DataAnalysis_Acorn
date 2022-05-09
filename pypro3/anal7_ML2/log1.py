# 로지스틱 회귀분석
# 분류 모델 : 이항분류가 기본
# 독립변수 : 연속형, 종속변수 : 범주형
# 출력된 연속형 자료를 logit 변환해 sigmoide function 함수로 0~ 1사이의 실수 값이 나오도록 한 후 0.5를 기준으로 분류

import math
import numpy as np
from sklearn.metrics._scorer import accuracy_scorer

def sigmoidFunc(x):
    return 1 / (1 + math.exp(-x))

print(sigmoidFunc(3))
print(sigmoidFunc(1))
print(sigmoidFunc(-2))
print(sigmoidFunc(-5))
#--------------------------------

# mtcars dataset으로 분류 작업
import statsmodels.api as sm

mtcarData = sm.datasets.get_rdataset('mtcars')
print(mtcarData.keys())
mtcars = sm.datasets.get_rdataset('mtcars').data
print(mtcars.head(3))
print(mtcars['am'].unique()) # [1 0] 수동 또는 자동
mtcar = mtcars.loc[:,['mpg','hp','am']]

# 연비와 마력수에 따른 변속기 분류
# 모델 작성 방법 1 : logit()
import statsmodels.formula.api as smf
formula = 'am ~ mpg + hp'
result = smf.logit(formula = formula, data=mtcar ).fit()
print(result)
print(result.summary())
# print('예측값:', result.predict())

pred = result.predict(mtcar[:10])
# print('예측값:',pred.values)
print('예측값:',np.around(pred.values))
print('실제값:',mtcar['am'][:10].values)
print()
conf_tab = result.pred_table()
print('confusion matrix : \n', conf_tab)
# 모델의 분류 정확도(accuracy)
print('정확도1:',((16+10)/len(mtcar)))
print('정확도2:',((conf_tab[0][0]+conf_tab[1][1])/len(mtcar)))

from sklearn.metrics import accuracy_score
pred2 = result.predict(mtcar)
print('정확도3:', accuracy_score(mtcar['am'], np.around(pred2)))

# 모델 작성 방법 2 : glm() : generalized linear model (일반화된 선형모델)
result2 = smf.glm(formula = formula, data=mtcar, family = sm.families.Binomial()).fit()
print(result2)
print(result2.summary())