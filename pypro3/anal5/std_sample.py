# 표준편차, 분산의 중요성 : 데이터의 분포 파악

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

np.random.seed(1)
print(stats.norm(loc = 1, scale = 2).rvs(10)) #랜덤표본 얻기

print('------')
centers = [1,1.5,2]
col = 'rgb'

std = 0.05 #표준편차
datas = []

for i in range(3):
    datas.append(stats.norm(loc = centers[i], scale = std).rvs(100)) 
    plt.plot(np.arange(100) + i * 100, datas[i], '*', color = col[i])
    
plt.show()