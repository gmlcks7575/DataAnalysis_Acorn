# MLP : 다층신경망 - 선형 / 비선형 분류가 가능
import numpy as np
from sklearn.neural_network import MLPClassifier 
from sklearn.metrics import accuracy_score

feature = np.array([[0,0],[0,1],[1,0],[1,1]])
print(feature)
#label = np.array([0,0,0,1]) # and
#label = np.array([0,1,1,1]) # or
label = np.array([0,1,1,0]) # xor 0.5

# ml = MLPClassifier(hidden_layer_sizes=30, activation = 'relu',
#                     solver='adam', learning_rate_init = 0.01).fit(feature, label)
ml = MLPClassifier(hidden_layer_sizes=(10,10,10), activation = 'relu',
                    solver='adam', learning_rate_init = 0.01).fit(feature, label)                    

print(ml)

pred = ml.predict(feature)
print('pred:',pred)
print('acc:',accuracy_score(label,pred))