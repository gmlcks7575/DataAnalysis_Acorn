# svm으로 XOR 분류 처리

x_data = [
    [0,0,0],
    [0,1,0],
    [1,0,0],
    [1,1,1]
]

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import svm, metrics

x_df = pd.DataFrame(x_data)
feature = np.array(x_df.iloc[:,0:2])
label = np.array(x_df.iloc[:,2])
print(feature)
print(label)

#model = LogisticRegression()
model = svm.SVC() #최소제곱법으로 추세선 값 구한다.
model.fit(feature, label) # feature와 label 사이 값의 차이(lost,cost,손실,error)가 최소
pred = model.predict(feature)
print('예측값:', pred)

print('정확도:',metrics.accuracy_score(label,pred))
pred = model.predict(feature)