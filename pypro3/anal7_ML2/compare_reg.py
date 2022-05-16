# sklearn이 지원하는 예측모델(연속형)

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import r2_score

adver = pd.read_csv('../testdata/Advertising.csv', usecols=[1,2,3,4])
print(adver.head(5))

x = np.array(adver.loc[:, 'tv':'newspaper'])
print(x[:2])
y = np.array(adver.sales)
print(y[:2])

print()
lmodel = LinearRegression().fit(x, y)
lpred = lmodel.predict(x)
print('LinearRegression pred:', lpred[:5])
print('r2_score:', r2_score(y, lpred)) #0.8972

print()
kmodel = KNeighborsRegressor(n_neighbors=3).fit(x, y)
kpred = kmodel.predict(x)
print('KNeighborsRegressor pred:', kpred[:5])
print('r2_score:', r2_score(y, kpred)) #0.9680

print() # n_estimators = 100개의 decisiontree, mean square error
rmodel = RandomForestRegressor(n_estimators = 100, criterion='mse').fit(x, y)
rpred = rmodel.predict(x)
print('RandomForestRegressor pred:', rpred[:5])
print('r2_score:', r2_score(y, rpred)) #0.9974

print() 
xmodel = XGBRegressor().fit(x, y)
xpred = xmodel.predict(x)
print('XGBRegressor pred:', xpred[:5])
print('r2_score:', r2_score(y, xpred)) #0.9999
