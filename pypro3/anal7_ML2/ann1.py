# 인공신경망 : 단층 신경망 (뉴런 또는 노드 1개) - Perceptron
# input data * 가중치의 합에 대해 임계 값(활성화함수)을 이항분류가 가능

import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score

feature = np.array([[0,0],[0,1],[1,0],[1,1]])
print(feature)
#label = np.array([0,0,0,1]) # and
label = np.array([0,1,1,1]) # or
#label = np.array([0,1,1,0]) # xor : 하나의 node로는 불가능하다. acc가 0.5밖에안나온다

ml = Perceptron(max_iter=100, eta0=0.1).fit(feature,label) 
# max_iter => epoch 수 (학습 수) # eta0 는 학습률(learning late)
print(ml)
pred = ml.predict(feature)
print('pred:',pred)
print('acc:',accuracy_score(label,pred))