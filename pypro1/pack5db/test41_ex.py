#사번과 이름을 입력하여 로그인에 성공하면 (buser,jikwon :join)
#사원, 직원명, 부서명, 부서전화, 연봉, 성별 출력
#1. 홍길동, 영업부,123-1234,12345,남
import MySQLdb
import pickle
with open('mydb.dat','rb') as obj:
    config = pickle.load(obj)

def login():
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        jikwon_no = input('사번을 입력하세요:')
        jikwon_name = input('이름을 입력하세요: ')
        
        sql=""" select j.jikwon_no, j.jikwon_name, b.buser_name, b.buser_tel, j.jikwon_pay, j.jikwon_gen
            from jikwon j, buser b
            where j.buser_num=b.buser_no and j.jikwon_no = {0} &&  j.jikwon_name= '{1}'
        """.format(jikwon_no, jikwon_name)
        
        cursor.execute(sql)
        datas = cursor.fetchall()
        
        if len(datas)==0:
            print('사번과 이름이 틀렸습니다')
            return 
        
        for jikwon_no, jikwon_name, buser_name, buser_tel, jikwon_pay, jikwon_gen in datas:
            print(jikwon_no, jikwon_name, buser_name, buser_tel, jikwon_pay, jikwon_gen)

    except Exception as e:
        print('err:',e)
    finally:
            cursor.close()
            conn.close() 
            
if __name__ == '__main__':
    login()   