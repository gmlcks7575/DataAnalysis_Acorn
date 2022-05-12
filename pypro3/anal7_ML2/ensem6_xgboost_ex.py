# [XGBoost 문제] 
#
# kaggle.com이 제공하는 'glass datasets'
#
# 유리 식별 데이터베이스로 여러 가지 특징들에 의해 7가지의 label(Type)로 분리된다.
#
# RI    Na    Mg    Al    Si    K    Ca    Ba    Fe    
#  Type
#
#                           ...
#
# glass.csv 파일을 읽어 분류 작업을 수행하시오.

import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from xgboost import plot_importance
from sklearn import preprocessing

df= pd.read_csv('../testdata/glass.csv')
print(df.info())


x = df.drop(columns = ['Type'])
y = df['Type']

y2 = preprocessing.LabelEncoder().fit(y).transform(y)

x_train, x_test, y_train, y_test = train_test_split(x, y2, test_size=0.2, random_state=3)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

model = xgb.XGBClassifier(booster = 'gbtree', max_depth = 6, n_estimators = 500).fit(x_train,y_train) #gbtree 의사결정기반
pred = model.predict(x_test)
print('예측값:',pred[:10])
print('실제값:',y_test[:10])

from sklearn import metrics 
print('분류정확도',metrics.accuracy_score(y_test,pred))
print('분류보고서',metrics.classification_report(y_test,pred))

# 시각화
fig, ax = plt.subplots(figsize=(10,12))
plot_importance(model, ax=ax)
plt.show()