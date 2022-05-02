# 상관관계 문제)
# https://github.com/pykwon/python 에 있는 Advertising.csv 파일을 읽어 tv,radio,newspaper 간의 상관관계를 파악하시오. 
# 그리고 이들의 관계를 heatmap 그래프로 표현하시오. 
import pandas as pd
data = pd.read_csv("../testdata/advertising.csv")
datas = pd.DataFrame(data, columns=('tv','radio','newspaper'))
print(datas.corr())

import seaborn as sns
import matplotlib.pyplot as plt
sns.heatmap(datas.corr())
plt.show()