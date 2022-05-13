import pandas as pd
from sklearn import svm, metrics

data = pd.read_csv('../testdata/Heart.csv')
data['Ca'] = data['Ca'].fillna(0)
print(data.columns)

label = data['AHD']
feature = data.drop(columns = ['Unnamed: 0','AHD','ChestPain','Thal'])
print(feature)
print(label)

from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(feature, label, random_state=1, test_size=0.2)

model = svm.SVC(C=1).fit(train_x, train_y)
pred = model.predict(test_x)

print('실제값:', list(test_y[:10]))
print('예측값:', pred[:10])
print('정확도:',metrics.accuracy_score(test_y,pred))