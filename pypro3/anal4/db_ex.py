import MySQLdb
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv

plt.rc('font', family='malgun gothic')

try:
    with open('mydb.dat', mode = 'rb') as obj:
        config = pickle.load(obj)
except Exception as e:
    print('연결오류:',e)
#사번 이름 부서명 연봉, 직급을 읽어 DataFrame을 작성    
try:
    conn = MySQLdb.connect(**config)
    cursor=conn.cursor()
    sql = """
        select jikwon_no, jikwon_name, buser_name, jikwon_pay, jikwon_jik
        from jikwon inner join buser
        on buser_num = buser_no
    """
    cursor.execute(sql)
    df1 = pd.DataFrame(cursor.fetchall(), columns=['jikwon_no', 'jikwon_name', 'buser_name', 'jikwon_pay', 'jikwon_jik'])
    print(df1)
#DataFrame의 자료를 파일로 저장    
    with open('jik_data2.csv', mode='w', encoding="UTF-8") as fobj:
        writer = csv.writer(fobj)
        for r in cursor:
            writer.writerow(r)
#부서명별 연봉의 합, 연봉의 최대/최소값을 출력
    print('부서별 연봉의 합:',df1.groupby(['buser_name'])['jikwon_pay'].sum())
    print('부서별 연봉의 최대',df1.groupby(['buser_name'])['jikwon_pay'].max())
    print('부서별 연봉의 최소',df1.groupby(['buser_name'])['jikwon_pay'].min())        
#부서명, 직급으로 교차테이블을 작성(crosstab)
    ctab = pd.crosstab(df1['buser_name'],df1['jikwon_jik'], margins=True)
    print(ctab)
#직원별 담당 고객자료(고객번호, 고객명, 고객전화)를 출력. 담당 고객이 없으면 "담당 고객  X"으로 표시
    sql2 = """
        select jikwon_name, gogek_no, gogek_name, gogek_tel
        from gogek right outer join jikwon
        on gogek_damsano = jikwon_no
        order by jikwon_name asc
    """
    cursor.execute(sql2)
    df2 = pd.DataFrame(cursor.fetchall(), columns=['jikwon_name','gogek_no', 'gogek_name', 'gogek_tel'])
    df3 = df2.fillna('담당 고객 X')
    print(df3)
#부서명별 연봉의 평균으로 가로 막대 그래프를 작성
    
except Exception as e:
    print('처리오류:',e)
    