# 카이제곱 문제1) 부모학력 수준이 자녀의 진학여부와 관련이 있는가?를 가설검정하시오
# 예제파일 : cleanDescriptive.csv
# 칼럼 중 level - 부모의 학력수준, pass - 자녀의 대학 진학여부
# 조건 :  level, pass에 대해 NA가 있는 행은 제외한다.
import  pandas as pd
import scipy.stats as stats

# 귀무 : 부모학력 수준이 자녀의 진학여부와 관련이 없다
# 대립 : 부모학력 수준이 자녀의 진학여부와 관련이 있다
data = pd.read_csv("../testdata/cleanDescriptive.csv")
ctab = pd.crosstab(index = data['level'], columns = data['pass'], dropna = True)
print(ctab)
chi2, p, ddof, _ = stats.chi2_contingency(ctab)
print('chi2:{}, p:{}, ddof:{}'.format(chi2, p, ddof))
# p:0.25070568406521354 > 0.05 이므로 귀무가설 채택한다.
# 부모학력 수준이 잔녀의 진학여부와 관련이 없다.

# 카이제곱 문제2) 지금껏 A회사의 직급과 연봉은 관련이 없다. 
# 그렇다면 정말로 jikwon_jik과 jikwon_pay 간의 관련성이 없는지 분석. 가설검정하시오.
# 예제파일 : MariaDB의 jikwon table 
# jikwon_jik   (이사:1, 부장:2, 과장:3, 대리:4, 사원:5)
# jikwon_pay (1000 ~2999 :1, 3000 ~4999 :2, 5000 ~6999 :3, 7000 ~ :4)
# 조건 : NA가 있는 행은 제외한다.

# 귀무 : A회사의 직급과 연봉은 관련이 없다.
# 대립 : A회사의 직급과 연봉은 관련이 있다.
import MySQLdb
import pickle
import numpy as np

try:
    with open('mydb.dat', mode = 'rb') as obj:
        config = pickle.load(obj)
except Exception as e:
    print('연결 오류:', e)

try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = """
        select jikwon_jik, jikwon_pay
        from jikwon
    """
    cursor.execute(sql)
    df = pd.DataFrame(cursor.fetchall(), columns=['jikwon_jik', 'jikwon_pay'])   
    jikwon_pay2=[]
    jikwon_jik2=[]
    print(df)
    for j in range(30):
        if df['jikwon_jik'][j] == '이사':
            jikwon_jik2.append('1')
        elif df['jikwon_jik'][j] == '부장':
            jikwon_jik2.append('2')
        elif df['jikwon_jik'][j] == '과장':
            jikwon_jik2.append('3')
        elif df['jikwon_jik'][j] == '대리':
            jikwon_jik2.append('4')
        elif df['jikwon_jik'][j] == '사원':
            jikwon_jik2.append('5')
            
    for i in range(30):
        if df['jikwon_pay'][i] < 3000:
            jikwon_pay2.append('1')
        elif 3000 <= df['jikwon_pay'][i] < 5000:
            jikwon_pay2.append('2')
        elif 5000 <= df['jikwon_pay'][i] < 7000:
            jikwon_pay2.append('3')
        elif 7000 <= df['jikwon_pay'][i] < 9999:
            jikwon_pay2.append('4')
    df['jikwon_pay2'] = jikwon_pay2
    df['jikwon_jik2'] = jikwon_jik2
    ctab = pd.crosstab(index = df['jikwon_pay2'], columns = df['jikwon_jik2'], dropna=True)
    ctab.columns = ['이사','부장','과장','대리','사원']
    print(ctab)
    
    chi2, p, ddof, _ = stats.chi2_contingency(ctab)
    print('chi2:{}, p:{}, ddof:{}'.format(chi2, p, ddof))

except Exception as e:
    print('연결 오류:', e)
# p:0.00019211533885350577 < 0.05 이므로 귀무가설 기각. 대립가설 채택
# A회사의 직급과 연봉은 관련이 있다.
