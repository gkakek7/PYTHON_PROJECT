import pymysql

conn = pymysql.connect(host='localhost', user='root',port=3305, password='python', db='python', charset='utf8')
 
curs = conn.cursor()
e_id = 6
e_name = "7"
gen = "7"
addr = "7"

sql = f""" 
    delete from emp
    where e_id = '{e_id}'
"""
#""" 넣으면 띄어쓰기 허용됨
cnt = curs.execute(sql)
print(cnt) #이것도 가능함
print(curs.rowcount,"개의 레코드가 입력됨")
conn.commit()
curs.close()
conn.close()