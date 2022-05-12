# RandomForest 문제1
# kaggle.com이 제공하는 'Red Wine quality' 분류 ( 0 - 10)
# https://www.kaggle.com/sh6147782/winequalityred?select=winequality-red.csv

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV

data = pd.read_csv('../testdata/winequality-red.csv')
#print(data.describe())

data_x = data.drop(columns = ['quality'], axis='columns')
data_y = data['quality']

x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, test_size=0.2, random_state=1)

rfmodel = RandomForestClassifier().fit(x_train, y_train)
rfpredict = rfmodel.predict(x_test)
print('RandomForestClassifier acc : {0:.5f}'.format(accuracy_score(y_test, rfpredict)))

print('특성(변수) 중요도 :\n{}'.format(rfmodel.feature_importances_))

# def plot_feature_importances(model):   # 특성 중요도 시각화
#     n_features = data_x.shape[1]
#     plt.barh(range(n_features), model.feature_importances_, align='center')
#     plt.yticks(np.arange(n_features), data_x.columns)
#     plt.xlabel("attr importances")
#     plt.ylabel("attr")
#     plt.ylim(-1, n_features)
#     plt.show()
#     plt.close()
# plot_feature_importances(rfmodel)

# 변수 5개로 줄이기
data_xx= data.drop(columns = ['chlorides','fixed acidity','citric acid','quality','residual sugar','pH','free sulfur dioxide'], axis='columns')
data_yy = data['quality']

xx_train, xx_test, yy_train, yy_test = train_test_split(data_xx, data_yy, test_size=0.2, random_state=1)
rfmodel2 = RandomForestClassifier().fit(xx_train, yy_train)
rfpredict2 = rfmodel2.predict(xx_test)
print('RandomForestClassifier acc : {0:.5f}'.format(accuracy_score(yy_test, rfpredict2)))

# 이상치를 제거
def remove_outlier(input_data):
    q1 = input_data.quantile(0.25) # 제 1사분위수
    q3 = input_data.quantile(0.75) # 제 3사분위수
    iqr = q3 - q1 # IQR(Interquartile range) 계산
    minimum = q1 - (iqr * 1.5) # IQR 최솟값
    maximum = q3 + (iqr * 1.5) # IQR 최댓값
    # IQR 범위 내에 있는 데이터만 산출(IQR 범위 밖의 데이터는 이상치)
    df_removed_outlier = input_data[(minimum < input_data) & (input_data < maximum)]
    return df_removed_outlier

# NA 평균 대체
data2 = remove_outlier(data)
print(data2.isnull().sum())
data2['fixed acidity'].fillna(data2['fixed acidity'].mean(), inplace = True)
data2['volatile acidity'].fillna(data2['volatile acidity'].mean(), inplace = True)
data2['residual sugar'].fillna(data2['residual sugar'].mean(), inplace = True)
data2['chlorides'].fillna(data2['chlorides'].mean(), inplace = True)
data2['free sulfur dioxide'].fillna(data2['free sulfur dioxide'].mean(), inplace = True)
data2['total sulfur dioxide'].fillna(data2['total sulfur dioxide'].mean(), inplace = True)
data2['density'].fillna(data2['density'].mean(), inplace = True)
data2['pH'].fillna(data2['pH'].mean(), inplace = True)
data2['sulphates'].fillna(data2['sulphates'].mean(), inplace = True)
data2['alcohol'].fillna(data2['alcohol'].mean(), inplace = True)
data2['quality'].fillna(data2['quality'].mean(), inplace = True)
print(data2.isnull().sum())

data2_x = data.drop(columns = ['quality'], axis='columns')
data2_y = data['quality']

x2_train, x2_test, y2_train, y2_test = train_test_split(data2_x, data2_y, test_size=0.2, random_state=1)

rfmodel3 = RandomForestClassifier().fit(x2_train, y2_train)
rfpredict3 = rfmodel3.predict(x2_test)
print('RandomForestClassifier acc : {0:.5f}'.format(accuracy_score(y2_test, rfpredict3)))

# 변수 5개
data2_xx= data.drop(columns = ['chlorides','fixed acidity','citric acid','quality','residual sugar','pH','free sulfur dioxide'], axis='columns')
data2_yy = data['quality']

xx2_train, xx2_test, yy2_train, yy2_test = train_test_split(data2_xx, data2_yy, test_size=0.2, random_state=1)
rfmodel4 = RandomForestClassifier().fit(xx2_train, yy2_train)
rfpredict4 = rfmodel4.predict(xx_test)
print('RandomForestClassifier acc : {0:.5f}'.format(accuracy_score(yy2_test, rfpredict4)))
