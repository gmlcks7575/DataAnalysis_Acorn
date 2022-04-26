import pandas as pd 
import numpy as np

#pandas 문제 1)
#a) 표준정규분포를 따르는 9 X 4 형태의 DataFrame을 생성하시오. 
datas = pd.DataFrame(np.random.randn(9,4))
print(datas)
#b) a에서 생성한 DataFrame의 칼럼 이름을 - No1, No2, No3, No4로 지정하시오
datas.columns=['No1','No2','No3','No4']
print(datas)
#c) 각 컬럼의 평균을 구하시오. mean() 함수와 axis 속성 사용
print(datas.mean(axis=0))

#pandas 문제 2)
#a) DataFrame으로 위와 같은 자료를 만드시오. colume(열) name은 numbers, row(행) name은 a~d이고 값은 10~40.
df = pd.DataFrame([[i] for i in range(10,41,10)], columns=['numbers'], index = ['a','b','c','d'])
print(df)
#b) c row의 값을 가져오시오.
print(df.loc['c'])
#c) a, d row들의 값을 가져오시오.
print(df.loc[['a','d']])
#d) numbers의 합을 구하시오.
print(df.sum(axis=0))
#e) numbers의 값들을 각각 제곱하시오. 아래 결과가 나와야 함.
print(df **2)
#f) floats 라는 이름의 칼럼을 추가하시오. 값은 1.5, 2.5, 3.5, 4.5    아래 결과가 나와야 함.
df['floats']=[1.5,2.5,3.5,4.5]
print(df)
#g) names라는 이름의 다음과 같은 칼럼을 위의 결과에 또 추가하시오. Series 클래스 사용.
df['names'] = pd.Series(['길동','오징','팔계','오공'], index=['d','a','b','c'])
print(df)