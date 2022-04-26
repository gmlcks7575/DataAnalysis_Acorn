# 웹용 파이썬 모듈
ss1 = '자료 1'
ss2 = 'data 2'

print('Content-Type:text/html; charset=utf-8\n')
print('''
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h2>반가워요</h2>
자료 출력 : {0} {1}
<p/>
<img src='../images/googlelogo_color_272x92dp.png' width='60%' />
<br>
<a href='../main.html'>메인으로</a>
</body>
    '''.format(ss1, ss2))