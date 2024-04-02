import pymysql

conn = pymysql.connect(host='localhost', user='root',port=3305, password='python', db='python', charset='utf8')
 
curs = conn.cursor(pymysql.cursors.DictCursor)

sql = 'select * from emp'

curs.execute(sql)

table = curs.fetchall()

print(table)

conn.commit

for a in table:
    print(a)

curs.close()
conn.close()