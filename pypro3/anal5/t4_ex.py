# [two-sample t 검정 : 문제3]
# DB에 저장된 jikwon 테이블에서 총무부, 영업부 직원의 연봉의 평균에 차이가 존재하는지 검정하시오.
# 연봉이 없는 직원은 해당 부서의 평균연봉으로 채워준다.
import MySQLdb
import pickle
import numpy as np
import pandas as pd
import scipy.stats as stats

try:
    with open('mydb.dat', mode = 'rb') as obj:
        config = pickle.load(obj)
except Exception as e:
    print('연결 오류:', e)

try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = """
        select buser_name, jikwon_pay
        from jikwon inner join buser
        on buser_num = buser_no
    """
    cursor.execute(sql)
    df = pd.DataFrame(cursor.fetchall(), columns=['buser_name', 'jikwon_pay'])   
    data1 = df[df['buser_name']=='총무부']
    data1 = data1['jikwon_pay']
    data2 = df[df['buser_name']=='영업부']
    data2 = data2['jikwon_pay']
    data1avg = np.mean(data1) #5414.2857
    data2avg = np.mean(data2) #4908.3333
    print(data1avg)
    print(data2avg)

    # 정규성 확인
    print(stats.shapiro(data1).pvalue) #0.0260448 < 0.05 정규성 만족X
    print(stats.shapiro(data2).pvalue) #0.0256084 < 0.05 정규성 만족X
    print(len(data1))
    print(len(data2))

    # 등분산성 확인
    print(stats.levene(data1, data2).pvalue) # 0.915044305043978 > 0.05 등분산성 만족
    
    print(stats.mannwhitneyu(data1, data2)) # pvalue=0.472133 > 0.05 귀무 채택, 연봉의 평균의 차이가 존재한다.
       
except Exception as e:
    print('연결 오류:', e)

# [대응표본 t 검정 : 문제4]
# 어느 학급의 교사는 매년 학기 내 치뤄지는 시험성적의 결과가 실력의 차이없이 비슷하게 유지되고 있다고 말하고 있다. 이 때, 올해의 해당 학급의 중간고사 성적과 기말고사 성적은 다음과 같다. 점수는 학생 번호 순으로 배열되어 있다.
#    중간 : 80, 75, 85, 50, 60, 75, 45, 70, 90, 95, 85, 80
#    기말 : 90, 70, 90, 65, 80, 85, 65, 75, 80, 90, 95, 95
# 그렇다면 이 학급의 학업능력이 변화했다고 이야기 할 수 있는가?

mid = [80, 75, 85, 50, 60, 75, 45, 70, 90, 95, 85, 80]
fin = [90, 70, 90, 65, 80, 85, 65, 75, 80, 90, 95, 95]

print(np.mean(mid))
print(np.mean(fin)) # 74.16 vs 81.66

print(stats.ttest_rel(mid, fin))
# Ttest_relResult(statistic=-2.6281127723493993, pvalue=0.023486192540203194)
# pvalue=0.0234 < 0.05 귀무 기각. 시험성적의 결과가 차이난다.