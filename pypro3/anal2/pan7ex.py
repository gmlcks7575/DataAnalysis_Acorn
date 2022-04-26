#pandas 문제 3)  타이타닉 승객 데이터를 사용하여 아래의 물음에 답하시오
import pandas as pd
df3=pd.read_csv('testdata/titanic_data.csv', header=None)
#1) 데이터프레임의 자료로 나이대(소년, 청년, 장년, 노년)에 대한 생존자수를 계산한다.
bins = [1,20,35,60,150]
labels = ["소년", "청년", "장년", "노년"]
df3.Age = pd.cut(df3.Age, bins, labels = labels)
print(df3.Age)
print(df3.Age.value_counts())
